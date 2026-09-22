# SES-061 — CHECKPOINT 01

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Status:** GREEN / CLOSED / STONE  
**Date:** 2026-09-22

## INSPECT

SES-060 is GREEN/CLOSED/STONE.

Current runtime remains:

`download → run Node B → connect Node A → handshake → identity → message → response`

The current listener accepts a TCP connection and reads the handshake with `_receive_line()`.

## IDENTIFIED GAP

**GAP-061-01 — incomplete peer handshake could leave the listener blocked indefinitely.**

The connector side already has a bounded connection timeout. The accepted listener socket did not explicitly receive a read timeout.

A peer could connect and send incomplete handshake data without a newline. The listener would remain blocked in `recv()` instead of terminating the peer attempt with a bounded error.

This was a real runtime-boundary gap, not a planned feature.

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

- `LISTEN_TIMEOUT_SECONDS = 2`;
- `conn.settimeout(LISTEN_TIMEOUT_SECONDS)` on accepted connections.

No protocol format, architecture, transport, or public CLI contract was changed.

The existing `OSError` boundary converts the timeout into:

`ERROR: Listening failed: timed out.`

**Fix commit:** `d50b8a71824430de124a80ed131bb2b487c910d9`

## TEST REGRESSION

**Test commit:** `ab7fc471e89087459dfd934afb70c88acc963441`

The test is included in `.github/workflows/build-p2p-linux.yml` under `Run P2P regression tests`, together with the existing SES-046, SES-047, SES-049, SES-055, SES-058, and SES-059 regressions. The same workflow also builds the packaged executable and runs the existing Node A ↔ Node B and non-loopback smoke flows.

## GREEN EVIDENCE

The required CI evidence is present on the current repository state:

- **Workflow:** `P2P Linux executable` (`.github/workflows/build-p2p-linux.yml`)
- **Workflow run:** [35688822581](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/35688822581)
- **Run conclusion:** `success`
- **Run commit SHA:** `b985091299d6e0a82ac0e53d944b2fcd8cc9aa2e`
- **Run commit:** `feat(demo): add independent GitHub P2P runtime demo`
- **Fix ancestry:** the run commit is later than and contains `d50b8a71824430de124a80ed131bb2b487c910d9`, `ab7fc471e89087459dfd934afb70c88acc963441`, and `afeb01246595fc8256ef6cac565d4a2baa2076fe`.

At that SHA, the workflow explicitly executes:

`python -m pytest -q sessions/SES-061/test_incomplete_handshake_timeout.py`

and the workflow completed successfully. The same successful workflow also includes the packaged executable Node A ↔ Node B smoke test. Therefore the reproducible evidence is:

`incomplete handshake → bounded timeout → listener remains healthy → CI GREEN`

The earlier successful runs on `ab7fc471...` and `afeb012...` are not used as the closeout evidence. The closeout evidence is the later successful run on `b985091299d6e0a82ac0e53d944b2fcd8cc9aa2e`.

## CLOSE CRITERION

SES-061 is closed only because the current repository state has a successful CI run that executes the named incomplete-handshake regression after the timeout implementation and completes the required P2P packaged-flow verification.

**Final status: GREEN / CLOSED / STONE.**

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
