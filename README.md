# P2P 60-24 OneClick Evo Positiv

**Minimal, standalone P2P runtime for direct Node A ↔ Node B communication.**

> **Current checkpoint: SES-081 = STONE.**  
> Current HEAD: `39154e20b168d72bb328e3c7cab805c4ee7f2595`

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

For the latest completed engineering change, see [SES-081 closeout](sessions/SES-081/SES-081_CLOSEOUT.md).
