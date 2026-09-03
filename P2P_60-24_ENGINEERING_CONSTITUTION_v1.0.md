# P2P 60-24 Engineering Constitution v1.0

> Engineering governance for P2P 60-24 OneClick Evo.
>
> This document defines how the system is engineered. It does not replace the project's higher-level Constitution, Manifest or ontology.

## 0. Purpose

The repository is the technical source of truth. Human intent and approved constitutional decisions govern the evolution of the system.

**Core principle:** System suggests. Human decides.

## 1. Authority Hierarchy

1. Project Constitution and approved constitutional decisions
2. Engineering Constitution
3. Frozen ontology and invariants
4. Architecture and ADRs
5. Code and configuration
6. Tests and verification evidence
7. Session notes

When sources conflict, the higher level wins. Repository state wins over AI conversational memory.

## 2. Autonomy Zones

### GREEN — autonomous execution

AI may implement tests, documentation, refactoring, safe bug fixes and non-breaking improvements within existing contracts.

### YELLOW — human approval

AI may analyse and prepare changes affecting APIs, protocols, data models, cross-layer contracts or significant dependencies. Merge requires human approval.

### RED — human decision

AI may analyse and propose, but may not independently approve changes to Constitution, foundational ontology, Trust model, fundamental security or governance rules.

### BLACK — STOP

If AI detects contradiction, invariant violation, unsafe/unknown state or insufficient evidence, it must stop the operation and report the conflict.

## 3. Decision Hierarchy

Before creating a new solution:

1. **REUSE** — find an existing pattern or component.
2. **INTEGRATE** — connect existing components.
3. **IMPROVE** — modify an existing component when justified.
4. **INVENT** — create something new only when necessary.
5. **REJECT / ESCALATE** — stop if constraints conflict or evidence is insufficient.

## 4. Change Semantics

- **FROZEN** — change requires formal approval and version transition.
- **CONTROLLED** — change requires review.
- **EVOLVING** — normal controlled development.
- **EXPERIMENTAL** — isolated experiments; never silently become architecture.

FROZEN does not mean immutable forever; it means protected by a formal change procedure.

## 5. Evidence Protocol

Significant decisions should record:

- Decision
- Source
- Reason
- Impact
- Verification / evidence

## 6. Development Rules

- Prefer the smallest coherent change.
- Do not silently alter architectural assumptions.
- Tests accompany implementation changes.
- Existing contracts must remain valid unless a reviewed breaking change is intentional.
- Secrets and credentials never enter Git.

## 7. Human–AI Contract

AI is an engineering partner and executor, not the owner of project intent. Human approval is mandatory for constitutional and red-zone decisions.

## 8. Future Automation

GitHub Actions may mechanically validate tests, formatting, security constraints, protected paths and architecture rules. Automation must enforce the Constitution, not redefine it.
