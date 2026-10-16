# Tagologia — proposal v0.1 (EXPERIMENTAL)

**Status:** Proposal only — not approved canonical ontology, not runtime code  
**Project:** P2P 60-24 OneClick Evo Positiv  
**Related session:** SES-086  
**Autonomy zone:** RED for foundational ontology approval; YELLOW for future protocol/data-model integration

## 1. Purpose

Tagologia is a proposed semantic layer that represents a communicative intent as a typed, versioned structure rather than relying only on free text. It must complement the existing P2P runtime, not replace its transport, authenticated handshake, message framing, identity, or trust model.

**Target:** two nodes can validate the same structure and apply the same versioned interpretation rules. This guarantees neither that a claim is true nor that the receiver trusts the sender.

## 2. Non-goals

- No changes to HELLO/WELCOME/AUTH, TCP framing, NodeID or Ed25519 identity.
- No global person score, token, wallet, mining, payment or central semantic authority.
- No requirement for a central server, database engine, graph service or GUI.
- No claim of 100% agreement about reality or intent.
- No automatic promotion of frequently used patterns into canonical ontology.
- No dependency on free-text autocomplete for protocol correctness.

## 3. Layer boundary

1. **Interaction:** optional UI/autocomplete helps a human compose a statement.
2. **Semantic contract:** typed terms, composition rules, identifiers and schema version.
3. **Application message:** carries a serialized semantic statement inside the existing application-message boundary, once separately approved.
4. **P2P protocol/transport:** continues to deliver framed messages and authenticate the peer.
5. **Evidence and local trust:** remains separate from syntax and semantics.

A semantic validator must be usable without a UI. Unknown schema versions or unknown required terms must fail closed or be explicitly marked unsupported; they must not be silently guessed.

## 4. Candidate primitive types

The following seven types are a proposal mapped to SEE-MG vocabulary, not a frozen ontology decision:

| Type ID | SEE-MG concept | Role |
|---|---|---|
| `actor` | Actor | Entity participating in a statement |
| `state` | State | Property or condition, with explicit value/domain |
| `relation` | Relation | Typed, directed connection between references |
| `event` | Event | Occurrence with an identified subject and event type |
| `operation` | Operation | Requested or performed action |
| `memory` | Memory | Reference to recorded information/evidence, not truth by itself |
| `goal` | Goal | Desired condition or outcome |

These are structural categories, not an exhaustive domain vocabulary. A tag is a stable semantic identifier plus a definition; its display label is not its identity. Avoid treating every ordinary noun/adjective as a new primitive type.

## 5. Minimal term contract

Every term definition should have:
- stable namespaced `id`;
- `type` from the approved primitive vocabulary;
- human-readable label and concise definition;
- schema/ontology version;
- permitted value shape or reference type, where applicable;
- allowed composition rules or relation signature;
- lifecycle state: `experimental`, `proposed`, `accepted`, `deprecated`;
- provenance: who/what proposed it and which evidence or decision supports it.

Canonical IDs and versioning govern interpretation; localized labels may change without changing identity. No term may redefine another term silently.

## 6. Composition rules

A statement is valid only when:
1. its schema version is supported;
2. every required term ID exists in that version;
3. values match declared types and bounds;
4. relation signatures and required references are satisfied;
5. required fields occur exactly as specified;
6. unsupported extensions are rejected or explicitly isolated.

Do not impose the oversimplified rule that every relation must connect two actors or states. Each relation definition must declare its own signature and cardinality. Composition is a deterministic validation problem, not a promise that all possible combinations are meaningful.

## 7. Evolution and governance

Repeated use may generate a **candidate** compound term. Usage frequency is a discovery signal only; it is not proof of correctness, safety, usefulness or consensus.

Lifecycle:
`observed pattern → candidate → reviewed definition + examples → explicit approval → versioned publication → local adoption`

- No arbitrary universal threshold such as 100 uses.
- No automatic canonical promotion.
- Conflicting definitions remain explicit conflicts; nodes do not silently overwrite one another.
- Human approval is required before a proposal becomes canonical ontology.
- Local nodes may experiment with candidates without representing them as universally understood.

## 8. First PoC domain: resource request

Use a small closed domain such as “request to make a resource available”. The PoC should include a compact vocabulary (target: about 20 terms), valid examples and invalid examples. It must distinguish request, offer, acceptance, refusal, availability state and evidence of an action.

Required demonstrations:
- two independently validated examples have the same normalized representation;
- malformed type, missing reference, invalid relation signature and unsupported schema version are rejected;
- a syntactically valid statement is not automatically treated as true or trusted;
- unknown optional extensions are handled according to an explicit policy;
- the existing plain-text P2P path and handshake remain unchanged.

The initial PoC may run as a local validator and fixture suite. Network integration is a separate decision after contract validation.

## 9. Candidate acceptance criteria

- [ ] Primitive vocabulary and term identity are explicitly approved.
- [ ] Schema versioning and unknown-version behavior are specified.
- [ ] Valid and invalid resource-request fixtures are documented.
- [ ] Deterministic validation tests cover all composition rules.
- [ ] Serialization is canonical or has a deterministic normalization rule.
- [ ] Syntax, claim truth, evidence and local trust are demonstrably separate.
- [ ] No runtime/protocol change is made without a reviewed integration proposal.
- [ ] Human approval is recorded before this proposal is promoted into canonical ontology.

## 10. Decision requested

Approve, amend or reject the **conceptual direction and candidate seven-type vocabulary** before any canonical ontology or wire-format change. Until then this document remains experimental and has no authority over the current runtime.
