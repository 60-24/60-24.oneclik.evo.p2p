# DEC-005 — SYSTEM BUILDER GRAPH BACKBONE

**Status:** APPROVED  
**Session:** SES-003  
**Decision:** The Graph is the structural backbone of System Builder.

## 1. Decision

System Builder shall treat the **Graph** as its structural memory and traceability backbone.

The Graph is not merely a database, visualization, or documentation index. It represents the relationships between meaning, decisions, system structure, artifacts, evidence, observations, and evolution.

## 2. Purpose

The Graph must allow System Builder to reconstruct and navigate the path from human intent to the verified operating target system, and back from implementation and runtime observations to the decisions and intent that produced them.

Canonical conceptual flow:

`HUMAN → INTENT → MODEL → DESIGN → CONTRACT → BUILD → VERIFY → EVIDENCE → VALIDATION → OBSERVE → EVOLVE → MODEL`

## 3. Minimal Conceptual Node Classes

### Meaning
- Intent
- Concept
- Entity
- Relation

### Decision
- Decision
- Constraint
- Invariant
- Assumption

### System
- Component
- Interface
- Contract
- Artifact

### Evidence
- Claim
- Test
- Observation
- Evidence
- Validation

### Evolution
- Change
- Proposal
- Version
- Event

These are semantic classes only. They do not yet prescribe implementation technology.

## 4. Minimal Conceptual Relations

The Graph must be capable of expressing at least:

- `DERIVED_FROM`
- `DEPENDS_ON`
- `CONSTRAINED_BY`
- `IMPLEMENTS`
- `SATISFIES`
- `VERIFIED_BY`
- `SUPPORTED_BY`
- `OBSERVED_BY`
- `CHANGED_BY`
- `PROPOSES`
- `SUPERSEDES`

## 5. Bidirectional Traceability

The Graph must support both directions of reasoning.

Forward:

`Intent → Design → Contract → Implementation → Test → Evidence`

Reverse:

`Implementation → Contract → Design → Intent`

This enables System Builder to answer questions such as:

- Why does this system element exist?
- Which decision created or constrained it?
- Which contract does it implement?
- What evidence verifies it?
- What intent would be affected if it changed?

## 6. Graph as Lifecycle Memory

The Graph must preserve the relationships necessary to understand system evolution over time.

A meaningful change follows the traceable path:

`OBSERVE → EVIDENCE → CHANGE PROPOSAL → HUMAN/AUTHORITY REVIEW → MODEL/DESIGN → BUILD → VERIFY`

Changes must not silently rewrite constitutional or ontological meaning.

## 7. Evidence and Truth Boundary

The Graph may record claims, tests, observations, evidence, and validation states, but the existence of a graph node or relationship does not itself constitute proof.

The governing evidence model remains:

`CLAIM → TEST / OBSERVATION → EVIDENCE → VALIDATION → CONFIDENCE`

## 8. Technology Boundary

This decision does **not** select:

- Neo4j
- RDF / OWL
- PostgreSQL
- JSON
- CRDT
- graph database
- event store
- any specific programming language or runtime

Technology selection is deferred until Graph semantics, invariants, contracts, and operational requirements are sufficiently defined.

## 9. Governing Principle

> **The Graph is the structural memory of System Builder: it preserves meaning, decisions, dependencies, artifacts, evidence and evolution so that the system can be understood, verified and changed without losing its traceability.**

## 10. Next Decision

The next step is to define **Graph Invariants**: properties that the Graph must never lose, violate, or silently change.

This is the prerequisite for selecting a concrete graph representation or technology.
