# SES-086 — Tagologia worked example H / S / bridge

**Status:** illustrative fixture proposal; not canonical and not a runtime contract  
**Purpose:** check whether the two-layer model reduces ambiguity without hiding uncertainty.

## 1. Human layer (H)

Example concept records (IDs are illustrative):

| ID | Label | Definition / boundary |
|---|---|---|
| `h:resource` | zasób | Identifiable item that may be referenced in a request. Does not imply ownership or permission. |
| `h:share` | udostępnienie | Making a specified resource available to another identified party under explicit conditions. |
| `h:read-only` | tylko do odczytu | Permission to inspect a resource without modifying it. Does not imply permission to copy, redistribute, or retain it. |
| `h:request` | prośba | A request for a decision; it is not itself authorization. |
| `h:accept` | akceptacja | An explicit response accepting a particular request under stated scope and conditions. |
| `h:trust` | zaufanie | A contextual assessment by an actor; not a universal property and not equivalent to authorization. |

Ambiguity fixture:

- Phrase: “Udostępnij mi raport.”
- Missing context: which report, which recipient identity, which operations, duration, and whether copying is allowed.
- H result: mark the request **underspecified**; ask for missing context. Do not infer permission to edit or redistribute.

A definition may be accepted for a stated context without claiming that all people use the word identically. Competing interpretations and their provenance remain visible.

## 2. System layer (S)

Illustrative JSON statement only. It must not be treated as an approved protocol message:

```json
{
  "schema": "urn:60-24:tagologia-s:resource-request",
  "version": "0.1",
  "kind": "resource.request",
  "statement_id": "urn:example:statement:001",
  "subject": {"type": "principal", "id": "principal:requester-7"},
  "resource": {"type": "resource", "id": "resource:report-17"},
  "requested_operations": ["read"],
  "constraints": {
    "copy": false,
    "expires_at": "2026-12-01T00:00:00Z"
  },
  "references": []
}
```

The schema must separately define allowed identifiers, timestamp rules, required fields, unknown-field handling, and validation errors. A valid request is **not** an authorization decision. A separate authorized decision must identify the request and its scope.

## 3. Explicit bridge H↔S

| H concept | S term/field | Mapping | Limitation |
|---|---|---|---|
| `h:resource` | `resource.type=resource` | Exact for the identifier role only | Does not establish ownership or existence. |
| `h:read-only` | `requested_operations=["read"]` | Partial/context-bound | Read permission does not settle copying, retention, or onward sharing unless specified. |
| `h:request` | `kind=resource.request` | Exact for message intent | Does not grant permission. |
| `h:trust` | No direct field | Unmapped | Do not convert a human trust judgment into authorization or a global score. |

Mapping metadata should include H concept ID and revision, S schema ID and version, direction, scope, mapping status, and lossiness. Any future change is versioned; old statements retain their original interpretation.

## 4. Negative fixtures (must fail safely)

1. Missing resource ID → reject as incomplete; do not guess which resource.
2. Unknown required schema version → return unsupported-version; do not parse using a guessed version.
3. `requested_operations=["read","delete"]` where delete is not in the schema → reject.
4. A valid request with no authorization decision → status remains **not authorized**.
5. Authenticated requester but no permission policy/decision → identity is established, authorization is not.
6. Mapping `h:read-only` to unrestricted access → fail bridge review as overbroad.
7. Two conflicting H definitions under the same label → retain both with context/provenance; do not silently merge.
8. Change a display label in H → S stable ID and existing messages remain unchanged.

## 5. Measurable acceptance checks

This example is useful only if a local fixture/validator can demonstrate all of the following:

- **Determinism:** same valid input normalizes to byte-identical canonical output.
- **No guessing:** every missing/unsupported/ambiguous case returns a named error or explicit unresolved state.
- **Separation:** tests independently assert syntax validity, semantic support, factual evidence, identity, authorization, and local trust.
- **Bridge honesty:** every mapping declares scope and lossiness; a lossy mapping cannot pass as exact.
- **Evolution:** changing H labels/definitions does not silently mutate an S schema or historic statement.
- **Human comprehension:** a reviewer can identify what is requested, by whom, for which resource, with what limits, and what remains undecided without reading implementation code.

No test is claimed to have run. After human approval of the model, implement fixtures first, then a pure local validator; do not connect this example to the P2P runtime in this step.
