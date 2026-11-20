# Independent reconstruction of the arithmetic moment criteria

Reviewer scope: `MOMENT_QUANTILES.md` at SHA-256
`178522c6954683f35730cc2da9b9d3aa49acf14dce59677880ded167691f0226`.
Reviewed claims: MQ1--MQ5; BC, NC, QC, PC; the pointwise-premise implication;
the intermittent-spike example; and the exclusion of periodic cycles from
these conclusions. This is mathematical internal review of that text, not
formal verification, independent publication review, or a verdict on future
edits. The numerical moment checker is not covered by this review.

## Source dependency reconstructed

I read PR153 at `eb04a5d79020cefa0ba46794095b5766c5ff66a4`,
`research/fixed-integer-descent/drift.md`, particularly FID-DRIFT-001/002/005.
The translated-interval proof uses injectivity of future values within one
finite simple path, a parity-cylinder count for high odd weights, and a
smaller-interval recursion for the low-weight images. The terminal correction,
integer-interval alignment, and strict smaller-width induction are retained.
This indeed yields a path-independent occupancy constant for every exponent
strictly above the stated entropy threshold.

I separately executed the four integer comparisons used for the advertised
`19/20` and explicit `29/30` exponents. All were true:

- `3**200 < 2**317`;
- `317**6340 < 2**6023 * 200**4000 * 117**2340`;
- `3**1170 < 2**1856`;
- `2**9664 < 39**1170 * 25**750`.

No uncomputed numerical value of `C_(19/20)` is needed. The constant 10 is
used only at exponent `29/30`.

## Narrow verdicts

| Claim | Verdict | Reconstruction |
|---|---|---|
| MQ1 | VERIFIED | Full numerator integrality forces every ordinary division and odd intermediate value. A negative odd starting representative cannot reach the positive final representative, so the chosen representative is positive. This gives the full source-cylinder partition. Summing the `k≥1` tails gives strictly less than `(1/2)(3/5)^q`, using `sum k^-2<2` and `sum_w J_w^4=(27/5)^q`. |
| MQ2 | VERIFIED | Occupancy on one nonperiodic orbit bounds its reciprocal sum and therefore its multiplicative correction `I_q≤M`. The single fixed original source contributes `J_q^4/n_q^2=n_q^2/(n_0^4 I_q^4)` to the global positive moment. The inequality direction is correct. |
| MQ3 | VERIFIED | Sorting the `N` distinct states at any selected times gives `y_j≥(j/C)^(1/alpha)`. Their inverse alpha powers have sum at most `C H_N`; MQ2 supplies precisely the stated source-dependent multiplier. |
| MQ4 | VERIFIED | Every time with `Q_q≤Y` has its distinct state below `n_0^2 M^2 sqrt(Y)`. Occupancy bounds even an initially infinite set of candidate times, by applying the finite bound to every finite subcollection. |
| MQ5 | VERIFIED | Sorting chronological states and summing the lower bounds on their squares gives the exponent `1+2/alpha` and the stated denominator `1+2/alpha`. |
| BC | VERIFIED | A nonperiodic deterministic positive-integer orbit has no repeated state, hence eventually leaves every finite set. MQ2 forces `Q_q→infinity`; since `Q_q−P_q→0`, it forces `P_q→infinity`. A bounded cofinal subsequence contradicts this. |
| NC, QC, PC | VERIFIED | Each contradicts the respective finite, fixed-source necessary upper/lower bound. The bounded cumulative correction `sum(Q_q−P_q)=3/4` does not affect PC. |
| Pointwise premise implies NC | VERIFIED | If `P_q=o(q^(40/19))`, then `q Q_q^(-19/40)→infinity`; its harmonic averages diverge. |
| Spike example | VERIFIED | At square times `q=j^2`, the negative power is `j^-1/2`, whose sum up to `sqrt(N)` grows at least as `N^(1/4)` up to the displayed integer rounding. Exponential nonsquare values violate the old pointwise premise and PC. This is properly labeled a comparison sequence. |
| Cycle boundary | VERIFIED | Repeated times cannot be counted using distinct-state occupancy, and the product `I_q` is not bounded along a positive periodic orbit. No cycle exclusion follows here. |

The explicit constant in MQ3 is also correct:
for `alpha=29/30,C=10`, `M=exp(100)` and
`C M^(2alpha)=10 exp(580/3)`.

## A useful additional hierarchy

The presentation does not need a hierarchy, but one can strengthen its
organization: **QC is implied by each of BC, NC, and PC.** Thus QC is a single
sufficient closing target encompassing the other three tests.

Write `s=alpha/2`. Suppose QC fails, so the counting function

`N(Y)=#{q≥1: Q_q≤Y}`

obeys `N(Y)≤K Y^s` for all `Y≥1`, for some finite `K`. There are only finitely
many positive `Q_q<1`; their minimum is positive. Enlarging the constant to
`K'` therefore gives `N(Y)≤K' Y^s` for every `Y>0`.

Order any finite `N` distinct indices by their moment values, writing
`Q_(1)≤...≤Q_(N)`. The count bound gives

`Q_(j)≥(j/K')^(1/s)`.

Consequently

`sum Q_(j)^(-s) ≤ K' H_N`,

so NC fails. Also

`sum Q_(j) ≥ (K')^(-1/s) N^(1+1/s)/(1+1/s)`,

so PC fails, including after removing the bounded total correction from
`Q` to `P`. Finally BC supplies infinitely many values of `Q_q` below one
fixed finite bound, and directly implies QC.

This is an elementary relation between the stated arithmetic tests, not a
proof of QC for the actual moment sequence. It may be added to the proof
packet, with the finite-small-value qualification above, if useful.

## Remaining debt

The source-qualified occupancy theorem and all algebraic deductions in scope
survive reconstruction. None supplies an actual upper or quantile estimate
for the sequence `P_q`. Proving QC (or a sufficient special case) remains an
open infinite arithmetic task. Positive-cycle exclusion is separately still
required for full Collatz. These are the exact limits of the verdict.

## Final-body addendum

A second complete read of the final body, including the QC hierarchy,
finite-count version of QC, bounded-liminf discussion, and new enclosure
section, was performed. The final body has SHA-256 `178522c6954683f35730cc2da9b9d3aa49acf14dce59677880ded167691f0226`
(length 14,241 bytes). The original scoped review above remains preserved.
This addendum explicitly covers the final wording of the added sections.

- The QC hierarchy is VERIFIED by the argument in this review. The final
  version retains the finite `Q_q<1` adjustment needed to extend the
  counting bound to all positive thresholds.
- The finite-count reformulation is VERIFIED: taking the supremum over
  finite initial windows recovers the full cardinality, including an
  infinite count. The two suprema can be interchanged for nonnegative
  quantities.
- The bounded-liminf corollary BC is VERIFIED: the fixed original source
  forces `P_q→infinity` if its orbit is nonperiodic; a cofinal bounded
  subsequence is contradictory. BC still says nothing about cycles.
- The enclosure derivation is VERIFIED. The full recurrence row mass is
  at most `27/5`, and its tail beyond exponent `A` is at most
  `(27/5)16^-A`. Induction bounds the supremum vector error by
  `q(27/5)^q16^-A`; summing endpoint weights gives the stated error less
  than `2q(27/5)^q16^-A`. Flooring each of `3^q` terms at scale `10^18`
  adds at most `3^q/10^18` to the upper enclosure. No infinite exponent
  tail is dropped without a bound.
- The five displayed numeric rows were compared to the retained normal
  report and match it. This is a report comparison, not a separate complete
  execution of the numerical recurrence or a proof of an asymptotic trend.

No broader acceptance is implied by these narrow verdicts.
