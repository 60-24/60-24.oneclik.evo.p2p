# SES-090 — Message Integrity: analysis, specification and decisions

Zone (AGENTS.md): YELLOW — protocol change. No Constitution, ontology or trust-model change.

## 1. Base and gap

Base commit: `main` = `9410b7457d0266bae9e7b95a5da0b669cde5710e` (2026-10-29).

Audit finding, re-confirmed on that commit: the HELLO/WELCOME/AUTH handshake authenticates both
identities, but the application line after AUTH was plain text. An active relay that forwards the
handshake unchanged could replace the message; the listener then recorded the replacement as a message
from the authenticated peer (`last_message` set, `last_peer_id` equal to the real client). Reproduced with
a local relay script before any change.

## 2. Specification (as implemented)

Application line after AUTH (and the optional `VOUCH` line):

```
MSG <seq> <signature_b64> <text>
```

Signed bytes (all fixed-width except the last field, which is length-prefixed, so the encoding is
unambiguous):

| Field | Bytes |
|---|---|
| context `P2P60-24-MSG-V1` | 15 |
| `session_id` | 32 |
| sender NodeID (raw) | 32 |
| recipient NodeID (raw) | 32 |
| `seq`, big-endian | 8 |
| length of text in UTF-8 bytes, big-endian | 4 |
| text, UTF-8 | n |

```
session_id = SHA-256("P2P60-24-SESSION-V1" || client_id || server_id
                     || client_challenge || server_challenge)
```

Both sides already hold every input after the handshake, so the handshake messages are unchanged.
Only the handshake context constant changed: `P2P60-24-IDENTITY-V1` → `P2P60-24-IDENTITY-V2`.

Replay model:

- Across sessions: each side contributes a fresh 32-byte challenge to `session_id`; a frame captured in one
  session does not verify in another.
- Within a session: the receiver accepts only `seq == expected_seq`, starting at 1, and advances after a
  verified message. Duplicate, lower and skipped numbers are rejected. Today one connection carries one
  message, so `seq` is always 1; the counter is kept so the session model stays correct if that changes.

Rejections (all before `last_message` is set, with no response sent): wrong frame structure, non-canonical
sequence or base64, signature not exactly 64 bytes, bad signature, unexpected sequence, data after the
message in the same buffer.

## 3. Decisions (human, 2026-11-18 and 2026-11-21)

1. Compatibility: `PROTOCOL_CONTEXT` V2. A V2 client never sends a message to a V1 server believing it
   protected; both mismatched directions fail during the handshake.
2. One message per connection; `seq` starts at 1; the public API is not extended.
3. Signing the response (`pong-from-B`) is out of scope and recorded as a separate task
   (`FOLLOWUP_SIGNED_RESPONSE.md`). The response is not presented as authenticated.
4. SES-069 is updated to the new frame format and keeps its purpose (coalesced AUTH + message); the reason
   is recorded in the test file.
5. This directory holds the session record; the new test is registered in the Linux and Windows build workflows.
6. Work on `ses-090/message-integrity`, draft PR, no merge to `main`.

## 3a. Pre-implementation clarifications requested by the human

1. *Are both challenges generated with a cryptographically secure generator and long enough?* Yes. Both are
   `secrets.token_bytes(32)` (client in `send`, server in `listen_once`). The HELLO/WELCOME builders and
   parsers reject any challenge that is not exactly 32 bytes. Tests (these already passed on `main` and are
   kept as regression guards): `test_handshake_challenges_are_32_bytes_and_fresh_per_connection`,
   `test_handshake_rejects_challenge_of_wrong_length` (0, 31, 33 bytes).
2. *Does the signature cover every field and the text length unambiguously?* Yes, see the table above.
   Tests: `test_message_payload_layout_matches_independent_reference` compares against a payload builder
   written separately inside the test (multi-byte text, so byte length differs from character count), and
   `MUTATION_CHECK.txt` shows that removing the session, the recipient or the length prefix is detected.
3. *Does the parser reject non-canonical encoding, wrong lengths and extra data?* Yes: 22 parametrized
   rejection cases in `test_invalid_frame_is_rejected_and_not_delivered`, 7 cryptographic (bad signature,
   other signer, other recipient, other session, sequence 2) and 15 structural (leading zero, `+`, Unicode digit, zero, empty and
   >2^63-1 sequence; 63- and 65-byte signatures; non-base64; base64 with non-zero padding bits, which
   Python's `validate=True` decoder accepts, so the parser re-encodes and compares), plus
   `test_second_frame_coalesced_after_the_message_is_rejected` for data after the message.
4. *Do the tests show rejection of modified, replayed and cross-session messages?* Yes:
   `test_message_modified_by_relay_is_rejected` (relay edits the text inside a valid frame),
   `test_frame_captured_in_one_session_is_rejected_in_another`, the sequence tests
   (`validly_signed_but_sequence_two`, receiver unit test for repeat and skip), and
   `test_changing_the_session_context_invalidates_the_signature`.

## 4. Residual risks and limits

- The response is unauthenticated: a relay can answer `pong-from-B` itself without the real server having
  received anything, and the client cannot tell (derived from the code; not exercised by a test in this
  session). Tracked in `FOLLOWUP_SIGNED_RESPONSE.md`.
- Messages are signed, not encrypted: no confidentiality (E2E explicitly out of scope).
- The client does not pin the server identity it expects (pre-existing). Integrity holds toward whichever
  authenticated peer the client connected to, not necessarily the intended one.
- The `VOUCH` line and the HELLO `label` are not covered by the message signature. Removing a voucher can only
  deny access; trust semantics (`is_authorized`) are unchanged.
- The handshake parsers (HELLO/WELCOME/AUTH) still decode base64 leniently, unchanged by design ("do not
  change the handshake without need"). The new `MSG` parser is strict.
- Compatibility: nodes built before and after this change cannot talk to each other. Release binaries from
  earlier `v*` tags are incompatible; the Android APK and desktop builds must be rebuilt together.
- CI: GitHub Actions passed on commit `5829486` (Linux, Windows, Android build, packaged smoke tests; see
  `CI_RESULTS.md`). Still not verified: physical networks, an Android device, and the workflows that only run
  on push to `main` or on tags.

## 5. Files

Changed: `src/p2p/protocol.py`, `src/p2p/node.py`, `sessions/SES-069/test_coalesced_frames.py`,
`.github/workflows/build-p2p-linux.yml`, `.github/workflows/build-p2p-windows.yml`, `README.md`,
`START_HERE.md`, `P2P_NODE.md`, `docs/CURRENT_STATE.md`.
Added: `tests/test_message_integrity.py` and this directory.
Not changed: handshake message formats, `src/p2p/trust.py`, `src/p2p/transport.py`, `demo/`, `android/`.
