# SES-080 — CLOSEOUT

**Project:** P2P 60-24 OneClick Evo Positiv  
**Status:** CLOSED / STONE  
**Branch:** main

## GAP-080-01 — release artifact identity

### Finding

The tag-triggered release workflow selected the latest successful Linux, Windows and Android builds from `main`.

That did not guarantee that the release artifacts belonged to the exact tagged commit.

### Minimal correction

Commit `8b15db7ddbe81a3528ac55479514c018f9ac327e` changed all three release artifact lookups from branch-based selection to exact commit selection using:

```
--commit ${GITHUB_SHA}
```

The release boundary is therefore:

**tag → exact commit → successful builds for that commit → release artifacts**

### Verification

P2P evidence workflow for the corrected implementation:

- commit: `8b15db7ddbe81a3528ac55479514c018f9ac327e`
- evidence run: `37147128617`
- result: SUCCESS

The release workflow itself remains tag-triggered. A real public release is a separate distribution event and is not claimed merely because the workflow exists.

## Scope control

No protocol, identity, transport or ontology change was introduced.

No speculative distribution infrastructure was added.

## Conclusion

GAP-080-01 is closed.

**SES-080 = STONE.**
