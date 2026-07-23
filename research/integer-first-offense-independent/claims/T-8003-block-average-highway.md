# T-8003 — Exact block-average highway criterion

**Claim ID:** `T-8003`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** local `L-8002` and `T-8002`  
**Scope:** positive ordinary paths in the negative-three-cycle pulse chart

## Statement

Use the exact maximal-run section of `L-8002`. At section time `j`, write

\[
z_j=2^{3r_j}u_j,
\qquad r_j\ge0,
\qquad u_j>0\text{ odd},
\]

so that one macro `A^(r_j)B` gives

\[
\boxed{
z_{j+1}=\frac{9^{r_j+1}u_j+7}{16}.}
\tag{1}
\]

For

\[
S_N=\sum_{j=0}^{N-1}r_j,
\]

every legal positive path satisfies

\[
\boxed{
z_N
>
z_0\,2^{(9S_N-44N)/53}.}
\tag{2}
\]

Consequently, either of the following is sufficient for an unconditional divergent Collatz orbit once one explicit ordinary all-time chart path is supplied:

1. **asymptotic average criterion**
   \[
   9S_N-44N\longrightarrow+\infty;
   \tag{3}
   \]
2. **nine-run block criterion**: there is an index `J` such that for every `m>=0`,
   \[
   \sum_{j=J+9m}^{J+9m+8}r_j\ge44.
   \tag{4}
   \]

Under `(4)`, the section states grow strictly at every ninth macro, with exact multiplicative lower factor

\[
\boxed{\frac{9^{53}}{2^{168}}>1.}
\tag{5}
\]

In particular, the earlier condition `r_j>=5` for every `j` is sufficient but not necessary. Condition `(4)` permits, for example, one run of length `4` together with eight runs of length `5` in each nine-run block.

The physical shortcut-Collatz state is `n_j=6z_j-5`; hence unbounded `z_j` gives an unconditional positive divergent Collatz orbit.

## Proof

From `(1)` and `z_j=2^(3r_j)u_j`,

\[
\begin{aligned}
z_{j+1}
&=\frac{9^{r_j+1}u_j+7}{16}\\
&>\frac{9^{r_j+1}u_j}{16}\\
&=\frac{9^{r_j+1}}{2^{3r_j+4}}z_j.
\end{aligned}
\tag{6}
\]

Multiplying `(6)` for `j=0,...,N-1` gives

\[
 z_N
>
z_0\frac{9^{S_N+N}}{2^{3S_N+4N}}.
\tag{7}
\]

The exact integer inequality

\[
\boxed{
9^{53}
=
375710212613636260325580163599137907799836383538729
>
374144419156711147060143317175368453031918731001856
=
2^{168}}
\tag{8}
\]

implies

\[
\log_2 9>\frac{168}{53}.
\tag{9}
\]

Taking base-two logarithms in the multiplier of `(7)` and using `(9)`,

\[
\begin{aligned}
(S_N+N)\log_2 9-(3S_N+4N)
&>\frac{168(S_N+N)-53(3S_N+4N)}{53}\\
&=\frac{9S_N-44N}{53}.
\end{aligned}
\tag{10}
\]

Exponentiating proves `(2)`. Criterion `(3)` now makes the right side of `(2)` tend to infinity.

For one block of nine macros with total run length at least `44`, the product in `(7)` over that block is at least

\[
\frac{9^{44+9}}{2^{3\cdot44+4\cdot9}}
=
\frac{9^{53}}{2^{168}}
>1.
\tag{11}
\]

Repeated application proves strict growth along the nine-block subsequence and hence unboundedness, proving `(4)--(5)`. The physical implication is the exact chart embedding of `O-8001`. ∎

## Why this matters

The one-counter construction no longer needs to force every run into the pointwise highway `r>=5`. It may spend a bounded number of short runs provided the exact cumulative resource obeys `(3)` or the finite-window certificate `(4)`.

This materially enlarges the target language for an inductive invariant:

```text
old target:
  every emitted run >= 5;

new finite-window target:
  every nine emitted runs have total >= 44.
```

The latter is compatible with a finite phase counter and can be searched by proof-carrying PDR or a changing-modulus quotient invariant without weakening the final divergence conclusion.

## Gap audit

- The theorem proves growth only after an ordinary all-time legal chart path has been constructed.
- It does not prove that any finite initial quotient emits a schedule satisfying `(3)` or `(4)`.
- It does not infer an ordinary path from a compatible `2`-adic directive.
- The strict `+7` toll is discarded in `(6)`, so the bound is safe but not optimal.
- Average run length exactly `44/9` is enough under the block condition because `(8)` is strict; a mere asymptotic liminf equal to `44/9` without controlled cumulative surplus is not separately asserted.

## Suggested next attack

Augment the exact quotient state of `L-8002` by a nine-step finite resource counter

```text
(number of runs in current window,
 accumulated run total capped at 44).
```

Search for an inductive ordinary top-boundary invariant that resets only after reaching total `44`. This is strictly less restrictive than the all-`r>=5` search and retains a finite, exact divergence certificate.