# DEC-008 — SYSTEM BUILDER SCHEMA-INDEPENDENT GRAPH CONTRACT TESTS

**Status:** PROPOSED FOR HUMAN APPROVAL  
**Session:** SES-003  
**Depends on:** DEC-005, DEC-006, DEC-007

## 1. Purpose

This decision defines the first testable contract for the System Builder Graph without selecting a database, serialization format, runtime, programming language, or graph technology.

The goal is to establish what every future Graph implementation MUST prove before it can be treated as conformant.

## 2. Principle

> **We test Graph semantics and invariants, not the implementation technology.**

A Graph implementation is conformant only when its behavior preserves the semantic contracts defined by DEC-005–DEC-007 and the Graph invariants defined by DEC-006.

## 3. Conformance Test Domains

### GT-01 — Identity

The implementation MUST:
- assign or preserve stable unique Node identity;
- distinguish Nodes with different identities;
- reject or expose identity collisions;
- preserve identity across non-semantic representation changes.

### GT-02 — Typed Relations

The implementation MUST:
- represent an Edge as a relationship between identified Nodes;
- preserve the declared relation type;
- distinguish relation semantics from storage-level references;
- reject or expose references to unknown Nodes.

### GT-03 — Provenance

The implementation MUST allow a meaningful derived/transformed element to be traced to its relevant source and transformation context.

At minimum the test MUST establish:
`RESULT → SOURCE → TRANSFORMATION/DECISION → TIME/CONTEXT`

### GT-04 — Authority and State Separation

The implementation MUST distinguish at least:
- proposed;
- approved;
- active/operational;
- rejected/superseded/deprecated where applicable.

A stored Node MUST NOT become authoritative merely because it exists in the Graph.

### GT-05 — Proposal vs Reality

The implementation MUST distinguish an AI/system proposal from an approved or observed state.

The following MUST remain semantically distinguishable:
`PROPOSAL ≠ APPROVED DECISION ≠ OBSERVED STATE ≠ VALIDATED STATE`

### GT-06 — Claim vs Evidence vs Validation

The implementation MUST preserve the distinction:
`CLAIM → TEST/OBSERVATION → EVIDENCE → VALIDATION → CONFIDENCE`

The existence of any one element MUST NOT automatically imply the truth of another.

### GT-07 — Temporal Lineage

The implementation MUST preserve relevant temporal information sufficient to determine:
- when an element became valid;
- when it changed;
- what previous state it superseded;
- what state is currently active.

### GT-08 — Forward Traceability

The implementation MUST support reconstruction of:
`INTENT → MODEL → DESIGN → CONTRACT → BUILD → VERIFY → EVIDENCE → VALIDATION → OBSERVE → EVOLVE`

The exact representation may differ, but semantic traceability MUST be preserved.

### GT-09 — Reverse Traceability / Impact Analysis

The implementation MUST support reconstruction from implementation-level elements back toward their governing meaning:
`ARTIFACT/COMPONENT → CONTRACT → DESIGN → INTENT`

This is required for impact analysis and controlled evolution.

### GT-10 — Explicit Change

A material change MUST be representable as an explicit change event/record containing, where applicable:
`WHAT → WHY → AUTHORITY → WHEN → PREVIOUS → RESULTING → EVIDENCE`

Silent mutation MUST fail the conformance test.

### GT-11 — Constraint Visibility

The implementation MUST allow a system element to be traced to the constraints/invariants that govern it.

At minimum:
`ELEMENT → CONSTRAINED_BY → CONSTRAINT/INVARIANT`

### GT-12 — Technology Independence

The same semantic test suite MUST be applicable to more than one possible storage/implementation technology without changing the meaning of the tests.

Technology-specific adapters MAY exist, but MUST NOT redefine the semantic contract.

## 4. Minimum Acceptance Set

A candidate Graph implementation MUST pass all of the following before being considered conformant:

1. stable identity;
2. typed relations;
3. provenance;
4. authority/state separation;
5. proposal/reality separation;
6. claim/evidence/validation separation;
7. temporal lineage;
8. forward traceability;
9. reverse traceability;
10. explicit material change;
11. constraint visibility;
12. technology-independent semantics.

## 5. Failure Semantics

A failed test MUST produce an explicit result and MUST NOT be silently ignored.

A critical failure affecting identity, authority, provenance, traceability, evidence separation, or lineage MUST block a conformance claim.

## 6. Relationship to DEC-006

DEC-006 defines the Graph invariants.

DEC-008 converts those invariants into a minimum behavioral conformance boundary.

Therefore:

`DEC-006 = WHAT MUST REMAIN TRUE`

`DEC-008 = HOW A FUTURE IMPLEMENTATION MUST DEMONSTRATE IT`

## 7. Relationship to DEC-007

DEC-007 defines the semantic Node/Edge model and contracts.

DEC-008 defines tests for those contracts.

Therefore the dependency chain is:

`DEC-005 Graph Backbone`
`→ DEC-006 Graph Invariants`
`→ DEC-007 Semantic Model + Contracts`
`→ DEC-008 Contract Tests`

## 8. Technology Gate

No technology selection is authorized by this decision.

The following remain intentionally open:
- graph database vs relational/document/event representation;
- serialization format;
- runtime;
- programming language;
- distributed synchronization mechanism;
- query language.

Technology selection may begin only after the semantic conformance boundary is accepted and concrete implementation requirements are derived from it.

## 9. Approval Gate

This document is **PROPOSED FOR HUMAN APPROVAL**.

If approved, the next step is:

**DEC-009 — Graph Conformance Scenarios / Reference Test Cases**

DEC-009 will turn the abstract contract tests into concrete, technology-neutral scenarios with expected outcomes and failure conditions.

## 10. Governing Rule

> **No Graph implementation is accepted because it stores Nodes and Edges. It is accepted only when it demonstrably preserves the project's meaning, authority, provenance, evidence, traceability, time and lineage.**
