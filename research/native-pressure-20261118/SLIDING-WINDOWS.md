# Diffusive window statistics and longest inverse drawdowns

Write a_i,S_q,X_q for the exponents, their sums and the odd states of
a fixed-root canonical inverse path. All conclusions below hold almost
surely for every fixed positive odd unit root, using the two-shell
short logarithmic source comparison. They describe fluctuations seen
across many starting positions of a single path.

[Two-shell source transfer](REAL-TAILS.md) · [All-depth growth](ITERATED-LOG-BOUND.md).

## Empirical Brownian windows

For every integer choice m=m(q) with m→∞ and m log q/q→0, draw a
starting position i uniformly from [q,2q) on the realized path. The
conditional law of the polygonal curve with values

    (S_(i+k)−S_i−2k)/√(2m),        at times k/m, 0≤k≤m,

converges weakly on C[0,1] to standard Brownian motion. The same law
holds on replacing the numerator by
(log X_(i+k)−log X_i−k log(4/3))/log 2. In particular the relative
empirical distribution of the centered end increments converges to
the standard Gaussian. These conclusions concern uniform positions
on one path and do not assert a marginal CLT at a prescribed root and
single depth.

For proof fix a bounded continuous test of the curve. On a reversed
iid proxy word the test on any m consecutive letters has mean tending
to the Brownian test mean by the iid functional CLT (geometric variance
two). In any interval of at least ηL origins, where L is the geometric
log-height shell scale and η>0 is fixed, separate the starts by residue
modulo m. Eligible windows in any one class are disjoint. For m≤L/(D log
L) Hoeffding and a union over the m classes give failure probability at
most O(m exp(−c η ε² L/m)) for an ε-error in their combined
average, with the constant depending on the test bound. Union over all
O(L²) interval locations and lengths and O(L) choices of m remains
O(L^(−2)) for sufficiently large fixed D=D(η,ε,test). Only intervals
whose windows fit into the proxy are counted. The extra outer shell
gives the entire required lookahead for inner-shell starts. The
two-shell comparison transfers this simultaneous good condition with
summable error along the geometric L scales. As in that comparison,
the good property of the whole iid list suffices for every possible
subsegment between the actual source's landing times.

The depths n_j of the shell endpoints satisfy n_j∼L_j/ℓ with adjacent
gaps comparable to L_j, ℓ=log(4/3). Hence [q,2q) meets a bounded
number of comparable shells. Discard pieces of relative length below
η, apply the good condition on the rest, and let η,ε decrease through
positive rationals. Since D is fixed at each such step, every choice
m log q/q→0 is covered. Intersect over a countable convergence-
determining family of bounded continuous tests on the path space.
Finally the discrepancy between the physical numerator and the
valuation numerator is bounded by a constant times
Σ_(i≥q)1/X_i=o(1), by positive exponential growth. This proves the
physical version.

## Erdős–Rényi extremes at logarithmic depth

For x≥1 define the geometric rate function

    I(x)=x log 2+(x−1)log(x−1)−x log x,        0 log 0=0.

For c>0 let x_+(c)>2 solve c I(x)=1. Let x_−(c)=1 when c log 2≤1,
and otherwise let it be the solution in (1,2) of the same equation.
For m=⌊c log q⌋, the maximum and minimum of (S_(i+m)−S_i)/m over
q≤i<2q converge to x_+(c) and x_−(c), respectively. In particular
the longest net drawdown in physical inverse height satisfies

    max {m≥1 : ∃ i∈[q,2q), X_(i+m)≤X_i} / log q
        → 1/I(log₂3).

To see the scanning law, optimize the geometric moment generating
function e^θ/(2−e^θ) to obtain I. A one-sided deviation to any
strict outer threshold at distance from the relevant extremum has
probability at most exp(−m I(x)). The union over O(L) origins on a
two-shell proxy is summably unlikely when cI(x)>1. Here log q differs
from log L by a bounded amount in every participating shell; a union
over the resulting bounded number of lengths costs a fixed factor.
For any strict inner threshold on the same side of two with cI(x)<1,
the corresponding iid tail has probability at least
exp(−m(I(x)+o(1))), by an exponential tilt just past x or the geometric
sum's exact negative-binomial mass and Stirling's formula. Each interval
of ηL origins contains order L/log L independent disjoint trials.
The failure probability tends to zero faster than any power of L,
also after union over interval locations. The transfer therefore gives
both extremal bounds, taking rational threshold limits. When the
lower endpoint equals one, only its upper approximation is needed.
The simultaneous assertion for all real c may be obtained from positive
rational c by monotonicity of the unnormalized extrema in m and
continuity of x_±.

For the drawdown upper bound, at positive growing depths the summed
affine correction over any forward-length inverse block is o(1),
uniformly, since Σ_(i≥q)1/X_i=o(1). Thus a drawdown requires
average exponent at most log₂3+o(1). Fix c>1/I(log₂3) and then
a slightly increased threshold x<2 with cI(x)>1. Summing the
Chernoff bound over all m≥c log q contained in the two-shell word
costs only a geometric factor beyond its first term. For m larger
than a fixed small fraction of i, so possibly extending beyond that
word, the global SLLN gives mean 2+o(1) uniformly. Shorter windows
all fit by the spare outer shell. This excludes all such drawdowns.
Conversely for c<1/I(log₂3) choose x<log₂3 with cI(x)<1. The lower
scanning estimate yields a length-⌊c log q⌋ window with mean below
log₂3, which is a genuine physical drawdown. Taking limits proves
the formula.
