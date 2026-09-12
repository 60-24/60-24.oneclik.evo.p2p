# SES-034 — System Builder Entrypoint Inspection

**Status:** IN_PROGRESS — RED GAP REPAIRED, CI VERIFICATION PENDING
**Date:** 2026-09-12
**Previous:** SES-033 GREEN / CLOSED
**Repository:** `60-24/60-24.oneclik.evo.p2p`
**Branch:** `main`

## 1. Repository-state decision

**ACCEPT with a real production gap.**

Inspection confirmed that the production System Builder entrypoint was missing the legal execution path for an ordinary `VALIDATED` BuildPlan.

The existing contracts distinguish:
- `VALIDATED` + `approval.required=false` + `NOT_REQUIRED`,
- `READY_FOR_APPROVAL` + explicit human approval,
- execution authorization,
- actual execution.

The previous entrypoint incorrectly forced every plan through the SES-014 human-approval authorizer. That made a normal valid Intent unable to reach the real local executor without manufacturing approval semantics.

## 2. Real gap

The actual repository flow was:

`VALID INTENT → VALID SPECIFICATION → VALIDATED BUILD PLAN → SES-014 HUMAN APPROVAL AUTHORIZER`

SES-014 correctly rejects `VALIDATED` plans because they do not require approval. The local executor also previously accepted only `READY_FOR_APPROVAL + APPROVED` plans.

This was a genuine contract mismatch, not a missing test artifact.

## 3. Minimal repair applied

Implemented a separate execution-authorization path for the already-declared no-approval case:

`VALIDATED + approval.required=false + approval.status=NOT_REQUIRED + no blockers`
`→ EXECUTION_AUTHORIZATION(status=AUTHORIZED, source=VALIDATED_NO_APPROVAL_REQUIRED)`

Important boundary preserved:

`AUTHORIZATION ≠ APPROVAL`

SES-014 remains unchanged. A plan requiring approval still must pass explicit human approval with exact `build_plan_id` binding.

The local executor now accepts exactly two legal authorization modes:

1. `READY_FOR_APPROVAL + APPROVED` from explicit human approval.
2. `VALIDATED + NOT_REQUIRED + AUTHORIZED/VALIDATED_NO_APPROVAL_REQUIRED`.

Blocked, pending, malformed, or unauthorized plans remain rejected.

## 4. Files changed

- `src/system_builder/validated_execution_authorization.py`
- `src/system_builder/entrypoint.py`
- `src/execution/local_executor.py`
- `sessions/SES-034/test_system_builder_entrypoint.py`

## 5. RED → repair evidence

Initial SES-034 production proof failed because the ordinary valid Intent produced `BuildPlan.status=VALIDATED`, while the entrypoint called the human-approval authorizer that requires `READY_FOR_APPROVAL`.

The repair adds a real production authorization branch and a test proving:

`INTENT → SPECIFICATION → VALIDATED BUILD PLAN → EXECUTION AUTHORIZATION → REQUEST → ATTEMPT → REAL EXECUTION → RESULT → EFFECT → OBSERVATION/EVIDENCE → VERIFICATION → DELIVERY`

The test also proves that the new authorization path rejects a plan that actually requires human approval.

## 6. CI trigger diagnosis and repair

The dedicated `.github/workflows/ses034-entrypoint.yml` was present and syntactically valid, but GitHub did not expose a SES-034 run while the established SES-032 workflow continued to execute on `main`.

A minimal PR registration probe was performed and merged as PR #4. It produced no observable SES-034 workflow run.

Decision: do not maintain a second CI workflow that GitHub is not reliably registering. The real SES-034 production-entrypoint test is now executed as an additional step inside the already-active SES-032 E2E workflow.

Active CI path:

`SES-032 E2E workflow → SES-032 integration test → SES-034 production entrypoint test`

Relevant CI commits:
- `f42f47d75fe92c76537579749c25ce3d2c40f4da` — add SES-034 test to active E2E workflow
- `141aab8bbf6bad65ca09a0e8d47a91f3aea3c6a8` — remove unregistered duplicate SES-034 workflow

This removes CI duplication without weakening the SES-034 production proof.

## 7. Current verification state

Latest CI integration change:
`f42f47d75fe92c76537579749c25ce3d2c40f4da`

Cleanup commit:
`141aab8bbf6bad65ca09a0e8d47a91f3aea3c6a8`

**CI:** pending. No PASS is declared until the active GitHub Actions E2E run executes `sessions/SES-034/test_system_builder_entrypoint.py` and reports success.

## 8. Next autonomous action

Inspect the next active SES-032 E2E run and verify that its final step is the SES-034 production entrypoint test.

If GREEN:
`VERIFY → CLOSE SES-034 → create SES-035 bootstrap`

If RED:
`inspect exact failure → smallest RED test/repair → CI again`

No weakening of the approval boundary and no artificial PASS are permitted.
