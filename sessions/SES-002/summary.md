# SES-002 — Canonical Knowledge Graph v0.1

**Status:** OPEN — CONTROLLED RECONSTRUCTION
**Project:** P2P 60-24 OneClick Evo
**Previous session:** SES-001 — Foundation
**Branch:** `phase/04-canonical-knowledge-graph`

## Mission

Build the first canonical, traceable representation of P2P 60-24 project knowledge before major architectural implementation.

SES-002 does **not** implement the product. It establishes the knowledge structure that future architecture, contracts, tests and code must use.

## Starting model

```text
CONCEPT
  ├── ENTITY
  ├── RELATION
  ├── PROPERTY
  ├── EVENT
  ├── CONTRACT
  └── INVARIANT
        ↓
   CANONICAL ID
        ↓
 STATUS + PROVENANCE
        ↓
 RELATION GRAPH
```

## Governing rules

1. Repository/canonical documents outrank conversation memory.
2. Human intent remains the final authority.
3. Historical material is evidence and provenance, not automatic architecture.
4. No duplicate concept is created before checking existing terminology.
5. No unresolved concept is silently promoted to canonical status.
6. Conflicts are registered explicitly in `docs/OPEN_CONFLICTS.md`.
7. Use **REUSE → INTEGRATE → IMPROVE → INVENT → REJECT/ESCALATE**.
8. Biological metaphors remain inspiration unless explicitly converted into technical contracts.
9. Do not freeze concepts merely because they are useful or frequently mentioned.
10. Every important reconstructed concept should be traceable to its provenance.

## Classification

Use the controlled states:

- **FROZEN** — protected architectural/constitutional invariant.
- **PROTECTED** — important and constrained, but not necessarily immutable.
- **EVOLVABLE** — canonical direction may change through controlled evolution.
- **HISTORICAL** — preserved project history; not current authority.
- **UNVERIFIED** — plausible but insufficiently evidenced.
- **CONFLICTED** — competing definitions or architectural interpretations exist.

## Work packages

### WP-1 — Inventory
Identify relevant concepts, documents, modules, protocols and prior decisions.

### WP-2 — Identity
Assign stable canonical IDs only where the concept is sufficiently distinct and justified.

### WP-3 — Provenance
Record source document/session/origin and confidence for reconstructed knowledge.

### WP-4 — Reconciliation
Detect duplicates, aliases, overloaded names and semantic collisions.

### WP-5 — Conflict registration
Link unresolved disagreements to explicit conflict records.

### WP-6 — Graph
Create the first machine-readable and human-readable canonical graph.

### WP-7 — Verification
Check completeness, traceability, consistency and absence of premature freezing.

## Initial canonical graph target

The first graph should make it possible to answer:

- What is this concept?
- Why does it exist?
- Where did it come from?
- What status does it have?
- What concepts does it depend on?
- What concepts depend on it?
- Is it duplicated or aliased?
- Is it conflicted?
- What decision is still required from the human?

## Explicitly deferred

The following are **not** to be finalized merely during reconstruction:

- final Kernel/OmniKernel/SEE/SFO/TAL/Cognitive Fabric/AIRN hierarchy;
- final Trust vs Reputation terminology;
- economic/token concepts as current architecture;
- final networking technology choices;
- detailed implementation architecture;
- production code.

These remain subject to evidence and controlled decisions.

## Session output

SES-002 should produce at minimum:

- canonical concept/entity registry;
- relation vocabulary;
- provenance map;
- duplicate/alias map;
- updated conflict register;
- first Canonical Knowledge Graph v0.1;
- verification report;
- handoff to the next architecture phase.

## Exit condition

SES-002 may close only when the graph is usable as a shared context for human and AI agents and unresolved decisions are clearly isolated rather than hidden inside implementation.
