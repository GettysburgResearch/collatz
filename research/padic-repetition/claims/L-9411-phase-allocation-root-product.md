# L-9411 — Phase-allocation root-product Padé family

Claim ID: `L-9411`  
Title: Arbitrary phasewise cancellation windows admit one exact root-product denominator  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9408`, `L-9410`  
Scope: every positive periodic increment word and every allocation of Padé cancellation conditions among its phases  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Use the periodic phase decomposition of `L-9410`. Thus

```text
W=d_1...d_r,
r=|W|>=1,
T=64/81,
lambda=T^(9S(W)),
R=lambda^r,
Z=T^e X^r,
F(Y)=sum_(j=0)^(r-1) C_j G_j(Y),
G_j(Y)=sum_(N>=0) R^[N(N-1)/2](Z lambda^j)^N Y^N.
```

Choose nonnegative integers

```text
n_0,...,n_(r-1),
D=sum_j n_j>=1.
```

The intention is to cancel `n_j` consecutive coefficients in phase `j`.
Define the set of root exponents

```text
C(n)
 = union_(j=0)^(r-1)
   { r(D+t)+j : 0<=t<n_j }.
```

It has exactly `D` distinct elements. For `0<=k<=D`, write

```text
E_k(C)
 = sum_(S subset C, |S|=k) lambda^[sum_(c in S)c]
```

for the elementary symmetric sum, with `E_0=1`. Put

```text
b_k
 =(-1)^k Z^k lambda^[-r k(k+1)/2] E_k(C),
B_n(Y)=sum_(k=0)^D b_k Y^k.
```

The displayed exponents are nonnegative: every selected root is at least `rD`,
and the sum of any `k` distinct roots dominates `r k(k+1)/2`.

For phase `j`, let `Gamma_(j,N)` be the coefficient of `Y^N` in

```text
B_n(Y) C_j G_j(Y).
```

Let `A_n(Y)` be the sum of all combined coefficients below degree `D`.

## Statement 1 — exact root-product formula

For every phase `j` and every `N>=D`,

```text
Gamma_(j,N)
 = C_j R^[N(N-1)/2](Z lambda^j)^N
   * product_(c in C(n)) (1-lambda^[c-rN-j]).       (1)
```

Consequently,

```text
Gamma_(j,N)=0
```

for

```text
D<=N<D+n_j.                                         (2)
```

Thus one denominator of total degree `D` imposes exactly the allocated
phasewise cancellation windows:

```text
B_n(Y)F(Y)-A_n(Y)
 = sum_(j=0)^(r-1) sum_(N>=D+n_j) Gamma_(j,N)Y^N.   (3)
```

## Proof

For `N>=D`, divide the `k`-th convolution summand by

```text
C_j R^[N(N-1)/2](Z lambda^j)^N.
```

Since `R=lambda^r`, the ratio of the phase-series coefficients is

```text
R^[-Nk+k(k+1)/2] Z^(-k) lambda^(-jk).
```

After multiplication by `b_k`, the normalized summand is

```text
(-1)^k E_k(C) lambda^[-(rN+j)k].
```

Summing over `k` and using the elementary-symmetric product identity gives

```text
sum_(k=0)^D (-1)^k E_k(C)lambda^[-(rN+j)k]
 = product_(c in C)(1-lambda^[c-rN-j]),
```

which is (1). If `N=D+t` with `0<=t<n_j`, then the root

```text
c=r(D+t)+j
```

belongs to `C(n)` and supplies a zero factor. This proves (2) and (3). **QED**

## Statement 2 — exact denominator exponent before cross-reduction

Let

```text
zeta=e(W)+9m r,
```

so `Z=T^zeta`, and put

```text
Q(n)
 = sum_(c in C(n)) c - rD(D+1)/2.                  (4)
```

Then

```text
Q(n)
 = (r/2)[D^2+sum_j n_j^2]
   -rD+sum_j j n_j.                                (5)
```

The all-root monomial in `B_n(1)` has total `T`-exponent

```text
H_B(n)=zeta D+9S(W)Q(n).                            (6)
```

It is the unique monomial of largest total `T`-exponent: removing any root can
preserve the `lambda` exponent only at the smallest boundary root, but always
loses the positive factor `Z`. Hence the universal odd denominator needed to
clear `B_n(1)` has exact exponent `H_B(n)` before any common-factor reduction
with the numerator approximant.

Equation (5) follows by summing

```text
rD+j, r(D+1)+j, ..., r(D+n_j-1)+j
```

over every phase and subtracting `rD(D+1)/2`.

## Recovery of L-9410

If every `n_j=n`, then `D=rn` and the root set is the consecutive interval

```text
{r^2 n, r^2 n+1, ..., r^2 n+D-1}.
```

The elementary symmetric sums reduce by the finite `q`-binomial theorem to the
coefficients in `L-9410`; every phase receives the same cancellation length.
Thus `L-9410` is the equal-allocation specialization of this lemma.

## Dependency audit

Only the exact periodic phase decomposition of `L-9408` is used. The proof is
finite algebra and the elementary-symmetric product identity. No experiment,
external irrationality theorem, or asymptotic estimate is a dependency.

## Gap audit

- The lemma constructs a larger denominator class but does not claim unequal
  allocation improves irrationality exponents.
- Cross-phase cancellation after the allocated windows is not excluded.
- Reduction by a common numerator/denominator factor can lower the final height;
  the exponent in (6) is the exact pre-reduction denominator scale.
- A genuinely coupled determinant need not be representable by one root set
  `C(n)` and remains outside this lemma.

## Adversarial tests

`X-9410` enumerates 657,774 finite allocation vectors and checks the asymptotic
phase functionals derived from (1), (5), and the first surviving phase
coefficients. The universal theorem is proved in `T-9416`; the experiment is not
a proof dependency.

## Suggested next attack

Use the exact root-product formula to classify what additional mechanism could
beat equal allocation: systematic cross-phase cancellation, a reduced-height
common factor, or a determinant not expressible as a single phasewise root
product.