# G-01 — Neo4j Reproducible Runtime Setup

**Status:** PREPARED FOR EXECUTION
**Candidate:** G-01 — Neo4j
**Evaluation phase:** System Builder Graph candidate conformance
**Scope:** Evaluation only — not production architecture and not technology selection.

## 1. Purpose

Define the smallest reproducible runtime setup required to execute GS-01–GS-14 against Neo4j without changing the System Builder Graph semantic contract.

## 2. Existing Repository Context

The repository already contains a Dev Container based on Ubuntu with Go, Rust, Python and Node.js features. It does not currently provide a Neo4j runtime or a Docker Compose definition for the G-01 evaluation.

The runtime setup therefore remains isolated to the G-01 evaluation and must not modify the project's production architecture.

## 3. Required Runtime

The execution environment MUST provide:

- Neo4j Community or Enterprise edition explicitly recorded;
- an exact Neo4j version, never a moving `latest` tag;
- a reproducible deployment method;
- an isolated clean database for the evaluation;
- Cypher execution with observable query results and errors;
- a deterministic reset/recreation mechanism between scenarios where required;
- persistent evidence capture.

For the initial reproducible reference environment, the Neo4j version SHALL be pinned explicitly when the runtime package is instantiated. The chosen version must be recorded in the execution evidence before GS-01 starts.

## 4. Recommended Evaluation Mechanism

Use an isolated containerized Neo4j runtime as the reference execution mechanism, provided the executing machine has a compatible container runtime.

Minimum structure:

```text
G-01 evaluation
├── pinned Neo4j runtime
├── isolated evaluation database
├── scenario execution procedure
├── evidence directory
└── recorded environment metadata
```

No production application code is required for GS-01–GS-14 at this stage.

## 5. Environment Metadata

Before GS-01, record:

- `NEO4J_VERSION`
- `NEO4J_EDITION`
- deployment method
- container image/package identifier
- host OS/environment
- container runtime and version
- Cypher version where relevant
- relevant Neo4j configuration
- database name
- fixture/reset method
- test procedure or harness version/commit

## 6. Reproducibility Rules

1. Do not use `latest`.
2. Do not rely on undocumented defaults when they affect a scenario.
3. Start from a clean or deterministically reset database.
4. Keep runtime configuration under version control when practical.
5. Record every version needed to reproduce the observation.
6. Preserve scenario evidence separately from explanatory documentation.
7. A runtime failure is `BLOCKED`, not `PASS`.
8. Documentation of capability is not evidence of conformance.

## 7. Execution Gate

GS-01 may begin only after all of the following are true:

- exact Neo4j version recorded;
- edition recorded;
- deployment method recorded;
- runtime starts successfully;
- isolated database is available;
- Cypher execution is observable;
- reset/recreation is verified;
- evidence location is established.

## 8. Relationship to Existing Documents

This setup implements the execution requirement defined by:

- `DEC-008` — Graph contract;
- `DEC-009` — conformance scenarios GS-01–GS-14;
- `DEC-010` — reference test matrix and acceptance criteria;
- `DEC-011` — technology evaluation framework;
- `DEC-013` — candidate evaluation protocol;
- `DEC-014` — candidate class registry;
- `DEC-015` — concrete candidate registry;
- `G-01_NEO4J_CANDIDATE_PROFILE_AND_SEMANTIC_MAPPING.md`;
- `G-01_NEO4J_CONFORMANCE_EVALUATION_PROTOCOL.md`;
- `G-01_NEO4J_TEST_ENVIRONMENT_SPECIFICATION.md`.

## 9. Current State

```text
SEMANTIC CONTRACT        ✅
CANDIDATE ADMITTED       ✅
PROFILE                  ✅
CONFORMANCE PROTOCOL     ✅
TEST ENVIRONMENT SPEC    ✅
RUNTIME SETUP DEFINED    ✅
LOCAL RUNTIME AVAILABLE  ❌
GS-01                    BLOCKED
```

## 10. Next Controlled Step

Instantiate the pinned container runtime on an execution host that supports it, verify the environment gate, and only then execute GS-01.

No GS-02 or later scenario is authorized until GS-01 has a complete evidence record.

**Governing rule:** We do not convert inability to execute into a PASS. We obtain reproducible runtime evidence first.
