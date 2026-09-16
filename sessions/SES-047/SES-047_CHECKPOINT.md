# SES-047 — Checkpoint

**Data:** 2026-09-16  
**Status:** AWAITING CI  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## Evidence collected

The existing `P2PNode` already provides the minimal lifecycle primitives needed for this stage:

- `listen_once()` accepts one connection and closes it after the exchange;
- the same node can call `listen_once()` again for a subsequent connection;
- malformed `HELLO` is rejected by the existing protocol parser;
- after a malformed handshake, the node can accept a valid subsequent connection.

No production-code change was required by the SES-047 audit.

## Test added

`sessions/SES-047/test_lifecycle_protocol.py`

The test proves:

1. successful connection/message exchange;
2. disconnect after exchange;
3. reconnect to the same listening node;
4. malformed handshake rejection;
5. successful valid connection after malformed input.

## CI integration

Workflow `.github/workflows/ses-045-p2p.yml` now runs the SES-047 lifecycle proof as job `ses-047-lifecycle`.

Relevant commits:

- `70fabafd3c1b73f2404eaf03ca1daddcffb9f4a9` — lifecycle test;
- `c35ab0223beb8bcd9c1cfdca860fbb62d622db50` — CI integration.

## Closure rule

SES-047 is **not closed yet**. No PASS is declared until the new CI run proves the lifecycle test GREEN together with the existing P2P regression jobs.

If CI is GREEN, close SES-047 with the CI run ID as evidence. If CI is RED, inspect the actual failure before changing production code.
