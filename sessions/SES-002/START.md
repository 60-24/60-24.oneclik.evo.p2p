# SES-002 — Canonical Knowledge Graph v0.1

**Project:** P2P 60-24 OneClick Evo  
**Session:** SES-002  
**Status:** OPEN  
**Phase:** Canonical Knowledge Reconstruction  
**Branch:** `phase/04-canonical-knowledge-graph`

---

## 1. Why this session exists

SES-001 established the governed project foundation and closed with a checkpoint. SES-002 now begins the next controlled step: reconstructing the project's knowledge into a canonical graph before allowing major architectural implementation.

The purpose is **not** to redesign the project from memory and not to erase historical ideas. The purpose is to determine what the project actually contains, where each concept came from, how concepts relate, which concepts are authoritative, and which remain uncertain or conflicting.

---

## 2. Primary objective

Create **P2P 60-24 CANONICAL KNOWLEDGE GRAPH v0.1**.

The graph must become the bridge between project history and future engineering decisions.

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

---

## 3. Governing rules

### 3.1 Source of truth

The repository is the technical source of truth. Existing documents are evidence and provenance. Conversation memory is supporting context only.

### 3.2 No silent promotion

A historical or proposed concept must not become canonical merely because it appears often or sounds architecturally attractive.

### 3.3 No silent deletion

Conflicting or obsolete material remains traceable as history unless there is an explicit decision to remove it.

### 3.4 Classification before implementation

Every significant concept should be classified before it is used as an architectural dependency:

- `FROZEN`
- `PROTECTED`
- `EVOLVABLE`
- `HISTORICAL`
- `UNVERIFIED`
- `CONFLICTED`

### 3.5 Human–AI contract

**System suggests. Human decides.**

AI agents may reconstruct, analyse, compare, detect conflicts, propose mappings and prepare implementation. They must not silently change project intent or constitutional meaning.

### 3.6 Reuse before invention

Use:

**REUSE → INTEGRATE → IMPROVE → INVENT → REJECT/ESCALATE**

before introducing a new concept, subsystem or terminology.

---

## 4. Work packages

### WP-01 — Knowledge inventory
Identify relevant existing project documents, specifications, prompts, prototypes and historical discussions represented in the repository.

### WP-02 — Concept extraction
Extract significant entities, concepts, relations, properties, events, contracts and invariants.

### WP-03 — Canonical identification
Give stable canonical IDs only where the evidence supports a distinct concept.

### WP-04 — Provenance
Record the source and status of reconstructed knowledge.

### WP-05 — Deduplication
Detect concepts that have different names but potentially the same meaning.

### WP-06 — Conflict mapping
Register semantic and architectural conflicts explicitly. Use `docs/OPEN_CONFLICTS.md` as an existing control point.

### WP-07 — Graph construction
Create the first machine-readable and human-readable canonical graph representation.

### WP-08 — Validation
Check graph consistency, missing provenance, duplicate identities, unresolved conflicts and unsupported assumptions.

---

## 5. Current known high-risk reconciliation areas

These are investigation targets, not decisions:

- Kernel / OmniKernel / KERNEL-DNA
- SEE / SEE-MG / SFO / TAL
- Cognitive Fabric / AIRN
- Identity / trust / reputation
- RealBond / TrustGraph
- Swarm Cognition / Neuro-Orchestrator
- Gossip / CRDT / network architecture
- OneClick / Evo
- economic and historical concepts such as Happycoin
- technology choices such as libp2p, WebRTC, Yjs, MCP and related components

No item above is automatically canonical merely because it is listed here.

---

## 6. Expected deliverables

At minimum, SES-002 should produce:

1. Canonical concept registry.
2. Canonical relation registry.
3. Provenance/status mapping.
4. Duplicate and alias mapping.
5. Conflict register updates.
6. Initial canonical graph.
7. Session decision log.
8. Clear handoff to the next architecture phase.

Suggested locations:

```text
ontology/
├── canonical/
│   ├── CONCEPTS.md
│   ├── RELATIONS.md
│   ├── INVARIANTS.md
│   ├── PROVENANCE.md
│   └── GRAPH.md
└── README.md

sessions/SES-002/
├── START.md
├── decisions.md
├── progress.md
└── next.md
```

The exact final structure may evolve during the session if the graph itself demonstrates a better organization.

---

## 7. Definition of done

SES-002 may close only when:

- the major known project concepts have been inventoried;
- canonical IDs exist for concepts that are sufficiently distinct;
- provenance and status are recorded;
- aliases and duplicates are visible;
- conflicts are explicit rather than hidden;
- the canonical graph is usable by both humans and AI agents;
- no major architectural decision depends on an unmarked assumption;
- the next architecture phase has a clean, evidence-backed input.

**SES-002 is a reconstruction session, not an implementation session.**

---

## 8. Opening command for an AI engineering agent

> Read `AGENTS.md`, the Engineering Constitution, the Project Constitution, `docs/ai/CANONICAL_PROJECT_CONTEXT.md`, `docs/RECONSTRUCTION_MATRIX.md`, `docs/OPEN_CONFLICTS.md`, and this file before making any project change.
>
> Your task in SES-002 is to reconstruct the Canonical Knowledge Graph v0.1 from repository evidence. Do not invent missing facts. Do not silently promote historical material to canonical status. Do not silently delete conflicts. Record provenance, status and uncertainty. Follow Graph Engineering and the Human–AI contract.

---

## 9. Session principle

> **Najpierw zrozumieć cały system. Potem nazwać go jednoznacznie. Następnie połączyć wiedzę w graf. Dopiero potem projektować architekturę i kod.**
