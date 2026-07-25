# X-6181 — criticality of the mx+1 family, and validation on real cycles

```text
Experiment ID:   X-6181
Agent:           claude-opus5-61
Claims:          T-6181 (criticality), validation of T-6140/T-6141 cycle machinery
Serves:          issue #26 (drift isolation at 5x+1)
Environment:     Python 3.11 (fractions only)
Runtime:         ~30 s
```

## Why

Two things this repository cannot do with `3x+1` alone:

1. **Falsify the dimension framework.** T-6131 explains why divergence is hard to find for
   `3x+1`. If that explanation were vacuous it would say the same about `5x+1`, where
   divergence is easy to find. `criticality.py` checks it does not.
2. **Test the cycle machinery against a real cycle.** No positive `3x+1` cycle is known, so
   T-6140/T-6141 have nothing to be checked against inside the problem. `cycle_validate.py`
   tests them on the three negative `3x+1` cycles and the three known `5x+1` cycles.

## Commands

```sh
python3 criticality.py      > results/criticality.txt
python3 cycle_validate.py   > results/cycle_validation.txt
```

## Results

**Criticality.** `alpha_m = log2/log m` versus the typical density `1/2` splits the family at
`m = 4`:

```text
 m   alpha_m        regime   dim D_m    codim   drift/step
 3   0.63093   SUBcritical  0.949956  0.050044    -0.14384
 5   0.43068 SUPERcritical  1 (full)  0           +0.11157
 7   0.35621 SUPERcritical  1 (full)  0           +0.27981
```

`m = 3` is the only odd multiplier in `2 < m < 4`, and sits `0.050044` into it out of `1`.

**The two predictions, tested on the first 20000 integers** ("exceeds `10^30` in 3000 steps"):

```text
m = 3 :     0 / 20000 =  0.00%   predicted ~0%     CONFIRMED
m = 5 : 18879 / 20000 = 94.39%   predicted ~100%   CONFIRMED
```

The `5.6%` shortfall at `m = 5` is the basins of its three small cycles; "measure 1" is
asymptotic in `Z_2` and does not claim every integer diverges.

**Cycle machinery, six real cycles, two maps, all exact:**

| map | cycle start | `q` | `k` | `2^q - m^k` | `x_w = c_w/(2^q-m^k)` |
|---|---:|---:|---:|---:|---:|
| 3x+1 | `-1` | 1 | 1 | `-1` | `-1` |
| 3x+1 | `-5` | 3 | 2 | `-1` | `-5` |
| 3x+1 | `-17` | 11 | 7 | `-139` | `-17` |
| 5x+1 | `1` | 5 | 2 | `7` | `1` |
| 5x+1 | `13` | 7 | 3 | `3` | `13` |
| 5x+1 | `17` | 7 | 3 | `3` | `17` |

The identity `prod (m + 1/n_i) = 2^q` holds exactly in all six, and **the sign of `2^q - m^k`
tracks the sign of the cycle in every case**, as T-6141(a) requires.

Incidental: `2^11 - 3^7 = -139` is the denominator of the `-17` cycle — the same `139` that
appears in the brief's H-subsystem ghost `g_3 = -2048/139`.

## Limitations

* The empirical percentages are evidence for the measure statements, not proof; measure 1 in
  `Z_2` implies nothing about any particular integer (the same gap as C-6111, reversed).
* The `m = 5` run uses a fixed cap and step budget; orbits classified as "diverges" are those
  exceeding `10^30` within 3000 steps, not proved divergent.
