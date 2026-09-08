# Original verifier snapshots

These two files preserve the exact PR105 verifier bodies before the F01 typed-payload repair. They are historical source evidence, not the active replay entrypoints.

Source PR105: `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`.

| Snapshot | Original Git blob |
|---|---|
| [Critical-tail verifier](X-ATT-001-critical-tails/verify.py) | `38588f83e8dd1a234e753bcd8fb8bd3f7d6e6902` |
| [Expanding-word verifier](X-ATT-003-expanding-word-rank/verify.py) | `760b5ade36c9927dfeea96cbbaafac08a99b07de` |

Use the active files under `experiments/` for current replay. The [integration candidate record](../../reports/integration-2026-09-08/README.md) describes the exact repair, fresh execution and remaining review gates. All source proof bodies and canonical artifacts are unchanged; no original reviewer receipt is rewritten.
