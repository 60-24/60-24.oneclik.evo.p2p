# DEC-015 — SYSTEM BUILDER GRAPH CONCRETE CANDIDATE REGISTRY

**Session:** SES-004  
**Status:** ACCEPTED BY HUMAN  
**Type:** Candidate Registry  
**Depends on:** DEC-011, DEC-012, DEC-013, DEC-014  

---

## Decision

DEC-015 is **accepted by human approval**.

The following seven concrete candidates are now the official evaluation set:

| ID | Class | Candidate |
|---|---|---|
| G-01 | Native Graph Database | Neo4j |
| G-02 | Relational Graph Representation | PostgreSQL |
| G-03 | Document-Oriented Graph Representation | MongoDB |
| G-04 | Event-Sourced Graph Representation | EventStoreDB / KurrentDB |
| G-05 | Embedded / Local Graph | SQLite + System Builder Graph layer |
| G-06 | Distributed Graph / State Representation | FoundationDB + System Builder Graph layer |
| G-07 | Hybrid Graph Architecture | PostgreSQL + dedicated Graph layer |

Admission means **subject of evaluation**, not recommendation.

## Evaluation Rule

Every candidate SHALL be evaluated against the same semantic contract, invariants, conformance scenarios, reference test matrix and mandatory criteria from DEC-011.

> **DOCUMENTED CAPABILITY ≠ OBSERVED CAPABILITY ≠ VERIFIED CONFORMANCE**

A capability supplied by a System Builder layer SHALL be distinguished from a capability guaranteed by the underlying technology.

## Current Status

No candidate is currently declared:

- semantically conformant;
- superior;
- production-ready;
- selected as the Graph foundation.

## Next Controlled Step

Begin **G-01 — Neo4j Candidate Profile + Semantic Mapping** using current primary documentation and the approved evaluation framework.

No production implementation is authorized by DEC-015.

**Decision status:** `ACCEPTED BY HUMAN`
