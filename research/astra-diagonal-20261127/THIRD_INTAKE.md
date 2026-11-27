# Third live intake: new same-source and cycle machinery

The three new research PRs below were read during the active pass on 27 November
2026 at about 14:15 UTC. The root read each current PR description and packet
README; the assigned mathematical agents then read the relevant detailed notes.
This is a source intake and a comparison of hypotheses, not a fresh independent
validation of the other packets' Lean closures or analytic inputs.

| PR | Observed head | Source packet |
|---|---|---|
| [211](https://github.com/GettysburgResearch/collatz/pull/211) | `0ce0c71c8fe1eabff57aa9b97160147cbc15ab19` | [Reciprocal rigidity](https://github.com/GettysburgResearch/collatz/tree/0ce0c71c8fe1eabff57aa9b97160147cbc15ab19/research/astra-reciprocal-rigidity-20261127) |
| [212](https://github.com/GettysburgResearch/collatz/pull/212) | `8cac31f51d9a5a2bd03c211495dec8f90c2aa48e` | [Infinite descent](https://github.com/GettysburgResearch/collatz/tree/8cac31f51d9a5a2bd03c211495dec8f90c2aa48e/research/astra-infinite-descent-20261127) |
| [213](https://github.com/GettysburgResearch/collatz/pull/213) | `de6384b4a232b996add4f5c620929d06a1982e90` | [Diagonal frontier](https://github.com/GettysburgResearch/collatz/tree/de6384b4a232b996add4f5c620929d06a1982e90/research/astra-diagonal-frontier-20261127) |

## Ordinary source and physical clocks

PR212 supplies first-hit pairs of ordinary positive integers with a prescribed
fixed gap, in every sufficiently large fixed relative window, with a common
clock and common odd-step count. This gives actual witnesses with quantitative
costs. It does not prescribe one previously supplied source or the side branch
at that source's own moving clock. Our [ordinary competitor-word theorem](global/ORDINARY_COMPETITOR_WORDS.md)
shows why one natural attempt to force that identification loses weight:
competitors sharing all but a sublinear head and tail have exponentially small
relative total weight. Allowing fewer than a specified logarithmic number of
scattered exponent edits also gives a negligible total weight.

PR213 strengthens first-landing localization to shrinking relative windows and
growing binary precision. In its notation, the residual height parameter is
`R = log₂(X/M)`, the relative window may be as small as `R^(-1/9)`, and the
allowed binary precision is proportional to `R`. When one tries to specify the
smaller source through a large power-of-two lift, the residual height parameter
still depends on that smaller source. Arbitrarily increasing the lift does not
pin a previously supplied positive integer. Our new [mesoscopic ancestor law](global/MESOSCOPIC_ANCESTOR_LAW.md)
instead works directly with the genuine positive ancestors and gives a uniform
relative lower bound on every initial binary–ternary cell at sublinear
precision. Its precision is measured against the overshoot past the original
seed, so it also leaves the same-depth sibling estimate open.

The no-return entrance probabilities and permanent-entry laws in PR213 have
their source-qualified analytic inputs stated in that packet. The stronger
density bound there is retained with its stated external-review boundary.
It is not silently used as a fully formalized result here.

## Ordered cycles

PR211 gives complete-denominator, all-shift merger costs and a restriction on
nearby rotation shifts. PR212 constructs positive rational cycles with nearly
one-octave spread and subexponential complete denominator. The latter are a
useful calibration: a small rational denominator is not denominator one.
PR213 supplies all-cut rotation information and finite parallel ordinary paths
that reverse higher differences. Such paths do not automatically form a
single periodic orbit.

Our [short midpoint theorem](arithmetic/SHORT_RANK_MIDPOINTS.md) retains one
actual integer cycle in the bounded least-tripling-disagreement alternative.
Its new assertion is exact exponential orientation for every sufficiently
short pair of rank spacings, at every origin. The adjacent convexity statement
alone was already established in [PR201 at its earlier pinned head](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md).
Our high-return cone gives an alternate proof of that adjacent statement and
extends it to both signs and unequal spacings. No nontrivial integer-cycle
exclusion follows yet from the resulting Fourier inequalities.

## Positive invariant currents

The [finite record current](escape/FINITE_RECORD_CURRENT.md) uses actual
permanent minima of a hypothetical escaping ordinary component. The
[positive-real transverse construction](escape/CRITICAL_POSITIVE_REAL_TRANSVERSE.md)
then gives a finite invariant law for the quadratic first-record operator,
with finite first real moment and a positive ordinary binary fibre. Its
real–ternary projection is absolutely continuous. This is an equivalent
representation of escape, not an impossibility theorem. In particular its
first-moment projection has infinite integral against the stationary
first-power harmonic function. Integrating that function as though the
integral were finite would create a false contradiction.

No new intake closes the ordinary same-depth comparison, the original
occupation endpoint lower bound, or the full integer-cycle exclusion. Those
remain the targets of the continuing pass.
