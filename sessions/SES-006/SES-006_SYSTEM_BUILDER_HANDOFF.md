# SES-006 — SYSTEM BUILDER
## Handoff / Start Document

**Status:** READY TO OPEN  
**Previous session:** SES-005  
**Previous checkpoint:** Architectural Pivot / Separation of System Builder and P2P 60-24  
**Next session:** SES-006  
**Date:** 2026-09-07

## Mission

SES-006 formally separates two systems:

1. **SYSTEM BUILDER** — the metasystem that understands human intent and builds systems or modules.
2. **P2P 60-24 ONECLICK EVO** — the first major target system built through System Builder.

They MUST NOT be conceptually conflated.

Core lifecycle:

```text
Human Intent → Understand → Model → Build → Test → Verify → Deliver
```

## Carried decisions

- System Builder and P2P 60-24 are separate systems.
- P2P 60-24 is the first serious target/reference implementation.
- Existing P2P work is retained and classified, not discarded.
- No premature complete-P2P implementation.
- The smallest executable System Builder Vertical Slice is the next implementation target.
- Repository remains the technical source of truth.

## SES-006 sequence

1. Define System Builder boundary.
2. Define minimal lifecycle/model.
3. Audit and classify existing repository knowledge: SYSTEM BUILDER / P2P / SHARED / HISTORICAL / CONFLICT.
4. Design a tiny safe Vertical Slice.
5. Implement the smallest coherent slice.
6. Verify with evidence.
7. Human decision gate before using System Builder to build P2P.

## Constraints

Do not begin with complete P2P, global trust, economic/token systems, distributed production execution, or unrestricted remote code execution.

Execution safety must cover sandboxing, capabilities, filesystem/network boundaries, process/resource limits, artifact isolation, auditability and human approval boundaries.

## Starting instruction

**First establish the formal boundary and minimal model of SYSTEM BUILDER. Do not code yet.**

Then inspect Constitution, AGENTS.md, architecture, ontology and session material before proposing changes.

## Project Lead directive

> **Najpierw budujemy System, który potrafi budować systemy.**  
> **Potem przez ten System budujemy P2P 60-24 ONECLICK EVO.**

# End of SES-006 Handoff
