# SES-017 — START

## Status

**OPEN — INSPECTION REQUIRED**

## Previous Milestone

SES-016 is CLOSED — GREEN / PASSED.

Verified boundary:

**Human Approval → exact BuildPlan identity binding**

CI evidence:
- Workflow: `SES-011 BuildPlan Contract`
- Run: `34337554949`
- Contract job: `102420404113`
- Commit: `dfa355d6d8c976673aff34b8c4e1e03009e3c1cc`
- Result: SUCCESS

## Objective of SES-017

Continue the contract-driven engineering sequence from the proven SES-016 boundary.

The session begins with repository inspection. No implementation or architectural decision is authorized before the next boundary is identified and its contract is defined.

## Mandatory Sequence

1. Inspect current `main` and repository state.
2. Verify SES-016 closeout and current CI evidence.
3. Review the boundary chain SES-010 → SES-016.
4. Identify exactly **one** next boundary.
5. Define the executable contract/test.
6. Establish RED evidence.
7. Implement the minimum GREEN change only.
8. Run CI and capture exact evidence.
9. If GREEN, place the milestone stone.
10. Write SES-017 closeout and next-session handoff.

## Project Control Rules

- Tests are executable evidence.
- Do not weaken a test merely to obtain GREEN.
- Do not make architectural or governance decisions implicitly.
- RED-zone decisions require explicit human approval.
- Do not open multiple boundaries in parallel.
- Do not expand scope because a future architectural need appears useful.
- `VALID Specification → BuildPlan → Human Approval → Execution` remains the governing execution chain.
- System suggests; Human decides.

## Explicit Hold

Previously proposed architectural roadmaps or lists of RED-zone decisions are **not approved scope** for SES-017.

SES-017 must first establish the next boundary from the actual repository state.

## Definition of Done

SES-017 may be closed only when one boundary is:

**defined → tested → minimally implemented → CI verified → documented → stoned.**
