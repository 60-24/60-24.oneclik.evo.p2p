# SES-041 — SESSION BOOTSTRAP

**Date:** 2026-09-14  
**Version:** 1.0  
**Status:** OPEN  
**Branch:** `main`  
**Project:** P2P 60-24 OneClick Evo / System Builder

## 1. ENTRY STATE

SES-040 has been explicitly accepted by the Project Lead as **GREEN / CLOSED**.

SES-040 is now a closed reference point. Do not reopen its scope unless a new requirement provides concrete evidence of a defect.

Previous confirmed state:
- System Builder proof chain established through the existing local execution boundary.
- Windows demo/release work was the scope of SES-040.
- Repository remains the Source of Truth.
- Chat is context only.

## 2. OPERATING RULE

Work autonomously within the delegated project scope.

Mandatory cycle:

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Do not guess PASS.
Do not reopen closed milestones without evidence.
Do not make broad changes when the smallest sufficient change is available.
Prefer one good solution.

## 3. FIRST ACTION

Before changing anything:

1. Inspect the current `main` repository state.
2. Read the latest session/bootstrap/checkpoint documents.
3. Verify the current System Builder boundary and existing proof.
4. Identify the **smallest real next requirement or functional boundary** after SES-040.
5. Define the RED test before implementation.

## 4. SCOPE CONTROL

SES-041 must not:
- rewrite the architecture without evidence;
- reopen Beta as an unfinished milestone;
- treat CI noise as product failure without diagnosis;
- declare success without executable evidence;
- add speculative functionality merely because it is possible.

## 5. EXPECTED SESSION RESULT

SES-041 should end with one of two states:

**A. GREEN:** a new, objectively verified capability/boundary is proven, documented, and committed; then create the next stone and session bootstrap.

**B. BLOCKED:** the exact blocker is proven, documented, and isolated; do not disguise BLOCKED as PASS.

## 6. HANDOFF PRINCIPLE

`SES-040 = CLOSED REFERENCE`

`SES-041 = NEW WORK`

The next objective must be derived from the actual repository state and the smallest meaningful gap, not from assumptions or unfinished conversation context.

## 7. PROJECT LEAD

The assistant acts as Project Lead for the technical workflow: maintain order, scope, evidence, checkpoints, documentation, and final verification.
