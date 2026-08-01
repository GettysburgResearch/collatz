# L-6806 — Mechanical swap area controls surplus and factor complexity

**Claim ID:** `L-6806`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** elementary binary-word dominance; PR #76's first-crossing mechanical extremizer  
**Scope:** coefficient-first-crossing binary words

## 1. Mechanical reference word

Put

\[
\alpha=\frac{\log2}{\log3}.
\]

Let `v` be a coefficient-first-crossing word of length `j`, with prefix counts

\[
S_m=\sum_{i=0}^{m-1}v_i.
\]

Then

\[
S_m\ge\lceil\alpha m\rceil
\qquad(1\le m<j),
\tag{1}
\]

and the final bit is zero. Since the interval

\[
[\alpha(j-1),\alpha j)
\]

has length `alpha<1`, the total weight is uniquely

\[
q=\lceil\alpha(j-1)\rceil.
\tag{2}
\]

Define the upper mechanical reference word `u` by

\[
U_m=\lceil\alpha m\rceil
\qquad(0\le m<j),
\]

with final bit zero. Then `u` has the same length and total weight as `v`.

## 2. Exact swap-area distance

Define the prefix excesses

\[
h_m=S_m-U_m
\qquad(1\le m<j),
\tag{3}
\]

and the total area

\[
\boxed{
K(v)=\sum_{m=1}^{j-1}h_m.}
\tag{4}
\]

Every `h_m` is a nonnegative integer.

The binary dominance order gives an exact interpretation:

\[
\boxed{
K(v)
=
\text{the minimum number of adjacent moves }10\to01
\text{ needed to transform }v\text{ into }u.}
\tag{5}
\]

### Proof

A move `10 -> 01` decreases exactly one prefix sum by one and leaves every later prefix sum and the total weight unchanged. Therefore it decreases the area `(4)` by exactly one.

Conversely, if `v!=u`, choose the last prefix at which `S_m>U_m`; the dominance condition and equality of total weights expose a `10` whose rightward move preserves every lower-bound constraint and decreases `(4)`. Iterating reaches `u` in exactly `K(v)` steps. ∎

## 3. Hamming-distance bound

One adjacent swap changes two coordinates. Consequently the Hamming distance satisfies

\[
\boxed{d_H(v,u)\le2K(v).}
\tag{6}
\]

This bound is crude but uniform; repeated swaps may cancel coordinate changes.

## 4. Proper-prefix surplus bound

For `m<j`,

\[
D_m(v)=S_m-\alpha m
=(U_m-\alpha m)+h_m.
\]

Since

\[
0<U_m-\alpha m<1,
\]

we obtain

\[
\boxed{
B_v:=\max_{m<j}D_m(v)
<1+\max_mh_m
\le1+K(v).}
\tag{7}
\]

Thus a small swap-area perturbation remains in a narrow coefficient-surplus strip.

## 5. Factor-complexity bound

Fix a factor length `L`. The mechanical word `u` belongs to a Sturmian language, so it has at most

\[
L+1
\]

distinct length-`L` factors.

A coordinate at which `v` differs from `u` belongs to at most `L` factor windows. Every factor window avoiding all changed coordinates is already a factor of `u`. Using `(6)`,

\[
\boxed{
p_v(L)
\le
L+1+2K(v)L.}
\tag{8}
\]

Here `p_v(L)` counts the distinct length-`L` factors inside the proper prefix used by `T-6803`; deleting the final position only decreases the count.

## 6. Exact remainder monotonicity

Each adjacent move `10 -> 01` increases the final affine remainder. Therefore the same `K(v)` is also the natural combinatorial distance from PR #76's maximum-remainder word.

More precisely, if the common suffix after the swapped pair has length `h` and weight `t`, the endpoint increase is exactly

\[
\boxed{
\frac{3^t}{2^{h+2}}.}
\tag{9}
\]

This follows because `01` exceeds `10` by `1/4` immediately after the two changed steps, and the common suffix multiplies differences by `3^t/2^h`.

Equation `(9)` is the starting point for a future quantitative stability theorem linking remainder retention to the swap area.

## 7. Gap audit

- A small Hamming distance does not determine the exact swap area, but `(6)` is sufficient for complexity control.
- The converse of `(8)` is false: a word may have low complexity without being close to this particular mechanical word.
- Large `K(v)` is not itself contradictory.
- The lemma does not prove that a no-descent word has small `K(v)`; that is the remaining stability problem.