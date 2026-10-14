# SES-085 — CLOSEOUT

Status: STONE — deterministic regression test added to `main`; Linux and Windows CI passed on tested commit `97d4d9efe7bff9b2cfd5c1e5e5ec975045295530`. Runtime unchanged.

## INSPECT

Inspected `src/p2p/node.py`, SES-068 EOF coverage, SES-069 coalesced-frame integration coverage, SES-084 deterministic coalescing test, and Linux/Windows P2P workflows.

Current `main` before this session's test commit was `0bdbc58fd70de7524822553f25fdd8ad8d031cb0`; resulting test commit is `97d4d9efe7bff9b2cfd5c1e5e5ec975045295530`.

## UNDERSTAND / GAP

SES-068 covered EOF before a complete HELLO frame. SES-069 and SES-084 covered coalesced frames, not EOF after a valid AUTH but before a complete application frame. This was a test-coverage gap, not a demonstrated runtime defect.

In `listen_once()`, `last_peer_id` is assigned only after AUTH signature verification; `last_message` is assigned only after `_receive_line()` returns a complete newline-delimited frame. `_receive_line()` raises `ValueError("incomplete frame")` on EOF before the delimiter.

## CHANGE

Added `sessions/SES-085/test_eof_after_auth.py`. The test performs the HELLO/WELCOME signature verification, signs and sends AUTH, then closes the socket without an application frame. It asserts listener termination, the incomplete-frame error, authenticated peer identity, and `server.last_message is None`.

Registered the test in both `.github/workflows/build-p2p-linux.yml` and `.github/workflows/build-p2p-windows.yml`.

No runtime code or protocol behavior changed. A runtime RED/GREEN cycle was not applicable: the pre-existing implementation already rejects this incomplete frame; the change closes the missing-test gap.

## EVIDENCE

Tested commit: `97d4d9efe7bff9b2cfd5c1e5e5ec975045295530`.

- [P2P Linux executable — run 38599711556](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/38599711556): SUCCESS; regression test step, build, packaged two-node smoke test, and artifact upload passed.
- [P2P Windows executable — run 38599711475](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/38599711475): SUCCESS; regression test step, build, packaged two-node smoke test, and artifact upload passed.
- [P2P Android APK — run 38599711390](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/38599711390): SUCCESS.
- [SES-032 E2E integration — run 38599711522](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/38599711522): SUCCESS.
- [SES-043 P2P proof — run 38599712183](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/38599712183): SUCCESS.
- [SES-045 concrete P2P node — run 38599711612](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/38599711612): SUCCESS.
- [P2P Evidence Check — run 38599873452](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/38599873452): SUCCESS.

## BOUNDARY

Evidence confirms this test and listed workflows on the tested commit; it does not establish production readiness, end-to-end encryption, automatic discovery, or NAT traversal.
