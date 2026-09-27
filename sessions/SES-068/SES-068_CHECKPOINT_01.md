# SES-068 — Checkpoint 01

**Status:** IMPLEMENTED / GREEN verification pending
**Date:** 2026-09-27

## Real GAP

`_receive_line()` previously treated TCP EOF as a valid end of frame even when no `\n` delimiter had been received.

That made an incomplete/truncated frame observable as a complete message.

## RED evidence

Test: `sessions/SES-068/test_incomplete_frame_eof.py`

The test requires EOF before the delimiter to raise `ValueError("incomplete frame")`.

The pre-fix implementation instead broke on EOF and returned the partial buffer, so the required contract was absent.

## Implementation

`src/p2p/node.py`

Minimal change:

- EOF before `\n` now raises `ValueError("incomplete frame")`;
- normal newline-terminated frames remain unchanged;
- existing maximum-frame-size protection remains unchanged.

Implementation commit:
`434121e525df836942659e971e922ee9eae53da2`

CI registration commit:
`5ca6b861f600366b9bf97932a555254a45dd322c`

## Verification boundary

The repository workflow contains the new SES-068 test.

Independent local execution was attempted, but the current execution environment has no DNS/network access to clone the repository. Therefore this checkpoint does **not** claim GREEN until GitHub Actions provides a successful run containing the new test.

## Rule

No STONE / CLOSED claim is made before CI GREEN evidence exists.
