# SES-008 — Specification Contract

**Status:** IMPLEMENTED — pending CI verification  
**Source:** validated SES-007 Intent Envelope  
**Contract version:** 1

## 1. Purpose

A `Specification` is the machine-representable form of a **VALID** Intent Envelope.
It makes the intended system explicit without granting the builder authority to invent unresolved or protected decisions.

## 2. Contract

```text
Specification
├── specification_id
├── source_intent_id
├── version
├── status
├── objective
│   ├── statement
│   ├── source_intent_id
│   ├── source_field
│   └── origin
├── requirements[]
│   ├── id
│   ├── statement
│   ├── source_element_id
│   └── origin
├── constraints[]
│   ├── id
│   ├── statement
│   ├── source_element_id
│   └── origin
├── inputs[]
├── outputs[]
├── acceptance_criteria[]
├── assumptions[]
│   ├── id
│   ├── statement
│   ├── source_element_id
│   └── origin
├── unresolved_decisions[]
├── provenance[]
│   ├── source_intent_id
│   ├── source_element_id
│   ├── specification_element_id
│   └── origin
└── authority
```

## 3. Origin semantics

- `DERIVED` — directly follows from validated Intent; may be produced deterministically.
- `PROPOSED` — builder proposal; requires explicit human decision before authority is granted.
- `UNRESOLVED` — not decided; must not become an executable choice.

SES-008 currently generates only `DERIVED` elements. It does not silently generate `PROPOSED` or `UNRESOLVED` decisions.

## 4. Blocking rule

Only `VALID` Intent Envelopes can be transformed.

`INCOMPLETE`, `AMBIGUOUS`, and `PROTECTED` states are hard blockers.

> **Brak informacji ≠ zgoda na jej wygenerowanie.**

## 5. Provenance

Minimum traceability:

`Intent Element → Specification Element → provenance → source_intent_id / source_element_id`

Requirements, constraints, and assumptions retain their SES-007 `element_id` as `source_element_id`.
The objective is traced explicitly by `source_intent_id + source_field=objective`, because SES-007 currently models objective as a top-level field rather than an element-id entry.

## 6. Determinism

For the same normalized Intent Envelope and Specification contract version:

- the resulting Specification is identical;
- list ordering does not change semantic identity;
- IDs derive from canonical content;
- assumptions remain assumptions;
- unresolved/protected decisions cannot be silently resolved.

## 7. Authority boundary

The Specification is a representation of intent, not authorization for autonomous execution.
Human authority remains authoritative for protected and unresolved decisions.
