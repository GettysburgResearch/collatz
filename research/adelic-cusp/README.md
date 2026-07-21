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

The packet then extracts a second exact fact. The full-frequency block-mean estimate proposed in the issue-#4 EQ program already makes the weighted Erdős--Turán tail above `81^M` exponentially small. Consequently, full EQ does **not** require a pointwise estimate for every `theta <= 2^K`. It is enough to control a polynomial-size low-frequency window.

Finally, combining the two perpendicular block-mean inputs proposed in issue #4 gives a conditional theorem stronger than the fixed-frequency statement recorded there: the complete EQ weighted sum tends to zero along a natural-density-one set of depths.

## Fixed notation

Set

\[
\rho=\frac{64}{81},\qquad d=\frac{17}{81},\qquad
J_\varepsilon(x)=\rho x+d\varepsilon
\quad(\varepsilon\in\{0,1\}).
\]

For a binary sequence `epsilon=(epsilon_0,epsilon_1,...)`, define

\[
\pi_2(\varepsilon)=\sum_{t\ge0}d\varepsilon_t\rho^t\in\mathbb Z_2.
\]

Let `mu` be the pushforward of fair Bernoulli measure under `pi_2`. For the depth-`K` coded residue set `R_K`, let

\[
S_K(\theta)=\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{\theta A}{64^K}\right),
\qquad
F_K(\theta)=\frac{|S_K(\theta)|}{2^K}.
\]

The active EQ target is the decay of

\[
E_K=\sum_{1\le\theta\le2^K}\frac{F_K(\theta)}{\theta}.
\]

## Results in this packet

| ID | Status | Content |
|---|---|---|
| `D-9301` | `PROPOSED` | One fixed self-similar survivor measure on `Z_2` |
| `L-9301` | `PROPOSED` | Exact moving-character identity `mu-hat(theta/64^K)=2^{-K}S_K(theta)` |
| `L-9302` | `PROPOSED` | Weighted shell lemma: block means force an exponentially small high-frequency tail |
| `T-9301` | `PROPOSED` | Polynomial-window maximal decay is sufficient for full EQ |
| `T-9302` | `PROPOSED` | The two issue-#4 block means imply full EQ along density-one depths |
| `D-9302` | `PROPOSED` | Exact `{2,3,infinity}`-solenoid natural extension and integer section |
| `C-9301` | `IDEA` | Logarithmic cusp-scattering theorem sufficient for all-depth EQ |

`PROPOSED` means that a complete-looking argument is supplied here but has not received independent repository review. `T-9302` is explicitly conditional on the branch-qualified issue-#4 block-mean claims; this packet does not promote those inputs.

## What is genuinely new here

1. **Stationarization.** The varying finite products are a single fixed `Z_2` Fourier transform sampled on a moving rational cusp.
2. **Weighted-shell compression.** Existing block averages dispose of all but a polynomial-size numerator window.
3. **Two-axis synthesis.** Frequency averaging plus depth averaging yields the full weighted EQ target on density-one depths.
4. **Adelic natural extension.** The real coding, 2-adic coding, and ordinary-integer obstruction become one diagonal-intersection problem for a hyperbolic S-arithmetic automorphism.
5. **A sharply weakened flagship lemma.** Only logarithmically many uniformly nondegenerate cosine factors are needed for each polynomially small numerator.

## Relation to existing work

- The exact product formula and the two proposed block-mean estimates are taken branch-qualified from issue #4's `EQ.md`.
- The literature audit in draft PR #13 correctly warns that fixed real self-similar Fourier-decay theorems do not directly cover the changing finite-group products. `L-9301` supplies a stationary object, but **does not** by itself verify the hypotheses of any external theorem.
- Draft PR #3's fractional-window law is compatible with the solenoid orbit identity. It is conceptual overlap, not a hidden dependency for `L-9301` or `L-9302`.
- No claim here constructs a positive integer in the survivor attractor, rules one out, or resolves Collatz.

## Main research offense

The first target is `C-9301`. Prove that for some fixed `A,c,delta>0`, every

\[
1\le |\theta|\le K^A
\]

has at least `c log K` phase positions whose distance from an integer is at least `delta`. This gives polynomial Fourier decay in the only low-frequency window still needed by `T-9301`.

Three possible proof mechanisms are developed in `PROOF_PROGRAM.md`:

1. an inverse theorem turning one exceptional frequency into forbidden block mass;
2. an S-unit/carry height argument for scattered near-degeneracies;
3. a quantitative shrinking-target theorem on the adelic solenoid.

Computation, if used at all, should be a small exact-arithmetic adversarial probe to choose or refute constants. Long orbit scans are not part of this program.

## Review order

1. `claims/L-9301-moving-character-identity.md`
2. `claims/L-9302-weighted-shell-tail.md`
3. `claims/T-9301-polynomial-window-reduction.md`
4. `claims/T-9302-density-one-full-eq.md`
5. `claims/D-9302-adelic-natural-extension.md`
6. `claims/C-9301-logarithmic-cusp-scattering.md`
7. `PROOF_PROGRAM.md`

## Acceptance boundary

A successful proof of `C-9301`, together with independently verified versions of the frequency block mean used by `T-9301`, would close the EQ discrepancy target for the `64 -> 81` subsystem. It would prove quantitative near-emptiness of finite survivors, **not** nonexistence of an exceptional infinite ordinary integer.

A direct construction of a nontrivial point in the integer section of `D-9302` would instead supply an M1 witness and, after the existing chart translation is independently checked, a candidate divergent Collatz orbit. No such point is presented here.
