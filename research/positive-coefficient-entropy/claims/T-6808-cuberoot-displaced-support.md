# T-6808 — Every acyclic first-crossing failure has cube-root growing displaced support

**Claim ID:** `T-6808`  
**Status:** **PROPOSED / SOURCE-QUALIFIED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6808`; PR #82 `L-6605`; the quoted Rhin bound  
**Scope:** unbounded acyclic canonical first-crossing target-failure families

## 1. Statement

Use the hypotheses of `T-6807`.  Let

\[
R_j
=
\#\{i:d_i(v_j)<d_i(w_j)\}
\]

be the number of odd positions displaced from the upper-mechanical word.

Then

\[
\boxed{
\liminf_{j\to\infty}
\frac{R_j}{j^{1/3}}
\ge
\left(\frac{\alpha^2}{2}\right)^{1/3},
\qquad
\alpha=\frac{\log2}{\log3}.
}
\tag{1}
\]

Numerically, the constant is

```text
0.5838626227...
```

for orientation only.

Thus a surviving delayed-crossing obstruction requires genuinely growing
support; one, two, three, or any \(o(j^{1/3})\) displaced odd positions are
eventually impossible.

## 2. Support ceilings for bank and swap area

`L-6808` proves

\[
B_j<R_j+1
\tag{2}
\]

and

\[
I_j
<
R_j\left[
1+\log_2j+(R_j+2)\log_2 3
\right].
\tag{3}
\]

Put

\[
G_j=\alpha+14.3\log_3j+\log_3(3/2).
\tag{4}
\]

The bank--displacement uncertainty theorem gives

\[
(I_j+1)(B_j+G_j)>\frac{\alpha(j-2)}2.
\tag{5}
\]

Substitution of `(2)--(3)` into `(5)` yields the explicit necessary condition

\[
\boxed{
\left(
R_j[1+\log_2j+(R_j+2)\log_2 3]+1
\right)
(R_j+1+G_j)
>
\frac{\alpha(j-2)}2.
}
\tag{6}
\]

## 3. Asymptotic extraction

If \(R_j/j^{1/3}\) is unbounded, `(1)` is automatic.  Otherwise pass to a
subsequence with

\[
\frac{R_j}{j^{1/3}}\longrightarrow t<\infty.
\]

After division of `(6)` by \(j\), all logarithmic terms vanish.  Since

\[
\log_2 3=\frac1\alpha,
\]

the limiting inequality is

\[
\frac{t^3}{\alpha}\ge\frac{\alpha}{2}.
\]

Therefore

\[
t^3\ge\frac{\alpha^2}{2},
\]

which proves `(1)`.

## 4. Full-denominator relevance

PR #82 `T-6609` reduces each fixed crossing length to fewer than \(j/2\)
complete-denominator target levels.  `T-6808` shows that an unbounded family
hitting those levels cannot arise from a fixed-support or slowly growing
repair packet.

This interfaces directly with the repository's centered-defect, pulse, and
full-denominator compilers:

\[
\boxed{
\text{any acyclic CST obstruction has at least }
(0.5838\ldots-o(1))j^{1/3}
\text{ displaced odd positions.}
}
\]

The cycle level is retained separately.

## 5. Gap audit

- Cube-root and larger support remains possible.
- The theorem is about displaced odd positions relative to the mechanical
  word, not arbitrary non-\(2\) accelerated valuations.
- The source dependence and positive-cycle alternative are explicit.
- No complete-denominator avoidance theorem is proved.
- Box 2 and Collatz remain open.
