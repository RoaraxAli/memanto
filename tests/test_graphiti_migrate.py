"""
Tests for Zep/Graphiti temporal knowledge graph migration to Memanto & OKF v0.2.
"""

from pathlib import Path
import sys
import pytest

example_dir = Path(__file__).resolve().parents[1] / "examples" / "migrations" / "zep-graphiti"
if str(example_dir) not in sys.path:
    sys.path.insert(0, str(example_dir))

from adapter import export_to_okf_bundle
from generate_dataset import generate_architect_dataset
from memanto.cli.migrate.mappers import map_graphiti
from memanto.cli.migrate.okf_loader import load_okf_bundle
from memanto.cli.migrate.runner import source_count


@pytest.fixture
def sample_graphiti_data():
    return generate_architect_dataset()


def test_map_graphiti_basic(sample_graphiti_data):
    rows = map_graphiti(sample_graphiti_data)
    # 8 nodes + 9 edges + 4 episodes = 21 memories
    assert len(rows) == 21

    # Check sources and provenance
    assert all(r["source"] == "graphiti" for r in rows)
    assert all(r["provenance"] == "imported" for r in rows)


def test_map_graphiti_temporal_invalidation(sample_graphiti_data):
    rows = map_graphiti(sample_graphiti_data)

    # Edge 1 (USED_DATABASE: Hyperion -> Postgres) was invalidated on 2026-04-15
    invalidated_edge = next(r for r in rows if r["source_ref"] == "edge-01")
    assert invalidated_edge["expires_at"] is not None
    assert invalidated_edge["expires_at"].year == 2026

    # Edge 2 (MIGRATED_TO_DATABASE: Hyperion -> CockroachDB) is currently active
    active_edge = next(r for r in rows if r["source_ref"] == "edge-02")
    assert active_edge["expires_at"] is None


def test_map_graphiti_types(sample_graphiti_data):
    rows = map_graphiti(sample_graphiti_data)

    # Check decision mapping
    decisions = [r for r in rows if r["type"] == "decision"]
    assert len(decisions) >= 1
    assert any("grpc" in r["content"].lower() for r in decisions)

    # Check preference mapping
    preferences = [r for r in rows if r["type"] == "preference"]
    assert len(preferences) >= 2
    assert any("mtls" in r["content"].lower() for r in preferences)

    # Check event mapping
    events = [r for r in rows if r["type"] == "event"]
    assert len(events) == 4


def test_graphiti_source_count(sample_graphiti_data):
    count = source_count("graphiti", sample_graphiti_data)
    assert count == 21


def test_export_to_okf_bundle_and_reload(tmp_path, sample_graphiti_data):
    bundle_dir = tmp_path / "test_okf_bundle"
    export_to_okf_bundle(sample_graphiti_data, bundle_dir)

    assert (bundle_dir / "index.md").exists()
    assert (bundle_dir / "memories" / "facts").exists()
    assert (bundle_dir / "memories" / "relationships").exists()
    assert (bundle_dir / "memories" / "decisions").exists()
    assert (bundle_dir / "memories" / "events").exists()

    # Load bundle back via Memanto's OKF loader
    loaded = load_okf_bundle(bundle_dir)
    assert "memories" in loaded
    assert len(loaded["memories"]) >= 21
