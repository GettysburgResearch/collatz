# T-9301 — Polynomial-window reduction to EQ

**Claim ID:** T-9301  
**Title:** Full weighted EQ follows from maximal decay on a polynomial-size numerator window  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9301`, `L-9302`; an explicitly stated frequency block-mean hypothesis  
**Scope:** conditional reduction for the issue-#4 EQ target  
**Related counterexample candidates:** none

## Statement

For every `K >= 1`, define

\[
F_K(\theta)
=\left|\widehat\mu\!\left(\frac{\theta}{64^K}\right)\right|
=\frac{|S_K(\theta)|}{2^K},
\qquad 1\le\theta\le2^K,
\]

using `L-9301`, and define the weighted Fourier sum

\[
E_K=\sum_{1\le\theta\le2^K}
\frac{F_K(\theta)}{\theta}.
\]

Assume that there is a constant

\[
\frac1{81}<a<1
\]

such that, for every `K`, every `r >= 0` with `81^r <= 2^K`, and every interval `I` of exactly `81^r` consecutive frequencies contained in `{1,...,2^K}`,

\[
\sum_{\theta\in I}F_K(\theta)
\le81^r a^r. \tag{FBM}
\]

Let `M_K` be any integer sequence satisfying

\[
M_K\longrightarrow\infty,
\qquad
81^{M_K}\le2^K,
\]

and put

\[
\eta_K=\max_{1\le\theta<81^{M_K}}F_K(\theta).
\]

If

\[
\boxed{M_K\eta_K\longrightarrow0,}
\]

then

\[
\boxed{E_K\longrightarrow0.}
\]

In particular, `(FBM)` plus the following polynomial-window estimate is sufficient:

> There exist constants `A>0`, `b>0`, and `K_0` such that, for every `K >= K_0`,
> \[
> \boxed{
> \max_{1\le\theta\le K^A}F_K(\theta)\le K^{-b}.
> } \tag{PWM}
> \]

Thus the all-depth EQ discrepancy target does not require pointwise control for all `2^K` frequencies. It is enough to prove polynomial decay on any fixed positive polynomial window.

## Definitions

`(FBM)` is an abstract hypothesis. The proposed Theorem 11 in issue #4 suggests the specific value

\[
a=\frac2\pi+\frac1{81},
\]

but this packet does not promote that branch-qualified result.

`(PWM)` is a maximal estimate over integer numerators, not a statement for each fixed numerator separately.

The phrase *full weighted EQ target* refers to `E_K -> 0`, the Fourier sum used in the issue-#4 Erdős--Turán reduction.

## Motivation

The live EQ discussion isolates an apparently severe demand: simultaneous decay for every `1 <= theta <= 2^K`. That demand is stronger than necessary because high frequencies are multiplied by `1/theta` and already have strong block-average control. This theorem identifies the true remaining pointwise burden.

The reduction changes the scale of the flagship problem from exponentially many frequencies to polynomially many. It does not make the residual maximal estimate automatic; one exceptional small numerator can still obstruct the conclusion.

## Proof

Split the weighted sum at `81^(M_K)`:

\[
E_K=E_K^{\mathrm{low}}+E_K^{\mathrm{high}},
\]

where

\[
E_K^{\mathrm{low}}
=\sum_{1\le\theta<81^{M_K}}
\frac{F_K(\theta)}\theta.
\]

By the definition of `eta_K`,

\[
\begin{aligned}
E_K^{\mathrm{low}}
&\le\eta_K
\sum_{1\le\theta<81^{M_K}}\frac1\theta\\
&\le\eta_K\bigl(1+\log(81^{M_K})\bigr)\\
&=\eta_K\bigl(1+M_K\log81\bigr).
\end{aligned}
\]

The assumption `M_K eta_K -> 0` therefore gives

\[
E_K^{\mathrm{low}}\longrightarrow0. \tag{1}
\]

For the high part, apply `L-9302` to

\[
H=2^K,\qquad F=F_K,\qquad M=M_K.
\]

The hypothesis `(FBM)` is exactly the block hypothesis of that lemma, so

\[
E_K^{\mathrm{high}}
=\sum_{81^{M_K}\le\theta\le2^K}
\frac{F_K(\theta)}\theta
\le C_a a^{M_K}.
\]

Since `a<1` and `M_K -> infinity`,

\[
E_K^{\mathrm{high}}\longrightarrow0. \tag{2}
\]

Equations `(1)` and `(2)` prove `E_K -> 0`.

For the polynomial-window corollary, assume `(PWM)` and choose

\[
M_K=\left\lfloor\frac{A\log K}{\log81}\right\rfloor.
\]

For all sufficiently large `K`,

\[
81^{M_K}\le K^A<2^K,
\]

so

\[
\eta_K\le K^{-b}.
\]

Also `M_K=O(log K)`, hence

\[
M_K\eta_K=O((\log K)K^{-b})\longrightarrow0.
\]

The first part now applies. QED.

## Dependency audit

- `L-9301` identifies the finite normalized Fourier sum with the fixed-measure coefficient. The reduction would remain true if `F_K` were defined directly from `S_K`.
- `L-9302` supplies the high-frequency harmonic-tail estimate.
- `(FBM)` is an explicit external input. The intended branch-qualified source is issue #4's proposed block-frequency theorem; this packet does not verify it.
- No fixed-frequency depth-average theorem is used.

## Gap audit

- Pointwise decay for every fixed `theta` does not imply `(PWM)` because the maximum ranges over a growing set.
- An average over `theta <= K^A` does not imply `(PWM)` without an inverse theorem controlling exceptional spikes.
- The theorem proves a sufficient condition for the EQ Fourier criterion, not the nonexistence of an integer in `V_infinity`.
- The cutoff exponent `A` may be arbitrarily small but must be fixed and positive.
- The polynomial decay exponent `b` may also be arbitrarily small but must be uniform in `theta` and `K`.
- No interchange of limits occurs: one explicit cutoff is chosen for each `K`, and both pieces are bounded uniformly.

## Adversarial tests

1. If `M_K` is bounded, the high-frequency estimate need not vanish; this is why `M_K -> infinity` is explicit.
2. If `eta_K=1/log K` and `M_K` is proportional to `log K`, then `M_K eta_K` stays bounded away from zero; the low harmonic sum can remain large.
3. If `(PWM)` holds only for `theta <= (log K)^A`, the same proof still works by choosing `M_K` proportional to `log log K`. Polynomial size is a clean sufficient target, not the weakest possible one.
4. If one frequency below the cutoff has coefficient `1`, the theorem correctly refuses to conclude even if all other frequencies are tiny.

## Remaining uncertainty

The reduction is elementary and complete-looking. The application risk is the exact all-block quantifier in `(FBM)` and the branch status of that input.

## Suggested next attack

Prove `C-9301`, or prove a weaker direct form of `(PWM)`. The most promising route may be an inverse theorem: show that one large low-frequency coefficient forces a whole nearby block of large coefficients, contradicting `(FBM)`.
