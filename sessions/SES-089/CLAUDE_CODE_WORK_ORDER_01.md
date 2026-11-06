# SES-089 — Claude Code Work Order 01
## Audit the shortest path to P2P Client v0.1

**Task type:** INSPECT / UNDERSTAND / GAP  
**Expected output:** one concise audit report (roughly 2–5 pages) plus a proposed test/implementation sequence.  
**Implementation authority:** NONE for this work order.

### Objective

Determine the simplest safe path from the existing repository to a usable P2P client for two people. Do not assume that a new desktop GUI is the right first step. Inspect the existing Android UI, Windows packaging, runtime lifecycle and trust/identity code first.

### Required inspection

1. Read `AGENTS.md`, Engineering Constitution, `START_HERE.md`, `docs/CURRENT_STATE.md`, `docs/REPOSITORY_MAP.md` and `docs/CLIENT_V0.1_PRODUCT_BRIEF.md`.
2. Inspect:
   - `src/p2p/node.py`
   - `src/p2p/protocol.py`
   - `src/p2p/transport.py`
   - `src/p2p/trust.py`
   - Android `MainActivity.java`, Python bridge/module, Gradle configuration and Android workflow;
   - Windows launchers/build workflow and current executable packaging;
   - relevant tests for identity persistence, handshake, trusted introductions, framing, disconnect and two-node integration.
3. Inspect current GitHub Actions definitions and recent evidence. Record the exact commit tested; do not treat old successful runs as proof for current HEAD.
4. Identify actual runtime behavior:
   - Does one listener accept one peer only or multiple sequential/concurrent peers?
   - Does a connection remain open for one message or multiple messages?
   - Is communication bidirectional within one connection?
   - What is the lifecycle on timeout, disconnect, app backgrounding and process exit?
   - Where are private identity keys and trusted peer keys stored on each platform?
   - Are keys protected with appropriate platform permissions/storage?
   - Can Android currently act as both initiator and listener in a practical two-device setup?
5. Separate facts, assumptions, proposals and unknowns.

### Required report structure

1. **Executive summary** — current maturity in plain language.
2. **What already works** — exact source files and tests.
3. **What the current Android app does** — screens/actions and limitations.
4. **What the current Windows client does** — launcher, CLI and packaging.
5. **Runtime lifecycle** — sequence diagram or numbered flow for connect/listen/message/disconnect.
6. **GAP matrix** — requirement / current evidence / missing behavior / risk / test needed.
7. **One recommended path** — choose the smallest coherent platform/UI approach; explain why alternatives are not preferred now.
8. **Test plan** — unit, integration, two-device LAN and packaged smoke tests.
9. **Approval gates** — identify any protocol/API/storage/security changes as YELLOW/RED.
10. **Next Claude work order** — one small measurable task only after audit.

### Non-negotiable constraints

- Do not modify production code or protocol.
- Do not add libraries, databases, services or frameworks.
- Do not introduce Docker or Kubernetes as end-user requirements.
- Do not introduce libp2p, IPFS, blockchain, tokens, mining, wallets or payment logic.
- Do not claim end-to-end encryption.
- Do not redesign the Trust model or change voucher semantics.
- Do not merge or push implementation changes to `main`.
- Do not trigger the known Docker-based G-01 Neo4j workflows.
- If the source contradicts documentation, report the exact contradiction; do not silently rewrite history.

### Acceptance criteria

The task is complete only when the report:
- cites concrete paths, symbols and tests;
- distinguishes existing behavior from intended behavior;
- identifies the smallest real GAP for a usable first client;
- recommends one path;
- states what needs human approval;
- proposes a testable next task.

If evidence is unavailable, mark it **NOT VERIFIED**. Do not guess.
