```text
Claim ID:            T-6244
Title:               The cycle bound and the chi = sigma bound are the same inequality; the
                     period of a positive cycle is confined to six values below 2*10^12
Status:              PROVED (the identification and the L0 structure);
                     the numerical candidate set is CONDITIONAL on an enumeration (see gaps)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-27
Last updated:        2026-07-27
Dependencies:        T-6141(a),(b); T-6242(a); T-6243(a); the verification bound B (an INPUT)
Scope:               positive cycles of the shortcut Collatz map
Experiment:          experiments/X-6150-cycle-convergents/cycle_bmax_floor.py
```

## Statement

**(a) The two lanes carry the same inequality.** T-6141(b) bounds a positive cycle's minimum by

```text
        m  <=  k * 2^q / ( 3 * (2^q - 3^k) ) ,
```

and T-6243's proof, at the point before the sharp term bound is applied, gives for a
counterexample to `chi = sigma`

```text
        n  <   k * 2^j / ( 3 * (2^j - 3^k) ) .
```

These are the *same formula*, with `(q, k, m)` and `(j, k, n)` interchanged. T-6141(b) is
exactly T-6243(a) with `G(k)` relaxed to its trivial bound `k`; the exact version carries
`G(k) = sum_{m<k} 2^(-theta_m) ~ 0.7213475 k`, so **the cycle bound has a factor `1.386` of
slack in it** that T-6243 identifies and removes.

**(b) A cycle's orbit is above the line up to an explicit first drop.** Let a positive cycle
have minimum `m`, period `q`, and `k` odd elements. Let `L0` be the least `L >= 1` with
`3^(k_L) < 2^L`. Then `L0` exists, `L0 <= q`, the orbit word of `m` is above the line at every
`L < L0`, and

```text
        m  <=  Bmax(L0)        with Bmax the exact quantity of T-6243(a).
```

So a cycle minimum is an instance of the T-6242(a) object, and the cycle lane inherits the
whole `chi = sigma` apparatus. This is the concrete form of T-6140's lane dichotomy: either the
minimum stays above the line forever (divergence lane, capped by T-6131) or `L0` exists and the
cycle lane's bound applies at `L0`.

**(c) Consequence: `q` is confined to a sparse, explicitly computable set.** With `B` a bound
below which every integer is verified to reach 1, `m >= B` forces `Bmax(L0) >= B`, and since
`L0 <= q` and the running maximum of `Bmax` is non-decreasing,

```text
        q  >=  L0  >=  min{ j : Bmax(j) >= B } .
```

At `B = 2^71` the right-hand side is `114208327604`. More: the set of `j` with `Bmax(j) >= 2^71`
is so thin that below `2*10^12` it has **six** elements, and only **two** of them are not
multiples of a smaller one:

```text
        q  in  { 114208327604,  217976794617,  228416655208,
                 342624982812,  435953589234,  456833310416 }      (if q <= 2*10^12),

        primitive:  114208327604  and  217976794617 .
```

That is a far stronger statement than a floor: below `2*10^12` the period of a positive cycle is
one of six known integers. **Both `L0` and `q` are confined to this set** — `L0` by (b), and `q`
directly by T-6141(b), which bounds `m` by the same expression evaluated at `j = q` (with no
above-the-line hypothesis, since it comes from the cycle identity). The two routes give the same
set because the set is defined by the `G(k) <= k` form of the bound, which is what T-6141(b) is.

**(d) Where the improvement over T-6141 comes from.** T-6141's floor at `B = 2^71` is
`q >= 1.0377*10^11` via route (f), the Khinchin best-approximation theorem. (c) gives
`1.14208*10^11`, a factor `1.1006`. **The gain is not a new idea — it is the relaxation being
undone.** T-6141(f) replaces "`delta_j` at the actual `j`" with the uniform lower bound
`eps_n > 1/(K_{n+1} + K_n)` valid for all `k < K_{n+1}`; evaluating `delta_j` at each candidate
`j` instead recovers the `1.10x`. T-6243(a) then explains *why* the candidates are what they
are: they are the one-sided best approximations to `log2(3)` from below.

**(e) The 1.386 of (a) does not move this floor.** Substituting the exact `G(k)` for `k` lowers
`Bmax` by `1.386` everywhere, but the ladder of candidate values is so sparse — the previous
candidate is `5.22*10^10` with `Bmax = 1.56*10^20`, two orders below `B` — that the crossing
point does not move. The sharpening is real and will matter at other `B`; at `B = 2^71` it is
absorbed. Reported because the negative result is the useful one: **do not expect the `1.386` to
buy floor.**

## Definitions

As in T-6141 and T-6243. `k_L` = number of odd steps in the first `L` shortcut steps of the
orbit of `m`; "above the line at `L`" means `3^(k_L) >= 2^L`; `Bmax(j)` is T-6243(a).

## Proof

**(a)** Direct comparison. T-6243's proof reaches `n < k/(3(1-r))` with `r = 3^k/2^j` by bounding
each summand of `G(k)` by `1`; multiplying numerator and denominator by `2^j` gives
`n < k 2^j/(3(2^j - 3^k))`. T-6141(b) is the same expression in `(q,k,m)`. `QED`

**(b)** `T^L(m) >= m` for every `L >= 0`, since `m` is the minimum of the cycle. By T-6141(a),
`2^q > 3^k`, so `L = q` satisfies `3^(k_L) < 2^L` and `L0` exists with `L0 <= q`. By minimality
of `L0`, the word is above the line at every `L < L0`, so it is a word counted by `Bmax(L0)`.
Writing `T^(L0)(m) = (3^(k_{L0}) m + c)/2^(L0) >= m` gives `c >= m (2^(L0) - 3^(k_{L0}))`, i.e.
`m <= c/D <= Bmax(L0)`. `QED`

**(c)** From (b), `Bmax(L0) >= m >= B`, so `L0` belongs to `{j : Bmax(j) >= B}`, and `q >= L0`
gives the floor. The candidate set is computed in `cycle_bmax_floor.py`. `QED`

## Dependency audit

| used | from | status |
|---|---|---|
| `prod(3 + 1/n_i) = 2^q`, hence `2^q > 3^k` | T-6141(a) | PROVED |
| `m <= c/D` for an above-the-line prefix | T-6242(a) | PROVED |
| exact `Bmax(j)` | T-6243(a) | PROVED |
| continued fraction of `log2(3)` | computed here by fixed-point squaring, integers only | exact |
| verification bound `B = 2^71` | **INPUT**, not proved here | external |
| Khinchin best-approximation theorem (only for the comparison in (d)) | classical | cited |

## Adversarial tests

1. **The candidate enumeration must reproduce brute force.** `cycle_bmax_floor.py` generates
   candidates from the continued fraction only. `chi_floor.c` evaluates `Bmax(j)` at **every**
   `j <= 3*10^8`. The record sets agree exactly: `1539, 2593, ..., 24727, 75235, 125743, 301994,
   17087915, 51263745, 102225496, 187363077, 272500658` — no record at any `j` outside the
   enumeration, over `3*10^8` values.
2. **The continued fraction must be right.** Computed here to 360 bits by fixed-point squaring
   with integers only; the terms `[1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,...]` and the
   numerators `1,2,3,8,19,65,84,485,1054,24727,50508,125743,176251,301994,16785921,17087915,
   85137581,272500658,...` match the independently computed list in X-6150.
3. **The candidate set is stable under enlarging it.** Closing the generator set under multiples
   up to `60x` and under sums among the 40 largest generators takes it from a few hundred to
   `59659` candidates. The allowed set below `2*10^12` is unchanged: the same six values.
4. **T-6141(e) is recovered.** T-6141(e) reported that the first *convergent* not excluded is
   `q = 217976794617, k = 137528045312`. That pair appears in this enumeration with
   `Bmax = 5.10*10^22`, and it is the second of the two primitive values — consistent, and the
   present computation additionally finds `114208327604` below it, which is not a convergent.

## Gap audit

* **`B` is an input.** Everything numerical here scales with the verification bound and none of
  it is proved in this repository. This is inherited from T-6141 and is not a new weakness.
* **The candidate enumeration is not proved complete, and this is the real gap.** (c)'s floor and
  its six-element set rest on the claim that every `j` with `Bmax(j) >= B` is generated from the
  continued fraction by the closure used. That is verified exhaustively only to `j = 3*10^8`
  (test 1), argued beyond it by the mediant property (a combination `j1 + j2` has
  `delta = delta_1 + delta_2`, so `j/delta` lies between `j1/delta_1` and `j2/delta_2` and cannot
  exceed both), and confirmed stable under a large enlargement (test 3) — but not proved.
  **The rigorous-for-all-`j` floor therefore remains T-6141(f)'s `1.0377*10^11`**, which uses the
  Khinchin bound and needs no enumeration. The `1.1006x` and the six-element set are conditional
  on the enumeration.
* The `G(k) ~ 0.7213475 k` used in (e) is the equidistribution value, with an `O(log k / k)`
  discrepancy correction that is not bounded explicitly. Nothing in (a)-(d) depends on it — the
  floor of (c) uses only the rigorous `G(k) <= k` — so this affects only the sentence saying the
  sharpening is absorbed, which is a negative result and safe in that direction.
* `L0 <= q` is used, not `L0 = q`. The `L0` route alone would therefore constrain only `L0`, not
  `q`. `q` is constrained too, but by a *second* argument — T-6141(b), which comes from the cycle
  identity and needs no above-the-line hypothesis — so the two must be quoted separately rather
  than as one. An earlier draft of (c) ran them together; they are now stated apart.

## Remaining uncertainty

The honest position: the *structure* — that the cycle lane and the coefficient-stopping lane are
one inequality, and that a cycle minimum is a T-6242(a) object — is proved and is the part worth
carrying forward. The numbers are a `1.10x` improvement on a bound that is itself proportional to
`sqrt(B)`, so they move with the verification frontier and not with any new mathematics.

What would change that is a lower bound on `L0` that does not come from `B`. (b) says the cycle's
orbit is above the line for `L0` steps; T-6131 says staying above the line forever has dimension
`0.94996`; R-6171 prices the loop that would close from there. Those three now speak about the
same object, which they did not before.

## Suggested next attack

1. **Close the enumeration gap.** Proving that `max_{j <= J} j/delta_j` is attained at a one-sided
   best approximation would make (c) unconditional and is a statement purely about continued
   fractions — no Collatz content. The mediant property gives it for combinations with all-positive
   contributions; the missing case is where the Ostrowski digits carry mixed signs.
2. **Recompute at the current verification frontier.** `B = 2^71` is the value T-6141 used. The
   whole apparatus is a `python3 cycle_bmax_floor.py` away from any other `B`, and the candidate
   set shrinks fast: the two primitive values are what they are because `B` sits between the
   `5.22*10^10` and `1.14*10^11` rungs of a ladder whose steps are a factor `~20` apart.
3. **Ask what `L0` is for the trivial cycle**, as a sanity anchor: `m = 1`, `q = 2`, `k = 1`,
   and `Bmax(2) = 1`, so the bound is tight there (T-6141 records the same tightness). Any
   sharpening that breaks tightness on the trivial cycle is wrong.
