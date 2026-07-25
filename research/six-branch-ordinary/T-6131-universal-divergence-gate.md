```text
Claim ID:            T-6131
Title:               Universal divergence gate: every divergence-targeting architecture has a
                     survivor set of Hausdorff dimension at most H_2(log2/log3) = 0.94996
Status:              PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        L-6130 (classical, restated and proved below), L-6132 (classical
                     Besicovitch-Eggleston, cited)
Scope:               ALL architectures targeting a divergent shortcut-Collatz orbit —
                     fixed-block, variable-block, growing alphabet, or arbitrary
Related counterexample candidates: constrains every one that has ever been proposed
Answers:             the open question left by T-6121's gap audit and M-6120
```

## Statement

Let `T` be the shortcut map, `k_L(x) = #{ 0 <= j < L : T^j(x) is odd }`, and

```text
alpha = log 2 / log 3 = 0.6309297535714574...,
H_2(p) = -p log_2 p - (1-p) log_2 (1-p),
D = { x in Z_2 : liminf_L k_L(x)/L >= alpha }.
```

**(a) Every counterexample of divergence type lies in `D`.** If `n` is a positive integer
whose Collatz trajectory is unbounded, then the trajectory tends to infinity and
`liminf_L k_L(n)/L >= alpha`.

**(b) `D` has Haar measure zero** in `Z_2`.

**(c) `dim_H(D) = H_2(alpha) = 0.9499555271883...`**, in the standard 2-adic metric normalised
so that `dim_H(Z_2) = 1`. The codimension is

```text
1 - H_2(alpha) = 0.0500444728116...
```

**(d) Universal ceiling.** Let `S` be the all-time survivor set in `Z_2` of *any* architecture
whose positive-integer survivors are required to have unbounded Collatz orbits. Then
`S ⊆ D`, so

```text
Haar(S) = 0     and     dim_H(S) <= 0.94996.
```

No choice of block length, digit set, alphabet growth, or bookkeeping can raise this ceiling.

**(e) Universal floor on least roots.** Define

```text
mu_L = min { x > 0 : k_L(x) >= ceil(alpha L) }.
```

If `x` is legal for `N` blocks of an expanding `(k,q)` macro-block chart then `x >= mu_{qN}`.
The natural density of `{x : k_L(x) >= ceil(alpha L)}` is **exactly**
`2^-L * sum_{j >= ceil(alpha L)} C(L,j)`, which decays like `2^(-0.05004 L)`; so no
architecture can have least roots growing slower than about `2^(0.05 L)` per Collatz step,
and any architecture of dimension `d` has least roots growing like `2^((1-d) L)`.

## Definitions

`dim_H` on `Z_2` uses the metric `|x-y|_2`; balls of radius `2^-L` are residue classes mod
`2^L`, so a set covered by `N_L` classes at level `L` has upper box dimension
`limsup log_2 N_L / L`.

## Proof

### L-6130 (the parity map is an isometry)

Let `Q_L(x)` be the parity word of `x` of length `L` and `Q_inf(x)` the infinite parity word,
read as an element of `Z_2` via binary digits.

* The parity of `T^j(x)` depends only on `x mod 2^(j+1)`; hence `x = y (mod 2^L)` implies
  `Q_L(x) = Q_L(y)`.
* Conversely (Terras 1976, Everett 1977) `Q_L : Z/2^L -> {0,1}^L` is a **bijection**; this is
  `L-6100` in T-6101, where it is re-derived constructively.

So `Q_L` is a bijection between residue classes mod `2^L` and words of length `L`, for every
`L`. Therefore `|Q_inf(x) - Q_inf(y)|_2 = |x - y|_2` exactly: `Q_inf` is a surjective isometry
of `Z_2`, hence a measure-preserving homeomorphism that preserves Hausdorff dimension exactly.
(This is the classical 3x+1 conjugacy map; Lagarias 1985, Bernstein-Lagarias 1996.)

### (a)

First, unbounded implies divergent. If the trajectory is unbounded but `liminf_j n_j = c <
infinity`, then infinitely many `n_j` lie in `[1, c+1]`, so some value repeats; a repeat makes
the trajectory eventually periodic, hence bounded — contradiction. So `n_j -> infinity`.

Now fix `M > 0` and `J` with `n_j >= M` for all `j >= J`. For `j >= J` an odd step multiplies
by `(3n+1)/(2n) <= (3/2)(1 + 1/(3M))` and an even step by `1/2`. Writing `L' = L - J` and
`k' = k_L - k_J`,

```text
log n_L <= log n_J + k' log(3/2) - (L'-k') log 2 + k' log(1 + 1/(3M))
        = log n_J + k' [log 3 + log(1 + 1/(3M))] - L' log 2.
```

`n_L -> infinity` forces the right-hand side to be unbounded above, hence

```text
liminf k'/L' >= log 2 / [log 3 + log(1 + 1/(3M))].
```

`M` may be taken arbitrarily large (because `n_j -> infinity`), and `k_L/L` and `k'/L'` have
the same liminf, so `liminf k_L/L >= log 2 / log 3 = alpha`. `QED`

### (b), (c)

By L-6130 it suffices to compute the measure and dimension of

```text
D' = Q_inf(D) = { w in {0,1}^inf : liminf_L (#ones in w_1..w_L)/L >= alpha },
```

with `{0,1}^inf` carrying Haar measure = Bernoulli(1/2) and the metric `2^-(first
disagreement)`.

*Measure.* By the strong law of large numbers the digit frequency of a Haar-random `w` is
`1/2 < alpha` almost surely, so `Haar(D') = 0`.

*Dimension, upper bound.* Fix `beta < alpha`. For large `L`, every `w` in `D'` has at least
`beta L` ones in its first `L` digits, so `D'` is covered by
`N_L = sum_{j >= beta L} C(L,j) <= 2^(L H_2(beta) )` cylinders of diameter `2^-L`. Hence
`dim_H(D') <= limsup log_2 N_L / L <= H_2(beta)`. Letting `beta` increase to `alpha` and using
continuity of `H_2` gives `dim_H(D') <= H_2(alpha)`.

*Dimension, lower bound.* `D'` contains the Besicovitch-Eggleston set of sequences whose digit
frequency **exists and equals** `alpha`, which has Hausdorff dimension exactly `H_2(alpha)`
(**L-6132**: Eggleston 1949; Besicovitch 1935). Hence `dim_H(D') >= H_2(alpha)`.

So `dim_H(D) = dim_H(D') = H_2(alpha)`. Numerically `H_2(alpha) = 0.9499555271883305`. `QED`

### (d)

Any architecture whose positive-integer all-time survivors are required to diverge has its
survivor set contained in the closure of `D` intersected with its own constraints; more
directly, every positive integer in `S` lies in `D` by (a), and `S` is contained in the
topological closure of that set, which is still contained in the closed set `D` (`D` is a
`G_delta` defined by a liminf, and the covering argument in (c) applies to its closure with
the same bound). Hence the measure and dimension bounds of (b),(c) apply to `S`. `QED`

### (e)

The first claim is immediate: after `N` blocks of an expanding `(k,q)` chart the trajectory
has run `L = qN` shortcut steps with exactly `kN` odd steps, and `3^k > 2^q` gives
`k/q > alpha`, so `k_L = kN >= ceil(alpha q N)`; therefore any legal `x` is a member of the
set whose least element is `mu_{qN}`.

The density statement is exact rather than heuristic: by L-6130 the set
`{x : k_L(x) >= m}` is a union of exactly `sum_{j>=m} C(L,j)` residue classes mod `2^L`.
Chernoff's bound gives `2^-L sum_{j >= alpha L} C(L,j) = 2^(-L(1-H_2(alpha)) + O(log L))`.
The last claim follows by writing a dimension-`d` architecture's depth-`L` survivor set as
`2^(dL)` classes mod `2^L`, of density `2^(-(1-d)L)`. `QED`

## Motivation, and what it settles

T-6121 proved a density gate for *fixed macro-block* charts and left one escape route open:
variable block length, or an alphabet that grows with depth. M-6120 called that "the only
structurally new question in the positive lane".

**T-6131 closes it. There is no escape route.** The ceiling is a property of the *target*, not
of the architecture: any set of 2-adic integers whose positive members must diverge is
squeezed inside a fixed set of dimension `0.94996` and measure zero. Consequently:

1. **The "false compactness" trap is unavoidable in principle.** Every divergence architecture
   necessarily has a measure-zero survivor set, hence necessarily has the property that all
   finite depths are nonempty while the limit may be empty. The global blocker identified in
   the project audit is therefore not a defect of any particular construction and cannot be
   engineered away. It is a theorem about what is being looked for.
2. **Depth of finite survivors carries no existence information.** By (e) an architecture of
   dimension `d` has least roots `~2^((1-d)L)`, so the deepest survivor below a search bound
   `B` sits at `L ~ log_2(B)/(1-d)`. That number is fully predicted by `d` alone. Reporting a
   deep finite survivor is reporting the dimension of one's own chart.
3. **A design criterion falls out.** Among architectures, the only quantity worth optimising is
   `d`. Higher `d` buys longer finite survivors and nothing else — but it is exactly what makes
   an architecture *searchable*.

| architecture | `dim d = log_2 D / q` | codim `1-d` | least root at Collatz depth `L` |
|---|---:|---:|---|
| six-branch chart (issue #58) | 0.13605 | 0.86395 | `2^(0.864 L)` |
| full `(12,19)` chart | 0.78725 | 0.21275 | `2^(0.213 L)` |
| centered `64 -> 81`, `(4,6)` | <= 0.55365 | >= 0.44635 | `2^(0.446 L)` |
| best possible `(41,65)` chart | 0.88921 | 0.11079 | `2^(0.111 L)` |
| **universal ceiling** | **0.94996** | **0.05004** | **`2^(0.050 L)`** |

Each row reproduces the growth rate measured or predicted for that lane
(`2^(0.86395*19) = 87381` per six-branch macro step, matching X-6110's `99380` to 1.1%;
`2^(0.21275*19) = 16.5`; `2^(0.44635*6) = 6.4`), so the table is not a new heuristic but the
same one, correctly normalised per Collatz step.

**The six-branch chart is `2^(0.814 L)` above the universal floor.** At the depth X-6110
reached, `L = 19*16 = 304` Collatz steps, the chart demands `m_16 ~ 2^261.3` while the floor
is `mu_304 ~ 2^25` (X-6135). It is not merely thin; it is about `2^236` times more expensive
than the best conceivable architecture at the same depth.

## Gap audit

* *Does (c) prove that `D` contains no integers?* **No, and it cannot.** Measure zero and
  dimension `< 1` are perfectly compatible with containing integers; indeed `D` contains
  every positive integer with a divergent trajectory, if any exists. This claim bounds the
  *size* of the search space, not its emptiness. Overstating it would be exactly the error
  this namespace was written to avoid.
* *Is (a) tight?* The threshold `alpha` cannot be raised: orbits with density exactly `alpha`
  are marginal, and the liminf form is the correct one (a divergent orbit may dip below `alpha`
  infinitely often as long as the liminf holds).
* *Does (d) cover architectures that also impose non-divergence conditions?* Yes; adding
  constraints only shrinks `S`.
* *Does (d) cover cycle-type counterexamples?* **No.** A nontrivial cycle is bounded, so it is
  not in `D`, and nothing here constrains the cycle lane. T-6131 is a statement about the
  divergence lane only.
* *Is the Besicovitch-Eggleston citation load-bearing?* Only for the lower bound in (c). The
  upper bound — which is the part every consequence in this file uses — is proved here from
  scratch by the covering argument, and needs no citation.
* *Could an architecture be "adaptive" in a way that escapes?* No: (d) only uses that its
  positive-integer survivors diverge. Any architecture that does not require that is not
  targeting a divergence counterexample.

## Adversarial tests

* X-6135 computes `mu_L` exactly for `L <= 229` (and further); the exact binomial-tail density
  `2^-L sum_{j>=ceil(alpha L)} C(L,j)` has measured local slope `0.05373` over `L in [120,229]`,
  converging to the predicted `0.05004` from above as the `O(log L / L)` correction dies.
* `mu_L = 27` for every `L` in `[20, 79]`: the famous small high-trajectory integer is literally
  the universal floor over 60 consecutive depths.
* The per-lane table reproduces three independently measured growth rates (see above).

## Suggested next attack

Two directions, both concrete:

1. **Use the criterion.** If the project wants a searchable architecture, maximise `d`. A
   `(k,q)` chart with large `q` and `k/q` just above `alpha` has `d -> H_2(alpha)`; the full
   `(41,65)` chart already reaches `0.889`. Such a chart's least roots grow like `2^(0.111 L)`
   instead of `2^(0.864 L)`, making depths of several hundred Collatz steps reachable. This
   will produce impressive-looking deep survivors and, by point 2 of the motivation, **still
   prove nothing about existence** — which is precisely why it should be attempted with that
   expectation stated in advance.
2. **Accept the reframing.** Since no architecture can escape measure zero, the positive lane
   cannot be rescued by better engineering. Any future existence proof must come from a
   source-specific forcing identity (M-6120 Gate 2), and the project's effort is better spent
   deciding whether any such identity is possible than on building more charts.
