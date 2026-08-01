# L-6805 — Bilateral canonical-corner stabilization

**Claim ID:** `L-6805`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6803`; elementary affine numerator expansion  
**Scope:** a hypothetical positive ordinary orbit with coefficient-supercritical every prefix

## 1. Statement

Let `n>0` and suppose its shortcut-Collatz orbit satisfies

\[
3^{q_k}\ge2^k
\qquad(k\ge0).
\tag{1}
\]

Let `w_k` be its length-`k` parity prefix, and let

\[
(r_k,s_k)
\in[1,2^k]\times[1,3^{q_k}]
\]

be the canonical start–end pair from `L-6803`.

Then for every sufficiently large `k`,

\[
\boxed{r_k=n,
\qquad
s_k=T^k(n).}
\tag{2}
\]

Moreover,

\[
\boxed{
\frac{r_k}{2^k}=rac{n}{2^k}\longrightarrow0,}
\tag{3}
\]

and

\[
\boxed{
0<rac{s_k}{3^{q_k}}
\le
\frac{n+k/2}{2^k}\longrightarrow0.}
\tag{4}
\]

Thus an ordinary all-time-supercritical path must approach the lower-left corner of the complete source–endpoint rectangle at both places, even while its unnormalized endpoint tends to `+infinity` under `T-6709`.

## 2. Source stabilization

For `2^k>n`, the fixed ordinary start `n` lies in the canonical source interval `[1,2^k]`. Since it realizes the parity word `w_k`, uniqueness in `L-6803` gives

\[
r_k=n.
\tag{5}
\]

This is the ordinary-extraction condition in its simplest finite form: the source representatives eventually stop changing.

## 3. Endpoint bound

The exact numerator expansion is

\[
A_k
=
\sum_{m=1}^{k}
 v_{m-1}2^{m-1}3^{q_k-q_m}.
\tag{6}
\]

Divide by `3^{q_k}`:

\[
\frac{A_k}{3^{q_k}}
=
\sum_{m=1}^{k}
 v_{m-1}\frac{2^{m-1}}{3^{q_m}}.
\tag{7}
\]

By `(1)`, every nonzero summand is at most `1/2`. Hence

\[
0\le\frac{A_k}{3^{q_k}}\le\frac{k}{2}.
\tag{8}
\]

Using

\[
T^k(n)=rac{3^{q_k}n+A_k}{2^k},
\]

we obtain

\[
\frac{T^k(n)}{3^{q_k}}
=
\frac{n+A_k/3^{q_k}}{2^k}
\le
\frac{n+k/2}{2^k}.
\tag{9}
\]

For all sufficiently large `k`, the right side is strictly below one. Thus

\[
1\le T^k(n)<3^{q_k}.
\]

The actual endpoint lies in the canonical endpoint interval, so uniqueness in `L-6803` gives

\[
s_k=T^k(n).
\tag{10}
\]

Equations `(3)`–`(4)` follow.

## 4. Exact reformulation of Box 1

Let `\mathcal W_k^{sup}` be the set of length-`k` words with

\[
3^{q_m}\ge2^m
\qquad(1\le m\le k).
\]

Box 1 is equivalent to the assertion that there is no sequence

\[
w_1\prec w_2\prec\cdots,
\qquad
w_k\in\mathcal W_k^{sup},
\]

whose canonical source coordinates `r_k` eventually stabilize at one positive integer.

`L-6805` adds the endpoint consequence: any such forbidden stabilization would automatically force the canonical endpoints to satisfy

\[
\frac{s_k}{3^{q_k}}\to0
\]

with the explicit exponential envelope `(4)`.

Thus the missing object is not merely a supercritical binary path. It is one path satisfying simultaneous:

```text
real drift:          3^(q_k)/2^k >= 1;
2-adic source:       r_k eventually constant in Z_{>0};
3-adic endpoint:     s_k/3^(q_k) -> 0;
physical replay:     s_k=T^k(r_k).
```

## 5. Gap audit

- The corner conditions are necessary, not contradictory by themselves.
- The theorem does not turn a measure-zero statement into pointwise exclusion.
- The normalized endpoint can tend to zero while the ordinary endpoint grows without bound.
- A proof of Box 1 still needs an arithmetic incompatibility between the supercritical language and eventual source stabilization.