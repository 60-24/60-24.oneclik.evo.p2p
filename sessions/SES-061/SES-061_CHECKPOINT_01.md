# SES-061 — CHECKPOINT 01

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Status:** IMPLEMENTED — CI VERIFICATION PENDING  
**Date:** 2026-09-21

## INSPECT

SES-060 is GREEN/CLOSED/STONE.

Current runtime remains:

`download → run Node B → connect Node A → handshake → identity → message → response`

The current listener accepts a TCP connection and reads the handshake with `_receive_line()`.

## IDENTIFIED GAP

**GAP-061-01 — incomplete peer handshake could leave the listener blocked indefinitely.**

The connector side already has a bounded connection timeout. The accepted listener socket did not explicitly receive a read timeout.

A peer could connect and send incomplete handshake data without a newline. The listener would remain blocked in `recv()` instead of terminating the peer attempt with a bounded error.

This is a real runtime-boundary gap, not a planned feature.

## RED TEST

Added:

`sessions/SES-061/test_incomplete_handshake_timeout.py`

The regression test:
1. starts the real CLI listener;
2. connects a TCP peer;
3. sends incomplete `HELLO` data without the terminating newline;
4. keeps the connection open;
5. requires the listener process to terminate with an actionable timeout error;
6. rejects a Python traceback.

The test was added before the implementation.

## IMPLEMENTATION

Minimal change in `src/p2p/node.py`:

- added `LISTEN_TIMEOUT_SECONDS = 2`;
- explicitly applies `conn.settimeout(LISTEN_TIMEOUT_SECONDS)` to accepted connections.

No protocol format, architecture, transport, or public CLI contract was changed.

The existing `OSError` boundary converts the timeout into:

`ERROR: Listening failed: timed out.`

## CI

The regression test was added to:

`.github/workflows/build-p2p-linux.yml`

CI must prove the complete regression suite and packaged executable path before SES-061 can be closed.

## Boundary

SES-061 does **not** introduce:
- encryption;
- authentication;
- discovery;
- NAT traversal;
- GUI;
- central infrastructure;
- System Builder integration;
- protocol redesign.

## Next action

`VERIFY → GREEN`

Do not close SES-061 until the repository/CI provides execution evidence for the new regression and the existing packaged P2P proof remains GREEN.
