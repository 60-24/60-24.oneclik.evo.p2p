# SES-027 — Canonical Runtime Proof

**Date:** 2026-09-11  
**Status:** OPEN  
**Previous session:** SES-026 — Canonical Runtime Boundary  
**Repository:** `60-24/60-24.oneclik.evo.p2p`

## 1. Session purpose

Continue from the verified SES-026 boundary migration and establish the next minimal, evidence-driven step toward a functional runtime proof.

Primary objective:

`INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`

The canonical implementation boundary is `src/runtime/`. Session directories contain contracts, tests, evidence and process records; they must not become the canonical runtime implementation location.

## 2. Starting state

SES-026 is considered technically verified:

- obsolete runtime implementations under `sessions/SES_*` were removed;
- canonical runtime exists under `src/runtime/`;
- old runtime imports were searched and no current matches were found;
- current CI for commit `e22c7b402f9e0caaa983a2c150cfced0aa2f35c6` completed successfully for the observed SES-011 BuildPlan Contract workflow.

Canonical runtime files:

- `src/runtime/entrypoint.py`
- `src/runtime/observation.py`
- `src/runtime/flow.py`

## 3. Scope

SES-027 is an **audit → contract → minimal proof** session.

First inspect the repository and existing contracts/tests before changing implementation.

Do not broaden into P2P networking, trust, discovery, ontology, protocol redesign, or new infrastructure.

## 4. Operating rules

### GREEN — autonomous

Refactor, tests, documentation, cleanup, verification and other changes that preserve approved semantics may be performed autonomously.

### YELLOW — propose and obtain human decision

Changes to API, protocol, data structures, cross-layer boundaries, or architectural semantics require explicit proposal and approval.

### RED — human decision only

Constitution, ontology, trust, governance, security fundamentals or other constitutional meaning changes must not be made autonomously.

### BLACK — stop

Contradiction, unsafe state, missing evidence or unknown architectural meaning: stop implementation and report the issue.

## 5. Mandatory workflow

1. Inspect current `main` and repository state.
2. Verify SES-026 closeout/evidence and identify any remaining GAPs.
3. Trace the real runtime path:
   `INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`.
4. Inspect all relevant tests and workflows.
5. Define the smallest missing contract, if any.
6. If GREEN, implement the smallest deterministic proof and test it.
7. Verify with CI/evidence.
8. Record decision, changes, evidence and remaining GAPs.
9. Do not start the next architectural layer until this proof is verified.

## 6. Design constraints

- Minimality first.
- Deterministic behavior.
- Explicit input.
- No hidden state.
- No unnecessary dependencies.
- No duplicated runtime implementation.
- No silent architectural changes.
- Tests must express the contract, not implementation details.
- Evidence must be observable and reproducible.

## 7. Success condition

SES-027 succeeds when the repository contains a verified minimal runtime proof in which an explicit input can be traced through the canonical runtime boundary to an observable evidence-ready result, with tests and CI providing reproducible evidence.

## 8. Checkpoint format

At every meaningful checkpoint record:

- **State** — what is true now.
- **Evidence** — where it is verified.
- **Decision** — what was decided and why.
- **Next** — one concrete next action.

## 9. Project principle

**Build the builder before scaling the built system.**

`REUSE → INTEGRATE → IMPROVE → INVENT → REJECT/ESCALATE`

Human sovereignty remains above autonomous execution.
