# Uniform denominator clearing and complete-witness additive handoffs

**Status: the new construction and its quantitative bounds are proved in
Lean core; the universal additive closure needed for Collatz remains OPEN.**

This attack started from the smaller-component-partner constructions in
PR180 at `9010a8790535002b6d9ff92304f0ba289e2e98fe`,
`research/lean-forward-band-20261121/lean/BandTransport.lean`, and PR184 at
`366dab89ee9548084ab9b5e4e90ff82abf287a20`,
`research/lean-band-coupling-20261121/lean/RisingMerge.lean`.
The new result is in
[`lean/Collatz/MergerDenominatorClear.lean`](lean/Collatz/MergerDenominatorClear.lean).

## 1. A template exists for every power of three

For a positive-gap word `W`, let `K` be its length, `A` its sum, and `C(W)`
its ordinary affine correction. The module proves, for **every integer
K>=1**, the existence of a word and an integer `z>=0` satisfying

\[
\begin{aligned}
 |W|&=K, & C(W)&=1+2^A z,\\
 1\le W_i&\le2K-1, & A&\le K(2K-1),\\
 &&2^K(z+1)&<3^K. \tag{M1}
\end{aligned}
\]

The word is constructed, rather than selected from a precomputed finite
menu. In rational language it clears the denominator of `-1/3^K` after
exactly `K` odd steps. The Lean construction uses natural-number numerator
identities throughout; it does not need a rational Collatz convergence
assumption.

For `K=1`, take `W=(1)` and `z=0`. For `K>=2`, first factor

\[
 3^{K-1}-1=2^a p,\qquad a\ge1,\quad p\text{ positive odd}.
\]

At a later stage with positive odd numerator `p` and remaining denominator
`3^j`, factor

\[
 p+3^{j-1}=2^b p',\qquad b\ge1,\quad p'\text{ positive odd},
\]

and continue with `j-1`. The denominator exponent strictly decreases, so
this process always terminates. The positive-numerator induction proves
`p+C(W)=2^A z`; attaching the first step gives M1's correction identity.

The proof is `positive_numerator_clear`, `denominator_clear`, and their
bounded versions. These are existence theorems for every index, not
conditional compiler interfaces requiring a successful word as input.

## 2. The clock and terminal bounds are uniform

Throughout a construction beginning at denominator `3^K`, every positive
numerator is at most `3^(K-1)`. Each new numerator before division is at
most `2*3^(K-1)`, and division by at least two preserves that bound.
Consequently each halving exponent is at most `2K-1`, using
`3^(K-1)<=4^(K-1)`. There are exactly `K` such steps, proving the quadratic
clock bound in M1.

Independently, every positive-gap word satisfies

\[
 2^{|W|}\bigl(C(W)+2^{A}\bigr)\le3^{|W|}2^A.
\]

This follows by induction from `|W|<=A`. Substituting
`C(W)=1+2^A z` and cancelling the positive factor `2^A` gives the strict
terminal bound in M1. The relevant declarations are
`denominator_clear_bounded`, `correction_height_bound`, and
`clearing_endpoint_bound`.

Clearing does not uniformly land at one. For example, the checked word
`(3,1,3,1,1,1,2)` has `K=7`, `A=12`, and `z=3`. Nor does clearing always
produce coefficient contraction: `K=2` uses `(1,1)` with `A=2,z=1`, so
`3^K/2^A=9/4`. The terminal bound asserts no convergence of `z`.

## 3. A universal transition for complete source certificates

Consider a reverse-power comparison with a supplied certificate

\[
 \operatorname{Certificate}(3^k n;(a)\Vert\tau).
\]

Its first exact source step provides the **same supplied suffix**

\[
 3^{k+1}n+1=2^a q,\qquad\operatorname{Certificate}(q;\tau).
\]

Use the automatically constructed template from M1 with `K=k+1`, and
assume its finite clock fits: `A<=a`. Direct substitution gives

\[
 3^{k+1}n+C(W)=2^A\bigl(2^{a-A}q+z\bigr). \tag{M2}
\]

The existing `Prefix` compiler proves that this is an actual ordinary
target path, with every intermediate oddness and divisibility condition
checked. Thus

\[
 B(n)\iff B(2^{a-A}q+z).
\]

The child known source is `S=2^(a-A)q`, carrying the powered certificate
`(a-A; tau)`. Its full rank satisfies

\[
 \Gamma(a-A;\tau)\prec\Gamma(0;(a)\Vert\tau), \tag{M3}
\]

because `A>=1`: the removed odd-source grade `2a` is replaced either by
nothing or by the strictly smaller initial even-run grade `2(a-A)+1`.
The entire inherited tail cancels. The remaining child comparison is

\[
 B(S)\Longrightarrow B(S+z).
\]

`complete_witness_additive_rewrite` proves M2, M3, the exact suffix
certificate, and the basin equivalence together.
`uniform_reverse_power_template` quantifies over **every k**, supplies the
bounded template automatically, and proves the transition for every
supplied certificate whose first exponent fits it. No additional ternary
congruence test is imposed.

## 4. The whole one-gap source family fits the budget

This subsection includes a written elementary valuation argument; the
quadratic comparison itself is additionally formalized as
`quadratic_clock_below_order_scale`.

For a one-gap source certificate, `q=1` and

\[
 3^K n+1=2^a.
\]

The standard elementary order calculation gives
`2*3^(K-1) | a`. For completeness, reducing modulo three first forces
`a=2t`. For every `t>=1`,

\[
 v_3(4^t-1)=1+v_3(t).
\]

If `3` does not divide `t`, reduction modulo nine gives valuation one.
Removing a factor of three from `t` uses
`X^3-1=(X-1)(X^2+X+1)` and `v3(X^2+X+1)=1` for `X=4^s`; modulo nine,
the possible `X` values are `1,4,7`, all giving the second factor congruent
to three. This proves the formula by induction on `v3(t)` and hence the
order assertion.

The numerical inequality

\[
 K(2K-1)\le2\,3^{K-1}
\]

holds for every `K>=1` and is proved in Lean with the index shifted by one.
Thus every one-gap source certificate fits the uniform clearing word.
What remains is the actual additive target `2^(a-A)+z`; fitting the word
does not by itself prove its convergence or its descent.

For example, the reverse-nine template is `(3,2,1)`, with `K=3,A=6,z=1`.
Its target coefficient contracts by `27/64`. In general that coefficient
can exceed one, as the `K=2` example shows. Appending a convergence
certificate for `z` would require proving that certificate and fitting its
additional clock; neither is assumed here.

## 5. A low-prefix transition for the new asymmetric reset

The companion `PsiSuffix.lean` construction produces a reverse-nine source
beginning with `(1,1,3)`. This case has an exact transition even though its
first source gap does not fit the six-clock high-gap template.

From

\[
 \operatorname{Certificate}(9n;(1,1,3)\Vert\tau)
\]

peeling the prefix gives `243n+19=32q` and
`Certificate(q,tau)`. The target takes five ordinary odd steps:

\[
 243n+211=32(q+6).
\]

Therefore

\[
 B(n)\iff B(q+6),\qquad
 \Gamma(0;\tau)\prec\Gamma(0;(1,1,3)\Vert\tau).
\]

`reverse_nine_low_handoff` proves the actual target prefix and the complete
source rank decrease. This links the asymmetric reset to the fixed
add-six comparison. It does not assume add-six closure.

## 6. What the merger attack did not establish

The existing PR180/184 long-block mergers cover two broad parts of the
family `2^d+2^k-1`, for `d-k>=2`: every even `k` is handled by the
unbounded odd-block exchange, and odd `k` with even `d` has a smaller odd
predecessor because the source is two modulo three. The remaining
odd-`d`, odd-`k` corner was examined directly. No universal smaller partner
for that corner was found.

The current attack instead obtained M1--M3: a uniform, quantitatively
bounded compiler covering every reverse power of three, and a concrete
low-prefix route to add-six. A complete proof still needs a sound cover of
the resulting additive comparisons, or a compatible construction of a
smaller certified child. A smaller component partner relative to a larger
marked visit cannot replace the required bound against the original
ordinary source. No such substitution is used in the new Lean module.
