# Infinite-survivor and real-escape claims

All claims in this file are `PROPOSED` until independently reviewed.

## T-9501: Infinite-survivor harmonic summability

**Claim ID:** T-9501  
**Title:** Infinite exact survivors have finite harmonic mass  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9502

### Statement

Let `I_h` be the set of positive exact states admitting an exact future of
length `h`, and let

\[
\mathcal I=\bigcap_{h\ge1}\mathcal I_h.
\]

Then

\[
\boxed{d(\mathcal I_h)=\frac1{12}\left(\frac27\right)^h}
\]

and there exist absolute constants `C,c>0` such that

\[
\boxed{
A_\infty(X):=\#\{n\le X:n\in\mathcal I\}
\le C X e^{-c\sqrt{\log X}}.
}
\]

Consequently

\[
\boxed{\sum_{n\in\mathcal I}\frac1n<\infty.}
\]

### Proof

For fixed length `h`, exact cylinders are disjoint and a word `w` has density
`1/(3*2^(E_w+2))`. Therefore

\[
\sum_{|w|=h}\frac1{3\,2^{E_w+2}}
=\frac1{12}\left(\sum_{r\ge0}2^{-(3r+2)}\right)^h
=\frac1{12}(2/7)^h.
\]

To count starts `p_0<=X`, note that exact legality gives
`2^(3r_i+2)<=p_i`. Put

\[
\beta=\frac{\log(9/8)}{3\log2}.
\]

Then `(9/8)^(r_i)<=p_i^beta`, and for an absolute constant `C_0`,

\[
p_{i+1}\le C_0 p_i^{1+\beta}.
\]

Induction yields

\[
\log p_i\le C_1(1+\beta)^i\log X,
\]

so every realizable letter satisfies

\[
r_i\le C_2(1+\beta)^i\log X.
\]

Hence the number of length-`h` words that can occur below `X` is at most

\[
W_h(X)\le(C_3\log X)^h(1+\beta)^{h(h-1)/2}.
\]

Each relevant cylinder contributes at most its density times `X`, plus one.
Thus

\[
A_\infty(X)\le A_h(X)
\le \frac X{12}(2/7)^h+W_h(X).
\]

Choose `h=floor(c_0 sqrt(log X))` with `c_0>0` sufficiently small. The first
term is `X exp(-c_1 sqrt(log X))`; the logarithm of the second is
`O(sqrt(log X) log log X)+O(c_0^2 log X)`, so it is `X^theta` for some
`theta<1`, and hence smaller than `X exp(-c_2 sqrt(log X))` for large `X`.
This proves the counting bound. Partial summation gives harmonic convergence.

### Gap audit

The constants are not optimized. A reviewer should check the uniform word-count
bound and the `+1` cylinder-count error; both are explicit above.

---

## T-9502: Nonperiodic survivors real-escape

**Claim ID:** T-9502  
**Title:** Every nonperiodic infinite exact orbit has multiplier capital tending to infinity  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9504, T-9501

### Statement

Define

\[
\kappa=\frac{\log(4/3)}{\log(9/8)},\qquad
K_L=\sum_{i<L}r_i-\kappa L.
\]

If an infinite exact positive orbit is nonperiodic, then

\[
\sum_{k\ge1}(8/9)^{K_k}<\infty,
\qquad K_k\to+\infty.
\]

### Proof

A nonperiodic deterministic orbit has distinct states, all in `I`. By T-9501,
`sum 1/p_j` converges. Since `p_j>=4`, the Euler product in L-9504 converges
to a finite positive value. Therefore `sum 1/M_k` converges, so `1/M_k -> 0`.
But

\[
M_k=(9/8)^{K_k},
\]

which gives the result.

---

## T-9503: Equivalent formulations of the infinite obstruction

**Claim ID:** T-9503  
**Title:** Prefix expansion, nonperiodicity, real escape, and finite extremals are equivalent  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9503, T-9502

### Statement

The following are equivalent:

1. an infinite exact orbit has `K_L>0` for every `L>=1`;
2. a nonperiodic infinite exact orbit exists;
3. an infinite exact orbit has `K_L -> +infinity`;
4. the quantities
   \[
   \mu_L=\min\{\Pi(w):|w|=L,\ K_j(w)>0\ (1\le j\le L)\}
   \]
   do not tend to infinity;
5. for some `B`, the tree of prefix-expanding words with `Pi(w)<=B` has an
   infinite branch.

### Proof

`(1)->(2)`: an eventually periodic tail with positive period capital has an
affine return `p -> M p+A` with `M>1,A>0`, whose fixed point is negative. A
negative-capital period eventually violates prefix positivity, and zero capital
is impossible because `kappa` is irrational.

`(2)->(3)` is T-9502. For `(3)->(1)`, `K_L` has a unique global minimum:
differences cannot vanish because `kappa` is irrational. Shift to this minimum.

`(1)->(4)` follows because the fixed start lies in every prefix cylinder.
If `(4)` holds, some bounded positive `P` realizes arbitrarily long
prefix-expanding words. Determinism makes them prefixes of one infinite exact
orbit, giving `(1)`.

`(4)<->(5)` is immediate from the definition and König's lemma once finite
branching is supplied by L-9505 below.

---

## L-9505: Bounded-representative finite branching

**Claim ID:** L-9505  
**Title:** The bounded prefix-expanding cylinder tree is finitely branching  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Dependencies:** L-9503

### Statement

Fix `B`. At a prefix `w` with data

\[
P=\Pi(w),\quad E=E_w,\quad S=S_w,\quad F_w(P)=4Y,
\]

all extensions with representative at most `B` are generated by the finite set

\[
0\le c\le\left\lfloor\frac{B-P}{3\,2^{E+2}}\right\rfloor.
\]

For each `c`, set `N=Y+3^(S+1)c`. A letter exists exactly when

\[
v_2(N)\equiv0\pmod3,
\qquad N/2^{v_2(N)}\equiv1\pmod4,
\]

with `r=v_2(N)/3`, `c<2^(3r+2)`, and the prefix-capital constraint. Hence the
bounded tree is finitely branching, and `mu_L -> infinity` is equivalent to
termination of every bounded tree.

### Proof

This is a direct rearrangement of the carry formula in L-9503. The bound on the
representative bounds `c`; exactness determines `r` uniquely from `N`.
