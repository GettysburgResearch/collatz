# Adelic cusp Fourier program

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21  
**Packet status:** theory-first independent attempt; no counterexample claimed

## Thesis

The depth-dependent Fourier products in the active `64 -> 81` survivor program are not intrinsically a triangular family of unrelated finite measures. They are evaluations of **one fixed Bernoulli self-similar measure on `Z_2`** at the moving characters

\[
q_{K,\theta}=\frac{\theta}{64^K}.
\]

The survivor range `1 <= theta <= 2^K` is therefore an adelic cusp: the same rational character tends to zero in the real absolute value while escaping to infinity in the 2-adic absolute value. This stationary reformulation is exact. It supplies the bridge that the literature audit identified as missing before fixed-measure Fourier or renewal techniques can even be considered.

The full-frequency block mean proposed on issue #4 already makes the weighted Erdős--Turán tail above `81^M` exponentially small. Consequently, full EQ does **not** require a pointwise estimate for every `theta <= 2^K`; a polynomial-size low-frequency window is sufficient.

A second pass audited the perpendicular depth-average claim. The subgroup period is real, but multiplication by a frequency divisible by `3` collapses initial phase grids. `L-9304` and `T-9303` now reconstruct the depth-period estimate from scratch with the exact loss `ceil(v_3(theta)/4)`. Summing those valuation strata proves the complete weighted EQ criterion along density-one depths using only the frequency-block theorem as an external input.

## Fixed notation

Set

\[
\rho=\frac{64}{81},\qquad d=\frac{17}{81},\qquad
J_\varepsilon(x)=\rho x+d\varepsilon
\quad(\varepsilon\in\{0,1\}).
\]

For a binary sequence `epsilon=(epsilon_0,epsilon_1,...)`, define

\[
\pi_2(\varepsilon)=
\sum_{t\ge0}d\varepsilon_t\rho^t
\in\mathbb Z_2.
\]

Let `mu` be the pushforward of fair Bernoulli measure under `pi_2`. For the depth-`K` coded residue set `R_K`, let

\[
S_K(\theta)=
\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{\theta A}{64^K}\right),
\qquad
F_K(\theta)=\frac{|S_K(\theta)|}{2^K}.
\]

The active EQ target is the decay of

\[
E_K=
\sum_{1\le\theta\le2^K}
\frac{F_K(\theta)}\theta.
\]

## Results in this packet

| ID | Status | Content |
|---|---|---|
| `D-9301` | `PROPOSED` | One fixed self-similar survivor measure on `Z_2` |
| `L-9301` | `PROPOSED` | Exact moving-character identity `mu-hat(theta/64^K)=2^{-K}S_K(theta)` |
| `L-9302` | `PROPOSED` | Weighted shell lemma: frequency-block means force an exponentially small high-frequency tail |
| `L-9303` | `PROPOSED` | Squared phase energy gives a deterministic Fourier-product bound |
| `L-9304` | `PROPOSED` | Exact reciprocity between the power-of-64 phase and a power-of-81 residue, including the valuation shift |
| `T-9301` | `PROPOSED` | Polynomial-window maximal decay is sufficient for full EQ |
| `T-9302` | `PROPOSED` | Frequency blocks plus `T-9303` imply full EQ along density-one depths |
| `T-9303` | `PROPOSED` | Every complete depth period contracts after losing exactly `ceil(v_3(theta)/4)` phase levels |
| `D-9302` | `PROPOSED` | Exact `{2,3,infinity}`-solenoid natural extension and integer section |
| `C-9301` | `IDEA` | Logarithmic cusp-scattering theorem sufficient for all-depth EQ |
| `O-9301` / `X-9301` | `EMPIRICAL` | Exact bounded scattering census through `K=80`, `theta<=K^2` |

`PROPOSED` means that a complete-looking argument is supplied but has not received independent repository review. `T-9301` and `T-9302` remain conditional on the branch-qualified frequency-block theorem. The depth-period component of `T-9302` is no longer imported: it is proved locally in `T-9303`.

## What is genuinely new here

1. **Stationarization.** The varying finite products are a single fixed `Z_2` Fourier transform sampled on a moving rational cusp.
2. **Weighted-shell compression.** Frequency blocks dispose of all but a polynomial-size numerator window.
3. **Exact 2–3 reciprocity.** Each power-of-64 phase equals a reciprocal residue modulo a power of `81` plus a fully explicit error.
4. **Valuation-stratified depth decay.** Divisibility by `81` removes phase levels, but the loss is exact and summable across a growing window.
5. **One-input density-one synthesis.** The complete EQ weighted sum tends to zero on density-one depths conditional only on the frequency-block theorem, with admissible exponent
   \[
   \alpha<\log_{81}\sqrt2\approx0.0788662.
   \]
6. **Adelic natural extension.** The real coding, 2-adic coding, and ordinary-integer obstruction become one diagonal-intersection problem for a hyperbolic S-arithmetic automorphism.
7. **A sharply weakened all-depth lemma.** Only logarithmically many uniformly nondegenerate cosine factors—or logarithmic total squared phase energy—are needed for each polynomially small numerator.

## Block-mean audit

`BLOCK_MEAN_AUDIT.md` records an asymmetric verdict.

- The written issue-#4 Theorem-11 interface says “every full block,” matching the arbitrary-block hypothesis needed by `L-9302`.
- The issue-#4 Theorem-12 subgroup period is correct, but its displayed first-`m+1`-factor proof is not uniform when `3 | theta`. For instance, `theta=81` has an identically zero first reciprocal phase, while `theta=9` gives first-factor mean `|cos(pi/9)|`, larger than the advertised universal contraction.
- This does not by itself refute the full source theorem, because deeper factors may contract. It does require a repaired proof interface. `T-9303` supplies one.

No issue-#4 status is changed by this packet.

## Relation to existing work

- The exact product formula and proposed frequency-block mean are taken branch-qualified from issue #4's `EQ.md`.
- The latest issue-#4 `EQ-INTERCHANGE.md` has independently moved toward room recursions, Cantor classes, and an exact product isomorphism. The stationary-cusp and reciprocal-period packet is complementary: it controls the weighted high tail and the depth-average exceptional set, while the room process remains the all-depth core.
- The literature audit in draft PR #13 correctly warns that fixed real self-similar Fourier-decay theorems do not directly cover the original changing finite-group products. `L-9301` supplies a stationary object, but **does not** by itself verify the hypotheses of any external theorem.
- Draft PR #3's fractional-window law is compatible with the solenoid orbit identity. It is conceptual overlap, not a hidden dependency for `L-9301` or `L-9302`.
- No claim here constructs a positive integer in the survivor attractor, rules one out, or resolves Collatz.

## Main research offense

The all-depth target remains `C-9301`. Prove that for some fixed `A,c,delta>0`, every

\[
1\le|\theta|\le K^A
\]

has at least `c log K` phase positions whose distance from an integer is at least `delta`. This gives polynomial Fourier decay in the low-frequency window still needed by `T-9301`. The more flexible alternative from `L-9303` is a lower bound of order `log K` for total squared phase distance.

The revised density-one theorem suggests an additional offense: characterize depths that are simultaneously exceptional in several adjacent `81`-adic annuli. Such a depth must carry coherent low-energy phase grids after every valuation stratum is removed. A cross-scale inverse theorem for those grids could upgrade density-one EQ toward all-depth EQ.

Three mechanisms are developed in `PROOF_PROGRAM.md`:

1. an inverse theorem turning one exceptional frequency into forbidden block mass;
2. an S-unit/carry height argument for scattered near-degeneracies;
3. a quantitative shrinking-target theorem on the adelic solenoid.

`X-9301` supplies one small exact-arithmetic adversarial probe to choose or refute lemma shapes. Long orbit scans are not part of this program.

## Review order

1. `claims/L-9301-moving-character-identity.md`
2. `claims/L-9304-phase-reciprocity.md`
3. `claims/T-9303-valuation-stratified-depth-mean.md`
4. `claims/L-9302-weighted-shell-tail.md`
5. `claims/T-9301-polynomial-window-reduction.md`
6. `claims/T-9302-density-one-full-eq.md`
7. `BLOCK_MEAN_AUDIT.md`
8. `claims/L-9303-phase-energy-product.md`
9. `claims/D-9302-adelic-natural-extension.md`
10. `claims/C-9301-logarithmic-cusp-scattering.md`
11. `PROOF_PROGRAM.md`
12. `../../experiments/X-9301-cusp-scattering/README.md`

## Acceptance boundary

A successful proof of `C-9301`, together with an independently verified frequency-block mean, would close the EQ discrepancy target for the `64 -> 81` subsystem. It would prove quantitative near-emptiness of finite survivors, **not** nonexistence of an exceptional infinite ordinary integer.

A direct construction of a nontrivial point in the integer section of `D-9302` would instead supply an M1 witness and, after the existing chart translation is independently checked, a candidate divergent Collatz orbit. No such point is presented here.