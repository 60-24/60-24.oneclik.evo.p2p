# SES-086 — Tagologia: test plan and GAP boundary

**Status:** Planning artifact; no implementation or test result claimed  
**Baseline branch:** `main` at inspection time: `3026d8149e2320a12ab0b0b6384d2242b459bd80`  
**Proposal branch:** `ses-086-tagology-proposal`

## INSPECT — verified facts

- The repository has an authenticated Node A ↔ Node B runtime and line-framed application messages.
- `src/p2p/protocol.py` currently defines HELLO/WELCOME/AUTH and Ed25519 proof-of-possession; it is not a semantic ontology module.
- `src/p2p/transport.py` defines the transport boundary; TCP is the current adapter.
- `architecture/README.md` and `ontology/README.md` identify canonical areas but do not yet define Tagologia.
- `AGENTS.md` and the Engineering Constitution require a human decision for foundational ontology and protocol/data-model changes.
- The latest main commit observed during inspection is `3026d8149e2320a12ab0b0b6384d2242b459bd80`, recording SES-085 EOF-after-AUTH evidence. Its recorded closeout reports Linux and Windows CI success on the tested regression commit `97d4d9efe7bff9b2cfd5c1e5e5ec975045295530`. The latest main commit's combined evidence status also reports success for `p2p/evidence`.

## UNDERSTAND

Tagologia belongs above transport and below user interaction: it defines a typed application meaning, while the existing P2P runtime delivers messages and authenticates peers. It must not conflate successful parsing with factual truth or trust.

## GAP

**Confirmed documentary gap:** there is no canonical Tagologia contract in the inspected architecture/ontology index.

**Not yet established:** whether a runtime semantic layer is needed now, what exact SEE-MG primitive vocabulary is already approved, and how an application envelope should carry semantic statements. These are not authorized implementation gaps yet.

## RED boundary

No production code, protocol, wire format, canonical ontology, trust behavior or existing test suite is changed in this proposal step. Approval is required before the candidate vocabulary becomes canonical or affects network messages.

## RED/GREEN plan after approval

1. Freeze the approved contract and a schema-version policy.
2. Add fixture-based tests for a pure validator, initially without network integration.
3. RED: show the tests reject malformed statements and unsupported required versions.
4. Implement the smallest pure validator and deterministic normalizer.
5. GREEN: test valid statements, unknown terms, missing references, invalid relation signatures, invalid values, duplicate/extra fields and schema-version mismatches.
6. Use a small resource-request vocabulary; target around 20 domain terms only if the examples prove it is sufficient.
7. Add a two-node serialization test only after the application-message integration contract is approved.
8. Run the relevant CI workflows and record the exact commit SHA and run URLs.
9. Update current-state documentation only after implementation evidence exists.

## Initial test matrix

| Case | Expected result |
|---|---|
| Valid resource request under supported schema | Accept; deterministic normalized structure |
| Unknown required term ID | Reject as unsupported/unknown |
| Unsupported schema version | Reject as unsupported; no guessed interpretation |
| Missing required reference | Reject |
| Wrong value type/domain | Reject |
| Relation endpoint violates declared signature | Reject |
| Duplicate field where schema disallows duplicates | Reject |
| Valid syntax but no evidence for the claim | Parse succeeds; truth remains unverified |
| Authenticated sender with semantically invalid message | Semantic validation rejects; authentication status is not converted into trust |
| Same statement with different display labels/locales | Same canonical IDs and semantic interpretation |

## Evidence boundary

This file records repository inspection and a future test plan. It does **not** claim that a Tagologia implementation exists, tests have run, or semantic communication works between nodes.
