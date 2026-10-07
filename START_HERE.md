# P2P 60-24 OneClick Evo Positiv — START HERE

## What this repository is

A small, standalone P2P runtime proving direct **Node A ↔ Node B** communication.

Current proven chain:

`local identity → HELLO/WELCOME/AUTH → authenticated peer → message → response`

The repository is **not** a production P2P network and is **not** the complete System Builder.

## Current checkpoint

- Branch: `main`
- Latest checkpoint: **SES-081 = STONE**
- Current HEAD: `39154e20b168d72bb328e3c7cab805c4ee7f2595`
- Current focus: preserve a small, modular Mini Node and find the next real GAP by inspection.
- Rule: **INSPECT → UNDERSTAND → REAL GAP → RED → MINIMAL CHANGE → GREEN → EVIDENCE → STONE**

## Read in this order

1. **[README](README.md)** — how the current runtime is used.
2. **[Current State](docs/CURRENT_STATE.md)** — what is actually implemented and proven now.
3. **[Repository Map](docs/REPOSITORY_MAP.md)** — where code, tests, architecture and evidence live.
4. **[Project Overview for Humans](docs/PROJECT_OVERVIEW_FOR_HUMANS.md)** — history and rationale.
5. **[AGENTS.md](AGENTS.md)** — rules for AI/human engineering work.
6. **[Engineering Constitution](P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md)** — authority and autonomy boundaries.
7. **[latest session](sessions/SES-081/SES-081_CLOSEOUT.md)** — latest completed engineering change.

## What is real today

Proven in repository/CI evidence:

- TCP Node A ↔ Node B communication.
- HELLO/WELCOME/AUTH handshake.
- Ed25519 proof of possession.
- NodeID derived from public key.
- Persistent local identity.
- Frame-size limit and malformed/truncated/coalesced-frame handling.
- Linux and Windows executable builds.
- Android APK build.
- Android ↔ native Windows USB/ADB integration path.
- GitHub Actions evidence and artifacts.
- Transport adapter boundary introduced in SES-081.

## What is deliberately not here yet

No current GAP authorizes adding:

- automatic discovery,
- NAT traversal,
- relay infrastructure,
- mesh,
- CRDT/OrbitDB,
- IPFS/Helia,
- libp2p,
- Trust/RealBond layers,
- AI/swarm orchestration,
- production security/GUI/installer.

These remain future candidates, not current implementation requirements.

## Important boundary

**P2P 60-24 is a concrete system. System Builder is a separate, broader metasystem concept.**

Historical System Builder material remains in the repository for traceability. It must not be mistaken for the current P2P runtime.

## Engineering rule

Do not create work merely because a technology or idea exists.

If inspection finds no real GAP, the correct result is **NO GAP / STOP**.
