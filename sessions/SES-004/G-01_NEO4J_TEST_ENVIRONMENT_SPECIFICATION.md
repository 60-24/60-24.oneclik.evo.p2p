# G-01 — Neo4j Test Environment Specification

**Session:** SES-004  
**Candidate:** G-01 — Neo4j  
**Status:** PROPOSED FOR EXECUTION  
**Purpose:** Define the minimum reproducible environment required to execute GS-01–GS-14.

## 1. Scope

This environment exists exclusively for conformance evaluation of Neo4j against the System Builder Graph semantic contract. It is not a production architecture and does not constitute technology selection.

## 2. Required Environment

The evaluation environment MUST provide:

- a reproducible Neo4j deployment;
- an explicitly recorded Neo4j version;
- edition explicitly recorded (Community or Enterprise);
- deployment method explicitly recorded (container, local installation, or equivalent);
- isolated, clean database state for each scenario or a documented reset procedure;
- access to execute Cypher statements and inspect results/errors;
- a documented test harness or manual execution procedure;
- persistent evidence of each scenario's expected and observed result.

## 3. Version Pinning

The exact Neo4j version MUST be pinned before GS-01 execution. A moving `latest` tag or equivalent is not acceptable evidence.

Record:

- Neo4j version
- edition
- Cypher version where relevant
- deployment image/package identifier
- operating environment
- relevant configuration
- test harness version/commit

## 4. Isolation

Tests MUST run against an isolated evaluation database. Existing project data MUST NOT be used as implicit test state.

Each scenario MUST either:

1. start from a clean database, or
2. use a deterministic fixture and reset procedure documented in the evidence.

## 5. Evidence

For every GS scenario record:

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

Allowed status values are those defined by DEC-010: `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`.

## 6. Execution Discipline

The execution sequence is:

`ENVIRONMENT VERIFICATION → GS-01 → EVIDENCE → GS-02 → ... → GS-14`

No scenario may be marked PASS solely from product documentation. Observed behavior is required.

A failure or blocked scenario MUST remain visible and MUST NOT be suppressed to obtain a composite result.

## 7. GS-01 Minimum Requirement

GS-01 may begin only after the environment record contains the exact Neo4j version, edition, deployment method, isolated database state, and execution method.

GS-01 tests whether the implementation can preserve unique node identity according to the System Builder Graph contract. The test MUST be derived from DEC-009 and evaluated against the acceptance criterion AC-01 in DEC-010.

## 8. Exit Condition

The environment is considered ready when all mandatory environment fields are recorded and the evaluator can execute and observe a controlled Neo4j operation.

Only then may GS-01 be executed.

## 9. Current State

`ENVIRONMENT SPECIFICATION DEFINED → RUNTIME VERIFICATION PENDING → GS-01 NOT YET EXECUTED`

**Governing rule:** No evidence is fabricated. If the required runtime cannot be established, the relevant evaluation state is `BLOCKED`.
