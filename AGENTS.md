# P2P 60-24 OneClick Evo — AI Agent Instructions

## Source of Truth
The Git repository is the authoritative technical source of truth. If conversation memory conflicts with repository content, repository content wins.

## Working Principle
Human defines intent and approves constitutional/architectural decisions. AI analyses, proposes, implements and verifies within defined autonomy boundaries.

## Decision Hierarchy
1. REUSE — find an existing solution.
2. INTEGRATE — connect existing components.
3. IMPROVE — modify an existing component when necessary.
4. INVENT — create a new concept only when justified.
5. REJECT / ESCALATE — stop when constraints conflict or evidence is insufficient.

## Autonomy Zones
- GREEN: implementation, tests, documentation, refactoring and safe fixes.
- YELLOW: API, protocol, data-model or cross-layer changes; prepare a proposal and request human approval.
- RED: Constitution, ontology foundations, Trust model, fundamental security/governance rules; human decision required.
- BLACK: detected contradiction, invariant violation, unsafe or unknown state; STOP and report.

## Required Workflow
1. Read the relevant Constitution, ontology and architecture documents.
2. Check autonomy zone and frozen constraints.
3. Search for existing patterns before inventing.
4. State a concise plan before non-trivial changes.
5. Implement the smallest coherent change.
6. Add/update tests.
7. Run applicable validation.
8. Report evidence, changed files and unresolved risks.

## Evidence Protocol
Every significant decision should identify: decision, source, reason, impact and verification/evidence.

## Do Not
- introduce financial tokens or wallets;
- turn Trust Infrastructure into a payment or rating system;
- create opaque global person scores;
- silently change constitutional or ontological assumptions;
- store secrets in the repository.
