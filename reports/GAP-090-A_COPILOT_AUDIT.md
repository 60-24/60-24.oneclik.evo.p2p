# GAP-090-A — Independent Audit Report

**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Audit date:** 2026-11-21  
**Status:** read-only audit of `main` and draft PR #20; no project implementation, tests, `main`, or PR #20 changed by this audit.

## Executive summary

SES-090’s central inbound-message protection is supported by a coherent implementation and a substantial new test suite: the receiver validates a canonical `MSG` frame and Ed25519 signature bound to session, sender, recipient and sequence before setting `last_message`. The documentation inspected in PR #20 clearly identifies the major security limits: messages are signed but not encrypted, the `pong-from-B` response is unauthenticated, server identity is not pinned, and V1/V2 interoperability breaks.

This audit does **not** mark SES-090 CI as passing. The draft’s evidence records local Linux runs, while the PR body says Actions have not run for its branch. Available Actions/check-run metadata could not be tied conclusively to the PR head and did not expose reliable per-job conclusions in this audit session. Windows test-step failure propagation is a concrete workflow concern: the PowerShell step chains multiple native `pytest` commands without explicit per-command exit checks, so a failed earlier invocation may be followed by a later command that succeeds and determines the script’s final exit code.

The CLI evidence is mixed in strength. `sessions/SES-043/test_p2p_two_nodes.py` launches two OS processes but checks only the client’s response and does not assert server-side receipt. By contrast, the Linux and Windows packaged smoke-test steps start a listener executable and a separate client executable and check server logs for the received message; those workflows are relevant evidence of real process-to-process communication when they run successfully. The checked-in `sessions/SES-090/E2E_RESULTS.txt` records a local two-process run, but this audit did not independently execute that script.

## Commit and review scope

- **Verified `main` base/HEAD:** `9410b7457d0266bae9e7b95a5da0b669cde5710e`.
- **Draft PR #20 reviewed:** head `5829486dfeb7eca3d12c72b5e03766f746f9910e`, base `main` at the SHA above; PR is open and marked draft in the retrieved PR metadata.
- **Source inspected on PR head:** `src/p2p/protocol.py`, `src/p2p/node.py`, `tests/test_message_integrity.py`, `sessions/SES-069/test_coalesced_frames.py`, `sessions/SES-083/test_inbound_message_line_validation.py`, `sessions/SES-067/test_frame_size_limit.py`, `sessions/SES-043/test_p2p_two_nodes.py`, `sessions/SES-045/test_p2p_node_api.py`, `demo/p2p_node_cli.py`.
- **Workflow inspected on PR head:** `.github/workflows/build-p2p-linux.yml`, `.github/workflows/build-p2p-windows.yml`, `.github/workflows/build-p2p-android.yml`, `.github/workflows/p2p-trusted-introductions.yml`.
- **Documentation inspected on PR head:** `README.md`, `P2P_NODE.md`, `docs/CURRENT_STATE.md`; also PR evidence/spec files under `sessions/SES-090/`.
- **Review method:** static inspection of source, tests, workflow YAML, documentation, PR metadata, and available Actions metadata/log excerpt. No dependencies installed; no tests or workflow reruns were performed as part of this audit.

## Confirmed findings

### C1 — Main is still pre-SES-090; PR docs label the draft status

The retrieved `main` ref resolves to `9410b7457d0266bae9e7b95a5da0b669cde5710e`. PR #20 is a separate draft branch at `5829486dfeb7eca3d12c72b5e03766f746f9910e`. `docs/CURRENT_STATE.md` in the PR explicitly says SES-090 is implemented on `ses-090/message-integrity` as draft work and reaches main only after a human merge. Its top snapshot still says the latest closed technical session is SES-085, which is not inconsistent with SES-090 remaining draft.

**Evidence:** PR #20 metadata; `docs/CURRENT_STATE.md` lines 3–6, 113–115 on the PR head.

### C2 — Inbound message signature binds the stated fields; replay and malformed-frame tests exist

`src/p2p/protocol.py` constructs session material from both node IDs and both 32-byte challenges (`session_id`, lines 137–151), builds a signed payload containing message context, session, sender, recipient, sequence and UTF-8 byte length (`message_payload`, lines 154–173), and checks canonical base64, signature size and sequence syntax in `parse_msg` (lines 184–201). `MessageReceiver.accept` verifies the Ed25519 signature and expected sequence (lines 223–238). `src/p2p/node.py` creates that receiver after AUTH, checks the frame, and sets `last_message` only after successful acceptance (lines 171–200).

`tests/test_message_integrity.py` includes independent reference builders (lines 62–82), relay tampering (281–297), invalid frame/signature cases (329–394), cross-session replay (400–417), V1/V2 handshake cases (437–505), and payload/session binding checks (551–618). This is evidence of test design and source behavior, **not an independent test execution by this audit**.

### C3 — SES-069 remains a coalesced-frame test, updated for the wire format

`sessions/SES-069/test_coalesced_frames.py` now places AUTH and a correctly signed `MSG` in the same `sendall` (lines 62–83) and asserts the listener handles both and records the message (lines 85–90). Its previous plain-text payload was replaced; the test’s coalescing purpose remains represented. The new test suite also has a distinct same-buffer post-message-data rejection test (`tests/test_message_integrity.py`, lines 420–431).

### C4 — Documentation does not claim confidentiality or authenticated replies

- `README.md` says the application message is signed and session-bound, explicitly says `pong-from-B` is not authenticated, and lists lack of end-to-end encryption and authenticated responses (lines 30–34, 121–135).
- `P2P_NODE.md` identifies the message as a signed `MSG`, says mixed V1/V2 peers fail and must be rebuilt together, and marks the response unauthenticated (lines 41–55).
- `docs/CURRENT_STATE.md` lists end-to-end encryption and authenticated responses as absent, and links to the response follow-up (lines 68–82); its SES-090 entry explicitly limits implementation status to the draft branch (lines 104–115).
- The draft’s `sessions/SES-090/SES-090_SPEC_AND_DECISIONS.md` additionally records lack of server identity pinning, handshake base64 parsing behavior, and compatibility limits (section 4).

Accordingly, the inspected documentation’s security boundary is materially explicit. The phrase “authenticated peer” should be read as the peer key authenticated by this handshake, not a separately pinned intended server; that pre-existing limit is called out in the PR description and SES-090 spec.

### C5 — Windows test step lacks explicit fail-fast handling for each pytest process

`.github/workflows/build-p2p-windows.yml` lines 27–47 runs a sequence of native `python -m pytest` commands in one PowerShell step. It has no explicit `$LASTEXITCODE` check after each invocation or loop wrapper that stops on a nonzero native process exit. PowerShell’s ordinary `$ErrorActionPreference` does not itself guarantee that a nonzero native executable exit aborts the script. Thus a failure in an earlier pytest invocation can be followed by later invocations; if a later command exits successfully, the step can finish successfully and mask that earlier failure. This is a confirmed workflow robustness gap from the script structure; no failing test was induced during this audit.

**Recommended:** ensure every native test invocation’s exit status is checked immediately and makes the step fail; retain the final status propagation as an additional guard.

### C6 — CLI test evidence varies; one test does not assert server receipt

`sessions/SES-043/test_p2p_two_nodes.py` starts Node B with `subprocess.Popen` and Node A with `subprocess.run`, so they are distinct OS processes (lines 30–64). But it only asserts `pong-from-B` in client stdout (line 66), leaves server output in pipes without reading/asserting it, and terminates the listener in cleanup (lines 67–75). This test alone does not assert that B recorded the submitted message.

The Linux packaged smoke test does stronger checks: it launches a listener executable in the background, runs a separate client executable, then checks the listener log for both peer label and `hello-from-A` (`build-p2p-linux.yml`, lines 57–65). The Windows packaged smoke test similarly starts a listener process, runs a separate executable client, waits for B to exit and asserts the log contains the peer and message (`build-p2p-windows.yml`, lines 59–68). These test designs genuinely involve separate processes and server-side receipt assertions, unlike an in-process mock. Whether they passed on the reviewed PR head is not established by this report.

`sessions/SES-090/E2E_RESULTS.txt` records two real CLI processes, output and exit codes, but it is a checked-in session result rather than independently reproduced evidence here.

## Potential issues / gaps in evidence

### P1 — Windows/Linux smoke coverage differs

The Linux packaged smoke step additionally exercises a non-loopback address path (`build-p2p-linux.yml`, lines 66–76); the Windows packaged smoke step tests loopback only (`build-p2p-windows.yml`, lines 51–71). This is an observable coverage difference, not proof that Windows networking is broken. The shared regression test `sessions/SES-058/test_non_loopback_ipv4.py` is invoked in both build workflows, but the separate packaged-executable LAN smoke remains Linux-only.

### P2 — Android workflow builds APK but does not run SES-090 Python regression tests

`.github/workflows/build-p2p-android.yml` sets up Java/Python and runs Gradle `assembleDebug`, verifies the APK exists, and uploads/attests it (lines 20–52); it does not invoke `tests/test_message_integrity.py` or a protocol integration test. The SES-090 spec says `android/` was not changed. The Android workflow therefore supplies APK build evidence, not evidence that the Android application implements or interoperates with the new Python V2 signed-message protocol. The docs describe APK build and an Android↔Windows ADB path but do not claim Android SES-090 protocol coverage.

### P3 — Frame-size regression does not exercise SES-090 boundary cases

`sessions/SES-067/test_frame_size_limit.py` sends an oversized application string through `P2PNode.send` and expects the listener to reject an oversized frame. Since SES-090 adds a `MSG` header and signature, the wire frame is larger than the text. No inspected test explicitly asserts the largest accepted signed payload and just-over-limit signed payload boundary. Existing rejection coverage supports oversize detection but does not document the precise usable text-size boundary after framing overhead.

### P4 — Test sets are split across workflows and platforms

The Linux and Windows executable workflows run matching SES-046/047/049/055/058/059/061/064/065/067/068/069/084/085/081/082/083 tests plus `tests/test_message_integrity.py`. Trusted introductions have a separate Linux workflow (`p2p-trusted-introductions.yml`, lines 12–25). Other node-related tests named in `GREEN_RESULTS.txt` are likewise not all listed in both executable workflows. This is not a direct omission of the new SES-090 test from Windows—the PR adds it to both—but the “all node-related test files” evidence is broader than any one Linux/Windows build workflow and should not be read as identical platform coverage.

## Workflow configuration and permissions

- The Linux and Windows build workflows both declare `contents: read`, `id-token: write`, and `attestations: write` (each lines 9–12), and both invoke `actions/attest@v4` for artifacts. The two write permissions are used by artifact attestation in those jobs; this audit found no basis to call them unnecessary for these workflows.
- The Android workflow declares the same write permissions and uses `actions/attest@v4` (lines 9–12, 43–46), so those permissions also have an apparent workflow purpose.
- The trusted-introductions workflow requests only `contents: read` (lines 9–10), a least-privilege pattern for its checkout/test job.
- No YAML syntax/configuration defect was confirmed by static inspection. This is not a workflow-validator run.
- PR #20 says GitHub Actions had not run on the feature branch. The available Actions metadata included completed check-run entries and recent default-branch workflow runs, but the tool responses did not provide reliable per-run conclusions and did not establish that the runs correspond to the PR head. The audit therefore makes no PASS claim for PR-head Linux, Windows, Android, or the full CI matrix.

## Confirmed problems

1. **Windows pytest step can mask an earlier failing native pytest command** because the step does not explicitly stop/check after each command (C5). Fix is recommended before relying on Windows as a regression gate.
2. **The SES-043 CLI test does not assert server-side receipt** despite starting two processes (C6). It should not be counted by itself as proof that the submitted application payload was received by the second process.

## Prioritized recommended follow-up

1. **P1 — Make Windows regression commands fail-fast per pytest invocation.** Check native exit codes immediately so a later successful test cannot mask a prior failure.
2. **P1 — Require actual PR-head CI evidence before declaring SES-090 green/stone.** Verify the exact head SHA and record Linux and Windows results; keep Android evidence clearly scoped to APK build unless protocol interoperation is tested there.
3. **P2 — Strengthen `sessions/SES-043/test_p2p_two_nodes.py` to assert B’s output/received message and cleanly wait for B.** This makes that test independently demonstrate request receipt, rather than relying on an unauthenticated response alone.
4. **P2 — Add/record signed-frame maximum-size boundary coverage.** Test the maximum accepted signed frame and an over-limit signed frame, with framing overhead included.
5. **P3 — Decide whether packaged Windows smoke should mirror Linux non-loopback coverage.** If parity is intended, add an equivalent Windows test; otherwise document the intentional platform boundary.

These are audit recommendations only; no fixes were made.

## SES-090 known limitations and documentation consistency

The inspected PR records these limits explicitly:

- no message confidentiality (Ed25519 signing, not encryption);
- unauthenticated `pong-from-B` response, with separate open follow-up;
- client does not pin the expected server identity;
- breaking V1/V2 compatibility; rebuild/deploy nodes together;
- physical-network behavior and PR-branch CI not established by local Linux evidence;
- handshake parsers retain pre-existing lenient base64 behavior;
- `VOUCH` and HELLO label are outside the application-message signature.

The README, `P2P_NODE.md`, and `CURRENT_STATE.md` specifically make the unauthenticated response and/or encryption boundary visible. No inspected claim suggested end-to-end encryption or authenticated response semantics.

## Not verified

- Independent execution of any tests, mutation checks, relay script, CLI E2E script, or YAML/workflow validation.
- GitHub Actions completion/conclusions for the exact PR head SHA, especially Windows and Android. The draft’s local result files are recorded evidence, not independent reruns.
- Whether Android APK behavior is intended to implement the same Python P2P protocol; `android/` was not changed in SES-090 and its full source behavior was outside this audit’s verification.
- Actual physical LAN, NAT/firewall, Internet, adversarial relay, or deployment behavior.
- Repository settings outside checked-in workflow permissions, including organization/repository token policy or protections.
- Whether all externally distributed historical release binaries have been rebuilt/deployed; compatibility risk is documented but distribution state was not audited.

## Audit boundary

This audit report is the only file added by this task, on branch `audit/GAP-090-A`, based on `main` at `9410b7457d0266bae9e7b95a5da0b669cde5710e`. No changes were made to source, tests, workflows, documentation outside this report, `main`, or PR #20; no merge or destructive operation was performed.
