# L-6815 — One-third long-return gate for every first-crossing non-descent

**Claim ID:** `L-6815`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6801`, `L-6812`; elementary affine orbit algebra  
**Scope:** positive ordinary coefficient-first-crossing segments whose endpoint does not descend

## 1. Setup

Let

\[
x_t=T^t(n)
\qquad(0\le t\le j)
\]

be a positive ordinary shortcut-Collatz segment. Put

\[
q_t=\sum_{i=0}^{t-1}v_i,
\qquad
D_t=q_t-\alpha t,
\qquad
\alpha={\log2\over\log3}.
\]

Assume first crossing at time `j`:

\[
D_t\ge0
\qquad(0\le t<j),
\qquad
D_j<0,
\tag{1}
\]

and assume no descent at the crossing:

\[
x_j\ge n.
\tag{2}
\]

Let

\[
q=q_j,
\qquad
B=\max_{0\le t<j}D_t,
\qquad
\lambda=j\log2-q\log3>0.
\tag{3}
\]

Suppose one length-`L` parity factor occurs at two proper times

\[
0\le a<b\le j-L-1
\]

and the two physical source states are distinct.

## 2. One-third affine height bound at every proper time

The exact affine formula is

\[
x_t
=3^{D_t}n
+{1\over2}
\sum_{m=1}^{t}
 v_{m-1}3^{D_t-D_m}.
\tag{4}
\]

For every nonzero summand, the step ending at time `m` is odd. Therefore

\[
D_m=D_{m-1}+1-\alpha
\ge1-\alpha.
\tag{5}
\]

Since `D_t<=B`,

\[
{1\over2}3^{D_t-D_m}
\le
{1\over2}3^{B-(1-\alpha)}
={3^B\over3}.
\tag{6}
\]

There are `q_t` nonzero terms. Hence every proper state satisfies

\[
\boxed{
x_t
\le
3^B\left(n+{q_t\over3}ight)
\le
3^B\left(n+{q\over3}ight).}
\tag{7}
\]

This improves the earlier coarse `3^B(n+j/2)` bound.

## 3. Exact ordinary start ceiling

The harmonic/product argument gives

\[
\boxed{
n<{q\over3\lambda}.}
\tag{8}
\]

For completeness, no descent and the exact product identity imply

\[
2^{j/q}
\le3+{1\over h},
\]

where `h>=n` is the harmonic mean of the odd sources. Since

\[
2^{j/q}=3e^{\lambda/q}
\]

and `e^x-1>x`, equation `(8)` follows.

Combining `(7)--(8)`,

\[
\boxed{
x_t
<
3^B\left({q\over3\lambda}+{q\over3}ight)
\qquad(t<j).}
\tag{9}
\]

## 4. Sharpened long-return inequality

The repeated length-`L` factor gives, by `L-6801`,

\[
2^L\mid x_b-x_a.
\]

The states are distinct, so

\[
|x_b-x_a|\ge2^L.
\]

Both are positive and bounded by `(9)`. Therefore

\[
\boxed{
2^L+1
<
3^B\left({q\over3\lambda}+{q\over3}ight).}
\tag{10}
\]

This is the source-free exact return gate.

Equivalently, any certified lower bound `lambda>=lambda_0` excludes the word
whenever

\[
\boxed{
2^L+1
\ge
3^B\left({q\over3\lambda_0}+{q\over3}ight).}
\tag{11}
\]

## 5. Source-qualified uniform form

Under the quoted Rhin specialization

\[
\lambda\ge j^{-13.3},
\]

and using `q<j`, equation `(10)` gives

\[
\boxed{
2^L+1
<
{2\over3}
3^B j^{14.3}}
\tag{12}
\]

for every `j>=1`.

Thus every repeated factor in an acyclic first-crossing failure satisfies

\[
\boxed{
L
<
B\log_2 3
+14.3\log_2j
+\log_2(2/3).}
\tag{13}
\]

The negative constant is legitimate: the right side is used only when a
repeated positive-length factor exists, and `(12)` already guarantees it is
positive in that situation.

## 6. Consumers

Equation `(10)` sharpens all return-based interfaces:

```text
support -> factor return -> ordinary contradiction;
swap budget -> factor return -> ordinary contradiction;
corridor entropy -> factor return -> ordinary contradiction;
mechanical-prefix shadowing -> canonical source floor.
```

In particular, `T-6810` uses `(12)` to improve its explicit square-root
support floor while retaining the same asymptotic constant.

## 7. Gap audit

- The theorem assumes no descent at the first crossing.
- A repeated physical state is the positive-cycle alternative, not part of
  the distinct-state inequality.
- The exact gate does not force a repeated factor; a separate complexity or
  support argument supplies it.
- The source-qualified exponent still requires primary-source audit.
- No proof of CST or Collatz is claimed.
