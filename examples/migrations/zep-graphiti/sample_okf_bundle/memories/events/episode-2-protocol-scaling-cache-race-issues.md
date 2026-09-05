---
type: Session Event
title: 'Episode 2: Protocol Scaling & Cache Race Issues'
description: 'P99 latency spiked past 600ms on REST endpoints under peak load. We
  approved ADR-014: migrating all inter-service commun'
tags:
- graphiti
- episode
- timeline
generated:
  by: zep-graphiti/adapter
  at: '2026-04-08T14:15:00Z'
x_memanto:
  type: event
  source: graphiti
  confidence: 0.8
  created_at: '2026-04-08T14:15:00Z'
  provenance: imported
  source_ref: ep-102
---

# Episode 2: Protocol Scaling & Cache Race Issues

P99 latency spiked past 600ms on REST endpoints under peak load. We approved ADR-014: migrating all inter-service communications to gRPC with protobuf schemas. Furthermore, Redis cache showed split-brain race conditions under cluster failover; decided to deprecate Redis in favor of an In-Memory Raft-synchronized cache layer.

## Session Provenance
- **Logged At**: `2026-04-08T14:15:00Z`
- **Channel/Source**: `meeting_transcript`
