# DEC-011 — SYSTEM BUILDER GRAPH TECHNOLOGY EVALUATION FRAMEWORK

**Status:** PROPOSED FOR HUMAN APPROVAL  
**Session:** SES-004  
**Depends on:** DEC-005, DEC-006, DEC-007, DEC-008, DEC-009, DEC-010

## 1. Purpose

This decision establishes a technology-independent framework for evaluating candidate Graph implementation approaches for System Builder.

The purpose is **not** to select a technology yet.

The purpose is to define a fair evaluation method so that candidate technologies are measured against the already-established semantic contract, invariants and acceptance criteria.

## 2. Governing Principle

> **Technology implements meaning. Technology does not define meaning.**

A candidate implementation must adapt to the project's semantic requirements. The semantic contract MUST NOT be weakened merely because a technology represents a requirement differently or cannot represent it naturally.

## 3. Evaluation Boundary

The evaluation target is:

`SEMANTIC CONTRACT → IMPLEMENTATION CAPABILITY → CONFORMANCE EVIDENCE`

The following are outside the primary technology-selection criterion:

- popularity;
- marketing claims;
- vendor preference;
- familiarity alone;
- benchmark performance without semantic relevance;
- preference for a specific database model before requirements are evaluated.

## 4. Candidate Classes

Candidate implementations may belong to different technical classes, including but not limited to:

1. native graph database;
2. relational representation;
3. document-oriented representation;
4. event-sourced representation;
5. embedded/local graph implementation;
6. distributed graph/state representation;
7. hybrid architecture.

A candidate is evaluated as an **implementation approach**, not merely as a product name.

## 5. Evaluation Dimensions

Each candidate SHALL be evaluated across the following dimensions.

### TE-01 — Semantic Fidelity

Can the implementation represent the required Node, Edge, type, state and semantic metadata without loss of meaning?

### TE-02 — Invariant Conformance

Can all mandatory Graph invariants G-01 through G-16 be represented and enforced or demonstrably validated?

### TE-03 — Contract Conformance

Can the implementation satisfy the semantic contracts defined by DEC-007 and the reference tests defined by DEC-008?

### TE-04 — Traceability

Can forward and reverse traceability be reconstructed reliably?

### TE-05 — Provenance and Lineage

Can origin, transformation, version and historical lineage be retained and reconstructed?

### TE-06 — Authority and State Separation

Can proposal, approval, claim, evidence, validation and reality remain semantically distinct?

### TE-07 — Evolution

Can the system preserve history while supporting explicit change and supersession?

### TE-08 — Integrity

Can identity, referential integrity and typed relations be protected or reliably detected when violated?

### TE-09 — Verification and Evidence

Can implementation behavior produce reproducible evidence suitable for audit and conformance testing?

### TE-10 — Operational Suitability

Can the implementation meet relevant requirements for deployment, backup, recovery, observability, maintenance and failure handling?

### TE-11 — Performance and Scale

Can the implementation support the expected workload and graph growth without compromising semantic guarantees?

Performance is secondary to mandatory semantic conformance.

### TE-12 — Portability and Technology Independence

Can the semantic model remain portable and understandable independently of the selected implementation technology?

### TE-13 — Complexity and Maintainability

What operational, architectural and cognitive complexity does the candidate introduce?

### TE-14 — Security and Trust Boundaries

Can the implementation preserve the project's authority, privacy, integrity and trust boundaries without introducing hidden authority mechanisms?

### TE-15 — Reversibility / Exit Cost

Can the project migrate away from the technology without losing semantic meaning, provenance or lineage?

## 6. Mandatory vs Comparative Criteria

Evaluation criteria are divided into two classes.

### Mandatory Gate

A candidate cannot be selected if it fails a mandatory semantic requirement.

Mandatory criteria include:

`TE-01, TE-02, TE-03, TE-04, TE-05, TE-06, TE-07, TE-08, TE-09, TE-12`

### Comparative Criteria

Among candidates that pass the mandatory gate, the following may be compared quantitatively or qualitatively:

`TE-10, TE-11, TE-13, TE-14, TE-15`

No comparative advantage can compensate for failure of a mandatory criterion.

## 7. Evidence Model

Every material evaluation claim SHOULD have an evidence record containing:

`CANDIDATE`
`CRITERION`
`VERSION`
`TEST_REFERENCE`
`EXPECTED`
`OBSERVED`
`STATUS`
`EVIDENCE_REFERENCE`
`LIMITATIONS`
`CONFIDENCE`

Evidence may include:

- executable tests;
- controlled experiments;
- documentation verified against observed behavior;
- reproducible prototypes;
- failure tests;
- migration tests;
- performance measurements.

Marketing statements alone are not sufficient evidence for conformance.

## 8. Evaluation States

Each criterion SHALL use:

- `PASS` — requirement demonstrated;
- `FAIL` — requirement not satisfied;
- `PARTIAL` — some capability demonstrated but material limitations remain;
- `UNKNOWN` — insufficient evidence;
- `BLOCKED` — valid evaluation could not be executed;
- `NOT_APPLICABLE` — explicitly justified.

For mandatory criteria:

`PASS` is required.

`PARTIAL`, `UNKNOWN` or `BLOCKED` MUST NOT be interpreted as conformance.

## 9. Scoring Rule

A numerical score MAY be used only after the mandatory gate is applied.

Recommended order:

1. eliminate candidates failing mandatory semantic requirements;
2. record evidence and limitations;
3. compare surviving candidates on operational and economic dimensions;
4. identify trade-offs explicitly;
5. produce a recommendation;
6. obtain human approval before technology selection.

A single composite score MUST NOT hide a mandatory semantic failure.

## 10. Technology-Neutral Test Harness

Where practical, the evaluation SHALL use a common reference test suite derived from:

`DEC-008 → DEC-009 → DEC-010`

The same semantic scenarios SHOULD be applied to every candidate.

Technology-specific adapters MAY exist, but they MUST NOT change the semantic expectation of the test.

## 11. Anti-Bias Rules

The evaluation MUST avoid:

- choosing a technology first and redefining requirements afterward;
- treating implementation convenience as semantic correctness;
- accepting undocumented behavior as proof;
- confusing API availability with semantic conformance;
- rewarding complexity merely because it provides more features;
- using benchmark results unrelated to project workloads;
- allowing a technology vendor's terminology to silently redefine project concepts.

## 12. Decision Output

The evaluation of each candidate SHALL produce:

1. capability profile;
2. mandatory-gate result;
3. evidence matrix;
4. known limitations;
5. operational trade-offs;
6. migration/exit implications;
7. recommendation or rejection rationale.

The final technology choice remains a **human architectural decision**.

## 13. Human Authority

System Builder may:

- discover candidates;
- construct evaluation matrices;
- execute approved tests;
- collect evidence;
- identify trade-offs;
- propose a recommendation.

System Builder MUST NOT silently make the final foundational technology decision.

## 14. Next Step

After approval of DEC-011, the next artifact should be:

**DEC-012 — Graph Candidate Evaluation Matrix**

DEC-012 will instantiate this framework without prematurely selecting a winner.

The first candidates should be represented as **technology classes**, followed by concrete technologies only when justified by the evidence.

## 15. Governing Rule

> **First prove semantic eligibility. Then compare engineering trade-offs. Only then choose technology.**
