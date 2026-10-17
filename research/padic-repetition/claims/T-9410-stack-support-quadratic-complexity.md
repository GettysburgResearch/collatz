# T-9410 — Quadratic complexity of bounded-increment stack support

Claim ID: T-9410  
Title: The sparse code of every bounded-increment increasing stack has exactly quadratic factor complexity  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9407 and T-9406 for the lower bound  
Scope: increasing stack heights with uniformly bounded positive increments  
Related counterexample candidates: issue #4 balanced stack frontier; no `K-####` candidate

## Setup

Let

```text
m_0<m_1<m_2<...
```

satisfy

```text
1<=m_(t+1)-m_t<=C_m.                                (1)
```

Put

```text
ell_t=9*m_t+1,
h_0=0,
h_t=sum_(0<=i<t) ell_i,
```

and let `eps` be the support word from L-9407:

```text
eps_n=1 iff n=h_t for some t.                       (2)
```

The zero gap following the `t`-th one is

```text
g_t=ell_t-1=9*m_t.                                  (3)
```

Hence

```text
9<=g_(t+1)-g_t<=9*C_m.                              (4)
```

## Statement 1 — explicit quadratic bounds

For every sufficiently large `n`,

```text
(floor(n/(90*C_m))-1)*(floor(2*n/5)-1)
 <= p_eps(n)
 <= n^2+n+1.                                        (5)
```

Consequently,

```text
p_eps(n)=Theta(n^2).                                (6)
```

For the active `17/18` interface, `C_m=18`, so the lower bound is

```text
(floor(n/1620)-1)*(floor(2*n/5)-1),                 (7)
```

while the universal upper bound remains `n^2+n+1`.

## Proof of the lower bound

Equation (4) puts the word exactly in the scope of T-9406 with gap-increment
constant

```text
C=9*C_m.
```

Substituting this value into T-9406 gives the left side of (5).

## Proof of the upper bound

Fix `n`. A length-`n` factor containing at most one `1` is one of

```text
0^n,
0^a 1 0^(n-a-1),  0<=a<n,
```

so there are at most `n+1` such factors.

A factor containing at least two `1`s contains some pair of consecutive ones
whose intervening zero gap satisfies

```text
g_t<=n-2.                                           (8)
```

Because the `g_t` are strictly increasing nonnegative integers, there are at
most `n-1` indices satisfying (8). For each such consecutive pair, a
length-`n` factor containing it has at most `n` possible start offsets relative
to the first one. Thus the number of factors containing at least two ones is at
most

```text
n*(n-1).
```

Adding the at-most-one-one factors gives

```text
p_eps(n)<=n*(n-1)+(n+1)<=n^2+n+1.
```

Together with the lower bound this proves (5) and (6). **QED**

## Statement 2 — quadratic support positions

If the increments also satisfy

```text
a<=m_(t+1)-m_t<=b,                                  (9)
```

then for every `j>=1`,

```text
j*(9*m_0+1)+9*a*j*(j-1)/2
 <=h_j
 <=j*(9*m_0+1)+9*b*j*(j-1)/2.                      (10)
```

Thus the number of ones among the first `N` digits is `Theta(sqrt(N))`.
For `17/18` increments the quadratic coefficients in (10) are respectively
`153/2` and `162/2`.

### Proof

From (9),

```text
m_0+a*i<=m_i<=m_0+b*i.
```

Sum `ell_i=9*m_i+1` for `0<=i<j`. This gives (10). Inverting the two quadratic
bounds gives the support-count statement. **QED**

## Statement 3 — exact formal-series class

Define

```text
F_m(T)=sum_(t>=0) T^h_t in Z[[T]].                  (11)
```

Its coefficient word is `eps`, has zero density, and has factor complexity
`Theta(n^2)`. It is not a rational function in `Q(T)`.

### Proof of nonrationality

A rational power series over `Q` has coefficients satisfying a fixed linear
recurrence from some point onward. Since the coefficients here lie in the
finite set `{0,1}`, the finite recurrence-state tuples would eventually repeat,
forcing the coefficient word to be eventually periodic. But the successive
zero gaps `g_t` are strictly increasing, so the word is not eventually
periodic. Hence `F_m(T)` is not rational. **QED**

## Interpretation

L-9407 turns the ordinary stack problem into the special value

```text
F_m(64/81) in Q_2.                                  (12)
```

T-9410 locates its coefficient word exactly between two familiar regimes:

- it is not low-complexity Sturmian output (`p(n)=n+1`);
- it is not Hadamard-lacunary in exponent ratio, because `h_(t+1)/h_t -> 1`;
- it has sparse support `Theta(sqrt(N))` but quadratic local factor complexity.

Therefore linear-complexity `p`-adic digit criteria and fixed-ratio lacunary
value theorems cannot be imported without an additional reduction. This is a
hypothesis boundary, not evidence that the value is algebraic.

## Dependency audit

- L-9407 supplies the exact support word and value interface.
- T-9406 supplies only the already-proved lower bound.
- The upper bound, position bounds, and nonrationality argument are elementary.

## Gap audit

- `Theta(n^2)` complexity is compatible with both algebraic and transcendental
  `2`-adic values; no value theorem is asserted.
- Nonrationality of the formal function does not imply that its value at one
  algebraic `2`-adic argument is nonrational.
- The word studied is the emitted binary code, not the `17/18` directive itself.
- The upper bound intentionally overcounts and is not claimed sharp in its
  constant.

## Adversarial tests

`X-9405` computes exact factor sets for a deterministic `17/18` directive at
several finite lengths, verifies (5), and checks the exponent bounds (10)
through 200 stages.

## Remaining uncertainty

The missing theorem is a `2`-adic value result for a nonrational series whose
support exponents grow quadratically and whose gap-increment word is Sturmian
or Ostrowski-computable.

## Suggested next attack

Develop a `2`-adic Subspace-Theorem or S-adic matrix criterion for (12), keeping
explicit that the coefficient complexity is quadratic rather than linear.