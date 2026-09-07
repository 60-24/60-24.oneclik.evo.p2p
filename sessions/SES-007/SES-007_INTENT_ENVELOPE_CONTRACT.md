# SES-007 — SYSTEM BUILDER INTENT ENVELOPE CONTRACT

**Status:** DRAFT — canonical contract for SES-007 implementation
**Scope:** System Builder only
**Target:** reusable input/interpretation layer used to build P2P 60-24 OneClick Evo Positiv

## 1. Purpose

The Intent Envelope is the deterministic boundary between human intent and System Builder interpretation.

Flow:

`Human Intent → Intent Envelope → Validation → Specification`

The envelope must preserve what the human explicitly requested without silently converting assumptions into requirements.

## 2. Canonical fields

```yaml
intent_id: stable identifier
version: integer
objective: explicit desired outcome
requirements: []
constraints: []
assumptions: []
optional_information: []
open_questions: []
protected_decisions: []
authority: human | system
status: VALID | INCOMPLETE | AMBIGUOUS | PROTECTED
```

## 3. Semantic classes

### REQUIREMENT
Explicitly requested outcome or behavior. May be transformed into specification.

### CONSTRAINT
Explicit boundary that the builder must respect.

### ASSUMPTION
Information introduced to make interpretation possible but not explicitly authorized by the human. Assumptions must remain visible and cannot silently become requirements.

### OPTIONAL_INFORMATION
Useful context that does not affect correctness unless explicitly promoted to a requirement or constraint.

### OPEN_QUESTION
Missing information whose resolution may change the resulting specification. It blocks a deterministic interpretation when material.

### PROTECTED_DECISION
A constitutional, ontological, governance, trust-foundation, security-authority, or other explicitly protected decision. The System Builder may identify and propose it, but may not decide it autonomously.

## 4. Validation states

### VALID
All material information is sufficiently explicit; no unresolved material ambiguity exists; no protected decision requires autonomous choice.

### INCOMPLETE
A material input is missing. The builder must identify the missing information and stop the affected interpretation path.

### AMBIGUOUS
Two or more materially different interpretations remain possible. The builder must not select one silently.

### PROTECTED
The requested outcome requires a protected decision. The builder may prepare alternatives and evidence but must stop before making the protected decision.

## 5. Determinism rules

1. Same normalized Intent Envelope + same builder contract version MUST produce the same validation classification.
2. Field ordering MUST NOT change semantic identity.
3. Stable identifiers MUST be derived from canonical normalized content, not runtime ordering.
4. Assumptions MUST NOT be promoted to requirements without explicit human authorization.
5. Open questions MUST remain explicit until resolved.
6. Protected decisions MUST never be auto-resolved.
7. `UNKNOWN` is not `VALID`.

## 6. Normalization

Before validation:

- normalize field names to the canonical schema;
- normalize whitespace and line endings;
- preserve semantic text content;
- normalize list ordering only where order has no declared semantic meaning;
- assign stable identifiers from canonical content;
- record the contract version used for validation.

Normalization MUST NOT change the meaning of the human intent.

## 7. Traceability

Every generated specification element MUST reference the originating Intent Envelope element.

Minimum chain:

`intent_id → intent_element_id → specification_element_id → artifact_id → verification_evidence_id`

If traceability cannot be established, the affected result is not verified.

## 8. Human authority gate

The System Builder operates under:

**System suggests. Human decides.**

The builder may interpret, model, implement, test and verify within declared authority. It must stop and request human decision for protected decisions.

## 9. Acceptance tests

The SES-007 implementation MUST demonstrate at least:

1. VALID intent is accepted deterministically.
2. INCOMPLETE intent identifies the missing material information.
3. AMBIGUOUS intent identifies the competing interpretations.
4. PROTECTED intent is blocked from autonomous decision-making.
5. Repeated validation of the same normalized envelope returns the same classification.
6. Traceability identifiers remain stable across repeated validation.
7. Assumptions remain distinguishable from requirements.

## 10. Non-goals

This contract does not select Neo4j or another graph technology, implement the P2P runtime, introduce tokens/blockchain/mining, or authorize unrestricted autonomous execution.

## 11. Exit criterion

SES-007 may close only when this contract is implemented, covered by executable tests, and produces verification evidence for VALID, INCOMPLETE, AMBIGUOUS and PROTECTED cases.
