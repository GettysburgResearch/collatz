# L-9603 — Two-support pulses reduce to bounded discrete logarithms

**Claim ID:** `L-9603`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-22  
**Dependencies:** `L-9602`  
**Scope:** perturbations of a negative accelerated cycle supported at exactly two positions

## 1. Two pulse supports

Retain the notation of `L-9602`. Cyclically rotate the word so that the first pulse support is at position zero. Let the second support be at

\[
1\le q<K,
\]

and let the two positive pulse sizes be

\[
b,c\ge1,
\qquad B=b+c.
\]

Thus

\[
b_0=b,
\qquad b_q=c,
\qquad b_j=0\quad(j\notin\{0,q\}).
\]

Put

\[
D_{B}=2^{A+B}-3^K.
\tag{1}
\]

The full pulse correction from `L-9602/(5)` is

\[
H=
W_0(2^b-1)+2^bW_q(2^c-1),
\tag{2}
\]

where

\[
W_p=(-z_{p+1})3^{K-1-p}2^{A_{p+1}}.
\]

## 2. Reduced exact congruence

Factor the unit

\[
3^{K-1-q}2^{A_1}
\]

from `(2)`. It is coprime to `D_B`. Therefore

\[
D_B\mid H
\]

if and only if

\[
\boxed{
D_B\mid
R_{q,b,c},}
\tag{3}
\]

where

\[
\boxed{
R_{q,b,c}
=
(-z_1)3^q(2^b-1)
+
(-z_{q+1})2^{b+A_{q+1}-A_1}(2^c-1).}
\tag{4}
\]

This removes all powers depending on the unused terminal portion of the repeated negative cycle.

## 3. One bounded discrete-log equation

For fixed total pulse `B`, put

\[
U_q=(-z_1)3^q,
\qquad
V_q=(-z_{q+1})2^{A_{q+1}-A_1}.
\tag{5}
\]

Since `c=B-b`, equation `(4)` becomes

\[
R_{q,b,B-b}
=
V_q2^B-U_q+2^b(U_q-V_q).
\tag{6}
\]

Hence the exact integrality condition is the bounded discrete-log congruence

\[
\boxed{
2^b(U_q-V_q)
\equiv
U_q-V_q2^B
\pmod {D_B},
\qquad1\le b<B.}
\tag{7}

Let

\[
g_q=\gcd(U_q-V_q,D_B).
\]

A first exact sieve is

\[
\boxed{
g_q\mid U_q-V_q2^B.}
\tag{8}
\]

When `(8)` holds, division by `g_q` reduces `(7)` to a discrete logarithm of base two modulo the odd integer `D_B/g_q`, with the exponent restricted to the finite interval `1,...,B-1`.

## 4. Completeness under rotation

Every pulse vector with exactly two nonzero supports has a cyclic rotation putting one support at zero. The rotation changes only the negative cycle state and the displayed primitive rotation of the base word. Scanning all negative states on the primitive cycle, every second position `q`, every total pulse `B`, and every split `b+(B-b)` is therefore complete for the stated family.

## 5. Negative three-cycle specialization

For the repeated negative three-cycle, scan the two rotations

\[
(1,2)^r\quad(z=-5),
\qquad
(2,1)^r\quad(z=-7).
\]

Let

\[
B_0(r)=\min\{B:2^{3r+B}>3^{2r}\}.
\]

`X-9603` checks exactly

```text
1 <= r <= 400
B_0(r) <= B <= B_0(r)+3
1 <= q < 2r
1 <= b < B, c=B-b
both primitive rotations
```

The frozen packet contains

```text
59,385,744
```

exact pulse splits. The gcd sieve `(8)` leaves `1,160,328` position/total-pulse rows requiring the bounded exponent test.

The only hit is

```text
r=2, base rotation (1,2)^2,
q=2, b=c=1,
word=(2,2,2,2), start=1.
```

This is the trivial cycle traversed four times; it is a proper power of `(2)` and contains no new orbit. There is no nontrivial positive cycle in the frozen family.

## 6. Strategic consequence

The two-support construction can be searched to much greater repeated depth than arbitrary distributed pulses because the entire combinatorics collapses to `(7)`. The absence of hits through `r=400` is evidence against a sparse-support perturbation of the negative three-cycle, but the theorem's larger value is the reusable reduction:

```text
two support positions
  -> remove terminal powers
  -> gcd sieve
  -> bounded discrete log
  -> exact positive-cycle certificate on a hit.
```

## 7. Gap audit

- Three or more pulse supports are not covered by `(7)`.
- `X-9603` freezes only the negative three-cycle and four total-pulse levels.
- The finite result is not an all-`r` theorem.
- The result does not exclude a multi-block or high-complexity valuation grammar.
- No nontrivial cycle, divergent seed, or Collatz counterexample is claimed.
