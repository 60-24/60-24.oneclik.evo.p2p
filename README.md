# P2P 60-24 OneClick Evo Positiv

**Minimal, standalone P2P runtime for direct Node A ↔ Node B communication.**

> **Latest closed technical session: SES-085 = STONE.** SES-087 is a separate documentation/audit session in progress.  

## Start here

If you are new to the repository, read in this order:

1. **[START HERE](START_HERE.md)** — shortest orientation.
2. **[Current State](docs/CURRENT_STATE.md)** — factual implementation boundary.
3. **[Repository Map](docs/REPOSITORY_MAP.md)** — where things live.
4. **[Project Overview](docs/PROJECT_OVERVIEW_FOR_HUMANS.md)** — history and rationale.
5. **[AGENTS.md](AGENTS.md)** — how changes are made safely.

## What the current program does

Two independent nodes can:

`Node A → TCP → HELLO/WELCOME/AUTH → authenticated peer → message → response`

The current runtime includes:

- Ed25519 cryptographic identity and proof-of-possession;
- persistent local CLI identity;
- NodeID derived from the public key;
- frame-size protection;
- malformed/truncated/coalesced-frame handling;
- optional trusted introductions (web of trust): a listening node can require
  that a peer's key is trusted or vouched for by a trusted sponsor;
- a transport boundary with TCP as the current adapter;
- Linux and Windows executable builds;
- Android APK build;
- Android ↔ native Windows ADB integration path;
- automated CI verification and build artifacts.

## Quick local test

### Node B

```bash
./P2P60-24Node --listen 127.0.0.1:39001 --node-id B
```

### Node A

```bash
./P2P60-24Node --connect 127.0.0.1:39001 --node-id A --message "hello-from-A"
```

Expected:

- Node A: `pong-from-B`
- Node B: `node B received from A: hello-from-A`

For Linux/Windows/Android packaged paths, use the relevant GitHub Actions artifact and the instructions in [windows/README.txt](windows/README.txt).

## LAN test

Node B:

```bash
./P2P60-24Node --listen 0.0.0.0:39001 --node-id B
```

Node A:

```bash
./P2P60-24Node --connect <NODE_B_LAN_IP>:39001 --node-id A --message "hello-from-LAN"
```

Use the real LAN IPv4 address of Node B.

## Trusted introductions (web of trust)

A listening node can require that every peer is either directly trusted or
introduced by someone trusted. An introduction (voucher) is the sponsor's
Ed25519 signature over the invited peer's public key. No server, no database.

```bash
# each person prints their identity once
./P2P60-24Node --show-identity --node-id tomek
./P2P60-24Node --show-identity --node-id siostra

# the sponsor signs the invited person's public key
./P2P60-24Node --issue-voucher <SIOSTRA_PUBLIC_KEY_B64> --node-id tomek > voucher-siostra.txt

# Node B accepts only keys listed in trusted_keys, or peers vouched by them
echo "<TOMEK_PUBLIC_KEY_B64>" > trusted_keys
./P2P60-24Node --listen 0.0.0.0:39001 --node-id B --trusted-keys trusted_keys

# the invited peer presents the voucher during the handshake
./P2P60-24Node --connect <NODE_B_IP>:39001 --node-id siostra --voucher voucher-siostra.txt --message "hello"
```

A peer that is neither listed nor vouched for is rejected after
authentication, before any message is accepted. Without `--trusted-keys` the
listener behaves exactly as before (open, backward compatible).

Evidence: `tests/test_trusted_introductions.py` (CI: "P2P trusted introductions").

## Evidence boundary

The repository is a proof-oriented engineering project.

Do not overclaim:

- CI success proves the checked CI path, not every physical network.
- ADB bridge proves Android ↔ native Windows integration, not physical LAN.
- An artifact is not automatically a permanent public release.
- Cryptographic authentication is not a global Trust system.
- The current runtime is not Internet-wide P2P.
- Future architecture documents are not current implementation.

## Current limitations

The runtime does not yet provide:

- automatic peer discovery,
- NAT traversal,
- relay infrastructure,
- end-to-end encryption,
- advanced authorization,
- GUI,
- automatic installation,
- production-grade Internet deployment.

These are **limitations, not automatic GAPs**.

## Engineering method

Every non-trivial change follows:

**INSPECT → UNDERSTAND → IDENTIFY REAL GAP → RED → MINIMAL IMPLEMENTATION → GREEN → EVIDENCE → STONE**

No artificial RED. No feature only because a technology exists.

## Scope boundary

**P2P 60-24 OneClick Evo Positiv is the concrete system.**

The **System Builder** is a separate, broader metasystem concept. Historical System Builder material remains for traceability and must not be confused with the current P2P runtime.

## Source of Truth

Repository state, approved architecture/ontology/Constitution, code, tests and CI evidence outrank chat memory.

For the latest completed technical change, see [SES-085 closeout](sessions/SES-085/SES-085_CLOSEOUT.md). For current architecture-authority audit work, see [SES-087 audit checkpoint 04](sessions/SES-087/SES-087_AUDIT_CHECKPOINT_04.md).
