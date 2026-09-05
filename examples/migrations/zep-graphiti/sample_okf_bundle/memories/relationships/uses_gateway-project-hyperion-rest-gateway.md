---
type: Relationship
title: 'USES_GATEWAY: Project Hyperion -> REST Gateway'
description: REST Gateway is retained exclusively for public ingress, terminating
  external HTTP requests before forwarding to gRPC me
tags:
- graphiti
- temporal-edge
- uses_gateway
generated:
  by: zep-graphiti/adapter
  at: '2026-04-08T14:15:00Z'
x_memanto:
  type: relationship
  source: graphiti
  confidence: 0.92
  created_at: '2026-04-08T14:15:00Z'
  expires_at: null
  provenance: imported
  source_ref: edge-06
---

# Relationship: USES_GATEWAY

> **Temporal Status**: Active / Current

### Statement
REST Gateway is retained exclusively for public ingress, terminating external HTTP requests before forwarding to gRPC mesh.

### Lineage & Traversal
- **From**: [Project Hyperion](../facts/project-hyperion.md)
- **To**: [REST Gateway](../facts/rest-gateway.md)
- **Valid Interval**: `2026-04-08T14:15:00Z` -> `indefinite`
- **Source Episodes**: ep-102
