# T-9302 — Density-one full EQ from two-axis block means

**Claim ID:** T-9302  
**Title:** Frequency-block and depth-block means imply the complete EQ Fourier criterion on density-one depths  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9302`; the two explicit block-mean hypotheses below  
**Scope:** conditional synthesis of the proposed issue-#4 Theorems 11 and 12  
**Related counterexample candidates:** none

## Statement

For `K >= 1` and `1 <= theta <= 2^K`, let

\[
F_K(\theta)=\frac{|S_K(\theta)|}{2^K}
\]

and

\[
E_K=\sum_{1\le\theta\le2^K}
\frac{F_K(\theta)}\theta.
\]

Assume two uniform estimates.

### Frequency-block mean `(FBM)`

There is a constant

\[
\frac1{81}<a<1
\]

such that, for every `K`, every `r >= 0` with `81^r <= 2^K`, and every interval `I` of `81^r` consecutive frequencies inside `{1,...,2^K}`,

\[
\frac1{81^r}\sum_{\theta\in I}F_K(\theta)
\le a^r. \tag{FBM}
\]

### Depth-block mean `(DBM)`

There is a constant

\[
0<b<1
\]

such that, for every integer `m >= 1`, every positive integer `theta`, and every interval `J` of

\[
P_m=9\cdot81^m
\]

consecutive depth indices with every `K in J` at least `m+1`,

\[
\frac1{P_m}\sum_{K\in J}F_K(\theta)
\le b^m. \tag{DBM}
\]

Put

\[
\gamma=-\frac{\log b}{\log81}>0.
\]

Then, for every fixed

\[
0<\alpha<\gamma,
\]

there is a set `G` of positive integers of natural density `1` such that

\[
\boxed{E_K\longrightarrow0\quad\text{as }K\longrightarrow\infty,\ K\in G.}
\]

More quantitatively, define the depth annulus

\[
\mathcal I_m=[P_m,P_{m+1})\cap\mathbb Z
\]

and let

\[
c=\frac{\gamma-\alpha}{2}>0.
\]

All but at most an `81^(-cm)` fraction of `K in I_m` satisfy

\[
\boxed{
E_K
\le81^{-cm}+C_a a^{\lfloor\alpha m\rfloor},
}
\]

where `C_a` is the explicit constant from `L-9302`.

For the proposed issue-#4 constants

\[
a=\frac2\pi+\frac1{81},
\qquad
b=\frac2\pi+\frac19,
\]

one has

\[
\gamma
=-\log_{81}\!\left(\frac2\pi+\frac19\right)
\approx0.06615.
\]

Thus any fixed `alpha < 0.06615` is allowed, conditional on independent verification of the two block hypotheses.

## Definitions

A set `G` has natural density `1` when

\[
\lim_{N\to\infty}\frac{|G\cap\{1,\ldots,N\}|}{N}=1.
\]

The theorem uses an unweighted low-frequency sum as a stronger intermediate quantity. This avoids a second harmonic loss.

The names `(FBM)` and `(DBM)` deliberately expose all quantifiers. The intended branch-qualified inputs are the results called Theorems 11 and 12 in issue #4's `EQ.md`; their repository status is not changed here.

## Motivation

Issue #4 records two perpendicular averaged forms of EQ:

1. strong average decay across frequency blocks at a fixed depth;
2. strong average decay across depth periods at a fixed frequency.

The residual discussion focuses on the all-depth/all-small-frequency interchange. Before attacking that maximal problem, one should combine the two established axes as far as they already go. The result is the full weighted EQ target—not merely fixed-scale equidistribution—along density-one depths.

This theorem localizes the genuine remaining obstruction to the exceptional zero-density set of depths.

## Proof

Fix `alpha` with `0<alpha<gamma`, and set

\[
c=\frac{\gamma-\alpha}{2}.
\]

For each `m`, define the low-frequency cutoff

\[
H_m=\lfloor81^{\alpha m}\rfloor
\]

and the unweighted low-frequency mass

\[
G_m(K)=\sum_{1\le\theta\le H_m}F_K(\theta).
\]

The annulus

\[
\mathcal I_m=[P_m,P_{m+1})
\]

has length

\[
P_{m+1}-P_m
=9\cdot81^{m+1}-9\cdot81^m
=80P_m.
\]

It is therefore the disjoint union of exactly `80` consecutive depth blocks of length `P_m`. Every depth in these blocks is much larger than `m+1`, so `(DBM)` applies.

Take one such depth block `J`. Summing `(DBM)` over all `theta <= H_m` gives

\[
\begin{aligned}
\frac1{|J|}\sum_{K\in J}G_m(K)
&=\sum_{1\le\theta\le H_m}
  \frac1{|J|}\sum_{K\in J}F_K(\theta)\\
&\le H_m b^m\\
&\le81^{\alpha m}b^m\\
&=81^{-(\gamma-\alpha)m}\\
&=81^{-2cm}. \tag{1}
\end{aligned}
\]

Markov's inequality applied to the nonnegative quantity `G_m(K)` shows that the fraction of `K in J` for which

\[
G_m(K)>81^{-cm}
\]

is at most

\[
\frac{81^{-2cm}}{81^{-cm}}=81^{-cm}. \tag{2}
\]

The same bound holds after taking the union of the `80` equal blocks: all but an `81^(-cm)` fraction of `K in I_m` satisfy

\[
G_m(K)\le81^{-cm}. \tag{3}
\]

Call these depths *good at scale `m`*.

Now fix a good `K in I_m`. Its low-frequency weighted contribution is bounded by the stronger unweighted mass:

\[
\sum_{1\le\theta\le H_m}
\frac{F_K(\theta)}\theta
\le G_m(K)
\le81^{-cm}. \tag{4}
\]

Set

\[
M_m=\lfloor\alpha m\rfloor.
\]

Then

\[
81^{M_m}\le H_m
\]

for all sufficiently large `m`. The frequencies above `H_m` form a subset of those above `81^(M_m)`. Applying `L-9302` with `(FBM)` gives

\[
\sum_{H_m<\theta\le2^K}
\frac{F_K(\theta)}\theta
\le
\sum_{81^{M_m}\le\theta\le2^K}
\frac{F_K(\theta)}\theta
\le C_a a^{M_m}. \tag{5}
\]

Combining `(4)` and `(5)` proves the quantitative bound

\[
E_K\le81^{-cm}+C_a a^{\lfloor\alpha m\rfloor}
\]

for every good depth in `I_m`. The right-hand side tends to zero as `m -> infinity`.

It remains to verify density. Let `B_m` be the bad depths in `I_m`. From `(2)`,

\[
|B_m|
\le|I_m|81^{-cm}
=80P_m81^{-cm}.
\]

Up to the endpoint `P_(M+1)`, the total number of bad depths is at most

\[
\sum_{m\le M}80P_m81^{-cm}
=720\sum_{m\le M}81^{(1-c)m}.
\]

If `c<1`, this is `O(81^((1-c)M))`; if `c>=1`, it is even smaller. Since

\[
P_{M+1}=9\cdot81^{M+1},
\]

the ratio is `O(81^(-cM))` and tends to zero. Intermediate endpoints between consecutive `P_M` change only the constant. Therefore the union of the good depths has natural density `1`, and `E_K -> 0` along it. QED.

## Dependency audit

- `L-9302` converts `(FBM)` into the high-frequency weighted tail.
- `(DBM)` is used only in equation `(1)`.
- Markov's inequality and a geometric-series count prove the density statement.
- The fixed-measure identity `L-9301` is conceptually useful but not algebraically necessary once `F_K` is defined.
- No independence between different frequencies or different depths is assumed.

## Gap audit

- This is a conditional theorem. It does not independently verify `(FBM)` or `(DBM)`.
- The phrase “one period” in the intended depth input must mean every complete consecutive period, or periodicity must be used to derive that uniformity.
- Density-one convergence does not imply convergence for every depth.
- The bad depths may contain an infinite structured subsequence and could still contain an M1 witness.
- The cutoff exponent is small because a union bound spends the depth-average exponent `gamma`; no optimality is claimed.
- This result proves the full weighted Fourier criterion along good depths, not merely fixed-frequency decay, but it still does not decide infinite ordinary-integer membership.

## Adversarial tests

1. If `alpha=gamma`, equation `(1)` has no decay and Markov gives no vanishing exceptional fraction. The strict inequality is necessary for this proof.
2. If `(DBM)` holds only for each fixed `theta` with a constant depending on `theta`, the sum over a growing window is invalid.
3. If the depth period were `81^m` but the estimate held only on one preferred block, the tiling of `I_m` would not be justified.
4. The proof never replaces a maximum by an average. It obtains a small **sum** for most depths, which is stronger than simultaneous smallness on those depths.

## Remaining uncertainty

The abstract implication is complete-looking. Independent review should focus on whether the precise `(FBM)` and `(DBM)` quantifiers are truly available from the branch proofs, especially for arbitrary consecutive blocks.

## Suggested next attack

Inspect the exceptional-depth sets produced by the Markov argument symbolically. A useful theorem would show that an exceptional depth at scale `m` forces a coherent low-height carry pattern across several scales; eliminating that pattern could upgrade density-one EQ to all-depth EQ.
