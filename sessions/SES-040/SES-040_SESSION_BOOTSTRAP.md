# SES-040 — Session Bootstrap

**Date:** 2026-09-14  
**Status:** OPEN  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. PURPOSE

Open a clean session after the SES-039 closeout and the unsuccessful Windows demo CI attempt. This session must recover the project from repository evidence, not from assumptions or chat history.

## 2. SOURCE OF TRUTH

The repository is the Source of Truth. Chat is context only.

Beta remains a **closed reference point**. Do not reopen or weaken Beta unless a new, explicit requirement demonstrates a real defect.

## 3. PREVIOUS STATE

- SES-039 completed the post-Beta completeness audit with no justified functional gap.
- The Windows downloadable-demo work was added to the Beta local-execution workflow.
- Relevant commit: `748a0c46d2eaf8a946bf488ef0bd6c1934bf37be`.
- GitHub Actions Run: `34821739434` (#55).
- Run conclusion: **FAILURE**.
- At the last inspection, the connector exposed no jobs and no artifacts, therefore the first failing step/root cause was not proven.
- No blind fix was authorized or justified.

## 4. CURRENT OBJECTIVE

Determine the smallest real next step required to finish or correctly close the Windows demo/release path.

Target proof, if the requirement remains active:

`SOURCE → BUILD → PACKAGE → RUN → VERIFY → ARTIFACT`

with the real production System Builder mechanism and the deterministic request:

`Hello Beta Extension`

Expected delivered artifact:

`Hello Beta Extension.txt`

with exact requested content and verification evidence.

## 5. EXECUTION RULE

Use:

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST (only if justified) → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CLOSE → CONTINUE`

Do not:

- guess a CI failure;
- make changes without a demonstrated gap;
- claim PASS without evidence;
- create work only to advance session numbering;
- modify the closed Beta boundary unnecessarily.

## 6. FIRST ACTIONS

1. Inspect current `main` and SES-039/040 repository state.
2. Inspect Run `34821739434` again for jobs, logs and artifacts; identify the **FIRST ERROR** if evidence is now available.
3. If the root cause is proven, apply the smallest fix only.
4. Re-run/verify CI only as justified and require actual Windows artifact evidence.
5. Record a checkpoint and close the session only when the evidence supports the conclusion.

## 7. HUMAN DECISION BOUNDARY

Human input is required only for constitutional, ontological, governance, product-scope, or explicitly out-of-scope decisions. Technical execution inside the delegated demo/CI scope is autonomous.

## 8. CHECKPOINT FORMAT

Every significant checkpoint:

`STATE → EVIDENCE → GAP → DECISION → ACTION → NEXT`

Maximum five significant actions per checkpoint.

## 9. SUCCESS CONDITION

SES-040 succeeds when the current requirement is either:

**A. PROVEN:** Windows demo is built, runs through the real production System Builder path, verifies the expected artifact, and produces a real downloadable GitHub Actions artifact;

or

**B. CLEANLY CLOSED:** evidence proves that no justified implementation action can be taken in this session, with the exact blocker documented for the next session.

---

**Opening principle:** No more chaos. Evidence first. One gap at a time. One good solution.
