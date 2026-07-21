# L-9410 — Block Gaussian-binomial Padé family

Claim ID: L-9410  
Title: One rational common denominator simultaneously cancels every phase of a periodic stack block  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9408, L-9409  
Scope: every finite positive height-increment word repeated periodically  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Put

```text
T=64/81.
```

Let

```text
W=d_1...d_r,
r=|W|>=1,
S=S(W)=sum_i d_i,
m>=0.
```

Use the transfer data of L-9408:

```text
e=e(W),
P_W(X)=sum_(j=0)^(r-1) p_j X^j,
p_j=T^[j+9 A_j(W)].
```

At the starting height `m`, define

```text
X=T^(9m),
lambda=T^(9S),
Z=T^e X^r,
R=lambda^r,
C_j=p_j X^j.                                      (1)
```

The repeated-block formula of L-9408 gives the phase decomposition

```text
F_(W,m)=Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j G_j,                         (2)
```

where

```text
G_j
 =sum_(N>=0) R^[N(N-1)/2] (Z lambda^j)^N.          (3)
```

Introduce an auxiliary variable `Y` and write

```text
G_j(Y)
 =sum_(N>=0) R^[N(N-1)/2] (Z lambda^j)^N Y^N,
F_(W,m)(Y)=sum_j C_j G_j(Y).                        (4)
```

Then `F_(W,m)(1)=F_(W,m)`.

## Common denominator

Fix `n>=1` and put

```text
D=rn.                                               (5)
```

For `0<=k<=D`, define the integer

```text
beta_(r,n)(k)
 =[(1-r)k^2+(2r^2 n-r-1)k]/2.                      (6)
```

It is integral because

```text
(r-1)k^2+(r+1)k=(r-1)k(k+1)+2k
```

is even. It is nonnegative on `0<=k<=rn`: for `r>1` the bracket in

```text
2 beta=k[(1-r)k+2r^2 n-r-1]
```

is smallest at `k=rn`, where it equals `(r+1)(rn-1)`; the case `r=1` is
immediate.

Let

```text
[D choose k]_lambda
```

be the Gaussian binomial polynomial evaluated at `lambda`, and put

```text
b_(n,k)
 =(-1)^k Z^k lambda^[beta_(r,n)(k)]
   [D choose k]_lambda,                             (7)
```

```text
B_n(Y)=sum_(k=0)^D b_(n,k)Y^k.                     (8)
```

For each phase `j` and block index `N`, let `Gamma_(j,N)` be the coefficient of
`Y^N` in `B_n(Y) C_j G_j(Y)`. Define

```text
A_n(Y)
 =sum_(N=0)^(D-1) [sum_(j=0)^(r-1) Gamma_(j,N)]Y^N. (9)
```

## Statement 1 — exact simultaneous cancellation

For every `j` and every `N>=D`,

```text
Gamma_(j,N)
 =C_j R^[N(N-1)/2](Z lambda^j)^N
  *prod_(h=0)^(D-1)
    (1-lambda^[h+r^2 n-rN-j]).                      (10)
```

Consequently,

```text
Gamma_(j,N)=0
```

for every

```text
D<=N<D+n,
0<=j<r.                                             (11)
```

Thus one rational denominator of degree `rn` cancels `n` consecutive block
coefficients in every one of the `r` phases simultaneously:

```text
B_n(Y)F_(W,m)(Y)-A_n(Y)
 =sum_(N>=D+n) [sum_j Gamma_(j,N)]Y^N.              (12)
```

### Proof

For `N>=D`, divide the convolution defining `Gamma_(j,N)` by

```text
C_j R^[N(N-1)/2](Z lambda^j)^N.
```

Since `R=lambda^r`, the `k`-th normalized summand is

```text
(-1)^k [D choose k]_lambda
 lambda^[beta-rNk+r k(k+1)/2-jk].                  (13)
```

The definition (6) gives

```text
beta+r k(k+1)/2
 =k(k-1)/2+r^2 n k.                                 (14)
```

Therefore (13) equals

```text
(-1)^k [D choose k]_lambda
 lambda^[k(k-1)/2]
 (lambda^[r^2 n-rN-j])^k.                           (15)
```

The finite `q`-binomial theorem turns the sum over `k` into the product in
(10). If `N=D+t` with `0<=t<n`, choose

```text
h=rt+j.
```

Then `0<=h<=rn-1=D-1`, and the corresponding factor in (10) has exponent
zero. This proves (11) and (12). **QED**

## Statement 2 — exact first error

Put

```text
N_0=(r+1)n,
zeta=e+9mr,                                         (16)
```

and

```text
L_(r,n)
 =n[n r(r^2+r+1)-r^2-2r]/2.                         (17)
```

Then

```text
v_2(B_n(1))=0,                                      (18)
```

and

```text
v_2(B_n(1)F_(W,m)-A_n(1))
 =6[N_0 zeta+9S L_(r,n)].                           (19)
```

The same value is

```text
v_2(F_(W,m)-A_n(1)/B_n(1)).                         (20)
```

### Proof

Every nonconstant term of `B_n(1)` contains the positive power `Z^k`; the
Gaussian binomial is a `2`-adic unit because `lambda` has positive valuation.
Hence `B_n(1)=1 mod 2`, proving (18).

At `N=N_0`, every exponent in the product (10) is negative. For phase `j`,
extracting those powers of `lambda` gives the net `lambda`-exponent

```text
rN_0(N_0-1)/2+jN_0-D(D+2j+1)/2
 =n[n r(r^2+r+1)-r^2-2r+2j]/2.                     (21)
```

The phase `j=0` therefore has exponent `L_(r,n)`. Every phase `j>0` gains
`9Snj` additional powers of `T`, as well as the positive fixed exponent in
`C_j`, so phase zero is the unique term of smallest `2`-adic valuation.

For `N>=N_0`, increasing `N` by one increases the `lambda`-exponent in (10) by

```text
r(N-D)+j>0,
```

and also increases the power of `Z`. Hence the phase-zero term at `N_0` is the
unique smallest term in the entire error and cannot cancel. Its `T`-exponent
is exactly

```text
N_0 zeta+9S L_(r,n),
```

which proves (19). Equation (18) gives (20). **QED**

## Statement 3 — rational-height bound

Let

```text
C_* =max_(0<=j<r)[j+9A_j(W)+9mj],
Q_(r,n)=(r+1)D(D-1)/2,
H_(r,n)=C_*+zeta D+9S Q_(r,n).                      (22)
```

There is a constant `C_(W,m)>0`, independent of `n`, such that

```text
height(A_n(1)/B_n(1))
 <=C_(W,m)(D+1)^3 81^[H_(r,n)].                     (23)
```

### Proof

A monomial in the Gaussian binomial in the `k`-th denominator term has
`lambda`-degree at most `k(D-k)`. From (6),

```text
beta_(r,n)(k)+k(D-k)
 =(r+1)k(2D-1-k)/2
 <=(r+1)D(D-1)/2=Q_(r,n).                           (24)
```

Its power of `Z` is at most `D`.

For a lower coefficient contributing to `A_n`, write

```text
N=k+t<D.
```

Its additional phase-series `lambda`-degree is at most

```text
r t(t-1)/2+(r-1)t.                                  (25)
```

Put `u=D-k`, so `t<=u-1`. The loss from the denominator maximum in (24) is

```text
Q_(r,n)-(r+1)k(2D-1-k)/2
 =(r+1)u(u-1)/2.                                    (26)
```

The right side dominates (25), because at the largest possible `t=u-1`,

```text
(r+1)u(u-1)/2
 -[r(u-1)(u-2)/2+(r-1)(u-1)]
 =(u-1)(u+2)/2>=0.                                  (27)
```

Thus every monomial in both evaluated polynomials has total `T`-exponent at
most `H_(r,n)`. Both can be cleared over the odd denominator
`81^[H_(r,n)]`.

In the real embedding, `0<lambda,Z<1`, and

```text
[D choose k]_lambda
 <=prod_(i>=1)(1-lambda^i)^(-1),                    (28)
```

which is a constant depending only on `W`. Counting the denominator and
convolution terms gives a polynomial factor at most `C_(W,m)(D+1)^3` after
clearing. Reduction can only decrease height, proving (23). **QED**

## Asymptotic approximation gain

Combining (19), (22), and (23),

```text
liminf_(n->infinity)
 v_2(F_(W,m)-A_n/B_n)
 /log_2 height(A_n/B_n)
 >=mu_r,                                             (29)
```

where

```text
mu_r
 =[6/log_2(81)]*(r^2+r+1)/[r(r+1)]
 =[1/log_64(81)]*(1+1/[r(r+1)]).                    (30)
```

The first values are

```text
mu_1=1.419591945535...,
mu_2=1.104127068750...,
mu_3=1.025260849553...,
mu_4=0.993714361875... .                            (31)
```

The scalar family L-9409 is exactly the case `r=1`.

## Dependency audit

- L-9408 supplies the repeated-block phase decomposition.
- L-9409 supplies the scalar model and motivates the normalization; no theorem
  from L-9409 is used without being rederived above.
- The proof uses only the finite `q`-binomial theorem and elementary exact
  rational estimates.

## Gap audit

- The claim constructs approximants; irrationality consequences are separated
  into T-9414 and T-9415.
- The word length `r` need not be its minimal period. The formula remains valid,
  though a shorter representation may give a stronger exponent.
- The estimate `mu_r<=1` for `r>=4` means this universal height calculation no
  longer certifies irrationality. It does not prove that the value is rational
  or that reduced heights cannot be smaller.
- The balanced nonperiodic directive is not periodic and is untouched.

## Adversarial tests

`X-9408` verifies the common-denominator cancellations, exact first error,
denominator-unit property, and reduced rational heights on period-two and
period-three `17/18` words.

## Remaining uncertainty

The period-four boundary and the nonperiodic standard-word limit require
additional height cancellation or a different determinant family.

## Suggested next attack

Exploit common factors in `A_n(1),B_n(1)` or couple adjacent block Padé systems.
Any proposed improvement should report the exact reduced-height gain needed to
raise `mu_4` above one.