# SES-075 — Windows Native P2P Enablement Checkpoint

**Project:** P2P 60-24 OneClick Evo Positiv  
**Branch:** main  
**Date:** 2026-09-30  
**Mode:** CONTROL → BUILD → EVIDENCE

## Finding

INSPECT confirmed that the concrete P2P runtime had a verified Linux executable path but no dedicated native Windows P2P executable workflow. This was an execution-environment gap for the planned Android → Windows test, not a protocol GAP.

## Minimal change

Added:

`.github/workflows/build-p2p-windows.yml`

The workflow:
- runs on `windows-latest`;
- installs the existing runtime dependencies;
- executes the existing P2P regression suite;
- builds `P2P60-24Node.exe` with PyInstaller;
- runs the packaged executable as Node B and Node A;
- verifies the application response and Node B message log;
- packages, attests and uploads `P2P60-24Node-windows-x86_64`.

No P2P protocol or architecture code was changed.

Updated:

`README.md`

with native Windows download/run instructions and the explicit boundary that CI does not prove Android → Windows LAN connectivity.

## Evidence

Commit:

`22fa01b5d84a23235df76ad46e46b0eb51752c2b`

Workflow run:

`36693797672`

Job:

`build-windows-p2p`

Result:

**SUCCESS**

Verified steps:
- regression tests — SUCCESS
- Windows executable build — SUCCESS
- packaged two-node smoke — SUCCESS
- artifact packaging — SUCCESS
- attestation — SUCCESS
- artifact upload — SUCCESS

Artifact:

`P2P60-24Node-windows-x86_64`

Artifact size:

11,875,962 bytes

## Interpretation

The native Windows executable boundary is now CI-proven.

This does **not** prove the real device path:

`Android → Wi-Fi/LAN → native Windows Node B`

That remains the next physical test.

No protocol GAP is opened by the previous WSL failure or by this checkpoint.

## Next controlled step

Run the real Windows native test:

`Windows Node B ← Wi-Fi/LAN ← Android Node A`

Collect observable evidence first. Modify P2P code only if that test produces a reproducible application-level failure.
