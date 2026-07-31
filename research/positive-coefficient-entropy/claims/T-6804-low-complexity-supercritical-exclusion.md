# T-6804 — Critical low-complexity supercritical paths are nonordinary

**Claim ID:** `T-6804`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6801`, `L-6802`, `L-6804`  
**Scope:** positive ordinary shortcut-Collatz paths with coefficient-supercritical every prefix

## 1. Exact multiscale pressure inequality

Let a fixed positive ordinary orbit satisfy

\[
D_k=q_k-\alpha k\ge0
\qquad(k\ge0),
\qquad
\alpha=\frac{\log2}{\log3}.
\tag{1}
\]

Put

\[
B_N=\max_{0\le k\le N}D_k.
\]

For `1<=L<=N`, let `p_N(L)` be the number of distinct length-`L` parity factors beginning at times `0,...,N-L`, and set

\[
M_N(L)=
\left\lceil
\frac{N-L+1}{p_N(L)}
\right\rceil.
\tag{2}
\]

`L-6804` proves that all orbit states are distinct. Therefore `L-6802` applies without a cycle alternative and gives

\[
n
\ge
3^{-B_N}
\bigl((M_N(L)-1)2^L+1\bigr)
-\frac N2.
\]

Equivalently,

\[
\boxed{
3^{B_N}
\left(n+\frac N2\right)
\ge
(M_N(L)-1)2^L+1.}
\tag{3}
\]

Whenever `M_N(L)>=2`,

\[
\boxed{
B_N
\ge
\log_3
\left(
\frac{2^L+1}{n+N/2}
\right).}
\tag{4}
\]

This places the factor-repetition cost directly on the coefficient surplus of the same ordinary orbit.

## 2. Linear-complexity consequence

Suppose there is a constant `C` such that

\[
p_N(L)\le L+C
\tag{5}
\]

for the scales under consideration. Fix

\[
0<c<\frac12
\]

and take

\[
L_N=\lfloor cN\rfloor.
\]

For all sufficiently large `N`,

\[
N-L_N+1>L_N+C,
\]

so `M_N(L_N)>=2`. Equation `(4)` yields

\[
\boxed{
B_N
\ge
c(\log_3 2)N-O(\log N).}
\tag{6}
\]

Thus a positive ordinary all-time-supercritical path with linear factor complexity must have **linear** maximum coefficient surplus.

## 3. Critical-slope exclusion

Assume instead that

\[
B_N=o(N).
\tag{7}
\]

Then `(6)` is impossible. Consequently:

\[
\boxed{
\begin{array}{c}
D_k\ge0\text{ for every }k,\\
B_N=o(N),\\
p_N(L)\le L+C
\text{ at linear scales}
\end{array}
\quad\Longrightarrow\quad
\text{no positive ordinary realization}.}
\tag{8}
\]

In particular, no Sturmian parity sequence of slope

\[
\alpha=\frac{\log2}{\log3}
\]

can be the parity sequence of a positive ordinary all-time-supercritical orbit. Such a sequence has

\[
p(L)=L+1
\]

and bounded discrepancy

\[
0\le D_k<1
\]

for the upper mechanical intercept.

The same conclusion applies to any fixed linear-complexity language whose realized path has sublinear coefficient surplus.

## 4. More general complexity/surplus dichotomy

Without assuming linear complexity, equation `(3)` gives the exact alternative:

```text
at scale L,

many repeated factors
    -> B_N must be large;

small B_N
    -> almost every starting position must carry a distinct length-L factor.
```

For example, if

\[
B_N=o(L_N),
\qquad
L_N/\log N\to\infty,
\]

then `(3)` forces

\[
M_N(L_N)=1
\]

for all sufficiently large `N`. Equivalently,

\[
\boxed{
p_N(L_N)=N-L_N+1,}
\tag{9}
\]

so **every** length-`L_N` factor in that prefix is distinct.

Any hypothetical ordinary all-time-supercritical path with sublinear surplus must therefore exhibit near-maximal finite factor complexity at every superlogarithmic scale.

## 5. Relationship to Box 1

Box 1 asks for complete source escape:

\[
m_N^{sup}\to\infty.
\]

`T-6804` proves this only for the strict family in `(8)`. It eliminates:

- coefficient-critical Sturmian/mechanical schedules;
- bounded-discrepancy linear-complexity schedules;
- more generally, any sublinear-surplus path with enough factor repetition at a superlogarithmic scale.

A surviving ordinary path must pay one of two extreme prices:

\[
\boxed{
\text{linear-scale surplus}
\quad\text{or}\quad
\text{near-maximal factor novelty at all relevant scales}.}
\tag{10}
\]

This is a genuine infinite-class exclusion but not the full escape theorem.

## 6. Gap audit

- Linear surplus is not contradictory; an aperiodic high-density path remains outside the theorem.
- High factor novelty is also not contradictory by itself.
- The result is pointwise and ordinary; no measure or randomness assumption is used.
- The theorem does not prove `m_N^{sup}->infinity` for the unrestricted supercritical language.
- `T-6802` supplies a weaker universal logarithmic surplus floor; `T-6804` supplies a much stronger family-specific linear floor.