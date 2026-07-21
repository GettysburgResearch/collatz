# Block-mean interface audit

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Audited branch:** `claude/collatz-migration-math-osr370`  
**Audited files:** `EQ.md`, `CLAIMS.md`, `experiments/eq_theorem12.py`  
**Date:** 2026-07-21

## Purpose

`T-9301` and `T-9302` use branch-qualified average estimates from issue #4. This note records the exact interface audit rather than treating the labels “Theorem 11” and “Theorem 12” as opaque dependencies.

No native issue-#4 status is changed by this audit.

## Frequency blocks: interface supported as written

The issue-#4 statement called Theorem 11 says:

> For every full `81^(m+1)`-block inside the survivor range, the mean normalized Fourier coefficient is at most `(2/pi + 1/81)^(m+1)`.

The corresponding ledger entry says “over any full `81^(m+1)`-block in the survivor range.” This is the arbitrary-consecutive-block quantifier needed by `L-9302`, after the harmless reindexing

\[
r=m+1,
\qquad
a=\frac2\pi+\frac1{81}.
\]

The `r=0` case in this packet is the trivial one-point estimate `F_K(theta)<=1`.

**Audit verdict:** the written branch interface supports `(FBM)`. The proof and its Markov decomposition still require independent mathematical reconstruction before promotion.

## Depth blocks: the written proof suppresses a valuation loss

The issue-#4 statement called Theorem 12 says that, for every fixed nonzero `theta`, averaging over a complete period

\[
P_m=9\cdot81^m
\]

gives a contraction `(2/pi+1/9)^(m+1)`. Its experiment header strengthens the wording to “any K-period.”

The subgroup-period part is correct:

\[
\langle64\rangle\pmod{81^{m+1}}
=1+9\mathbb Z/81^{m+1}\mathbb Z,
\]

so every consecutive `P_m` depths traverse the same subgroup.

However, the proof sentence that the Theorem-11 digit decomposition “applies verbatim” for every `theta` misses multiplication collapse when `3 | theta`.

### Exact proof-step counterexamples

These examples concern the reciprocal **partial product used to prove the theorem**, not necessarily the full product after all deeper factors are included.

1. If `theta=81` and `m=0`, the first reciprocal residue is identically zero over the nine-depth period. Its mean cosine factor is `1`, not `2/pi+1/9`.
2. If `theta=9` and `m=0`, the first reciprocal factor is the constant
   \[
   |\cos(\pi/9)|\approx0.9396926,
   \]
   again larger than
   \[
   2/\pi+1/9\approx0.7477309.
   \]

Thus a proof that discards the deeper factors and charges the same contraction at all first `m+1` levels is not uniform in `theta`.

This observation does **not** by itself refute the full issue-#4 theorem statement: the omitted deeper factors can add substantial contraction. It identifies a gap in the displayed proof mechanism and in any downstream theorem that assumes a uniform partial-product bound without valuation bookkeeping.

## Repair

`L-9304` proves the exact reciprocity formula, including the small rational error. `T-9303` then proves, over every complete consecutive period,

\[
\operatorname{mean}_{K\in J}F_K(\theta)
\le
2^{-\frac12\max\{0,m+1-\lceil v_3(\theta)/4\rceil\}}
+
\frac{\pi\theta}{64^{K_0}}.
\]

The lost levels are exact:

- every full factor `81^d | theta` removes `d` reciprocal phases;
- a residual factor `3`, `9`, or `27` costs one initial grid;
- every later grid still has at least three equally spaced points, whose mean absolute cosine is at most `1/sqrt(2)` by an exact second-moment calculation.

`T-9302` groups frequencies by `ceil(v_3(theta)/4)`. The density cost `1/81` per lost level beats the compensation factor `sqrt(2)`, so the valuation strata sum geometrically. The density-one full-EQ conclusion therefore survives with the improved admissible low-window exponent

\[
\alpha<\log_{81}\sqrt2
\approx0.0788662192.
\]

Only the frequency-block theorem remains an external input to the revised `T-9302`.

## Review requests

1. Reconstruct the reciprocal identity and sign in `L-9304`.
2. Check the subgroup filtration in `T-9303`: initial `9`-point grid versus later `81`-lift grids.
3. Check that the issue-#4 Theorem-11 proof is genuinely position-free for every complete consecutive block.
4. Decide whether the issue-#4 Theorem-12 statement itself remains true by a different argument, or should be narrowed to the valuation-stratified form. This packet makes no verdict beyond the proof-interface gap.

## Process recommendation

Average theorems should expose divisibility dependence in their public statement. “For each fixed frequency” and “uniformly over a growing frequency window” are different interfaces even when both yield density-one conclusions after separate summation.