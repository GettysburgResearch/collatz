# X-SYR-002: critical cascade structure of the Syracuse density

Supports [`research/syracuse-critical-cascade`](../../research/syracuse-critical-cascade/README.md).

| File | What it does |
|---|---|
| `verify_structure.py` | 22 checks, floating point at tolerance 1e-9 (S7 exact): cascade form and critical moments, singular value decomposition, flat Jacobi kernel, selection rule, pair-operator identity, renewal remainder bound, absence of resonances. About 1 s. |
| `results_structure.json` | Output of the above. |
| `fast_levels.py` | Level densities by the cascade recursion, with energies, odometer correlations (also truncated), tails and truncated second moments. |
| `results_levels_18.json` | Output of `python3 fast_levels.py 18 results_levels_18.json` (about 9 GB of memory, a few minutes). |

```bash
python3 verify_structure.py
```

```bash
python3 fast_levels.py 14 out.json
```

Limits: the checks are numerical confirmations at small levels, not proofs. The level data are double
precision; the odometer average is truncated after 30 terms (relative error below 1e-17).
