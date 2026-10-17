# X-8002 — distributed three- and four-pulse scans

This exact standard-library search continues the negative-cycle offense beyond
`L-8001`'s two-pulse theorem.

For each raw pulse set, cyclic rotation puts one pulse at index zero.  The
script then scans every later position set and every positive composition of
the total pulse at the minimal multiplier threshold and the next three totals.

Frozen scopes:

| family | pulses | repetitions | exact candidates | nontrivial hits |
|:---|---:|---:|---:|---:|
| negative 3-cycle | 3 | `r<=50` | 17,045,448 | 0 |
| negative 3-cycle | 4 | `r<=20` | 2,298,920 | 0 |
| negative 11-cycle | 3 | `r<=20` | 4,396,770 | 0 |
| negative 11-cycle | 4 | `r<=8` | 451,822 | 0 |

Total:

```text
24,192,960 exact candidates
0 nontrivial cycles
```

The two hits are the expected trivial `n=1` all-`2` words at three and four
negative-three-cycle repetitions.

```text
results SHA-256:
722890b0566d266126601a3a2193ec69e6b1ec296607d94a086c8d196479f0ff
```

Replay:

```bash
python3 -B run.py --check-results results/canonical.json
```
