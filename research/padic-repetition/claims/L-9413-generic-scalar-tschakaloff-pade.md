# L-9413 — Generic scalar Tschakaloff Padé exponent

Claim ID: `L-9413`  
Title: Every rational stack phase has a scalar `q`-binomial Padé family with exponent `9/log_2(81)`  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: the finite `q`-binomial theorem; generalizes `L-9409`  
Scope: every `T`-power Tschakaloff phase appearing in a periodic stack vector  
Related counterexample candidates: period-ten special-vector program; no `K-####` candidate

## Setup

Put

```text
T=64/81,
A>=1,
B>=1,
q=T^A,
z=T^B,
```

and define

```text
F_(A,B)
 =f_q(z)
 =sum_(N>=0) q^[N(N-1)/2] z^N
 in Q_2.                                              (1)
```

The series also converges in the real embedding.

Write

```text
X=z/q=T^(B-A).
```

Then

```text
F_(A,B)
 =sum_(N>=0) q^[N(N+1)/2] X^N.                       (2)
```

The exponent `B-A` may be negative; the quadratic power of `q` still makes
(1) convergent, and all assertions below concern sufficiently large Padé order.

## Padé denominator

For `n>=1`, define

```text
b_(n,k)
 =(-1)^k q^(nk) [n choose k]_q,
```

and

```text
B_n(X)=sum_(k=0)^n b_(n,k) X^k.                      (3)
```

Let `A_n(X)` remove the coefficients of `B_n(X)F_(A,B)` below degree `n`, as in
`L-9409`.

## Statement 1 — exact cancellation

For every `n>=1`,

```text
B_n(X)F_(A,B)-A_n(X)
 =sum_(N>=2n)
   q^[N(N+1)/2]
   product_(j=0)^(n-1)(1-q^[n-N+j])
   X^N.                                               (4)
```

Thus the coefficients of degrees

```text
n,n+1,...,2n-1
```

vanish exactly.

The proof is the same finite `q`-binomial calculation as `L-9409`: after
division by the degree-`N` base term, the convolution becomes

```text
sum_(k=0)^n
 (-1)^k [n choose k]_q
 q^[k(k-1)/2]
 (q^[n-N])^k.
```

## Statement 2 — exact first error

For every `n>=1`,

```text
v_2(B_n(X))=0.                                       (5)
```

At `N=2n`, the exact `T`-exponent of the first error is

```text
E_err(n)
 =A(3n^2+n)/2+2n(B-A)
 =(3A/2)n^2+(2B-3A/2)n.                              (6)
```

Consequently

```text
v_2(F_(A,B)-A_n(X)/B_n(X))
 =6 E_err(n).                                        (7)
```

### Proof

Every nonconstant term of `B_n(X)` has minimum `T`-exponent

```text
k[A(n-1)+B]>0,
```

so `B_n(X)=1 mod 2`.

At `N=2n`, extracting the negative powers from the product in (4) gives the
net `q`-exponent `(3n^2+n)/2`; the factor `X^(2n)` supplies the rest of (6).

For `N>=2n`, increasing `N` by one increases the total `T`-exponent by

```text
A(N-n)+B>0.
```

Hence the first nonzero term is uniquely smallest in `2`-adic valuation and
cannot cancel.

## Statement 3 — rational height

There is a constant `C_(A,B)>0`, independent of `n`, such that

```text
height(A_n(X)/B_n(X))
 <=C_(A,B)(n+1)^2
   81^[A n^2+|B-A|n].                                (8)
```

Here rational height means `max(|p|,|q|)` after reduction.

### Proof sketch

The Gaussian binomial has `q`-degree at most `k(n-k)`. Every monomial in the
`k`-th denominator term has total `T`-exponent at most

```text
A(2nk-k^2)+(B-A)k
 <=A n^2+|B-A|n.
```

The lower convolution coefficients defining `A_n` satisfy the same quadratic
bound, exactly as in `L-9409`. Since `0<q<1` in the real embedding, all Gaussian
binomials are bounded by one infinite Euler-product constant depending only on
`q`. Clearing the displayed odd power of `81` and counting terms gives (8).
Reduction can only lower height.

## Asymptotic exponent

Equations (7)--(8) give

```text
liminf_(n->infinity)
 v_2(F_(A,B)-A_n/B_n)
 /log_2 height(A_n/B_n)
 >=9/log_2(81)
 =1.419591945535779... .                              (9)
```

This is independent of `A` and `B`.

## Application to periodic stack phases

For a period-`r` word,

```text
R=T^(9Sr),
y_j=Z lambda^j=T^[e+9mr+9Sj].
```

Thus every individual phase

```text
f_R(y_j)
```

has the form (1) with

```text
A=9Sr,
B=e+9mr+9Sj>=1.
```

Every phase therefore admits the same scalar exponent (9).

## Dependency audit

- The proof is an exact scalar specialization of the `q`-binomial argument in
  `L-9409`.
- No external irrationality theorem is used.
- The height bound is pre-asymptotic only through a linear term; its quadratic
  coefficient is exact enough for (9).

## Gap audit

- A scalar exponent above one proves each individual phase irrational, but the
  native period-ten value is a rational linear combination of ten phases.
- Irrational summands may have a rational sum.
- One needs a quantitative measure for the other phases or a coupled
  special-vector construction.
- The lemma does not prove transcendence.

## Adversarial tests

`X-9411` freezes the constant in (9) and checks its place conversion. The exact
coefficient identities are already exercised in `X-9407`.

## Suggested next attack

Combine (9) with a quantitative nine-phase linear-independence measure through
the elimination lemma `L-9414`.
