# SES-022 — SESSION BOOTSTRAP

**Date:** 2026-09-10
**Status:** OPEN
**Previous checkpoint:** SES-021 = GREEN / PASSED
**Role:** Project Lead — autonomous execution within agreed scope

## 1. Purpose

Start a clean working session from the confirmed repository state.
The repository is the Source of Truth. Chat history is context only.

## 2. Confirmed checkpoint

SES-021 established and verified:

`EXECUTION_RESULT → EXECUTION_EFFECT`

The effect authorization must bind to the same `build_plan_id` as the execution result.
CI run `34457481601` = GREEN / PASSED.
SES-021 closeout is recorded in the repository.

## 3. Execution chain

`EXECUTION_AUTHORIZATION
→ EXECUTION_REQUEST
→ EXECUTION_ATTEMPT
→ EXECUTION_RESULT
→ EXECUTION_EFFECT`

Never conflate:

`AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTION_RESULT ≠ EXECUTION_EFFECT`

## 4. SES-022 objective

Audit the current repository and identify the **smallest next semantic execution boundary** after SES-021.

Do not assume the boundary in advance.

## 5. Working method

1. Inspect current repository state.
2. Read the latest confirmed session/checkpoint.
3. Define the smallest missing contract.
4. RED test.
5. Wire/run CI and obtain RED evidence.
6. Minimal implementation.
7. CI GREEN.
8. Verify scope and evidence.
9. Write `sessions/SES-022/SES-022_CLOSEOUT.md`.
10. Close SES-022 only when GREEN evidence is confirmed.

Maximum: 5 meaningful work actions per checkpoint.

## 6. Autonomous-operation rule

For this test session, the Project Lead may independently perform actions that remain inside the agreed project/session scope.

No approval request is required for:
- repository inspection;
- session documentation;
- contract tests;
- minimal implementation;
- CI wiring;
- CI verification;
- closeout documentation.

Stop and report before actions that change the agreed scope or cross a protected boundary.

## 7. Hard boundaries

DO NOT:
- perform real-world execution or external side effects;
- touch production systems/files/network;
- introduce payments or value transfer;
- add retry/orchestration/autonomous side effects;
- modify closed session artifacts;
- make Constitution/Ontology/Trust decisions;
- introduce architecture without a demonstrated contract need.

Fail closed.

## 8. TDD rule

`RED → CI RED → minimal implementation → CI GREEN → evidence → CLOSEOUT`

Tests define the contract before implementation.

## 9. Project principles

- Minimalization.
- Balance.
- Human sovereignty.
- System suggests; human decides.
- Ontology before code.
- Repository before memory.
- Evidence before closure.
- No premature architecture.

## 10. Communication

Report:

**STATE → EVIDENCE → DECISION → ACTION → NEXT CHECKPOINT**

Do not ask for confirmation when the action is already authorized by this session.

## 11. First action

Begin with repository audit.
Determine the smallest next boundary.
Do not code before the boundary is evidenced.
