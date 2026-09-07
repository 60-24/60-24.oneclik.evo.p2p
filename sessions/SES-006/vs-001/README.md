# VS-001 — Local Execution

## Purpose

Minimal deterministic implementation of:

`Intent → Specification → Verification → Delivery`

## Run

From this directory:

```text
python3 run_vs001.py --output ./vs-001-output
python3 -m unittest test_vs001.py
```

The builder uses only the Python standard library. It does not access the network or execute shell commands.

## Outputs

A successful run creates:

- `specification.json`
- `specification.md`
- `verification.json`
- `delivery-manifest.json`

Delivery is marked `DELIVERED` only when verification is `PASS`.
