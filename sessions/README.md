# Session Records

`/sessions/` is the project's engineering history and evidence trail.

## Purpose

Session records preserve:

- why a change was made,
- which GAP was identified,
- what was changed,
- how it was verified,
- what checkpoint was created.

They are **history/evidence**, not the primary definition of the current architecture.

## Current session pattern

Recent sessions use some combination of:

- `*_BOOTSTRAP.md` — opening state and scope,
- `*_CHECKPOINT*.md` — intermediate evidence,
- `*_CLOSEOUT.md` or `STONE.md` — completed checkpoint,
- `test_*.py` — executable regression proof.

Older sessions contain additional naming conventions. They are historical records and should not be mechanically rewritten just to make filenames uniform.

## Canonical current state

Use:

- `START_HERE.md`
- `docs/CURRENT_STATE.md`
- `docs/REPOSITORY_MAP.md`
- code and tests
- current CI/evidence

Then use the latest session closeout to understand the most recent completed change.

## Rule

Do not use an old session note as proof of the current runtime if newer code or CI contradicts it.

Historical records remain valuable because they show the reasoning and evidence chain that led to the current state.
