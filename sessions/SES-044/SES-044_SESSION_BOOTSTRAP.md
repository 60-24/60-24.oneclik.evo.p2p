# SES-044 — Standalone Downloadable P2P Node

**Date:** 2026-09-15  
**Status:** VERIFICATION PENDING  
**Project:** P2P 60-24 OneClick Evo  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. Previous stone

SES-043 = **GREEN / CLOSED**.

Verified evidence:

- two independent local node processes,
- connection A → B,
- message A → B,
- response B → A,
- GitHub Actions run `34928265888`, job `two-node-proof` = SUCCESS.

The SES-043 TCP transport is an experimental local proof only, not a final architecture decision.

## 2. User-defined next requirement

The next useful deliverable is now explicit:

> **A small downloadable program that can be started as two independent nodes and make a P2P connection between them.**

The program must:

- be a single downloadable Python file;
- require Python 3.x only;
- require no external packages;
- support one node in listen mode;
- support a second node in connect mode;
- exchange a message and response;
- be executable on the same LAN when the listener address is reachable.

## 3. INSPECT → GAP

Existing `src/p2p/node.py` already proves the communication primitive, but it is package-oriented and requires the repository source layout. That does not yet satisfy the simplest user-facing **download one file → run two nodes** requirement.

Therefore the smallest coherent GAP is a standalone root-level executable script.

## 4. RED contract

Added:

`sessions/SES-044/test_downloadable_two_nodes.py`

Commit:

`4a62e3b733bd8ededbf87d6c04019e12ba013c34`

The test requires two independently started processes using `p2p_node.py`, with A connecting to B and receiving `pong-from-B`.

## 5. Implementation

Added:

`p2p_node.py`

Commit:

`dc725a6040abe9cd43cc69cc3f431150c44762dd`

The program uses only Python standard-library TCP sockets.

## 6. Automated proof

Added:

`.github/workflows/ses-044-p2p-download.yml`

Commit:

`3a4aee3b0cabbc53479656b3b886c2b4ff189b78`

The workflow executes the SES-044 two-node test on pushes to `main` and pull requests.

## 7. User documentation

Added:

`P2P_NODE.md`

Commit:

`17f7f04a40713b19e0e84bedb159c2ef7057f4cc`

It contains copy/paste commands for node B and node A, including the LAN usage case.

## 8. Current verification boundary

Implementation exists and is documented. **Do not mark SES-044 GREEN yet.**

Required final evidence:

1. SES-044 standalone two-node CI job = SUCCESS;
2. verify the final `main` commit contains the program, test and documentation;
3. only then close the session with a stone.

## 9. Hard boundaries

Do not introduce without explicit requirement and appropriate decision level:

- Trust / LocalTrust / RealBond,
- blockchain / token / payments,
- central server,
- libp2p,
- broad discovery architecture,
- Internet production deployment,
- GUI,
- persistence,
- swarm/agent architecture,
- final transport commitment.

## 10. Scope

SES-044 is proving a **downloadable minimal two-node communication program**, not a production P2P network.

It does not yet prove:

- discovery,
- NAT traversal,
- authentication,
- encryption,
- persistence,
- Internet production readiness,
- final transport architecture.
