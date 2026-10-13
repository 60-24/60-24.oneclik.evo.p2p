# SES-084 — CLOSEOUT

Status: STONE — PR #11 squash-merged into main. Merge commit: `825b55a5fe7d5e887c4e3971aed8bb028796322c`.

## INSPECT
Reviewed `src/p2p/node.py`, the existing SES-069 TCP integration test, and Linux/Windows CI workflow commands on `main` at `336684c06c90284d053b10f6d4cf60aa2770ad20`.

## GAP
The SES-069 integration test sends AUTH and the application frame in one `sendall`, but TCP does not guarantee that the receiver gets both frames in one `recv`. Therefore it does not deterministically prove that `_receive_line` preserves the second frame in its internal buffer after a single receive.

## CHANGE
Added `sessions/SES-084/test_deterministic_coalesced_frames.py`. Its socket stub returns both newline-delimited frames in exactly one `recv`; the test asserts both lines are read and no second receive occurs. Registered the test in Linux and Windows P2P regression workflows.

No runtime code or protocol behavior was changed.

## EVIDENCE
Tested PR head: `54b613a2edf9e9263f37f239eb5463ead5380558`. Linux and Windows regression workflows and the other listed workflows passed on this exact PR head.
- Linux P2P executable workflow 38373172670: SUCCESS; regression test step passed.
- Windows P2P executable workflow 38373172815: SUCCESS; regression test step passed.
- Android APK workflow 38373172333: SUCCESS.
- E2E integration workflow 38373172510: SUCCESS.
- Two-node proof workflow 38373172341: SUCCESS.
- Concrete-node workflow 38373172819: SUCCESS.
- Beta local execution workflow 38373172537: SUCCESS.

## BOUNDARY
This improves deterministic regression coverage only. It does not claim a protocol defect, production readiness, or end-to-end encryption. PR #11 was merged after all listed workflows passed on head `54b613a2edf9e9263f37f239eb5463ead5380558`. The merge integrates tests and CI wiring only; no runtime code changed.
