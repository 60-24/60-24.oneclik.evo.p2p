# SES-090 — CI RESULTS (GitHub Actions)

Tested commit: `5829486dfeb7eca3d12c72b5e03766f746f9910e` — head of branch `ses-090/message-integrity` and of draft PR #20,
base `main` = `9410b7457d0266bae9e7b95a5da0b669cde5710e` (unchanged at the time of the check).
Collected: 2026-11-21, read from the GitHub REST API and the job logs. No source change was made after the
local GREEN run (`17cf123` is the last commit that touches code or tests).

## Result

All 9 workflow runs and all 13 check runs on this commit completed with `success`; the commit status
`p2p/evidence` is `success`. Nothing failed, so no code or workflow change was needed.

## Workflow runs

| Workflow | Event | Result | Run |
|---|---|---|---|
| P2P Linux executable | pull_request | success | [44866639457](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639457) |
| P2P Windows executable | pull_request | success | [44866639283](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639283) |
| P2P Android APK | pull_request | success | [44866639420](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639420) |
| P2P trusted introductions | pull_request | success | [44866639268](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639268) |
| SES-043 P2P proof | pull_request | success | [44866639250](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639250) |
| SES-045 concrete P2P node | pull_request | success | [44866639321](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639321) |
| SES-032 E2E integration | pull_request | success | [44866639318](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639318) |
| Beta local execution | pull_request | success | [44866639241](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866639241) |
| P2P Runtime Demo | push | success | [44866621350](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/44866621350) |

Check runs (13): `build-linux-p2p`, `build-windows-p2p`, `build-android-p2p`, `build-windows-demo`,
`trusted-introductions`, `concrete-node-api`, `ses-046-handshake`, `ses-047-lifecycle`,
`ses-049-linux-message-delivery`, `two-node-proof`, `e2e`, `test-local-executor`, `demo` — all `success`.

## What the Linux and Windows jobs actually executed (from the job logs)

- Step `Run P2P regression tests`: success on both. It runs every node-related test file; each file passed.
- `python -m pytest -q tests/test_message_integrity.py` (the new test, registered by this PR):
  **42 passed in 1.41 s on Linux, 42 passed in 0.36 s on Windows.**
- Step `Smoke test packaged two-node executable`: success on both. The PyInstaller-built executables ran a
  listener and a client over the V2 protocol, and the step asserts the response `pong-from-B` and the log line
  `node B received from A` (Linux also asserts this over the LAN address).
- Android: the APK build succeeded. No on-device or instrumented test ran.

## Not run for this PR, and why (workflow triggers, read from the workflow files)

| Workflow | Trigger | Why it did not run |
|---|---|---|
| SES-011, SES-023, SES-024, SES-025 | push to `main` | branch filter; they run after a merge. They cover System Builder paths this PR does not touch |
| SES-007, SES-008, VS-001, G-01 GS-01/GS-02, Build System Builder Demo | push with path filters | no matching paths changed |
| P2P Release | tag `v*` | tag only |
| P2P Evidence Check | after `P2P Linux executable` completes | reported as the commit status `p2p/evidence: success` |

`main` has no branch protection and no rulesets, so GitHub defines no "required" checks. The judgment of
relevance above is mine: every workflow that exercises the node runtime ran and passed.

## Per-commit note

The three commits were pushed together to a new branch, so GitHub created runs only for the head commit
`5829486`. `6a61527` (intentional RED tests) and `17cf123` (implementation) have no runs of their own. Their
combined effect is what `5829486` tested.

## Boundary

This establishes CI success for `5829486` only. Documentation-only commits added after it (including the one
that adds this file) change no source or test, but their own CI runs are separate. It does not establish
behavior on physical networks, on an Android device, or in production.
