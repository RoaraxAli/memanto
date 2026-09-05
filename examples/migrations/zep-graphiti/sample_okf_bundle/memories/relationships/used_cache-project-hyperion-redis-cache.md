---
type: Relationship
title: 'USED_CACHE: Project Hyperion -> Redis Cache'
description: Project Hyperion initially utilized Redis for session and response caching.
tags:
- graphiti
- temporal-edge
- used_cache
generated:
  by: zep-graphiti/adapter
  at: '2026-04-01T09:30:00Z'
x_memanto:
  type: relationship
  source: graphiti
  confidence: 0.9
  created_at: '2026-04-01T09:30:00Z'
  expires_at: '2026-04-08T14:15:00Z'
  provenance: imported
  source_ref: edge-03
---

# Relationship: USED_CACHE

> **Temporal Status**: Invalidated / Deprecated

### Statement
Project Hyperion initially utilized Redis for session and response caching.

### Lineage & Traversal
- **From**: [Project Hyperion](../facts/project-hyperion.md)
- **To**: [Redis Cache](../facts/redis-cache.md)
- **Valid Interval**: `2026-04-01T09:30:00Z` -> `2026-04-08T14:15:00Z`
- **Source Episodes**: ep-101, ep-102
