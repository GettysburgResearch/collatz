# L-9408 — Exact S-adic transfer polynomials

Claim ID: L-9408  
Title: Every finite height-increment word acts by an explicit skew-affine polynomial transfer  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9407  
Scope: every finite positive height-increment word  
Related counterexample candidates: issue #4 balanced stack and Q-9409; no `K-####` candidate

## Setup

Let `T` be a formal variable. For a starting stack height `m` and an infinite
increment word

```text
d=d_1 d_2 d_3 ...,
d_i>=1,
```

put

```text
m_j=m+sum_(1<=i<=j)d_i,
E_0=0,
E_j=sum_(1<=i<=j)(9*m_i+1).                         (1)
```

Define the formal tail value

```text
Theta(m;d)=sum_(j>=0) T^E_j.                        (2)
```

At `T=64/81`, this is the context partial-theta tail of L-9407, up to its fixed
initial affine factor.

For a finite word

```text
W=d_1...d_r,
```

define

```text
|W|=r,
S(W)=sum_(i=1)^r d_i,
C_j(W)=sum_(i=1)^j d_i,
A(W)=sum_(j=1)^r C_j(W).                            (3)
```

Put

```text
e(W)=r+9*A(W).                                      (4)
```

For `0<=j<=r`, let `A_j(W)=sum_(i=1)^j C_i(W)`, with `A_0=0`, and define

```text
P_W(X)
 =sum_(j=0)^(r-1) T^(j+9*A_j(W))*X^j.               (5)
```

## Statement 1 — finite-word transfer identity

For every infinite suffix `V`,

```text
Theta(m;WV)
 =P_W(T^(9m))
  +T^e(W)*T^(9m*r)*Theta(m+S(W);V).                 (6)
```

Equivalently, with `X=T^(9m)`, the word `W` acts through the triangular matrix

```text
M_W(X)
 =[[T^e(W)*X^r, P_W(X)],
   [0,             1   ]].                          (7)
```

### Proof

After `j` letters, the exponent in (1) is

```text
E_j
 =sum_(i=1)^j(9*(m+C_i(W))+1)
 =9jm+j+9A_j(W).                                    (8)
```

The terms with `0<=j<r` give (5). The full-word exponent is

```text
E_r=9mr+e(W),                                       (9)
```

and the remaining suffix begins at height `m+S(W)`. Factoring `T^E_r` proves
(6) and (7). **QED**

## Statement 2 — exact concatenation calculus

For finite words `U,V`, with `r=|U|`,

```text
S(UV)=S(U)+S(V),                                    (10)
```

```text
e(UV)=e(U)+e(V)+9*|V|*S(U),                        (11)
```

and

```text
P_(UV)(X)
 =P_U(X)
  +T^e(U)*X^r*P_V(T^(9S(U))*X).                     (12)
```

In matrix form,

```text
M_(UV)(X)
 =M_U(X)*M_V(T^(9S(U))*X).                          (13)
```

### Proof

The height entering `V` is shifted by `S(U)`. Therefore every one of the
`|V|` exponent increments gains `9S(U)`, which gives (11). Splitting the
prefix terms before and after the boundary proves (12). Direct multiplication
of the triangular matrices gives (13). **QED**

## Statement 3 — one-letter generators

For a one-letter word `(d)`,

```text
S(d)=d,
e(d)=1+9d,
P_d(X)=1,                                           (14)
```

and

```text
M_d(X)
 =[[T^(1+9d)*X, 1],
   [0,            1]].                              (15)
```

Thus the balanced `17/18` stack is an S-adic product of exactly two explicit
skew-affine generators.

## Statement 4 — repeated block formula

Let `W` have length `r`, sum `S`, and transfer data `(e,P)`. For `a>=1`,

```text
e(W^a)
 =a*e+9*r*S*a*(a-1)/2.                              (16)
```

Moreover,

```text
P_(W^a)(X)
 =sum_(q=0)^(a-1)
   T^(q*e+9*r*S*q*(q-1)/2)
   X^(q*r)
   P(T^(9qS)*X).                                    (17)
```

### Proof

Apply (11) and (12) inductively. Before the `q`-th copy, the starting height is
shifted by `qS`, and the preceding `q` copies contribute the exponent displayed
in (17). **QED**

## Standard-word interface

Let a mechanical directive have continued-fraction standard words satisfying

```text
W_(n+1)=W_n^(a_(n+1))*W_(n-1).                      (18)
```

Equations (10)--(17) compute the exact transfer matrix of every standard word
without expanding its exponentially long letter string. The data needed are

```text
(|W_n|, S(W_n), e(W_n), P_(W_n)).                   (19)
```

This is the intended input to a Padé/Subspace-Theorem attack on Q-9409.

## Dependency audit

Only the sparse tail definition from L-9407 is used. The proof is finite
algebra on exponent sums.

## Gap audit

- The transfer matrices are upper triangular; their existence alone gives no
  transcendence or irrationality.
- `P_W` has degree `|W|-1`, so a naive expanded representation is still large.
  Standard-word recursion is needed for compression.
- The variable shift `X -> T^(9S(U))X` is load-bearing. Omitting it incorrectly
  turns the skew product into an ordinary monoid representation.
- Periodic increment words lead to a `q`-difference equation, not automatically
  a rational approximant.

## Adversarial tests

`X-9406` checks (6), (11), (12), and (17) exhaustively on short `{17,18}` words
and recursively on standard words.

## Remaining uncertainty

It is unknown whether the standard-word matrices yield rational or algebraic
approximants strong enough to cross T-9411's direct-truncation barrier.

## Suggested next attack

Construct low-rank determinants from two adjacent standard-word transfers,
evaluate at `T=64/81` and `X=T^(9m)`, and measure both reduced height and
`2`-adic vanishing.