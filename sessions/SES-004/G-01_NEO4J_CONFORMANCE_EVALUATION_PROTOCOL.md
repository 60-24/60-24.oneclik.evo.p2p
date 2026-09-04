# G-01 — NEO4J CONFORMANCE EVALUATION PROTOCOL

**Status:** PROPOSED FOR EXECUTION
**Session:** SES-004
**Candidate:** G-01 — Neo4j
**Depends on:** DEC-008, DEC-009, DEC-010, DEC-015, G-01 candidate profile

## 1. Purpose

This protocol defines the controlled execution of the System Builder Graph reference conformance scenarios against Neo4j.

It does not select Neo4j as the project Graph technology and does not authorize production implementation.

## 2. Governing Principle

> The candidate is evaluated against the frozen semantic contract; the contract is not modified to accommodate the candidate.

## 3. Test Scope

Mandatory reference scenarios:

- GS-01 — Unique Node Identity
- GS-02 — Typed Edge
- GS-03 — Invalid Reference
- GS-04 — Derived Artifact Provenance
- GS-05 — Proposal Does Not Become Approval
- GS-06 — Claim Does Not Become Evidence
- GS-07 — Evidence Does Not Equal Validation
- GS-08 — Historical State Preservation
- GS-09 — Forward Trace
- GS-10 — Reverse Trace
- GS-11 — Constraint Visibility
- GS-12 — Explicit Material Change
- GS-13 — Supersession
- GS-14 — Technology-Neutral Reproduction

DEC-009 requires GS-01 through GS-14 for a first conformant Graph implementation.

## 4. Acceptance Mapping

| Acceptance | Scenario | Requirement |
|---|---|---|
| AC-01 | GS-01 | Unique, stable identities |
| AC-02 | GS-02 | Typed relations and correct endpoints |
| AC-03 | GS-03 | Referential integrity |
| AC-04 | GS-04 | Reconstructable provenance |
| AC-05 | GS-05 | Authority/state separation |
| AC-06 | GS-06, GS-07 | Claim/evidence/validation separation |
| AC-07 | GS-08 | Temporal lineage |
| AC-08 | GS-09 | Forward traceability |
| AC-09 | GS-10 | Reverse traceability |
| AC-10 | GS-11 | Constraint visibility |
| AC-11 | GS-12 | Explicit material change |
| AC-12 | GS-13 | Supersession and governing status |
| AC-13 | GS-14 | Technology independence |

## 5. Execution Environment

Before execution, record:

- Neo4j exact version;
- edition;
- deployment method;
- operating environment;
- Cypher version where relevant;
- configuration relevant to test behavior;
- test harness version/commit;
- clean database state or documented fixture state.

No result is valid without an identified implementation/version and test context.

## 6. Test Discipline

Each scenario MUST follow:

1. establish GIVEN state;
2. execute WHEN action;
3. observe actual state;
4. execute THEN verification;
5. record expected result;
6. record actual result;
7. assign PASS / FAIL / BLOCKED / NOT_APPLICABLE;
8. retain reproducible evidence.

No undocumented behavior may be treated as proof.

## 7. Evidence Record

For every scenario record:

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

Additional evidence SHOULD include the exact test commands/queries, relevant output, fixture identifiers, and timestamps.

## 8. Special Evaluation Rules

### Authority and state

Storage of a Proposal, Claim or Evidence MUST NOT itself create approval, validation or authority.

### Provenance and lineage

Where the semantic contract requires origin or historical reconstruction, the test must demonstrate that reconstruction—not merely the existence of current properties.

### Referential integrity

An implementation that permits an invalid reference may only pass if the violation is explicitly exposed according to the semantic contract. Silent acceptance fails GS-03.

### Technology independence

GS-14 is not a claim that Neo4j alone can prove technology independence. It establishes whether the same semantic scenario can produce equivalent results across candidates. The G-01 result must therefore be recorded without prematurely declaring cross-candidate equivalence.

## 9. Result Gate

The G-01 candidate cannot be declared CONFORMANT unless every mandatory acceptance item is PASS and no critical or major semantic failure remains unresolved.

Any unresolved BLOCKED item prevents a full conformance claim.

## 10. No Premature Architecture Decision

Even a full PASS does not select Neo4j.

The result becomes evidence for the later comparative evaluation of G-01 against G-02 through G-07.

## 11. Execution State

Current state:

`PROTOCOL DEFINED → EXECUTION NOT YET PERFORMED`

Therefore no GS or AC result is currently claimed.

## 12. Next Step

Execute the protocol against the identified Neo4j environment, beginning with GS-01 and progressing sequentially through GS-14, recording evidence after each scenario.
