# T-9824 -- The visible Vandermonde leaves a positive cubic-height Schur quotient

Claim ID: `T-9824`
Title: The normalized combined-moment alternant is an exact positive Schur sum whose principal specialization still has cubic two-place height
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-period-ten`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `T-9821`
Scope: the canonical combined-moment Pade minors for every positive periodic word; especially period ten
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Retain `T-9821/(1)--(3)`.  Thus

\[
 P_W(Xz)=\sum_{h=0}^{r-1}C_hz^h,\qquad
 C_h=T^{\gamma_h},qquad
 0=\gamma_0<\cdots<\gamma_{r-1},                    \tag{1}
\]

and `lambda=T^(9S)`.  For independent variables
`z_0,...,z_(n-1)`, define the row-factor-stripped base alternant

\[
 \mathcal A_n(\mathbf z)
 =\det\left[z_i^{rj}P_W(X\lambda^jz_i)\right]_{0\le i,j<n},
 \qquad
 V_n(\mathbf z)=\det(z_i^j)_{0\le i,j<n}.           \tag{2}
\]

## Theorem 1 -- exact positive Schur expansion

For `mathbf h=(h_0,...,h_(n-1)) in {0,...,r-1}^n`, put

\[
 \mu(\mathbf h)
 =\bigl((r-1)(n-1)+h_{n-1},\ldots,
         (r-1)+h_1,h_0\bigr).                       \tag{3}
\]

This is a partition, and

\[
 \boxed{
 {\mathcal A_n(\mathbf z)\over V_n(\mathbf z)}
 =\sum_{\mathbf h\in\{0,\ldots,r-1\}^n}
   \left(\prod_{j=0}^{n-1}C_{h_j}\lambda^{jh_j}\right)
   s_{\mu(\mathbf h)}(\mathbf z).
 }                                                   \tag{4}
\]

In particular the quotient is a symmetric polynomial with nonnegative
rational coefficients.  It has exact minimum and maximum total degrees

\[
 { (r-1)n(n-1)\over2},qquad
 { (r-1)n(n+1)\over2},                              \tag{5}
\]

selected respectively by `h_j=0` and `h_j=r-1` for every `j`.

### Proof

Expanding (2) independently in its columns gives

\[
 \mathcal A_n
 =\sum_{\mathbf h}
 \left(\prod_jC_{h_j}\lambda^{jh_j}\right)
 \det(z_i^{rj+h_j})_{i,j}.                          \tag{6}
\]

The exponents `rj+h_j` are strictly increasing.  The alternant definition of
a Schur polynomial therefore identifies its quotient by `V_n` with
`s_(mu(mathbf h))`, proving (4).  Adjacent parts in (3) differ by
`r-1+h_j-h_(j-1)>=0`.  Schur polynomials have nonnegative integral
coefficients, while every weight in (4) is positive.  Finally,

\[
 |\mu(\mathbf h)|
 ={(r-1)n(n-1)\over2}+\sum_jh_j,                    \tag{7}
\]

which proves (5). **QED**

## Theorem 2 -- the Vandermonde quotient retains exact cubic height

Specialize

\[
 z_i=\lambda^i\quad(0\le i<n),qquad
 \mathcal Q_n
 ={\mathcal A_n(1,\lambda,\ldots,\lambda^{n-1})
   \over V_n(1,\lambda,\ldots,\lambda^{n-1})}.       \tag{8}
\]

Put

\[
 K_n={n(n-1)(n-2)\over6},qquad
 L_n={n(n-1)(2n+5)\over6},qquad
 \gamma_*=\gamma_{r-1}.                             \tag{9}
\]

Then

\[
 \boxed{v_2(\mathcal Q_n)=6\cdot9S(r-1)K_n,}        \tag{10}
\]

\[
 \boxed{
 v_3(\mathcal Q_n)
 =-4\{n\gamma_*+9S(r-1)L_n\}.
 }                                                   \tag{11}
\]

Consequently, for every `r>=2`,

\[
 \log_2 H(\mathcal Q_n)
 \ge\max\left\{
 54S(r-1)K_n,
 4\log_2(3)\{n\gamma_*+9S(r-1)L_n\}
 \right\}
 =\Theta(n^3).                                      \tag{12}
\]

### Proof

At `2`, strict rearrangement in the numerator alternant selects `h_j=0` and
the reverse permutation.  Its `T`-exponent is
`9Sr sum_i i(n-1-i)`.  The same reverse permutation in `V_n` has exponent
`9S sum_i i(n-1-i)`.  Their difference is `9S(r-1)K_n`, proving (10).

At `3`, the unique selectors are `h_j=r-1` and the identity permutation.
After subtracting the identity term of `V_n`, the remaining `T`-exponent is

\[
 n\gamma_*+9S(r-1)
 \left\{\sum_{i=0}^{n-1}i^2+2\sum_{i=0}^{n-1}i\right\}
 =n\gamma_*+9S(r-1)L_n.                             \tag{13}
\]

Since `v_2(T)=6` and `v_3(T)=-4`, this proves (10)--(11).  The elementary
height lower bounds at the primes `2` and `3` give (12). **QED**

## Exact method boundary

The ordinary Vandermonde identified in `T-9821/(24)` is therefore a genuine
common factor, and (4) explains the residual alternant without cancellation
or sign ambiguity.  But (10)--(12) prove that removing this factor alone does
not turn the normalized minors into quadratic-height objects: for period ten
their residual Schur quotient already has exact cubic local height.

This is not a no-go for the combined-moment Pade program.  Cramer **ratios**
of two such quotients have only the quadratic endpoint differences proved in
`T-9821/(15)--(16)`.  What remains open is whether their cubic integer unit
parts share further content or cancel after forming the evaluated numerator
and denominator.  Thus any proof of `T-9821/(23)` must find a common factor or
global height mechanism beyond the ordinary Vandermonde; positivity and that
visible factor by themselves cannot supply it.

## Dependency and gap audit

- `T-9821` supplies the combined moments and opposite tropical selectors.
  The new content is the exact Schur expansion (4) and the residual
  specialization orders (10)--(12).
- Polynomial coefficient positivity is not arithmetic specialization
  independence and does not prove the period-ten value irrational.
- The cubic lower bound concerns each separately normalized base alternant.
  It is not a cubic lower bound for every Cramer ratio, whose endpoint orders
  cancel to quadratic size.
- At `r=1`, the partitions are constant and the cubic terms vanish, agreeing
  with the scalar Gaussian-binomial case.
