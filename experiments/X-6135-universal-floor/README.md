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
| `results/` | raw scan output and the derived analysis |

## Commands

```sh
gcc -O2 -o floor floor.c -lm
./floor 200000000 > results/floor.txt     # ~8 min
python3 analyse.py results/floor.txt
```

## Results

See `results/analysis.txt`. Headline findings:

* `mu_L` grows geometrically with measured local slope close to the predicted codimension
  `1 - H_2(alpha) = 0.05004`, approaching it from above exactly as the `O(log L / L)` Chernoff
  correction predicts. The exact binomial tail `1/p_L` has slope `0.05373` over
  `L in [120, 229]`, and the measured `mu_L` slope is `0.06115` over the same range.
* `mu_L` exceeds `1/p_L` by a slowly growing factor (about 30-130 in that range). This is the
  expected behaviour of a minimum over *correlated* trials: `mu_L` is a step function that
  changes value rarely, since one good `x` serves many consecutive depths.
* **`mu_L = 27` for every `L` in `[20, 79]`.** The classical small integer with an unusually
  high trajectory is literally the universal floor across 60 consecutive depths.

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
demands `m_16 ≈ 2^261`, while the universal floor at the same depth is around `2^25`.

**This does not make any architecture wrong; it makes the depth of its finite survivors
uninformative.** By T-6131(e) the reachable depth is fully determined by the architecture's
dimension, so observing deep finite survivors measures the chart, not the conjecture.

## Limitations

* `mu_L` is exact only up to the scan bound; beyond it the table reports the inequality.
* The measured slope is still `~20%` above the asymptotic value at `L ~ 230`; the convergence
  is `O(log L / L)` and would need much deeper scans to be tight. The exact binomial slope is
  computed alongside precisely so that this finite-size effect is visible rather than hidden.
* Nothing here bears on the cycle lane: cycles are bounded orbits and are not in `D`.
