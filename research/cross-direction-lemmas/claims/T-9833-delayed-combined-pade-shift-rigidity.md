# T-9833 -- Delayed combined-moment Pade systems retain the cubic Schur-core barrier

Claim ID: `T-9833`
Title: Moving the combined cancellation window changes the quadratic endpoint budget but does not remove the prime-to-six cubic core
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave22-fixed-width-sunit`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9821`, `T-9824`, `T-9830`; branch-qualified `PR20/L-9418`, `R-9410`, and `Q-9413` at `82ca2f932438a9fe0897704ba62959ca23ec830f`
Scope: every positive periodic stack word of length at least two; especially the first unresolved primitive period ten
Related counterexample candidates: issue #4 periodic stack frontier; PR #38 atom `ACL-N024`; no `K-####` candidate

## Motivation

Live PR #20 proves that moving a phasewise root-product cancellation window
improves the elementary fixed-period range from three to nine but remains just
below the period-ten threshold. The direct combined-moment system spends only
one condition per combined coefficient, so it is essential to test whether
the same delay removes its global-height obstruction. This claim computes the
shift exactly and distinguishes local endpoint gain from normalized Schur-core
height.

## Setup

Retain the notation of `T-9830`:

\[
 r\ge2.
\tag{0}
\]

\[
 T={64\over81},\qquad
 \lambda=T^{9S},\qquad
 R=\lambda^r,\qquad
 Z=T^\zeta,
\tag{1}
\]

\[
 P_W(Xz)=\sum_{h=0}^{r-1}C_hz^h,qquad
 C_h=T^{\gamma_h},\qquad
 0=\gamma_0<\cdots<\gamma_{r-1}=\gamma_*.
\tag{2}
\]

Put

\[
 q=9Sr,
 \qquad
 c=\zeta+9S(r-1),
\tag{3}
\]

and use the combined moments

\[
 u_N=R^{N(N-1)/2}Z^NP_W(X\lambda^N),
 \qquad
 H(Y)=\sum_{N\ge0}u_NY^N.
\tag{4}
\]

Write `H_2` and `H_infinity` for the 2-adic and real values of the convergent
series, respectively; they are not identified.

Fix integers

\[
 n\ge1,
 \qquad M\ge n+1,
 \qquad a=M-n\ge1.
\tag{5}
\]

The letter `M` in this claim is a cancellation-window location. It is not the
base of a completion chart.

## Statement 1 -- the delayed combined system and its exact Cramer factors

There is a unique polynomial

\[
 B_{n,M}(Y)=\sum_{k=0}^n b_{n,M,k}Y^k,
 \qquad b_{n,M,0}=1,
\tag{6}
\]

for which the coefficients of `B_(n,M)H` at degrees

\[
 M,M+1,\ldots,M+n-1
\tag{7}
\]

vanish. Define the shifted numerator explicitly by

\[
 A_{n,M}(Y)
 =\sum_{N=0}^{M-1}[Y^N]\bigl(B_{n,M}(Y)H(Y)\bigr)Y^N.
\tag{7a}
\]

Thus

\[
 B_{n,M}(Y)H(Y)-A_{n,M}(Y)
 =\sum_{\ell\ge0}\varepsilon_{n,M,\ell}Y^{M+n+\ell}.
\tag{8}
\]

For `0<=k<=n`, put

\[
 \boxed{
 \alpha_{n,M,k}=k\{\zeta+q(M-1)\},}
\tag{9}
\]

\[
 \boxed{
 \beta_{n,M,k}
 =k\{c+q(M+n-k-1)\}.}
\tag{10}
\]

The normalized base Schur core has degree

\[
 \boxed{
 d_{n,M}
 =d_n+9S(r-1)n(M-n),}
\tag{11}
\]

where

\[
 d_n
 =n\gamma_*+{9S(r-1)\over6}n(n-1)(n+7)
\tag{12}
\]

is the canonical degree from `T-9830`.

More precisely, there are monic polynomials

\[
 F_{n,M,k}(T)\in\mathbf Z_{\ge0}[T],
 \qquad F_{n,M,k}(0)=1,
\tag{13}
\]

of degrees

\[
 \boxed{
 d_{n,M,k}
 =d_{n,M}+\beta_{n,M,k}-\alpha_{n,M,k}.}
\tag{14}
\]

Define

\[
 G_{n,M,k}
 =81^{d_{n,M,k}}F_{n,M,k}(64/81).
\tag{15}
\]

Then

\[
 G_{n,M,k}\in\mathbf Z_{>0},
 \qquad \gcd(G_{n,M,k},6)=1,
\tag{16}
\]

and

\[
 \boxed{
 b_{n,M,k}=(-1)^k
 {2^{6\alpha_{n,M,k}}G_{n,M,k}
  \over
  3^{4\beta_{n,M,k}}G_{n,M,0}}.}
\tag{17}
\]

Uniformly in the delay `M`,

\[
 81^{d_{n,M,k}}
 \le G_{n,M,k}
 \le81^{d_{n,M,k}}
 r^n(3r-1)^{n(n-1)/2}.
\tag{18}
\]

Consequently

\[
 \log_2G_{n,M,k}
 =d_{n,M,k}\log_2 81+O_r(n^2).
\tag{19}
\]

### Proof

Write `c_j=b_(n,M,n-j)`. The equations in (7) have coefficient matrix

\[
 \left(u_{a+i+j}\right)_{0\le i,j<n}.
\tag{20}
\]

This is the `T-9821` minor with row set

\[
 a,a+1,\ldots,a+n-1
\tag{21}
\]

and column set `0,1,...,n-1`; it is nonzero. Cramer's rule replaces the
column `n-k` by column `n`.

The replacement raises the column sum by `k` and raises the column
binomial sum by

\[
 {k(2n-k-1)\over2}.
\tag{22}
\]

In the reverse pairing selected at two, it additionally raises the dot
product by

\[
 \sum_{i=0}^{k-1}(a+i)
 =ka+{k(k-1)\over2}.
\tag{23}
\]

Substitution in `T-9821/(8)` gives (9). In the identity pairing selected at
three, the dot-product increment is

\[
 \sum_{i=n-k}^{n-1}(a+i)
 =k\left(M-{k+1\over2}\right).
\tag{24}
\]

Substitution in `T-9821/(9)` gives (10).

It remains to track the prime-to-six core. Shifting every row index by `a`
multiplies the phase-vector summand of the normalized alternant by

\[
 \lambda^{a\sum_i h_i}.
\tag{25}
\]

The unique least selector still has every `h_i=0`. The unique greatest
selector still has every `h_i=r-1`, and its exponent is increased by

\[
 9Sa n(r-1).
\tag{26}
\]

Division by the ordinary Vandermonde is unchanged by the common row shift.
Thus the base exponent span increases by exactly (26), proving (11).
Replacing one column changes the span by `beta-alpha`, proving (14).

The Schur expansion used in `T-9824` still has nonnegative integral
coefficients. Its endpoint selectors have coefficient one, proving (13).
At `T=1`, the extra shift factor (25) is one, while the column gaps remain at
most two. The Weyl-factor estimate of `T-9830` is therefore unchanged and
gives (18). Homogenization at `64/81`, together with the constant and monic
endpoint coefficients, proves (15)--(19). The Cramer sign and the endpoint
valuation differences give (17). **QED**

## Statement 2 -- exact first error after an arbitrary delay

Put

\[
 \boxed{
 V_{n,M}
 =\zeta(M+n)
 +{q\over2}\{M^2+(2n-1)M-2n\}.}
\tag{27}
\]

Then

\[
 \boxed{v_2(B_{n,M}(1))=0,}
\tag{28}
\]

and

\[
 \boxed{
 v_2\left(
 H_2-{A_{n,M}(1)\over B_{n,M}(1)}
 \right)=6V_{n,M}.}
\tag{29}
\]

### Proof

Equation (9) is positive for every `k>0`, so the constant term is the unique
2-adic unit in `B_(n,M)(1)`. This proves (28).

The coefficient `epsilon_(n,M,ell)` is the bordered determinant with row set

\[
 a,a+1,\ldots,M-1,M+\ell
\tag{30}
\]

and column set `0,1,...,n`, divided by the base determinant (20). Applying
`T-9821/(8)` gives

\[
 {1\over6}v_2(\varepsilon_{n,M,\ell})
 =\zeta(M+n+\ell)
 +q\left\{
 { (M+\ell)(M+\ell-1)\over2}
 +{n(n-1)\over2}
 +\sum_{i=0}^{n-1}(a+i)
 \right\}.
\tag{31}
\]

At `ell=0`, the bracket simplifies to

\[
 {M^2+(2n-1)M-2n\over2},
\tag{32}
\]

which gives (27). Increasing `ell` by one raises (31) by

\[
 \zeta+q(M+\ell)>0.
\tag{33}
\]

Hence the first error coefficient is nonzero and is the unique term of least
2-adic valuation in the evaluated convergent error series. Division by the
2-adic unit in (28) proves (29). **QED**

## Statement 3 -- exact raw height and the delayed outside-prime gcd gate

For `t>=0`, put

\[
 U_t=ct+q{t(t-1)\over2}+\gamma_*.
\tag{34}
\]

The last denominator coefficient has exponent

\[
 \beta_{n,M,n}=n\{c+q(M-1)\}.
\tag{35}
\]

Define

\[
 \boxed{
 L_{n,M}=\beta_{n,M,n}+U_{a-1}.}
\tag{36}
\]

Then

\[
 \boxed{
 v_3(B_{n,M}(1))=-4\beta_{n,M,n},
 \qquad
 v_3(A_{n,M}(1))=-4L_{n,M}.}
\tag{37}
\]

Both evaluated values are 2-adic units. With

\[
 \mathcal D_{n,M}=3^{4L_{n,M}}G_{n,M,0},
\tag{38}
\]

put

\[
 \widehat A_{n,M}=\mathcal D_{n,M}A_{n,M}(1),
 \qquad
 \widehat B_{n,M}=\mathcal D_{n,M}B_{n,M}(1).
\tag{39}
\]

These are integers and

\[
 \boxed{
 \gcd(\widehat A_{n,M},\widehat B_{n,M})
 \text{ is coprime to }6.}
\tag{40}
\]

As `n->infinity` through any choices `M>=n+1`,

\[
 B_{n,M}(1)\longrightarrow1,
 \qquad
 A_{n,M}(1)\longrightarrow H_\infty>0
\tag{41}
\]

in the real embedding. Therefore, if

\[
 N_{n,M}^{\rm raw}
 =\max\{|\widehat A_{n,M}|,|\widehat B_{n,M}|\},
\tag{42}
\]

then

\[
 \boxed{
 \log_2N_{n,M}^{\rm raw}
 =(d_{n,M}+L_{n,M})\log_2 81+O_r(n^2).}
\tag{43}
\]

For

\[
 g_{n,M}=\gcd(|\widehat A_{n,M}|,|\widehat B_{n,M}|),
\tag{44}
\]

the reduced rational height is exactly

\[
 \boxed{
 H\left({A_{n,M}(1)\over B_{n,M}(1)}\right)
 ={N_{n,M}^{\rm raw}\over g_{n,M}}.}
\tag{45}
\]

Thus every reduction not visible in (43) is again an outside-prime gcd
supported at primes at least five.

### Proof

The quantities `beta_(n,M,k)` are strictly increasing in `k`. Indeed,

\[
 \beta_{k+1}-\beta_k
 =c+q(M+n-2k-2),
\tag{46}
\]

whose value at `k=n-1` is `c+q(M-n)>0`. This proves the first equality in
(37).

Let

\[
 H_t=\sum_{j=0}^tu_j.
\tag{47}
\]

The phase `h=r-1` in `u_t` is the unique term of greatest `T`-exponent, and
the exponents grow strictly with `t`. Hence

\[
 v_3(H_t)=-4U_t.
\tag{48}
\]

Reordering the finite convolution gives

\[
 A_{n,M}(1)
 =\sum_{k=0}^n b_{n,M,k}H_{M-1-k}.
\tag{49}
\]

For `0<=k<n`, direct subtraction gives

\[
 \bigl(\beta_{k+1}+U_{M-2-k}\bigr)
 -\bigl(\beta_k+U_{M-1-k}\bigr)
 =q(n-k)>0.
\tag{50}
\]

Thus the unique 3-adically dominant term in (49) has `k=n` and
`t=M-1-n=a-1`, proving the second equality in (37).

Equations (17), (36), and (48)--(50) prove the integrality in (39). At two,
the degree-zero contributions make both `A(1)` and `B(1)` units. At three,
the first raw integer in (39) is a unit, while the second has valuation
`4U_(a-1)`. Since `G_(n,M,0)` is prime to six, (40) follows.

The real coefficient bound in `T-9830/(76)` is unchanged by the shift: the
extra phase factors in (25) have absolute value at most one. Since
`alpha_(n,M,1)>=zeta+q n`, the proof of `T-9830/(80)` gives, uniformly in
`M>=n+1`,

\[
 \sum_{k=1}^n|b_{n,M,k}|\longrightarrow0.
\tag{51}
\]

Equation (49), boundedness of the positive partial sums `H_t`, and
`M-n>=1` give (41). Finally, (18), (38), and (41) show that both raw integers
have size comparable to `mathcal D_(n,M)` up to the factor allowed in (18).
This proves (43). Division by the ordinary gcd proves (45). **QED**

## Statement 4 -- arbitrary delay cannot cross the rationality threshold without gcd cancellation

Let `M_n>=n+1` be arbitrary and abbreviate

\[
 V_n=V_{n,M_n},\qquad
 L_n=L_{n,M_n},\qquad
 d_n'=d_{n,M_n}.
\tag{52}
\]

Then

\[
 \boxed{
 \limsup_{n\to\infty}{V_n\over d_n'+L_n}\le1.}
\tag{53}
\]

Consequently the exponent supplied by the unreduced raw pair satisfies

\[
 \boxed{
 \limsup_{n\to\infty}
 {6V_n\over\log_2N_{n,M_n}^{\rm raw}}
 \le\log_{81}(64)
 =0.9549982179\ldots<1.}
\tag{54}
\]

This holds for every delay scale, including delays growing faster than every
fixed multiple of `n`.

### Proof

Pass to an arbitrary subsequence. If

\[
 {M_n\over n^{3/2}}
\tag{55}
\]

is bounded, pass again so that it converges to `lambda>=0`. When `lambda=0`,
the cubic term

\[
 {3\over2}S(r-1)n^3
\tag{56}
\]

in `d_n'` dominates `V_n`, so the ratio in (53) tends to zero. When
`lambda>0`, the `n^3` terms give

\[
 \lim {V_n\over d_n'+L_n}
 ={3r\lambda^2\over3r\lambda^2+(r-1)}<1.
\tag{57}
\]

The shift term `9S(r-1)n(M_n-n)` is only `O(n^(5/2))` in this scaling and
does not enter (57).

If instead `M_n/n^(3/2)->infinity`, the common leading term of `V_n` and
`L_n` is

\[
 {q\over2}M_n^2.
\tag{58}
\]

All remaining terms in `V_n` and `L_n`, as well as both terms
`O(nM_n)+O(n^3)` in `d_n'`, are `o(M_n^2)`. Therefore

\[
 {V_n\over d_n'+L_n}\longrightarrow1.
\tag{59}
\]

Every subsequence has a further subsequence covered by one of these cases,
which proves (53). Equation (43) turns (53) into (54). **QED**

## Period-ten consequence

For `r=10`, the exact shift contribution is quadratic at every delay linear
in `n`:

\[
 d_{n,M}
 ={27\over2}S n^3+81Sn(M-n)+O_{W,m}(n^2).
\tag{60}
\]

while the exact error and local endpoint denominators remain quadratic. Thus
under the same linear-delay hypothesis `M-n=O(n)`, an `O(n^2)`
primitive-height bound still requires

\[
 \boxed{
 \log_2g_{n,M}
 =54S\log_2(3)n^3
 +O_{W,m}\!\left(n^2+n(M-n)+(M-n)^2\right),}
\tag{61}
\]

entirely at primes at least five. This is the same almost-total cubic
cancellation required by `T-9830`.

For reference, without any linear-delay restriction the full period-ten raw
exponent is

\[
 \boxed{
 d_{n,M}+L_{n,M}
 ={27\over2}Sn^3+171Sn(M-n)+45S(M-n)^2
 +O_{W,m}\!\left(n^2+M-n\right).}
\tag{62}
\]

Thus arbitrary-delay gcd accounting should use (62), while (61) is the clean
linear-delay specialization relevant to preserving quadratic order in `n`.

Superlinear delay does not evade the obstruction. Once the delayed moment
tail dominates the cubic core, the raw accuracy-to-height exponent tends to
the scalar base ceiling `log_81(64)<1`, as (54) shows. Hence moving the
combined cancellation window alone cannot close `PR20/Q-9413`.

The remaining live mechanisms are genuinely arithmetic:

1. a large specialization gcd among the shifted Schur cores;
2. a cross-minor polynomial factor not removed by the ordinary Vandermonde;
3. a phase-sensitive Hermite--Pade construction with a different height
   balance; or
4. the native homogeneous order-two route.

## Adversarial tests

An independent reviewer rederived the shifted row and column sums, bordered
error, Schur homogeneity shift, and unique 3-adic numerator maximizer. A
symbolic exact audit verified the closed formulas for every exponent
difference and for `d_(n,M)+L_(n,M)-V_(n,M)`. Two boundary tests are essential:

- at `M=n`, the numerator maximizer is `k=n-1,t=0`, so Statement 3 is not
  extended to the canonical edge;
- at `r=1`, the cubic Schur term vanishes and `M=n+1` gives
  `V/(d+L)->3/2`, so the arbitrary-delay ceiling is correctly restricted to
  `r>=2`.

## Dependency audit

- `T-9821` supplies every shifted minor's nonvanishing and exact opposite
  endpoint selectors.
- `T-9824` supplies the positive Schur expansion after ordinary Vandermonde
  division.
- `T-9830` supplies the canonical core normalization and the real coefficient
  bounds; this claim recomputes every change caused by the row shift.
- `PR20/L-9418` delays a different, phasewise root-product family. The present
  theorem shows that applying the same strategic idea to the direct combined
  moment system does not remove its global-height barrier.

## Gap audit

- Equation (54) concerns the raw determinant clearing. A large gcd can lower
  primitive height and is not ruled out.
- The theorem does not prove a lower bound for `g_(n,M)` or an upper bound
  refuting it.
- No period-ten irrationality and no Collatz conclusion are claimed.

## Remaining uncertainty

The shifted determinant and raw-height analysis are exact. The arithmetic
size of the prime-to-six specialization gcd is completely open, both for one
delay and across delays. The theorem therefore closes only window movement as
an ungcded-height mechanism.

## Suggested next attack

Compute the shifted cores modulo primes at least five and compare them across
`k` and `M`. The delay parameter supplies an additional arithmetic variable,
but (61) quantifies the size of the correlation needed at every linear delay.
Any successful modular-resultant theorem must account for that full cubic
amount rather than only the quadratic endpoint factors.
