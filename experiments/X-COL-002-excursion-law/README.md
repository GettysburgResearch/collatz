# X-COL-002: excursion law and the 3x - 1 control

Supports [`research/collatz-exploration-log`](../../research/collatz-exploration-log/README.md).

| File | What it does |
|---|---|
| `excursion.py` | For random odd `y` near `2^31` and `2^41`, counts odd iterates in `[r y, 2 r y)` and compares with `1/(2 m' r)`, `m' = log 3 - (4/3) log 2`; also `r P(max >= r)`. About 5 s for 100000 samples. |
| `minus_one.py` | For the map `(3y-1)/2^a`, the shares of the three known basins by dyadic scale and by residue mod 9. About 2 s for `X = 2000000`. |
| `results_excursion.json`, `results_minus_one.json` | Outputs. |

```bash
python3 excursion.py 100000
```

```bash
python3 minus_one.py 2000000
```

Limits: finite samples and ranges; statistical agreement, not proof.
