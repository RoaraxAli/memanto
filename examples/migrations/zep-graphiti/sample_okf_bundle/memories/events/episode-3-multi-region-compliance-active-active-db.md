---
type: Session Event
title: 'Episode 3: Multi-Region Compliance & Active-Active DB'
description: EU GDPR and latency requirements mandate multi-region active-active writes.
  PostgreSQL single-primary topology cannot sa
tags:
- graphiti
- episode
- timeline
generated:
  by: zep-graphiti/adapter
  at: '2026-04-15T11:00:00Z'
x_memanto:
  type: event
  source: graphiti
  confidence: 0.8
  created_at: '2026-04-15T11:00:00Z'
  provenance: imported
  source_ref: ep-103
---

# Episode 3: Multi-Region Compliance & Active-Active DB

EU GDPR and latency requirements mandate multi-region active-active writes. PostgreSQL single-primary topology cannot satisfy this SLA. We officially invalidated the PostgreSQL architecture and migrated the primary transactional datastore to CockroachDB. Established strict team preference: all new microservices must enforce mutual TLS (mTLS).

## Session Provenance
- **Logged At**: `2026-04-15T11:00:00Z`
- **Channel/Source**: `architecture_review`
