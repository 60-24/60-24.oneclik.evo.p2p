# SES-025 — Runtime Flow Contract

Status: PROPOSED → RED

## Purpose

Prove the smallest real integration of the already-established runtime boundaries.

## Contract

Given explicit runtime input:

`INPUT → SES-023 start_runtime → SES-024 observe_runtime → EVIDENCE-READY`

The integrated flow MUST:

1. accept an explicit non-empty `runtime_id`;
2. produce `STARTED` through the existing SES-023 entrypoint;
3. pass that runtime state to the existing SES-024 observation boundary;
4. produce `OBSERVED` evidence containing the same `runtime_id`;
5. introduce no network, persistence, clock, subprocess, payment, or external side effect.

## Reuse rule

The integration MUST reuse the existing SES-023 and SES-024 functions. It MUST NOT duplicate their contracts or introduce P2P, Trust, Node, Agent, or transport architecture.

## Acceptance

The integration test must fail before the minimal implementation exists and pass after implementation.
