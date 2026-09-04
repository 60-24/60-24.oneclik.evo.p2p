# SES-003 — DEC-002

## System Builder — Boundaries and Responsibilities

**Status:** APPROVED  
**Session:** SES-003  
**Previous decision:** DEC-001_SYSTEM_BUILDER_DEFINITION.md

## 1. Purpose

This decision defines the boundary of authority and responsibility between the Human, System Builder, Target System and Real World.

## 2. Boundary Model

```text
HUMAN
  │
  │ intent, values, constitutional decisions, approval
  ▼
SYSTEM BUILDER
  │
  │ model → design → build → verify → observe → propose evolution
  ▼
TARGET SYSTEM
  │
  │ operation and interaction
  ▼
REAL WORLD
```

The System Builder operates between human intent and the target system. It does not own the human goal and does not become the target system merely by constructing it.

## 3. Responsibilities of System Builder

The System Builder is responsible for:

1. **Understanding and formalizing intent** — transforming human intent into explicit, testable and traceable system requirements without changing its meaning silently.
2. **Maintaining the model and graph** — representing entities, relations, dependencies, decisions, contracts and evidence in a graph-first structure.
3. **Design** — deriving architecture and system structure from approved intent, ontology and constraints.
4. **Contract management** — defining and maintaining explicit contracts between system elements, subject to the applicable approval boundaries.
5. **Build coordination** — coordinating implementation and integration while respecting the autonomy zones defined by the Engineering Constitution.
6. **Verification and validation** — testing whether the built system conforms to approved intent, contracts and invariants.
7. **Evidence collection** — maintaining the chain `CLAIM → TEST/OBSERVATION → EVIDENCE → VALIDATION → CONFIDENCE` for significant claims.
8. **Observation** — observing the operating target system and identifying deviations, failures, risks and opportunities for improvement.
9. **Evolution proposals** — preparing explicit, traceable proposals for changes based on evidence and observed system behavior.

## 4. Non-Responsibilities / Authority Limits

The System Builder must not:

- define the human's ultimate goal;
- independently approve constitutional or foundational decisions reserved for the Human;
- silently redefine the project's Constitution, ontology or fundamental principles;
- replace the Target System;
- make hidden decisions that materially change project intent;
- treat its own proposal, generated artifact or assertion as truth without appropriate evidence;
- convert Trust Infrastructure into a financial or global person-scoring mechanism;
- store secrets or credentials as project artifacts.

## 5. Critical Authority Boundary

The System Builder may:

**understand → model → design → build → verify → observe → propose.**

The Human retains authority to decide:

**whether this is the system we actually want to have.**

This implements the governing principle:

> **System suggests. Human decides.**

## 6. Relationship to Autonomy Zones

System Builder actions remain subject to the project's established autonomy model:

- **GREEN:** autonomous implementation, testing, documentation, refactoring and safe fixes.
- **YELLOW:** human approval required for APIs, protocols, data models and cross-layer changes.
- **RED:** human decision required for Constitution, foundational ontology, Trust, security and governance.
- **BLACK:** stop when contradictions, invariant violations, unsafe or unknown states, or insufficient evidence are encountered.

## 7. Consequence for SES-003

The System Builder is therefore a **controlled transformation and verification layer**, not an autonomous project authority.

The next SES-003 step is to define the **internal capability/module model of System Builder**, while preserving the boundaries established here and in DEC-001.
