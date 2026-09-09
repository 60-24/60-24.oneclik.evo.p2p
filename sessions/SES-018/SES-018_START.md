# SES-018 — START

## Status
OPEN — INSPECTION REQUIRED

## Previous milestone
SES-017 = GREEN / PASSED

CI evidence:
- Workflow: `SES-011 BuildPlan Contract`
- Run: `34380238007`
- Job: `102563021178`
- Commit: `3e4aca3e3b85be3a3f54d3f49a500aeece327837`
- SES-017 execution-request contract: SUCCESS

## Previous boundary
**Execution Authorization → Execution Request**

Established invariant:

`AUTHORIZED ≠ REQUESTED ≠ EXECUTED`

SES-017 created an explicit `Execution Request` seam. The request is only a handoff/intention and does not execute any step or create execution results.

## SES-018 single boundary
**Execution Request → Execution Dispatch / Execution Attempt**

## Objective
Determine whether and how an explicit `Execution Request` may cross into an execution attempt, while preserving the separation between requesting execution and actually performing an action.

## Central question
Can an explicit `Execution Request` be accepted by a clearly defined execution-dispatch seam as an **execution attempt**, without silently changing authorization, bypassing human approval, or introducing execution side effects before the boundary is explicitly defined and tested?

## Mandatory invariants
1. `AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTED`
2. An Execution Request does not itself execute anything.
3. No execution side effect is introduced before the contract is defined and tested.
4. Human approval remains bound to the exact BuildPlan identity.
5. No authorization bypass is permitted.
6. Only this single boundary is in scope.
7. Do not weaken existing tests to obtain GREEN.
8. RED-zone architectural or governance decisions require explicit human approval.

## Work sequence
1. Inspect the current repository and SES-017 implementation.
2. Identify whether an execution-dispatch / execution-attempt seam already exists.
3. Define the smallest executable contract test for this boundary.
4. Run CI and establish valid RED evidence if the seam is absent.
5. Implement only the minimum required change.
6. Run CI again and require real GREEN evidence.
7. Document the result and place the milestone stone only after GREEN.
8. Prepare SES-019 handoff.

## Out of scope
- Actual execution of project operations.
- External side effects.
- New executor architecture.
- Scheduling, retries, workers, queues, or distributed execution.
- Changes to Human Approval semantics.
- Changes to BuildPlan semantics.
- Any second execution boundary.

## Definition of Done
**defined → tested → minimally implemented → CI verified → documented → stoned**

## Rule for this session
Do not proceed to SES-019 until SES-018 has a verified CI GREEN result and its milestone stone is documented.
