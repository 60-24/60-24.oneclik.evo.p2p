# External Audits

External audits and analyses are treated as **control material and sources of hypotheses**, not as automatic project roadmaps.

## Review rule

`EXTERNAL AUDIT → CURRENT REPOSITORY → REAL GAP? → PRIORITY → RED → IMPLEMENT → GREEN`

Every useful observation should be checked against current repository state and runtime evidence before implementation.

## What to extract

- technical gaps and reproducible failure modes,
- security risks and trust/execution boundary issues,
- architectural blind spots,
- useful regression or runtime tests,
- future requirements that can be safely deferred,
- proposals that conflict with existing invariants.

## What to avoid

Do not implement an external proposal merely because it is sophisticated, popular, or extensively documented. Do not let external documentation create a documentation loop in which ontology/specification grows faster than verified functionality.

## Project principle

> Zewnętrzny audyt rozszerza zbiór hipotez. Repozytorium i rzeczywiste dowody wykonania decydują, co staje się prawdą projektu.

External audits should therefore be reviewed continuously as the project evolves.
