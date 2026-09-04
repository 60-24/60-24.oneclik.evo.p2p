# DEC-012 — SYSTEM BUILDER GRAPH CANDIDATE EVALUATION MATRIX

**Status:** PROPOSED FOR HUMAN APPROVAL  
**Session:** SES-004  
**Depends on:** DEC-005, DEC-006, DEC-007, DEC-008, DEC-009, DEC-010, DEC-011

## 1. Purpose

This decision defines the reference matrix used to compare candidate Graph implementation approaches after the mandatory semantic gate established by DEC-011.

It does **not** select a technology.

Its purpose is to make candidate comparison explicit, reproducible and resistant to technology-first bias.

## 2. Governing Principle

> **No candidate is a winner because it is popular, fast or convenient. It must first prove semantic eligibility.**

The evaluation order is:

`SEMANTIC ELIGIBILITY → EVIDENCE → ENGINEERING COMPARISON → RECOMMENDATION → HUMAN DECISION`

## 3. Candidate Representation

Candidates SHALL initially be represented by implementation class.

Reference candidate classes:

| ID | Candidate class | Initial question |
|---|---|---|
| GC-01 | Native Graph Database | Does a graph-native model naturally satisfy the semantic contract? |
| GC-02 | Relational Graph Representation | Can relational structures reproduce the required graph semantics without unacceptable complexity? |
| GC-03 | Document-Oriented Representation | Can document structures preserve typed relations, lineage and traceability? |
| GC-04 | Event-Sourced Representation | Can event history serve as a reliable semantic and temporal graph foundation? |
| GC-05 | Embedded / Local Graph | Can a local embedded implementation satisfy semantic and operational requirements? |
| GC-06 | Distributed Graph / State | Can distributed state preserve graph semantics, lineage and authority? |
| GC-07 | Hybrid Architecture | Can multiple technologies be combined without creating semantic ambiguity or hidden authority? |

Concrete products or libraries MUST NOT be ranked before their class has passed the semantic gate.

## 4. Mandatory Semantic Gate

Every candidate SHALL be evaluated against:

`TE-01 Semantic Fidelity`
`TE-02 Invariant Conformance`
`TE-03 Contract Conformance`
`TE-04 Traceability`
`TE-05 Provenance and Lineage`
`TE-06 Authority and State Separation`
`TE-07 Evolution`
`TE-08 Integrity`
`TE-09 Verification and Evidence`
`TE-12 Portability and Technology Independence`

The result for each criterion is:

`PASS | FAIL | PARTIAL | UNKNOWN | BLOCKED | NOT_APPLICABLE`

### Gate rule

A candidate that has any mandatory criterion other than `PASS` is **NOT SEMANTICALLY ELIGIBLE** for final selection.

`PARTIAL ≠ PASS`  
`UNKNOWN ≠ PASS`  
`BLOCKED ≠ PASS`

## 5. Candidate Evaluation Matrix

| Candidate | TE-01 | TE-02 | TE-03 | TE-04 | TE-05 | TE-06 | TE-07 | TE-08 | TE-09 | TE-12 | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GC-01 Native Graph | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GC-02 Relational | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GC-03 Document | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GC-04 Event-Sourced | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GC-05 Embedded/Local | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GC-06 Distributed | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| GC-07 Hybrid | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

`TBD` means **not evaluated**, not PASS.

## 6. Comparative Engineering Matrix

Only candidates that pass the mandatory semantic gate may be compared using:

| Dimension | Evaluation question | Result |
|---|---|---|
| TE-10 Operational Suitability | Deployment, backup, recovery, observability and maintenance | TBD |
| TE-11 Performance and Scale | Expected workload and graph growth | TBD |
| TE-13 Complexity and Maintainability | Operational and cognitive complexity | TBD |
| TE-14 Security and Trust Boundaries | Privacy, integrity, authority and trust boundaries | TBD |
| TE-15 Reversibility / Exit Cost | Migration and preservation of semantic meaning | TBD |

No numerical score may compensate for mandatory semantic failure.

## 7. Evidence Requirements

Every evaluated cell SHOULD link to an Evidence Record containing:

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

Evidence hierarchy:

1. reproducible test result;
2. controlled experiment;
3. verified observed behavior;
4. authoritative technical documentation confirmed by testing where material;
5. prototype evidence;
6. vendor claim — discovery input only, not sufficient proof of conformance.

## 8. Evaluation Procedure

For every candidate:

1. define the exact candidate/version;
2. map candidate capabilities to TE-01 through TE-15;
3. execute applicable reference scenarios GS-01 through GS-14;
4. record evidence;
5. apply the mandatory gate;
6. reject or quarantine candidates that fail the gate;
7. compare surviving candidates on engineering dimensions;
8. document trade-offs;
9. produce recommendation;
10. obtain explicit human architectural approval.

## 9. Anti-Bias Rules

The evaluation MUST NOT:

- start from a preferred product;
- change the semantic contract to fit a candidate;
- interpret missing evidence as success;
- convert benchmark performance into semantic conformance;
- hide limitations inside a composite score;
- treat an implementation's internal terminology as project ontology;
- select a technology solely because it reduces short-term coding effort.

## 10. Required Output Per Candidate

Each candidate evaluation SHALL produce:

- candidate identity and version;
- implementation class;
- semantic capability profile;
- mandatory gate result;
- evidence matrix;
- failed/partial/unknown requirements;
- operational trade-offs;
- complexity profile;
- security/trust implications;
- exit/migration implications;
- recommendation status.

Recommendation statuses:

`ELIGIBLE`
`NOT_ELIGIBLE`
`INSUFFICIENT_EVIDENCE`
`BLOCKED`

## 11. Selection Rule

The final selection MAY be made only from candidates marked:

`ELIGIBLE`

The recommendation is advisory.

The final foundational technology decision remains a human decision.

## 12. Important Non-Decision

DEC-012 does **not** decide:

- which graph technology will be used;
- whether a graph database is ultimately required;
- which vendor/product is preferred;
- whether a hybrid solution is superior;
- implementation architecture;
- deployment topology.

Those questions require evidence generated by the evaluation process.

## 13. Next Step

After approval of DEC-012:

**DEC-013 — Candidate Set Definition & Evaluation Protocol**

DEC-013 will define the concrete candidate set and the controlled procedure for evaluating each candidate against the matrix.

Only then should we begin current, evidence-based technology research and comparison.

## 14. Governing Rule

> **We do not choose the Graph technology. We construct a process in which the technology must prove that it deserves to be chosen.**

## 15. Approval Gate

**PROPOSED FOR HUMAN APPROVAL**
