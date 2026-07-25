```text
Claim ID:            T-6181
Title:               Criticality of the mx+1 family: 3x+1 is the unique odd subcritical
                     multiplier, and it is subcritical by only 0.050044
Status:              PROVED (the dichotomy); the empirical confirmations are EMPIRICAL
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        T-6131 (same proof, applied at a general multiplier)
Scope:               the family T_m(n) = (mn+1)/2 for odd n, n/2 for even n, m odd >= 3
Serves:              issue #26 (drift isolation at 5x+1)
Experiment:          experiments/X-6181-mx1-criticality/
```

## Statement

Let `m >= 3` be odd, `T_m(n) = (mn+1)/2` for odd `n` and `n/2` for even `n`, and

```text
alpha_m = log 2 / log m ,       D_m = { x in Z_2 : liminf_L k_L(x)/L >= alpha_m }.
```

**(a)** Every unbounded `T_m`-trajectory of a positive integer lies in `D_m`.

**(b) Dichotomy.**

```text
m < 4  (i.e. m = 3)  :  alpha_m > 1/2,  Haar(D_m) = 0,  dim_H(D_m) = H_2(alpha_m) < 1.
m > 4  (i.e. m >= 5) :  alpha_m < 1/2,  Haar(D_m) = 1,  dim_H(D_m) = 1.
```

The transition is at `m = 4`, where `alpha_4 = 1/2` exactly.

**(c) Numerically.**

| `m` | `alpha_m` | regime | `dim D_m` | codimension | typical drift (nats/step) |
|---:|---:|---|---:|---:|---:|
| 3 | 0.63093 | **sub**critical | 0.949956 | **0.050044** | `-0.14384` |
| 5 | 0.43068 | **super**critical | 1 | 0 | `+0.11157` |
| 7 | 0.35621 | supercritical | 1 | 0 | `+0.27981` |
| 9 | 0.31546 | supercritical | 1 | 0 | `+0.40547` |
| 181 | 0.13334 | supercritical | 1 | 0 | `+1.90610` |

**(d)** `m = 3` is the **only odd multiplier in the subcritical range** `2 < m < 4`, and its
codimension is `0.050044` out of a possible `1`.

## Proof

**(a)** Verbatim T-6131(a) with `3` replaced by `m`: an unbounded trajectory is divergent
(otherwise a value repeats and the orbit is eventually periodic, hence bounded), and for
`n_j >= M` an odd step multiplies by at most `(m/2)(1 + 1/(mM))` while an even step multiplies
by `1/2`, so `n_L -> infinity` forces `liminf k_L/L >= log2/log(m(1+1/(mM)))`; let `M ->
infinity`. `QED`

**(b)** By L-6130 (the parity map is an isometry for **every** odd `m` — the Terras bijection
argument uses only that `m` is odd, so `Q_L : Z/2^L -> {0,1}^L` remains a bijection) it is
enough to work in symbol space with Bernoulli(1/2) measure. The digit frequency is `1/2`
almost surely, so

* if `alpha_m > 1/2` the constraint is a large deviation: measure `0`, and the covering plus
  Besicovitch-Eggleston argument of T-6131(c) gives dimension exactly `H_2(alpha_m)`;
* if `alpha_m < 1/2` the constraint is satisfied by almost every sequence (SLLN), so
  `Haar(D_m) = 1` and the dimension is `1`.

`alpha_m > 1/2 <=> log 2 / log m > 1/2 <=> log m < 2 log 2 <=> m < 4`. `QED`

**(c)** Direct evaluation; the drift column is the almost-sure log-growth per step,
`(1/2) log(m/2) + (1/2) log(1/2) = (1/2) log(m/4)`, which changes sign at `m = 4` in agreement
with (b). `QED`

**(d)** The odd integers `m >= 3` with `m < 4` are exactly `{3}`. `QED`

## Why this is worth having

**It is a falsifiable test of the whole T-6131 framework, and the framework passes.** The
dimension machinery was built to explain why divergence is hard to find for `3x+1`. If it were
merely a restatement of "we have not found one", it would say the same thing about `5x+1` —
where divergence is not hard to find at all. It does not: it predicts full measure there.

Measured (`criticality.py`, first 20000 integers, "exceeds `10^30` within 3000 steps"):

```text
m = 3 :     0 / 20000  =  0.00%   framework predicts ~0%    -> CONFIRMED
m = 5 : 18879 / 20000  = 94.39%   framework predicts ~100%  -> CONFIRMED
```

The `5.6%` shortfall at `m = 5` is the basins of the known small `5x+1` cycles
(`1 -> 3 -> 8 -> 4 -> 2`, and the cycles through `13` and `17`), which have positive density at
this scale; "measure 1" is an asymptotic statement in `Z_2`, not a claim that every integer
diverges.

**And it prices the difficulty of Collatz.** `3x+1` is subcritical by `0.050044` out of a
possible `1`: it is the only odd multiplier below the critical value `4`, and it is barely
below it. R-6171 shows the self-referential attack needs `0.584963` of codimension. So the
entire difficulty of the Collatz conjecture sits in a `0.050`-wide margin that the elementary
tools need `0.585` of.

## Adversarial tests

Independent validation of the cycle machinery of T-6140/T-6141 on cycles that **actually
exist** — none are known for positive `3x+1`, so this is the only way to test it against
reality (`cycle_validate.py`). For each, the generalised identity `prod (m + 1/n_i) = 2^q` and
the formula `x_w = c_w/(2^q - m^k)` are checked exactly:

| map | cycle | `q` | `k` | `2^q - m^k` | `x_w` | matches |
|---|---|---:|---:|---:|---:|---|
| 3x+1 | `-1` | 1 | 1 | `2-3 = -1` | `-1` | yes |
| 3x+1 | `-5, -7, -10` | 3 | 2 | `8-9 = -1` | `-5` | yes |
| 3x+1 | `-17, ..., -34` | 11 | 7 | `2048-2187 = -139` | `-17` | yes |
| 5x+1 | `1, 3, 8, 4, 2` | 5 | 2 | `32-25 = 7` | `1` | yes |
| 5x+1 | `13, 33, 83, ...` | 7 | 3 | `128-125 = 3` | `13` | yes |
| 5x+1 | `17, 43, 108, ...` | 7 | 3 | `128-125 = 3` | `17` | yes |

**The sign of `2^q - m^k` tracks the sign of the cycle in every case** — negative cycles have
`2^q < m^k`, positive cycles have `2^q > m^k` — exactly as T-6141(a) requires. Six real cycles
across two different maps, all exact.

Note `2^11 - 3^7 = -139`: the same `139` that appears in the brief's H-subsystem ghost
`g_3 = -2048/139`. It is the denominator of the `-17` cycle.

## Gap audit

* *Does (b) prove `5x+1` has divergent integer orbits?* **No.** Measure 1 in `Z_2` does not
  imply any particular integer diverges — the same gap as C-6111, in the opposite direction.
  The empirical table is evidence, not proof.
* *Does (a) cover `m` even?* No; `T_m` needs `m` odd for `(mn+1)/2` to be an integer at odd
  `n`. `m = 4` is a boundary value of the formula, not a member of the family.
* *Is the drift column an independent fact?* No — it is `(1/2)log(m/4)` and changes sign at the
  same place. It is included because it is the form in which the heuristic is usually stated,
  and its agreement with the dimension dichotomy is a consistency check, not new information.
* *Does L-6130 really hold for all odd `m`?* Yes: the parity of `T_m^j(n)` depends only on
  `n mod 2^(j+1)`, and the level-`L` map is injective because `m` is invertible mod `2^L`. The
  computation in `cycle_validate.py` exercises `m = 5` and finds the expected structure.

## Suggested next attack

Issue #26 asks to factor exclusions into drift-driven versus format-driven. (b) gives the
clean split: everything that depends only on `alpha_m` versus `1/2` is drift-driven and
transfers across the family with the codimension as its parameter; anything that does not
survive replacing `3` by `5` is format-driven. This is a cheap and decisive test to apply to
existing exclusion claims.
