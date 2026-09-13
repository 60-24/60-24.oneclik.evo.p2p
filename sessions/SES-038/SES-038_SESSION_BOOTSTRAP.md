# SES-038 — New Requirement Stage Bootstrap

**Status:** OPEN
**Date:** 2026-09-14
**Repository:** `60-24/60-24.oneclik.evo.p2p`
**Branch:** `main`
**Role:** Project Lead / evidence-first autonomous execution

## 1. STARTING POINT

SES-037 is GREEN / CLOSED.

SES-037 proved one concrete post-Beta requirement without production changes:

> Create one text artifact containing the requested text.

Evidence:

- closeout: `sessions/SES-037/SES-037_CLOSEOUT.md`
- proof commit: `c1aec27c27badd86a59db8e52f7fab39f3b327fb`
- CI run: `34788645097` — SUCCESS
- closeout commit: `c0feedb6f7cfc320be08788840d3893e1fca175d`

## 2. BETA BOUNDARY

Functional Beta remains the closed reference point.

Do not reopen, weaken, reinterpret, or modify Beta evidence unless a new explicit requirement demonstrates a real defect.

Canonical Beta flow remains:

`INTENT → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL / AUTHORIZATION → REQUEST → ATTEMPT → REAL EXECUTION → RESULT → EFFECT → OBSERVATION/EVIDENCE → VERIFICATION → DELIVERY MANIFEST`

Mandatory semantic distinctions remain:

`APPROVAL ≠ AUTHORIZATION`

`AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTED ≠ RESULT ≠ EFFECT`

`VERIFIED ≠ real-world effect`

`DELIVERY MANIFEST ≠ EXTERNAL DELIVERY`

## 3. SOURCE OF TRUTH

The repository is the Source of Truth. Chat is context only.

Operating cycle:

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST (only if justified) → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CLOSE → CONTINUE`

No false PASS. No implementation without a real requirement and real gap.

## 4. FIRST TASK

Before implementation:

1. Inspect the current repository state after SES-037.
2. Recover the current project goal and active constraints from repository artifacts.
3. Identify whether a new explicit requirement already exists.
4. If a requirement exists, audit it evidence-first.
5. If no new requirement exists, record that fact and prepare a clean handoff rather than inventing scope.

## 5. AUTONOMOUS EXECUTION

Within delegated project-lead scope, continue autonomously through coherent inspection, testing, documentation, CI verification and closeout steps.

Ask the human only for genuinely constitutional, ontological, governance-level, product-defining, or otherwise out-of-scope decisions.

## 6. CHECKPOINT

Use:

`STATE → EVIDENCE → GAP → DECISION → ACTION → NEXT`

Maximum five significant actions per checkpoint.

## 7. OUT-OF-SCOPE UNLESS EXPLICITLY REQUIRED

Do not introduce automatically:

- P2P / UDP runtime
- Trust / LocalTrust / TrustGraph
- agent swarm / multi-agent orchestration
- persistence
- UI
- External Delivery
- new authorization sources
- new runtime layers/contracts
- natural Proposal generation as a production requirement

These require an explicit new requirement.

## 8. SESSION EXIT

SES-038 closes only after its actual requirement-driven work is evidenced and documented, or after establishing that no new requirement exists and recording a clean handoff.
