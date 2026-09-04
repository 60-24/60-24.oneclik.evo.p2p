# DEC-014 — SYSTEM BUILDER GRAPH CANDIDATE REGISTRY AND EVALUATION SET

**Session:** SES-004  
**Status:** PROPOSED FOR HUMAN APPROVAL  
**Type:** Decision / Evaluation Preparation  
**Depends on:** DEC-011, DEC-012, DEC-013  

---

## 1. Purpose

This document establishes the initial **Candidate Registry / Evaluation Set** for the System Builder Graph.

It does **not** select the final Graph technology.

Its purpose is to define a small, explicit and auditable set of candidate implementation approaches that can be evaluated against the already accepted semantic contract, invariants, conformance scenarios and technology-evaluation framework.

> **We select candidates for evidence, not technologies for preference.**

---

## 2. Governing Principle

> **Technology implements meaning. Technology does not define meaning.**

The candidate registry therefore starts from the System Builder Graph contract and asks whether an implementation approach can preserve and verify that meaning.

No candidate receives preference because it is popular, familiar, fast, fashionable, or convenient to implement.

---

## 3. Candidate Classes

The initial evaluation set SHALL cover the following architectural classes:

| ID | Candidate Class | Evaluation Role |
|---|---|---|
| C-01 | Native Graph Database | Test whether native graph semantics provide strong contract fidelity and verification. |
| C-02 | Relational Graph Representation | Test whether graph semantics can be represented rigorously using relational primitives. |
| C-03 | Document-Oriented Graph Representation | Test graph representation in document-centric storage. |
| C-04 | Event-Sourced Graph Representation | Test whether graph state can be derived and verified from immutable events. |
| C-05 | Embedded / Local Graph | Test autonomous, local-first graph execution and portability. |
| C-06 | Distributed Graph / State Representation | Test graph semantics across multiple nodes and replicated state. |
| C-07 | Hybrid Graph Architecture | Test combinations where storage, event, query, or verification responsibilities are separated. |

These are **evaluation classes**, not technology choices.

---

## 4. Candidate Admission Rules

A concrete technology may enter the official evaluation set only when:

1. its architectural model can be documented;
2. the relevant version or release line can be identified;
3. meaningful evaluation can be executed or independently verified;
4. its representation can be mapped to the System Builder Graph semantic contract;
5. evidence can be inspected and reproduced to a reasonable degree;
6. licensing and operational constraints can be recorded;
7. limitations and unknowns can be stated explicitly.

A technology that cannot satisfy these conditions is not silently treated as a weak candidate. It SHALL be marked `BLOCKED` or excluded with an explicit reason.

---

## 5. Concrete Candidate Selection Rule

The first registry intentionally avoids premature commitment to named products.

Concrete technologies SHALL be added in the next evaluation step only when there is a credible reason to use them as representatives of one of the candidate classes.

Selection SHALL consider:

- semantic relevance;
- evidence availability;
- architectural diversity;
- ability to test the same contract;
- reproducibility;
- technology independence;
- realistic applicability to System Builder.

The registry SHALL remain small enough that every admitted candidate can receive serious evidence-based evaluation.

---

## 6. Required Candidate Record

Each concrete candidate SHALL receive a stable record containing at least:

```text
CANDIDATE_ID
CLASS
TECHNOLOGY
VERSION
ARCHITECTURE_REFERENCE
SEMANTIC_MAPPING_REFERENCE
TEST_SET_REFERENCE
EVIDENCE_REFERENCE
LICENSING_REFERENCE
OPERATIONAL_CONSTRAINTS
KNOWN_LIMITATIONS
STATUS
CONFIDENCE
REPRODUCIBILITY
EXIT_IMPLICATIONS
```

`STATUS` SHALL use the states defined by DEC-013:

- `ELIGIBLE`
- `INELIGIBLE`
- `BLOCKED`
- `DEFERRED`

Evaluation evidence itself SHALL continue to use the evidence states defined by DEC-011:

- `PASS`
- `FAIL`
- `PARTIAL`
- `UNKNOWN`
- `BLOCKED`
- `NOT_APPLICABLE`

These two status systems SHALL NOT be conflated.

---

## 7. Evaluation Set Discipline

Every admitted concrete candidate SHALL be evaluated against the same semantic basis.

Minimum common basis:

- Graph semantic contract;
- graph invariants;
- contract-conformance tests;
- conformance scenarios;
- reference test matrix;
- mandatory technology criteria TE-01 through TE-09 and TE-12;
- evidence and provenance requirements.

The candidate SHALL NOT be allowed to redefine the contract to fit its implementation.

---

## 8. Fair Comparison Rule

For all candidates:

> **Same contract. Same tests. Same evidence discipline. Different technologies. Human chooses.**

The evaluation SHALL maintain:

- identical semantic expectations;
- equivalent test intent;
- equivalent evidence requirements;
- explicit failure reporting;
- explicit limitations;
- explicit unknowns;
- no hidden mandatory failures.

Comparative performance or convenience SHALL NOT compensate for failure of a mandatory semantic or integrity criterion.

---

## 9. Evaluation Order

The registry SHALL be processed in this order:

```text
1. Candidate Class
       ↓
2. Concrete Candidate Admission
       ↓
3. Version / Architecture Identification
       ↓
4. Semantic Mapping
       ↓
5. Mandatory Conformance Evaluation
       ↓
6. Evidence Review
       ↓
7. Gate Result
       ↓
8. Comparative Evaluation
       ↓
9. Trade-off Analysis
       ↓
10. Human Architectural Decision
```

No step may be skipped merely because a technology appears obviously suitable.

---

## 10. Explicit Non-Goals

DEC-014 does **not**:

- select a Graph database;
- authorize production implementation;
- authorize premature coding;
- define a final deployment architecture;
- replace the semantic contract;
- replace the conformance test suite;
- establish performance as the primary selection criterion;
- permit vendor popularity to become an architectural criterion.

---

## 11. Next Step

After human approval of DEC-014, the next controlled action is:

**Populate the registry with a limited set of concrete technologies and establish the evidence sources required to evaluate them.**

Only after that registry is approved should detailed candidate evaluation begin.

---

## 12. Human Approval Gate

DEC-014 requires explicit human approval before:

- concrete technologies become official evaluation candidates;
- the candidate set is reduced or expanded materially;
- a candidate is declared eligible for final architectural selection;
- the evaluation proceeds to a technology recommendation.

**Current decision:** `PROPOSED FOR HUMAN APPROVAL`
