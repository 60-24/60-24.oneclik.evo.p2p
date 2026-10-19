# Tagologia S — isolated contract experiment

**Status:** experimental; local-only; not a canonical schema or P2P protocol.

This folder tests one narrow question: can a small typed contract reject missing or unsupported input without guessing?

## Run

From the repository root:

```bash
python -m unittest discover -s experiments/tagologia_s -p 'test_*.py' -v
```

Uses only the Python standard library.

## Scope

- Validates a small `resource.request` envelope.
- Rejects missing required fields/references, unsupported schema/version/kind, unsupported operations, wrong types, and unknown top-level fields.
- Produces deterministic JSON after validation.

## Explicit non-goals / known limits

- Does not implement Tagologia H or the H↔S bridge.
- Does not validate timestamps or a full formal JSON Schema.
- Does not establish that a resource exists, that a sender is authentic, that a request is true, or that an operation is authorized.
- Does not calculate trust, call the network, or change the P2P runtime.
- Does not define compatibility policy for a production contract.

A passing test means only that this isolated prototype behaves as its tests specify. It is not evidence of production readiness or of improved human comprehension. Human-layer and bridge fixtures remain separate acceptance gates.
