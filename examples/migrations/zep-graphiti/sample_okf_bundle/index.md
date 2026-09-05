# Open Knowledge Format (OKF) Bundle

Migrated from **Zep / Graphiti Temporal Knowledge Graph** to vendor-neutral portable markdown.
- **Exported At**: `2026-09-05T02:42:42.271655+00:00`
- **Total Concepts**: 21
- **Specification**: [OKF v0.2 (Google Cloud)](https://github.com/GoogleCloudPlatform/open-knowledge-format)

## Knowledge Index
| Concept | Type | Path | Summary |
| :--- | :--- | :--- | :--- |
| DECIDED_PROTOCOL (Project Hyperion -> gRPC Service Mesh) | `Architecture Decision` | [DECIDED_PROTOCOL (Project Hyperion -> gRPC Service Mesh)](memories/decisions/decided_protocol-project-hyperion-grpc-service-mesh.md) | Engineering approved ADR-014: all internal microservices communicate via gRPC with Protobu... |
| CockroachDB | `Entity Fact` | [CockroachDB](memories/facts/cockroachdb.md) | Distributed SQL database providing serializable ACID transactions and multi-region active-... |
| In-Memory Raft Cache | `Entity Fact` | [In-Memory Raft Cache](memories/facts/in-memory-raft-cache.md) | Consistent distributed in-memory cache synchronized via Raft consensus, replacing Redis.... |
| PostgreSQL | `Entity Fact` | [PostgreSQL](memories/facts/postgresql.md) | Legacy single-primary relational database used during prototype and initial alpha stages.... |
| Project Hyperion | `Entity Fact` | [Project Hyperion](memories/facts/project-hyperion.md) | Next-generation distributed agent orchestration and processing platform.... |
| REST Gateway | `Entity Fact` | [REST Gateway](memories/facts/rest-gateway.md) | External HTTP/JSON edge gateway handling third-party client ingress.... |
| Redis Cache | `Entity Fact` | [Redis Cache](memories/facts/redis-cache.md) | Deprecated caching layer removed due to cluster failover split-brain synchronization anoma... |
| Security & Auth Service | `Entity Fact` | [Security & Auth Service](memories/facts/security-auth-service.md) | Zero-trust internal identity service managing mTLS certificates and SPIFFE identities.... |
| gRPC Service Mesh | `Entity Fact` | [gRPC Service Mesh](memories/facts/grpc-service-mesh.md) | High-performance RPC framework using HTTP/2 transport and Protocol Buffers for typed inter... |
| PREFERS_OBSERVABILITY (Project Hyperion -> Project Hyperion) | `Preference` | [PREFERS_OBSERVABILITY (Project Hyperion -> Project Hyperion)](memories/preferences/prefers_observability-project-hyperion-project-hyperion.md) | Team preference: Prometheus metrics and Grafana dashboards are required for service health... |
| PREFERS_SECURITY_POLICY (Project Hyperion -> Security & Auth Service) | `Preference` | [PREFERS_SECURITY_POLICY (Project Hyperion -> Security & Auth Service)](memories/preferences/prefers_security_policy-project-hyperion-security-auth-servi.md) | Team preference established: all internal inter-service traffic must strictly enforce mutu... |
| ADOPTED_CACHE (Project Hyperion -> In-Memory Raft Cache) | `Relationship` | [ADOPTED_CACHE (Project Hyperion -> In-Memory Raft Cache)](memories/relationships/adopted_cache-project-hyperion-in-memory-raft-cache.md) | Project Hyperion adopted an In-Memory Raft Cache to eliminate Redis failover race conditio... |
| COMMITTED_TASK (Project Hyperion -> Project Hyperion) | `Relationship` | [COMMITTED_TASK (Project Hyperion -> Project Hyperion)](memories/relationships/committed_task-project-hyperion-project-hyperion.md) | Team commitment: complete comprehensive chaos engineering and load testing by Friday 5 PM ... |
| MIGRATED_TO_DATABASE (Project Hyperion -> CockroachDB) | `Relationship` | [MIGRATED_TO_DATABASE (Project Hyperion -> CockroachDB)](memories/relationships/migrated_to_database-project-hyperion-cockroachdb.md) | Project Hyperion migrated primary persistence to CockroachDB for multi-region active-activ... |
| USED_CACHE (Project Hyperion -> Redis Cache) | `Relationship` | [USED_CACHE (Project Hyperion -> Redis Cache)](memories/relationships/used_cache-project-hyperion-redis-cache.md) | Project Hyperion initially utilized Redis for session and response caching.... |
| USED_DATABASE (Project Hyperion -> PostgreSQL) | `Relationship` | [USED_DATABASE (Project Hyperion -> PostgreSQL)](memories/relationships/used_database-project-hyperion-postgresql.md) | Project Hyperion initially used PostgreSQL as its primary transactional store.... |
| USES_GATEWAY (Project Hyperion -> REST Gateway) | `Relationship` | [USES_GATEWAY (Project Hyperion -> REST Gateway)](memories/relationships/uses_gateway-project-hyperion-rest-gateway.md) | REST Gateway is retained exclusively for public ingress, terminating external HTTP request... |
| Episode 1: Initial Architecture Kickoff | `Session Event` | [Episode 1: Initial Architecture Kickoff](memories/events/episode-1-initial-architecture-kickoff.md) | Kickoff meeting for Project Hyperion. We decided to build a monolithic REST API using Post... |
| Episode 2: Protocol Scaling & Cache Race Issues | `Session Event` | [Episode 2: Protocol Scaling & Cache Race Issues](memories/events/episode-2-protocol-scaling-cache-race-issues.md) | P99 latency spiked past 600ms on REST endpoints under peak load. We approved ADR-014: migr... |
| Episode 3: Multi-Region Compliance & Active-Active DB | `Session Event` | [Episode 3: Multi-Region Compliance & Active-Active DB](memories/events/episode-3-multi-region-compliance-active-active-db.md) | EU GDPR and latency requirements mandate multi-region active-active writes. PostgreSQL sin... |
| Episode 4: Production Launch Readiness | `Session Event` | [Episode 4: Production Launch Readiness](memories/events/episode-4-production-launch-readiness.md) | Final pre-production sprint. Commitment made: complete comprehensive chaos engineering and... |
