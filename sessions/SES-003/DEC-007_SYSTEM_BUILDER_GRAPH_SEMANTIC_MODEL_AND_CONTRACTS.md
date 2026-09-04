# DEC-007 — SYSTEM BUILDER GRAPH SEMANTIC MODEL AND CONTRACTS

**Status:** PROPOSED FOR HUMAN APPROVAL  
**Session:** SES-003  
**Previous decisions:** DEC-005, DEC-006

## 1. Purpose

This decision defines the minimal semantic model of the System Builder Graph and the contracts that every conforming representation must satisfy.

It defines meaning, not storage technology.

## 2. Core Graph Model

The minimal Graph consists of two fundamental elements:

```text
NODE  — something that has identity and semantic meaning
EDGE  — a typed relationship between two nodes
```

A Graph state is therefore:

`GRAPH = NODES + TYPED EDGES + SEMANTIC METADATA`

## 3. Minimal Node Contract

Every meaningful Node MUST provide or be derivable with:

- `id` — stable identity;
- `type` — semantic class;
- `state` — lifecycle/semantic state where applicable;
- `provenance` — origin or derivation information;
- `authority` — authority status where applicable;
- `temporal metadata` — creation/change/version information where applicable;
- `content/reference` — the meaning or reference represented by the node.

A display name is not a sufficient identity.

## 4. Minimal Node Classes

The semantic classes are grouped into five domains.

### Meaning
- `Intent`
- `Concept`
- `Entity`
- `Relation`

### Decision
- `Decision`
- `Constraint`
- `Invariant`
- `Assumption`

### System
- `Component`
- `Interface`
- `Contract`
- `Artifact`

### Evidence
- `Claim`
- `Test`
- `Observation`
- `Evidence`
- `Validation`

### Evolution
- `Change`
- `Proposal`
- `Version`
- `Event`

These classes are the minimum semantic vocabulary for System Builder. They are extensible, but extensions must not redefine the meaning of the core classes silently.

## 5. Minimal Edge Contract

Every meaningful Edge MUST identify:

- source Node;
- target Node;
- relation type;
- provenance/context where required;
- temporal validity where required.

An Edge is not merely a database pointer. Its relation type carries semantic meaning.

## 6. Canonical Relation Vocabulary

The minimum relation vocabulary is:

- `DERIVED_FROM`
- `DEPENDS_ON`
- `CONSTRAINED_BY`
- `IMPLEMENTS`
- `SATISFIES`
- `VERIFIED_BY`
- `SUPPORTED_BY`
- `OBSERVED_BY`
- `CHANGED_BY`
- `PROPOSES`
- `SUPERSEDES`

Additional relations may be introduced only when their semantic distinction is necessary and documented.

## 7. State Semantics

Graph elements must distinguish at least the following semantic states where applicable:

- `PROPOSED`
- `APPROVED`
- `ACTIVE`
- `OBSERVED`
- `VALIDATED`
- `SUPERSEDED`
- `REJECTED`
- `DEPRECATED`

State is not authority. In particular, existence or `ACTIVE` state must not by itself imply constitutional authority.

## 8. Authority Contract

Authority must be explicit and distinguish at least:

- human/constitutional authority;
- approved project decision;
- delegated/system authority;
- AI proposal or action;
- unapproved or unknown status.

An AI-generated proposal must never become an approved decision merely because it is stored in the Graph.

## 9. Provenance Contract

For every derived or transformed element, the Graph must preserve enough provenance to answer:

- what produced it;
- from what source;
- by which transformation or decision;
- when it occurred;
- under which relevant version/context.

This directly implements G-02 and G-14.

## 10. Evidence Contract

Evidence semantics remain explicitly separated:

```text
CLAIM
  ↓
TEST / OBSERVATION
  ↓
EVIDENCE
  ↓
VALIDATION
  ↓
CONFIDENCE
```

A `Claim`, `Test`, `Observation`, `Evidence` or `Validation` node is not automatically proof merely because it exists.

## 11. Change Contract

A material change MUST be representable as an explicit change relationship or change record.

At minimum the change model must preserve:

`WHAT CHANGED → WHY → AUTHORITY → WHEN → PREVIOUS STATE → RESULTING STATE → EVIDENCE`

Supersession must preserve lineage rather than erase the previous semantic state.

## 12. Traceability Contract

The Graph must support the canonical lifecycle path:

`Intent → Model → Design → Contract → Build → Verify → Evidence → Validation → Observe → Evolve`

It must also support reverse impact analysis:

`Artifact/Component → Contract → Design → Intent`

The exact path may be incomplete for legitimate cases, but the semantic model must not prevent reconstruction where the necessary relations exist.

## 13. Contract of Meaning

A Node or Edge type is a semantic contract.

Therefore:

1. its meaning must be explicitly defined;
2. its identity must remain stable;
3. its relations must have declared semantics;
4. changes of meaning require explicit version/change handling;
5. implementation limitations must not redefine the semantics.

## 14. Minimal Conformance Test

A future Graph implementation is conforming only if it can demonstrate, without relying on hidden application knowledge, that it can:

1. uniquely identify meaningful nodes;
2. preserve typed relations;
3. preserve provenance;
4. distinguish proposal from approval;
5. distinguish claim from evidence and validation;
6. preserve historical lineage;
7. reconstruct significant forward and reverse traces;
8. represent material change explicitly;
9. detect or expose invalid references;
10. remain independent of a specific storage technology.

## 15. Technology Boundary

This decision intentionally does NOT select a graph database, relational database, RDF model, JSON format, CRDT implementation, event store, programming language or runtime.

Those choices are downstream engineering decisions and must be evaluated against this semantic contract.

## 16. Relationship to Ontology

The repository's ontology layer is project state, not session history. The Graph semantic model therefore acts as an execution/traceability model for project meaning; it must not silently replace the project's canonical ontology.

## 17. Relationship to Governance

The Graph must implement the project's authority hierarchy and Human–AI contract. The repository remains the technical source of truth, while human intent and approved constitutional decisions govern evolution.

## 18. Approval Gate

This document is a **proposal for human approval**.

Approval will authorize the next step: deriving the Graph's concrete **schema-independent contract tests and implementation requirements**.

No concrete storage technology should be selected before those requirements are established.
