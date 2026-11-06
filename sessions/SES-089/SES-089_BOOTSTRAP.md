# SES-089 — CLIENT v0.1 BOOTSTRAP

**Project:** P2P 60-24 OneClick Evo Positiv  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Base branch:** `main`  
**Working branch:** `ses-089-client-v01-brief`  
**Purpose:** move from a developer-oriented P2P runtime to the smallest usable end-user client.

## 1. Mission

Build the simplest usable client that lets two people operate their own P2P nodes and communicate. Tox/Jami are usability references; Bitcoin Core is a reference for owning/running a node. Do not copy blockchain, token, payment or unrelated infrastructure.

## 2. Shared understanding

The repository already contains a functioning minimal P2P runtime, Ed25519 identity, authenticated handshake, persistent CLI identity, TCP transport and signed trusted introductions. It also contains a basic Android UI and Windows console launch/test path.

The Android UI is currently a prototype with host/port/label/message fields and Connect / Listen once actions. The CLI listener handles one connection/message and exits. This is not yet a continuous chat client.

Read `docs/CLIENT_V0.1_PRODUCT_BRIEF.md` for the product goal, verified current boundaries, constraints, open questions and acceptance criteria.

## 3. Authority and working rules

Read in this order:

1. `AGENTS.md`
2. `P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md`
3. `START_HERE.md`
4. `docs/CURRENT_STATE.md`
5. `docs/REPOSITORY_MAP.md`
6. `docs/CLIENT_V0.1_PRODUCT_BRIEF.md`
7. Relevant source, tests, workflow files and latest session evidence.

Repository is source of truth; chat memory is not. Human decides intent and protected architecture. Follow GREEN/YELLOW/RED/BLACK boundaries in AGENTS.md.

## 4. First work order

See `sessions/SES-089/CLAUDE_CODE_WORK_ORDER_01.md`.

The first task is inspection and a decision-quality audit only. Do not implement a GUI, change protocol, add dependencies, alter runtime, or merge anything in this task.

## 5. Communication contract

Report in plain Polish or clear technical English with short explanations:

- **Plan:** what will be inspected and expected output size.
- **Findings:** facts with exact file paths and relevant symbols.
- **GAP:** demonstrated gap, not an assumed feature request.
- **Recommendation:** one preferred implementation path and why.
- **Approval gates:** identify GREEN/YELLOW/RED/BLACK.
- **Evidence:** exact commands, test names/results, commit SHA and CI run URLs.
- **Unknowns:** state explicitly; never convert unknown into PASS.

For every proposed change, explain:
1. what changes;
2. why it is needed;
3. what remains unchanged;
4. how it will be tested;
5. what user-visible result it creates.

Do not claim GREEN unless the relevant test/CI result is observed on the exact commit.

## 6. Current session state

- Documentation-only preparation is being made on `ses-089-client-v01-brief`.
- No runtime implementation is authorized by this bootstrap.
- No change to protocol, trust semantics, identity format, canonical ontology or Constitution is authorized.
- Next checkpoint: Claude Code completes Work Order 01; ChatGPT reviews the evidence and updates the shared plan.
