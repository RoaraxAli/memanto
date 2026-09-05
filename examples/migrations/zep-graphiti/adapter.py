"""
Zep / Graphiti to Memanto & OKF v0.2 Migration Adapter.
Transforms temporal knowledge graphs (episodes, entities, edges) into Memanto typed memories and valid OKF bundles.
"""

from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Any
import yaml


def _slugify(text: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", text.lower().strip())
    return re.sub(r"[-\s]+", "-", cleaned)[:60] or "concept"


def load_graphiti(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object root, got {type(data).__name__}")
    return data


def graphiti_to_memanto(graphiti_data: dict[str, Any]) -> list[dict[str, Any]]:
    """Maps Graphiti nodes, edges, and episodes to Memanto batch-remember rows."""
    from memanto.cli.migrate.mappers import map_graphiti
    return map_graphiti(graphiti_data)


def export_to_okf_bundle(graphiti_data: dict[str, Any], output_dir: str | Path) -> Path:
    """Exports Graphiti temporal knowledge graph into a valid OKF v0.2 bundle."""
    bundle_root = Path(output_dir)
    memories_dir = bundle_root / "memories"
    bundle_root.mkdir(parents=True, exist_ok=True)

    node_map = {n.get("uuid") or n.get("id"): n for n in (graphiti_data.get("nodes") or [])}
    index_entries = []

    # 1. Export Entity Nodes
    facts_dir = memories_dir / "facts"
    facts_dir.mkdir(parents=True, exist_ok=True)
    for node in graphiti_data.get("nodes") or []:
        name = node.get("name", "Unknown Entity")
        summary = node.get("summary", "")
        slug = _slugify(name)
        file_path = facts_dir / f"{slug}.md"
        labels = [str(l).lower() for l in (node.get("labels") or [])]
        created_at = node.get("created_at") or datetime.now(timezone.utc).isoformat()

        frontmatter = {
            "type": "Entity Fact",
            "title": name,
            "description": summary[:120] if summary else name,
            "tags": ["graphiti", "entity", *labels],
            "generated": {"by": "zep-graphiti/adapter", "at": created_at},
            "x_memanto": {
                "type": "fact",
                "source": "graphiti",
                "confidence": 0.9,
                "provenance": "imported",
                "source_ref": node.get("uuid") or node.get("id"),
            },
        }
        body = f"# {name}\n\n{summary}\n\n## Metadata\n- **Labels**: {', '.join(labels)}\n- **Node UUID**: `{node.get('uuid') or node.get('id')}`\n"
        content = f"---\n{yaml.safe_dump(frontmatter, sort_keys=False)}---\n\n{body}"
        file_path.write_text(content, encoding="utf-8")
        index_entries.append({"title": name, "type": "Entity Fact", "rel_path": f"memories/facts/{slug}.md", "desc": summary[:90]})

    # 2. Export Temporal Edges (Relationships, Decisions, Preferences)
    rel_dir = memories_dir / "relationships"
    dec_dir = memories_dir / "decisions"
    pref_dir = memories_dir / "preferences"
    for d in (rel_dir, dec_dir, pref_dir):
        d.mkdir(parents=True, exist_ok=True)

    for edge in graphiti_data.get("edges") or []:
        fact = edge.get("fact", "")
        relation = edge.get("name") or edge.get("relation") or "RELATION"
        src_node = node_map.get(edge.get("source_node_uuid") or edge.get("source"), {})
        tgt_node = node_map.get(edge.get("target_node_uuid") or edge.get("target"), {})
        src_name = src_node.get("name", edge.get("source"))
        tgt_name = tgt_node.get("name", edge.get("target"))

        rel_lower = relation.lower()
        if "prefer" in rel_lower:
            target_dir = pref_dir
            folder = "preferences"
            concept_type = "Preference"
            m_type = "preference"
        elif "decid" in rel_lower:
            target_dir = dec_dir
            folder = "decisions"
            concept_type = "Architecture Decision"
            m_type = "decision"
        else:
            target_dir = rel_dir
            folder = "relationships"
            concept_type = "Relationship"
            m_type = "relationship"

        slug = _slugify(f"{relation}-{src_name}-{tgt_name}")
        file_path = target_dir / f"{slug}.md"
        valid_at = edge.get("valid_at")
        invalid_at = edge.get("invalid_at")
        status = "Invalidated / Deprecated" if invalid_at else "Active / Current"

        frontmatter = {
            "type": concept_type,
            "title": f"{relation}: {src_name} -> {tgt_name}",
            "description": fact[:120] if fact else f"{src_name} {relation} {tgt_name}",
            "tags": ["graphiti", "temporal-edge", rel_lower],
            "generated": {"by": "zep-graphiti/adapter", "at": valid_at or datetime.now(timezone.utc).isoformat()},
            "x_memanto": {
                "type": m_type,
                "source": "graphiti",
                "confidence": float(edge.get("weight") or 0.85),
                "created_at": valid_at,
                "expires_at": invalid_at,
                "provenance": "imported",
                "source_ref": edge.get("uuid") or edge.get("id"),
            },
        }

        src_slug = _slugify(str(src_name))
        tgt_slug = _slugify(str(tgt_name))
        body = (
            f"# {concept_type}: {relation}\n\n"
            f"> **Temporal Status**: {status}\n\n"
            f"### Statement\n{fact}\n\n"
            f"### Lineage & Traversal\n"
            f"- **From**: [{src_name}](../facts/{src_slug}.md)\n"
            f"- **To**: [{tgt_name}](../facts/{tgt_slug}.md)\n"
            f"- **Valid Interval**: `{valid_at or 'genesis'}` -> `{invalid_at or 'indefinite'}`\n"
            f"- **Source Episodes**: {', '.join(edge.get('episodes') or [])}\n"
        )
        content = f"---\n{yaml.safe_dump(frontmatter, sort_keys=False)}---\n\n{body}"
        file_path.write_text(content, encoding="utf-8")
        index_entries.append({"title": f"{relation} ({src_name} -> {tgt_name})", "type": concept_type, "rel_path": f"memories/{folder}/{slug}.md", "desc": fact[:90]})

    # 3. Export Episodes as Events
    events_dir = memories_dir / "events"
    events_dir.mkdir(parents=True, exist_ok=True)
    for ep in graphiti_data.get("episodes") or []:
        name = ep.get("name") or f"Episode {ep.get('uuid') or ep.get('id')}"
        slug = _slugify(name)
        file_path = events_dir / f"{slug}.md"
        created_at = ep.get("created_at") or datetime.now(timezone.utc).isoformat()
        ep_content = ep.get("content", "")

        frontmatter = {
            "type": "Session Event",
            "title": name,
            "description": ep_content[:120],
            "tags": ["graphiti", "episode", "timeline"],
            "generated": {"by": "zep-graphiti/adapter", "at": created_at},
            "x_memanto": {
                "type": "event",
                "source": "graphiti",
                "confidence": 0.8,
                "created_at": created_at,
                "provenance": "imported",
                "source_ref": ep.get("uuid") or ep.get("id"),
            },
        }
        body = f"# {name}\n\n{ep_content}\n\n## Session Provenance\n- **Logged At**: `{created_at}`\n- **Channel/Source**: `{ep.get('source', 'internal')}`\n"
        content = f"---\n{yaml.safe_dump(frontmatter, sort_keys=False)}---\n\n{body}"
        file_path.write_text(content, encoding="utf-8")
        index_entries.append({"title": name, "type": "Session Event", "rel_path": f"memories/events/{slug}.md", "desc": ep_content[:90]})

    # 4. Generate Root index.md (progressive disclosure directory catalog)
    index_md = [
        "# Open Knowledge Format (OKF) Bundle",
        "",
        "Migrated from **Zep / Graphiti Temporal Knowledge Graph** to vendor-neutral portable markdown.",
        f"- **Exported At**: `{datetime.now(timezone.utc).isoformat()}`",
        f"- **Total Concepts**: {len(index_entries)}",
        "- **Specification**: [OKF v0.2 (Google Cloud)](https://github.com/GoogleCloudPlatform/open-knowledge-format)",
        "",
        "## Knowledge Index",
        "| Concept | Type | Path | Summary |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for item in sorted(index_entries, key=lambda x: (x["type"], x["title"])):
        index_md.append(f"| {item['title']} | `{item['type']}` | [{item['title']}]({item['rel_path']}) | {item['desc']}... |")

    (bundle_root / "index.md").write_text("\n".join(index_md) + "\n", encoding="utf-8")
    return bundle_root


def main() -> None:
    parser = argparse.ArgumentParser(description="Zep / Graphiti to Memanto & OKF v0.2 Migration Adapter")
    parser.add_argument("-i", "--input", required=True, help="Path to Graphiti export JSON")
    parser.add_argument("-o", "--output-okf", help="Output directory for generated OKF v0.2 bundle")
    parser.add_argument("-j", "--export-json", help="Output path for Memanto batch import JSON")
    args = parser.parse_args()

    data = load_graphiti(args.input)
    print(f"Loaded Graphiti graph: {len(data.get('nodes', []))} nodes, {len(data.get('edges', []))} edges, {len(data.get('episodes', []))} episodes")

    if args.export_json:
        rows = graphiti_to_memanto(data)
        Path(args.export_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.export_json).write_text(json.dumps({"memories": rows}, indent=2, default=str), encoding="utf-8")
        print(f"Mapped {len(rows)} memories to: {args.export_json}")

    if args.output_okf:
        bundle_path = export_to_okf_bundle(data, args.output_okf)
        print(f"Exported valid OKF v0.2 bundle to: {bundle_path}")


if __name__ == "__main__":
    main()
