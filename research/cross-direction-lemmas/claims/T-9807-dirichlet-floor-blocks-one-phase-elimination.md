# T-9807 -- A Dirichlet floor blocks the stated full-measure comparison

Claim ID: `T-9807`
Title: In the L-9414 height convention every nine-value p-adic linear-independence exponent is at least ten
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-period-ten`
Reviewing agents: `gpt56-synthesis-01-wave14-cap-cell-hierarchy`; `gpt56-synthesis-01-wave14-quant-fresh-primes`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: elementary pigeonholing in `Z_p`; applied to refreshed `PR20/L-9412`, `L-9413`, `L-9414`, `Q-9413`, and `R-9408` at `93739b4dbc4ac317f660477e7805dabfe484b287`
Scope: the numerical full-measure comparison currently stated in Route A for the primitive period-ten phase vector
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup and exact convention

Fix a prime `p` and values

\[
 \alpha_1,\ldots,\alpha_D\in\mathbf Q_p
\tag{1}
\]

such that

\[
 1,\alpha_1,\ldots,\alpha_D
\tag{2}
\]

are linearly independent over `Q`.  For a nonzero integer vector

\[
 \mathbf a=(a_0,a_1,\ldots,a_D)\in\mathbf Z^{D+1}
\tag{3}
\]

put

\[
 L(\mathbf a)=a_0+\sum_{i=1}^D a_i\alpha_i,
 \qquad
 H(\mathbf a)=\max_{0\le i\le D}|a_i|.
\tag{4}
\]

Valuations are normalized by `v_p(p)=1`, and coefficient height is the
ordinary Archimedean integer height in (4).  Thus `log_p H`, rather than a
projective or denominator-only height, is the normalization relevant below.

The quantitative hypothesis in `PR20/L-9414/(1)` says, for every
`epsilon>0` and all sufficiently large nonzero integer vectors,

\[
 v_p(L(\mathbf a))
 \le (\omega+\epsilon)\log_p H(\mathbf a).
\tag{5}
\]

An additive constant on the right of (5) would not change any conclusion of
this claim.

## Theorem 1 -- the sharp Dirichlet dimension floor

There is a sequence of nonzero integer vectors `a` of unbounded height such
that

\[
 \boxed{
 v_p(L(\mathbf a))
 \ge (D+1)\log_p H(\mathbf a)-O_{\boldsymbol\alpha,p}(1).
 }
\tag{6}
\]

Consequently every exponent `omega` satisfying (5) obeys

\[
 \boxed{\omega\ge D+1.}
\tag{7}
\]

This is the p-adic Dirichlet floor for one constant coefficient and `D`
value coefficients.  In particular, qualitative linear independence does
not permit a full linear-independence measure with exponent below the number
`D+1` of integer coefficients.

### Proof

Choose an integer `c>=0` for which

\[
 \beta_i=p^c\alpha_i\in\mathbf Z_p
 \qquad(1\le i\le D).
\tag{8}
\]

For an integer `H>=1`, consider all `(H+1)^(D+1)` vectors

\[
 \mathbf x=(x_0,\ldots,x_D)\in\{0,1,\ldots,H\}^{D+1}
\tag{9}
\]

and send them to the residue class

\[
 p^c x_0+\sum_{i=1}^D x_i\beta_i\pmod {p^{k_H}},
\tag{10}
\]

where

\[
 k_H
 =\left\lceil (D+1)\log_p(H+1)\right\rceil-1.
\tag{11}
\]

The choice (11) gives the strict inequality

\[
 p^{k_H}<(H+1)^{D+1}.
\tag{12}
\]

Indeed, if the number inside the ceiling is integral, (11) subtracts one;
otherwise `k_H` is its floor.  There are only `p^(k_H)` residue classes in
(10), so two distinct box vectors `x,y` have the same image.  Put

\[
 \mathbf a=\mathbf x-\mathbf y.
\tag{13}
\]

Then `a` is nonzero, `H(a)<=H`, and (10) gives

\[
 p^cL(\mathbf a)\in p^{k_H}\mathbf Z_p.
\tag{14}
\]

Therefore

\[
 \begin{aligned}
 v_p(L(\mathbf a))
 &\ge k_H-c\\
 &\ge (D+1)\log_p(H+1)-1-c\\
 &\ge (D+1)\log_p H(\mathbf a)-1-c.
 \end{aligned}
\tag{15}
\]

The vectors obtained as `H` tends to infinity have an unbounded-height
subsequence.  Otherwise only finitely many nonzero integer vectors would
occur; independence in (2) makes each corresponding valuation finite, in
contradiction with `k_H->infinity`.  Equation (15) proves (6).

If (5) held with `omega<D+1`, choose

\[
 0<\epsilon<{D+1-\omega\over2}.
\tag{16}
\]

Along the unbounded sequence from (6), the lower coefficient of `log_p H`
is `D+1`, while the upper coefficient in (5) is `omega+epsilon<D+1`.
The fixed constant in (6) is eventually negligible, a contradiction.  This
proves (7). **QED**

## Theorem 2 -- no scalar rational approximants can beat the nine-phase measure

For a primitive period-ten word, `PR20/L-9414` retains the nine phase values

\[
 \alpha_j=f_R(Z\lambda^j),
 \qquad 0\le j\le8,
\tag{17}
\]

and appends

\[
 \beta=f_R(Z\lambda^9).
\tag{18}
\]

`PR20/L-9412` supplies the rational linear independence of

\[
 1,\alpha_0,\ldots,\alpha_8.
\tag{19}
\]

There are `D=9` values in (19), hence Theorem 1 forces every full-space
exponent in the precise convention `PR20/L-9414/(1)` to satisfy

\[
 \boxed{\omega_9\ge10.}
\tag{20}
\]

The refreshed `PR20/R-9408` transcribes the Vaananen--Wallisser exponent

\[
 \theta(\gamma,D)
 =1+{2D-1+\sqrt{1+4D^2}
 \over 2-\gamma(2D+1+\sqrt{1+4D^2})}.
\tag{21}
\]

Apply that source theorem at dimension one to the single value `beta`.  It
gives a uniform rational linear-form upper exponent

\[
 \omega_1=\theta(\gamma,1)
 =1+{1+\sqrt5\over2-\gamma(3+\sqrt5)}.
\tag{22}
\]

For every sequence of reduced rational approximants `p_n/q_n` with `q_n`
odd and `H_n=max(|p_n|,|q_n|)` tending to infinity,

\[
 \boxed{
 \limsup_{n\to\infty}
 {v_2(\beta-p_n/q_n)\over\log_2 H_n}
 \le\omega_1.
 }
\tag{23}
\]

Moreover, `L-9412` proves `gamma<Gamma(9)`.  Since
`sqrt(325)>18`,

\[
 0<\gamma<\Gamma(9)
 ={19-\sqrt{325}\over18}<{1\over18}.
\tag{24}
\]

Using `sqrt(5)<3` in (22),

\[
 \boxed{
 \omega_1
 <1+{4\over 2-(1/18)6}
 ={17\over5}<10\le\omega_9.
 }
\tag{25}
\]

Thus no scalar rational-approximation family for `beta` can have the exponent
strictly larger than `omega_9` required by `L-9414`.  The full-measure
one-phase elimination route is impossible in the stated ordinary reduced
height convention.

### Proof

The dimension-nine lower bound is (20).  At dimension one, `beta` is a
nonzero rational evaluation point of the same Tschakaloff function, and the
source condition already verified through dimension nine in `L-9412`
certainly applies.  For a reduced approximant with odd denominator,

\[
 v_2(\beta-p_n/q_n)=v_2(q_n\beta-p_n),
\tag{26}
\]

and the integer coefficient vector `(-p_n,q_n)` has height exactly `H_n`.
Substitution in the dimension-one measure, followed by `epsilon` tending to
zero along the unbounded sequence, proves (23).  Equations (24)--(25) are
exact comparisons, so (23) is strictly below every possible `omega_9` from
(20). **QED**

## Corollary -- the published full measure cannot bootstrap even one phase

For every admitted `D>=1`, `R-9408` proves that
`theta(gamma,D)>=theta(gamma,1)=omega_1`.  The dimension-one argument above
upper-bounds the actual rational-approximation limsup of any proposed new
phase by `omega_1`.  Therefore no scalar approximant family can satisfy the
strict comparison

\[
 \tau>\theta(\gamma,D)
\tag{27}
\]

needed to append that phase by `L-9414`.  This rigorously recovers the
published-measure closure asserted in `R-9408`, without identifying a
certified scalar lower bound with the scalar family's actual exponent.

For context, `L-9413` proves only

\[
 \liminf_{n\to\infty}
 {v_2(\beta-p_n/q_n)\over\log_2 H_n}
 \ge\tau_{\rm cert},
 \qquad
 \tau_{\rm cert}={9\over\log_2 81}<{3\over2}.
\tag{28}
\]

It does not prove equality in (28).  The genuine closure comes from the
dimension-one upper bound (23), not from comparing `tau_cert` directly with
the larger published exponent.

## What remains open

The abstract algebra in `PR20/L-9414` is correct.  What fails is its use of a
**uniform full-space** measure for the retained phases together with scalar
rational approximants for the new phase: the dimension-one source measure
puts every such scalar family below the retained full-measure exponent.

A hypothetical native relation produces only the structured sequence of
coefficient vectors

\[
 \left(
 q_nC_0+C_{10}p_n,
  q_nC_1,\ldots,q_nC_9
 \right),
\tag{29}
\]

not every vector in an unrestricted ten-dimensional integer box.  Therefore
another viable replacement for Route A is a directional estimate specifically
on (29), for every fixed hypothetical relation vector `C`.  The pigeonhole
argument proving (20) does not impose a ten-dimensional floor on that thin
family.

Equivalently, a successful argument must exploit at least one of:

1. the native coefficient direction in (29);
2. the nonscalar triangular `q`-difference dynamics of `Q-9413`; or
3. a combined-moment or Hermite--Pade construction.

The scalar aligned-order routes are already separately bounded by local
`L-9891`, `L-9895`, and `T-9804`; none alters the dimension floor (20).

At the refreshed PR #20 head, `R-9408` independently transcribes the actual
Vaananen--Wallisser exponent and obtains

\[
 \omega_9=2318.657271149257\ldots.
\tag{30}
\]

This is the value in the canonical `X-9412` output; the nearby decimal printed
in `R-9408/(6)` has a non-load-bearing last-digit transcription error.  The
exact source computation is much stronger numerically than (20).
`R-9408` compares it directly with the certified scalar lower bound, which by
itself would show only that the two published estimates do not verify the
desired strict inequality.  The dimension-one application (22)--(26) supplies
the missing upper bound on the scalar family's actual limsup and thereby makes
the closure rigorous.

The other distinct contribution here is the source-independent dimension
floor: it explains before any source constants are read why the certified
exponent below `3/2` cannot by itself beat an unrestricted measure in ten
integer coefficients, and it supplies a normalization sanity check for every
future transcription.

## Dependency and source audit

- Theorem 1 is elementary and source-independent.
- `PR20/L-9412` supplies independence of the nine retained phase values and
  verifies the same source condition at dimension one for `beta`.
- `PR20/L-9413` supplies only the certified scalar lower bound (28), with
  `v_2(2)=1` and ordinary reduced rational height.  Equality is not used.
- `PR20/L-9414` supplies the convention (5) and the strict sufficient
  comparison.  This claim does not refute its abstract implication.
- Refreshed `PR20/R-9408` supplies the exact formula (21), its monotonicity in
  the admitted dimension, and the source translation into convention (5).
  Theorem 2 uses its dimension-one instance as well as Theorem 1's
  source-independent dimension-nine floor.
- The base of the logarithm is load-bearing.  Theorem 1 uses `log_p`; at the
  period-ten place `p=2`, this is exactly the `log_2` normalization of
  `L-9414`.
- No experiment or numerical approximation is a proof dependency.  Theorem 2
  is explicitly source-dependent through the inspected transcription in
  `R-9408`; Theorem 1 is not.

## Gap and scope audit

- Equation (20) is a lower bound on any **uniform full-space upper-measure
  exponent**.  It is not a lower bound for a restricted directional family
  such as (29).
- The result does not decide the irrationality of the native period-ten
  value.
- It does not obstruct a direct theorem for the triangular system, a
  phase-sensitive Hermite--Pade determinant, or combined-moment Pade.
- The full scalar closure in Theorem 2 is source-dependent on the quantitative
  formula transcribed in `PR20/R-9408`.  If that transcription changed,
  Theorem 1 and the certified-comparison obstruction would survive, while the
  universal scalar upper bound would require reaudit.
- No exact value is asserted for the scalar liminf in (28); only its certified
  lower bound and the independent limsup upper bound (23) are used.
- The ordinary height includes `a_0`.  Removing the constant coefficient from
  the height convention would be a different statement and cannot be silently
  substituted into `L-9414`.

## Adversarial checks

- For `D=0`, (7) gives the sharp floor one for a nonzero integer `a_0`, since
  `v_p(a_0)<=log_p|a_0|`.
- For one irrational p-adic value (`D=1`), (7) gives the classical
  two-variable Dirichlet floor two.  This distinguishes a linear-independence
  measure from the weaker exponent `>1` needed merely to contradict
  rationality of a fixed scalar.
- Clearing the finitely many negative valuations of the `alpha_i` costs only
  the fixed integer `c` in (15), so nonintegral inputs do not change the
  asymptotic floor.
- Exact zero forms are excluded by (2); without independence, a measure of the
  form (5) is impossible anyway.
- The strict pigeonhole inequality (12) remains correct when
  `(D+1)log_p(H+1)` is an integer because of the explicit minus one in (11).
- Applying the dimension-one measure to `(-p_n,q_n)` uses exactly the same
  reduced height `H_n`; oddness of `q_n` is what makes (26) valuation-neutral.
- The exact exponents newly recorded in `PR20/R-9408` satisfy
  `omega_D>=D+1` for every admitted `1<=D<=9`; this is an independent
  normalization check, not a proof input.

## Suggested next attack

Replace the full source measure in Route A by an upper bound only along the
coefficient rays (29), or attack the triangular system directly.  Any future
claim invoking a full nine-phase measure should first record the unavoidable
floor `omega_9>=10`.  The scalar-approximant/full-measure comparison is now
closed by the dimension-one upper bound, not by treating (28) as an equality.
