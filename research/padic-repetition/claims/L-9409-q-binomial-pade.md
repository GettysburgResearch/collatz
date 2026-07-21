# L-9409 — `q`-binomial Padé approximants for constant increments

Claim ID: L-9409  
Title: Exact diagonal Padé family for a constant-increment stack tail  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9408  
Scope: every constant positive stack-height increment  
Related counterexample candidates: issue #4 periodic stack models; no `K-####` candidate

## Setup

Put

```text
T=64/81,
d>=1,
m>=0,
rho=T^(9d),
X=T^(9m+1).                                         (1)
```

The constant-increment tail is

```text
F_(d,m)
 =sum_(N>=0) rho^(N(N+1)/2)*X^N
 in Q_2.                                             (2)
```

It is the L-9408 value `Theta(m; ddd...)`.

For `0<=k<=n`, let

```text
[n choose k]_rho
```

be the Gaussian binomial polynomial evaluated at `rho`.

Define

```text
b_(n,k)
 =(-1)^k*rho^(n*k)*[n choose k]_rho,                (3)
```

```text
B_n(X)=sum_(k=0)^n b_(n,k)*X^k.                    (4)
```

Write

```text
u_N=rho^(N(N+1)/2).                                 (5)
```

For `0<=N<n`, define

```text
a_(n,N)=sum_(k=0)^N b_(n,k)*u_(N-k),                (6)
```

and

```text
A_n(X)=sum_(N=0)^(n-1) a_(n,N)*X^N.                (7)
```

## Statement 1 — exact Padé vanishing

For every `n>=1`,

```text
B_n(X)*F_(d,m)-A_n(X)
 =sum_(N>=2n)
   u_N*prod_(j=0)^(n-1)(1-rho^(n-N+j))*X^N.         (8)
```

In particular, the coefficients of degrees

```text
n,n+1,...,2n-1
```

vanish exactly.

### Proof

For `N>=n`, the coefficient of `X^N` in `B_n F` is

```text
sum_(k=0)^n b_(n,k)*u_(N-k).
```

Divide by `u_N`. Since

```text
u_(N-k)/u_N
 =rho^(-N*k+k(k-1)/2),                              (9)
```

the normalized coefficient is

```text
sum_(k=0)^n
 (-1)^k*[n choose k]_rho
 *rho^(k(k-1)/2)
 *(rho^(n-N))^k.                                    (10)
```

The finite `q`-binomial theorem turns (10) into

```text
prod_(j=0)^(n-1)(1-rho^(n-N+j)).                    (11)
```

For `n<=N<2n`, one factor has exponent zero, so the product vanishes. For
`N>=2n`, it is the displayed coefficient in (8). The terms below degree `n`
are exactly removed by the definition of `A_n`. **QED**

## Statement 2 — exact first error

At the evaluation point `X` in (1),

```text
v_2(B_n(X))=0,                                      (12)
```

and

```text
v_2(B_n(X)*F_(d,m)-A_n(X))
 =27*d*(3n^2+n)+12*n*(9m+1).                        (13)
```

Therefore the same value is the valuation of

```text
F_(d,m)-A_n(X)/B_n(X).                              (14)
```

### Proof

Every term of `B_n(X)` except the constant term contains a positive power of
`rho` and of `X`. The Gaussian binomial has constant term one and is a
`2`-adic unit. Thus `B_n(X)=1 mod 2`, proving (12).

At `N=2n`, the coefficient in (8) is

```text
u_(2n)*prod_(r=1)^n(1-rho^(-r)).                    (15)
```

Each factor in (15) has `rho`-valuation `-r`, because `1-rho^r` is a `2`-adic
unit. Hence the net `rho`-exponent is

```text
n*(2n+1)-n*(n+1)/2
 =(3n^2+n)/2.                                       (16)
```

Now

```text
v_2(rho)=54d,
v_2(X)=6(9m+1).                                    (17)
```

Multiplying (16) by `v_2(rho)` and adding the contribution of `X^(2n)` gives
(13).

For `N>=2n`, the `rho`-exponent of the coefficient in (8) is

```text
N(N+1)/2+n(n-N)+n(n-1)/2.                           (18)
```

Its increase from `N` to `N+1` is `N+1-n>0`; the power of `X` also increases.
Thus the first nonzero term is uniquely smallest in the `2`-adic valuation and
cannot cancel. Equation (12) proves (14). **QED**

## Statement 3 — rational-height bound

Put

```text
E_n=9*d*n^2+(9m+1)*n.                               (19)
```

There is a constant `C_(d,m)>0`, independent of `n`, such that

```text
height(A_n(X)/B_n(X))
 <=C_(d,m)*(n+1)^2*81^E_n.                          (20)
```

### Proof

The Gaussian binomial is an integer polynomial in `rho` of degree `k(n-k)`.
Every monomial occurring in the `k`-th term of `B_n(X)` has total `T`-exponent
at most

```text
9d*(2nk-k^2)+(9m+1)k
 <=9dn^2+(9m+1)n=E_n.                               (21)
```

For a coefficient of `A_n`, write `N-k=t`. Since `N<n`, we have `t<=n-k-1`.
The largest possible `rho`-exponent is

```text
2nk-k^2+t(t+1)/2<=n^2.                              (22)
```

After multiplying by `X^N`, its total `T`-exponent is also at most `E_n`.
Therefore both evaluated polynomials can be written over the common odd
denominator `81^E_n`.

In the real embedding `0<rho<1`. The product expression for the Gaussian
binomial gives a uniform bound

```text
[n choose k]_rho
 <=prod_(i>=1)(1-rho^i)^(-1)=C_rho.                 (23)
```

Consequently the real absolute values of the cleared numerators are bounded by
`C_(d,m)*(n+1)^2*81^E_n`. Taking the ratio and then reducing can only decrease
height. This proves (20). **QED**

## Asymptotic gain

Combining (13), (19), and (20) gives

```text
liminf
 v_2(F_(d,m)-A_n/B_n)
 /log_2 height(A_n/B_n)
 >=9/log_2(81)
 =1.419591945535... .                               (24)
```

This exceeds the direct-truncation value `0.946394...` from T-9411 and crosses
the threshold `1` needed to contradict a fixed rational target with odd
denominator.

## Dependency audit

- L-9408 identifies the constant-increment tail and its one-letter transfer.
- The proof otherwise uses only the finite `q`-binomial theorem and exact
  integer/rational estimates written above.

## Gap audit

- The lemma constructs rational approximants and proves their exact errors; the
  irrationality conclusion is separated into T-9412.
- The limiting exponent remains below `2`, so this family does not by itself
  prove transcendence or exclude algebraic irrational values through Ridout.
- Periodic increment models are not assumed rational; the Padé family is what
  creates rational approximants.
- Height is measured after reduction; (20) is an upper bound sufficient for the
  irrationality theorem.

## Adversarial tests

`X-9407` verifies every coefficient cancellation, first-error formula,
`2`-adic-unit denominator, and reduced evaluated height for `d in {17,18}` and
small Padé orders.

## Remaining uncertainty

The balanced nonperiodic directive needs a matrix or standard-word analogue of
this scalar `q`-binomial family.

## Suggested next attack

Use L-9408 to replace the scalar Gaussian binomial by a block/standard-word
orthogonality relation, preserving a limiting exponent greater than one.