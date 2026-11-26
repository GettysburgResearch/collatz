# Six-hour continuation: ordinary mergers, measured escape, and arithmetic closure

**Collatz remains open.** This continuation started from PR201 at
`21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a` and inspected the new work at
the five source pins below. The first checkpoint contains independently
reconstructed written results, three new finite Lean modules, and exact
controls. It supplies neither a successful merger for every start nor a
vanishing escape statistic nor an exclusion of every nontrivial cycle.

## The exact early merger theorem

Put `M_m = 2^m - 1`, `P_m = 3^m - 1`, and use the native shortcut map.
For an arbitrary supplied positive `x < M_m`, write `x+1 = 2^n b` with
`b` odd. If

\[
 T^iP_m=T^{n+l}x,\qquad 2i+\max(i,l)<m,
\]

then **the clocks coincide**: `i=l`. Moreover `b=3^d` for an integer
`d≥0`, `t=n+d<m`, and the same meeting occurs between the two pure
peaks `P_m,P_t`, with the exact compensating odd count. Before the
lower source reaches its own peak, a meeting is impossible when `3i<m`.
Thus the whole short-window search over all smaller ordinary sources
reduces to the finite list of earlier peaks. The theorem preserves both
physical clocks; it does not supply a successful member of that list.

[Statement, proof, infinite obstruction, and source comparisons](coupling/PEAK_RIGIDITY.md)
· [Actual native-map Lean proof](coupling/PeakRigidity.lean).

The finite-class argument from PR195 also shows that infinitely many
actual exponents have **no** smaller visitor anywhere in the entire
square through `floor((m-1)/3)`, with the lower initial ascent added to
its clock. These exponents are not asserted to lie on a prescribed
hard progression. The all-time merger question remains open.

## An escape test on the actual positive representatives

Let `ρ_k=3^k p_k` be the density of the original geometric Syracuse law,
`Φ(u)=u²/(1+u)`, and

\[
 M_k=\frac1k\sum_{0<y<2\cdot3^k,\ y\ {\rm odd}}
       \Phi(\rho_k(y)/y)\,\delta_y.
\]

Under the named PR193 inputs, these finite measures approach, in total
variation on the ordinary integers, the weighted empirical initial
segments of the actual escaping rays. This permits depth-dependent
tests of the representatives themselves. Write `α=log₂3` and let
`K_b(m)` be the positive odds whose first `j` odd steps use at most
`bj` halvings for every `j≤m`. For every `α<b<2` and **any** sequence
of depths, including infinite depths,

\[
 \liminf_k M_k(K_b(m(k)))\ge\frac{b-\alpha}{b-1}
            \sum_C\Phi(H_C).
\]

The sum is over escaping components and is strictly positive if one
exists. The same dyadic test has exponentially small Haar probability.
The latter fact does not prove a small measured mass on the left.

[Total-variation argument and permanent sieve](escape/PERMANENT_SIEVE.md)
· [Lean proof of the whole-future selection count](escape/PermanentSieve.lean).

The measurable inverse entropy dichotomy of PR200 gives another
consequence: on an explicit positive portion of any nonzero limiting
mass, arbitrarily accurate finite ternary tables predict the actual
preceding word, even across different positive targets in the same
residue class. The methodological predecessor is PR200's
`trace/UNIFORM_DECODER.md`: it already uses Markovization and finite
prediction on low-entropy subshifts. The present result uses a thin
state portion of arbitrary finite-mean processes and the actual
clipped ordinary measure. Prediction alone is compatible with many
known convergent integer segments.

[Ternary decoder with the precise limit order](escape/TERNARY_DECODER.md)
· [Ordinary integer controls](escape/ORDINARY_DECODER_CONTROLS.md).

## What the arithmetic tower now proves

The new arguments retain the actual vertex integers and all finite
primes, including repeated quadratic fields.

* On a high interval of `m` odd departures with distinct Pell labels,
  the cubic unit product has height asymptotic to one third of the
  sum of the logarithms of the vertex heights. A scalar which reduces
  this to negligible height must generally have degree
  `3^((1-o(1))m)`. The exact ordinary telescope has precisely that
  degree. [Height and degree theorem](arithmetic/CUBIC_HEIGHT_COST.md).
* One compatible place over each rational prime can be selected for
  the **entire** infinite orbit field so that the finite-place
  corrections telescope. This is one selected place, not all places.
  The full normalized traces on simple intervals are rational and
  uniformly approach one as their minimum grows. An exact convergent
  interval from `43681` gives trace `369/362`; its denominator has an
  interior prime absent from both endpoints. Thus selected-place
  cancellation does not imply trace integrality.
  [All-time places and full trace](arithmetic/ALL_TIME_CUBIC_TRACE.md).
* A fixed normalized rational function at any finite level of the
  Pell division tower, supported only above the two actual edge
  factors, either is the ordinary rational telescoping correction or
  has leading real order at most `x^(-2/3)`. Allowing arbitrary
  algebraic coefficients does not remove this gap; the divisor
  multiplicities remain integers. [Uniform tower theorem](arithmetic/PELL_TOWER_ORDER.md).

[Finite valuation-average Lean kernel](arithmetic/CubicHeight.lean).
The Galois, height, and infinite trace arguments are written proofs,
not complete Lean formalizations.

## Evidence and dependencies

The root replay freshly rebuilt the imported `CoreBranching` module
and the three new Lean modules with warnings as errors. It queried
24 declarations, of which 12 are new; only the standard logical
axioms were reported. The three finite controls ran in normal and
optimized Python with identical complete outputs. These checks do
not discharge the remaining analytic or arithmetic closing steps.

[Replay program](../../reports/six-hour-20261127/replay.py)
· [Root proof review](../../reports/six-hour-20261127/ROOT_FIRST_REVIEW.md)
· [Coupling cross-review](../../reports/six-hour-20261127/ARITHMETIC_REVIEW_OF_COUPLING.md)
· [Escape cross-review](../../reports/six-hour-20261127/COUPLING_REVIEW_OF_ESCAPE.md)
· [Arithmetic cross-review](../../reports/six-hour-20261127/ESCAPE_REVIEW_OF_ARITHMETIC.md).

| Source | Exact intake head | Main imported work inspected |
|---|---|---|
| PR192 | `ed7a6fe30b8602407f77855ceb74ce0489ce9c10` | Actual hard-parent repairs; Pell and cubic fields |
| PR193 | `25f5462e2c43feea65760884f7ea8f53576fbc18` | Original-law collision energy; uniform physical ray trace |
| PR195 | `51d97cbe17054415acaf95e422801a3532545033` | Bounded canonical floors; augmented peak classes |
| PR197 | `1f0f496fbea37792439feada6106eaaff596bcd1` | All-source clocks and signed-carry exclusion |
| PR200 | `ad70a3b831867cb8a74d402a2a1abdc419f5a09b` | Measurable inverse entropy; exact pressure; reset and decoder work |

The intake report records 100 PR metadata snapshots and their remote
head checks. That inventory is not a proof review of every file on
those branches. Paths reused on different branches are always qualified
by their commit. The preceding pass remains at
[unconventional-20261126](../unconventional-20261126/README.md).

## Continuing targets

The next steps are an actual all-time ordinary merger beyond the short
cone, a cancellation estimate for the exact weighted integer diagonal,
and exclusion of the full positive-cycle denominator. A new criterion
will be promoted only with its ordinary realization and missing
quantifiers checked; the first checkpoint is not the end of the
requested six-hour pass.
