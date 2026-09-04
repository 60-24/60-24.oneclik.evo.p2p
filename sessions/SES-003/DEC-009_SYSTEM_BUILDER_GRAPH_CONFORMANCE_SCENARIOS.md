# DEC-009 — SYSTEM BUILDER GRAPH CONFORMANCE SCENARIOS

**Status:** PROPOSED FOR HUMAN APPROVAL  
**Session:** SES-003  
**Depends on:** DEC-005, DEC-006, DEC-007, DEC-008

## 1. Purpose

This decision converts the schema-independent Graph contract tests from DEC-008 into concrete reference scenarios.

The scenarios define expected semantic behavior without prescribing implementation technology.

## 2. Scenario Format

Each scenario uses:

`GIVEN → WHEN → THEN`

A conformant implementation MUST produce the expected semantic result, regardless of its internal storage or runtime model.

## 3. Reference Scenarios

### GS-01 — Unique Node Identity

**GIVEN** two meaningful Nodes are created.

**WHEN** they receive identities.

**THEN** each identity is unique and remains stable across representation changes.

**FAIL:** two distinct Nodes become indistinguishable or an identity silently changes.

### GS-02 — Typed Edge

**GIVEN** Node A and Node B exist.

**WHEN** an Edge is created between them as `IMPLEMENTS`.

**THEN** the implementation preserves A, B and the semantic relation `IMPLEMENTS`.

**FAIL:** the relation is reduced to an untyped pointer or its meaning changes.

### GS-03 — Invalid Reference

**GIVEN** an Edge references Node X.

**WHEN** Node X does not exist.

**THEN** the implementation rejects the invalid reference or exposes it explicitly as an integrity violation.

**FAIL:** the invalid reference is silently treated as valid.

### GS-04 — Derived Artifact Provenance

**GIVEN** Artifact A is derived from Intent I through a documented transformation.

**WHEN** the Graph records A.

**THEN** the path from A to I and the relevant transformation/context remains reconstructable.

**FAIL:** the artifact exists without recoverable origin.

### GS-05 — Proposal Does Not Become Approval

**GIVEN** an AI-generated Proposal P exists.

**WHEN** P is stored in the Graph.

**THEN** P remains a proposal until an authorized decision changes its state/authority.

**FAIL:** persistence alone makes P an approved decision.

### GS-06 — Claim Does Not Become Evidence

**GIVEN** Claim C states that a property is true.

**WHEN** C is stored without supporting evidence.

**THEN** C remains a claim and cannot be represented as validated merely because it exists.

**FAIL:** claim existence is interpreted as proof.

### GS-07 — Evidence Does Not Equal Validation

**GIVEN** Evidence E exists for Claim C.

**WHEN** no validation decision has occurred.

**THEN** E remains evidence and C does not automatically become validated.

**FAIL:** evidence is silently promoted to validation.

### GS-08 — Historical State Preservation

**GIVEN** Node N has state S1.

**WHEN** a material change produces state S2.

**THEN** the implementation preserves enough lineage to identify S1, S2 and the transition between them.

**FAIL:** S1 is silently overwritten with no recoverable history where history is semantically required.

### GS-09 — Forward Trace

**GIVEN** an Intent has downstream Design, Contract, Artifact, Test and Evidence relations.

**WHEN** the Graph is queried from the Intent.

**THEN** the downstream chain can be reconstructed.

**FAIL:** a required semantic link is lost.

### GS-10 — Reverse Trace

**GIVEN** an Artifact is governed by a Contract derived from a Design and Intent.

**WHEN** the Graph is queried from the Artifact.

**THEN** the governing Contract, Design and Intent can be reconstructed.

**FAIL:** impact analysis cannot reach the governing meaning.

### GS-11 — Constraint Visibility

**GIVEN** Component C is constrained by Invariant I.

**WHEN** C is inspected.

**THEN** the relation `C CONSTRAINED_BY I` is recoverable.

**FAIL:** the governing invariant is invisible to the Graph.

### GS-12 — Explicit Material Change

**GIVEN** an active Contract changes materially.

**WHEN** the change is accepted.

**THEN** the Graph records the change, reason, authority, time, previous state, resulting state and relevant evidence.

**FAIL:** the active contract changes without an explicit semantic change record.

### GS-13 — Supersession

**GIVEN** Decision D1 is replaced by Decision D2.

**WHEN** D2 becomes the governing decision.

**THEN** the relationship between D1 and D2 is explicit and D1 is not falsely represented as simultaneously governing unless the project semantics explicitly permit that state.

**FAIL:** lineage or governing status becomes ambiguous.

### GS-14 — Technology-Neutral Reproduction

**GIVEN** the same semantic scenario is implemented using two different candidate technologies.

**WHEN** both execute the reference scenario.

**THEN** both produce semantically equivalent conformance results.

**FAIL:** the scenario's meaning depends on a particular storage technology.

## 4. Mandatory Scenario Set

A first conformant Graph implementation MUST pass at least GS-01 through GS-14.

Additional implementation-specific tests MAY be added, but they MUST NOT weaken the reference scenarios.

## 5. Evidence Requirement

A conformance claim MUST be accompanied by evidence identifying:
- scenario executed;
- implementation/version tested;
- expected result;
- actual result;
- pass/fail status;
- relevant observations;
- test execution context.

`CONFORMANCE CLAIM ≠ TEST DEFINITION`

`CONFORMANCE CLAIM = TEST RESULT + EVIDENCE`

## 6. Failure Classification

Failures SHOULD be classified as:

- **CRITICAL** — identity, authority, provenance, evidence separation, traceability or lineage violation;
- **MAJOR** — required semantic behavior missing or inconsistent;
- **MINOR** — non-semantic implementation limitation that does not change the contract.

Critical and major failures block a conformance claim.

## 7. Approval Gate

This document is **PROPOSED FOR HUMAN APPROVAL**.

If approved, the next step is:

**DEC-010 — Graph Reference Test Matrix and Acceptance Criteria**

DEC-010 will map DEC-006 invariants → DEC-008 contracts → DEC-009 scenarios → measurable acceptance criteria and evidence requirements.

## 8. Governing Rule

> **A Graph implementation earns trust by reproducing the project's semantic behavior under test—not by the reputation or capabilities of the technology used to implement it.**
