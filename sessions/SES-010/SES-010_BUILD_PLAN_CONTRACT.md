# SES-010 — Build / Execution Plan Contract

**Status:** CONTRACT — TDD / no implementation
**Source:** validated SES-008 Specification
**Session:** SES-010
**Contract version:** 1

## 1. Purpose

A `BuildPlan` is the machine-representable plan for transforming a validated `Specification` into an executable build sequence **without itself executing the system**.

The BuildPlan describes *what may be built, in what order, under which conditions, and with what evidence*. It does not grant autonomous authority to resolve protected or unresolved decisions.

Boundary:

`VALID Specification → BuildPlan → Human Approval → Execution`

There is deliberately no direct path:

`Specification → autonomous execution`

## 2. Contract

```text
BuildPlan
├── build_plan_id
├── source_specification_id
├── contract_version
├── status
├── objective
│   ├── statement
│   └── origin
├── steps[]
│   ├── id
│   ├── sequence
│   ├── action
│   ├── target
│   ├── preconditions[]
│   ├── inputs[]
│   ├── expected_outputs[]
│   ├── acceptance_criteria[]
│   ├── provenance[]
│   ├── origin
│   └── execution_state
├── dependencies[]
├── constraints[]
├── assumptions[]
├── unresolved_decisions[]
├── approval
│   ├── required
│   ├── status
│   └── authority_scope
├── blockers[]
├── provenance[]
│   ├── source_specification_id
│   ├── source_specification_element_id
│   ├── build_plan_element_id
│   └── origin
└── determinism
    ├── canonicalization
    ├── ordering
    └── identity_rule
```

## 3. Origin semantics

Every BuildPlan element that can affect execution MUST declare its origin:

- `DERIVED` — directly determined by the validated Specification. It may be generated deterministically.
- `PROPOSED` — introduced by the System Builder because the Specification does not uniquely determine the choice. It requires explicit human approval.
- `UNRESOLVED` — a decision or dependency that remains undecided. It MUST remain non-executable.

The transformer MUST NOT relabel `PROPOSED` or `UNRESOLVED` content as `DERIVED`.

## 4. Transformation boundary

The transformer accepts only:

1. a `VALID` Specification;
2. a supported BuildPlan contract version;
3. deterministic normalization/canonicalization rules.

The transformer produces a BuildPlan, not execution side effects.

Invalid input states MUST fail closed.

## 5. Blocking rules

The BuildPlan MUST be marked blocked when any execution-relevant condition is unresolved or unauthorized, including:

- `UNRESOLVED` decision affecting a step, dependency, constraint, input, output, or acceptance criterion;
- required human approval not granted;
- protected decision without explicit authority;
- missing mandatory provenance;
- invalid or incomplete source Specification;
- contradictory execution preconditions;
- unsupported action or target semantics.

> **Brak informacji ≠ zgoda na jej wygenerowanie.**

A blocked BuildPlan MUST NOT be treated as executable.

## 6. Human authority boundary

`approval.required = true` by default for any plan containing `PROPOSED` elements or protected decisions.

The System Builder may:

- derive steps from the Specification;
- identify dependencies;
- identify missing information;
- propose implementation alternatives;
- calculate deterministic metadata.

The System Builder may NOT:

- silently choose between materially different alternatives;
- resolve `UNRESOLVED` decisions;
- grant itself approval;
- widen authority scope;
- execute a blocked plan.

Canonical rule:

> **System suggests. Human decides.**

## 7. Provenance

Minimum required traceability:

`Specification Element → BuildPlan Element → provenance`

Every execution-relevant `DERIVED` step MUST identify the source Specification element(s).

Every `PROPOSED` element MUST identify:

- the Specification gap that caused the proposal;
- the proposal itself;
- the fact that human approval is required.

Every `UNRESOLVED` element MUST identify the unresolved source decision or missing information when such a source exists.

No execution-relevant element may exist without provenance classification.

## 8. Determinism

For the same canonical Specification and the same BuildPlan contract version:

- the derived BuildPlan content MUST be identical;
- step IDs MUST be stable;
- dependency ordering MUST be stable;
- canonical serialization MUST be stable;
- provenance MUST be stable;
- no timestamp, random value, model sampling result, or environment-specific value may alter derived semantics.

`PROPOSED` content is not considered deterministic unless its generation rule is itself deterministic; regardless, its origin remains `PROPOSED` and it remains subject to approval.

## 9. Execution state

BuildPlan generation and execution are separate state machines.

Allowed planning states:

`DRAFT → VALIDATED → BLOCKED | READY_FOR_APPROVAL`

Only an explicitly approved plan may transition to an execution-authorized state in a later session/contract.

SES-010 does **not** define or implement remote execution.

## 10. Acceptance criteria

A BuildPlan contract implementation is acceptable only if it can demonstrate that:

1. a valid Specification produces a structurally valid BuildPlan;
2. every derived execution-relevant element has provenance;
3. proposed elements are explicitly marked `PROPOSED`;
4. unresolved decisions remain `UNRESOLVED`;
5. blocked plans cannot be represented as executable/approved;
6. human approval cannot be synthesized by the transformer;
7. identical canonical inputs produce identical derived plans;
8. stable IDs and ordering are preserved;
9. invalid Specification input is rejected;
10. generation produces no execution side effects.

## 11. TDD gate

Before implementing the transformer, tests MUST be written for at least:

- valid Specification → derived BuildPlan;
- provenance preservation;
- deterministic identity;
- stable ordering;
- `PROPOSED` preservation;
- `UNRESOLVED` blocking;
- approval blocking;
- protected-decision blocking;
- invalid Specification rejection;
- no-execution-side-effect boundary.

## 12. Explicit non-goals

This contract does not define:

- production deployment;
- remote command execution;
- runtime orchestration;
- credentials or secret management;
- TrustGraph policy;
- governance policy;
- token/blockchain/mining;
- autonomous authorization;
- implementation technology choices not required by the Specification.

## 13. Canonical boundary

```text
Human Intent
    ↓
Intent Envelope
    ↓
Deterministic Validation
    ↓
Specification
    ↓
[SES-010]
Build / Execution Plan
    ↓
Human Approval
    ↓
[future session]
Execution
```

**SES-010 contract decision:** the BuildPlan is an auditable execution proposal, not execution authority.
