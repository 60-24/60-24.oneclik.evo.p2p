# SES-046 — Microkernel Genealogy & Terminology Boundary

**Date:** 2026-09-16  
**Status:** AUDIT CHECKPOINT  
**Purpose:** evidence-first reconciliation of Microkernel / Kernel-DNA / OmniKernel / Node / Module terminology before new implementation or ADR.

## 1. Authority rule

This document is an engineering/session audit. It does **not** modify the Project Constitution, ontology, or frozen architecture. Historical documents are evidence, not authority. Current repository state remains the Source of Truth.

## 2. Evidence collected

### A. Current engineering boundary

SES-046 starts after SES-045 GREEN. The repository already proves a reusable concrete P2P boundary:

`Node A → connect → Node B → message → response`

Therefore a new "MiniKernel foundation" must not blindly duplicate the already-proven P2P node primitive.

### B. Earlier Microkernel definition — infrastructure, not system center

`P2P_60-24_OneClick_Evo_Sesja_Podsumowanie.md` states that the Microkernel is **not the center of the system** and is responsible for message validation, security, event transport and module isolation. It explicitly separates the kernel from system intelligence.

This is consistent with the later statement that the Microkernel is only a reliable execution foundation.

### C. Earlier minimal implementation genealogy

Historical design material records:

`KERNEL-DNA v3.0 → Microkernel v0.2 → Modules`

with Microkernel described as technical infrastructure containing Event Bus, Registry, Memory Store and PAC-loop runner.

Another historical implementation proposal defined `Microkernel v0.1` as:

`Event Bus + Registry`

with a target of approximately 150 LOC.

This is the strongest evidence that **Microkernel was originally conceived as a deliberately small infrastructure boundary**, not as a complete P2P application containing every node function.

### D. Kernel-DNA role

Historical material describes KERNEL-DNA as the contract layer for entities, state transitions, events and relations. Another design explicitly states that Kernel-DNA stores primitives such as Entity, State, Event and Relation without deciding their domain meaning; strategy remains outside the kernel.

Therefore Kernel-DNA and Microkernel must not be collapsed into one implementation object without further evidence.

### E. PAC genealogy

Historical PAC material states:

- PAC is a semantic model of autonomy, not an implementation layer of the kernel;
- each autonomous entity may implement PAC at its own level;
- KERNEL-DNA provides cooperation contracts;
- Microkernel provides technical infrastructure;
- modules may implement PAC at their level.

This supports keeping PAC above/beside the raw runtime mechanism rather than making PAC itself synonymous with Microkernel.

### F. StemCell / Module distinction

The Project Constitution v0.3.3 defines StemCell as a module that has no predetermined role and differentiates according to context and need. It also states that the same module can behave differently in different nodes through environmental configuration.

Separate historical material explicitly contains the statement:

`StemCell to NIE node — to tylko komórka.`

This is strong evidence against equating the smallest biological analogy with a network Node.

### G. Node in the project vision

The Constitution describes the virtual node as corresponding to a real person in a real place, and describes the network as the virtual reflection of real-world relationships. The project therefore gives **Node** a meaning broader than a mere source-code class.

### H. Event-first / decentralized direction

The project start material describes event-first communication and the topology:

`Node A ↔ Node B`
`Node C ↔ Node D`

with gossip as a mechanism for distribution without a central controller. It also places local state, CRDTs and vector clocks in the Kernel-DNA architectural context.

These mechanisms are relevant to the eventual node/network layers but are not automatically part of the minimal two-node kernel proof.

## 3. Terminology decision for SES-046

### Confirmed / high-confidence

**OmniKernel** — higher-level ecosystem kernel / shared foundational mechanism. Do not redefine it during this session.

**Kernel-DNA** — foundational contracts/invariants/primitives governing how system entities, state, events and relations cooperate. It is not synonymous with the concrete Node process.

**Microkernel** — minimal technical runtime/infrastructure boundary. It is not the center of intelligence and should remain as small as the justified contracts allow.

**Node** — concrete autonomous network participant/runtime. It is not automatically synonymous with Microkernel and should not be defined as such until the remaining genealogy is resolved.

**Module** — independently attachable capability/function above the minimal infrastructure boundary. Domain intelligence does not belong in the Microkernel merely because the node can host it.

**StemCell** — biological/architectural pattern for a context-differentiated module; not equivalent to Node.

## 4. What this means for the Claude MiniKernel proposal

The proposal is accepted as a **development experiment**, not as the project definition.

Good and compatible:

- start from a two-node communication proof;
- keep the foundation small;
- exclude blockchain, cryptocurrency, DHT, NAT traversal and premature discovery/routing;
- use tests as the definition of done;
- keep modules isolated;
- prefer correctness over optimization.

Not yet accepted as architecture:

- `Node = Microkernel`;
- `ModuleLoader` as a mandatory kernel component;
- `State` as a specific implementation such as MVCC/StateVault;
- Ed25519 as the final identity contract for the kernel;
- a new `MiniKernel` naming layer;
- replacing the existing SES-045 P2P primitive with a parallel implementation.

## 5. Current minimal boundary hypothesis

For implementation purposes only, pending further audit:

`Microkernel = smallest technical runtime that provides the contracts required for an autonomous concrete node to exist and communicate.`

The exact minimum must be derived from existing repository code and contracts, not invented from the Claude proposal.

A useful provisional separation is:

`OmniKernel`
`    ↓`
`Kernel-DNA / foundational contracts`
`    ↓`
`Microkernel / minimal runtime`
`    ↓`
`Node / concrete autonomous participant`
`    ↓`
`Modules / optional capabilities`

This diagram is **provisional**, not frozen architecture.

## 6. Immediate implementation rule

Do not create ADR-014 for Module Marketplace yet.

Do not add discovery, routing, trust, storage, consensus, GUI, marketplace or AI runtime to the minimal foundation.

First determine whether the existing SES-045 `P2PNode` is already the network portion of the required minimal runtime and identify the smallest missing boundary around it.

## 7. Next audit action

Inspect the current repository implementation and tests for:

1. `P2PNode` lifecycle and public API;
2. identity assumptions;
3. message/protocol boundary;
4. event representation;
5. state ownership;
6. logging/observability;
7. module/capability hooks.

Then formulate one concrete GAP and one RED test. No artificial RED.

## 8. Gate

**No new architecture is frozen by this document.**

The next implementation may proceed only from an observed repository GAP and the smallest justified change.
