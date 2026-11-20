# The stopping-time burden hidden in the inverse potential

**PROPOSED, with an elementary written proof. Collatz is unresolved.**

This note examines the auxiliary condition `W(1)<infinity` in PR #149,
frozen at `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
`research/forward-inverse-defect/CLOSURE_BOUNDARY.md`. It does not prove
that condition. It shows that even *on the already convergent basin*, the
condition carries a uniform logarithmic stopping-time bound. Thus it is
not a harmless boundedness premise to attach to a qualitative Collatz
argument.

The map is the shortcut Collatz map `T`, and `U` is its odd acceleration.
Let `S` be the positive odd integers coprime to three. For `n` in `S` that
actually reaches 1, let `a(n)` count the odd inputs strictly before the
first hit of 1, and let `d(n)` count shortcut steps before that hit. The
counts are zero at 1. No first-hit count is assigned to an unproved
converger.

Write

\[
\ell=\log_2 3,\qquad \delta=8-5\ell>0,
\qquad C_a=5/\delta=66.5004188\ldots,
\qquad C_d=8/\delta=106.4006701\ldots.
\]

## SB1. An exact first-hit formula for the all-word supremum

Use precisely PR #149's potential: a legal inverse letter is
`I_g(t)=(2^g t-1)/3`, with every state in the ternary units, and a word
of length `k` and total exponent `A` has score `8k-5A`. Include the
empty word.

Then, in the extended nonnegative integers,

\[
\boxed{W(1)=\sup_{n\in S,\ n\to1}\{8a(n)-5d(n)\}.}                 \tag{1}
\]

The term `n=1` supplies zero. To prove (1), interpret any legal inverse
word from 1 as an actual positive ordinary inverse path. Its terminal
source `n` reaches 1 in odd time `k`. It consists, in forward order, of
the first-hit path and then `r=k-a(n)` repetitions of the fixed point of
`U`, whose exponent is two. Thus

\[
A=d(n)+2r,\qquad 8k-5A=8a(n)-5d(n)-2r.
\]

This is at most the first-hit score. Conversely the reverse of every
first-hit path from such an `n` is a legal word from 1. This proves both
inequalities. In particular, the repeated trivial cycle cannot increase
this supremum.

## SB2. An elementary distortion bound with no analytic input

Let `u_1,...,u_a` be the odd inputs before that first hit, and put

\[
D(n)=\prod_{i=1}^a\left(1+\frac1{3u_i}\right).
\]

The empty product is one. The exact product identity is

\[
2^{d(n)}=3^{a(n)}nD(n).                                             \tag{2}
\]

For every such ordinary first-hit path,

\[
\boxed{1\le D(n)^9\le 3a(n)+1.}                                  \tag{3}
\]

Indeed its odd inputs are distinct, greater than 1, and prime to three.
After sorting them increasingly, the `i`-th value is at least `3i+1`:
the smallest possibilities are `5,7,11,13,17,19,...`. Therefore

\[
\log D(n)\le\sum_{i=1}^a\frac1{3u_i}
\le\sum_{i=1}^a\frac1{9i+3}
\le\int_0^a\frac{dx}{9x+3}
=\frac19\log(3a+1).
\]

This proves (3). It uses only deterministic first-hit simplicity and the
unit restriction, not a statistical parity model, a density theorem, or
any assumption about nonconvergent starts. A bounded replay of (3) can be
made entirely in integer arithmetic after clearing the product's
denominator.

Combining (1) and (2) gives the exact score identity

\[
8a(n)-5d(n)
=\delta a(n)-5\log_2n-5\log_2D(n).                                \tag{4}
\]

## SB3. A finite inverse bound imposes logarithmic stopping times

Suppose `W(1)<=B`, with `B` a finite nonnegative integer. Equations
(3)--(4) imply, for **every actually convergent** `n` in `S`,

\[
\delta a(n)\le5\log_2n+B+\frac59\log_2(3a(n)+1).                  \tag{5}
\]

Consequently, with effective constants depending only on `B`,

\[
\boxed{
a(n)\le C_a\log_2n+\frac{C_a}{9}\log_2(1+\log_2n)+O_B(1),
}                                                               \tag{6}
\]

and

\[
\boxed{
d(n)\le C_d\log_2n+\frac{C_d}{9}\log_2(1+\log_2n)+O_B(1).
}                                                               \tag{7}
\]

For completeness, the inversion of (5) does not assume the conclusion.
The elementary inequality `log(3a+1)=o(a)` first gives
`a<=2 C_a log_2 n+O_B(1)`. Substitution into the logarithm in (5) then
gives (6). Substituting (6) and (3) into
`d=ell a+log_2 n+log_2 D` gives (7), since
`ell C_a+1=C_d`. The estimates concern first hits only.

The usual unaccelerated map takes `d(n)+a(n)` steps along the same first
hit, so its leading constant is `(8+5)/delta=172.9010889...`.

There is also an elementary converse with no logarithmic correction:
if for some finite `K`

\[
a(n)\le C_a\log_2 n+K\quad\hbox{for every convergent }n\in S,
\]

then (4) and `D(n)>=1` give `W(1)<=max(0,delta K)`. The elementary
argument leaves a logarithmic gap between this sufficient condition and
(6); it does not silently identify them.

The same leading constants apply to every convergent positive integer,
after its initial even factors and, if needed, its first odd nonunit are
removed. These take respectively `v_2(n)` shortcut steps and at most
one odd step before entering `S`; their contribution changes the
displayed upper bound by a bounded constant or is absorbed by the
initial logarithmic term. The exact formulas (1)--(5) retain their
stated domain `S`.

## SB4. An explicit, conditional membership deadline

The implication above can be made a finite exact procedure without
evaluating logarithms. For a nonnegative integer `B` and a positive
integer `n`, define `L_B(n)` as the
smallest integer `a>=10` for which

\[
\boxed{2^{72a}>2^{9B}3^{45a}n^{45}(3a+1)^5.}                     \tag{8}
\]

Such an `a` exists because `2^8>3^5`. Moreover the ratio of the left
side to the right side increases strictly once `a>=10`. Indeed its
successive ratio is

\[
\frac{2^{72}}{3^{45}}\left(\frac{3a+1}{3a+4}\right)^5>1,
\]

as follows already at `a=10` from the exact integer comparison
`2^72*31^5 > 3^45*34^5`; the parenthetical fraction is increasing.

If `W(1)<=B`, every convergent `n` in `S` must satisfy

\[
a(n)<L_B(n).                                                       \tag{9}
\]

To see this, exponentiate (5) after multiplying by nine. It gives the
opposite weak inequality to (8), and that opposite inequality is
impossible at all `a>=L_B(n)` by the monotonicity just proved.

Thus a *known valid* value of `B` would give a total decision algorithm
for membership in the basin of 1 on `S`: iterate from the specified
ordinary input for `L_B(n)` odd steps, stopping immediately at 1. For
an arbitrary positive integer, first remove its even factors and, if
its odd part is divisible by three, perform one odd event; apply the
deadline to the resulting unit. These finite operations preserve basin
membership. Under the
assumption, failure to hit by that deadline proves that this input never
hits 1. It does not prove the assumption or say that the rejecting case
cannot occur. An observed finite sample of first-hit scores cannot be
substituted for the all-source bound `B`.

## SB5. The sharper equivalence from the uniform simple-path budget

The self-contained appendix `LOCAL_DISTORTION.md` proves the uniform
reciprocal bound `sum 1/x<600` on a finite simple shortcut segment.
Its anchored shell count discards the final physical steps before
using injectivity; it does not assume convergence for arbitrary
sources. Therefore

\[
0\le\log_2 D(n)\le D_*:=200/\ln2
\]

for every first-hit path above. Equation (4) now gives the equivalence

\[
W(1)<\infty
\quad\Longleftrightarrow\quad
\sup_{n\in S,\ n\to1}\left(a(n)-C_a\log_2n\right)<\infty.
\tag{10}
\]

More quantitatively, if `W(1)<=B`, then

\[
a(n)\le C_a\log_2n+(B+5D_*)/\delta,
\qquad
d(n)\le C_d\log_2n+(\ell B+8D_*)/\delta.
\tag{11}
\]

Thus the logarithmic corrections in (6)--(7) can be replaced by
absolute additive constants using the reviewed simple-path budget.
Those constants are large; SB4's elementary integer deadline remains
a different, often more useful effective bound.

This section has a self-contained, independently reconstructed local
dependency; it does not import the harmonic trace, a stationary-law
theorem, or an unproved global orbit estimate. For attribution and
comparison, the stronger reciprocal budget 320 at PR #140,
`fe2247fcd7730c15430941a7b6e011d006d41d84`,
`research/novel-swarm-20261030/pass4/WINDOWS.md`, W1--W3, would improve
the constant to `320/(3 ln2)`. Its separate narrow reconstruction is
recorded in `REVIEW_PACKING.md`; it is not needed for the present
claims. SB1--SB4 do not use any uniform packing input. Neither (10)
nor (11) establishes the missing bounded supremum.

## Scope and remaining inference

The extra burden is now explicit: before using the closing bounds from
PR #149, one must control a uniform near-critical first-hit clock over
the entire convergent basin, in addition to excluding other components.
This note does not establish that clock bound, universal convergence,
or a bound on the all-word supremum at 1. It makes no assertion that
qualitative Collatz and this quantitative statement are logically
inequivalent; that would require a separate argument.

The companion `check_stopping_burden.py` verifies the algebra, exact
distortion bound, inverse-word/first-hit score identity, and monotone
deadline comparisons on explicitly bounded families. Its generated
report is finite arithmetic evidence and does not certify `W(1)`.
