# Independent review: finite critical spikes force small ancestors

**Date:** 2026-11-22 UTC.  
**Reviewed note:** `FINITE_SPIKES_FORCE_SMALL_ANCESTORS.md`.  
**Final source SHA-256:**
`130219761341f3ac612da557ece5d1a96a674cf72a4da18d5883eff16f5823b7`.

## Finding

The new corollary is sound in its stated source-qualified scope. A
critical-size finite density or obstacle certificate at a fixed
polylogarithmic odd-step horizon forces an actual smaller positive odd
unit ancestor. No deeper inverse-floor assumption, Haar-to-ordinary
substitution, or uniform infinite-horizon bound is used.

This is a read-only mathematical review. No earlier build or computation
was repeated. The underlying horizon note and analytic input
normalization were checked in `REVIEW_POLYLOG_INVERSE_FLOORS.md`.

## The finite-prefix localization

The earlier estimate applies the counting operator to

\[
P^d(D_t-D_m)(q),
\qquad d=k_j-2m,\quad t=2m.
\]

Its retained ordinary sources are the prefix ancestors at depth `d`,
where the function `H=D_t-D_m` is evaluated. Because `H` vanishes at
nonunits, the coefficient bound `omega<=q/b` requires a floor only for
unit ancestors at that prefix depth. Every such depth is at most the
requested horizon `K`.

Although each finite density inside `H` itself sums over deeper inverse
words, these deeper sources are not subjected to the floor in this
argument. Their entire contribution is controlled by the unconditional
finite-residue average `L1` estimate for `H`. Its periodicity and mixing
bound do not require an ordinary size restriction on those suffix
ancestors. Thus the proposed weakening from a full inverse-basin floor
to `F_K` is legitimate.

The initial-depth estimate uses only `q>=b`, which is precisely the
depth-zero part of `F_K`. The final note now states this explicitly.

## Scaling and extraction of the physical ancestor

With `b=exp((log q)^gamma)`, `0<gamma<1`, one has `1<b<q` for all
sufficiently large `q`. The chosen integer

\[
m=\left\lfloor\frac{(\log q)^\gamma}{4\log3}\right\rfloor
\]

satisfies `m>=c(log q)^gamma` and `3^(4m)<=b` eventually. Under the
contrary finite-floor hypothesis, the established telescope therefore
gives

\[
D_s(q)/q\le e^{-(\log q)^\gamma/2}
 + O_A\bigl((\log q)^{2B-\gamma(A+1)}\bigr)
\]

for `s<=(log q)^B`. Choosing a fixed `A` with
`gamma(A+1)>2B+2` makes this `O((log q)^(-2))`, hence strictly below
`eta/log(q+2)` for sufficiently large `q`. The constants may depend on
the chosen `A`, and the note correctly absorbs them into its threshold;
it does not change `A` with `q`.

Failure of `F_s` supplies an actual positive odd unit `n<b` at some
integer depth `j<=s`. Depth zero is impossible because its sole source
is `q>b`. Thus `1<=j<=s`, with the exact ordinary identity `U^j(n)=q`.
No limit or probabilistic surrogate is needed to obtain this source.

## Obstacle depth and quantifiers

For any witness `k` to the obstacle certificate, the source-proved
comparison `V_k<=kappa D_(k+1)` supplies the density certificate with
`s=k+1` and threshold `eta/kappa`. The additive one is absorbed by any
fixed horizon exponent larger than `B`, or directly by a factor two
in the same horizon estimate. Consequently the physical ancestor has
`1<=j<=k+1`, as claimed. The final note explicitly scopes the conclusion
to any witnessing `k`, removing ambiguity from the displayed existential.

The proof of the ancestor does not assume convergence. Using that
ancestor to infer convergence of `q` additionally requires the stated
induction or independent convergence premise for smaller sources.
Likewise a large limiting obstacle value alone supplies no asserted
polylogarithmic bound on when its finite certificate appears.

## Corrections before freezing

Only presentation clarifications were needed: a missing LaTeX
backslash, the explicit witness scope for `k`, and the depth-zero use
of `q>=b`. They were incorporated in the hash reviewed above. No
substantive proof change was required.
