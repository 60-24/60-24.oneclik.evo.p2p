# SES-087 — CHECKPOINT 08: CI and root artifact provenance

**Date:** 2026-10-21  
**Branch:** `main`  
**CI snapshot HEAD:** `cdcdbb2bde1b7b87d6a51a39c02f575a8abcc6d0`  
**Status:** CHECKPOINT — audit remains open

## 1. CI snapshot

The following 15 workflow runs were inspected for the CI snapshot HEAD. All completed with `success`:

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

This is a snapshot of listed workflows for that commit, not a blanket claim that every repository workflow or every product behavior is covered.

## 2. Root-level files with a `.bin` extension

All four files were introduced together in commit `c48f327b5a` (“Ses 1”, 2026-09-24). Inspection of that commit's diff and the base64 prefix of the fourth file clarifies their formats:

| File | Size (bytes) | Observed content / format | Blob SHA |
|---|---:|---|---|
| `6c52d31b-aabd-4dbf-b731-62cc19a6b2d9.bin` | 22,328 | HTML document titled “P2P 60-24 EVO — Balanced State Report” | `c11580a09949653ceb82b3e9b8ffc076995a55bc` |
| `8cd087d4-11f3-4c0d-aa11-5a8dd405fadf.bin` | 7,243 | Bash script labelled as an autonomous GitHub push script; references a historical local path and old repository | `38b58e0ff764e443c5c447b4e16a1eb22d2d93fa` |
| `a77f7a52-983f-4bb7-b316-7df927ca80c9.bin` | 10,646 | Text report describing a sandbox/network limitation and historical push recommendation | `0a94b9286bcd6763773a36428a9164b938cc9264` |
| `b341b83c-e7a8-416a-adce-d8e87d2ba370.bin` | 56,813 | Git bundle; base64-decoded prefix begins `# v2 git bundle` and names `refs/heads/main` | `e6ef0239a929b60a0936139a10d9a64cc60fd89e` |

The first three are text/document artifacts mislabeled with a binary extension; the fourth is a Git bundle. The historical diff exposes the first three text contents, while the fourth's header was identified via base64 content. The bundle's full contents, embedded commit graph, and relationship to current `main` have **not** yet been inspected.

**Risk note:** the Bash script contains historical push-oriented commands. It has not been executed. Do not run it without a separate line-by-line safety review. No files were deleted, renamed, or modified.

**Next bounded step:** inspect the Git bundle metadata/commit graph using a safe, byte-preserving method; then decide whether these artifacts should remain in the root, move to a clearly named archive, or be removed. Preserve traceability before any mutation.

## 3. Historical transcript

`chat-Decentralized Computing Network.txt` is 224,663 bytes; its path history reports a single introduction commit `78edaac61b` (“Add files via upload”, 2026-04-20). Inspection of its beginning and end confirms it is a historical conversation/document dump containing aspirational architecture proposals and a prior-session closeout. It is not evidence that those proposed components are implemented in the current runtime.

No transcript content was changed. Avoid treating old claims such as “Trust Layer + Network Abstraction = ready” as current implementation evidence without matching code/tests.

## 4. Authority and scope boundaries

- G-01 GS-01 run `39380809928` and GS-02 run `39380814995` remain bounded successful developer/CI checks; they do not establish full Graph conformance or approve DEC-007–DEC-013.
- Developer-side Docker use in CI is distinct from the shipped product. The end-user runtime must not require Docker, Kubernetes, Neo4j, or other test infrastructure.
- No runtime, protocol, trust model, or canonical ontology change was made.
- Tagology remains deferred/experimental; human approval boundaries remain unchanged.

## 5. Outcome

**CI snapshot: GREEN for the 15 listed runs on the audited HEAD.**  
**Repository hygiene audit: OPEN.** Three `.bin` files are text artifacts with misleading extensions; the fourth is a Git bundle whose internal graph remains uninspected. No destructive cleanup was performed.


## 6. Follow-up verification — 2026-10-22

After this checkpoint was committed, CI for documentation commit `376a95ba79795e35ec523792a324064128d9bd6a` completed. The 13 listed workflow runs are all `success`: Windows, Linux, Android APK, SES-032 E2E, SES-043 proof, SES-045 node, SES-011/023/024/025 contracts, Beta local execution, and two P2P Evidence Check runs. This confirms the bounded workflow set, not every possible test or runtime condition.

The Git bundle header contains only this advertised ref:

`f79f53af7ff99caa06deda8cc2fa1b8d247f5f29 refs/heads/main`

A direct lookup of that commit in the current repository API returned `No commit found for SHA`. Therefore the bundle appears to reference history not directly addressable as a commit in the current repository. Its embedded object graph has not been unpacked or validated; do not assume it is a backup of current `main` or restore it over the repository.

No source/runtime files were changed. No binary artifact was deleted or executed.


## 7. Safety review of the archived Bash script

A static review of the script's GitHub commit diff found a fallback instruction that places a Personal Access Token directly in the Git remote URL (`https://[PAT]@github.com/...`). This is unsafe practice because credentials can persist in Git configuration and may be exposed through logs or command history. The script was **not executed**, and no token was found or tested by this inspection.

Recommendation: retain the artifact for traceability for now, but clearly treat it as historical/untrusted and never run it as-is. If a future archive cleanup is approved, move it to a clearly labelled historical-artifacts area and preserve its original commit/blob identity.
