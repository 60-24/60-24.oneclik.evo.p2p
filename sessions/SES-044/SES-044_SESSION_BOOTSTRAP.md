# SES-044 — Standalone Downloadable P2P Node

**Date:** 2026-09-15  
**Status:** GREEN / CLOSED  
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

## 2. User-defined requirement

> **A small downloadable program that can be started as two independent nodes and make a P2P connection between them.**

The program must:

- be a single downloadable Python file;
- require Python 3.x only;
- require no external packages;
- support one node in listen mode;
- support a second node in connect mode;
- exchange a message and response;
- be executable on the same LAN when the listener address is reachable.

## 3. GAP and RED

Existing `src/p2p/node.py` proved the communication primitive, but it was package-oriented and required the repository source layout. The smallest coherent GAP was therefore a standalone root-level executable script.

RED test:

`sessions/SES-044/test_downloadable_two_nodes.py`

Commit: `4a62e3b733bd8ededbf87d6c04019e12ba013c34`

The test starts two independent processes using `p2p_node.py`, with A connecting to B and receiving `pong-from-B`.

## 4. Implementation

Added:

`p2p_node.py`

Commit: `dc725a6040abe9cd43cc69cc3f431150c44762dd`

The program uses only Python standard-library TCP sockets.

Documentation:

`P2P_NODE.md`

Commit: `17f7f04a40713b19e0e84bedb159c2ef7057f4cc`

## 5. Final automated proof

The SES-044 standalone test was integrated into the existing P2P CI workflow to ensure the exact test executes on `main`.

Verification commit:

`0dccb7baff6b23f04347435c4ed8a001709a4999`

GitHub Actions:

- run `34935150469` = **SUCCESS**;
- job `standalone-two-node-proof` = **SUCCESS**;
- step `Run SES-044 standalone two-node proof` = **SUCCESS**;
- existing `two-node-proof` also remained **SUCCESS**.

This is the required positive CI evidence for the SES-044 artifact.

## 6. Result

SES-044 is **GREEN / CLOSED**.

The repository now contains a minimal downloadable program that can be copied as one Python file and run as two independent nodes:

```text
Node B: python p2p_node.py --listen 0.0.0.0:9000 --node-id B
Node A: python p2p_node.py --connect <IP_B>:9000 --node-id A --message ping-from-A
```

Expected response:

```text
pong-from-B
```

## 7. Stone

**SES-044 stone:** the verified repository state represented by CI run `34935150469` and commit `0dccb7baff6b23f04347435c4ed8a001709a4999` proves the standalone two-node P2P requirement.

No broader P2P capability is implied by this stone.

## 8. Hard boundaries

Not introduced:

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

## 9. Scope limitation

SES-044 proves a **downloadable minimal two-node communication program**, not a production P2P network.

It does not prove:

- discovery,
- NAT traversal,
- authentication,
- encryption,
- persistence,
- Internet production readiness,
- final transport architecture.
