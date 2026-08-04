# Q-9410 — Standard-word determinant and Padé approximants

Claim ID: Q-9410  
Title: Can S-adic transfer matrices beat the direct `2`-adic truncation barrier?  
Status: IDEA / primary constructive approximation target  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-21  
Dependencies: L-9408, T-9411, R-9402  
Scope: balanced mechanical `17/18` directives and their continued-fraction standard words

## Starting point

L-9408 assigns to each finite increment word `W` the exact skew-affine transfer

```text
Theta(m;WV)
 =P_W(T^(9m))
  +T^e(W)*T^(9m|W|)*Theta(m+S(W);V),                (1)
```

with

```text
M_W(X)
 =[[T^e(W)*X^|W|, P_W(X)],
   [0,                    1]].                       (2)
```

Concatenation obeys

```text
M_(UV)(X)=M_U(X)*M_V(T^(9S(U))*X).                  (3)
```

For a mechanical directive, continued-fraction standard words satisfy a
recursion of the form

```text
W_(n+1)=W_n^(a_(n+1))*W_(n-1).                      (4)
```

T-9411 proves that ordinary partial sums have limiting rational approximation
exponent

```text
1/log_64(81)=0.946394630357...<1.                   (5)
```

R-9402 proves that the nearest standard `p`-adic lacunary theorem does not apply.
Therefore any successful irrationality or transcendence proof must extract a
new cancellation from (2)--(4).

## Exact objective

Construct integer or rational linear forms

```text
L_n
 =A_n*Theta_m+B_n                                  (6)
```

or multi-value determinants

```text
Delta_n
 =det [[A_n, B_n],
       [A'_n,B'_n]],                                (7)
```

built from adjacent standard-word transfers, such that after reduction

```text
v_2(L_n)
 >(2+epsilon)*log_2 height(A_n,B_n)                 (8)
```

for infinitely many `n`, or such that a suitable higher-dimensional
Subspace-Theorem inequality holds.

The required gain must be measured after all common powers of `3` and all
integer gcds are removed. Unreduced transfer coefficients are not acceptable
height estimates.

## Candidate construction 1 — adjacent-tail elimination

Let

```text
Y_n(m)=Theta(m; W_n V_n),
```

where `V_n` is the true suffix after the standard prefix. Equation (1) writes
`Y_n(m)` as a polynomial prefix plus one scaled shifted tail. Use the recursions
for `W_(n+1)`, `W_n`, and `W_(n-1)` to eliminate two shifted tails and obtain a
linear form in the original value.

Deliverables:

```text
- exact determinant identity;
- first nonzero `2`-adic term;
- reduced numerator/denominator height;
- comparison with the threshold in (8).
```

## Candidate construction 2 — periodic-standard-word Padé model

Replace the suffix by infinite repetition `W_n^infinity`. L-9408 gives a
`q`-difference recursion under height shift by `S(W_n)`. Seek a finite Padé
system for several shifted values

```text
Theta(m+q*S(W_n); W_n^infinity),
0<=q<=d,                                            (9)
```

then compare the true directive against the periodic model through its long
standard-word overlap.

The periodic model is **not** rational by default: height grows linearly and
support exponents quadratically. Any rational approximation must be proved by
the Padé system, not assumed from periodicity of the increment word.

## Candidate construction 3 — Hankel determinant

Use coefficients or transfer-polynomial moments to build a Hankel determinant
whose vanishing would force a bounded-order recurrence for the sparse support.
T-9410 rules out an eventual fixed recurrence for the full coefficient word.
The quantitative task is to turn a nonzero determinant into a rational linear
form with enough `2`-adic vanishing.

## Candidate construction 4 — adelic standard-word form

Evaluate the same transfer determinant in:

```text
- the `2`-adic absolute value, where long common support prefixes are small;
- the real absolute value, where `0<64/81<1` controls polynomial tails;
- the `3`-adic or denominator place, where reduced height is visible.
```

A successful product-formula argument must prove a net gain after including all
places. It must not identify the real and `2`-adic infinite sums.

## Frozen baseline tests

`X-9406` verifies:

- every short-word transfer and concatenation identity;
- the repeated-block closed formula;
- recursively composed Fibonacci standard words through length `89`;
- the direct approximation exponent at balanced-prefix checkpoints.

The experiment intentionally contains no claimed successful determinant.

## Success criterion

A candidate approximant is promising only if its measured exponent exceeds the
direct baseline (5) by a stable positive amount after exact reduction. A proof
route toward irrationality needs a threshold appropriate to the theorem being
used; for Ridout-type rational approximants this means eventually exceeding
`2`, not merely exceeding `1`.

## Falsification criteria

1. If the reduced height retains the full `81^H` denominator scale, no gain has
   been achieved.
2. If the apparent vanishing is only the shared standard prefix, the exponent
   is bounded by T-9411's ratio calculation.
3. If the determinant vanishes identically because two transfer rows encode the
   same shifted tail, it supplies no linear form.
4. If a periodic increment model is silently treated as a rational value, the
   construction is invalid.
5. Finite large exponents at small standard-word levels do not establish an
   infinite sequence above threshold.

## First computational program

For adjacent standard words `W_n,W_(n-1)`:

```text
1. construct transfer data recursively without word expansion;
2. generate low-degree elimination determinants;
3. evaluate exactly at T=64/81 and X=T^(9m_0);
4. reduce every rational coefficient;
5. record height, v_2, and approximation exponent;
6. freeze both successes and negative asymptotic trends.
```

Any discovered identity should be promoted only after a symbolic proof and an
independent exact verifier.