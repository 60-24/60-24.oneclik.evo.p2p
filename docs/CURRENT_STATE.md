# Current State — P2P 60-24 OneClick Evo Positiv

**As of:** 2026-10-19  
**Branch:** `main`    
**Latest closed technical session:** SES-085 — STONE
**Latest documentation work:** SES-087 in progress (authority/status index; not a runtime change)

## 1. Identity of the project

This repository contains the concrete **P2P 60-24 OneClick Evo Positiv** system.

It is currently a **minimal proof-of-concept/runtime**, not a production product.

The separate **System Builder** is a broader metasystem concept. Historical System Builder artifacts may exist here, but they are not the current P2P runtime.

## 2. Proven runtime boundary

Current runtime:

`Identity → Protocol → Transport adapter → socket`

Application flow:

`Node A → TCP → HELLO/WELCOME/AUTH → authenticated peer → message → response`

Identity:

- Ed25519 key pair.
- `NodeID = SHA-256(public key)`.
- Persistent local key storage for the CLI.
- Corrupt existing identity is rejected.

Protocol:

- HELLO / WELCOME / AUTH.
- Proof-of-possession signatures.
- Maximum frame size.
- Explicit handling of EOF/truncated and coalesced frames.

Transport:

- Internal `Transport` contract.
- `TCPTransport` implementation.
- TCP remains the default.
- Added in SES-081 without changing protocol or identity semantics.

## 3. Build and evidence

GitHub Actions currently builds/tests:

- Linux executable.
- Windows executable.
- Android debug APK.
- Linux evidence status.
- Tagged release packaging workflow exists for Linux/Windows/Android.

Important evidence boundary:

**CI success proves the checked workflow. It does not prove every physical network environment.**

In particular:

- Android ↔ Windows through ADB is not physical LAN evidence.
- Build artifact is not the same as public release.
- Current runtime is not Internet-wide P2P.
- Authentication is not a global Trust system.

## 4. Known intentional limitations

The runtime currently does not provide:

- automatic peer discovery,
- NAT traversal,
- relay infrastructure,
- end-to-end encryption,
- advanced authorization,
- GUI,
- automatic installation,
- production-grade Internet deployment.

These are limitations, not automatically GAPs.

## 5. Latest completed change — SES-081

**GAP-081-01:** TCP transport concerns were directly owned by `P2PNode`.

Minimal correction:

- `src/p2p/transport.py`
- internal `Transport` contract
- `TCPTransport` adapter
- optional transport injection into `P2PNode`
- transport-boundary regression test

Verified implementation commit:

`df1b2ec4c31fe3edb2c22d885de44ca1330efd5a`

SES-081 closeout:

`sessions/SES-081/SES-081_CLOSEOUT.md`

## 6. Later verified engineering checkpoints (through 2026-10-19)

The following sessions were recorded after the earlier SES-081 snapshot:

- SES-082: outgoing single-line message validation; see `sessions/SES-082/`.
- SES-083: inbound message line validation; merged to `main` according to its session record.
- SES-084: deterministic regression test for coalesced TCP frames.
- SES-085: regression test for EOF after authenticated handshake but before a complete application frame. The test checks the listener terminates, rejects the incomplete frame, records the authenticated peer, and leaves `last_message` unset. See `sessions/SES-085/SES-085_CLOSEOUT.md` and `sessions/SES-085/test_eof_after_auth.py`.

The Linux and Windows build workflows both invoke the SES-085 test. SES-085 closeout records Linux and Windows CI success for its tested implementation commit. This does **not** establish CI status for later documentation-only commits or every current HEAD.

SES-086 Tagologia is a separate experimental proposal, not merged into `main`. The proposal and its isolated validator are not part of the P2P runtime. See `docs/TAGOLOGY_DEFERRED.md` for the current defer decision.

SES-087 is currently documenting architecture authority and traceability. No runtime or canonical ontology change has been made in that work.

## 7. Current engineering question

The next session must not assume that another feature is required.

First inspect:

1. architecture boundaries,
2. code/tests,
3. CI/evidence,
4. documentation consistency,
5. release/distribution boundary,
6. current Mini Node behavior.

Then identify **one real GAP or NO GAP**.

## 8. Authority

When information conflicts:

1. approved project Constitution / frozen decisions,
2. Engineering Constitution,
3. ontology and invariants,
4. architecture/ADRs,
5. code/configuration,
6. tests/evidence,
7. session notes,
8. chat memory.

Repository state wins over conversational memory.

## 9. One-line status

> **A real, small, authenticated and testable Node A ↔ Node B foundation exists; the project is now strengthening its boundaries before adding the next layer.**
