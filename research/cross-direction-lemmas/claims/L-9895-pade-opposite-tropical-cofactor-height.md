# L-9895 -- Opposite tropical permutations force cofactor height

Claim ID: `L-9895`
Title: Linear-width adjacent Pade cancellation has unavoidable quadratic projective cofactor height
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: none
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR20/L-9408`, `PR20/L-9410`, `PR20/L-9411`, `L-9884`, `L-9891`
Scope: canonical scalar cofactors of monomial-aligned, equal-allocation adjacent-order Pade errors
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Fix the positive word `W`, its starting height `m`, and the notation

\[
T={64\over81},\qquad r=|W|,\qquad S=S(W)>0,
\qquad Z=T^\zeta
\tag{1}
\]

from `L-9884` and `L-9891`.  The phase exponents are

\[
\gamma_j=j+9A_j(W)+9mj,
\qquad 0\le j<r.
\tag{2}
\]

They strictly increase with `j`, because

\[
\gamma_{j+1}-\gamma_j
=1+9C_{j+1}(W)+9m>0.
\tag{3}
\]

Here and below (3) is asserted for `0<=j<r-1`; it is vacuous when `r=1`.

For the equal-allocation error of order `t`, write

\[
E_t(Y)=Y^{(r+1)t}\sum_{\ell\ge0}g_{t,\ell}Y^\ell
\tag{4}
\]

as in `L-9891`.  Put

\[
N(t,\ell)=(r+1)t+\ell
\tag{5}
\]

and define the last-phase raw exponent

\[
\boxed{
P(t,\ell)
=\gamma_{r-1}+\zeta N(t,\ell)
 +9S\left{
 {rN(t,\ell)(N(t,\ell)-1)\over2}
 +(r-1)N(t,\ell)
 \right}.
}
\tag{6}
\]

All valuations below are valuations of rational numbers, normalized by
`v_p(p)=1`.

## Statement 1 -- exact last-phase 3-adic dominance

Every completed-tail coefficient has exact valuation

\[
\boxed{
v_3(g_{t,\ell})=-4P(t,\ell).
}
\tag{7}
\]

Thus the same combined coefficient which is controlled by phase zero at the
prime `2` is controlled by phase `r-1` at the prime `3`.  When `r=1`, these
are the same sole phase.

### Proof

At block `N=N(t,ell)`, the phase-`j` product of `PR20/L-9411` is

\[
C_jR^{N(N-1)/2}(Z\lambda^j)^N
\prod_c(1-\lambda^{c-rN-j}),
\tag{8}
\]

where `lambda=T^(9S)`.  Every exponent in the product is negative after the
equal-allocation cancellation window.  If `d=rN+j-c>0`, then

\[
v_3(\lambda^{-d})>0,
\qquad
1-\lambda^{-d}\in\mathbb Z_3^\times.
\tag{9}
\]

Hence the phase-`j` valuation is `-4` times

\[
P_j(t,\ell)
=\gamma_j+\zeta N
 +9S\left{{rN(N-1)\over2}+jN\right}.
\tag{10}
\]

Equations (3) and (10) show that `P_j(t,ell)` strictly increases with `j`.
The last phase is therefore the unique phase of least `3`-adic valuation,
so it cannot cancel in the phase sum.  Substituting `j=r-1` proves (7).
**QED**

## Statement 2 -- the two primes select opposite permutations

For `q>=2`, `n>=1`, and `ell>=q-1`, let `Delta_(q,n)(ell)` be the adjacent
Casoratian from `L-9891/(12)`, whose columns are

\[
0,1,\ldots,q-2,\ell.
\tag{11}
\]

Its exact `3`-adic valuation is

\[
\boxed{
v_3(\Delta_{q,n}(\ell))
=-4\left{
 \sum_{i=0}^{q-2}P(n+i,i)
 +P(n+q-1,\ell)
 \right}.
}
\tag{12}
\]

The uniquely least `3`-adic determinant term is the identity permutation.
By `L-9891/(13)`, the uniquely least `2`-adic term is instead the reverse
permutation.  In particular, every such determinant is nonzero at both
places for two different structural reasons.

### Proof

As a function of `N=N(t,ell)`, equation (6) is a quadratic with leading
coefficient `9Sr/2`.  Its exact mixed difference is

\[
P(t,\ell)+P(t+1,\ell+1)
-P(t,\ell+1)-P(t+1,\ell)
=9Sr(r+1)>0.
\tag{13}
\]

For any determinant permutation, all one-variable row and column terms in
the sum of the exponents cancel from the comparison.  The strict
rearrangement inequality therefore makes the increasing row-to-column
assignment the unique maximizer of the sum of the `P` exponents.  Because
`v_3(g)=-4P`, that identity assignment is the unique term of least
valuation.  It assigns row `n+i` to column `i` for `0<=i<=q-2` and the last
row to column `ell`, giving (12).  The reverse `2`-adic assertion is exactly
`L-9891/(13)`. **QED**

## Statement 3 -- exact projective cofactor-height obstruction

Let `d_i`, `0<=i<q`, be the canonical signed cofactors of the first `q-1`
columns, as in `L-9891/(24)`.  Their valuations run in opposite directions:

\[
v_2(d_{i+1})-v_2(d_i)
=U(n+i)-U(n+i+1)-54Sr(q-2-i)<0,
\tag{14}
\]

where `U` is `L-9891/(15)`, while

\[
\boxed{
v_3(d_{i+1})-v_3(d_i)
=4\{P(n+i+1,i)-P(n+i,i)\}>0.
}
\tag{15}
\]

Thus `d_(q-1)` is uniquely smallest at `2`, whereas `d_0` is uniquely
smallest at `3`.

Define the positive integer gaps

\[
S_2=v_2(d_0)-v_2(d_{q-1}),
\qquad
S_3=v_3(d_{q-1})-v_3(d_0).
\tag{16}
\]

They are exactly

\[
\boxed{
S_2
=U(n+q-1)-U(n)
 +54Sr{(q-1)(q-2)\over2},
}
\tag{17}
\]

and

\[
\boxed{
\begin{aligned}
S_3
&=4\sum_{i=0}^{q-2}\{P(n+i+1,i)-P(n+i,i)\}\\
&=4(r+1)(q-1)\left\{
 \zeta+9S\left[
 r(r+1)n+{r(r+2)(q-2)\over2}
 +{r^2\over2}+r-1
 \right]
 \right\}.
\end{aligned}
}
\tag{18}
\]

Clear the rational cofactor vector and divide its coordinates by their
common integer gcd.  If

\[
H_{\rm proj}(d_0:\cdots:d_{q-1})
\tag{19}
\]

denotes the maximum absolute coordinate of the resulting primitive integer
vector, then

\[
\boxed{
H_{\rm proj}(d_0:\cdots:d_{q-1})
\ge \max\{2^{S_2},3^{S_3}\}.
}
\tag{20}
\]

In particular, put

\[
t=n+q-1,
\qquad
{q-1\over t}\longrightarrow\theta,
\qquad 0\le\theta\le1,
\tag{21}
\]

and set `C=r^2+r+1`.  Then

\[
\boxed{
{S_2\over t^2}
\longrightarrow
27Sr\{2C\theta-(C-1)\theta^2\},
}
\tag{22}
\]

\[
\boxed{
{S_3\over t^2}
\longrightarrow
36Sr(r+1)\theta
 \left\{(r+1)-{r\theta\over2}\right\}.
}
\tag{23}
\]

Consequently every fixed positive linear width has a strictly positive
quadratic projective-height cost:

\[
\boxed{
\begin{aligned}
\liminf {\log H_{\rm proj}\over t^2}
\ge\max\bigg\{
&27Sr\{2C\theta-(C-1)\theta^2\}\log2,\\
&36Sr(r+1)\theta
 \left\{(r+1)-{r\theta\over2}\right\}\log3
\bigg\}.
\end{aligned}
}
\tag{24}
\]

### Proof

For each cofactor, the `2`-adic reverse matching from `L-9891` and the
`3`-adic identity matching from Statement 2 are unique.  Comparing the two
minors which omit consecutive rows gives (14) and (15).  Summing (14) from
`i=0` to `q-2` telescopes the `U` terms and sums the remaining column indices,
which proves (17).  Summing (15) gives the first line of (18).  From (6),

\[
P(n+i+1,i)-P(n+i,i)
=(r+1)\left\{
 \zeta+9S\left[
 r(r+1)n+r(r+2)i+{r^2\over2}+r-1
 \right]
 \right\},
\tag{25}
\]

and the arithmetic progression in `i` proves the second line.

Now

\[
v_2(d_0/d_{q-1})=S_2,
\qquad
v_3(d_0/d_{q-1})=-S_3.
\tag{26}
\]

In lowest terms, the numerator of this ratio is divisible by `2^(S_2)` and
its denominator is divisible by `3^(S_3)`.  Those numerator and denominator
divide the corresponding two coordinates of every integral representative
of the projective vector.  This proves (20).

Finally, `U(x)` has quadratic coefficient `27SrC`.  Substituting
`n=t-(q-1)` in (17) gives (22).  Substituting the same relation in (18) gives
(23).  Taking logarithms in (20) proves (24). **QED**

## Statement 4 -- opposite endpoint terms in the coupled denominator

The individual order-`t` common denominator of `PR20/L-9410` obeys

\[
\boxed{
v_2(B_t(1))=0,
\qquad
v_3(B_t(1))=-4H_B(t),
}
\tag{27}
\]

where

\[
\boxed{
H_B(t)
=\zeta rt
 +9S(r+1){rt(rt-1)\over2}.
}
\tag{28}
\]

For the canonical coupled denominator

\[
\mathcal B_{q,n}
=\sum_{i=0}^{q-1}d_iB_{n+i}(1),
\tag{29}
\]

the two places again select opposite endpoints:

\[
\boxed{
v_2(\mathcal B_{q,n})=v_2(d_{q-1}),
\qquad
v_3(\mathcal B_{q,n})=v_3(d_0)-4H_B(n).
}
\tag{30}
\]

Indeed, consecutive `3`-adic summand valuations have the exact positive gap

\[
\boxed{
\begin{aligned}
&v_3(d_{i+1}B_{n+i+1}(1))
 -v_3(d_iB_{n+i}(1))\\
&\qquad=4\left\{
 \zeta+9S(r+1)
 \left[r(n+2i)+{3r-2\over2}\right]
 \right\}>0.
\end{aligned}
}
\tag{31}
\]

### Proof

For the `k`-th term of `B_t(1)`, the Gaussian binomial
`[rt choose k]_lambda` has a unique highest monomial of degree `k(rt-k)`.
Because `v_3(lambda)<0`, this monomial uniquely controls that term at `3`.
Its total `T` exponent is

\[
\zeta k
 +9S(r+1){k(2rt-1-k)\over2}.
\tag{32}
\]

The increment from `k` to `k+1` is

\[
\zeta+9S(r+1)(rt-1-k)>0
\tag{33}
\]

for `0<=k<rt`.  Hence the unique least-valuation term is `k=rt`, and its
exponent is (28).  The `2`-adic unit assertion is `PR20/L-9410`.

At `2`, equation (14) and the unit property make `i=q-1` the unique least
summand of (29), reproducing `L-9891/(27b)`.  At `3`, subtract the increment
of (28) from (15).  Direct simplification gives (31), so `i=0` is the unique
least summand.  Neither endpoint can cancel, proving (30). **QED**

## What this advances

- It resolves the cofactor-vector part of the determinant-height question
  left by `L-9891`: any adjacent-order coupling wide enough to change the
  quadratic cancellation exponent has quadratic projective coefficient
  height.
- It finds a rigid two-place mechanism rather than an archimedean estimate.
  The prime `2` sees the reverse determinant permutation and the prime `3`
  sees the identity permutation.
- It gives exact, independently replayable valuation formulas for every
  cofactor and for the canonical coupled denominator before rational
  reduction.

## Dependency audit

- `PR20/L-9408` supplies the phase exponents and their strict ordering.
- `PR20/L-9410` supplies `B_t`, its Gaussian-binomial degree, and its
  `2`-adic unit property.
- `PR20/L-9411` supplies the exact phasewise root product.
- `L-9884` identifies the completed equal-allocation tail coefficients.
- `L-9891` supplies the reverse `2`-adic permutation, cofactor construction,
  and the function `U`.
- The new ingredients are the last-phase `3`-adic unit calculation, strict
  rearrangement, and elementary projective-height arithmetic.

## Gap audit

- Equation (20) is a height lower bound for the projective cofactor vector,
  not yet for the reduced rational approximant
  `mathcal A_(q,n)/mathcal B_(q,n)`.  Large factors may cancel between those
  two evaluated linear forms.
- Equations (30)--(31) concern the canonical unscaled cofactor construction.
  A common projective rescaling changes both displayed valuations while
  leaving their difference data invariant.
- General polynomial multipliers, nonadjacent orders, unequal allocations,
  and phase-sensitive Hermite--Pade systems lie outside the claim.
- A quadratic coefficient cost does not by itself prove that the period-four
  coupled approximants fail.  A lower bound for their final reduced height is
  still required.
- No irrationality theorem and no Collatz conclusion is claimed.

## Adversarial checks

- At `3`, the factors discarded from (8) are units because their exponents
  are negative.  Extracting them as at the prime `2` would give the wrong
  tropical permutation.
- The last phase, not phase zero, has least `3`-adic valuation; (3) excludes
  a cross-phase tie.
- The sign reversal `v_3(g)=-4P` is why maximizing the exponent gives the
  least valuation.
- Formula (18) remains integral although it is written with halves: if `r`
  is odd then `r+1` is even, and if `r` is even the bracketed half-terms are
  integral.
- For `q=2`, the triangular sums in (17)--(18) reduce to one row comparison,
  as they should.
- Projective height is taken only after clearing all rational denominators
  and removing the full coordinate gcd.

## Remaining uncertainty

Can the evaluated numerator and denominator erase this quadratic projective
cofactor cost through a common rational factor?  The cofactor vector itself
cannot be made small; the remaining escape route is now cancellation in the
map from that vector to the final reduced rational approximant.

## Suggested next attack

Compute the `2`- and `3`-adic valuations of the coupled numerator alongside
(30), or prove a nonarchimedean lower bound for the determinant of the map
from primitive cofactor vectors to evaluated `(mathcal A,mathcal B)`.  Either
would convert the projective-vector obstruction into a reduced-height theorem.
