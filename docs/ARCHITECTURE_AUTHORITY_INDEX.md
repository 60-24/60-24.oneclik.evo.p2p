# Architecture & Authority Index

**Status:** DOCUMENTARY / NON-NORMATIVE.  
**Inspected:** 2026-10-19.  
**Purpose:** help contributors distinguish approved governance, working models, proposals, history and deferred ideas. This index does not approve or freeze architecture.

## Status rules

- **Existing governance:** defines engineering process or authority.
- **Working model:** useful for exploration; not canonical approval.
- **Proposed for human approval:** not approved merely because the file exists.
- **Historical/reference:** records prior reasoning; not binding by itself.
- **Planned area:** README describes intended content not present in the checked directory.
- **Parked/experimental:** deferred; do not integrate without reopening the decision.

## Governance and current direction

| Artifact | Observed status | Boundary |
|---|---|---|
| `P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md` | Existing engineering governance | Does not replace the higher-level Project Constitution or ontology. |
| `constitution/README.md` | Index; planned areas disclosed | Explicitly warns that listed project-constitution and frozen-invariant documents are not proven to exist. |
| `docs/SYSTEM_BUILDER.md` | Architectural direction | Defines the pipeline; does not blanket-approve historical artifacts. |
| `docs/REPOSITORY_MAP.md` | Repository orientation | Explains areas and source-of-truth boundaries. |
| `docs/CURRENT_STATE.md` | Runtime snapshot dated 2026-10-07 | Not a current CI report; verify against code, tests and workflow evidence. |

## Constitution and ontology

- `ontology/README.md`: the checked `ontology/` directory contains only this README. Canonical concepts, entities, relations and invariants are described as planned areas, not yet represented there by specific ontology files.
- Project Constitution / frozen-invariant files listed in `constitution/README.md`: their existence and approval were not established by this inspection. Do not infer either from historical references.

## Graph decisions

| Artifact | Declared status | Safe interpretation |
|---|---|---|
| `sessions/SES-003/DEC-005_SYSTEM_BUILDER_GRAPH_BACKBONE.md` | APPROVED | Graph is the structural backbone of System Builder; this does not approve a specific storage technology or every downstream contract. |
| `sessions/SES-003/DEC-006_SYSTEM_BUILDER_GRAPH_INVARIANTS.md` | APPROVED | Approved semantic graph invariants; this does not automatically approve other graph decisions or a technology choice. |
| `sessions/SES-003/DEC-007_SYSTEM_BUILDER_GRAPH_SEMANTIC_MODEL_AND_CONTRACTS.md` | PROPOSED FOR HUMAN APPROVAL | Not approved canonical ontology. |
| `sessions/SES-003/DEC-008_SYSTEM_BUILDER_SCHEMA_INDEPENDENT_GRAPH_CONTRACT_TESTS.md` | PROPOSED FOR HUMAN APPROVAL | Proposed conformance contract/tests; do not treat as approved active conformance proof. |
| `sessions/SES-003/DEC-009_SYSTEM_BUILDER_GRAPH_CONFORMANCE_SCENARIOS.md` | PROPOSED FOR HUMAN APPROVAL | Proposal only. |
| `sessions/SES-004/DEC-011_SYSTEM_BUILDER_GRAPH_TECHNOLOGY_EVALUATION_FRAMEWORK.md` | PROPOSED FOR HUMAN APPROVAL | Not a technology selection. |
| `sessions/SES-004/DEC-012_SYSTEM_BUILDER_GRAPH_CANDIDATE_EVALUATION_MATRIX.md` | PROPOSED FOR HUMAN APPROVAL | Not proof of final selection. |
| `sessions/SES-004/DEC-013_SYSTEM_BUILDER_GRAPH_CANDIDATE_SET_AND_EVALUATION_PROTOCOL.md` | PROPOSED FOR HUMAN APPROVAL | Evaluation proposal only. |
| `sessions/SES-003/DEC-010_SYSTEM_BUILDER_GRAPH_REFERENCE_TEST_MATRIX_AND_ACCEPTANCE_CRITERIA.md` | PROPOSED FOR HUMAN APPROVAL | Reference acceptance matrix proposal; not an approved test gate. |
| `sessions/SES-004/DEC-014_SYSTEM_BUILDER_GRAPH_CANDIDATE_REGISTRY.md` | ACCEPTED BY HUMAN | Candidate evaluation preparation/registry only; does not itself approve a graph technology. |
| `sessions/SES-004/DEC-015_SYSTEM_BUILDER_GRAPH_CONCRETE_CANDIDATE_REGISTRY.md` | ACCEPTED BY HUMAN | Concrete candidate registry only; does not itself approve a graph technology. |
| `sessions/SES-004/G-01_NEO4J_REPRODUCIBLE_RUNTIME_SETUP.md` | PREPARED FOR EXECUTION | Candidate conformance evaluation setup only; explicitly not production architecture or technology selection. |

## System Builder and Kernel-DNA

| Artifact | Declared status | Safe interpretation |
|---|---|---|
| `sessions/SES-006/02_SYSTEM_BUILDER_MINIMAL_MODEL.md` | WORKING MODEL — NOT CONSTITUTIONAL APPROVAL | Useful minimal object/traceability model; not an approved constitutional contract. |
| `sessions/SES-046/SES-046_MICROKERNEL_GENEALOGY.md` | GREEN CHECKPOINT — session audit | Terminology analysis; explicitly does not modify Constitution, ontology or frozen architecture. Not a canonical Kernel-DNA specification. |
| `docs/history/PROJECT_HISTORY_6_MONTHS.md` | Historical synthesis | Context and provenance, not a substitute for approved current artifacts. |

## Runtime evidence

The P2P runtime is a concrete tested system and must be evaluated separately from the broader System Builder meta-architecture.

- Runtime snapshot: `docs/CURRENT_STATE.md`
- Verification map: `docs/REPOSITORY_MAP.md`
- SES-085 evidence: `sessions/SES-085/SES-085_CLOSEOUT.md`
- Linux and Windows regression workflows: `.github/workflows/build-p2p-linux.yml` and `.github/workflows/build-p2p-windows.yml`

CI evidence applies to the tested commit and checks only. It does not approve ontology or prove production readiness.

## Deferred proposal

- `docs/TAGOLOGY_DEFERRED.md`: PARKED / EXPERIMENTAL. Preserve Tagologia as one possible system entity; do not pursue perfection or integrate it into runtime now.
- PR #13: open Draft and not merged at last check. Keep it separate from `main`; revisit only when a concrete need justifies it.

## Rule for future changes

1. Locate the source artifact and declared authority.
2. Distinguish a concept from historical discussion and proposals.
3. State a concrete GAP and evidence.
4. For Constitution, foundational ontology, Trust, security/governance or cross-layer contracts, stop for the human decision required by the Engineering Constitution.
5. Never let a proposal become canonical through repetition or directory placement alone.

**Conclusion:** this index improves navigation and exposes authority gaps; it does not resolve them by itself.
