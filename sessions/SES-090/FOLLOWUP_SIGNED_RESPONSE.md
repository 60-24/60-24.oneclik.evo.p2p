# Follow-up (separate task, outside SES-090): authenticate the response

Status: OPEN, not started. Decision needed from the human before any work (protocol change, YELLOW).

## Problem

After SES-090 the message A → B is signed and session-bound. The response B → A is the constant line
`pong-from-B` and is **not** authenticated. `send()` returns whatever line the peer sends. A relay that
forwards the handshake can therefore reply `pong-from-B` itself, without the real listener having received
the message, and the client reports success. (Derived from the code; to be demonstrated by a test as the
first step of this task.)

The README, `P2P_NODE.md` and `docs/CURRENT_STATE.md` state that the response is not authenticated. They
must not be changed to claim otherwise until this task is done.

## Proposed direction (for review, not decided)

- Listener answers with a signed `ACK <seq> <signature_b64>` instead of the bare constant. The signature
  covers a distinct context (for example `P2P60-24-ACK-V1`), `session_id`, sender and recipient (reversed
  roles), `seq`, and a SHA-256 of the received message payload.
- Client verifies it against the server's authenticated public key and rejects anything else, including the
  old constant.
- Compatibility: another wire change. Either bump the handshake context again or document that mixed
  versions are rejected through the message format.

## Tests to write first (RED)

1. A relay that drops the message and answers `pong-from-B` is detected by the client.
2. An ACK for a different message, session or sequence is rejected.
3. An ACK signed by another identity is rejected.
4. A valid ACK is accepted.

## Where to track

Open a GitHub issue with this text once the session has write access to the repository (this session had
read-only access, so no issue could be created).
