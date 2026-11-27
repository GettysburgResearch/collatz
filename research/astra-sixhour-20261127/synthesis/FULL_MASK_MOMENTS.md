# Every fixed individual absolute moment misses the full-mask threshold

**Written method boundary with an exact finite certificate.** This concerns
the full unweighted three-layer physical path family used in
[the bounded-source count](../arithmetic/PHYSICAL_STRIP_TRANSFER.md).
It does not exclude a hypothetical cycle, and it does not rule out a count
using the original source's additional constraints or a joint transform of
several segments.

The new fifth-moment theorem on PR200 crosses the cubic threshold for the
complete two-layer family and a very small third-layer extension. Its true
one-variable phase process is a useful improvement over separate even
moments. The full physical mask here has a larger population. The following
calculation shows that changing the individual moment order, including to
a noninteger order, cannot by itself extend that theorem to this mask.
[PR200 fifth-moment source reduction](https://github.com/GettysburgResearch/collatz/blob/df2f17a117bea06bb34040a5a97e7dc9711d9871/research/six-hour-20261127/cycles/FIFTH_MOMENT_SOURCE_REDUCTION.md)
and [its two-layer even-moment boundary](https://github.com/GettysburgResearch/collatz/blob/df2f17a117bea06bb34040a5a97e7dc9711d9871/research/six-hour-20261127/cycles/ALL_EVEN_MOMENT_BARRIER.md).

## The ordinary polynomial and the claim

Put `lambda=log_2 3`. At mechanical slope `theta` near `lambda`, intercept
`phi`, and `M_i=floor(phi+i theta)`, let `beta_i=M_(i+1)-M_i`.
The allowed layers satisfy `0<=k_i<=3-beta_i`, and the physical odd
exponent is `beta_i+k_i-k_(i+1)` in `{1,2}`. Fix the entrance and exit
layers of a segment with `a` odd departures. Its actual native dates are
`r_i=M_i-M_0+k_0-k_i`, and its ordinary numerator is

\[
 B=\sum_{i<a}3^{a-1-i}2^{r_i},\qquad
 F(v)=\sum_{\text{all allowed paths}}e^{2\pi i Bv}.
\]

For every fixed real `q>1`, uniformly in these cuts and intercepts, in the
joint limit `a -> infinity`, `theta -> lambda` from the physical side,

\[
 \liminf \frac{1}{a\log 3}\log\int_0^1|F(v)|^q\,dv
 \ \ge\ (q-1)\left(\frac13+\frac1{30000}\right).                 \tag{1}
\]

The finite inequalities below are strict, so the same conclusion with a
slightly smaller margin holds eventually in a fixed sufficiently small
slope neighborhood, for each fixed `q`. The quantified theorem is the
displayed joint-limit statement. No statement uniform as `q` tends to
infinity with `a` is needed or made.

## Two lower certificates and the earlier upper certificate

Let `N` be the number of paths with the specified cut layers. The exact
512-letter transfer evaluates all 514 phase schedules and all 2,908
entrance/exit choices. Every population is at least

```
40147753876380311573194241879795457186244128421394423838115747841191113008228631422917890827637213580303644006980629
```

and this integer to the hundredth power exceeds `3^(47*512)`.
Concatenating blocks with prescribed common boundary layers gives

\[
 \liminf \frac{\log N}{a\log3}\ge\frac{47}{100}.
\]

For the second transfer, keep four ordered paths whose two positive layers
and two negative layers have the same unordered pair at every date.
Then their digit sums, and hence their two sums of ordinary numerators,
are equal. The transfer has 15 states at a three-layer site and six at
a two-layer site; every transition has its literal ordered multiplicity.
All four entrance layers and all four exit layers are fixed to the
specified segment cuts. Every such 512-letter count is at least

```
23533249183800008423443746217722129485866705158238321409183032547063269145213677706199582199833979106580725697241364487866520105157360004590009947308628459672831157871612755451678634821121522640130383841103765583866332486086898230958604405926120218925769198327338871317
```

and its hundredth power exceeds `3^(109*512)`. These are a subset of the
ordinary four-sum collisions. Concatenation therefore gives

\[
 \liminf\frac1{a\log3}\log\int|F|^4\ge\frac{109}{100}.           \tag{2}
\]

An initial incomplete block can be taken identically in all four copies.
Every allowed starting layer has a continuation. The last complete
512-letter block connects every prescribed pair of cut layers, as the
strictly positive minimum verifies. Thus the incomplete part costs only
a bounded factor, independently of the intercept. All finite phase
arrangements remain unchanged in a neighborhood of the irrational slope.

The earlier 256-letter [rank population certificate](../arithmetic/RANK_SPACING.md)
gives, in the same joint limit,

\[
 \limsup\frac{\log N}{a\log3}\le\frac{12}{25}.
\]

The new checker independently enumerates literal eight-letter paths,
groups every ordered pair by its complete sequence of unordered layer
pairs, and compares the squared signature populations with the transfer.
It also checks the population transfer against that enumeration. All
tests remain active under Python optimization.
[Exact checker](check_moment_barrier.py) ·
[Complete output](../../../reports/astra-sixhour-20261127/synthesis/moment_barrier.json).

## The inequalities for every real moment

For these fixed cuts all native words have the same duration and odd count.
The ordinary numerator determines such a word: its lowest two-adic term
determines the first odd position, and subtraction and induction determine
the rest. Thus its coefficients are zero or one, `integral |F|^2=N`, and
`sup |F|=N`. Define the normalized lower logarithmic moment rate by `L(q)`.
The preceding certificates imply the following elementary bounds:

\[
\begin{array}{ll}
 L(q)\ge\frac{47}{100}(q-1),&1<q\le2,\\
 L(q)\ge\frac{47}{200}q,&q\ge2,\\
 L(q)\ge\frac{109}{100}-\frac{12}{25}(4-q),&1<q\le4,\\
 L(q)\ge\frac{109}{400}q,&q\ge4.
\end{array}                                                       \tag{3}
\]

The first and third use `|F|<=N`, and the second and fourth use monotonicity
of the probability-space `L^q` norm. All of these apply to the ordinary
one-variable polynomial; an auxiliary independent phase law is not used.

There is also the near-zero-frequency bound

\[
                            L(q)\ge\frac{47}{100}q-1.                \tag{4}
\]

Indeed the numerator degree is at most `C a 2^(theta a)` on the physical
side. In an interval of length a fixed constant divided by this degree,
all summands have positive real part at least one half. Its contribution
to the integral is at least a constant depending on `q` times
`N^q/(a 2^(theta a))`. Taking the joint limit proves (4).

Use respectively the first bound of (3) on `(1,2]`, the second on
`[2,61/18]`, the third on `[61/18,4]`, the fourth on `[4,5]`, and (4)
on `[5,infinity)`. Each exceeds or equals the right side of (1).
The narrow joining point is intentional: before adding the margin, the
second bound exceeds `(q-1)/3` there by exactly `1/10800`.
The checker verifies every affine endpoint and the infinite-tail slope.
[MomentBarrier.lean](MomentBarrier.lean) additionally proves the rational
piecewise envelope and its strict separation from the cubic threshold.
It does not formalize the Fourier or infinite transfer arguments.

## What the boundary does and does not say

In the usual architecture of `r` comparably long independent conditioned
segments, Holder orders `q_j>1` obey `sum 1/q_j=1`. Paying the individual
moment norms with (1) costs at least the exponential rate

\[
 \sum_j\frac{q_j-1}{q_j}
       \left(\frac13+\frac1{30000}\right)
   =(r-1)\left(\frac13+\frac1{30000}\right).
\]

The source interval in this architecture has logarithmic size proportional
to `(r-1)` segment lengths. These individual unweighted norms therefore
cannot supply an exponent below one third for the full mask. This is a
limitation of that estimate, not a lower bound on the true joint
convolution atom. It leaves the exact common-frequency product open.
It also leaves a smaller positively specified family open, such as paths
satisfying the original integer source's carried inverse-rival constraints.
One cannot simply delete paths after bounding an odd absolute moment:
such moments are not monotone under arbitrary coefficient deletion.

The fifth-moment certificate on the genuinely smaller two-layer family
is fully compatible with (1). This pass uses its published statement and
reads its reduction; it does not claim to have rebuilt that external
angular certificate.
