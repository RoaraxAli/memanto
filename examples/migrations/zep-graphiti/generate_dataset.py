"""
Generates a realistic, lived-in Graphiti temporal knowledge graph for a software architect agent.
Tracks evolving architectural decisions, tech stack changes, and temporal invalidations over 3 weeks.
"""

from datetime import datetime, timezone
import json
from pathlib import Path


def generate_architect_dataset(output_path: str | Path | None = None) -> dict:
    data = {
        "metadata": {
            "source": "zep-graphiti",
            "version": "0.3.1",
            "agent_id": "architect-agent-hyperion",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "description": "Lived-in memory of Project Hyperion tech lead over 4 episodes across 3 weeks.",
        },
        "episodes": [
            {
                "uuid": "ep-101",
                "name": "Episode 1: Initial Architecture Kickoff",
                "content": "Kickoff meeting for Project Hyperion. We decided to build a monolithic REST API using PostgreSQL for persistence and Redis for session and response caching.",
                "created_at": "2026-04-01T09:30:00Z",
                "source": "slack_sync",
            },
            {
                "uuid": "ep-102",
                "name": "Episode 2: Protocol Scaling & Cache Race Issues",
                "content": "P99 latency spiked past 600ms on REST endpoints under peak load. We approved ADR-014: migrating all inter-service communications to gRPC with protobuf schemas. Furthermore, Redis cache showed split-brain race conditions under cluster failover; decided to deprecate Redis in favor of an In-Memory Raft-synchronized cache layer.",
                "created_at": "2026-04-08T14:15:00Z",
                "source": "meeting_transcript",
            },
            {
                "uuid": "ep-103",
                "name": "Episode 3: Multi-Region Compliance & Active-Active DB",
                "content": "EU GDPR and latency requirements mandate multi-region active-active writes. PostgreSQL single-primary topology cannot satisfy this SLA. We officially invalidated the PostgreSQL architecture and migrated the primary transactional datastore to CockroachDB. Established strict team preference: all new microservices must enforce mutual TLS (mTLS).",
                "created_at": "2026-04-15T11:00:00Z",
                "source": "architecture_review",
            },
            {
                "uuid": "ep-104",
                "name": "Episode 4: Production Launch Readiness",
                "content": "Final pre-production sprint. Commitment made: complete comprehensive chaos engineering and load testing by Friday at 5 PM. Verified that gRPC endpoints achieve p95 latency of 38ms. The team prefers Prometheus and Grafana for all observability dashboards.",
                "created_at": "2026-04-22T16:45:00Z",
                "source": "standup_notes",
            },
        ],
        "nodes": [
            {
                "uuid": "node-1",
                "name": "CockroachDB",
                "summary": "Distributed SQL database providing serializable ACID transactions and multi-region active-active replication.",
                "labels": ["Technology", "Database", "DistributedSystem"],
                "created_at": "2026-04-15T11:00:00Z",
            },
            {
                "uuid": "node-2",
                "name": "PostgreSQL",
                "summary": "Legacy single-primary relational database used during prototype and initial alpha stages.",
                "labels": ["Technology", "Database", "Legacy"],
                "created_at": "2026-04-01T09:30:00Z",
            },
            {
                "uuid": "node-3",
                "name": "gRPC Service Mesh",
                "summary": "High-performance RPC framework using HTTP/2 transport and Protocol Buffers for typed internal contracts.",
                "labels": ["Technology", "Networking", "Protocol"],
                "created_at": "2026-04-08T14:15:00Z",
            },
            {
                "uuid": "node-4",
                "name": "REST Gateway",
                "summary": "External HTTP/JSON edge gateway handling third-party client ingress.",
                "labels": ["Technology", "Gateway", "API"],
                "created_at": "2026-04-01T09:30:00Z",
            },
            {
                "uuid": "node-5",
                "name": "In-Memory Raft Cache",
                "summary": "Consistent distributed in-memory cache synchronized via Raft consensus, replacing Redis.",
                "labels": ["Technology", "Cache", "DistributedSystem"],
                "created_at": "2026-04-08T14:15:00Z",
            },
            {
                "uuid": "node-6",
                "name": "Redis Cache",
                "summary": "Deprecated caching layer removed due to cluster failover split-brain synchronization anomalies.",
                "labels": ["Technology", "Cache", "Deprecated"],
                "created_at": "2026-04-01T09:30:00Z",
            },
            {
                "uuid": "node-7",
                "name": "Project Hyperion",
                "summary": "Next-generation distributed agent orchestration and processing platform.",
                "labels": ["Project", "CorePlatform"],
                "created_at": "2026-04-01T09:00:00Z",
            },
            {
                "uuid": "node-8",
                "name": "Security & Auth Service",
                "summary": "Zero-trust internal identity service managing mTLS certificates and SPIFFE identities.",
                "labels": ["Security", "Infrastructure"],
                "created_at": "2026-04-15T11:00:00Z",
            },
        ],
        "edges": [
            {
                "uuid": "edge-01",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-2",
                "name": "USED_DATABASE",
                "fact": "Project Hyperion initially used PostgreSQL as its primary transactional store.",
                "valid_at": "2026-04-01T09:30:00Z",
                "invalid_at": "2026-04-15T11:00:00Z",
                "weight": 0.95,
                "episodes": ["ep-101", "ep-103"],
            },
            {
                "uuid": "edge-02",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-1",
                "name": "MIGRATED_TO_DATABASE",
                "fact": "Project Hyperion migrated primary persistence to CockroachDB for multi-region active-active ACID compliance.",
                "valid_at": "2026-04-15T11:00:00Z",
                "invalid_at": None,
                "weight": 0.98,
                "episodes": ["ep-103", "ep-104"],
            },
            {
                "uuid": "edge-03",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-6",
                "name": "USED_CACHE",
                "fact": "Project Hyperion initially utilized Redis for session and response caching.",
                "valid_at": "2026-04-01T09:30:00Z",
                "invalid_at": "2026-04-08T14:15:00Z",
                "weight": 0.90,
                "episodes": ["ep-101", "ep-102"],
            },
            {
                "uuid": "edge-04",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-5",
                "name": "ADOPTED_CACHE",
                "fact": "Project Hyperion adopted an In-Memory Raft Cache to eliminate Redis failover race conditions.",
                "valid_at": "2026-04-08T14:15:00Z",
                "invalid_at": None,
                "weight": 0.95,
                "episodes": ["ep-102", "ep-104"],
            },
            {
                "uuid": "edge-05",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-3",
                "name": "DECIDED_PROTOCOL",
                "fact": "Engineering approved ADR-014: all internal microservices communicate via gRPC with Protobuf contracts.",
                "valid_at": "2026-04-08T14:15:00Z",
                "invalid_at": None,
                "weight": 0.99,
                "episodes": ["ep-102", "ep-104"],
            },
            {
                "uuid": "edge-06",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-4",
                "name": "USES_GATEWAY",
                "fact": "REST Gateway is retained exclusively for public ingress, terminating external HTTP requests before forwarding to gRPC mesh.",
                "valid_at": "2026-04-08T14:15:00Z",
                "invalid_at": None,
                "weight": 0.92,
                "episodes": ["ep-102"],
            },
            {
                "uuid": "edge-07",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-8",
                "name": "PREFERS_SECURITY_POLICY",
                "fact": "Team preference established: all internal inter-service traffic must strictly enforce mutual TLS (mTLS).",
                "valid_at": "2026-04-15T11:00:00Z",
                "invalid_at": None,
                "weight": 0.96,
                "episodes": ["ep-103", "ep-104"],
            },
            {
                "uuid": "edge-08",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-7",
                "name": "COMMITTED_TASK",
                "fact": "Team commitment: complete comprehensive chaos engineering and load testing by Friday 5 PM before release.",
                "valid_at": "2026-04-22T16:45:00Z",
                "invalid_at": None,
                "weight": 0.93,
                "episodes": ["ep-104"],
            },
            {
                "uuid": "edge-09",
                "source_node_uuid": "node-7",
                "target_node_uuid": "node-7",
                "name": "PREFERS_OBSERVABILITY",
                "fact": "Team preference: Prometheus metrics and Grafana dashboards are required for service health visualization.",
                "valid_at": "2026-04-22T16:45:00Z",
                "invalid_at": None,
                "weight": 0.91,
                "episodes": ["ep-104"],
            },
        ],
    }

    if output_path:
        dest = Path(output_path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return data


if __name__ == "__main__":
    out = Path(__file__).parent / "data" / "architect_agent_graphiti.json"
    generate_architect_dataset(out)
    print(f"Generated realistic Graphiti dataset at: {out}")
