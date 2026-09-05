---
type: Relationship
title: 'ADOPTED_CACHE: Project Hyperion -> In-Memory Raft Cache'
description: Project Hyperion adopted an In-Memory Raft Cache to eliminate Redis failover
  race conditions.
tags:
- graphiti
- temporal-edge
- adopted_cache
generated:
  by: zep-graphiti/adapter
  at: '2026-04-08T14:15:00Z'
x_memanto:
  type: relationship
  source: graphiti
  confidence: 0.95
  created_at: '2026-04-08T14:15:00Z'
  expires_at: null
  provenance: imported
  source_ref: edge-04
---

# Relationship: ADOPTED_CACHE

> **Temporal Status**: Active / Current

### Statement
Project Hyperion adopted an In-Memory Raft Cache to eliminate Redis failover race conditions.

### Lineage & Traversal
- **From**: [Project Hyperion](../facts/project-hyperion.md)
- **To**: [In-Memory Raft Cache](../facts/in-memory-raft-cache.md)
- **Valid Interval**: `2026-04-08T14:15:00Z` -> `indefinite`
- **Source Episodes**: ep-102, ep-104
