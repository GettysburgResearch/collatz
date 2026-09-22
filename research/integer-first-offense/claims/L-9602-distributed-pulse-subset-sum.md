# L-9602 — Distributed-pulse subset-sum formula

**Claim ID:** `L-9602`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-22  
**Dependencies:** elementary accelerated Collatz affine algebra; `L-9601` as the one-pulse specialization  
**Scope:** arbitrary extra dyadic divisions inserted into a repeated negative accelerated cycle

## 1. Base negative cycle

Let

\[
w=(a_0,\ldots,a_{K-1}),
\qquad a_j\ge1,
\]

be an accelerated valuation word with an ordinary negative closed orbit

\[
z_0,z_1,\ldots,z_K=z_0<0,
\]

so that

\[
3z_j+1=2^{a_j}z_{j+1}.
\tag{1}
\]

Put

\[
A_0=0,
\qquad
A_j=\sum_{i<j}a_i,
\qquad
A=A_K.
\tag{2}
\]

Now choose a pulse vector

\[
b=(b_0,\ldots,b_{K-1}),
\qquad b_j\in\mathbf Z_{\ge0},
\]

and replace the valuation word by

\[
a'_j=a_j+b_j.
\tag{3}
\]

Write

\[
B_j=\sum_{i<j}b_i,
\qquad
B=B_K,
\qquad
D_b=2^{A+B}-3^K.
\tag{4}
\]

The positive-cycle regime is `D_b>0`.

## 2. Exact pulse correction

Define

\[
\boxed{
H_w(b)=
\sum_{j:b_j>0}
(-z_{j+1})(2^{b_j}-1)
3^{K-1-j}2^{A_{j+1}+B_j}.}
\tag{5}
\]

Then the rational fixed point of the perturbed affine word is

\[
\boxed{
n_b=z_0+{H_w(b)\over D_b}.}
\tag{6}
\]

Consequently, when `D_b>0`, the perturbed word is a positive accelerated cycle certificate if and only if

\[
\boxed{D_b\mid H_w(b).}
\tag{7}
\]

If `(7)` holds, the standard numerator of the perturbed word is

\[
C_b=z_0D_b+H_w(b),
\tag{8}
\]

so `D_b|C_b`. Since every standard accelerated numerator is positive, `n_b=C_b/D_b` is positive. The usual prefix-congruence argument then makes every intermediate state an odd integer with exactly the prescribed valuation. Thus a modular hit is already a complete finite certificate; an independent replay remains a useful implementation guard.

## 3. Proof by the orbit-difference cocycle

Let `y_j` follow the perturbed affine branches and put

\[
d_j=y_j-z_j.
\]

Using `(1)` gives

\[
\begin{aligned}
d_{j+1}
&={3y_j+1\over2^{a_j+b_j}}
  -{3z_j+1\over2^{a_j}}\\
&={3d_j\over2^{a_j+b_j}}
  -z_{j+1}(1-2^{-b_j}).
\end{aligned}
\tag{9}
\]

Iterating through the `K` steps yields

\[
d_K
={3^K\over2^{A+B}}d_0
-
\sum_{j:b_j>0}
 z_{j+1}(1-2^{-b_j})
 {3^{K-1-j}\over2^{(A-A_{j+1})+(B-B_{j+1})}}.
\tag{10}
\]

For a fixed point, `d_K=d_0`. Multiply `(10)` by `2^(A+B)` and use

\[
(1-2^{-b_j})2^{A_{j+1}+B_{j+1}}
=(2^{b_j}-1)2^{A_{j+1}+B_j}.
\]

This gives

\[
D_b d_0=H_w(b),
\]

which is `(6)`.

## 4. Distinct unit pulses

Suppose each pulse is one unit and the pulse positions are

\[
0\le p_1<\cdots<p_e<K.
\]

Then `B_(p_t)=t-1`. Define the fixed positional weight

\[
\boxed{
W_p=(-z_{p+1})3^{K-1-p}2^{A_{p+1}}.}
\tag{11}
\]

Equation `(5)` becomes the rank-weighted subset sum

\[
\boxed{
H(P)=\sum_{t=1}^e2^{t-1}W_{p_t}.}
\tag{12}
\]

This is not an ordinary unordered subset sum: the factor `2^(t-1)` records how many earlier pulse bits have already been inserted. It nevertheless has an exact concatenation law.

Cut the positions into a left interval and a right interval. If `P_L` has `ell` pulses and the local rank in each half starts at zero, then

\[
\boxed{
H(P)=H_L(P_L)+2^\ell H_R(P_R).}
\tag{13}
\]

Thus, for fixed `ell`, divisibility by `D_b` is a genuine two-list meet-in-the-middle join.

## 5. Cyclic half-balance lemma

Let `K=2r` and let `P` be any `e`-element subset of the cyclic positions `Z/KZ`. For a cyclic cut `s`, let

\[
c_s=\#\bigl(P\cap\{s,s+1,\ldots,s+r-1\}\bigr).
\]

Then

\[
c_{s+r}=e-c_s,
\tag{14}
\]

and moving the cut by one position changes `c_s` by at most one. Hence some cut satisfies

\[
\boxed{
c_s\in\{\lfloor e/2\rfloor,\lceil e/2\rceil\}.}
\tag{15}
\]

Indeed, if `c_s` lies on one side of `e/2`, `(14)` lies on the other; the integer sequence cannot cross without taking one of the two values in `(15)`.

Because cyclic rotation preserves the cycle divisibility condition, every pulse set has a representative with a balanced half split.

## 6. Negative three-cycle specialization

For

\[
w=(1,2)^r,
\qquad K=2r,
\qquad A=3r,
\]

the only primitive rotations begin at `z=-5` and `z=-7`. Therefore scanning those two rotations and only the two balanced values of `ell` in `(15)` covers **every** distinct unit-pulse set up to cyclic rotation.

`X-9602` freezes the first complete distributed-pulse packet:

```text
1 <= r <= 45
pulse count e = min{e : 2^(3r+e) > 3^(2r)}
all distinct e-position pulse sets
both primitive rotations
```

The balance reduction covers

```text
508,127,577,642
```

raw labeled pulse words. The only hits are the two rotations of the trivial `n=1` word at `r=1`; there is no nontrivial positive cycle in the frozen packet.

## 7. Strategic consequence

The perturbation program has moved from exponential word enumeration to an exact modular join:

```text
negative cycle
  -> pulse correction H(P)
  -> cyclic half-balance
  -> two-list congruence
  -> positive cycle certificate if D|H.
```

This makes substantially larger distributed perturbations auditable. It does not make a hit likely: a successful word must still satisfy one full odd denominator, not merely several selected factors.

## 8. Gap audit

- `X-9602` uses the minimum number of **distinct unit pulses** only.
- Multiple pulse units at one position are covered by `(5)` but not by that experiment.
- Pulse counts above the minimum are not covered by the frozen `X-9602` packet.
- The theorem applies to perturbations of an already known negative cycle; it does not cover arbitrary compressed valuation words.
- No nontrivial positive cycle, divergent seed, or Collatz counterexample is claimed.
