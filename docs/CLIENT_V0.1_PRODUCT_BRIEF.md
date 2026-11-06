# P2P 60-24 Client v0.1 — Product Brief

**Status:** proposed product scope; not an approved protocol/API change  
**Session:** SES-089  
**Audience:** human collaborators, ChatGPT, Claude Code and future agents

## 1. Purpose in plain language

Turn the existing P2P 60-24 runtime into the smallest program a normal person can launch and use to communicate with another person.

The product should feel like a small standalone P2P client (the usability reference is Tox/Jami), not like a developer CLI. Bitcoin Core is a reference for running one's own node, not for copying its blockchain or financial model. ZeroNet is a reference for decentralised operation, not a requirement to reproduce its web stack.

The immediate objective is a real, testable first user experience—not a complete production messenger.

## 2. User-visible first milestone

A user should be able to:

1. launch the client;
2. create or reuse a persistent local identity;
3. see their own public identity / share an invitation;
4. add or accept another person's identity/invitation;
5. see whether the peer is connected or reachable (the UI must distinguish these states honestly);
6. send and receive a message;
7. close and reopen the client without losing identity or trusted contacts.

The minimum acceptance demonstration is two independent devices and two independent identities. Begin with a controlled LAN scenario. Do not claim Internet-wide operation.

## 3. What exists in the inspected main branch

The repository README and source currently document/provide:

- Python P2P runtime in `src/p2p/`;
- Ed25519 identity and proof-of-possession handshake;
- NodeID derived from the public key;
- persistent CLI identity storage;
- TCP transport adapter;
- HELLO/WELCOME/AUTH handshake;
- trusted-key authorization and signed trust-introduction vouchers (`src/p2p/trust.py`);
- Linux and Windows executable build paths;
- Android application/build path.

Relevant inspected files:

- `src/p2p/node.py` — P2PNode and CLI;
- `src/p2p/protocol.py` — wire protocol and handshake;
- `src/p2p/transport.py` — transport boundary and TCP adapter;
- `src/p2p/trust.py` — signed introductions;
- `android/app/src/main/java/org/p2p6024/android/MainActivity.java` — existing basic Android UI;
- `android/app/build.gradle` — Android packaging and Chaquopy integration;
- `windows/README.txt` — Windows console test instructions.

This is a source inspection snapshot, not a claim that every build artifact or physical network path was tested in this session.

## 4. Important implementation reality

The current CLI flow is one-shot:

- listener calls `listen_once()`, handles one connection/message/response and exits;
- connector sends one message, receives one response and exits.

The existing Android UI exposes host, port, node label and message fields with `Connect` and `Listen once` actions. It is a useful prototype, but it is not yet a normal contact-and-chat client.

Therefore, persistent bidirectional conversations, background listening, peer lifecycle, contact storage and a finished user experience must be inspected as real gaps—not assumed to exist.

## 5. Product constraints

- End-user installation must not require Docker or Kubernetes.
- Do not introduce libp2p, IPFS, databases, relay services or other dependencies without a demonstrated GAP and review.
- Do not require a central service for the basic local P2P demonstration.
- A client and its node run on the same device.
- Preserve the existing identity and protocol contracts unless a reviewed change is explicitly approved.
- Keep the System Builder separate. This repository is the P2P product.
- No blockchain, token, mining, wallet or payment feature.
- No claim of end-to-end encryption: current authenticated identity is not equivalent to E2E message encryption.
- No claim of Internet-wide connectivity until discovery/NAT traversal/relay requirements are solved and evidenced.

## 6. Scope discipline

### v0.1 must prove

- first launch and persistent identity;
- peer invitation / trusted peer setup using the existing mechanisms where possible;
- a usable two-device connection flow on LAN;
- message exchange with clear status and error feedback;
- restart persistence for identity and contacts;
- reproducible automated tests and packaged build evidence.

### Explicitly out of scope until justified

- automatic global peer discovery;
- NAT traversal and relay;
- mesh routing;
- group chat;
- file transfer;
- voice/video;
- global reputation or trust score;
- production security certification;
- cloud account or central user directory.

## 7. Key architectural questions — answer before implementation

1. Which current platform is the shortest path to a usable v0.1: extend Android UI, create a Windows desktop UI, or share a UI layer? Base the recommendation on actual code/build evidence.
2. Can the existing runtime support a persistent, bidirectional session without unsafe protocol shortcuts?
3. What is the minimum listener lifecycle needed for an always-available foreground client? What happens when the app is backgrounded or closed?
4. Can identity and trusted contacts be managed through existing APIs, or is a minimal service boundary required?
5. What exact changes are GREEN (internal/UI/docs/tests) and what changes are YELLOW (wire protocol, public API, storage schema, security semantics)?
6. What is the smallest end-to-end test that proves two real clients can exchange multiple messages and reconnect?

## 8. Definition of done for the first usable client

A v0.1 claim is allowed only when evidence demonstrates:

- two separately installed/running clients on independent devices;
- stable distinct identities across restart;
- invitation/trust path works and an untrusted peer is rejected;
- both sides can exchange more than one message in a session, or the product explicitly labels the first version as one-message demo;
- connection/error state is understandable to a non-developer;
- automated regression tests pass on the relevant code;
- the exact packaged artifact and tested commit are recorded;
- no Docker/Kubernetes setup is required by the end user.

## 9. Decision rule

**Reuse → Integrate → Improve → Invent.**

First inspect and reuse the existing Android/client/runtime pieces. Do not start a new GUI framework or redesign the protocol until the audit demonstrates that it is necessary.

A recommendation must name one preferred path, explain why, state trade-offs and identify approval gates.
