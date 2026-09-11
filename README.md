# 60-24.oneclik.evo.p2p

System Builder carries an explicit human intent through a chain of verified boundaries —
`INTENT → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL → EXECUTION AUTHORIZATION → EXECUTION REQUEST → EXECUTION → RESULT → EFFECT → VERIFICATION → DELIVERY`
— where every step is a deterministic transformation that records its own provenance.
`DELIVERY` currently produces an internal, reproducible delivery manifest rather than transmission to an
external system, and the canonical runtime is the bounded `INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`
flow implemented in `src/runtime/`.

## Running the tests

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest
```

Test files in `sessions/` share some basenames, so the collective run relies on the pytest
configuration in `pyproject.toml`. Individual contracts can also be run on their own:

```bash
python3 -m pytest sessions/SES-011/test_build_plan_contract.py
```

## Repository layout

| path | contents |
| --- | --- |
| `src/runtime/` | canonical runtime: entry point, observation, flow |
| `sessions/` | boundary contracts, their tests and verification evidence |
| `docs/` | architectural direction and project history |
| `constitution/`, `ontology/`, `architecture/` | governance and modelling layers |
| `.github/workflows/` | per-contract CI verification |
