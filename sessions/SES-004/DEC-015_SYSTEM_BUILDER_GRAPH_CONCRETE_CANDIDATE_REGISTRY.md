# DEC-015 — SYSTEM BUILDER GRAPH CONCRETE CANDIDATE REGISTRY

**Session:** SES-004  
**Status:** PROPOSED FOR HUMAN APPROVAL  
**Type:** Candidate Registry  
**Depends on:** DEC-011, DEC-012, DEC-013, DEC-014  

---

## 1. Purpose

This document proposes the first **concrete technology evaluation set** for the System Builder Graph.

It is a registry for evidence gathering, not a technology decision.

The set deliberately contains architecturally different approaches so that the evaluation tests the System Builder Graph contract rather than merely comparing products within one technology family.

> **Candidates are admitted to be tested, not because they are preferred.**

---

## 2. Proposed Concrete Candidates

| ID | Class | Concrete Candidate | Why admitted |
|---|---|---|---|
| G-01 | Native Graph Database | **Neo4j** | Mature property-graph model with native nodes, relationships, paths and declarative graph querying through Cypher. Current documentation also exposes graph types and constraints, making semantic/integrity evaluation meaningful. |
| G-02 | Relational Graph Representation | **PostgreSQL** | Strong relational foundation and recursive querying; current PostgreSQL documentation also contains a property-graph query model, making it especially relevant for testing whether graph semantics can coexist with relational authority. |
| G-03 | Document-Oriented Graph Representation | **MongoDB** | General-purpose document model with `$graphLookup` recursive traversal. It is explicitly not a dedicated graph database, making it a useful negative/control comparison for semantic fidelity. |
| G-04 | Event-Sourced Graph Representation | **EventStoreDB / KurrentDB** | Purpose-built event-sourcing storage model. Useful for testing whether graph state, provenance and temporal reconstruction can be derived from an event-centric source of truth. |
| G-05 | Embedded / Local Graph | **SQLite + System Builder Graph layer** | Small, self-contained embedded database with a portable single-file representation. Tests whether the semantic Graph contract can be implemented above minimal local storage without requiring a database server. |
| G-06 | Distributed Graph / State Representation | **FoundationDB + System Builder Graph layer** | Distributed transactional ordered key-value foundation with ACID transactions and application-defined higher-level data models. Useful for testing graph semantics independently of a native graph engine. |
| G-07 | Hybrid Graph Architecture | **PostgreSQL + dedicated Graph layer** | Explicit hybrid control candidate. Tests separation of semantic Graph representation from underlying storage/query mechanisms and allows comparison against direct relational and native-graph approaches. |

---

## 3. Initial Admission Status

All seven candidates are **proposed evaluation candidates**.

No candidate is currently declared:

- `ELIGIBLE` for final architecture;
- semantically conformant;
- superior to another candidate;
- production-ready for System Builder.

The registry status is therefore:

`PROPOSED → PENDING EVIDENCE EVALUATION`

The final DEC-013 outcome states (`ELIGIBLE`, `INELIGIBLE`, `BLOCKED`, `DEFERRED`) SHALL be assigned only after evaluation evidence exists.

---

## 4. Evidence Basis

Initial admission is supported by current primary documentation:

- **Neo4j:** current Cypher documentation describes Neo4j as a property-graph database and documents nodes, relationships, paths, graph querying, constraints and graph types. Neo4j 2026.02+ uses Cypher 25 for new databases; graph types are generally available from 2026.06. 
- **PostgreSQL:** current documentation covers recursive queries; PostgreSQL documentation also provides a property-graph query model through `GRAPH_TABLE`. 
- **MongoDB:** official documentation describes `$graphLookup` as recursive traversal across collections and explicitly distinguishes MongoDB from dedicated graph databases.
- **EventStoreDB / KurrentDB:** available documentation describes EventStoreDB as a database designed for Event Sourcing and documents its open-source and enterprise editions.
- **SQLite:** official documentation describes SQLite as self-contained, embedded, serverless and portable; current release information identifies SQLite 3.53.4 dated 2026-07-24.
- **FoundationDB:** current official documentation describes a distributed ordered key-value database with ACID transactions, replication and application-defined higher-level data models.

These facts establish **candidate relevance only**. They are not conformance results.

---

## 5. Why This Set Is Intentionally Heterogeneous

The evaluation must answer a deeper question than:

> "Which graph database should we use?"

The relevant architectural question is:

> **What implementation foundation can preserve the System Builder Graph semantic contract, invariants, provenance, authority boundaries and evolution requirements with the strongest evidence and lowest unacceptable architectural cost?**

Therefore the registry includes:

1. a native graph implementation;
2. a relational implementation;
3. a document implementation;
4. an event-centric implementation;
5. a minimal embedded implementation;
6. a distributed primitive implementation;
7. a deliberately explicit hybrid implementation.

This prevents the evaluation from assuming in advance that the answer must be a graph database.

---

## 6. Evaluation Priority

The first detailed evaluations SHOULD proceed in the following order:

### Priority A — Semantic reference candidates

1. G-01 Neo4j
2. G-02 PostgreSQL
3. G-05 SQLite + Graph layer

These establish the baseline across native graph, relational and minimal embedded approaches.

### Priority B — Architectural alternatives

4. G-04 EventStoreDB / KurrentDB
5. G-06 FoundationDB + Graph layer
6. G-07 PostgreSQL + Graph layer

### Priority C — Control candidate

7. G-03 MongoDB

MongoDB is particularly useful as a control because its official documentation explicitly identifies it as a general-purpose document database with graph traversal capability rather than a dedicated graph database.

The order is an evaluation convenience, not a ranking of architectural merit.

---

## 7. Required Evaluation for Every Candidate

Every candidate SHALL be tested against the same mandatory criteria from DEC-011:

- TE-01 Semantic Fidelity
- TE-02 Invariant Conformance
- TE-03 Contract Conformance
- TE-04 Traceability
- TE-05 Provenance and Lineage
- TE-06 Authority and State Separation
- TE-07 Evolution
- TE-08 Integrity
- TE-09 Verification and Evidence
- TE-12 Portability and Technology Independence

Comparative criteria SHALL be applied only after the mandatory gate.

---

## 8. Special Attention Areas

The evaluation SHALL explicitly investigate whether each candidate can represent and verify:

- Node identity;
- typed relationships;
- relationship direction;
- graph invariants;
- semantic contracts;
- provenance and lineage;
- temporal/history information;
- authority versus derived state;
- controlled evolution;
- integrity constraints;
- reproducible verification;
- local operation;
- distributed operation where applicable;
- migration and exit paths.

The evaluation must distinguish **native capability** from **capability constructed by an additional System Builder layer**.

A feature implemented by our own layer is not automatically equivalent to a feature guaranteed by the underlying technology.

---

## 9. Critical Distinction

The registry adopts the following evidence discipline:

> **DOCUMENTED CAPABILITY ≠ OBSERVED CAPABILITY ≠ VERIFIED CONFORMANCE**

For example, the existence of graph traversal in a product does not prove conformance with the System Builder Graph contract.

Likewise, the existence of transactions does not by itself prove conformance with System Builder invariants.

Every such claim requires a specific evidence record.

---

## 10. Expected Evaluation Artifacts

For each candidate we SHALL eventually produce:

1. Candidate Profile;
2. Semantic Mapping;
3. Mandatory Test Results;
4. Evidence Records;
5. Limitations / Unknowns;
6. Gate Result;
7. Comparative Trade-offs;
8. Reversibility / Exit Analysis.

Only after these exist should a candidate contribute to a technology recommendation.

---

## 11. No Technology Selection Yet

DEC-015 does **not** authorize selection of Neo4j, PostgreSQL, MongoDB, EventStoreDB/KurrentDB, SQLite, FoundationDB, or the hybrid approach as the System Builder Graph foundation.

It authorizes only their admission as proposed subjects of controlled evaluation.

The architectural decision remains human-owned.

---

## 12. Human Approval Gate

Explicit human approval is required before:

- this concrete candidate set becomes the official evaluation set;
- a candidate is removed or replaced materially;
- additional technologies are promoted into the official set;
- detailed candidate evaluation is declared complete;
- any technology is recommended as the Graph foundation.

**Current decision:** `PROPOSED FOR HUMAN APPROVAL`

---

## 13. Next Step After Approval

The next controlled action is **Candidate Profile + Semantic Mapping for G-01 (Neo4j)**, followed by the same procedure for the remaining candidates.

No production implementation is authorized by DEC-015.
