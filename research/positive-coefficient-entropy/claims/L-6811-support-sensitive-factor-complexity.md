# L-6811 — Displaced support controls factor complexity and forces a long return

**Claim ID:** `L-6811`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6806`, `L-6808`; elementary factor counting  
**Scope:** coefficient-first-crossing words relative to the upper-mechanical extremizer

## 1. Setup

Fix a valid first-crossing length `j` and weight `q`.  Let

\[
w=w^{\rm mech}_{j,q}
\]

be the upper-mechanical word and let `v` be any other admissible
first-crossing word of the same length and weight.

Write the odd positions as

\[
d_1(v)<\cdots<d_q(v),
\qquad
d_1(w)<\cdots<d_q(w).
\]

Prefix dominance gives

\[
d_i(v)\le d_i(w).
\]

Put

\[
h_i=d_i(w)-d_i(v)\ge0
\]

and define the **displaced support**

\[
\boxed{
R(v)=\#\{i:h_i>0\}.}
\tag{1}
\]

All factors below are taken in the proper prefix

\[
v_0v_1\cdots v_{j-2},
\]

so that the forced final crossing bit is not used as a factor endpoint.
Let `p_v(L)` be the number of distinct length-`L` factors beginning at the
`j-L` proper starts

\[
0,1,\ldots,j-1-L.
\]

## 2. Hamming support is at most twice the displaced support

Moving the `i`th odd bit from `d_i(v)` to `d_i(w)` can change only the two
endpoint positions

\[
d_i(v),\qquad d_i(w).
\]

Different moves may cancel or share endpoints.  Consequently the set

\[
\mathcal E(v,w)
=\{m<j-1:v_m\ne w_m\}
\]

satisfies

\[
\boxed{|
\mathcal E(v,w)|\le2R(v).}
\tag{2}
\]

This bound is deliberately one-sided: no disjointness of the moved intervals
is assumed.

## 3. Support-sensitive factor-complexity bound

The proper mechanical word is a factor of one Sturmian language, so its
length-`L` factors have cardinality at most

\[
L+1.
\tag{3}
\]

A length-`L` window of `v` that avoids `\mathcal E(v,w)` is also a
length-`L` factor of `w`.  Each edited position belongs to at most `L`
proper windows.  Thus at most

\[
|
\mathcal E(v,w)|L\le2R(v)L
\]

windows meet an edit, even if every such window creates a new factor.
Therefore

\[
\boxed{
p_v(L)\le L+1+2R(v)L.}
\tag{4}
\]

This replaces the earlier swap-area estimate

\[
p_v(L)\le L+1+2I(v)L
\]

by the generally stronger support-sensitive bound.

## 4. Forced repeated factor

Put

\[
\boxed{
L_R(j,R)
=
\left\lfloor
{j-2\over2(R+1)}
\right\rfloor.}
\tag{5}
\]

Whenever `L_R>=1`,

\[
2(R+1)L_R\le j-2.
\]

Using `(4)`,

\[
\begin{aligned}
p_v(L_R)
&\le (2R+1)L_R+1\\
&=2(R+1)L_R-L_R+1\\
&\le j-L_R-1\\
&<j-L_R.
\end{aligned}
\]

There are `j-L_R` proper starts, so two of them carry the same
length-`L_R` parity factor.  Hence

\[
\boxed{
L_R(j,R)\ge1
\Longrightarrow
\text{the proper prefix contains a repeated factor of length }L_R.}
\tag{6}
\]

## 5. Physical alternatives

Let `r_v` be the canonical ordinary source of `v` and replay the proper
segment physically.

The two starts obtained in `(6)` have one of two exact dispositions.

1. **Equal physical states.**  The canonical segment has entered a positive
   periodic orbit.  This is the positive-cycle alternative and must be
   retained explicitly.

2. **Distinct physical states.**  `L-6801` gives full dyadic separation:
   their difference is a nonzero multiple of `2^(L_R)`.  Therefore every
   no-descent return/gap theorem may be applied with this exact factor length.

In particular, combining `(6)` with the source-free return barrier of the
parallel coefficient-tangent packet gives the necessary inequality

\[
\boxed{
2^{L_R}+1
<
3^{B(v)}
\left({j\over\lambda_j}+{j\over2}\right),}
\tag{7}
\]

for every acyclic canonical first-crossing failure, where

\[
\lambda_j=j\log2-q\log3>0.
\]

Equation `(7)` is recorded here as a handoff; its proof is the exact physical
return argument, not an entropy approximation.

## 6. Why support is the correct variable

The total swap area

\[
I(v)=\sum_i h_i
\]

can be concentrated in a few very long moves.  Such concentration does not
create many edited bit positions.  Conversely, factor complexity sees the
number of positions at which the binary word actually differs from the
mechanical word.

`L-6811` therefore supplies the missing conversion

```text
number of displaced odd positions
    -> Hamming support
    -> factor complexity
    -> one exact long physical return.
```

This is what allows the square-root support theorem `T-6810`.

## 7. Gap audit

- The result does not exclude the positive-cycle alternative.
- A support of order `sqrt(j)` can defeat the forced-return contradiction.
- The factor count is an upper bound, not an equality.
- No modular distribution of the displacement numerator is asserted.
- No proof of CST, Box 1, Box 2, or Collatz is claimed.
