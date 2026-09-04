# G-01 — NEO4J CANDIDATE PROFILE AND SEMANTIC MAPPING

**Session:** SES-004  
**Candidate:** G-01  
**Class:** Native Graph Database  
**Status:** EVALUATION IN PROGRESS  
**Depends on:** DEC-011, DEC-012, DEC-013, DEC-014, DEC-015  

---

## 1. Purpose

This document begins the controlled evaluation of **Neo4j** as representative of the Native Graph Database class.

It is a candidate profile and semantic mapping, **not a technology recommendation**.

---

## 2. Current Technology Reference

The current Neo4j documentation identifies Neo4j as a property-graph database using Cypher. The current documentation states that Neo4j 2026.07.1 is the latest release listed by its Operations Manual, and the supported-versions page lists 2026.07.1 with a release date of August 5, 2026. citeturn0search1turn0search14turn0search2

Neo4j provides native nodes, relationships and graph traversal/querying through Cypher. It supports ACID transactions, and constraints can enforce uniqueness, existence, property types and keys. citeturn0search9turn0search3

Neo4j 2026.02 introduced graph types in Cypher 25 for Enterprise Edition, and graph types are generally available from 2026.06. Graph types allow an open schema over nodes, relationships and properties. citeturn0search4turn0search6

The licensing model must remain an explicit evaluation dimension: Neo4j documents Community Edition as GPLv3 and Enterprise Edition as commercially licensed. citeturn0search8turn0search10

These are **documented capabilities only**. None is yet a System Builder conformance result.

---

## 3. Architectural Profile

### Native semantic primitives

Neo4j directly represents:

- nodes;
- relationships;
- relationship direction;
- labels / types;
- properties;
- paths;
- graph queries;
- transactional updates.

This makes G-01 a strong candidate for testing whether a native property-graph substrate can express the System Builder Graph contract with relatively little semantic translation.

### Schema / integrity mechanisms

Neo4j supports constraints for uniqueness, existence, property types and keys. Current Enterprise graph types provide a broader open-schema mechanism. citeturn0search3turn0search4

The evaluation must determine which System Builder invariants can be enforced natively and which would remain application-level rules.

### Transaction model

Neo4j documents Cypher updates as transactional, with failed updates rolled back rather than partially persisted. citeturn0search9

This is relevant to Graph integrity but does not itself establish conformance with System Builder invariants.

---

## 4. Preliminary Semantic Mapping

| System Builder Graph Concept | Neo4j Mapping | Initial Assessment | Verification Required |
|---|---|---|---|
| Node | Neo4j node | Direct | Identity and lifecycle test |
| Relationship | Neo4j relationship | Direct | Direction, typing and lifecycle tests |
| Relationship direction | Directed relationship | Direct | Bidirectional/causal interpretation test |
| Node/relationship properties | Properties | Direct | Type and mandatory-property tests |
| Graph traversal | Cypher pattern/path queries | Direct | Conformance scenarios |
| Graph invariants | Constraints + Cypher/application rules | Partial pending test | Determine native vs external enforcement |
| Semantic contract | Graph types/constraints + application layer | Partial pending test | Contract-conformance suite |
| Provenance / lineage | Properties / connected provenance nodes / application model | Not yet established | Dedicated provenance test |
| Authority vs derived state | Application/domain modeling | Not native by default | Authority-boundary test |
| Temporal history | Modeling / transaction mechanisms / external event layer | Not established as equivalent | Temporal reconstruction test |
| Controlled evolution | Schema/graph types + migrations | Partial pending test | Evolution test |
| Reproducible verification | Queries + constraints + external test harness | Plausible | Evidence reproducibility test |
| Local deployment | Docker / self-hosted deployment | Supported | Operational reproducibility test |
| Technology independence | Requires System Builder abstraction | External concern | Portability / exit test |

**Important:** “Direct” means the conceptual primitive has a natural representation. It does **not** mean System Builder conformance has been proven.

---

## 5. Mandatory Evaluation Questions

The detailed G-01 evaluation SHALL answer at least:

1. Can every required System Builder node and relationship invariant be represented without semantic distortion?
2. Which invariants can Neo4j enforce natively?
3. Which invariants require Cypher procedures, application logic or a dedicated System Builder layer?
4. Can provenance and lineage remain first-class and auditable?
5. Can authority state be separated reliably from derived state?
6. Can graph evolution occur without silently changing historical meaning?
7. Can the same conformance tests be executed reproducibly?
8. Can the System Builder Graph remain portable if Neo4j is later replaced?
9. What capabilities are edition-dependent?
10. What licensing or operational constraints could create unacceptable architectural coupling?

---

## 6. Preliminary Gate Position

No TE criterion is marked PASS solely from documentation.

Current evidence classification:

| Criterion | Current State | Reason |
|---|---|---|
| TE-01 Semantic Fidelity | UNKNOWN | Mapping exists; conformance not tested. |
| TE-02 Invariant Conformance | UNKNOWN | Native constraints identified; System Builder invariants not tested. |
| TE-03 Contract Conformance | UNKNOWN | Contract test suite not executed. |
| TE-04 Traceability | UNKNOWN | Evidence chain not yet demonstrated. |
| TE-05 Provenance and Lineage | UNKNOWN | No dedicated test yet. |
| TE-06 Authority and State Separation | UNKNOWN | Requires domain-level evaluation. |
| TE-07 Evolution | UNKNOWN | Requires controlled evolution scenarios. |
| TE-08 Integrity | UNKNOWN | Transaction and constraint capabilities documented, but System Builder integrity not verified. |
| TE-09 Verification and Evidence | UNKNOWN | Formal evidence package not yet produced. |
| TE-12 Portability and Technology Independence | UNKNOWN | Requires exit/abstraction testing. |

Therefore:

> **G-01 is not yet eligible for the final architecture.**

This is an evaluation state, not a negative judgment.

---

## 7. Evidence References

Primary sources used for this profile:

- Neo4j Cypher Manual — introduction and property-graph model. citeturn0search1
- Neo4j Cypher Manual — constraints. citeturn0search3
- Neo4j Cypher Manual — graph types. citeturn0search4turn0search6
- Neo4j Cypher Manual — transactions and editions. citeturn0search9
- Neo4j Operations Manual — current release information. citeturn0search14turn0search2
- Neo4j official pricing/licensing information. citeturn0search8turn0search10

---

## 8. Next Controlled Step

The next step is **not** to select Neo4j.

The next step is to execute the approved System Builder Graph conformance scenarios against G-01 and create evidence records for each mandatory criterion.

> **Documentation establishes capability. Testing establishes observation. Conformance evidence establishes architectural eligibility.**
