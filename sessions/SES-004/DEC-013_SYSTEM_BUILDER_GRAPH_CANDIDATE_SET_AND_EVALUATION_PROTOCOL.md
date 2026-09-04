# DEC-013 — SYSTEM BUILDER GRAPH CANDIDATE SET & EVALUATION PROTOCOL

**Status:** PROPOSED FOR HUMAN APPROVAL  
**Session:** SES-004  
**Depends on:** DEC-005, DEC-006, DEC-007, DEC-008, DEC-009, DEC-010, DEC-011, DEC-012

## 1. Purpose

This decision defines how Graph implementation candidates will be selected for evaluation and how each candidate will be evaluated under a common, technology-independent protocol.

DEC-013 does **not** select the final Graph technology.

## 2. Governing Principle

> **We select candidates for evidence, not technologies for preference.**

The candidate set must be broad enough to avoid premature architectural lock-in and small enough to permit meaningful, reproducible evaluation.

## 3. Candidate Representation

Candidates SHALL first be represented as implementation classes. A concrete product or project may be introduced only when it is a credible representative of a relevant class and sufficient evidence can be obtained.

Initial candidate classes:

1. Native Graph Database
2. Relational Graph Representation
3. Document-Oriented Graph Representation
4. Event-Sourced Graph Representation
5. Embedded / Local Graph
6. Distributed Graph / State Representation
7. Hybrid Graph Architecture

No class is presumed to be the winner.

## 4. Candidate Admission Criteria

A concrete candidate may enter evaluation only if:

- its architecture can be documented;
- its relevant version can be identified;
- the project can execute or otherwise verify meaningful tests;
- its data and relation semantics can be mapped to the System Builder contract;
- evidence can be reproduced or independently inspected;
- known licensing or operational constraints can be recorded.

A candidate that cannot be meaningfully evaluated is marked `BLOCKED` or excluded with an explicit reason; it is never silently treated as `PASS`.

## 5. Evaluation Sequence

Every admitted candidate SHALL follow the same sequence:

`CANDIDATE IDENTIFICATION → CAPABILITY PROFILE → SEMANTIC MAPPING → MANDATORY TESTS → EVIDENCE REVIEW → GATE DECISION → COMPARATIVE EVALUATION → RECOMMENDATION`

Technology-specific adapters may be used, but semantic expectations remain unchanged.

## 6. Mandatory Gate

The candidate must demonstrate all mandatory dimensions defined by DEC-011:

`TE-01, TE-02, TE-03, TE-04, TE-05, TE-06, TE-07, TE-08, TE-09, TE-12`

A mandatory failure means the candidate is **not eligible for final selection**, regardless of performance, popularity, cost or implementation convenience.

## 7. Required Evidence Package

For every evaluated candidate, record:

- candidate and exact version;
- implementation architecture;
- semantic mapping;
- test references;
- expected behavior;
- observed behavior;
- status;
- evidence references;
- limitations;
- confidence;
- reproducibility notes;
- migration/exit implications.

Documentation claims must be distinguished from behavior demonstrated by testing.

## 8. Test Discipline

The evaluation SHALL distinguish:

`DOCUMENTED CAPABILITY ≠ OBSERVED CAPABILITY ≠ VERIFIED CONFORMANCE`

A feature being available in documentation is not proof that the System Builder contract is satisfied.

Failure tests are mandatory wherever an invariant or contract requires rejection or detection of invalid state.

## 9. Comparative Evaluation

Only candidates passing the mandatory gate may be compared on:

- operational suitability;
- performance and scale;
- complexity and maintainability;
- security and trust boundaries;
- reversibility / exit cost;
- relevant economic or infrastructure implications.

Numerical scoring is optional and must never conceal a mandatory failure.

## 10. Fairness Rules

All candidates SHALL receive, as far as technically practical:

- the same semantic scenarios;
- the same acceptance expectations;
- equivalent evidence requirements;
- equivalent scrutiny of failure cases;
- explicit recording of limitations.

Differences caused by the implementation model must be documented rather than silently normalized away.

## 11. Decision States

Candidate-level outcome:

- `ELIGIBLE` — mandatory gate passed;
- `INELIGIBLE` — mandatory criterion failed;
- `BLOCKED` — valid evaluation could not be completed;
- `DEFERRED` — candidate retained for later evidence.

`BLOCKED` and `DEFERRED` are not equivalent to eligibility.

## 12. Human Approval Gates

Human approval is required before:

1. changing the candidate classes;
2. promoting a concrete technology into the official candidate set;
3. changing mandatory evaluation criteria;
4. declaring a candidate eligible for final selection;
5. selecting the foundational Graph technology.

System Builder may prepare evidence and recommendations but does not possess final authority.

## 13. Expected Output

DEC-013 evaluation work SHALL produce:

`Candidate Registry + Evaluation Matrix + Evidence Records + Gate Results + Trade-off Analysis + Recommendation`

The final selection shall be recorded separately as an explicit architectural decision.

## 14. Next Step

After approval of DEC-013, the next operational artifact is:

**Candidate Registry / Evaluation Set**

followed by evidence-backed evaluation of the selected candidates.

No implementation coding is authorized by DEC-013 alone.

## 15. Governing Rule

> **Same contract. Same tests. Same evidence discipline. Different technologies. Human chooses.**
