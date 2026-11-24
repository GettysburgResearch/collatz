# Execution record

Exact rational controls executed in the available JavaScript V8 environment, before commit. The same control function is in `controls.js`; execute with `node controls.js`. All checks completed without exceptions.

```json
{
  "telescope": 93,
  "substitution": 13860,
  "regularity": 924,
  "ratio": 924,
  "physical": 2044,
  "expanding": 19
}
```

- Lean/Lake: not available in the local execution environment (`command -v lean`, `command -v lake` yielded no paths). `MahlerCore.lean` is uncompiled proposed source, not kernel verification. To replay: `lake env lean -DwarningAsError=true research/mahler-physical-scripts-20261124/MahlerCore.lean` in a Mathlib-enabled Lean environment consistent with PR182. The full transcendence proof remains written mathematics.
- Full repository validator: NOT RUN (local checkout unavailable; git ls-remote failed to resolve GitHub). Connector writes and remote readback are distinct from repository validation.
- Evidence levels: exact finite arithmetic checks and proposed written theorem; no independent review or historical novelty assertion.
