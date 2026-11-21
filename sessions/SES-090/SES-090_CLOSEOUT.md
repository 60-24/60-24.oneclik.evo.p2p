# SES-090 — CLOSEOUT

Status: IMPLEMENTED — GREEN locally and GREEN in GitHub Actions on commit `5829486` (9 of 9 workflow runs and
13 of 13 check runs succeeded, including Linux, Windows and the Android build; see `CI_RESULTS.md`). Draft PR
#20, **not merged**. STONE placement is left to the human decision.

## INSPECT

Base `main` = `9410b7457d0266bae9e7b95a5da0b669cde5710e`. Read `AGENTS.md`, `docs/CURRENT_STATE.md`,
`P2P_NODE.md`, `src/p2p/{protocol,node,trust,transport}.py`, the session tests that hand-craft frames, and the
workflows that run node tests. Baseline on that commit: 41 tests in 21 files passed.

## UNDERSTAND / GAP

The handshake authenticated identities; the application message was unauthenticated plain text. Confirmed
by a local relay that replaced the message after AUTH: the listener recorded the replacement as coming from
the authenticated peer. Specification and decisions: `SES-090_SPEC_AND_DECISIONS.md`.

## RED

Commit `6a61527` adds `tests/test_message_integrity.py` with `src/` unchanged: **36 failed, 6 passed**
(`RED_RESULTS.txt`). The 6 passing tests are regression guards for behavior that already held (valid and
empty message, 32-byte fresh handshake challenges). The relay test failed for the right reason: the
listener accepted the modified text and acknowledged it.

## IMPLEMENT

Commit `17cf123`: handshake context V2, `session_id`, signed payload, strict `MSG` parser,
`MessageReceiver` (strict sequence), signing in `send`, verification in `listen_once`, data-after-message
check. SES-069 updated to the new frame, keeping its coalesced-segment purpose. The handshake message
formats, `trust.py` and `transport.py` are unchanged; trust semantics are unchanged.

## GREEN (evidence)

- `tests/test_message_integrity.py`: **42 passed**; every node-related CI test file passes, including
  SES-069 after its update (`GREEN_RESULTS.txt`).
- Mutation check on a copy of the code: removing the session binding, the recipient, the length prefix, the
  server challenge, the sequence check, the canonical-base64 check, the data-after-message check, or
  reverting to V1 each makes tests fail, 8 of 8 (`MUTATION_CHECK.txt`).
- End to end: the audit relay attack no longer succeeds (client gets no acknowledgement, the listener sets no
  message); two real CLI processes exchange `hello-from-A` with exit codes 0 and 0 (`E2E_RESULTS.txt`).

## CI (evidence)

GitHub Actions on `5829486`: all 9 workflow runs and 13 check runs `success`, commit status `p2p/evidence`
`success`. The new test passed 42/42 on both Linux and Windows runners, and the packaged executables passed
the two-node smoke test. No failure occurred, so no code change followed. Details, run links and the
workflows that did not run (path, branch or tag filters) are in `CI_RESULTS.md`.

## BOUNDARY

Evidence covers a local Linux run and the CI run of commit `5829486`. It does not establish: CI status of
later documentation-only commits, behavior on physical networks or an Android device, confidentiality
(messages are signed, not encrypted), or authenticity of the response (`FOLLOWUP_SIGNED_RESPONSE.md`). Nodes before and after this change cannot
interoperate; deploy all nodes together. Residual risks: see section 4 of the specification.

## Open for the human

Review the draft PR, decide the follow-up on the response, and decide on merging. Nothing was
merged and no repository setting was changed.
