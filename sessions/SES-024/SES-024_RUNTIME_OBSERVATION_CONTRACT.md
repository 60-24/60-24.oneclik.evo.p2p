# SES-024 — Runtime Observation Contract

**Status:** RED target
**Date:** 2026-09-11

## Purpose
Define the smallest deterministic local observation boundary after `STARTED`.

## Contract
Given a valid started runtime identity, observation MUST produce exactly an evidence-ready local record containing:

- `status: OBSERVED`
- `runtime_id`
- `runtime_status: STARTED`
- `source: RUNTIME_STATE`

The observation is descriptive only. It MUST NOT execute external work or claim an external result.

## Determinism
Identical input state MUST produce an identical observation record.

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
- autonomous external effects

## Boundary
`STARTED → OBSERVATION → EVIDENCE-READY RECORD`

This contract does not define persistence, transport, external effects, or higher-level domain semantics.
