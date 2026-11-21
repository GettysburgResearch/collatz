# Independent review of fractional Green moments

Reviewer: the discrete-closure research lane, independent of the mass-lane
author. Review date: 2026-11-21.

Reviewed source:
`research/reframe-20261121/GREEN_FRACTIONAL_MOMENTS.md`, SHA-256
`b54169b4ee8f2530688984d9816872eebff88cc668a34710506bbc4ad7caaf6b`.

**Verdict:** no mathematical gap found in GF1, GF2, or the stated distinction
between compact Haar conclusions and ordinary sampling. This is a paper-proof
review, not a Lean check. The note does not resolve the ordinary eventual
column inequality or Collatz.

## Exact inverse-word domains

Each map `R_a(u)=(3u+1)/2^a` takes ternary units to ternary units. Its
composition along a length-`q` word is affine with coefficient
`3^q/2^A`, and therefore scales additive Haar measure by `3^(−q)`.
The normalization to the unit space cancels on the domain and image, giving
`mu(E_w)=3^(−q)` exactly.

The image `E_w` is also the full legal domain for the corresponding inverse
word. An intermediate-domain condition is not missing: if the starting point
is an image under the composition, the inverse intermediate values are the
remaining forward compositions of a unit. The order of composition agrees
with expanding the stated inverse operator. Different word domains may
overlap, but the subadditivity calculation does not require disjointness.

The coefficient sum at fixed depth is finite. Each domain indicator is
clopen, so the asserted bounded continuity of each finite-depth column is
justified by uniform convergence of its nonnegative word expansion.

## GF1: the exact moment threshold

For `0<eta<1`, subadditivity and the exact domain measures give

\[
\int F_q^\eta\,d\mu\le
\left(\frac{3^{2\eta-1}}{2^{2\eta}-1}\right)^q.
\]

For `beta=2eta` in `(1,2)`, strict concavity of `x^(beta−1)` at the
midpoint of one and three gives `2^beta>1+3^(beta−1)`. Hence the geometric
factor is strictly below one throughout the claimed interval
`1/2<eta<1`. A second application of subadditivity bounds the Green
moment by the geometric sum. Since `G>=1`, this supplies every positive
moment below one, including exponents at or below one half.

Without subadditivity, integration of the word expansion gives
`integral(F_q)=1` at every depth. Tonelli therefore makes the first moment
of `G` infinite. All higher positive moments are also infinite because
`G>=1`. The stated threshold is exact, and the fractional Markov tail
bound follows with the displayed constant.

## GF2: no nonzero integrable superharmonic density

The branch Jacobian `1/3` gives `integral(P_2 f)=integral(f)` for every
nonnegative measurable function. This defines a positive mass-preserving
operator on nonnegative `L^1` classes: null sets remain null under the
branches, and an integrable input has an integrable image.

The fractional estimate makes `F_q=P_2^q1` tend to zero in measure. For
an arbitrary nonnegative integrable `f`, split it into `min(f,M)` and its
nonnegative tail. The bounded part is dominated by `M F_q`, while the
tail's `L^1` norm is preserved. Markov's inequality followed by first
`q→infinity` and then `M→infinity` gives `P_2^q f→0` in measure.

If `P_2f<=f` almost everywhere, equality of integrals forces equality
almost everywhere. Iteration gives `P_2^qf=f`, so convergence in measure
forces `f=0`. Applying this to the integrable function `G^theta>=1`,
for `0<theta<1`, proves that its superharmonic inequality fails on a set
of positive Haar measure. This is consistent with mass preservation:
convergence in measure is not asserted to be convergence in `L^1`.

## Ordinary histories and the remaining transfer

For a positive odd ordinary target, every legal compact inverse branch
produces a positive odd integer, with exactly the prescribed valuation:
`3n+1=2^a t` and odd `t` force `v_2(3n+1)=a`. The unit guard is precisely
the required source restriction. A given ordinary source and fixed depth
have a unique valuation word because the forward map is deterministic.
Thus the word expansion counts each actual length-`q` inverse history
once, and F10's equality with the ordinary Green values is sound.

This pointwise equality does not identify ordinary sampling with Haar
integration. The ordinary targets form a countable null set, while the
all-depth Green function is unbounded and can be infinite at exceptional
ternary points. Positive-measure failure of the compact inequality cannot
be transferred to sufficiently large ordinary targets merely by density.

F11 is a precise sufficient additional sampling assertion. Its right side
is finite and positive by GF1, GF2, and mass preservation. Every term on
its ordinary left side is finite: at ordinary targets, `G` is finite by the
credited first-hit/cycle bound, and `G^theta<=G` with `P_2G=G−1` bounds the
incoming compressed value. Consequently an eventual ordinary contraction
would leave only finitely many finite positive terms and force that
average to zero. Proving F11 would contradict such a contraction.

The note correctly leaves F11 unproved. Compact fractional moments alone
do not give the required control of unbounded Green tails under ordinary
sampling.
