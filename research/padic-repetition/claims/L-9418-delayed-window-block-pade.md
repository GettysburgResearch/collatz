# L-9418 — Delayed-window block Gaussian-binomial Padé family

Claim ID: `L-9418`  
Title: A fixed-degree periodic block denominator may place its exact cancellation window at an independent later depth  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9408`; the finite `q`-binomial theorem  
Scope: every positive periodic stack increment word of arbitrary finite period  
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
S=S(W),
m>=0.
```

Use the exact transfer data of `L-9408`:

```text
e=e(W),
P_W(X)=sum_(j=0)^(r-1) p_j X^j,
p_j=T^[j+9A_j(W)].
```

At starting height `m`, define

```text
X=T^(9m),
lambda=T^(9S),
R=lambda^r,
Z=T^e X^r=T^zeta,
zeta=e+9mr,
C_j=p_j X^j.
```

Then

```text
F_(W,m)(Y)
 =sum_(j=0)^(r-1) C_j
   sum_(N>=0) R^[N(N-1)/2](Z lambda^j)^N Y^N,        (1)
```

and `F_(W,m)(1)=Theta(m;W^infinity)`.

Fix an order `n>=1`, put

```text
D=rn,                                                 (2)
```

and choose an independent integer delay

```text
M>=D+1.                                               (3)
```

The old equal-window construction is recovered when the window is placed as
early as its degree permits. The present lemma allows the same degree to place
its zero window later.

## Delayed denominator

For `0<=k<=D`, define

```text
beta_(r,n,M)(k)
 =[(1-r)k^2+(2rM-r-1)k]/2.                           (4)
```

This is an integer: modulo two, `k^2` may be replaced by `k`, and the total
coefficient becomes `-2r`. It is nonnegative on `0<=k<=D`; the bracket in

```text
2 beta
 =k[(1-r)k+2rM-r-1]
```

is smallest at `k=D`, and (3) makes that value positive.

Let `[D choose k]_lambda` be the Gaussian binomial polynomial evaluated at
`lambda`, and put

```text
b_k
 =(-1)^k Z^k lambda^[beta_(r,n,M)(k)]
   [D choose k]_lambda,

B_(n,M)(Y)=sum_(k=0)^D b_k Y^k.                      (5)
```

For phase `j` and block `N`, let `Gamma_(j,N)` be the coefficient of `Y^N` in
`B_(n,M)(Y) C_j G_j(Y)`. Define

```text
A_(n,M)(Y)
 =sum_(N=0)^(M-1)
   [sum_(j=0)^(r-1) Gamma_(j,N)]Y^N.                 (6)
```

## Statement 1 — exact delayed product and zero window

For every phase `0<=j<r` and every `N>=D`,

```text
boxed:
Gamma_(j,N)
 =C_j R^[N(N-1)/2](Z lambda^j)^N
  *prod_(h=0)^(D-1)
    (1-lambda^[h+rM-rN-j]).                          (7)
```

Consequently,

```text
boxed:
Gamma_(j,N)=0
```

for every

```text
M<=N<M+n,
0<=j<r.                                               (8)
```

Thus

```text
B_(n,M)(Y)F_(W,m)(Y)-A_(n,M)(Y)
 =sum_(N>=M+n)[sum_j Gamma_(j,N)]Y^N.                (9)
```

### Proof

For `N>=D`, divide the `k`-th convolution summand by

```text
C_j R^[N(N-1)/2](Z lambda^j)^N.
```

Because `R=lambda^r`, the normalized summand is

```text
(-1)^k [D choose k]_lambda
 lambda^[beta-rNk+r k(k+1)/2-jk].                   (10)
```

Equation (4) gives

```text
beta+r k(k+1)/2
 =k(k-1)/2+rMk.                                      (11)
```

The finite `q`-binomial theorem therefore turns the sum over `k` into (7).
If `N=M+t` with `0<=t<n`, choose

```text
h=rt+j.
```

Then `0<=h<=rn-1=D-1`, and the corresponding factor in (7) is
`1-lambda^0=0`. This proves (8) and (9). **QED**

## Statement 2 — exact first error

Put

```text
N_0=M+n,                                              (12)
```

and

```text
L_(r,n,M)
 =[rN_0(N_0-1)-D(D+1)]/2.                            (13)
```

Then

```text
boxed:
v_2(B_(n,M)(1))=0,                                   (14)
```

and

```text
boxed:
v_2(
 F_(W,m)(1)-A_(n,M)(1)/B_(n,M)(1)
 )
 =6[N_0 zeta+9S L_(r,n,M)].                          (15)
```

### Proof

Every nonconstant term of `B_(n,M)(1)` contains the positive power `Z^k`; all
other displayed powers have nonnegative `2`-adic valuation. Hence
`B_(n,M)(1)=1 mod 2`, proving (14).

At `N=N_0`, every exponent in the product (7) is negative. Extracting those
powers gives, for phase `j`, the net `lambda` exponent

```text
L_(r,n,M)+j(N_0-D).                                  (16)
```

Phase zero has `C_0=1`. Every phase `j>0` has both the positive increment in
(16) and a positive fixed exponent in `C_j`, so phase zero is uniquely smallest
at the prime two and cannot cancel.

For `N>=N_0`, increasing `N` by one raises the extracted `lambda` exponent in
phase `j` by

```text
r(N-D)+j>0,
```

and also raises the power of `Z`. Thus the phase-zero contribution at `N_0` is
the unique term of least `2`-adic valuation in the entire evaluated error. Its
`T` exponent is `N_0 zeta+9S L_(r,n,M)`, proving (15). **QED**

## Statement 3 — exact common-height scale

Put

```text
Q_A(r,n,M)
 =[D^2+D+rM^2-rM-2M+2]/2,                            (17)
```

```text
C_*=max_(0<=j<r)[j+9A_j(W)+9mj],                     (18)
```

and

```text
H_(r,n,M)=C_*+zeta M+9S Q_A(r,n,M).                  (19)
```

There is a constant `C_(W,m)>0`, independent of `n` and `M`, such that

```text
boxed:
height(A_(n,M)(1)/B_(n,M)(1))
 <=C_(W,m)(M+D+1)^3 81^[H_(r,n,M)].                  (20)
```

Here height means `max(|p|,|q|)` after rational reduction.

### Proof

A monomial of `[D choose k]_lambda` has degree at most `k(D-k)`. For a
coefficient of `B_(n,M)`, its `lambda` exponent is therefore at most

```text
beta_(r,n,M)(k)+k(D-k).                              (21)
```

For a monomial contributing to a coefficient below `M` in `A_(n,M)`, write
`N=k+t<M`. Its additional phase-series exponent is at most

```text
r t(t-1)/2+(r-1)t.                                   (22)
```

For fixed `k`, (21)+(22) is largest at `t=M-1-k`. Direct simplification gives

```text
[rM^2-rM-2M+2-k^2+(2D+1)k]/2.                       (23)
```

The concave quadratic in `k` is maximized on `0<=k<=D` at `k=D`, and its value
is exactly (17). The denominator monomials obey the same bound; condition (3)
places their endpoint maximum below (17).

Every numerator term has `Z` exponent `<M` and phase factor at most `T^C_*`.
Thus the evaluated numerator and denominator may both be cleared over the odd
denominator in (19).

In the real embedding, `0<lambda,Z<1`, and the Gaussian binomials are bounded by
one Euler-product constant depending only on `W`. Counting the finitely many
convolution terms contributes only the polynomial factor in (20). Rational
reduction can only lower height. **QED**

## Statement 4 — asymptotic exponent and optimal delay

Let `n` tend to infinity through any sequence for which

```text
M/n -> alpha,
alpha>=r.                                             (24)
```

Then (15) and (20) give

```text
boxed:
liminf
 v_2(F_(W,m)(1)-A_(n,M)(1)/B_(n,M)(1))
 /log_2 height(A_(n,M)(1)/B_(n,M)(1))
 >=mu_r^delay(alpha),                                 (25)
```

where

```text
boxed:
mu_r^delay(alpha)
 =log_81(64)*[((alpha+1)^2-r)/(alpha^2+r)].           (26)
```

The shape in (26) is uniquely maximized on `alpha>=r` at

```text
boxed:
alpha_r^*
 =(2r-1+sqrt(4r^2+1))/2.                             (27)
```

### Proof

The quadratic part of (13) is

```text
(r/2)[(alpha+1)^2-r]n^2,
```

while the quadratic part of (17) is

```text
(r/2)(alpha^2+r)n^2.
```

The fixed word, starting height, and polynomial counting factors contribute
only lower-order terms. Since `v_2(T)=6` and the odd denominator is a power of
`81`, their ratio gives (26).

Differentiation of the rational shape gives numerator

```text
2[-alpha^2+(2r-1)alpha+r].                            (28)
```

Its unique positive zero is (27), and the sign changes from positive to
negative there. **QED**

## Consequences and boundary

The optimized delayed-window exponents are above one through period nine and
below one at period ten. The exact source-independent period-nine theorem is
separated as `T-9422`; the exact period-ten ceiling for this construction class
is separated as `R-9410`.

This lemma is stronger than `L-9410` as an approximant family: its cancellation
window is no longer forced to begin at the denominator degree. It does not make
`L-9410`, `T-9414`, or the period-four regression suite obsolete; those files
remain the simplest exact instances and independent review anchors.

## Dependency audit

- `L-9408` supplies the periodic phase decomposition.
- The proof uses only the finite `q`-binomial theorem and elementary exact
  rational estimates.
- No Väänänen–Wallisser, Matala-aho, Subspace Theorem, or finite experiment is a
  dependency.

## Gap audit

- The result concerns fixed periodic words. It does not give constants uniform
  enough for a growing S-adic standard-word sequence.
- The bound is an upper bound for reduced height, not an exact reduced-height
  formula.
- Period ten remains below the elementary rationality threshold in this family.
- A phase-sensitive determinant, a low-dimensional `q`-difference theorem, or a
  different arithmetic height saving may still close period ten.

## Adversarial tests

`X-9413` reconstructs 630 Laurent-product identities, 180 exact zero-window
checks, 36 first-error checks, and 49,680 monomial-height inequalities over a
frozen finite range. It also verifies the exact period-nine and period-ten
threshold certificates.

## Suggested next attack

Use the delayed family as the new baseline. Any period-ten construction should
state whether it gains by cross-phase cancellation, by lower-dimensional
`q`-difference structure, or by a genuine reduced-height factor; merely moving
the same cancellation window is now completely optimized.