# SES-078 — DISTRIBUTION CHECKPOINT

**Project:** P2P 60-24 OneClick Evo Positiv  
**Status:** IMPLEMENTED / VERIFICATION PENDING  
**GAP:** GAP-078-01 — no permanent public release path

## Observed

Linux, Windows and Android builds are produced as GitHub Actions artifacts. These artifacts are temporary and retained according to the Actions retention policy. README explicitly treated a permanent release asset as a separate distribution decision.

## Difference

The runtime can already be built and independently executed, but a new user does not yet have one stable public release page from which the current platform packages can be downloaded.

For the intended progression toward two independent users, this is now a concrete distribution bottleneck.

## Minimal repair

Added:

`.github/workflows/p2p-release.yml`

A tag `v*` now defines the release boundary. The workflow:

1. resolves the latest successful Linux, Windows and Android P2P build runs;
2. downloads their verified artifacts;
3. packages platform downloads;
4. creates a GitHub Release with the three assets.

No P2P runtime or protocol code was changed.

## Evidence boundary

This commit proves only that the release mechanism has been added to the repository. A real release is not claimed until a version tag executes the workflow successfully and the three release assets are verified.

## Next verification

Create/execute the first versioned release tag and verify:

- Linux asset present and runnable;
- Windows asset present with launcher files;
- Android APK package present;
- release page is stable and publicly navigable.

