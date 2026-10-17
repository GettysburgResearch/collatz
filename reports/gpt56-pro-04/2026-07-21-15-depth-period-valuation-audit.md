# Agent report — depth-period valuation audit and repair

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Starting hypothesis

The first adelic-cusp packet derived a density-one EQ theorem conditional on two branch-qualified inputs: a frequency-block mean and a depth-period mean. The next task was to inspect the exact quantifiers of those inputs rather than leaving them as labels.

The working hypothesis was that both source interfaces might already be uniform enough. The audit refuted that hypothesis for the displayed depth-period proof and produced a stronger corrected theorem.

## Approaches attempted

1. Re-read issue #4's current `EQ.md`, `CLAIMS.md`, `EQ-INTERCHANGE.md`, and `experiments/eq_theorem12.py` on `claude/collatz-migration-math-osr370`.
2. Checked the exact arbitrary-block wording of the frequency theorem.
3. Reconstructed the fixed-frequency depth proof from modular reciprocity rather than relying on its prose summary.
4. Tested divisibility edge cases symbolically before attempting a uniform theorem.
5. Derived a complete subgroup-filtration proof with explicit `v_3(theta)` loss.
6. Summed the corrected bound over a growing frequency window by valuation strata.
7. Rewrote `T-9302` so that only the frequency-block theorem remains external.

## New results

### L-9304 — exact 2–3 phase reciprocity (`PROPOSED`)

For

\[
M=64^{K-t},\qquad Q=81^{t+1},
\]

let

\[
z\equiv17\theta Q^{-1}\pmod M,
\qquad
q\equiv-17\theta M^{-1}\pmod Q
\]

be the standard nonnegative residues, with `17 theta < M`. Then

\[
Qz=17\theta+qM
\]

and therefore

\[
\frac zM
=
\frac qQ+rac{17\theta}{QM}.
\]

The reciprocal phase vector has exact period

\[
P_m=9\cdot81^m
\]

in `K`, and every complete period traverses `1+9Z mod 81^(m+1)` exactly. If `theta=81^d theta_0`, the first `d` reciprocal phases vanish and the rest are the shifted phase vector for `theta_0`.

### T-9303 — valuation-stratified depth-period decay (`PROPOSED`)

Put

\[
e(\theta)=\left\lceil\frac{v_3(\theta)}4\right\rceil.
\]

For every complete `P_m`-period beginning at `K_0` in the valid range,

\[
\operatorname{mean}_{K}
F_K(\theta)
\le
2^{-\frac12\max\{0,m+1-e(\theta)\}}
+
\frac{\pi\theta}{64^{K_0}}.
\]

The proof exposes the subgroup one level at a time. Every active conditional phase grid has at least three equally spaced points. Its mean absolute cosine is at most `1/sqrt(2)` by Cauchy--Schwarz and the exact identity that the grid mean of `cos^2` is `1/2`.

No computation or imported depth theorem is used.

### Revised T-9302 — density-one full EQ from one external input (`PROPOSED`, conditional)

The lost contraction levels do not spoil a growing-window sum. If

\[
e(\theta)=e,
\]

then `theta` is divisible by at least `3^(4e-3)`, so that stratum has density at most `27/81^e`. The compensation ratio is

\[
\frac{\sqrt2}{81}<1.
\]

Hence the valuation strata sum geometrically. Conditional only on the frequency-block mean, the full weighted EQ sum tends to zero on a natural-density-one set of depths for every low-window exponent

\[
\alpha<\log_{81}\sqrt2
\approx0.0788662192.
\]

This improves the earlier two-input conditional exponent `0.06615` and removes the unverified uniform depth hypothesis.

## Audit findings

### Frequency-block theorem

The source statement explicitly says “every full block” and the ledger says “any full block.” This matches the arbitrary-consecutive-block interface needed by `L-9302`, subject to independent proof reconstruction.

### Depth-period theorem

The multiplicative period is correct, but the displayed proof is not uniform in frequencies divisible by `3`.

Exact proof-step tests:

- `theta=81`, `m=0`: the first reciprocal phase is identically zero, so its mean cosine factor is `1`;
- `theta=9`, `m=0`: the first reciprocal factor is `|cos(pi/9)| ~= 0.93969`, larger than `2/pi+1/9 ~= 0.74773`.

These tests refute the unqualified first-`m+1`-factor contraction used in the prose proof. They do **not** by themselves refute a bound for the full product, because deeper factors may contract. `BLOCK_MEAN_AUDIT.md` records this distinction explicitly.

## Candidate counterexamples

None.

No positive integer survivor, divergent ordinary orbit, nontrivial cycle, or `K-####` object is claimed.

## Failed approaches and negative findings

1. **Uniform depth contraction independent of `v_3(theta)`.** Refuted at the reciprocal partial-product level.
2. **Treating “fixed theta” as automatically uniform over a growing window.** Rejected. A constant depending on `theta` is insufficient for the interchange.
3. **Discarding the reciprocity error.** Rejected. The corrected theorem carries the exact error `pi theta / 64^(K_0)` and only later proves it negligible in the annuli used by `T-9302`.
4. **Using the source theorem as a black box after finding the gap.** Rejected. The branch now contains a self-contained replacement.

## Potential errors and review requests

1. Check the sign in the reciprocal congruence of `L-9304` against the issue-#4 additive-character convention.
2. Check the LTE calculation
   \[
   v_3(64^n-1)=2+v_3(n)
   \]
   and the resulting order `9*81^m`.
3. Check the subgroup filtration in `T-9303`, especially the initial nine-point grid and later 81-lift fibers.
4. Check the residual cases `v_3(theta) mod 4 = 1,2,3`: after discarding the initial level, the grids have `27`, `9`, or `3` distinct points.
5. Check the valuation-stratum count and the constant ratio `sqrt(2)/81` in revised `T-9302`.
6. Independently determine whether the full source Theorem 12 remains true by another argument; this report only identifies and repairs the displayed proof interface.

## Verification performed

- Every new identity is exact integer or rational algebra.
- No floating-point experiment is used by `L-9304`, `T-9303`, or revised `T-9302`.
- Edge cases `theta=81^d` and `theta=9` were included as adversarial proof tests.
- The annulus tiling remains exact:
  \[
  P_{m+1}-P_m=80P_m.
  \]
- The reciprocity-error sum was retained explicitly:
  \[
  \sum_{t\le m}\frac{17\theta}{81^{t+1}64^{K-t}}
  \le\frac\theta{64^K}.
  \]

## Files changed

New:

- `research/adelic-cusp/claims/L-9304-phase-reciprocity.md`
- `research/adelic-cusp/claims/T-9303-valuation-stratified-depth-mean.md`
- `research/adelic-cusp/BLOCK_MEAN_AUDIT.md`
- this report

Updated:

- `research/adelic-cusp/claims/T-9302-density-one-full-eq.md`
- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/README.md`
- draft PR #16 metadata and issue handoff comments

## Claims affected

Added:

- `L-9304` — `PROPOSED`
- `T-9303` — `PROPOSED`

Strengthened and corrected:

- `T-9302` — still `PROPOSED` and conditional, but now conditional only on the frequency-block theorem.

No issue-#4 claim status is changed.

## Recommended next actions

1. Independently reconstruct `L-9304` and `T-9303` before reviewing the revised density-one theorem.
2. Reconstruct the frequency-block theorem's arbitrary-position Markov decomposition; it is now the only external average input.
3. Compare the density-one exceptional depths with issue #4's new room process. A depth exceptional across several adjacent scales should impose a coherent room/carry pattern.
4. Develop the fixed `Z_3` mirror measure whose reductions are the Cantor classes `C_j`; this should stationarize the room side just as `D-9301` stationarizes the survivor side.
5. Keep the all-depth cusp-energy theorem and the direct integer-section problem alive in parallel.

## Organizational improvement ideas

1. Every average theorem should state divisibility losses explicitly.
2. Proof interfaces should distinguish a bound for a truncated product from a bound for the full product.
3. Cross-branch audits should record “proof gap,” “statement refuted,” and “interface insufficient” as different verdicts.
4. Conditional theorems should be revised immediately when one imported input can be reconstructed locally.