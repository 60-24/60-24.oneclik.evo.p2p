# SES-026 — Canonical Runtime Boundary Proposal

**Status:** PROPOSAL — YELLOW / human approval required
**Date:** 2026-09-11
**Scope:** runtime implementation boundary only

## 1. Decision Context

SES-023 → SES-024 → SES-025 established a verified minimal runtime proof:

`INPUT → STARTED → OBSERVED → EVIDENCE-READY`

The proof is currently implemented in `sessions/SES_023`, `sessions/SES_024` and `sessions/SES-025`, while the session contracts and tests live in the hyphenated `sessions/SES-023` … `SES-025` directories.

The repository therefore contains a working runtime proof, but its implementation location is still session-scoped rather than canonical application/source code.

## 2. Evidence

- `docs/SYSTEM_BUILDER.md` defines Runtime as a canonical stage after Implementation and separates System Builder from the target system.
- `AGENTS.md` defines cross-layer changes as YELLOW and requires human approval.
- `src/README.md` defines `src/` as the implementation-code boundary.
- SES-023/024/025 contracts and tests currently exercise the implementation from `sessions/SES_023`, `sessions/SES_024` and `sessions/SES-025`.

## 3. Proposed Boundary

Adopt the following separation:

```text
sessions/SES-023..025
    = contracts + tests + evidence + historical/session records

src/runtime/
    = canonical runtime implementation

runtime contract tests
    = verify canonical implementation without becoming implementation owners
```

The first canonical implementation target would therefore be:

```text
src/runtime/entrypoint.py
src/runtime/observation.py
src/runtime/flow.py
```

The exact module names may be adjusted only to preserve the existing public contract and minimize migration risk.

## 4. Migration Rule

The migration must preserve behavior first:

1. Copy/rehome the existing verified implementation into `src/runtime/`.
2. Update imports in the SES contract tests to target `src.runtime`.
3. Keep SES contracts/tests and closeout records in their session directories.
4. Run all affected tests and the corresponding GitHub Actions gates.
5. Only after green verification remove the obsolete session-scoped implementation copies.

No runtime behavior, protocol, data model, Trust model, or architecture beyond this boundary is changed.

## 5. Non-Goals

This proposal does **not**:

- expand runtime functionality;
- introduce networking, persistence, agents, Trust, Node, payment or transport architecture;
- define the full System Builder implementation;
- change Constitution or Ontology;
- remove historical session evidence.

## 6. Acceptance Criteria

The boundary is accepted when:

- one canonical runtime implementation exists under `src/runtime/`;
- SES-023/024/025 remain valid evidence/contract sessions;
- all existing runtime contract tests pass against the canonical implementation;
- SES-025 integrated flow remains `INPUT → STARTED → OBSERVED`;
- GitHub Actions gates remain green;
- no duplicate executable runtime implementation remains under `sessions/`.

## 7. Human Decision

**Approve or reject the proposed canonical boundary:**

`session artifacts → src/runtime/ canonical implementation → runtime observation → evidence`

Until approval, this document is only a proposal. No architectural move is authorized.
