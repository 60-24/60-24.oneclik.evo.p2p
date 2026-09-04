# DEC-010 — SYSTEM BUILDER GRAPH REFERENCE TEST MATRIX AND ACCEPTANCE CRITERIA

**Status:** PROPOSED FOR HUMAN APPROVAL  
**Session:** SES-003  
**Depends on:** DEC-006, DEC-007, DEC-008, DEC-009

## 1. Purpose

This decision establishes the acceptance matrix connecting Graph invariants, semantic contracts and reference scenarios.

It defines the minimum evidence required before a future Graph implementation may claim conformance.

## 2. Acceptance Principle

> **A Graph is conformant only when every mandatory semantic requirement has a reproducible test result and sufficient evidence.**

## 3. Reference Matrix

| ID | Requirement | Primary Scenario | Acceptance Condition | Blocking Failure |
|---|---|---|---|---|
| AC-01 | Identity | GS-01 | Unique, stable identities are demonstrable | Yes |
| AC-02 | Typed relations | GS-02 | Relation type and endpoints remain semantically correct | Yes |
| AC-03 | Referential integrity | GS-03 | Invalid references are rejected or explicitly exposed | Yes |
| AC-04 | Provenance | GS-04 | Origin and transformation context are reconstructable | Yes |
| AC-05 | Authority/state separation | GS-05 | Proposal cannot become approval through storage | Yes |
| AC-06 | Evidence separation | GS-06, GS-07 | Claim, evidence and validation remain distinct | Yes |
| AC-07 | Temporal lineage | GS-08 | Required historical states and transitions remain reconstructable | Yes |
| AC-08 | Forward traceability | GS-09 | Intent-to-evidence path is reconstructable | Yes |
| AC-09 | Reverse traceability | GS-10 | Artifact-to-intent path is reconstructable | Yes |
| AC-10 | Constraint visibility | GS-11 | Governing constraints/invariants are discoverable | Yes |
| AC-11 | Explicit change | GS-12 | Material changes have explicit records and lineage | Yes |
| AC-12 | Supersession | GS-13 | Previous and governing decisions remain distinguishable | Yes |
| AC-13 | Technology independence | GS-14 | Semantic result is implementation-independent | Yes |

## 4. Invariant Coverage

The acceptance matrix is intended to exercise the following DEC-006 invariants:

- G-01 Identity
- G-02 Provenance
- G-03 Meaning Preservation
- G-04 Traceability
- G-05 Decision Integrity
- G-06 Authority Integrity
- G-07 Evidence Separation
- G-08 Temporal Integrity
- G-09 Referential Integrity
- G-10 Bidirectional Reconstruction
- G-11 No Silent Mutation
- G-12 Separation of Proposal and Reality
- G-13 Constraint Visibility
- G-14 Evolution Without Loss of Lineage
- G-15 Technology Independence
- G-16 No Authority by Existence

## 5. Pass Criteria

A candidate implementation passes the reference acceptance gate only if:

1. all mandatory scenarios GS-01 through GS-14 execute successfully;
2. no critical or major semantic failure remains unresolved;
3. expected and actual results are recorded;
4. implementation/version under test is identified;
5. test context is recorded;
6. evidence is retained sufficiently to reproduce or audit the result;
7. failures are not silently suppressed;
8. the implementation does not require a change to the semantic contract in order to pass.

## 6. Evidence Record

For each acceptance item, the minimum evidence record SHOULD contain:

`TEST_ID`
`IMPLEMENTATION_VERSION`
`CONTEXT`
`EXPECTED_RESULT`
`ACTUAL_RESULT`
`STATUS`
`OBSERVATION`
`EVIDENCE_REFERENCE`
`VALIDATION_STATUS`
`CONFIDENCE`

## 7. Result States

Each acceptance item uses one of:

- `PASS` — requirement demonstrated;
- `FAIL` — requirement violated;
- `BLOCKED` — test could not be validly executed;
- `NOT_APPLICABLE` — only when justified by the semantic model and explicitly recorded.

`BLOCKED` MUST NOT be treated as `PASS`.

## 8. Conformance Decision

The final conformance result is:

`CONFORMANT` only if all mandatory acceptance items are `PASS`.

Otherwise:

`NON-CONFORMANT`.

An implementation with unresolved `BLOCKED` items cannot claim full conformance.

## 9. Change Control

If a candidate implementation cannot satisfy an acceptance criterion, the default assumption is that the implementation is deficient.

Changing the semantic contract or acceptance criterion requires an explicit architectural/constitutional decision where applicable. It MUST NOT be done merely to make an implementation pass.

## 10. Technology Gate

DEC-010 does not select technology.

It creates the evaluation boundary that future technologies must satisfy.

Only after approval of this acceptance matrix should candidate technologies be compared against the established requirements.

## 11. Approval Gate

This document is **PROPOSED FOR HUMAN APPROVAL**.

If approved, the next step is:

**DEC-011 — Graph Technology Evaluation Framework**

DEC-011 will define how candidate implementation approaches are compared against the already-frozen semantic and acceptance requirements, without allowing technology to redefine the project's meaning.

## 12. Governing Rule

> **The project chooses technology to satisfy the contract; the technology does not choose the contract.**
