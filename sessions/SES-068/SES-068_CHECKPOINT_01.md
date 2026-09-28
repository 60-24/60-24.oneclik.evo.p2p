# SES-068 — Checkpoint 01

**Status:** GREEN / verification complete
**Date:** 2026-09-28

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

## Regression discovered and corrected

The new EOF contract exposed a test-contract issue in SES-067: after the listener rejects an oversized frame and closes the socket, the client may observe either a protocol-level `ValueError` or a transport-level `OSError`.

The production framing rule was kept unchanged. SES-067 was corrected to assert the server-side contract:

- listener raises `ValueError("frame exceeds maximum size")`;
- `server.last_message` remains unset.

Regression-test correction commit:
`053fdcdf1abeb91f1cf448b08d85894df024e5eb`

## GREEN evidence

Authoritative GitHub Actions workflow:

- Workflow: **P2P Linux executable**
- Run: `36385776327`
- Commit: `bd3bdf42dbe712026e1dff5db29ba535df1d5271`
- Result: **completed / success**
- Regression test step: **success**
- Linux executable build: **success**
- Two-node packaged smoke test: **success**
- Linux artifact upload: **success**
- Artifact attestation: **success**

The successful regression-test step includes SES-068 after the corrected SES-067 test, so the workflow no longer stops before reaching SES-068.

## Evidence layer

A separate workflow now records machine-readable verification:

- `.github/workflows/p2p-evidence.yml`
- evidence schema: `P2P60-24-EVIDENCE/v1`
- commit status: `p2p/evidence`
- current status for the verified commit: **success / P2P verification GREEN**
- evidence artifact: `P2P60-24-EVIDENCE-36385776327`

The evidence workflow is triggered automatically after **P2P Linux executable** completes.

## Verification boundary

Local execution is not required for this checkpoint because the authoritative execution environment is GitHub Actions and the repository now exposes both a machine-readable Evidence artifact and a commit status tied to the exact verified SHA.

## Rule

GREEN evidence is now present. STONE / CLOSED may be declared only after the session-level closeout records this evidence and confirms there is no remaining SES-068 scope gap.
