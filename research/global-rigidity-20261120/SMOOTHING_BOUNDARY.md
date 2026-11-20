# A closing regularity criterion, and two failed analytic shortcuts

**PROPOSED; exact reductions and counterexamples to specified shortcuts.**
The regularity criterion below would exclude nonperiodic positive orbits,
but its hypothesis is not proved. The finite-clock obstruction and critical
perpetuity calculation are unconditional. They do not establish or refute
the all-clock moment target of PR144.

Use the ordinary odd map, `c(n)=3n/(3n+1)`, and the operators defined in
`ORDINARY_ESSENTIAL_SPECTRUM.md`. Set

\[
 r_q(n)=\prod_{j<q}c(U^j n),\qquad
 r(n)=\lim_{q\to\infty}r_q(n),\qquad r_0(n)=1.
\]

## SM1. A precise global regularity statement would close escape

Using the PR150 local simple-path reciprocal budget identified in OE5,
the following are equivalent:

1. Every positive ordinary orbit is eventually periodic.
2. `r(n)=0` for every positive odd `n`.
3. `r(n+2)-r(n) -> 0` as positive odd `n -> infinity`.

The equivalence of the first two is already the product/energy interface;
it is not claimed as a new result. Here is the additional adjacent-value
criterion. On a nonperiodic source the same local reciprocal budget gives
`r(n)>=epsilon:=exp(-200)`. On an eventually periodic source `r(n)=0`.
If both kinds of source occur, both sets are unbounded: a nonperiodic
orbit has infinitely many distinct odd states, while

\[
 N_k=(4^k-1)/3\quad(k\ge1)
\]

are arbitrarily large odd integers satisfying `U(N_k)=1`. In the ordered
sequence of positive odd integers, two unbounded complementary sets have
infinitely many adjacent changes of membership. At each such boundary
`|r(n+2)-r(n)|>=epsilon`. This proves that condition 3 excludes every
nonperiodic source. The other directions are immediate.

Thus an ordinary-specific smoothing theorem for the **actual infinite
product**, even just vanishing adjacent differences, would be sufficient.
It would not exclude additional positive cycles, whose products also
vanish. The first unsupported inference is that this smoothing holds.

## SM2. The finite operators destroy that regularity after two steps

Let

\[
 (Kf)(n)=c(n)f(Un),\qquad
 \mathcal S=\{f\in\ell^\infty(O):f(n+2)-f(n)\to0\}.
\]

Although `1 in S` and `K1=c in S`, `K^2 1` is not in `S`.
The failure is witnessed by explicit positive ordinary integers, not a
completion point. Put

\[
 N_k=(4^k-1)/3,\qquad M_k=N_k+2=(4^k+5)/3.
\]

For every `q>=1`,

\[
 r_q(N_k)=(1-4^{-k})(3/4)^{q-1}.                         \tag{1}
\]

For `k>=4`, the first odd valuations of `M_k` are `1,1,4`, followed
by `2` through odd clock `k-1`. More explicitly,

\[
 U(M_k)=2^{2k-1}+3,\qquad
 U^2(M_k)=3\,4^{k-1}+5,
\]

and

\[
 U^q(M_k)=3^{q-1}4^{k-q}+1\quad(3\le q\le k-1).          \tag{2}
\]

Substitution in `3x+1` proves every stated valuation and (2). Thus for
every fixed `q`, all of the first `q` states from `M_k` tend to infinity
as `k` tends to infinity. It follows that

\[
 \lim_{k\to\infty}r_q(M_k)=1,
 \qquad
 \limsup_{n\to\infty\atop n\ {m odd}}
 |r_q(n+2)-r_q(n)|\ge1-(3/4)^{q-1}.                      \tag{3}
\]

In particular the failure already occurs at `q=2`, with a jump of at
least `1/4`. The displayed defect tends to one as `q` increases. The
limit in (2) is always at a fixed finite clock with changing sources.
It makes no claim about the infinite orbit of any one `M_k`.

## SM3. Positive averages that reach later clocks retain the jump

Let `alpha_q>=0`, `sum alpha_q=1`, be any probability distribution on
nonnegative integer clocks, and define

\[
 R_\alpha(n)=\sum_{q\ge0}\alpha_q r_q(n).
\]

Since `0<=r_q<=1`, dominated summation along the explicit pair above gives

\[
 \lim_k R_\alpha(M_k)=1,\qquad
 \lim_k R_\alpha(N_k)
 =\alpha_0+\sum_{q\ge1}\alpha_q(3/4)^{q-1}.              \tag{4}
\]

Consequently its adjacent oscillation is at least one minus the second
quantity in (4). This is positive for any law giving positive mass to
clocks `q>=2`; laws supported on `{0,1}` are the trivial exceptions.
If a family of clock laws escapes every finite clock set, that quantity
tends to zero. Hence these positively averaged profiles become maximally
rough in the adjacent sup seminorm.

Two useful exact special cases are

\[
 \limsup_{n\to\infty}|\Delta R_Q(n)|
 \ge1-\frac{5-4(3/4)^{Q-1}}Q,
 \quad R_Q=\frac1Q\sum_{q=0}^{Q-1}r_q,                  \tag{5}
\]

and

\[
 \limsup_{n\to\infty}|\Delta R_z(n)|
 \ge\frac{z^2}{4-3z},
 \quad R_z=(1-z)\sum_{q\ge0}z^q r_q,\quad0<z<1.         \tag{6}
\]

Both lower bounds tend to one at their infinite-clock limits. A proof
of SM1 therefore cannot be obtained by establishing uniform adjacent
smoothing for these finite, Cesaro, Abel, or other positive
source-independent clock averages. Source-dependent stopping clocks,
signed cancellations, and other regularity notions are not ruled out.
The actual pointwise limit `r` can still be identically zero even though
every approximation in (5)--(6) has large jumps at changing sources.

## SM4. An exact critical trace reorganization

This is an attempted route toward PR144's moment bound, not a proof of
that bound. The all-word expansion is the same population accounting as
PR144 `TRACE.md`, T1--T3; the following normalization isolates its critical
renewal law.

Fix a word `w=(a_1,...,a_q)` of positive odd-step valuations. Let
`A_j=sum_{i<=j}a_i`, `A_0=0`, `A=A_q`, and

\[
 C_w=\sum_{j=0}^{q-1}3^{q-1-j}2^{A_j},\quad
 J_w=3^q/2^A,\quad \gamma_w=C_w/2^A.
\]

Its affine forward formula is `t=J_w n+gamma_w`. Let `m=3^q` and
let `r_w` be the **least positive odd** representative of

\[
 2^A t\equiv C_w\pmod {3^q}.
\]

Thus `1<=r_w<2m`. This is not necessarily the least ordinary residue
in `[0,m)`. The single congruence implies integrality at every inverse
intermediate: reduce modulo 3 for the last forward step, divide, and
induct. Starting from positive odd `r_w`, each integral inverse step
`(2^a t-1)/3` remains positive odd. Therefore its source

\[
 n_w=(2^A r_w-C_w)/3^q
\]

is a positive odd integer, all valuations replay exactly, and

\[
 r_w=J_w n_w+\gamma_w\ge J_w+\gamma_w.                  \tag{7}
\]

There is no additional positivity shift once the least **odd**
representative is used. All endpoints for this word are exactly
`r_w+2m l`, `l>=0`; their sources are `n_w+2^{A+1}l`.
Define

\[
 W_m(r)=\sum_{l\ge0}(r+2ml)^{-2}.
\]

Regrouping the all-source diagonal moment by its unique valuation word
gives

\[
 D_q=\sum_w J_w^4 W_{3^q}(r_w).                         \tag{8}
\]

Now `sum_{a>=1}3/4^a=1`, and `sum_w J_w^2=3^q`. Under independent
gaps with law

\[
 \mathbb P(a=g)=3/4^g\quad(g\ge1),
\]

the word probability is `J_w^2/3^q`, so (8) becomes

\[
 \boxed{D_q=3^q\,\mathbb E[J_w^2 W_{3^q}(r_w)].}         \tag{9}
\]

This probability law is a normalization of a sum over inverse words.
It is **not** asserted to be the valuation distribution along any fixed
ordinary forward trajectory.

The concrete sufficient estimate still missing is, for one finite `B`,

\[
 \mathbb E[J_w^2 W_{3^q}(r_w)]
 \le B(q+1)^2 3^{-q}\quad\hbox{for all }q\ge0.           \tag{10}
\]

It is exactly PR144's quadratic diagonal-moment hypothesis under this
normalization. That packet also supplies weaker sufficient Cesaro or
reciprocal-moment alternatives. The representative `r_w` and the real
data `J_w,gamma_w` come from the **same** word. Replacing their joint
law by an independently uniform ternary residue law is not authorized.

## SM5. The real critical perpetuity is finite a.s. but has infinite mean

The real offset in (7) is

\[
 \beta_q:=\frac{\gamma_w}{J_w}
 =\frac13\sum_{j=0}^{q-1}M_j,\qquad
 M_j=2^{A_j}/3^j.                                       \tag{11}
\]

Under the critical law in SM4, `E 2^a=3`, so `M_j` is a nonnegative
martingale with `E M_j=1`. On the other hand,

\[
 \mathbb E\sqrt{M_j}=\rho^j,\qquad
 \rho=\frac{\sqrt6}{4-\sqrt2}<1.                         \tag{12}
\]

The strict inequality follows from `sqrt2<3/2`, after squaring positive
quantities. Tonelli gives `E sum_j sqrt(M_j)=1/(1-rho)<infinity`.
Thus `sum_j sqrt(M_j)<infinity` almost surely, and then
`sum_j M_j<infinity` almost surely. However

\[
 \beta_q\uparrow\beta_\infty<\infty\quad\hbox{almost surely},
 \qquad E\beta_q=q/3,\qquad E\beta_\infty=\infty.         \tag{13}
\]

In particular `M_j->0` almost surely while `E M_j=1` at every clock:
this martingale is not uniformly integrable. The typical real contraction
of the inverse coefficients and almost-sure finiteness of their offset
do not supply a uniform integrability estimate, much less the coupled
ordinary-rational trace estimate (10). The failure in (13) is explicit,
not an appeal to an unspecified possible correlation.

A survival-specific joint real/ternary estimate might still prove (10)
or a weaker sufficient moment criterion. None is proved here. Scalar
Haar mixing on an adelic quotient also cannot silently replace that
estimate: the ordinary arithmetic representatives and their real
positivity constraint must remain in the same state space and measure.

## Evidence and final boundary

The companion exact script checks the explicit ordinary pairs in SM2
for `4<=k<=20`, `0<=q<=k-1`, and the rational Abel identity. Its main
purpose remains the all-predecessor finite spectral certificates.
The convergence and non-uniform-integrability statements in SM5 are
proved by the written nonnegative summations; they are not numerical
claims about random experiments.

The closure attempts were: a spectral/Fredholm exclusion (refuted by
the convergent-basin approximate spectrum), global adjacent regularity
(sufficient but open, with its natural finite-clock domain refuted),
and critical renewal/ternary decoupling (exact reformulation with a
specific missing inequality and an explicit uniform-integrability
failure). No one of these attempts resolves escape or nontrivial cycles.
