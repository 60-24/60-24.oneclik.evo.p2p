# SES-087 — CHECKPOINT 06: CONSTRAINT CLARIFICATION

**Date:** 2026-10-20  
**Status:** Documentation corrected; CI verification pending.

The no-Docker/no-Kubernetes constraint applies to the finished P2P product and the end-user installation/runtime experience: users must not need developer or test infrastructure to run it. It does not automatically prohibit Docker in isolated developer/CI evaluation of a future Graph candidate.

The temporary `if: false` guards in `.github/workflows/g01-neo4j-gs01.yml` and `.github/workflows/g01-neo4j-gs02.yml` have been removed. Read-back confirmed both are absent. These workflows are restored for developer-side evaluation; this does not claim that G-01 ran or that Neo4j passed conformance.

Updated:
- `docs/ARCHITECTURE_AUTHORITY_INDEX.md`
- `sessions/SES-087/SES-087_GAP_ASSESSMENT.md`
- `README.md`
- `START_HERE.md`

README and START HERE now identify SES-085 as the latest closed technical session and SES-087 as ongoing audit/documentation work.

DEC-007–DEC-013 retain their human-approval status. No runtime, transport, trust model or canonical ontology changed.

Remaining audit: verify CI for the newest commits and classify the root-level UUID-named binary files and historical transcript without moving or deleting anything absent evidence.
