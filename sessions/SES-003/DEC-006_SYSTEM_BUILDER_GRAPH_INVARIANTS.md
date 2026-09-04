# DEC-006 — SYSTEM BUILDER GRAPH INVARIANTS

**Status:** APPROVED  
**Session:** SES-003  
**Scope:** Semantic invariants of the System Builder Graph

## 1. Purpose

This document defines the properties that the System Builder Graph must preserve regardless of the eventual storage model, database, serialization format, runtime, or implementation technology.

These invariants are semantic constraints, not implementation details.

## 2. Invariant G-01 — Identity

Every meaningful Graph element must have a stable identity sufficient to distinguish it from other elements.

Identity must not depend solely on display name, file path, database position, or presentation order.

## 3. Invariant G-02 — Provenance

Every meaningful derived element must be traceable to the element, decision, observation, or transformation from which it originated.

The Graph must preserve provenance rather than only the latest state.

## 4. Invariant G-03 — Meaning Preservation

A Graph representation must not silently change the semantic meaning of an Intent, Concept, Constraint, Invariant, Contract, Decision, or other constitutional element.

Any intentional semantic change must be represented as an explicit change or supersession.

## 5. Invariant G-04 — Traceability

The Graph must preserve sufficient relationships to trace significant system elements across the lifecycle:

`INTENT → MODEL → DESIGN → CONTRACT → BUILD → VERIFY → EVIDENCE → VALIDATION → OBSERVE → EVOLVE`

Loss of a meaningful trace is a Graph integrity failure unless explicitly accepted and recorded as such.

## 6. Invariant G-05 — Decision Integrity

A decision recorded in the Graph must remain distinguishable from an assumption, proposal, observation, implementation detail, or fact.

The Graph must not silently promote a proposal or assumption into an approved decision.

## 7. Invariant G-06 — Authority Integrity

The Graph must preserve who or what has authority over a decision.

Human constitutional authority must remain distinguishable from AI-generated proposals and autonomous implementation actions.

## 8. Invariant G-07 — Evidence Separation

Claims, tests, observations, evidence, validation, and confidence must remain semantically distinguishable.

The existence of a Claim node, generated artifact, test definition, or relationship is not itself proof of correctness.

Canonical evidence chain:

`CLAIM → TEST / OBSERVATION → EVIDENCE → VALIDATION → CONFIDENCE`

## 9. Invariant G-08 — Temporal Integrity

The Graph must be capable of distinguishing current state from historical state and must not erase meaningful evolution history through silent replacement.

Supersession and change must remain reconstructable.

## 10. Invariant G-09 — Referential Integrity

Relationships must reference valid Graph elements and must preserve their declared semantic type.

An orphaned relationship or relationship whose meaning has been silently changed is a Graph integrity failure.

## 11. Invariant G-10 — Bidirectional Reconstruction

The Graph must support reconstruction in both directions where the required relationships exist:

Forward:
`Intent → Design → Contract → Implementation → Verification → Evidence`

Reverse:
`Implementation → Contract → Design → Intent`

This does not require every node to have a complete path in both directions, but it requires the Graph model to preserve such traceability where applicable.

## 12. Invariant G-11 — No Silent Mutation

No constitutional, ontological, contractual, or otherwise materially significant Graph meaning may be changed silently.

Material change requires an explicit change record and, where required by authority boundaries, human approval.

## 13. Invariant G-12 — Separation of Proposal and Reality

A proposed state, predicted state, generated artifact, simulated result, or AI assertion must remain distinguishable from an observed and validated state.

The Graph must never collapse these categories into a single undifferentiated truth state.

## 14. Invariant G-13 — Constraint Visibility

Constraints and invariants that materially affect a system element must be representable and traceable through the Graph.

A system element must not appear unconstrained when a relevant constraint exists.

## 15. Invariant G-14 — Evolution Without Loss of Lineage

Evolution may add, modify, supersede, or remove elements, but must preserve enough lineage to determine what changed, why it changed, what authorized it, and what evidence supports the resulting state.

## 16. Invariant G-15 — Technology Independence

The invariants must remain valid regardless of whether the eventual implementation uses a graph database, relational database, document store, event store, CRDT-based representation, RDF, or another technology.

Technology must implement the semantic invariants; the invariants must not be defined by technology limitations.

## 17. Invariant G-16 — No Authority by Existence

An element does not become authoritative merely because it exists in the Graph.

Authority is an explicit semantic property derived from the project's governance and decision model.

## 18. Minimum Integrity Rule

At minimum, a conforming Graph must preserve:

`IDENTITY + PROVENANCE + MEANING + TRACEABILITY + AUTHORITY + EVIDENCE + TIME + LINEAGE`

If any of these are materially lost, System Builder must treat the affected Graph state as degraded or invalid rather than silently continuing as if nothing changed.

## 19. Relationship to Previous Decisions

This decision operationalizes DEC-005, which established the Graph as the structural backbone of System Builder.

It does not select a concrete implementation technology.

## 20. Approval Gate

This decision is approved by the human project authority for progression to the next design step.

The next action is to derive the **minimal Graph semantic model and contracts** from these invariants.

No implementation technology should be selected before that step unless a separate decision explicitly authorizes it.
