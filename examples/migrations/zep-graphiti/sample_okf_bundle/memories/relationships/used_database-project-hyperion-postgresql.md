---
type: Relationship
title: 'USED_DATABASE: Project Hyperion -> PostgreSQL'
description: Project Hyperion initially used PostgreSQL as its primary transactional
  store.
tags:
- graphiti
- temporal-edge
- used_database
generated:
  by: zep-graphiti/adapter
  at: '2026-04-01T09:30:00Z'
x_memanto:
  type: relationship
  source: graphiti
  confidence: 0.95
  created_at: '2026-04-01T09:30:00Z'
  expires_at: '2026-04-15T11:00:00Z'
  provenance: imported
  source_ref: edge-01
---

# Relationship: USED_DATABASE

> **Temporal Status**: Invalidated / Deprecated

### Statement
Project Hyperion initially used PostgreSQL as its primary transactional store.

### Lineage & Traversal
- **From**: [Project Hyperion](../facts/project-hyperion.md)
- **To**: [PostgreSQL](../facts/postgresql.md)
- **Valid Interval**: `2026-04-01T09:30:00Z` -> `2026-04-15T11:00:00Z`
- **Source Episodes**: ep-101, ep-103
