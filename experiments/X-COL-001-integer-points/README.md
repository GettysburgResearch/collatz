# X-COL-001: Syracuse densities at integer points and Collatz hitting fractions

Supports [`research/collatz-integer-points`](../../research/collatz-integer-points/README.md).

| File | What it does |
|---|---|
| `hitting.py` | Part 1 checks the identity `f_n(x) = sum 3^n/2^s` over `n`-th Collatz predecessors by brute-force enumeration (`x` = 5, 23, 29; `n` = 1, 2, 3). Part 2 computes, for odd `N <= X`, the fraction of orbits passing through each target, compares it with the level-15 renewal prediction, and tabulates the generations of the tree of 23. About 10 s for `X = 2000000`. |
| `results_hitting.json` | Output for `X = 2000000`. |

```bash
python3 hitting.py 2000000
```

Limits: finite range, double precision; the renewal formula is a heuristic and the table shows where it fails at level 15. Nothing here is evidence for or against the conjecture beyond the range computed.
