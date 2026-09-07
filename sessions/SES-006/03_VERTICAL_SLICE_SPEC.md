# SES-006 — Vertical Slice Specification

**Status:** WORKING SPECIFICATION — NOT CONSTITUTIONAL APPROVAL  
**Session:** SES-006  
**Purpose:** Prove the minimal System Builder chain with one small, local, deterministic task.

---

## 1. Selected Vertical Slice

### VS-001 — Build a Project Specification from Human Intent

The System Builder receives a small human request and produces a structured Markdown specification plus a machine-readable JSON representation.

Example intent:

> "Create a small local utility that reads a text file and reports the number of lines, words and characters. It must not modify the input file or access the network."

The slice is intentionally generic and unrelated to P2P runtime functionality.

---

## 2. Why This Slice

VS-001 exercises the core System Builder capability without introducing unnecessary infrastructure.

It tests:

- intent capture;
- normalization;
- explicit assumptions;
- constraints;
- acceptance criteria;
- machine representation;
- artifact generation;
- deterministic validation;
- traceability.

It does **not** require Neo4j, networking, distributed execution, blockchain, tokens, or autonomous deployment.

---

## 3. Input Contract

Input consists of:

```text
Intent.statement
Intent.constraints
Intent.acceptance_criteria
```

The System Builder must preserve the original intent and separately record its normalized interpretation.

If the intent is ambiguous, the ambiguity must become an explicit `open_question` or documented assumption. It must not be silently invented away.

---

## 4. Required Outputs

VS-001 must produce:

1. `specification.md`
2. `specification.json`
3. `verification.json`
4. a delivery manifest linking all outputs.

The JSON representation must contain at minimum:

```text
id
intent
purpose
inputs
outputs
constraints
assumptions
open_questions
acceptance_criteria
status
```

---

## 5. Acceptance Criteria

VS-001 succeeds only when all conditions are true:

- [ ] original Intent is preserved;
- [ ] Specification is explicitly derived from Intent;
- [ ] all stated constraints are represented;
- [ ] assumptions are explicit;
- [ ] open questions are explicit when applicable;
- [ ] acceptance criteria are testable;
- [ ] Markdown and JSON representations describe the same specification;
- [ ] generated files are deterministic for identical input;
- [ ] output files have content hashes;
- [ ] verification evidence identifies what was checked;
- [ ] delivery manifest links the outputs to their source specification;
- [ ] no network access is required;
- [ ] no remote code execution is required;
- [ ] no protected project decision is changed.

---

## 6. Test Scenarios

### T-001 — Valid Intent

Input contains a clear purpose, constraints and measurable acceptance criteria.

Expected result: valid Specification and successful verification.

### T-002 — Ambiguous Intent

Input contains an unresolved requirement.

Expected result: ambiguity is represented as an `open_question`; the System Builder does not silently guess a protected requirement.

### T-003 — Constraint Preservation

Input contains a safety or scope constraint.

Expected result: the constraint appears unchanged in the normalized Specification.

### T-004 — Deterministic Rebuild

The same Intent is processed twice.

Expected result: equivalent normalized outputs and reproducible content hashes, excluding explicitly dynamic metadata.

### T-005 — Traceability Failure

Attempt to produce a delivery package without a source specification or verification evidence.

Expected result: delivery is rejected.

### T-006 — Protected Change

Attempt to alter a protected project invariant through the normal build path.

Expected result: execution stops and the decision is escalated to the appropriate human authority.

---

## 7. Safety Boundary

The Vertical Slice runs locally in a bounded environment.

Allowed:

- read explicitly supplied input;
- transform text/data;
- create local output files;
- calculate hashes;
- run deterministic validation tests.

Not allowed:

- arbitrary network access;
- secrets access;
- unrestricted shell execution;
- modification of unrelated repository files;
- changes to Constitution or protected ontology;
- autonomous production deployment.

---

## 8. Minimal Execution Pipeline

```text
1. Receive Intent
2. Validate Intent envelope
3. Normalize → Specification
4. Validate Specification
5. Serialize Specification → Markdown + JSON
6. Hash generated artifacts
7. Execute validation tests
8. Produce Verification Evidence
9. Build Delivery Manifest
10. Deliver only if verification passes
```

Every step should have an observable result.

---

## 9. Definition of Done

VS-001 is complete when the complete chain works locally:

```text
Human Intent
   ↓
Specification
   ↓
Artifacts
   ↓
Tests
   ↓
Verification Evidence
   ↓
Delivery Manifest
```

and the chain can be repeated with the same input to obtain the same substantive result.

The purpose of VS-001 is **not** to build the final System Builder. Its purpose is to prove the smallest complete loop on which the System Builder can safely evolve.

---

## 10. Next Engineering Step

After this specification is accepted as the working basis, implement only the minimal local execution path required by VS-001.

Do not expand the architecture before the slice produces evidence that expansion is necessary.
