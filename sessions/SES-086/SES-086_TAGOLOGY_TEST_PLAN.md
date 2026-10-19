# SES-086 — test plan for Tagologia H / S / bridge

**Status:** planning only; no implementation or test result claimed  
**Base inspected:** main at 3026d8149e2320a12ab0b0b6384d2242b459bd80  
**Proposal:** architecture/proposals/TAGOLOGY_PROPOSAL_v0.1.md

## INSPECT — verified facts

- The repository has an authenticated Node A ↔ Node B runtime and line-framed application messages.
- src/p2p/protocol.py defines HELLO/WELCOME/AUTH and Ed25519 proof-of-possession; it is not a semantic ontology module.
- src/p2p/transport.py defines the transport boundary; TCP is the current adapter.
- architecture/README.md and ontology/README.md are indexes, not an approved Tagologia contract.
- Foundational ontology and network/data-contract changes require human approval under repository governance.
- The existing runtime, handshake, identity, and trust behavior remain out of scope for this design step.

## UNDERSTAND — proposed model

- **H:** human-readable concept repository with stable IDs, definitions, scope, relations, provenance, lifecycle, revisions, and explicit disagreements.
- **S:** machine-readable typed statement contract with explicit schema version, validation, deterministic normalization, and unknown-version policy.
- **H↔S:** optional, versioned mapping that records scope and whether translation is exact or lossy.
- H and S evolve independently. Neither is required to model every concept or field of the other.
- Correct syntax does not establish truth, evidence, authorization, identity, or local trust.

## GAP

**Confirmed documentary gap:** no approved contract currently defines the two-layer model and the H↔S boundary.

**Not yet authorized/established:** canonical H vocabulary, S schema, wire format, bridge mappings, or a runtime need. These are design decisions, not implementation gaps.

## RED boundary

Do not change production code, HELLO/WELCOME/AUTH, TCP framing, NodeID, trust behavior, canonical ontology, or network message format during proposal review. Do not claim semantic tests or GREEN without implementation and recorded CI evidence.

## Test sequence after human approval

### H PoC — concept consistency
- stable IDs are independent of display labels/locales;
- revision preserves prior definition and provenance;
- relation signature and required scope are checked;
- conflicting definitions remain visible rather than silently overwriting;
- deprecated concepts remain resolvable historically but cannot be mistaken for current accepted terms.

### S PoC — contract validation
- valid statement under supported schema accepted;
- unsupported schema version and unknown required term rejected as unsupported;
- missing required field/reference and wrong value type rejected;
- invalid relation signature and disallowed duplicate/extra field rejected;
- deterministic normalization yields identical canonical representation;
- syntactically valid but unsupported semantic extension is not guessed.

### Bridge PoC — explicit mapping
- known mapping produces expected target ID/version;
- missing or ambiguous mapping returns explicit unmappable/ambiguous result;
- lossy mapping is declared and never represented as exact;
- deprecated or changed mapping does not rewrite historical statements;
- round-trip equality is required only for mappings declared lossless.

### Separation invariants
- valid syntax does not imply factual truth;
- evidence reference does not itself prove the referenced claim;
- authenticated sender does not imply trust or authorization;
- human label changes do not silently alter S identity;
- H-only concept and S-only operational field are both allowed.

## Minimal first domain

Use a resource access/share request. Build only the terms required by fixtures; approximately 10–20 H concepts is a target ceiling, not a quota. Start with local fixture tests and pure validators. Network integration, UI, autocomplete, compact encoding, and AI-generated ontology promotion are out of scope until separately justified and approved.

## Evidence requirements

For every GREEN claim, record exact commit SHA, test command/workflow, result, and run URL. This plan itself is not evidence that implementation or tests exist.
