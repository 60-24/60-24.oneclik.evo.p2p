# SES-084 — CLOSEOUT

Status: GREEN pending CI evidence; no protocol implementation changed.

## INSPECT
Reviewed `src/p2p/node.py`, the existing SES-069 TCP integration test, and Linux/Windows CI workflow commands on `main` at `336684c06c90284d053b10f6d4cf60aa2770ad20`.

## GAP
The SES-069 integration test sends AUTH and the application frame in one `sendall`, but TCP does not guarantee that the receiver gets both frames in one `recv`. Therefore it does not deterministically prove that `_receive_line` preserves the second frame in its internal buffer after a single receive.

## CHANGE
Added `sessions/SES-084/test_deterministic_coalesced_frames.py`. Its socket stub returns both newline-delimited frames in exactly one `recv`; the test asserts both lines are read and no second receive occurs. Registered the test in Linux and Windows P2P regression workflows.

No runtime code or protocol behavior was changed.

## EVIDENCE
Pending Linux/Windows CI on this branch. Do not mark STONE until both workflows execute the new test successfully.

## BOUNDARY
This improves deterministic regression coverage only. It does not claim a protocol defect, production readiness, or end-to-end encryption.
