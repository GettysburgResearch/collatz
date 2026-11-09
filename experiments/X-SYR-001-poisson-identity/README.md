# X-SYR-001: Poisson identity for the Syracuse transfer operator

Evidence for [research/syracuse-poisson-identity](../../research/syracuse-poisson-identity/README.md).

| File | What it does | Arithmetic |
|---|---|---|
| `verify_exact.py` | Checks the operator identity, the energy recursion, the class sums and the `qx+1` variant at small levels | exact rationals, standard library |
| `results_exact.json` | its output | |
| `numerics.py` | Levels up to 13: energies, autocorrelations, singular values, Plancherel, tails, the character-basis kernel | binary64, numpy |
| `results_numerics_13.json` | its output | |
| `deep_levels.py` | Energies and autocorrelations to a deeper level | binary64, numpy |
| `results_deep.json` | recorded output of the deep run | |

```bash
python3 verify_exact.py
```

```bash
python3 numerics.py 13
```

The exact script proves nothing beyond the levels it enumerates. The numerical scripts are finite-level observations. The proofs are in the research note.
