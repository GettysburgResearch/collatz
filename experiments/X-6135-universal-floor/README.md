# X-6135 — the universal floor `mu_L`

```text
Experiment ID:   X-6135
Agent:           claude-opus5-61
Issue:           #58 (follow-on); answers the open question in T-6121 / M-6120
Claims:          T-6131 (universal divergence gate), T-6121, M-6120, X-6110
Environment:     Linux 6.18.5 x86_64, gcc 12 (-O2), Python 3.11, 4 cores
Randomness:      none (fully deterministic exhaustive scan)
```

## Research question

T-6131(e) defines

```text
mu_L = min { x > 0 : the first L shortcut-Collatz steps of x contain
                     at least ceil(L * log2/log3) odd steps }.
```

`mu_L` lower-bounds the least root of **every** divergence-targeting architecture at Collatz
depth `L` — no architecture, however cleverly its blocks are chosen, can have a survivor
smaller than `mu_L`. Two questions:

1. Does `mu_L` grow at the rate `2^((1-H_2(alpha)) L) = 2^(0.05004 L)` that T-6131 predicts?
2. How far above this floor do the project's actual architectures sit?

## Method

Exhaustive scan of `x = 1, 2, 3, ...` in increasing order. For each `x` the shortcut orbit is
run for up to `LMAX = 900` steps with a running count of odd steps; the first `x` that reaches
`k_L >= ceil(alpha L)` is recorded as `mu_L`. Because `x` is scanned in increasing order, the
first hit *is* the minimum, so every reported `mu_L` is exact. Arithmetic is `unsigned
__int128` with an explicit overflow abort (never triggered in the published run).

`mu_L` is reported only for `L` where the scan bound was sufficient; the first `L` with no hit
gives the certified inequality `mu_L > XMAX` and the table stops there.

The comparison quantity is the **exact** density

```text
p_L = 2^-L * sum_{j >= ceil(alpha L)} C(L, j),
```

which by L-6130 (the parity map is an isometry, so `k_L` depends only on `x mod 2^L` and every
word occurs exactly once) is not a heuristic but the true natural density of the depth-`L`
condition. If the classes were equidistributed one would expect `mu_L ~ 1/p_L`.

## Contents

| file | purpose |
|---|---|
| `floor.c` | the exhaustive scan |
| `analyse.py` | slopes, exact binomial tail, floor-vs-architecture comparison |
| `isometry.py` | adversarial test of L-6130: the parity map is an isometry of `Z_2` |
| `best_charts.py` | `dim(q)` for the best chart at each block length; refutes the convergent guess |
| `results/` | raw scan output and the derived analysis |

## Commands

```sh
gcc -O2 -o floor floor.c -lm
./floor 200000000 > results/floor.txt     # ~11 min
python3 analyse.py results/floor.txt
```

## Results

Scan of every `x <= 2 * 10^8`. `mu_L` is exact for `L <= 420`; `mu_421 > 2 * 10^8`.
Full output in `results/floor.txt`, analysis in `results/analysis.txt`.

```text
mu_35  = 27           mu_210 = 665215        mu_420 = 169941673  (~2^27.3)
mu_105 = 2919         mu_315 = 8400511
```

* **The floor tracks the exact density.** The right test is the product `mu_L * p_L`, where
  `p_L = 2^-L sum_{j>=ceil(alpha L)} C(L,j)` is the *exact* natural density (L-6130 makes this
  a count, not an estimate). Over `L in [30, 420]` that product stays in `[0.41, 171.7]`, with
  mean `41.0` over the first half of the range and `34.8` over the second — **bounded, with no
  systematic growth**. So `mu_L ~ 1/p_L` up to a bounded factor.
* **The density has the predicted slope.** `d log2(1/p_L)/dL = 0.05215` over `L in [210,420]`,
  converging from above to the predicted codimension `1 - H_2(alpha) = 0.05004`.
* **Do not regress on `mu_L` directly.** It is a step function with long plateaus, so a local
  slope estimate is dominated by where the window starts and ends: over `L in [210,420]` it
  reads `0.03237`, while over the whole range `log2(mu_L)/L = 0.06510`. Both are artefacts of
  the plateaus, which is why the ratio test above is the published comparison.
* **The plateaus are the interesting object.** `mu_L = 27` for every `L` in `[20, 79]`
  (60 depths) and `mu_L = 63728127` for every `L` in `[330, 418]` (73 depths). The classical
  small integers with unusually long high trajectories are literally the universal floor over
  long stretches of depth.

## Operational ceiling: how deep can anything go?

`max{L : mu_L <= X}` is the deepest above-threshold confinement any integer below `X` achieves
— the ceiling on every divergence architecture at once:

| `X` | deepest `L` | local exponent `log2(mu_L)/L` |
|---|---:|---:|
| `2^10` | 90 | 0.1085 |
| `2^15` | 133 | 0.1127 |
| `2^20` | 217 | 0.0891 |
| `2^25` | 329 | 0.0727 |
| `2^27.3` | 420 (scan-limited) | 0.0651 |

The local exponent drifts down toward the asymptotic `0.05004` (not monotonically at small
`L`, since `mu_L` is a step function). Extrapolating to `X = 2^64` gives between `983` steps
(current local exponent) and `1279` (asymptotic) — **both are extrapolations** and are labelled
as such; the certified statement is only the table above.

## Interpretation

The floor is *low*. Growth of `2^(0.05 L)` means that, in principle, an optimally designed
architecture could exhibit survivors of several hundred Collatz steps starting from numbers of
only a few dozen bits. Every architecture in this project sits far above that floor:

| architecture | codim `1-d` | least root at `L` | ratio to floor |
|---|---:|---|---|
| six-branch (issue #58) | 0.86395 | `2^(0.864 L)` | `2^(0.814 L)` |
| full `(12,19)` | 0.21275 | `2^(0.213 L)` | `2^(0.163 L)` |
| `64 -> 81`, `(4,6)` | 0.44635 | `2^(0.446 L)` | `2^(0.396 L)` |

At the depth X-6110 actually reached — `L = 19*16 = 304` Collatz steps — the six-branch chart
demands `m_16 = 2^261.3`, while the universal floor at the same depth is about `2^23.6`: a
ratio of `2^238`. At `L = 152` and `L = 228` the ratios are `2^108` and `2^175`.

**This does not make any architecture wrong; it makes the depth of its finite survivors
uninformative.** By T-6131(e) the reachable depth is fully determined by the architecture's
dimension, so observing deep finite survivors measures the chart, not the conjecture.

## Limitations

* `mu_L` is exact only up to `L = 420` (scan bound `2 * 10^8`); beyond that the table reports
  the inequality `mu_421 > 2 * 10^8`.
* The exact-density slope is still `4%` above its asymptotic value at `L ~ 420`; convergence is
  `O(log L / L)`. This is reported rather than hidden.
* The bounded-ratio finding is empirical over the computed range, not a theorem: nothing here
  proves `mu_L * p_L` stays bounded for all `L`.
* Nothing here bears on the cycle lane: cycles are bounded orbits and are not in `D`.
