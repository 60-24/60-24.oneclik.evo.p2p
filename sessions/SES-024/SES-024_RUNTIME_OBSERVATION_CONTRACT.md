# SES-024 — Runtime Observation Contract

**Status:** RED target  
**Date:** 2026-09-11  
**Boundary:** `STARTED → OBSERVATION → EVIDENCE-READY RECORD`

## Purpose
Define the smallest deterministic local observation boundary after `STARTED`.

## Input
The observation function accepts an explicit runtime state record containing:

- `runtime_id` — non-empty string
- `runtime_status` — must be `STARTED`

Invalid or incomplete input MUST fail closed with `ValueError`.

## Contract
Given a valid started runtime identity, observation MUST produce exactly an evidence-ready local record containing:

- `status: OBSERVED`
- `runtime_id`
- `runtime_status: STARTED`
- `source: RUNTIME_STATE`

The observation is descriptive only. It MUST NOT execute external work or claim an external result.

## Determinism
Identical input state MUST produce an identical observation record.

The implementation MUST NOT depend on system clock, randomness, environment state, network state, external files, or subprocesses.

## Fail-closed
The implementation MUST reject:

- non-dictionary input
- missing `runtime_id`
- empty or non-string `runtime_id`
- missing `runtime_status`
- runtime status other than `STARTED`

## Forbidden
The SES-024 implementation MUST NOT introduce:

- `executed`
- real `result`
- UDP/P2P transport
- Node / Agent / Peer
- Trust / TrustGraph
- persistence
- system-clock dependence
- subprocess/process execution
- external filesystem mutation
- network access
- retries
- orchestration
- autonomous external effects
- payment or value transfer

## TDD acceptance criteria
1. Observation module is importable and callable from a test.
2. Valid started state produces `OBSERVED` record.
3. Invalid state fails closed.
4. Identical input is deterministic.
5. Output contains no execution/effect claim.
6. Implementation has no external side effects.

## Required order
`CONTRACT → RED TEST → CI RED → MINIMAL IMPLEMENTATION → CI GREEN → EVIDENCE → CLOSEOUT`

No GREEN status may be declared without actual CI evidence.
