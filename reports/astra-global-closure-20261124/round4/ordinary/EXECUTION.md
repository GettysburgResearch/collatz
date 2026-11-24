# Ordinary prefix counts and independent checks

Both modules compiled separately from source with Lean 4.34.1, `-j1 -DwarningAsError=true`, Lean commit `5045d0056413266e57c625dcd7c365b10e377c52`, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The runs used the provisioned Mathlib/package build cache and `/tmp/collatz-ff0fa7-leanlib` for the compiler shared library. These modules import Mathlib and no other project module. Both final builds exited zero. The six and four printed theorem inventories respectively contain only `propext`, `Classical.choice` and `Quot.sound`. [TruncatedDivisors.log](TruncatedDivisors.log) · [DyadicCutoff.log](DyadicCutoff.log)

| Compiled source or replay file | SHA-256 |
|---|---|
| `research/astra-global-closure-20261124/round4/ordinary/TruncatedDivisors.lean` | `5c54cf54e9e11c0cd359991d7bf669b25fd43e889a28a713c19b38ad61f04d60` |
| `research/astra-global-closure-20261124/round4/ordinary/DyadicCutoff.lean` | `e124f4a3175be41a0ce3c90518399be8e15198928ec0609d2663678d1da207e8` |
| `research/astra-global-closure-20261124/round4/ordinary/check.py` | `76ad163fd2b5b1dae838c6769985583aee135fd3f4472854acac5c0465515bf4` |

`python -B research/astra-global-closure-20261124/round4/ordinary/check.py` and the same command with `-O -B` both exited zero on Python 3.12.14. Their counters agreed. The arithmetic checks use explicit failure exceptions, which stay enabled under optimization. They tested 6,102 translated divisor intervals with 11,758 first-crossing factor codes, 60 physical maximal inequalities on whole translated binary periods, and 12,288 original-source probes across 24 window configurations. Of these repeated probes, 528 had a covered row; 86 had one in the short-clock, bounded-multiplier portion. The translations include (3^{80}+17). Each finite test class checks the inequality stated for that class, with no inferred all-time realization. [controls.json](controls.json)

The shifted divisor and finite Rankin inequalities, physical row widths and the finite binary first-passage mechanism are formally proved. The asymptotic prime split and entropy estimates, their assembly, and fixed-basin and common-endpoint consequences are written proofs. The Krasikov–Lagarias computer-aided predecessor input and PR193 synchronized image count were inspected as stated and used only for their named corollaries. The packet contains no generator or assertion of a nonconvergent trajectory. [Scientific note](../../../../research/astra-global-closure-20261124/round4/ordinary/README.md)
