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

The survivor range `1 <= theta <= 2^K` is therefore an adelic cusp: the same rational character tends to zero in the real absolute value while escaping to infinity in the 2-adic absolute value. This stationary reformulation is exact.

The full-frequency block mean proposed on issue #4 makes the weighted Erdős--Turán tail above `81^M` exponentially small. Consequently, full EQ does **not** require a pointwise estimate for every `theta <= 2^K`; a polynomial-size low-frequency window is sufficient.

A second pass audited the perpendicular depth-average claim. The subgroup period is real, but multiplication by a frequency divisible by `3` collapses initial phase grids. `L-9304` and `T-9303` reconstruct the depth-period estimate from scratch with the exact loss `ceil(v_3(theta)/4)`. Summing those valuation strata proves the complete weighted EQ criterion along density-one depths using only the frequency-block theorem as an external input.

A third pass engages issue #4's newest room/Cantor frontier. The finite Cantor classes `C_j` are reductions of **one fixed Bernoulli self-similar measure on `Z_3`**. Their finite transform is a moving-character coefficient of this measure, and the exact CRT comparison set `R_n x C_j` has Fourier transform

\[
\widehat\mu_2(q_2)\widehat\nu_3(q_3)
\]

along an arithmetic two-place cusp. The varying joint modular products are therefore restrictions of one fixed product measure on `Z_2 x Z_3`.

## Fixed notation

Set

\[
\rho=\frac{64}{81},\qquad d=\frac{17}{81},
\qquad
J_\varepsilon(x)=\rho x+d\varepsilon
\quad(\varepsilon\in\{0,1\}).
\]

For a binary sequence `epsilon`, define the survivor coding

\[
\pi_2(\varepsilon)=
\sum_{t\ge0}d\varepsilon_t\rho^t
\in\mathbb Z_2,
\]

and let `mu` be its fair Bernoulli pushforward.

For the triadic mirror put

\[
\lambda=\frac{81}{64},
\qquad
c=-\frac{17}{64},
\]

and define

\[
\pi_3(\eta)=
\sum_{r\ge0}c\eta_r\lambda^r
\in\mathbb Z_3,
\]

with fair Bernoulli pushforward `nu`.

For the depth-`K` survivor set `R_K`, let

\[
S_K(\theta)=
\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{\theta A}{64^K}\right),
\qquad
F_K(\theta)=\frac{|S_K(\theta)|}{2^K}.
\]

The active EQ target is

\[
E_K=
\sum_{1\le\theta\le2^K}
\frac{F_K(\theta)}\theta
\longrightarrow0.
\]

## Results in this packet

| ID | Status | Content |
|---|---|---|
| `D-9301` | `PROPOSED` | One fixed self-similar survivor measure on `Z_2` |
| `D-9302` | `PROPOSED` | Exact `{2,3,infinity}`-solenoid natural extension and integer section |
| `D-9303` | `PROPOSED` | One fixed self-similar triadic mirror measure whose reductions are the Cantor classes `C_j` |
| `L-9301` | `PROPOSED` | Exact moving-character identity `mu-hat(theta/64^K)=2^{-K}S_K(theta)` |
| `L-9302` | `PROPOSED` | Weighted shell lemma: frequency-block means force an exponentially small high-frequency tail |
| `L-9303` | `PROPOSED` | Squared phase energy gives a deterministic survivor Fourier-product bound |
| `L-9304` | `PROPOSED` | Exact reciprocity between a power-of-64 phase and a power-of-81 residue, including valuation shift |
| `L-9305` | `PROPOSED` | Exact moving-character identity for the triadic Cantor transform |
| `T-9301` | `PROPOSED` | Polynomial-window maximal decay is sufficient for all-depth EQ |
| `T-9302` | `PROPOSED` | Frequency blocks plus `T-9303` imply full EQ along density-one depths |
| `T-9303` | `PROPOSED` | Every complete depth period contracts after losing exactly `ceil(v_3(theta)/4)` phase levels |
| `T-9304` | `PROPOSED` | Exact two-place CRT transform factorization into `mu-hat` and `nu-hat` |
| `C-9301` | `IDEA` | Logarithmic cusp-scattering theorem sufficient for all-depth EQ |
| `Q-9301` | `IDEA` | Nontrivial ordinary-integer intersection in the adelic natural extension |
| `Q-9302` | `IDEA` | Uniform two-place decay along the room-relevant CRT cusp |
| `O-9301` / `X-9301` | `EMPIRICAL` | Exact bounded scattering census through `K=80`, `theta<=K^2` |

`PROPOSED` means that a complete-looking argument is supplied but has not received independent repository review. `T-9301` and `T-9302` remain conditional on the branch-qualified frequency-block theorem. The depth-period component of `T-9302` is proved locally in `T-9303`. The main CRT factorization in `T-9304` is self-contained; only its transfer to actual deeper survivor positions is conditional on issue #4's proposed position-rigidity theorem.

## What is genuinely new here

1. **Survivor stationarization.** The varying finite products are one fixed `Z_2` Fourier transform sampled on a moving rational cusp.
2. **Weighted-shell compression.** Frequency blocks dispose of all but a polynomial-size numerator window.
3. **Exact 2–3 reciprocity.** Each power-of-64 phase equals a reciprocal residue modulo a power of `81` plus a fully explicit error.
4. **Valuation-stratified depth decay.** Divisibility by `81` removes phase levels, but the loss is exact and summable across a growing window.
5. **One-input density-one synthesis.** Conditional only on the frequency-block theorem, the complete EQ weighted sum tends to zero on density-one depths for
   \[
   \alpha<\log_{81}\sqrt2\approx0.0788662.
   \]
6. **Triadic stationarization.** The Cantor classes and their finite product are one fixed `Z_3` self-similar measure and transform.
7. **Two-place factorization.** The exact CRT product of `R_n` and `C_j` is one coefficient of the fixed product measure `mu x nu` at coupled moving local characters.
8. **Adelic natural extension.** The real coding, 2-adic coding, and ordinary-integer obstruction become one diagonal-intersection problem for a hyperbolic S-arithmetic automorphism.
9. **A sharply weakened all-depth lemma.** Only logarithmically many uniformly nondegenerate cosine factors—or logarithmic total squared phase energy—are needed for each polynomially small numerator.

## Block-mean audit

`BLOCK_MEAN_AUDIT.md` records an asymmetric verdict.

- The written issue-#4 Theorem-11 interface says “every full block,” matching the arbitrary-block hypothesis needed by `L-9302`.
- The issue-#4 Theorem-12 subgroup period is correct, but its displayed first-`m+1`-factor proof is not uniform when `3 | theta`. For instance, `theta=81` has an identically zero first reciprocal phase, while `theta=9` gives first-factor mean `|cos(pi/9)|`, larger than the advertised universal contraction.
- This does not by itself refute the full source theorem, because deeper factors may contract. It does require a repaired proof interface. `T-9303` supplies one.

No issue-#4 status is changed by this packet.

## Relation to issue #4's room/Cantor work

The latest `EQ-INTERCHANGE.md` isolates:

- a survivor core `R_n` modulo `64^n`;
- an admissible Cantor class set `C_j` modulo `81^j`;
- an exact CRT product comparison;
- a room displacement controlling the archimedean ordering of the actual deeper set `R_(n+j)`.

This packet supplies the fixed local objects underneath that finite architecture:

\[
2^{-n}S_n(a)=\widehat\mu(a/64^n),
\qquad
2^{-j}\widehat C_j(b)=\widehat\nu(b/81^j).
\]

For the CRT product and the canonical inverse pair

\[
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j},
\]

`T-9304` gives

\[
G_{n,j}(h)
=
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j).
\]

The remaining frontier is no longer “find a stationary model.” It is to control this coupled two-place cusp and then transfer that control through the room-position map without losing the short-interval scale.

## Relation to external literature and other branches

- The exact product formula and proposed frequency-block mean are taken branch-qualified from issue #4's `EQ.md`.
- The literature audit in draft PR #13 correctly warns that fixed real self-similar Fourier-decay theorems do not directly cover the original changing finite-group products. The stationary local measures now exist, but **no external theorem is imported without checking its nonarchimedean and coupled-cusp hypotheses**.
- Draft PR #3's fractional-window law is compatible with the solenoid orbit identity. It is conceptual overlap, not a hidden dependency for the local Fourier identities.
- No claim here constructs a positive integer in the survivor attractor, rules one out, or resolves Collatz.

## Main research offenses

### Offense A — all-depth survivor cusp energy

Prove that for some fixed `A,c,delta>0`, every

\[
1\le|\theta|\le K^A
\]

has at least `c log K` nondegenerate phase positions, or total squared phase energy at least `c log K`. This would close all-depth EQ through `T-9301`.

### Offense B — two-place room-cusp decay

Study the coupled inverse pair

\[
((81^j)^{-1}\bmod64^n,
 (64^n)^{-1}\bmod81^j)
\]

as one orbit in the dual `{2,3}` solenoid. Seek a uniform estimate for

\[
\left|
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j)
\right|
\]

in the room-relevant range, together with a displacement-stable transfer to actual `R_(n+j)` positions.

### Offense C — exceptional-depth inverse theorem

Characterize depths simultaneously exceptional in several adjacent `81`-adic annuli. After valuation strata are removed, such depths must carry coherent low-energy phase grids and room digits across scales. Eliminating that coherence could upgrade density-one EQ toward all-depth EQ.

`X-9301` remains the only computation in this packet. Long scans are not part of the program.

## Review order

1. `claims/L-9301-moving-character-identity.md`
2. `claims/D-9303-stationary-triadic-mirror.md`
3. `claims/L-9305-triadic-moving-character.md`
4. `claims/T-9304-two-place-crt-factorization.md`
5. `claims/L-9304-phase-reciprocity.md`
6. `claims/T-9303-valuation-stratified-depth-mean.md`
7. `claims/T-9302-density-one-full-eq.md`
8. `claims/L-9302-weighted-shell-tail.md`
9. `claims/T-9301-polynomial-window-reduction.md`
10. `BLOCK_MEAN_AUDIT.md`
11. `claims/L-9303-phase-energy-product.md`
12. `claims/D-9302-adelic-natural-extension.md`
13. `claims/C-9301-logarithmic-cusp-scattering.md`
14. `PROOF_PROGRAM.md`
15. `../../experiments/X-9301-cusp-scattering/README.md`

## Acceptance boundary

A successful proof of `C-9301`, together with an independently verified frequency-block mean, would close the EQ discrepancy target for the `64 -> 81` subsystem. It would prove quantitative near-emptiness of finite survivors, **not** nonexistence of an exceptional infinite ordinary integer.

A two-place theorem for `T-9304`'s coupled cusp could instead close the newer room/Cantor formulation or improve the unconditional near-window exponent.

A direct construction of a nontrivial point in the integer section of `D-9302` would supply an M1 witness and, after the existing chart translation is independently checked, a candidate divergent Collatz orbit. No such point is presented here.