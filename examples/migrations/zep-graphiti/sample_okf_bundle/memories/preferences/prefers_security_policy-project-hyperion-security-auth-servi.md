---
type: Preference
title: 'PREFERS_SECURITY_POLICY: Project Hyperion -> Security & Auth Service'
description: 'Team preference established: all internal inter-service traffic must
  strictly enforce mutual TLS (mTLS).'
tags:
- graphiti
- temporal-edge
- prefers_security_policy
generated:
  by: zep-graphiti/adapter
  at: '2026-04-15T11:00:00Z'
x_memanto:
  type: preference
  source: graphiti
  confidence: 0.96
  created_at: '2026-04-15T11:00:00Z'
  expires_at: null
  provenance: imported
  source_ref: edge-07
---

# Preference: PREFERS_SECURITY_POLICY

> **Temporal Status**: Active / Current

### Statement
Team preference established: all internal inter-service traffic must strictly enforce mutual TLS (mTLS).

### Lineage & Traversal
- **From**: [Project Hyperion](../facts/project-hyperion.md)
- **To**: [Security & Auth Service](../facts/security-auth-service.md)
- **Valid Interval**: `2026-04-15T11:00:00Z` -> `indefinite`
- **Source Episodes**: ep-103, ep-104
