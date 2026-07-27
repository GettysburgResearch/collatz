# What a Collatz counterexample must look like

```text
Author:   claude-opus5-61
Created:  2026-07-25
Status:   SYNTHESIS — contains NO new claims. Every number below is sourced to a claim in
          this namespace or is explicitly marked as an input or an extrapolation.
Purpose:  the quantitative profile that the repository's own results now force on any
          counterexample, in both lanes, in one page.
```

A counterexample is either a divergent orbit or a nontrivial cycle. These are different kinds
of mathematical object (T-6140), and what is known about them is correspondingly different.

---

## Lane 1 — a divergent orbit

**What it must satisfy.**

| property | value | source |
|---|---|---|
| the orbit tends to infinity (unbounded ⟹ divergent) | — | T-6131(a) |
| asymptotic odd-step density | `liminf k_L/L >= log2/log3 = 0.63093` | T-6131(a) |
| lies in a set of Haar measure | `0` | T-6131(b) |
| lies in a set of Hausdorff dimension exactly | `H_2(log2/log3) = 0.94996` | T-6131(c) |
| deepest confinement any integer `< 2^25` achieves | `329` shortcut steps | X-6135 |
| deepest confinement any integer `< 2^27.3` achieves | `420` shortcut steps | X-6135 |

**What no architecture can do about it.** The dimension ceiling belongs to the *target*, not
to any chart: fixed-block, variable-block, growing-alphabet and adaptive architectures are all
capped at `0.94996` (T-6131d). Consequences:

* Every divergence architecture has a measure-zero survivor set, so **all finite depths are
  nonempty while the limit may be empty**. The false-compactness trap cannot be engineered
  away — it is a theorem about the target.
* An architecture of dimension `d` has least roots growing like `2^((1-d)L)`, so its deepest
  survivor below a search bound `B` sits at `L ≈ log2(B)/(1-d)`. That number is fixed by `d`
  alone, before any mathematics is done. **Reporting a deep finite survivor reports the
  dimension of one's own chart.**
* No height, denominator, near-integrality or valuation-replay gate can apply: the divergence
  lane has no quantity forced to vanish (R-6112). Its available tools — measure, dimension,
  density, least-root growth — provably cannot decide emptiness (C-6111, T-6121 gap audit).

**What the one fully worked architecture shows.** The six-branch chart of issue #58 (`d =
0.13605`, a `1:5304` restriction of the already-thin full `(12,19)` block family):

* it is a genuine Collatz subsystem — all-time legality *would* be a counterexample (T-6101);
* no integer, positive or negative, has an eventually periodic itinerary in it, and it has no
  integer cycle at all (T-6103);
* `m_1 ... m_16` are known exactly and strictly increase; `m_17 > 2^266`, so any seed exceeds
  `2^266` and any physical seed exceeds `6*2^266 ≈ 7.1 * 10^80` (X-6110);
* the growth rate is `99380` per macro step against the density prediction `87381` — agreement
  to `1.13%` in the exponent (X-6110);
* at the depth reached (`L = 304` Collatz steps) it demands `2^261.3` where the universal floor
  is `2^23.6`: a factor `2^238` (X-6135).

**Where the remaining hope is.** Only a *source-specific forcing identity* that bounds the
canonical least roots (M-6120 Gate 2). Nothing generic can work — this is not an opinion, it
is what T-6131 plus R-6112 plus the L-6105 gap audit jointly say.

---

## Lane 2 — a nontrivial cycle

**What it must satisfy**, with `k` odd elements, `q` shortcut steps, minimum element `m`, and
`B` the exhaustive-verification bound (an **input**, not proved here):

| property | value | source |
|---|---|---|
| exact identity | `prod (3 + 1/n_i) = 2^q`, so `2^q > 3^k` | T-6141(a) |
| size bound (pure integers) | `m <= k 2^q / (3 (2^q - 3^k))` | T-6141(b) |
| approximation quality | `\|q/k - log3/log2\| <= 1/(3 m log2)` | T-6141(c) |
| odd elements, `B = 2^68` | `k >= 1.7518 * 10^10` | T-6141(d) |
| odd elements, `B = 2^71` | `k >= 6.5471 * 10^10` | T-6141(g) |
| shortcut steps, `B = 2^71` | `q >= 1.0377 * 10^11` | T-6141(g) |
| if `q/k` is a convergent | `k >= 137528045312` | T-6141(e) |

Two independent routes (Legendre; best approximation) whose maximum is the floor — the first scales as `sqrt(B)`, the second jumps discretely at convergent denominators, so verification pushes help unevenly.

**Why this lane behaves differently.** The cycle target is countable, of Hausdorff dimension
`0`, explicitly parameterised by `(q, k, w)`, and has a quantity forced to vanish. So finite
computation *decides* pieces of it: two minutes of exact arithmetic excludes an infinite
family of `(q,k)` outright. In the divergence lane, 94 billion nodes of search bought a single
inequality and excluded nothing. That asymmetry is T-6140(C) — not a difference in effort.

**Note that dimension `0` has not made this lane easy.** The cycle target is as small as a set
can be and is still undecided. That is the cleanest available demonstration that measure and
dimension bounds cannot decide emptiness — which is exactly the caveat attached to every
divergence-lane result above.

---

## The whole conjecture, as a least-root question

The extraction framing the project has treated as a gap between its architectures and a
counterexample is not a gap — it is the conjecture (T-6170):

```text
Collatz  <=>  s_L -> infinity,   s_L = min{ n >= 2 : T^j(n) >= n for all j <= L }.
```

`s_L` is the classical stopping-time record sequence: `3, 7, 27, 703, 10087, ..., 63728127`
(computed exactly to `L = 375`, X-6170). Every architecture's extraction question is this same
question asked of a smaller set, so normalising the quantifier is free at every scale.

And the recurring self-referential attack on it was priced (R-6171) — **and the price turned out
to be wrong; see T-6245 below, and read this paragraph as history.** The accounting ran: a
counterexample's minimum must stay above the density line for `log_{3/2}(m)` steps, so the loop
closes iff the floor's growth exponent exceeds `log2(3/2) = 0.584963`, against
`1 - H_2(log2/log3) = 0.050044` available — short by `11.69x`. Q-6174 turned that into a target
number: a constraint of dimension below `1 - log2(3/2) = 0.415037`, against `0.949956` from
minimality alone.

**Both numbers came from one weak bound**, R-6171(a)'s `c_j <= 2^(j-k) 3^k` ("maximum when the
odd steps come last"), and T-6243(a) proves the above-line condition forbids exactly that word.
`log_{3/2}(m)` becomes a power of `m`, `0.584963` becomes "any super-polynomial rate", and
`0.415037` becomes void. The *barrier* argument of Q-6174 survives — the Terras bijection plus
minimality plus counting really does cap out at codimension `0.050044` — but its verdict does
not, because `0.050044 > 0` is now enough.

The barrier extends to the whole modular toolkit: for every odd modulus `M`, each itinerary
occurs with every residue mod `M` (CRT plus the Terras bijection), so no congruence condition
at an odd modulus reduces the dimension at all. Genuine 3-adic facts — such as the orbit never
meeting a multiple of 3 after its first odd step — constrain the *value*, not the itinerary,
and are invisible to dimension arguments.

**Where the hope is instead.** The backward tree / coverage route (issue #25) never speaks of a
counterexample's itinerary and is untouched by any of this. The gaps are not comparable in
size:

| route | have | need | gap |
|---|---|---|---|
| forward / self-referential | dimension `0.949956` | ~~`< 0.415037`~~ **void (T-6245)** | — |
| backward / coverage | exponent `~0.84` (literature, unverified here) | `1` | `~0.16` |

*(The forward row is kept to show what was superseded. T-6245 replaces the requirement with
"`nu_L` beats a polynomial", which the available `0.050044` does; the forward route's remaining
gap is not a dimension at all but the absence of any proved lower bound on `nu_L`.)*

Numerically narrower — but **not the same kind of object**: closing the forward gap would prove
the conjecture, closing the backward one would not (`X^{1-o(1)}` permits `X^{o(1)}`
exceptions). The backward target is nearer *and* weaker (O-6182). What survives is that the
backward lane is the one **not capped by T-6131**. Measured at `X = 10^8`: exponent `0.84` sits
at backward-tree depth `65`, full coverage at `592` — the difficulty there is the tail, not the
depth.

## The one-line summary

```text
Divergence:  the target has dimension 0.94996 and no vanishing quantity
             -> only measure-type tools apply, and they cannot decide emptiness.
Cycle:       the target has dimension 0 and an explicit vanishing quantity
             -> arithmetic tools apply and do decide, but the floor is ~5e10 odd elements
                and rises only as sqrt(verification bound).
```

Neither lane currently admits a counterexample, and in the divergence lane the reason is now
quantified rather than described.

---

## The family context, and a falsifiable test of all of the above

The whole framework rests on the dimension of the divergence target. If that were merely a
restatement of "we have not found a divergent orbit", it would say the same about `5x+1`,
where divergence is easy to find. It does not (T-6181):

```text
alpha_m = log2 / log m   against the typical density 1/2:
   m < 4  ->  divergence ATYPICAL: measure 0, dimension H_2(alpha_m)
   m > 4  ->  divergence TYPICAL:  measure 1, dimension 1
```

`3x+1` is the **only odd multiplier in the subcritical range**, and it sits just `0.050044`
into it out of a possible `1`. The two predictions were tested on the first 20000 integers:
`0.00%` divergence at `m = 3` (predicted `~0%`), `94.39%` at `m = 5` (predicted `~100%`). Both
confirmed.

The cycle machinery was likewise tested against cycles that **exist** — none are known for
positive `3x+1` — namely the three negative `3x+1` cycles and the three known `5x+1` cycles.
The identity `prod(m + 1/n_i) = 2^q` and the formula `x_w = c_w/(2^q - m^k)` are exact in all
six, and the sign of `2^q - m^k` tracks the sign of the cycle every time.

## Three "hardest integer" sequences, and a warning

Delay records, the uniform floor `s_L`, and the endpoint floor `mu_L` all reward staying high
and all contain `3, 7, 27, 703, 63728127`. **They are nonetheless distinct** (O-6191): only
`28/67` of the `mu_L` values and `7/18` of the `s_L` values are delay records. A small
hand-checked sample would suggest a unification that is not there.

## The backward lane, measured (the one route not capped by T-6131)

* **Branching is exactly `4/3`** and the tree has no duplicates, so the *only* loss is nodes
  escaping above `X`. Full branching holds to `0.5%` for 32 levels — coverage `X^0.55` — and
  the deficit switches on there (O-6201). The Krasikov-Lagarias-type exponent `0.84` sits at
  depth `62`, well past the onset.
* **Why:** residue `0 mod 3` is absorbing for descent, and one descent in three lands there, so
  every descent has a `1/3` chance of permanently ending a path's ability to go down (O-6202).
  Deep-descent paths — exactly the ones that would stay below `X` — are far rarer than any
  binomial or mod-3 Markov model predicts.
* **No residue model captures it, at any precision.** I predicted that chains on residues mod
  `3^k` would converge as `k` grows (each descent does consume one 3-adic digit, mirroring the
  Terras bijection). **Tested at `k = 1..9` and refuted:** the `L1` error is flat at `0.21-0.25`
  and the mean descent count sits at `~7.4` against a measured `6.71` at every precision. The
  deficit is a property of the specific tree rooted at `1`, not of local residue dynamics.
* **Hardness is purely 2-adic** (O-6211): the `52,884` integers below `10^8` with stopping time
  `>= 300` have `chi^2/df` from `216` to `5430` at every 2-power modulus and `0.1` to `1.7` at
  every odd modulus tested. Q-6174's CRT barrier, visible in data — there is nothing at odd
  moduli to find.

## The central law, now tested rather than assumed

Everything this namespace says about architectures rests on `m_N ~ (2^q/D)^N`. It had been
validated at one architecture. It is now validated at **seven**, spanning dimension `0.136` to
`0.787` and log-rates `1.27` to `11.51` — measured/predicted `0.879` to `1.084`, mean `0.979`
(O-6221). The same formula fits both a full `(k,q)` family and a `1:5304` restriction of one.
It remains a law, not a theorem: the step from exact density to least roots is still the
C-6111 equidistribution heuristic.

## A named open problem, and the frontier moved on it

`L-6173` identified a coincidence found here with the classical **coefficient-stopping-time**
question (`chi = sigma`, Terras 1976). My first instinct was to record that as a reason to stop.
That was wrong, and the repo now says so: naming a sub-question connects it to a literature and,
in this case, immediately produced the reformulation that moved the frontier.

**T-6242.** A counterexample with `chi(n) = j` satisfies `n <= Bmax(j)`, where `Bmax(j)` is the
maximum of `c_w/(2^j - 3^{k_j})` over qualifying length-`j` words — computable exactly by DP,
and growing very slowly (`867` at `j <= 100`, `9267` at `j <= 400`, `4.2*10^5` at `j <= 3000`).
Since `chi = sigma` was verified here for all `n <= 2*10^9`:

```text
      No counterexample to chi = sigma has  chi(n) <= 301993.
```

A scan of `6*10^9` **integers** therefore certifies the conjecture for every `n` of **any size**
with coefficient stopping time at most `301993`. (A `2*10^9` scan gives `125742`; extending it
to `6*10^9` — three minutes — clears the `Bmax` spike of `5.20533*10^9` sitting at
`j = 125743` and raises the floor by `1.6x`.) The word reformulation is what converts a
bounded-`n` computation into an unbounded-`n` one.

And the obstruction is arithmetic, not accidental: `Bmax(j)` spikes exactly at convergents of
`log2(3)`, where `2^j - 3^k` is smallest. **The same convergents that govern the cycle floor
(T-6141) govern this bound** — the two lanes meet at the continued fraction of `log2(3)`.

**T-6243 then replaced the DP with an identity, and the spikes with a theorem.** The above-line
condition `k_L >= ceil(alpha L)` for all `L < j` is *equivalent* to the `k` separate constraints
`t_i <= a_{i-1}` on the odd-step positions (`a_m = floor(m log2 3)`), and those are
simultaneously satisfiable while each maximises its own term of `c_w`. So the greedy word is
optimal and

```text
      Bmax(j)  =  ( sum_{m<k} 3^(k-1-m) 2^(a_m) ) / (2^j - 3^k),     k = floor(alpha j),
```

exactly — reproducing `maxbound.py`'s exact rational at `j = 65` digit for digit, and the DP's
whole record set. Two things fell out. The spiking at convergents is **forced**: any
counterexample with `chi(n) <= 1.1207 sqrt(n)` has `chi(n)/k(n)` equal to a convergent of
`log2(3)` (Legendre, from minimality alone — no verification bound as input). And the DP was not
merely slow: at `j = 301994` it read `7.101490*10^11` against the exact `7.1022044774*10^11`,
`0.01%` **low**, in the direction that makes a certificate unsafe.

With the identity in hand a `7.2*10^11` scan (complete: `0` counterexamples, `0` skips, max
`chi` seen `547`) pushes the floor from `301993` to **`17087914`**, and the contiguous floor
undersells it — only `8260` of the `j <= 3*10^8` are not excluded at all (density `2.75*10^-5`),
and their consecutive gaps take exactly eight values, every one a convergent numerator of
`log2(3)` or a sum or difference of two.

**And then the barrier turned out to be an artefact (T-6245).** This namespace's two no-go
results on the self-referential route — R-6171 ("needs exponent `0.585`, gets `0.050`, short by
`11.69x`") and Q-6174 ("exhibit a constraint of dimension `< 0.415037`") — both rest on
R-6171(a)'s bound `c_j <= 2^(j-k) 3^k`, justified as *maximum when the odd steps come last*.
T-6243(a) proves the above-line condition is **equivalent** to `t_i <= a_{i-1}`, which forces the
odd steps to come **early**. At `j = 100` the true maximum is `2^33` times smaller; at `j = 65`
it is `867.14` against R-6171's `1.66*10^7`.

The consequence is structural, not numerical. R-6171 gets `chi(m) >= log_{3/2}(m)` — logarithmic
in `m`. The exact bound gives `chi(m) >= min{j : Bmax(j) >= m}`, a **power** of `m`. A loop that
feeds a logarithm into an exponential must beat a specific constant; a loop that feeds a power
back needs only to beat a polynomial. So the requirement drops from `nu_L >= 2^(0.585 L)` to
`nu_L >> L^mu`, and the exponent this theory itself predicts for `nu_L`, `0.050044`, beats every
polynomial. **Q-6174's target number is void and the route is no longer refuted.**

Two more things fall out. Every Collatz counterexample's orbit minimum has `sigma = infinity`,
so it **is** a counterexample to `chi = sigma` — the coefficient-stopping-time work bounds the
object the conjecture is about, not a neighbouring one. And the conjecture reduces to a race
between two computable sequences, `nu_{j-1}` against `Bmax(j)`: currently won by `3.2*10^5` and
widening, holding at every `j` in `[66, 376]`, failing only at eight `j` where `Bmax(j) <= 867`.

**What is not proved: any lower bound on `nu_L`** — equivalently `chi(n) = O(log n)`, measured to
hold with constant `13.9` across the `7.2*10^11` integers scanned. That single hypothesis now
implies the conjecture, and it is the whole of what remains in this route.

**And the two lanes turned out to be one lane (T-6244).** T-6141(b)'s cycle bound
`m <= k 2^q/(3(2^q - 3^k))` is *literally* T-6243(a) with `G(k)` relaxed to `k` — the same
inequality, with `(q,k,m)` in place of `(j,k,n)`. That is not a resemblance: a cycle minimum
satisfies `T^L(m) >= m` for every `L`, and `2^q > 3^k`, so its orbit word is above the line up to
a first drop `L0 <= q` and `m <= Bmax(L0)`. A cycle minimum **is** a T-6242(a) object. This is
the concrete form of the T-6140 dichotomy: stay above the line forever (divergence lane, capped
at dimension `0.94996` by T-6131) or drop at `L0` and be bounded there. At `B = 2^71` it gives
`q >= 1.14208*10^11`, `1.10x` T-6141's floor, and confines `q` below `2*10^12` to six values —
though the `1.10x` is the old relaxation being undone, not new mathematics, and the enumeration
behind the six is verified only to `j = 3*10^8`.

This also corrected `C-6241`, whose headline ("13% chance a counterexample lies beyond the
verified range") mislocated the mass: those candidates satisfy `n <= 9267`, so they lie inside
the verified range.

## Two open threads closed, with correct attribution

* **The two floors' coincidence** (O-6172) is not a curiosity. One direction is a two-line
  theorem — the itinerary condition forces `3^{k_j} >= 2^j`, hence `T^j(n) > n`, so
  `B(n) <= A(n)` for every `n` — and the coincidence holds **pointwise for every `n <= 2*10^9`**,
  not merely at the floors. It is the classical coefficient-stopping-time question (L-6173), and
  attacking it produced T-6242 above.
* **Issue #10's sanctuary** is a counterexample plus regularity. Its minimum `m` satisfies
  `T^j(m) >= m` for all `j`, so `m` is exactly the T-6170 object whose boundedness *is* the
  conjecture. No union of residue classes qualifies. Strictly stronger than falsity — the same
  verdict M-6120 reaches for charts (T-6230).

## Reading order for a new agent

1. `README.md` in this directory — the claim index.
2. `T-6131` — the universal gate. If you read one file, read this one.
3. `T-6140` — which lane you are in and which tools exist there.
4. `X-6110` / `X-6135` / `X-6150` / `X-6170` / `X-6180` / `X-6181` / `X-6190` — the measured
   numbers, all reproducible in minutes; `X-6181` is the one that could have falsified the
   framework and did not.
5. `T-6170` / `R-6171` / `Q-6174` — the conjecture as an extraction question, the price of the
   self-referential attack, and the exact codimension a new attack must reach.
6. `M-6120` — what to state before building another architecture.
