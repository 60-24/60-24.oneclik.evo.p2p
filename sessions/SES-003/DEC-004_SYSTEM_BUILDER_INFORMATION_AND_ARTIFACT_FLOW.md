# SES-003 — DEC-004

## System Builder — Information and Artifact Flow

**Status:** APPROVED  
**Session:** SES-003  
**Previous decisions:** DEC-001, DEC-002, DEC-003

## 1. Principle

The System Builder operates as a sequence of explicit transformations. Each stage consumes and produces identifiable artifacts and preserves traceability between them.

The System Builder must not silently bypass the modeling, design, contract or verification layers in order to move directly from human intent to implementation.

## 2. Canonical Flow

```text
HUMAN INTENT
     ↓
[INTENT]
Intent Model
     ↓
[MODEL]
System Graph
     ↓
[DESIGN]
Architecture / Design
     ↓
[CONTRACT]
Contracts + Invariants
     ↓
[BUILD]
Implementation Artifacts
     ↓
[VERIFY]
Tests + Observations
     ↓
[EVIDENCE]
Evidence Record
     ↓
[VALIDATION]
Validated System State
     ↓
[OBSERVE]
Runtime Observations
     ↓
[EVOLVE]
Change Proposal
     ↺
MODEL / DESIGN
```

## 3. Traceability Requirement

Every significant artifact, decision and claim should maintain explicit relationships in the project graph where applicable:

- `DERIVED_FROM`
- `IMPLEMENTS`
- `CONSTRAINED_BY`
- `VERIFIED_BY`
- `SUPPORTED_BY_EVIDENCE`
- `CHANGED_BY`

These relations are part of the intended Graph Engineering model and are not merely documentation conventions.

## 4. Evidence Chain

Significant claims follow the project's evidence-first chain:

```text
CLAIM
  ↓
TEST / OBSERVATION
  ↓
EVIDENCE
  ↓
VALIDATION
  ↓
CONFIDENCE
```

A generated artifact, model output or AI assertion is not by itself proof of correctness.

## 5. No Silent Skipping

A System Builder operation may simplify or combine stages only when the semantic and traceability requirements of the skipped representation are preserved explicitly.

A direct transition such as:

```text
HUMAN IDEA → CODE
```

is therefore not the canonical System Builder process.

The canonical transformation is:

```text
INTENT → MODEL → DESIGN → CONTRACT → BUILD → VERIFY → EVIDENCE → VALIDATION
```

## 6. Evolution Loop

Observation of the running Target System can produce an evidence-backed change proposal. Evolution returns to the model/design layer rather than modifying the system through an untracked mutation path.

```text
OBSERVE → EVIDENCE → CHANGE PROPOSAL → HUMAN/AUTHORITY REVIEW → MODEL/DESIGN → BUILD → VERIFY
```

## 7. Consequence for Architecture

This decision establishes the information-flow foundation for System Builder. Concrete agents, services, databases, programming languages or runtime technologies are deliberately deferred until the capability and contract models justify them.

## 8. Governing Principle

> **No important system transformation without a traceable meaning, decision, artifact and verification path.**
