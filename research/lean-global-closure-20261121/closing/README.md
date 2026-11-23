# Four direct attacks after the whole-repository refresh

**Full Collatz remains OPEN.** This checkpoint attacks universal source
descent, ordinary escape and arbitrary positive cycles. It obtains the
exact deductions below, but no argument closes all counterexamples.

The repository pass inventoried all **145 open and closed PRs** by updated
time, retaining older PRs with newer commits. The scientific inputs were
read selectively at frozen heads; this is not a claim to have audited every
proof in all 145 PRs. PR180 advanced again during this work, to
`5e29f56f6d44669a8aa9134e5617b78d65c074c2`; its new source surgery and
weighted routing were incorporated before publication. The complete
[inventory](../../../reports/lean-global-closure-20261121/nov22/closing/REPOSITORY_SNAPSHOT.json)
and [late refresh](../../../reports/lean-global-closure-20261121/nov22/closing/LATE_REFRESH.json)
record that distinction.

## 1. Arbitrary cycles: count the actual zero atom

[The cycle attempt](ZERO_ATOM_CLOSING_ATTEMPT.md) uses every parity word
with length A and p odd steps and the full denominator D=2^A−3^p>0.
If m is the minimum in a positive cycle, the complete product identity
and an elementary product-deficit inequality give

\[
\boxed{D(3m+1)\le p2^A.}
\]

Put M=floor((p2^A−D)/(3D)). Different cycles have different positive
ordinary minima, each at most M. Consequently the exact zero-fiber count
obeys N₀(A,p)≤A·#{m≤M:gcd(m,6)=1}. This holds for arbitrary word
complexity. The existing Matveev specialization makes this a polynomial
bound in A and supplies a complete polynomial-time minimum census in
**numeric A**, with an enormous worst-case degree. This is a deduction
from the classical cycle-minimum/logarithmic-form machinery, not a claim
of a new transcendence theorem.

[CycleMinimum.lean](CycleMinimum.lean) proves the exact finite product
and natural-number minimum inequality from all cycle edge equations and
the full denominator identity. The word bijection, zero-fiber count,
algorithm and Matveev application are written mathematics. Two fresh
source compilations and five axiom audits passed. No Collatz hypothesis
or Matveev theorem was installed as a Lean axiom.

The missing closing improvement is specific: a primitive A-cycle needs
N₀≥A, while the upper bound still permits it. An exponentially small
probability under the word law is not enough; the integer multiplicity
must fall below A.

## 2. Descent: allow arbitrarily complicated prefix edits

[The nonlocal repair attempt](NONLOCAL_SURPLUS_REPAIR_ATTEMPT.md) keeps
the original target t, its actual parity suffix, the complete source clock
A and the complete grade. If an edited prefix ends in a positive integer
that can follow the retained suffix to a safe endpoint, then

\[
2^{A-b}\mid x_b-y,\quad x_b>2^{A-b},\quad
5\,2^A<6\,3^{o_b}t,\quad o_b\ge r-2.
\]

Here b is the cut clock and r is the original source's odd count. For
bounded-four source words, b≥A/4−2. The edit may have arbitrary
description complexity; this is not another fixed-language restriction.

The exact record source S=1092 with target t=2047 exposes the attempted
closing failure. Its first integral positive copied-tail repair is at
clock 18, with current target 112103 and repaired state seven. Its
lower-grade powered source 28 only pays up to 57. The imported
all-certificate source maximum 1092 excludes every permitted-grade
completion at the feasible cuts through this source clock. The target
itself later descends, at clock 58; it is not a Collatz counterexample.

The [late source-surgery comparison](LATE_LEGAL_DESCENT_COMPARISON.md)
consumes PR180's further update. Its positive carry still requires the
original interval slack to pay the new source; it does not provide the
missing activation for this attempt.

## 3. Escape potential: preserve the actual stopping mass

[The sibling attempt](UNEQUAL_DEPTH_SIBLING_ATTEMPT.md) allows paired
inverse words to have different depths and keeps their exact critical
weights. The endpoint ratio, rather than congruence legality alone,
controls whether the transport carries enough mass.

On a stipulated escaping ordinary orbit q_k, almost all of every
high-payoff stopping antichain must eventually pass one late fixed
anchor q_K. This statement is proved for the actual **payoff measure**,
not just an auxiliary path probability. It implies the witness-depth
bound

\[
\boxed{V^{[r]}(q_k)\ge\eta q_k\quad\Longrightarrow\quad
 r\ge k-K_\eta.}
\]

This directly consumes the freshest weighted-routing estimate in PR180:
the common-precision transplant's remaining 3^(−r−1) coefficient is
exponentially small in k on these witnesses. That bounds this proposed
lower certificate; it is **not** an upper bound on true sibling mass.
The required reciprocal endpoint-distortion estimate remains open.
All harmonic, envelope and path-product inputs keep their original
source qualifications.

## 4. Escape entropy: keep the original integer in the approximation

[The fixed-source shadow attempt](FIXED_SOURCE_SHADOW_ENTROPY.md) uses an
actual parity prefix matching uv^∞ through L bits. With a=|u|,
N=|u|+|v|, and the original source x₀, its exact rational-shadow
numerator satisfies

\[
Dx_0-Z=2^N(x_a-x_N).
\]

For a nonperiodic source this is nonzero and divisible by 2^L. Hence

\[
\boxed{L\le N+\log_2\!\left(1+\max_{j\le N}x_j\right).}
\]

This would exclude sufficiently strong actual repetition. The latest
time-law entropy ceiling supplies neither that repetition nor the fixed
local factor-complexity bound needed by the inspected Subspace-theorem
route. A written two-rotation symbolic control tests the proposed
entropy-to-repetition implication. It is explicitly not an ordinary
Collatz orbit and not a realization of every compact-joining property.

## Evidence and boundaries

- [Formal build and finite-control evidence](../../../reports/lean-global-closure-20261121/nov22/closing/VALIDATION.md).
- [Independent cycle review](../../../reports/lean-global-closure-20261121/nov22/closing/REVIEW_ZERO_ATOM_CLOSING_ATTEMPT.md).
- [Independent fixed-source review](../../../reports/lean-global-closure-20261121/nov22/closing/REVIEW_FIXED_SOURCE_SHADOW_ENTROPY.md).
- [Integration reviews and exact scope](../../../reports/lean-global-closure-20261121/nov22/closing/INTEGRATION_REVIEWS.md).

The new cycle census matched direct enumeration at all 99 positive-
denominator parameter pairs with 1≤A≤18, covering 453,148 words. A
separate complete (27,17) residue-law control covered 8,436,285 words.
Those finite controls validate the implementation and the stated example;
the written proof owns the all-parameter deductions.

The prior Lean corpus was not rebuilt. The new formal module and its audit
are the only project sources freshly compiled in this checkpoint. The
required repository-integrity validator is run separately in a clean
complete checkout of the exact proposed commit, with its receipt bound
in the PR description. Repository integrity does not certify mathematics.

The remaining obligations are actual source activation/descent, a
sufficient sibling mass or same-orbit entropy estimate, and an all-word
zero count below the primitive-cycle threshold. None is asserted here.
