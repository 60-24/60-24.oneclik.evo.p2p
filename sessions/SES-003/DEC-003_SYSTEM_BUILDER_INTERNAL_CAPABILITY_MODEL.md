# SES-003 — DEC-003

## System Builder — Internal Capability Model

**Status:** APPROVED  
**Session:** SES-003  
**Previous decision:** DEC-002_SYSTEM_BUILDER_BOUNDARIES_AND_RESPONSIBILITIES.md

## 1. Purpose

This decision establishes the minimal internal capability model of System Builder. These are capabilities, not yet concrete software modules, agents, services or technologies.

## 2. Minimal Capability Chain

```text
HUMAN INTENT
     ↓
  INTENT
     ↓
   MODEL
     ↓
   DESIGN
     ↓
 CONTRACT
     ↓
   BUILD
     ↓
  VERIFY
     ↓
 OBSERVE
     ↓
  EVOLVE
     ↺
```

## 3. Capability Definitions

### INTENT

Understands, clarifies and formalizes human intent without silently changing its meaning.

### MODEL

Maintains the graph-based representation of entities, relations, dependencies, decisions, constraints and evidence.

### DESIGN

Transforms approved intent and model knowledge into system structure and architecture.

### CONTRACT

Makes interfaces, invariants, responsibilities and expected behavior explicit and traceable.

### BUILD

Transforms approved designs and contracts into system artifacts and integrations within authorized autonomy boundaries.

### VERIFY

Tests and validates whether the resulting system conforms to approved intent, contracts, invariants and acceptance criteria.

### OBSERVE

Collects runtime observations and evidence about the target system and detects deviations, failures, risks and relevant changes.

### EVOLVE

Transforms verified observations into explicit change proposals and feeds approved changes back into the lifecycle.

## 4. Capability Classes

For further architecture work, the capabilities are grouped as follows:

**CORE — transformation capabilities**
- INTENT
- MODEL
- DESIGN
- BUILD

**CONTROL — correctness and boundary capabilities**
- CONTRACT
- VERIFY

**FEEDBACK — operational learning and controlled evolution**
- OBSERVE
- EVOLVE

This grouping is organizational only. It does not yet define deployment boundaries or implementation components.

## 5. Architectural Principle

The capability model follows the project lifecycle:

`UNDERSTAND → MODEL → DESIGN → BUILD → VERIFY → OBSERVE → EVOLVE`

The model therefore describes a continuous controlled transformation loop rather than a conventional collection of independent services.

## 6. Non-Decisions

This decision does **not** yet determine:

- programming languages;
- frameworks;
- agent topology;
- process or service boundaries;
- database technology;
- network protocols;
- deployment topology;
- specific AI models;
- concrete implementation of the graph.

Those decisions require later analysis and appropriate approval according to the project's autonomy zones.

## 7. Invariant

No internal capability may acquire authority that contradicts DEC-001 or DEC-002.

In particular:

> **System suggests. Human decides.**

The System Builder may transform, verify, observe and propose; it does not become the sovereign authority over project intent.

## 8. Next Step

The next SES-003 step is to define the **information and artifact flow between these capabilities**: what enters each capability, what it produces, what must be preserved, and how traceability is maintained across the complete lifecycle.
