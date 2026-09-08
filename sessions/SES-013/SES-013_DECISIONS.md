# SES-013 — DECISIONS

## D-013-01 — Mandatory provenance is a hard BuildPlan boundary

A VALID Specification without mandatory provenance must not produce an approvable BuildPlan.

**Enforcement:** blocker type `MISSING_PROVENANCE`.

## D-013-02 — Minimal implementation only

The SES-013 implementation change is limited to provenance validation in `sessions/SES_011/build_plan.py`. No execution behavior or authorization boundary is changed.

## D-013-03 — GREEN requires executable evidence

Previous Gate 01 evidence does not prove SES-013. SES-013 remains OPEN until the new test is actually executed and a real PASS result is available.

## D-013-04 — No autonomous authorization

The BuildPlan remains a proposal. Human approval remains mandatory before execution.
