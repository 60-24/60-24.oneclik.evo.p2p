# SES-034 — System Builder Entrypoint Inspection

**Status:** IN_PROGRESS — HARDENING APPLIED, CI VERIFICATION PENDING
**Date:** 2026-09-12
**Previous:** SES-033 GREEN / CLOSED
**Repository:** `60-24/60-24.oneclik.evo.p2p`
**Branch:** `main`

## 1. Repository-state decision

**ACCEPT with a real production gap; repair applied, verification still open.**

Inspection confirmed that the production System Builder entrypoint was missing the legal execution path for an ordinary `VALIDATED` BuildPlan.

The existing contracts distinguish:
- `VALIDATED` + `approval.required=false` + `NOT_REQUIRED`,
- `READY_FOR_APPROVAL` + explicit human approval,
- execution authorization,
- actual execution.

The previous entrypoint incorrectly forced every plan through the SES-014 human-approval authorizer. That made a normal valid Intent unable to reach the real local executor without manufacturing approval semantics.

## 2. Real gap and repair

The actual gap was:

`VALID INTENT → VALID SPECIFICATION → VALIDATED BUILD PLAN → SES-014 HUMAN APPROVAL AUTHORIZER`

SES-014 correctly rejects `VALIDATED` plans because they do not require approval. The local executor also previously accepted only `READY_FOR_APPROVAL + APPROVED` plans.

A separate authorization path was implemented for the already-declared no-approval case:

`VALIDATED + approval.required=false + approval.status=NOT_REQUIRED + no blockers`
`→ EXECUTION_AUTHORIZATION(status=AUTHORIZED, source=VALIDATED_NO_APPROVAL_REQUIRED)`

The boundary remains explicit:

`AUTHORIZATION ≠ APPROVAL`

## 3. Provenance hardening

A second real contract issue was found after tightening execution authorization: the `READY_FOR_APPROVAL` executor branch checked `APPROVED` but did not bind the authorization provenance.

It is now fail-closed and requires both:

`READY_FOR_APPROVAL + APPROVED + AUTHORIZED/EXPLICIT_HUMAN_APPROVAL`

The Beta executor fixture was updated to carry that explicit authorization, and a negative test now proves that an approved plan with the wrong authorization source cannot execute.

The two legal executor modes are therefore:

1. `READY_FOR_APPROVAL + APPROVED + AUTHORIZED/EXPLICIT_HUMAN_APPROVAL`.
2. `VALIDATED + NOT_REQUIRED + AUTHORIZED/VALIDATED_NO_APPROVAL_REQUIRED`.

Blocked, pending, malformed, or provenance-invalid plans remain rejected.

## 4. Files changed in SES-034

- `src/system_builder/validated_execution_authorization.py`
- `src/system_builder/entrypoint.py`
- `src/execution/local_executor.py`
- `sessions/SES-034/test_system_builder_entrypoint.py`
- `tests/test_local_executor_beta.py`

## 5. RED → repair evidence

Initial SES-034 production proof failed because the ordinary valid Intent produced `BuildPlan.status=VALIDATED`, while the entrypoint called the human-approval authorizer that requires `READY_FOR_APPROVAL`.

A later active CI run exposed contract drift in the older Beta executor fixture: it supplied `APPROVED` without an explicit execution authorization. That fixture was corrected rather than weakening the executor contract.

The current proof target is:

`INTENT → SPECIFICATION → VALIDATED BUILD PLAN → EXECUTION AUTHORIZATION → REQUEST → ATTEMPT → REAL EXECUTION → RESULT → EFFECT → OBSERVATION/EVIDENCE → VERIFICATION → DELIVERY`

and the security boundary:

`READY_FOR_APPROVAL + APPROVED + wrong provenance → REJECT`

## 6. CI trigger diagnosis and repair

The dedicated `.github/workflows/ses034-entrypoint.yml` was not reliably producing an exposed SES-034 run while the established SES-032 workflow continued to execute on `main`.

Decision: do not maintain a second CI workflow that GitHub is not reliably registering. The SES-034 production-entrypoint test is executed inside the already-active SES-032 E2E workflow.

Active CI path:

`SES-032 E2E workflow → SES-032 integration test → SES-034 production entrypoint test`

Relevant commits:
- `f42f47d75fe92c76537579749c25ce3d2c40f4da` — add SES-034 test to active E2E workflow
- `141aab8bbf6bad65ca09a0e8d47a91f3aea3c6a8` — remove unregistered duplicate SES-034 workflow
- `6432d56a5daef8b1c97821454ae01a011b39e61e` — bind approved execution to human authorization provenance
- `2436365bc130d0981a577a771d1747298a610423` — align Beta executor fixtures and add provenance rejection test

## 7. Current verification state

Latest known failing CI exposed the Beta fixture drift. That failure has now been repaired.

**CI:** pending. No PASS is declared until the active GitHub Actions E2E run executes the complete relevant test path and reports success.

## 8. Next autonomous action

1. Inspect the next active SES-032 E2E run.
2. Verify SES-034 production-entrypoint coverage and Beta executor tests are GREEN.
3. If GREEN: perform the repository-wide audit requested after confirmation, then close SES-034 and create the next focused session only if the audit identifies a concrete boundary gap.
4. If RED: inspect the exact failure and make the smallest contract-preserving repair.

No weakening of approval/provenance boundaries and no artificial PASS are permitted.
