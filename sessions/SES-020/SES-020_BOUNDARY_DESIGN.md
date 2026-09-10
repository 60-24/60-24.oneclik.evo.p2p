# SES-020 — Execution Boundary Design

**Status:** DESIGN / TDD
**Date:** 2026-09-10
**Previous gate:** SES-019 = GREEN / PASSED

## Audit result

The current chain is:

`EXECUTION_AUTHORIZATION → EXECUTION_REQUEST → EXECUTION_ATTEMPT → EXECUTION_RESULT`

SES-018 creates an attempt record only; it does not execute or produce a result. SES-019 creates an explicit result record only; it performs no execution or side effects.

Therefore the smallest missing semantic boundary is the boundary between an execution result and an explicit record of an applied execution effect.

## Decision

Define the next boundary as:

`EXECUTION_RESULT → EXECUTION_EFFECT`

`EXECUTION_EFFECT` is an explicit effect record. Its factory is a boundary contract, not the side effect itself.

The contract must require:
- a valid `EXECUTION_RESULT`;
- a non-empty `execution_effect_id`;
- a non-empty and matching `build_plan_id`;
- an explicit `effect_authorization` with status `AUTHORIZED`;
- a declared outcome of `SUCCEEDED` before an effect may be recorded.

The factory MUST NOT execute a process, touch production files, use production network, retry, orchestrate, transfer value, or perform any external side effect.

## Rationale

This preserves the distinction:

`AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTION_RESULT ≠ EXECUTION_EFFECT`

A result is evidence about an attempt. An effect is the explicit boundary at which a system can later integrate real side effects under a separately controlled authorization. No implicit execution is allowed merely because a result exists.

## TDD order

1. RED contract test.
2. CI RED evidence.
3. Minimal contract implementation.
4. CI GREEN evidence.
5. SES-020 closeout.

## Scope guard

No real side effect is authorized by SES-020.
