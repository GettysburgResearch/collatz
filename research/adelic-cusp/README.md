# Adelic cusp Fourier program

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21  
**Packet status:** theory-first independent attempt; no counterexample claimed

## Thesis

The depth-dependent Fourier products in the active `64 -> 81` survivor program are evaluations of **one fixed Bernoulli self-similar measure on `Z_2`** at the moving characters

\[
q_{K,\theta}=\frac{\theta}{64^K}.
\]

The survivor range is therefore an adelic cusp: the same rational character tends to zero in the real absolute value while escaping in the `2`-adic absolute value. This stationarization is exact.

The frequency-block mean proposed on issue #4 makes the weighted Erdős--Turán tail above `81^M` exponentially small. Hence full EQ does not require a pointwise estimate for every `theta<=2^K`; a polynomial-size low-frequency window is sufficient.

A second pass audited the perpendicular depth-average claim. Multiplication by a frequency divisible by `3` collapses initial phase grids. `L-9304` and `T-9303` reconstruct the depth-period estimate with the exact loss

\[
\left\lceil\frac{v_3(\theta)}4\right\rceil.
\]

Summing the valuation strata proves the complete weighted EQ criterion along density-one depths using only the frequency-block theorem as an external input.

A third pass stationarized issue #4's room/Cantor side. The finite Cantor classes `C_j` are reductions of **one fixed Bernoulli self-similar measure on `Z_3`**, and the exact CRT comparison transform factors through the fixed product measure on

\[
\mathbb Z_2\times\mathbb Z_3.
\]

A fourth pass now closes the apparent split freedom. `L-9307` proves that the dyadic survivor factors and triadic Cantor factors are adjacent portions of **one reciprocal phase chain** attached to the same global rational character. `T-9305` proves that, in every frequency range `H=o(64^K)`, the original EQ sum, its triadic mirror, and every two-place CRT split differ by at most `O(H/64^K)`.

Thus the two-place target is not a weaker theorem. Its remaining value is methodological: signed transfer operators, bilateral inverse theorems, solenoid renewal, or positivity-native room dynamics may still prove the equivalent criterion more effectively.

## Fixed notation

Set

\[
\rho=\frac{64}{81},
\qquad
d=\frac{17}{81},
\qquad
J_\varepsilon(x)=\rho x+d\varepsilon.
\]

For a binary sequence `epsilon`, define

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
| `D-9303` | `PROPOSED` | One fixed self-similar triadic mirror measure whose reductions are `C_j` |
| `L-9301` | `PROPOSED` | `mu-hat(theta/64^K)=2^{-K}S_K(theta)` exactly |
| `L-9302` | `PROPOSED` | Frequency-block means force an exponentially small weighted tail |
| `L-9303` | `PROPOSED` | Squared phase energy controls the survivor product |
| `L-9304` | `PROPOSED` | Exact `64`/`81` phase reciprocity and valuation shift |
| `L-9305` | `PROPOSED` | `nu-hat(h/81^j)=2^{-j}C_j-hat(h)` exactly |
| `L-9306` | `PROPOSED` | Every complete-group absolute Fourier moment factors |
| `L-9307` | `PROPOSED` | One global rational diagonal and one stitched reciprocal phase chain |
| `T-9301` | `PROPOSED` | Polynomial-window maximal decay suffices for all-depth EQ |
| `T-9302` | `PROPOSED` | Frequency blocks plus `T-9303` imply full EQ on density-one depths |
| `T-9303` | `PROPOSED` | Complete depth periods contract after exact `v_3` losses |
| `T-9304` | `PROPOSED` | Exact two-place CRT transform factorization |
| `T-9305` | `PROPOSED` | Every CRT split is weighted-equivalent to the original EQ criterion |
| `C-9301` | `IDEA` | Logarithmic cusp scattering sufficient for all-depth EQ |
| `Q-9301` | `IDEA` | Nontrivial ordinary-integer intersection in the adelic natural extension |
| `Q-9302` | `IDEA` | Can two-place dynamics prove the equivalent criterion by a new mechanism? |
| `O-9301` / `X-9301` | `EMPIRICAL` | Exact bounded scattering census through `K=80`, `theta<=K^2` |

`PROPOSED` means that a complete-looking argument is supplied but has not received independent repository review. `T-9301` and `T-9302` remain conditional on the branch-qualified frequency-block theorem. The depth-period component of `T-9302` is proved locally in `T-9303`.

The main CRT factorization in `T-9304`, the phase stitching in `L-9307`, and the magnitude comparison in `T-9305` are self-contained. Ordered-position consequences remain separate from absolute Fourier equivalence.

## What is genuinely new here

1. **Survivor stationarization.** The varying finite products are one fixed `Z_2` transform sampled on a rational cusp.
2. **Weighted-shell compression.** Frequency blocks remove all but a polynomial-size numerator window.
3. **Exact `2`--`3` reciprocity.** A power-of-`64` phase is a reciprocal residue modulo a power of `81` plus a fully explicit circle shift.
4. **Valuation-stratified depth decay.** Divisibility by `81` removes phase levels, but the loss is exact and summable.
5. **One-input density-one synthesis.** Conditional only on the frequency-block theorem, full weighted EQ holds on density-one depths for
   \[
   \alpha<\log_{81}\sqrt2\approx0.0788662.
   \]
6. **Triadic stationarization.** The Cantor classes are finite quotients of one fixed `Z_3` measure.
7. **Two-place factorization.** The CRT product is one coefficient of `mu x nu`.
8. **Full-group decorrelation.** Every complete-dual absolute moment factors; the obstruction is only the short rational diagonal.
9. **Global rational diagonal.** The CRT inverse pair is simply the two local representation classes of
   \[
   h/(64^n81^j).
   \]
10. **Bilateral phase stitching.** The triadic factor supplies the low indices and the dyadic factor supplies the high indices of one reciprocal chain.
11. **Split collapse.** For `K=n+j`,
   \[
   \left|
   |G_{n,j}(h)|-F_K(h)
   \right|
   <\frac{2\pi|h|}{64^K}.
   \]
   Hence every weighted split target with `H=o(64^K)` is equivalent to the original EQ sum.
12. **Adelic integer section.** The direct M1 problem is a diagonal-intersection question in a hyperbolic S-arithmetic solenoid.

## Block-mean audit

`BLOCK_MEAN_AUDIT.md` records an asymmetric verdict.

- Issue #4's Theorem-11 interface says “every full block,” matching the hypothesis needed by `L-9302`.
- The Theorem-12 subgroup period is correct, but its displayed first-factor proof is not uniform when `3|theta`.
- `T-9303` supplies a self-contained valuation-corrected replacement for the depth-period interface.

No issue-#4 claim status is changed by this packet.

## Relation to issue #4's room walk

The current `EQ-INTERCHANGE.md` identifies:

- a core `R_n` modulo `64^n`;
- Cantor classes `C_j` modulo `81^j`;
- a position-rigid CRT product;
- base-`81` room digits equal to wrap counts of successive `H`-steps;
- an inverse-limit marginal tower that does not close at fixed modulus.

The stationary crosswalk is

\[
2^{-n}S_n(a)=\widehat\mu(a/64^n),
\qquad
2^{-j}\widehat C_j(b)=\widehat\nu(b/81^j).
\]

For

\[
Q=64^n81^j,
\qquad
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j},
\]

`T-9304` gives

\[
G_{n,j}(h)=
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j).
\]

`L-9307` strengthens the interpretation:

\[
\frac{hu}{64^n}
\equiv
\frac hQ
\pmod{\mathbb Z_2},
\qquad
\frac{hv}{81^j}
\equiv
\frac hQ
\pmod{\mathbb Z_3}.
\]

The two factors are therefore local views of one global rational character. Their phases stitch the same chain, and `T-9305` proves

\[
\left|
\sum_{h\le H}\frac{|G_{n,j}(h)|}{h}
-
\sum_{h\le H}\frac{F_K(h)}h
\right|
<
\frac{2\pi H}{64^K}.
\]

The remaining room frontier is no longer “prove a different two-place decay theorem.” It is “use the two-place or room representation to prove the equivalent original criterion by a genuinely new mechanism.”

## Relation to external literature and other branches

- The product formula and frequency-block mean are taken branch-qualified from issue #4.
- Draft PR #13 correctly warns that fixed real self-similar Fourier theorems do not directly cover these nonarchimedean cusp characters.
- The fixed local measures now exist, but no external theorem is imported without checking its precise hypotheses.
- Draft PR #3's fractional-window law is compatible with the solenoid orbit identity, but is not a proof dependency for the local Fourier claims.
- No claim here constructs or rules out a positive integer in the survivor attractor.

## Main research offenses

### Offense A — all-depth cusp energy

Prove that every

\[
1\le|\theta|\le K^A
\]

has logarithmic phase energy. This closes all-depth EQ through `T-9301`.

### Offense B — bilateral low-energy inverse theorem

The split chain is

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}}.
\]

Show that low energy forces one of:

1. exact `64`-power reduction;
2. exact `81`-valuation loss;
3. a bounded-complexity periodic carry template;
4. amplification to a full frequency block forbidden by the frequency-block mean.

### Offense C — signed or positive room transfer

Absolute values collapse to the old target. Retain complex phases across frequencies, or work directly with the positive room-counting recursion. Seek contraction of a signed kernel, relative entropy, or a positivity-native transfer operator on the inverse-limit tower.

### Offense D — exceptional-depth coherence

Characterize depths bad across several adjacent `81`-adic annuli. The valuation-corrected proof forces coherent low-energy grids at such depths; eliminate that coherence to upgrade density-one EQ toward all-depth EQ.

`X-9301` remains the only computation in this packet. Long scans are not part of the program.

## Review order

1. `claims/L-9307-global-rational-phase-stitching.md`
2. `claims/T-9305-split-collapse-weighted-equivalence.md`
3. `claims/L-9301-moving-character-identity.md`
4. `claims/D-9303-stationary-triadic-mirror.md`
5. `claims/L-9305-triadic-moving-character.md`
6. `claims/T-9304-two-place-crt-factorization.md`
7. `claims/L-9306-full-group-moment-factorization.md`
8. `claims/L-9304-phase-reciprocity.md`
9. `claims/T-9303-valuation-stratified-depth-mean.md`
10. `claims/T-9302-density-one-full-eq.md`
11. `claims/L-9302-weighted-shell-tail.md`
12. `claims/T-9301-polynomial-window-reduction.md`
13. `claims/Q-9302-two-place-room-cusp.md`
14. `claims/D-9302-adelic-natural-extension.md`
15. `PROOF_PROGRAM.md`
16. `../../experiments/X-9301-cusp-scattering/README.md`

## Acceptance boundary

A proof of `C-9301`, together with an independently verified frequency-block mean, would close the all-depth EQ discrepancy target. It would prove quantitative near-emptiness of finite survivors, not nonexistence of an exceptional infinite ordinary integer.

A proof using the room or two-place representation automatically proves the same original criterion by `T-9305`; it must not be advertised as an independent weaker target.

A direct nontrivial point in the integer section of `D-9302` would instead supply an M1 witness and, after the existing chart translation is independently checked, a candidate divergent Collatz orbit. No such point is presented here.