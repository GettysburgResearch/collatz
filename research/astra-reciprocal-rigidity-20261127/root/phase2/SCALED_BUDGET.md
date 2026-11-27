# The finite prefix budget survives scaled and postpeak targets

**Proposed proof, with compiler status recorded separately.** The source is
always one positive ordinary integer. All competing starts are positive and
strictly smaller, and their physical clocks are unrestricted. The finite
certificate is the same one from the first checkpoint; no larger convergence
oracle is introduced.

## Scaling the virtual ramp

Let `s` be 0 or 1, let `n>s`, and suppose `3^K` divides `n−s`.
Let `c≥1` be any positive integer. At a target `Y` satisfying

\[
 2^j(Y+1)=3^j c(n+1),
\]

the scaled-ramp theorem excludes every smaller visitor with at most `K+j`
odd departures. The same finite budget strengthens this to more than
`K+j+b` whenever `SmallPrefixBound b L` and the first checkpoint's exact
power margin hold.

Here is the point at which the scale could have caused a problem. Remove
the first `b` odd departures of a proposed smaller visitor, and translate
the remaining prefix to an ordinary positive origin `q`. For a suitable
prefix clock `r` and remaining odd count `k'`, put

\[
 D'=2^r3^{j-k'}c.
\]

The ordinary shifted-height bound and the signed translation give

\[
 z'=q+D'(n-s),\qquad 0\le q<D'(s+1),\qquad
 z'<(3/2)^b n.
\]

Since `n/(n−s)≤2`, these imply `D'<2(3/2)^b` and
`q<4(3/2)^b`, independently of `c`. Thus the scale does not enlarge the
finite set of ordinary origins. The subsequent prefix inequality gains
the extra factor `c≥1` on its stronger side. The original margin therefore
still suffices.

The implementation reuses `translated_origin` with virtual parameters
`N=c(n+1)−1` and `S=c(s+1)−1`. That helper only needs `S≥0`; the
special assumptions `s=0` or `1` are used in the original smaller-source
comparison. This avoids introducing a rational source into the sign argument.

[ScaledPrepaid.lean](ScaledPrepaid.lean) contains the generic result and the
instantiation `twelve_extra_scaled_odds`: for every `K≥84`, every scale `c≥1`,
and every allowed target, the cost exceeds `K+j+12`.

## Keeping the bonus after a peak

Write `n=2^H v−1`, with `v>0`, and let an actual postpeak word `w` take
the peak `3^H v−1` to `Y`. Let `f` and `q` be its counts of odd and even
departures. Its signed offset is the affine numerator evaluated at `−1`.
Call the word maximal when no word of the same length and signed offset
has more odd departures.

The postpeak cone theorem supplies the missing physical connection: a
proposed cheap visitor, before its final same-offset word, must visit an
actual pure-odd peak

\[
 z=3^{H+f-u}v-1,
\]

where `u≤f` is the competing tail's odd count. Put `δ=f−u`. This endpoint
is precisely the scaled virtual ramp with `j=H+δ` and `c=2^δ`, because

\[
 2^{H+\delta}(z+1)
   =3^{H+\delta}2^\delta(n+1).
\]

Applying the scaled prepaid theorem to the original smaller start gives
the following explicit conclusion:

\[
\boxed{\quad
 K\ge84,\qquad H\ge21q+9(K+12)+3
 \quad\Longrightarrow\quad
 \text{every smaller visitor to }Y\text{ costs more than }H+f+K+12.
 \quad}
\]

The other hypotheses are the original divisibility `3^K | n−s`, the
positive ordinary path, and maximality of `w`. There is no ceiling on
the number of upper odd departures or on the lower physical time.
[ProtectedBudget.lean](ProtectedBudget.lean) states the generic finite-budget
version and `twelve_extra_postpeak_odds`.

This is a restriction on specified ordinary targets. Maximality is
essential: the descent packet supplies explicit matching-offset words
that admit much cheaper visitors. Neither this restriction nor its finite
certificate establishes a smaller merger for every residual ordinary source.

## Credit

The basic all-clock barriers and small-positive-origin prepayment architecture
have written antecedents in PR146 at
`f431078244e868dc699fad011044f0d5e7f76437`, identified in the
[corrected descent note](../../descent/README.md). The first checkpoint
formalized the fixed-point finite budget and its 648-source instantiation.
The postpeak source extraction is the new `paid_peak` theorem of this packet.
This note composes that physical extraction with the scaled finite budget.
