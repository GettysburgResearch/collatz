# Exact arithmetic check receipt

Command actually run in the complete original checkout:

```sh
python -X utf8 -B research/structural-reset-20261120/component/check_component_rigidity.py
```

It exited with code 0 and reported `PASS` for all 480 symbolic residue cells.
Every cell denotes all positive affine lifts, with the single base input 1
excluded from the strict-descent assertion. The largest certificate uses nine
primitive applications of laws (A)--(D). All certificates passed their exact
domain, divisibility, positivity, strict-descent and uniform-bound checks.

The cell counts were:

| Selector branch | Cells |
|---|---:|
| Remove factor 2 | 240 |
| Remove factor 3 | 80 |
| Remove factor 5 | 32 |
| Input 1 modulo 4 | 64 |
| Input 7 modulo 8 | 32 |
| Remaining input 3 modulo 5 | 8 |
| Remaining input 1 modulo 5 | 8 |
| Remaining input 4 modulo 5 | 8 |
| Reverse law (D) | 4 |
| Final auxiliary value even | 2 |
| Final auxiliary value 1 modulo 4 | 1 |
| Final auxiliary value 3 modulo 4 | 1 |

This is exact validation of the conditional arithmetic selector. It does not
establish the merger hypothesis (E), give ordinary merger clocks for it, or
prove unconditional Collatz convergence. The theorem's elementary derivation
and its ordinary-domain checks remain part of the written proof, not outputs
of this checker.
