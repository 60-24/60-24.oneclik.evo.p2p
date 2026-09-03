# P2P 60-24 OneClick Evo — Repository Inventory v0.1

**Phase:** 4 — Canonical Knowledge Graph  
**Session:** SES-002  
**Status:** CONTROLLED / WORKING  
**Branch:** `phase/04-ses-002-knowledge-graph`  
**Purpose:** inventory repository knowledge before canonical concept promotion.

> This inventory is an evidence map, not an architectural decision document. Presence of a file or concept does not make it canonical.

## 1. Inventory Rules

1. Repository content outranks conversational memory.
2. Historical material is provenance, not automatic architecture.
3. No concept is promoted merely because it appears in a document.
4. Contradictions are preserved and recorded in `docs/OPEN_CONFLICTS.md`.
5. Every promoted concept must eventually receive a canonical identifier and canonical location.
6. Technology choices remain candidates until explicitly approved.
7. Constitutional, foundational ontology, Trust and fundamental security/governance decisions require human review.

## 2. Current Repository Surface

The SES-002 branch currently contains the following principal knowledge areas:

### Governance / Constitution

- `AGENTS.md` — operating rules for AI/human collaboration and repository authority.
- `P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md` — engineering governance baseline.
- `constitution/PROJECT_CONSTITUTION.md` — project-level constitution, currently DRAFT and not frozen.
- `constitution/AUTONOMY_ZONES.md` — AI autonomy boundaries.
- `constitution/INVARIANTS_FROZEN.md` — protected/frozen invariant mechanism.
- `constitution/CONSTITUTIONAL_DECISION_TEMPLATE.md` — decision workflow.

### Reconstruction / Knowledge Control

- `docs/RECONSTRUCTION_MATRIX.md` — classification of reconstructed knowledge.
- `docs/OPEN_CONFLICTS.md` — unresolved semantic and architectural conflicts.
- `docs/ai/CANONICAL_PROJECT_CONTEXT.md` — controlled context for AI agents.
- `sessions/SES-001/*` — closed Phase 3 decisions, summary and handoff.
- `sessions/SES-002/CHECKPOINT-001.md` — current SES-002 checkpoint.

### Architecture / ADR

- `architecture/ADRs/ADR-TEMPLATE.md`
- `architecture/ADRs/README.md`
- `architecture/README.md`

Current state: architecture is structurally prepared but not yet canonically populated.

### Graph Engineering

- `docs/graph-engineering/README.md`

Current state: structural area exists; canonical graph artifact is the next target.

### Ontology

- `docs/ontology/README.md`
- `ontology/README.md`

Current state: ontology areas exist, but the canonical ontology itself has not yet been frozen.

### Trust / Security / Protocols / Governance

- `docs/trust/README.md`
- `docs/security/README.md`
- `docs/protocols/README.md`
- `docs/governance/README.md`

Current state: domains are reserved; detailed canonical specifications remain future work after reconciliation.

### Human / AI Documentation

- `docs/human/README.md`
- `docs/ai/README.md`
- `docs/ai/CANONICAL_PROJECT_CONTEXT.md`

Current state: collaboration framework exists; detailed human and AI manuals can be derived after ontology stabilization.

### Implementation Surface

- `src/README.md`

Current state: intentionally not the focus of SES-002. No implementation should be inferred from historical concepts.

### Historical Material

- `Qwen_markdown_20260420_t61kqxivh.md`
- `chat-Decentralized Computing Network.txt`

These files are valuable provenance and must be mined for concepts, decisions and conflicts. They are not automatically canonical.

## 3. Knowledge Classification from Reconstruction Matrix

| Domain | Current classification | Inventory action |
|---|---|---|
| Project identity | PROTECTED | retain and map to Constitution/Ontology |
| Human–AI engineering | PROTECTED | retain |
| Graph Engineering chain | PROTECTED | canonicalize |
| Kernel / OmniKernel | EVOLVABLE / PROTECTED candidate | resolve vocabulary |
| KERNEL-DNA | PROTECTED candidate | locate authoritative provenance |
| SEE | EVOLVABLE | resolve naming/version |
| TAL | EVOLVABLE | resolve role and boundaries |
| SFO | EVOLVABLE | locate/assess provenance |
| Identity | PROTECTED | preserve separation from trust/reputation |
| Trust Infrastructure | PROTECTED | preserve constitutional boundary |
| TrustGraph | EVOLVABLE | define canonical role |
| Reputation variants | CONFLICTED | resolve terminology |
| RealBond | HISTORICAL / EVOLVABLE | reconcile with TrustGraph |
| Swarm principle | PROTECTED candidate | constitutional review later |
| Biological patterns | PROTECTED | preserve as inspiration only |
| Gossip / CRDT | EVOLVABLE | validate after architecture |
| AIRN | EVOLVABLE | reconcile with graph |
| OneClick | PROTECTED candidate | define semantics before implementation |
| Evo | PROTECTED candidate | define controlled-evolution boundary |
| MCP | EVOLVABLE | avoid premature proliferation |
| TIL Engine | HISTORICAL / UNVERIFIED | do not implement |
| Happycoin / economy | HISTORICAL | preserve as history; excluded from current core |
| Impact framework | HISTORICAL / UNVERIFIED | preserve for later review |

## 4. Historical-to-Canonical Mapping Targets

The following canonical destinations are proposed as *locations*, not decisions about the concepts themselves:

| Knowledge type | Canonical destination |
|---|---|
| Why / fundamental constraints | `constitution/` |
| What exists / relationships | `ontology/` and `docs/ontology/` |
| Why a technical choice exists | `architecture/ADRs/` |
| How the system is constructed | `architecture/` |
| Protocol semantics | `docs/protocols/` |
| Trust semantics | `docs/trust/` |
| Security semantics | `docs/security/` |
| AI operating context | `docs/ai/` |
| Human explanation | `docs/human/` |
| Reconstruction evidence | `docs/` |
| Process / continuity | `sessions/` |
| Implementation | `src/` |
| Executable evidence | `tests/` when implementation begins |

## 5. Six-Month Knowledge Areas Requiring Provenance Mapping

The six-month project history contains the following major concept families that must be traced to source material before promotion:

### Core system

- P2P 60-24 OneClick Evo
- OmniKernel / Kernel
- Kernel-DNA
- Node
- Identity
- Capability
- Resource
- Event
- State
- Contract

### Knowledge / cognition

- SEE / SEE-MG
- OES
- Cognitive Fabric
- Memory layers
- Evidence
- Knowledge graph
- Neuro-Orchestrator
- Swarm Cognition
- Intelligentbit
- AKO / pheromone coordination

### Trust / relationships

- Trust Infrastructure
- TrustGraph
- Reputation
- Reputation Manager
- Reputation Ledger
- RealBond
- Proof-of-Meeting
- Trust decay
- Contextual trust
- Social Recovery

### Networking

- TAL
- TPI
- PTP-Message
- Gossip
- CRDT
- DHT / DHT alternatives
- libp2p
- QUIC / transport candidates
- WireGuard / Mesh VPN
- WebRTC
- LoRa / Meshtastic

### Evolution / operations

- OneClick
- Evo
- homeostasis
- controlled evolution
- recovery
- observability
- evidence loops
- TIL
- technology intelligence

### Extended / research concepts

- Happycoin / Local Economy
- HappyLang
- Earth Digital Twin
- MCS-1 / TIFM
- biological architecture research

These extended concepts must not be promoted to core architecture merely because they are present in the six-month history.

## 6. Current Conflicts Confirmed by Repository

The repository explicitly records five major conflict groups:

- **C-001:** architecture vocabulary — Kernel/OmniKernel, SEE, SFO, TAL, AIRN, Cognitive Fabric and related layers.
- **C-002:** Trust/Reputation terminology.
- **C-003:** economic/Happycoin concepts versus current financial boundary.
- **C-004:** impact framework status.
- **C-005:** technology choices.

See `docs/OPEN_CONFLICTS.md` for controlled treatment.

## 7. Immediate Next Artifact

The next SES-002 artifact should be a **Concept Register / Canonical Candidate Register** derived from this inventory.

Recommended fields:

```text
concept_id
preferred_label
aliases
source_files
source_dates
provenance
classification
current_definition
conflicting_definitions
relations
canonical_destination
promotion_status
human_decision_required
notes
```

## 8. Stop Conditions

Stop rather than infer when:

- two sources provide materially different definitions;
- provenance cannot establish authority;
- merging concepts would erase a meaningful distinction;
- a constitutional or foundational boundary would be changed;
- historical material is the only evidence for a proposed current requirement.

## 9. Checkpoint

This inventory establishes **repository coverage**, not architectural truth.

**Next:** systematic concept extraction and provenance mapping.
