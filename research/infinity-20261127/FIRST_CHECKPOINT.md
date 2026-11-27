# First checkpoint: exact old-source failure and arithmetic packing

**Collatz remains open.** The all-input finite-mass implication has been
freshly rebuilt, but its small-mass premise is not proved. This checkpoint
records three independently pursued routes and the root's weighted-counting
supplement. It is an intermediate checkpoint in the requested six-hour pass.

## 1. Failure of a fixed old ordinary source

Use the accelerated odd map `U` and its actual dyadic clock `A_j`. The
ordinary prefix gate is `4 A_j <= 7 j`. For an odd source `m`, the explicit
integer condition

\[
3^{12n}m^{12}(2n+1)^2<2^{21n},\qquad n>0,
\]

persists at every later depth. If the source's first gate failure is `F>=n`,
then it has already reached 1 at a clock `tau<F`, and

\[
F+4A_\tau=8\tau+1,\qquad F\equiv1\pmod4.
\]

For an eligible source that passed through `n`, all intervening prefix
tests up to any later horizon are equivalent to the single terminal clock
test. The proof controls the correction product on a simple segment by
`(2j+1)^(1/6)`, removes repeated nontrivial laps before first failure, and
uses the actual `1 -> 1` odd loop. An adapter identifies the abstract edge
equations with PR200's executable valuation and state definitions.

[Complete argument](mass/OLD_HEAD_FIRST_FAILURE.md) ·
[Budget](mass/OldHeadBudget.lean) ·
[First-failure proof](mass/OldHeadFirstFailure.lean) ·
[Ordinary adapter](mass/OldHeadOrdinary.lean).

This identifies what eventual failure would mean; it does not prove its
occurrence. The separate written rate comparison shows why exponential
decay of this source mass is considerably stronger than a qualitative
extinction statement: it also forces a uniform logarithmic odd stopping
bound. That rate is not assumed here.

The first mass wave proves actual same-source one-step deaths at resonant
depths `n=2^k`, `k>=55`, of order `n^(-3/2) gamma^n`, where
`gamma=(7/8)(7/6)^(3/4)<1`. Three explicit suffixes cover all relevant
phases and produce literal positive ordinary sources. These losses match
the size of the recent birth population. Their sources grow with depth;
the result supplies no nonsummable loss estimate for a fixed old atom.
[Native loss proof and scope](mass/RESONANT_NATIVE_LOSS.md).

## 2. Pell packing on actual ordinary paths

For an odd departure `x`, put `D=sf(3x(3x+1))`. Distinct positive odd
departures sharing `D` have successive height ratios exceeding both
`97+56 sqrt(3)` and `4D`. If the same `D` returns after `h` actual shortcut
steps, the initial height is less than `3*12^h`. The second result uses a
nonzero odd algebraic norm; it allows arbitrarily large individual
valuations and retains the intervening ordinary path.
It sharpens PR192's prior same-field return bound `4*36^h`; the return
mechanism itself is credited there.

This bounds the population in any prescribed squareclass space, even if
the unmarked intervening states have no rank or height restriction. A
short square relation before a maximum gives a separate height bound.
Combining these facts with exact pivot-prime counting yields the proposed
all-period result: **every nontrivial ordinary cycle has affine
edge-product squareclass rank at least 32**.

The rank-31 exclusion compares an exact upper bound of
`127,901,154,889` odd states with Hercher's published period floor
`137,500,000,000`, using Barina's published verification below `2^71`.
Those external searches are not repeated here. The entire rank theorem is
a written argument plus exact finite arithmetic; the new Lean module
checks five of its algebraic interfaces, not the whole analytic theorem.
[Packing proof](arithmetic/PELL_RETURN_PACKING.md) ·
[Numerical rank certificate and dependencies](arithmetic/RANK_CERTIFICATE.md) ·
[Lean scope](arithmetic/PellReturnPacking.lean).

The root's [weighted supplement](HEIGHT_WEIGHTED_RANK.md), independently
checked by the arithmetic agent, retains the ordinary sizes of the pivot
primes. For `N` distinct departures below `X`, with affine edge-product
squareclass rank `r`, it gives, for every fixed `0<sigma<1`,

\[
N\le\left(1+\frac{\log X}{\log(97+56\sqrt3)}\right)
(12X^2)^\sigma\exp\!\left(\frac{(r+1)^{1-\sigma}}{1-\sigma}\right).
\]

Consequently `X<=N^(B+o(1))` forces
`liminf log(r+1)/log log N >= 2B/(2B-1)`.
The finite weighted-subset inequality is formalized separately. A
`6/5` rank exponent on the earlier bounded physical cycle band retains
Chudnovsky's explicitly quoted October 2026 preprint input. No upper rank
bound has been proved that contradicts these lower bounds.

## 3. Joint targets cannot be replaced by independent predecessor counts

For an ordinary invariant `b`, write `d(n)=b(n+1)-b(n)`. At every dyadic
scale the same prescribed pair satisfies

\[
b(3q)-b(q)=d(2^{k+2}q)-d(2^k3q).
\]

There is also an explicit four-path merger in every block of 128 exponent
choices. Its negative neighbors use exponent `k`, whereas its positive
neighbors use exponent `2k`. They are not neighbors of one common center.

For prescribed targets `a,b`, the joint event that `x` visits `a` and
`3x` visits `b` agrees, outside the stated finite-coalescence error, with
the event that `x` visits both. The latter event requires one target to
visit the other. The quantitative error uses the pinned PR146 proof;
the exact finite comparison and a counterexample are newly formalized.

For canonical `q=113`, the repaired upper target is `T(3q)=509`. Both
targets reach 1, but neither visits the other. Their joint predecessor
population is therefore `O(X/sqrt(log X))` on octaves, under the stated
coalescence estimate. This refutes a universal positive-density lower
bound for the proposed repaired pair, even within the convergent basin.
It does not rule out every weaker joint estimate or a different global
construction. [Proof, dependencies, and controls](coupling/PINNED_TARGETS.md).

## Verification boundary

The first checkpoint freshly compiles **nine new Lean modules with 36
distinct printed declaration audits**, and nine distinct prior/dependency
modules with 76 audits, including the full-problem finite-mass consumer.
Only `propext`, `Classical.choice`, and `Quot.sound` occur in the audited
declarations. No complete Collatz proof is claimed by those counts.

Four bounded control scripts are replayed against their complete archived
JSON, in ordinary and optimized Python. They test finite arithmetic and
actual trajectories. Pinned Mathlib and third-party compiled dependencies
are reused; this is fresh project-source compilation, not an independent
LeanChecker run or a cold build of all Mathlib.

[Root reconstruction](../../reports/infinity-20261127/ROOT_FIRST_REVIEW.md) ·
[Source-bound replay record](../../reports/infinity-20261127/FIRST_REPLAY.json) ·
[Control manifest](../../reports/infinity-20261127/CONTROL_MODULES.json).
