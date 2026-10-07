# Repository Map

This page is the orientation map for people and AI agents.

## Core

| Path | Role |
|---|---|
| `START_HERE.md` | shortest orientation path |
| `README.md` | current runtime usage |
| `AGENTS.md` | AI/human working rules |
| `P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md` | engineering authority/autonomy |
| `requirements.txt` | Python dependencies |

## Runtime

| Path | Role |
|---|---|
| `src/p2p/node.py` | Mini Node and CLI |
| `src/p2p/protocol.py` | wire protocol / framing / handshake semantics |
| `src/p2p/transport.py` | transport contract + TCP adapter |
| `demo/` | runnable/demo entrypoints |
| `windows/` | Windows launchers and test instructions |
| `android/` | Android client/build |

## Verification

| Path | Role |
|---|---|
| `sessions/SES-*/test_*.py` | regression tests tied to discovered boundaries |
| `.github/workflows/build-p2p-linux.yml` | Linux build + regression + packaged smoke |
| `.github/workflows/build-p2p-windows.yml` | Windows build + regression + packaged smoke |
| `.github/workflows/build-p2p-android.yml` | Android APK build |
| `.github/workflows/p2p-evidence.yml` | machine-readable Linux evidence status |
| `.github/workflows/p2p-release.yml` | tag-bound release packaging |

## Architecture and project meaning

| Path | Role |
|---|---|
| `ontology/` | canonical ontology area; currently mostly structural/documentary |
| `architecture/` | canonical architecture area; currently mostly structural/documentary |
| `constitution/` | constitutional document index; do not infer frozen rules from planned files |
| `docs/CURRENT_STATE.md` | current factual snapshot |
| `docs/PROJECT_OVERVIEW_FOR_HUMANS.md` | human-readable project history |
| `docs/FUTURE_ARCHITECTURE_REFERENCE.md` | future/reference concepts; not automatic implementation requirements |
| `docs/history/` | historical summaries/audits |

## Sessions

`sessions/` is the engineering evidence/history trail.

Current sessions use a practical pattern such as:

- `*_BOOTSTRAP.md` — starting state and scope,
- `*_CHECKPOINT*.md` — intermediate evidence,
- `*_CLOSEOUT.md` / `STONE.md` — completed checkpoint,
- `test_*.py` — executable regression proof.

Older sessions use additional historical naming conventions. Do not rewrite historical records merely to make them uniform.

**Latest completed session is the strongest session-level orientation point.**

## External audits and research

- `docs/external-audits/` — external audit material.
- `Qwen_*.md`, `chat-*.txt` and similar large imported texts are research/history inputs, not canonical architecture.
- External proposals must be evaluated against repository contracts before adoption.

## What is canonical?

For implementation:

**code + tests + CI/evidence + approved architecture/ontology/Constitution**

For history:

**session records**

For research:

**external-audit/reference documents**

For conversation:

**chat is context only**

## Safe navigation rule

If a document claims something about the current runtime, verify it against code and current CI before treating it as fact.

If a proposed change affects Constitution, ontology foundations, Trust semantics, protocol/data model or cross-layer contracts, follow the autonomy rules in `AGENTS.md`.
