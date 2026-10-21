# SES-087 — CHECKPOINT 08: CI and root artifact provenance

**Date:** 2026-10-21  
**Branch:** `main`  
**Audited HEAD:** `cdcdbb2bde1b7b87d6a51a39c02f575a8abcc6d0`  
**Status:** CHECKPOINT — audit remains open

## 1. CI snapshot

The following 15 workflow runs were inspected for the audited HEAD. All completed with `success`:

- P2P Evidence Check: `39381110437`, `39381108446`, `39381104504`, `39381073000`, `39381009579`
- SES-032 E2E integration: `39380991950`
- P2P Windows executable: `39380991893`
- P2P Android APK: `39380991890`
- SES-045 concrete P2P node: `39380991867`
- P2P Linux executable: `39380991865`
- SES-025 Runtime Flow Contract: `39380991864`
- SES-023 Runtime Entry Point Contract: `39380991855`
- SES-043 P2P proof: `39380991854`
- Beta local execution: `39380991853`
- SES-024 Runtime Observation Contract: `39380991848`
- SES-011 BuildPlan Contract: `39380991844`

This is a snapshot of listed workflows for this commit, not a blanket claim that every repository workflow or every product behavior is covered.

## 2. Root-level binary files — provenance

Four UUID-named `.bin` files remain in the repository root:

| File | Size (bytes) | Blob SHA |
|---|---:|---|
| `6c52d31b-aabd-4dbf-b731-62cc19a6b2d9.bin` | 22,328 | `c11580a09949653ceb82b3e9b8ffc076995a55bc` |
| `8cd087d4-11f3-4c0d-aa11-5a8dd405fadf.bin` | 7,243 | `38b58e0ff764e443c5c447b4e16a1eb22d2d93fa` |
| `a77f7a52-983f-4bb7-b316-7df927ca80c9.bin` | 10,646 | `0a94b9286bcd6763773a36428a9164b938cc9264` |
| `b341b83c-e7a8-416a-adce-d8e87d2ba370.bin` | 56,813 | `e6ef0239a929b60a0936139a10d9a64cc60fd89e` |

GitHub path history reports all four were introduced by commit `c48f327b5a` (“Ses 1”, 2026-09-24). This establishes common provenance, **not** their content, purpose, safety, or whether they are required.

The connected GitHub fetch path rejected attempts to retrieve the binary blob payload as UTF-8. Therefore file signatures/content could not be verified in this audit pass. No binary was deleted, renamed, or modified.

**Next bounded step:** inspect these files through a byte-preserving route and correlate their content with the originating “Ses 1” work before deciding whether to document, relocate, or remove them.

## 3. Historical transcript

`chat-Decentralized Computing Network.txt` is 224,663 bytes and its path history reports a single introduction commit `78edaac61b` (“Add files via upload”, 2026-04-20). Inspection of its beginning and end confirms it is a historical conversation/document dump containing aspirational architecture proposals and a prior-session closeout. It is not evidence that those proposed components are implemented in the current runtime.

No transcript content was changed. Avoid treating old claims such as “Trust Layer + Network Abstraction = ready” as current implementation evidence without matching code/tests.

## 4. Authority and scope boundaries

- G-01 GS-01 run `39380809928` and GS-02 run `39380814995` remain bounded successful developer/CI checks; they do not establish full Graph conformance or approve DEC-007–DEC-013.
- Developer-side Docker use in CI is distinct from the shipped product. The end-user runtime must not require Docker, Kubernetes, Neo4j, or other test infrastructure.
- No runtime, protocol, trust model, or canonical ontology change was made.
- Tagology remains deferred/experimental; human approval boundaries remain unchanged.

## 5. Outcome

**CI snapshot: GREEN for the 15 listed runs on the audited HEAD.**  
**Repository hygiene audit: OPEN.** The four binary files are traceable to one commit but their content and purpose remain unresolved.
