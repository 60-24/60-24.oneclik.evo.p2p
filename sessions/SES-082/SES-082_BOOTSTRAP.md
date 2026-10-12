# SES-082 — SESSION BOOTSTRAP

**Project:** P2P 60-24 OneClick Evo Positiv  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Previous checkpoint:** SES-081 — STONE  
**Session goal:** repo audit, clarity, evidence integrity; continue from actual repository state, not assumptions.

## 1. Communication and execution contract

Work autonomously within the repository. Be concise, minimize tokens, but inspect thoroughly.

Required workflow:
**INSPECT → UNDERSTAND → GAP → RED → IMPLEMENT → GREEN → EVIDENCE → STONE**

- Repository is the source of truth.
- First inspect the live `main` HEAD and working state; do not assume this bootstrap still matches HEAD.
- Do not invent a GAP to justify a change.
- Do not claim GREEN without observed test/CI evidence.
- Prefer one evidence-backed correction over broad refactoring.
- Do not change runtime, protocol, identity rules, or ontology during a documentation audit unless a concrete, demonstrated GAP requires it.
- Preserve useful history; distinguish historical notes from current normative documentation.
- No Docker/Kubernetes requirement; no 24/7 uptime assumption.
- Do not adopt libp2p/IPFS/mesh/CRDT/AI components without a demonstrated need and explicit architecture reasoning.
- No account purchases, billing changes, or other external commitments without user approval.

## 2. Project identity

This repository is the concrete **P2P 60-24 OneClick Evo Positiv** project, not the complete System Builder.

Current scope: minimal standalone P2P runtime / proof of concept for direct Node A ↔ Node B communication.

Known protocol path:
`local identity → HELLO/WELCOME/AUTH → authenticated peer → message → response`

Known implementation/evidence from earlier sessions includes Ed25519 identity and proof-of-possession, NodeID derived from the public key, TCP transport, framing/handshake checks, Linux and Windows builds, and Android APK CI. Re-verify all of this against current source and current runs before making fresh claims.

Not established as production-ready: end-to-end encryption, automatic peer discovery, NAT traversal, relay, GUI, automatic installer, and Internet-wide P2P operation. Treat these as explicit limitations, not automatically as current work items.

## 3. Previous engineering state

- SES-080 found and fixed a release integrity GAP: release builds must correspond to the exact tagged commit, not merely the latest successful build on `main`. Fix was recorded as commit `8b15db7ddbe81a3528ac55479514c018f9ac327e`; earlier release workflow run `37147128617` was reported SUCCESS.
- SES-081 introduced a transport abstraction: `src/p2p/transport.py`, `Transport` contract, `TCPTransport`, optional transport injection in `P2PNode`. Its closeout was recorded as STONE.
- Earlier CI runs were reported SUCCESS for evidence check, Linux executable, Windows executable, Android APK, runtime demo, and beta local execution. These are historical results; verify current workflow state and commit association rather than treating them as proof for later commits.

## 4. Documentation reorganization already applied

Documentation-only commits were made directly on `main`. Latest known commit in that series: `94c0144d959b4d9033993ec596c6aa184276bc0c6` (README stale HEAD pointer cleanup). Verify live HEAD before using this as a reference.

Added:
- `START_HERE.md` — entry point for humans and agents.
- `docs/CURRENT_STATE.md` — current-state snapshot.
- `docs/REPOSITORY_MAP.md` — repository navigation.
- `sessions/SES-080/SES-080_CLOSEOUT.md` — SES-080 evidence/closeout.

Updated:
- `README.md` — quick start, evidence boundary, known limitations.
- `sessions/README.md` — session-record conventions.
- `constitution/README.md` — clarifies authority and avoids implying that referenced/planned files necessarily exist.
- `PROJECT_GOAL_AND_CURRENT_STATE.md` — marked as historical System Builder material, not the current P2P specification.

No runtime/protocol change was made as part of this documentation reorganization.

**Verification boundary:** CI for the newest documentation commits was not confirmed in the prior session. Do not report the latest documentation state as GREEN until checked.

## 5. Canonical reading order

1. `START_HERE.md`
2. `README.md`
3. `docs/CURRENT_STATE.md`
4. `docs/REPOSITORY_MAP.md`
5. `sessions/README.md`
6. Relevant session closeouts and workflow definitions
7. Source code and tests — source and executable checks override stale prose.

## 6. First task in SES-082

Perform a read-only audit before editing:

1. Resolve current `main` HEAD and inspect the latest commits.
2. Compare `START_HERE.md`, `README.md`, `docs/CURRENT_STATE.md`, and `docs/REPOSITORY_MAP.md` against actual files, commands, protocol code, tests, and workflows.
3. Verify the actual command-line arguments and LAN instructions against the current implementation.
4. Inspect workflow triggers, artifact names, commit/tag binding, and available checks for the current HEAD.
5. Identify stale, conflicting, duplicated, missing, or overstated documentation. Check repository paths rather than assuming files exist.
6. Record findings as:
   - **FACT** — directly verified,
   - **GAP** — concrete mismatch or missing proof,
   - **UNKNOWN** — not verified.
7. Choose the single highest-value real GAP, or explicitly report **NO GAP FOUND** in the inspected scope.
8. Only then decide whether a minimal correction is justified. Run relevant checks, capture exact evidence, and write a closeout. If evidence cannot be obtained, leave the state open rather than declaring STONE.

## 7. Expected output

A short audit report:
- live HEAD SHA,
- scope inspected,
- confirmed facts,
- ranked concrete GAPs / unknowns,
- one recommended next action,
- exact verification evidence,
- state: OPEN / GREEN / STONE, with the meaning stated plainly.

Do not confuse a successful documentation write with a successful audit. Do not close SES-082 until the defined work and evidence are complete.
