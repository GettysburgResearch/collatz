# Independent review of the permanent sieve and ternary decoder

**Verdict: verified as written implications, conditional on the named
source results.** Inspected the two texts at these SHA-256 digests.

| Source under research/six-hour-20261127/escape | SHA-256 |
|---|---|
| PERMANENT_SIEVE.md | 95642b16cb20e7b24957df270c6850b02745852add7b3c331c5076effd845e9a |
| TERNARY_DECODER.md | e096e81b3d3aa8c07cdb006d1cf9c3eb70ca4d7552651c21b9a9426266c6fce4 |

## Positive ordinary mass

PR193, commit 25f5462e2c43feea65760884f7ea8f53576fbc18,
research/astra-unconventional-20261126/global/COLLISION_ENERGY.md,
uses the complete system of positive odd representatives below $2\,3^k$.
Its (2) bounds the first moment on precisely that system. Its (3)
states the uniform-in-clock error along one ordinary ray and initially
gives only Cesàro convergence on the negative-lag side. The section
following (6) also proves the pointwise negative-lag limit using the
fixed-target ordinary-depth limit. This stronger conclusion **is** in
the pinned source. The positive-lag limit handles the arbitrarily many
sites that could come back below the cutoff after clock $k+J$. Their
maximum first-hit value tends to zero with $J$, so one factor of the
clipped square pays that maximum and the remaining factor costs $O(k)$.
Before clock $k$, the complete initial ray segment fits under the physical
cutoff for all large $k$. Summing the absolute error there costs $o(k)$
by the lag limits and the Lipschitz bound. On the complement of a
finite union of rays and their finite transient ends, the inherited
small-source exclusion pays a uniform negative power of the source
cutoff in the same first-moment argument. The corresponding omitted ray
amplitudes have summable clipped mass. At any fixed finite collection
of components, replacing chosen starts by the actual coalescing rays
changes only $O(1)$ sites per component. PR193 (8) removes periodic
lap mass in normalized first norm, which suffices before applying any
bounded mark. This reconstructs the asserted pointwise-measure
total-variation statement. The upstream first-hit estimates and ordinary
limit law remain named dependencies.

On each ray $B_i=bi-A_i$ goes to positive infinity at least linearly.
The infimum of each tail is attained even for irrational $b$, because
only finitely many terms can be below any fixed level. A strict increase
of successive tail minima forces the earlier term itself to realize the
minimum. The rise is at most $b-1$. Telescoping gives the advertised
lower density for the set that passes **all future tests at once**.
Every $K_b(m(k))$ contains that same set, including when $m(k)$ is
infinite. Combining finitely many rays and then summable exhaustion
avoids any onset uniformity across rays. The Haar cylinder cost uses
a different measure. Its exponential estimate follows directly by
minimizing $s^{-b}s/(2-s)$ on $0<s<1$. An infinite-depth site test
in the theorem is a mathematical predicate and is not a finite decision
procedure.

## Entropy, the genuine word, and limiting tables

PR200, commit ad70a3b831867cb8a74d402a2a1abdc419f5a09b,
research/unconventional-20261126/operator/EXACT_BERGMAN_PRESSURE.md,
states equation (4) for each stationary ergodic *Markov* law of legal
inverse edges with finite mean exponent. It is stronger than its
pressure-radius numerical conclusion. The output directions in the
decoder match the source. For a selected uniform position on a fixed
ordinary ray, each translated finite window is tight by truncating
labels and using the slope bound for the prefix ending at $k+O(1)$.
Discarding finitely many positions at the ends makes its limit stationary.
Fatou through truncation gives the finite mean. Finite ray exhaustion
and the summable amplitudes give tightness after the mixture is formed.

Constructing a Markov extension of the one-edge law preserves the
state marginal and the conditional probabilities on the actual
labelled edges. Its ergodic components retain the kernel because every
invariant event is measurable modulo null sets in the completed past,
by shifting cylinder approximations into the past. The Markov
conditional law given the past is already the state kernel. On the
positive-branch-entropy components of that extension, full ternary
entropy rate forces zero mass on the nested thin set by the elementary
two-cell entropy bound. On the other components the *same kernel* is
a point mass almost everywhere and its future visits only states with
this property. Restricted to that latter set, equality of **one-edge**
laws suffices to recover all finite words in the original process:
at each time a wrong deterministic edge is a null event. A countable
union covers every finite word. No higher-order Markov assumption
on the original stationary limit is needed.

The finite word labels are a countable discrete space. An error
integral for a fixed table on a finite digit partition is bounded and
continuous. Its infimum over tables is upper semicontinuous, and
refining the digits while shrinking the tested set can only decrease
the optimum. For each limiting law, measurable deterministic labels can
be approximated in measure by finite cylinder tables after truncating
the countable word alphabet. The compact family of probability-law
limits permits the closed-superlevel argument. For a fixed $d$,
upper semicontinuity then bounds the limsup along the original
sequence by the supremum over that compact family. This order of
operations permits data-dependent tables. On the mass side the strict
upper records of $B_i$ give the backwards inequalities through
depth $i$. Discarding $O(d+r)$ sites justifies fixed or sublinear
$d$; this is a different conclusion from the arbitrary-depth forward
test.

This review reconstructs the deductions at the two hashes and checks
the hypotheses and orientation of the upstream results. It does not
rebuild the upstream formalizations or independently prove the
entropy-gain theorem in PR200. The first unsupported closing step is
still a vanishing measured sieve mass, or a positive irreducible
prediction error on this same clipped mass under escape. Neither is
a consequence of ambient Haar rarity or of the Markov extension.
