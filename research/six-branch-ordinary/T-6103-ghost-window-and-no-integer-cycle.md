```text
Claim ID:            T-6103
Title:               Native ghost window of the six-branch chart; no integer has an eventually
                     periodic legal itinerary
Status:              PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        none
Scope:               the fixed chart of T-6101
Related counterexample candidates: none (this claim *excludes* a family)
```

## Statement

Let `c_w = sum_{j=0..L-1} a_{w_j} P^(L-1-j) Q^j` for a word `w` in `{0..5}^L`.

**(a) Tail determinacy.** The infinite legal itinerary determines the point: if `x` in `Z_2`
is legal forever with digit word `(a_n)`, then for every `m`

```text
x_m = - sum_{j>=0} a_{m+j} Q^j / P^(j+1)          (convergent in Z_2).
```

**(b) Ghost window.** For every `L >= 1` and every `w` in `{0..5}^L`, the unique 2-adic point
whose itinerary is `w` repeated forever is the rational

```text
g_w = - c_w / (P^L - Q^L),
```

and it satisfies

```text
-a_5/(P-Q)  <=  g_w  <=  -a_0/(P-Q),        i.e.
-57.785964... <= g_w <= -32.067105...
```

The six constant-word ghosts are exactly

```text
g_i = -a_i/7153:
  -229376/7153, -258048/7153, -290304/7153, -326592/7153, -367416/7153, -413343/7153.
```

None is an integer (`7153 = 23 * 311` is coprime to every `a_i = 7 * 3^(2i) * 2^(15-3i)`).

**(c) No integer eventually periodic itinerary.** No integer — positive or negative — has an
eventually periodic legal itinerary. In particular the chart has **no integer cycle at all**.

**(d) Divergence dichotomy.** Every legal itinerary of a *positive* integer is aperiodic, and
the orbit satisfies `x_n >= (P/Q)^n x_0 -> infinity`. Conversely every *bounded* legal orbit
in `Z_2` is eventually periodic and therefore lands in the ghost window `[-57.79, -32.06]`.

## Motivation

This is the six-branch chart's own version of the phenomenon that the global-blocker audit
identified in the shortcut map (`(1110)^inf -> -19/11`) and in the H subsystem
(`r^inf -> -2^(3r+2)/(3^(2r+1) - 2^(3r+2))`, e.g. `g_3 = -2048/139`). Making it native here
matters because it settles, *unconditionally and by a finite computation*, the entire family
of "prescribed schedule" attacks on this architecture: no periodic, eventually periodic, or
otherwise ultimately-repeating digit schedule can ever be realised by an ordinary integer.
Any future all-time seed for this chart must have an aperiodic itinerary, so schedule-shaped
constructions are dead here and need not be re-attempted.

## Proof

### (a)

From `Q x_{m+1} = P x_m + a_m` we get, exactly, for every `n >= 1`:

```text
x_m = - sum_{j=0}^{n-1} a_{m+j} Q^j / P^(j+1)  +  Q^n x_{m+n} / P^n.        (*)
```

(Induction on `n`; each step is the previous identity solved for `x_m`.) `P` is a 2-adic unit
and `x_{m+n}` lies in `Z_2`, so `v_2(Q^n x_{m+n}/P^n) >= 19n -> infinity`. Letting `n ->
infinity` in `Z_2` gives (a). Note the series also converges in `R`, but the two limits are
*a priori* different objects; only the 2-adic one is used here.

### (b)

If the itinerary is `w` repeated, then the tail at `m` and at `m+L` are the same infinite
word, so by (a) `x_{m+L} = x_m =: g_w`. Unwinding `L` chart steps,

```text
Q^L x_{m+L} = P^L x_m + c_w   =>   g_w (Q^L - P^L) = c_w   =>   g_w = -c_w/(P^L - Q^L).
```

For the bounds, put `S = sum_{j=0..L-1} P^(L-1-j) Q^j = (P^L - Q^L)/(P - Q)`. Since
`a_0 <= a_{w_j} <= a_5` for every `j`, we get `a_0 S <= c_w <= a_5 S`, hence

```text
a_0/(P-Q)  <=  c_w/(P^L - Q^L)  <=  a_5/(P-Q),
```

which is the claim after negation. Numerically `P - Q = 7153` and
`a_0/7153 = 32.067105...`, `a_5/7153 = 57.785964...`.

For `L = 1` the formula gives `g_i = -a_i/(P-Q) = -a_i/7153`. Since `7153 = 23 * 311` and
`a_i = 7 * 3^(2i) * 2^(15-3i)` has only the prime factors 2, 3, 7, we have `gcd(a_i, 7153) = 1`
and `g_i` is never an integer.

### (c)

Suppose `x_0` in `Z` is legal forever with itinerary eventually periodic: there are `m >= 0`
and `L >= 1` with `a_{n+L} = a_n` for all `n >= m`. Then the tail at `m` is purely periodic,
so by (b) `x_m = g_w` for the corresponding `w`, hence

```text
x_m in [-57.785964..., -32.067105...].
```

But `x_0` in `Z` forces `x_m` in `Z` (each chart step of a legal integer yields an integer).
Therefore `x_m` lies in

```text
Z ∩ [-57.785964, -32.067105] = {-57, -56, ..., -33}    (25 candidates).
```

Each of these 25 integers is checked directly (`window.py`): for every one of them the very
first digit `d(x) = (-P x) mod 2^19` fails to lie in `A`. So none of them is even one-step
legal, let alone all-time legal. Contradiction. `QED`

A cycle of the chart in `Z` would be a purely periodic legal integer itinerary, so (c)
excludes integer cycles as a special case (`m = 0`). This includes negative integers, so the
chart — unlike the true Collatz map, which has the negative cycles at `-1, -5, -17` — has no
integer cycles whatsoever.

### (d)

If `x_0 >= 1` is legal forever, its itinerary cannot be eventually periodic by (c); and
`x_{n+1} = ceil(P x_n/Q) >= P x_n/Q` gives `x_n >= (P/Q)^n x_0 -> infinity` since `P > Q`.
For the converse, a legal orbit in `Z_2` that is bounded in the real sense and takes rational
values with bounded denominator must repeat a value, and repetition of the value forces
repetition of the itinerary (the itinerary is a function of the point). `QED`

## Dependency audit

* (a) is self-contained; (b) uses (a); (c) uses (b) plus the 25-case finite check; (d) uses
  (c). Nothing outside this file is invoked.
* The finite check is reproducible: `experiments/X-6110-six-branch-least-root/window.py`.

## Gap audit

* *Is the window closed under the chart?* Not needed. The argument never requires the ghost
  window to be invariant; it only needs the single point `x_m` to lie in it.
* *Eventually periodic vs. periodic*: handled — the theorem is applied at the index `m` where
  periodicity begins, not at `0`.
* *Integrality of `x_m`*: `x_{k+1} = (P x_k + a)/Q` with `Q | P x_k + a` by legality, so a
  legal orbit of an integer stays in `Z`. Stated explicitly above.
* *Does (b) secretly assume the periodic point is the 2-adic limit rather than a real limit?*
  No. `g_w` is derived from the algebraic identity `Q^L x_{m+L} = P^L x_m + c_w` together with
  `x_{m+L} = x_m`, and the latter comes from (a), which is a genuine `Z_2` statement. The real
  series is never equated to the 2-adic one.
* *Sharpness of the window*: the endpoints are attained in the limit by the constant words
  `0^inf` and `5^inf`, so the interval cannot be shrunk without more information; the
  candidate set `{-57,...,-33}` is therefore not artificially large.
* *(d) converse rigor*: the converse half of (d) is the only place where a soft argument is
  used ("bounded + bounded denominator ⇒ repetition"). It is not used anywhere else in this
  namespace, and no later claim depends on it. Marked accordingly.

## Adversarial tests

* All six `g_i` recomputed exactly as fractions and confirmed non-integral (`ghosts.py`).
* Exhaustive search over **all** `6^L` words for `L = 1..8` (2,015,538 words) for a word with
  `(P^L - Q^L) | c_w`, i.e. an integral ghost: **none found**, consistent with (b)+(c).
* All 25 window integers checked: legal-step count `0` for every one of them.

## Remaining uncertainty

None on (a)-(c). The converse half of (d) is stated loosely on purpose and is not load-bearing.

## Suggested next attack

None on this claim; it is closed. Its value is negative-directional: it removes the entire
"choose a schedule and realise it" family from the six-branch lane. Consumers should cite
T-6103(c) rather than re-running schedule exclusions.
