# SES-006 — SYSTEM BUILDER BOUNDARY

**Status:** WORKING MODEL — NOT CONSTITUTIONAL APPROVAL
**Date:** 2026-09-07

## 1. Purpose

System Builder is a distinct metasystem whose purpose is to transform an approved human intent into a built, tested, verified and deliverable system or module.

It is not P2P 60-24. P2P 60-24 is a target system that System Builder may build.

## 2. Boundary

```text
                         HUMAN
                           │
                    intent + authority
                           │
                           ▼
                 ┌───────────────────┐
                 │   SYSTEM BUILDER  │
                 │                   │
                 │ Understand        │
                 │ Model             │
                 │ Plan              │
                 │ Build             │
                 │ Test              │
                 │ Verify            │
                 │ Package / Deliver │
                 └─────────┬─────────┘
                           │
                           ▼
                    BUILT ARTIFACT
                           │
                           ▼
                 TARGET SYSTEM / MODULE
```

## 3. Input

The primary input is human intent, supplemented by explicit constraints, available knowledge, approved specifications and existing reusable components.

System Builder may clarify ambiguity and propose interpretations, but it must not silently redefine human intent.

## 4. Output

The output is a deliverable artifact accompanied by sufficient evidence to establish what was built, how it was tested, and what verification was performed.

A proposal, architecture sketch or generated code without verification is not a completed System Builder result.

## 5. Internal lifecycle

The minimal lifecycle is:

**Intent → Understand → Model → Build → Test → Verify → Deliver**

Each stage must produce an observable intermediate result or evidence sufficient for the next stage.

## 6. Human authority

Human authority remains outside System Builder's autonomous decision loop for constitutional, foundational architectural, governance, trust and other explicitly protected decisions.

System Builder can analyse and recommend. It cannot silently convert recommendations into authoritative project decisions.

## 7. System Builder vs target system

| System Builder | Target system |
|---|---|
| builds systems/modules | is the built system/module |
| operates at metasystem level | operates at domain/system level |
| consumes human intent | implements domain purpose |
| produces artifacts + evidence | consumes delivered artifacts |
| can build different targets | is one concrete target |

P2P 60-24 therefore must not be embedded into the definition of System Builder.

## 8. Verification boundary

System Builder is responsible for establishing build/test/verification evidence for the artifact it produces.

It is not automatically the final authority over constitutional acceptance of the target system. Human approval remains required wherever the repository governance marks a decision as protected.

## 9. Safety boundary

No unrestricted execution is part of the minimal System Builder definition.

Any execution capability must be constrained by explicit sandbox, capability, filesystem, network, process/resource and artifact-isolation rules, with auditability and approval boundaries defined before unsafe execution is introduced.

## 10. Open questions for the next stage

These are deliberately unresolved and must be analysed before implementation:

1. What is the minimal machine-readable representation of Intent?
2. What is the minimal System/Module Model?
3. What artifact contract connects Model → Build → Test → Verify?
4. What evidence is sufficient to mark an artifact VERIFIED?
5. What is the smallest deterministic Vertical Slice that proves the lifecycle?
6. Which existing repository components can be reused?
7. What part of Graph Engineering/Neo4j, if any, belongs to System Builder?

## 11. Decision status

This document is a **working model for SES-006**, not a constitutional amendment.

Any change affecting protected constitutional, ontological, trust, security or governance assumptions must follow the repository's existing approval hierarchy.

---

**Next action:** define the minimal machine-readable model and select the first safe Vertical Slice before writing implementation code.
