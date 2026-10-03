# SES-080 — CHECKPOINT 01

**Data:** 2026-10-03
**Status:** CHANGE APPLIED / GREEN VERIFICATION PENDING
**GAP:** GAP-080-01 — release assets were not bound to the tagged commit

## INSPECT
The tag-triggered `.github/workflows/p2p-release.yml` resolved the latest successful Linux, Windows and Android builds from `main`. A release tag therefore could package artifacts produced by a different commit than the tagged source.

## RED / Difference
The documented release boundary is the version tag, but the artifact selection boundary was the latest successful build on `main`. These are not equivalent.

## Minimal change
Commit `8b15db7ddbe81a3528ac55479514c018f9ac327e` changes all three build-run lookups from `--branch main` to `--commit ${GITHUB_SHA}`.

The release workflow now requires successful Linux, Windows and Android builds associated with the exact tagged commit. If such a build does not exist, the release job stops instead of silently mixing versions.

No runtime, protocol, identity or Mini Node code was changed.

## Verification boundary
The repository confirms the exact three-line workflow change. CI execution for commit `8b15db7ddbe81a3528ac55479514c018f9ac327e` must complete successfully before this checkpoint is declared GREEN.

A real versioned release remains a separate evidence step and is not claimed here.

## Principle preserved
**Tag = release boundary. Commit = artifact identity.**

Do not publish a release from artifacts belonging to another source revision.
