# Verification of the actual-certificate and ordered-gap packet

**PASS.** The complete execution used clean detached science commit `7cbc58c754a2a2653a21e9cebe8654099132fe5f`, tree `a71c91f5778d5c554416f2564f219a938782a745`, with 839 tracked files. The nine project modules were rebuilt in a new empty object directory. The replay began at the timestamp recorded in the receipt and its repository validation finished at 08:09:52 UTC on 2026-11-25. The checkout and its 18 source-manifest entries were unchanged at completion.

| Executed check | Observed result |
| --- | --- |
| Six new Lean modules | Exit 0, warnings treated as errors, automatic implicit variables disabled; all 53 public declarations audited |
| Three exact local dependency modules | Freshly rebuilt; all 37 public declarations audited |
| Transitive axiom inspection | All 90 reports contain only `propext`, `Classical.choice`, and `Quot.sound`, or no axioms |
| Both Python control scripts, ordinary and optimized | Four successful executions; both pairs have byte-identical output and no Python assertion nodes |
| Complete-checkout repository validator with `--regressions` | Exit 0; all 11 child commands passed |
| Checkout and source hashes after execution | Clean; same commit and tree; all 18 manifest entries match |

The 53 declarations include the 19 in the two scoped intake copies. They are not 53 new theorems claiming convergence. The written rational existence construction, external logarithm estimate and asymptotic cycle consequences are independently reviewed written mathematics, not covered by the kernel count. The controls check the literal two rank-one progression representatives, the exact numerical cost comparison at 1600, and the rational cycle examples at odd periods 41 and 306.

[Full replay receipt](fresh_replay/receipt.json) · [Repository receipt](fresh_replay/repository-validation.json)

## Reproduce the execution

The schedule rebuilds three exact project dependencies and all six new modules, then audits every public theorem, runs both finite-control scripts in ordinary and optimized Python, and invokes the repository validator with its bounded regressions. The output directory must be outside the checkout and must not already exist. The reused external dependencies are Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`; all nine project objects are freshly generated.

```bash
python -X utf8 -B reports/astra-ultra-closure-20261125/replay.py \
  --lean /path/to/pinned/toolchain/bin/lean \
  --mathlib /path/to/pinned/mathlib4 \
  --leanpath-file /path/to/dependency-lean-path.txt \
  --output /path/outside/checkout/new-replay-directory
```

The dependency search-path file contains the absolute Mathlib and package object directories separated by the platform path separator. The driver prepends a fresh directory for the project modules. It does not reuse project objects from another checkout. A final receipt-only commit adds these outcomes without changing the science. The PR description records the final publication head and its separate complete-checkout checks; this immutable report identifies the science execution above.

[Replay driver](replay.py) · [Root mathematical review](ROOT_REVIEW.md) · [Independent core/cycle/intake review](core-review.md) · [Independent core review](bridge-review.md) · [Independent bridge review](cycle/BRIDGE_REVIEW.md)
