# Adelic cusp Fourier program

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21  
**Packet status:** theory-first independent attempt; no counterexample claimed

## Thesis

The depth-dependent Fourier products in the active `64 -> 81` survivor program are evaluations of **one fixed Bernoulli self-similar measure on `Z_2`** at moving rational characters. The issue-#4 Cantor-class products are likewise evaluations of **one fixed Bernoulli self-similar measure on `Z_3`**.

The two local systems are not independent on the room-relevant CRT orbit. They are local components of one rational character

\[
r=\frac h{64^n81^j},
\]

and their factors stitch one reciprocal phase chain. Consequently, every CRT split is asymptotically equivalent to the original EQ coefficient—both in absolute value and against arbitrary bounded harmonic tests—in every range `H=o(64^K)`.

Thus the multi-place formulation does not define a weaker target. Its value is methodological: the hyperbolic, room, or inverse-limit representation may make the **same carry chain** easier to control.

## Fixed measures

Set

\[
\rho=\frac{64}{81},
\qquad
d=\frac{17}{81}.
\]

For `epsilon in {0,1}^N`, define

\[
\pi_2(\varepsilon)=
\sum_{t\ge0}d\varepsilon_t\rho^t
\in\mathbb Z_2,
\]

and let `mu` be the fair Bernoulli pushforward.

For the triadic mirror set

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

For the depth-`K` survivor set `R_K`, put

\[
S_K(\theta)=
\sum_{A\in R_K}
\exp\!\left(2\pi i\frac{\theta A}{64^K}\right),
\qquad
F_K(\theta)=\frac{|S_K(\theta)|}{2^K}.
\]

The all-depth EQ target is

\[
E_K=
\sum_{1\le\theta\le2^K}
\frac{F_K(\theta)}\theta
\longrightarrow0.
\]

## Claim map

| ID | Status | Content |
|---|---|---|
| `D-9301` | `PROPOSED` | Fixed self-similar survivor measure on `Z_2` |
| `D-9302` | `PROPOSED` | `{2,3,infinity}`-solenoid natural extension and integer section |
| `D-9303` | `PROPOSED` | Fixed triadic mirror measure whose reductions are `C_j` |
| `L-9301` | `PROPOSED` | `mu-hat(theta/64^K)=2^{-K}S_K(theta)` |
| `L-9302` | `PROPOSED` | Frequency-block means force an exponentially small harmonic tail |
| `L-9303` | `PROPOSED` | Squared phase energy controls `F_K` |
| `L-9304` | `PROPOSED` | Exact `64`/`81` phase reciprocity and valuation loss |
| `L-9305` | `PROPOSED` | `nu-hat(h/81^j)=2^{-j}C_j-hat(h)` |
| `L-9306` | `PROPOSED` | Full-group absolute Fourier moments factor exactly |
| `L-9307` | `PROPOSED` | Global rational diagonal and absolute bilateral phase stitching |
| `L-9308` | `PROPOSED` | Complex bilateral phase stitching |
| `T-9301` | `PROPOSED` | Polynomial-window maximal decay suffices for all-depth EQ |
| `T-9302` | `PROPOSED` | Full weighted EQ on density-one depths, conditional only on frequency blocks |
| `T-9303` | `PROPOSED` | Valuation-stratified complete depth-period decay |
| `T-9304` | `PROPOSED` | Exact two-place CRT transform factorization |
| `T-9305` | `PROPOSED` | Absolute split collapse and weighted criterion equivalence |
| `T-9306` | `PROPOSED` | Complex coefficient and bounded test-sequence equivalence |
| `C-9301` | `IDEA` | Logarithmic phase-energy/scattering theorem |
| `Q-9301` | `IDEA` | Nontrivial integer-section intersection |
| `Q-9302` | `IDEA` | Can the equivalent two-place representation yield a better proof mechanism? |
| `O-9301` / `X-9301` | `EMPIRICAL` | Bounded exact scattering census through `K=80`, `theta<=K^2` |

All proof-looking claims remain `PROPOSED` pending independent review. No native issue-#4 status is changed.

## Principal exact results

### Stationary survivor identity

\[
\widehat\mu(\theta/64^K)=2^{-K}S_K(\theta).
\]

The changing finite modular products are one fixed transform sampled along a cusp.

### Weighted-shell compression

Under the issue-#4 arbitrary-full-block frequency mean, the weighted tail above `81^M` is `O(a^M)`. Hence all-depth EQ follows from polynomial decay in any fixed positive polynomial numerator window.

### Valuation-corrected depth averaging

For

\[
P_m=9\cdot81^m,
\qquad
e(\theta)=\left\lceil\frac{v_3(\theta)}4\right\rceil,
\]

every complete depth period satisfies

\[
\frac1{P_m}
\sum_{K\in J}F_K(\theta)
\le
2^{-\frac12\max\{0,m+1-e(\theta)\}}
+
\frac{\pi\theta}{64^{K_0}}.
\]

Summing the valuation strata gives density-one full EQ for every

\[
\alpha<\log_{81}\sqrt2
\approx0.0788662,
\]

conditional only on the frequency-block theorem.

### Fixed triadic mirror

The admissible classes `C_j` are reductions of `nu`, and

\[
\widehat\nu(h/81^j)=2^{-j}\widehat C_j(h).
\]

### Exact CRT product

For

\[
Q=64^n81^j,
\qquad
u=(81^j)^{-1}\pmod{64^n},
\qquad
v=(64^n)^{-1}\pmod{81^j},
\]

the normalized CRT coefficient is

\[
G_{n,j}(h)=
\widehat\mu(hu/64^n)
\widehat\nu(hv/81^j).
\]

Every complete-dual absolute moment factors. In particular,

\[
\frac1Q
\sum_{h\bmod Q}|G_{n,j}(h)|^2
=
2^{-(n+j)}.
\]

### One global rational diagonal

The local characters satisfy

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

They are not arbitrary coupled frequencies; they are the two local classes of one rational.

### Bilateral phase stitching

For `K=n+j`, define

\[
M_\ell=64^{K-\ell},
\qquad
N_\ell=81^{\ell+1},
\]

\[
q_\ell(h)
\equiv
-17hM_\ell^{-1}
\pmod{N_\ell},
\qquad
\delta_\ell(h)=
\frac{17h}{M_\ell N_\ell}.
\]

The triadic product uses the unshifted phases for all `ell`; the dyadic product uses the shifted phases for all `ell`; a CRT split uses unshifted phases for `ell<j` and shifted phases for `ell>=j`.

This holds for the full complex Bernoulli masks, not only their moduli.

### Split collapse

For every split,

\[
\left|
G_{n,j}(h)
-
\widehat\mu(h/64^K)
\right|
<
\frac{2\pi|h|}{64^K}.
\]

For arbitrary complex tests `a_h`,

\[
\left|
\sum_{h\le H}
a_h
\left(
G_{n,j}(h)-
\widehat\mu(h/64^K)
\right)
\right|
\]

is bounded by an explicit split-uniform constant times

\[
\sum_{h\le H}|a_h|h.
\]

In particular, for `a_h=w_h/h`, `|w_h|<=1`,

\[
\left|
\sum_{h\le H}
\frac{w_h}{h}G_{n,j}(h)
-
\sum_{h\le H}
\frac{w_h}{h}
\widehat\mu(h/64^K)
\right|
<
\frac{2\pi H}{64^K}.
\]

At the EQ cutoff `H=2^K`, this error is below

\[
2\pi2^{-5K}.
\]

## Relation to issue #4's room tower

The current room program proves that base-`81` room digits are wrap counts of successive `H`-steps and that finite marginals form an inverse-limit tower: modulus `81^m` is driven by information at modulus `81^(m+1)`.

The stationarization identifies the fixed local measures under that tower. The split-collapse theorems then show:

- the room/Cantor absolute target is exactly the old EQ target asymptotically;
- the same is true for every bounded signed harmonic test;
- a new proof must exploit a nonlinear positive operator, a carry inverse theorem, or hyperbolic renewal—not merely multiply two local coefficients.

Ordered-position rigidity remains useful for geometric and recursive counting statements. It is not needed for the direct coefficient comparisons above.

## Research offenses

### A. Carry-template inverse theorem

For

\[
y_\ell=rac{q_\ell}{81^{\ell+1}},
\]

the lift recurrence is

\[
y_{\ell+1}
=
\frac{\{64y_\ell\}+j_\ell}{81},
\qquad
j_\ell\in\{0,\ldots,80\}.
\]

Prove that a polynomial-height low-energy path has bounded-complexity lift digits and must:

1. reduce by an exact power of `64` or `81`;
2. belong to an arithmetically impossible template; or
3. persist on enough nearby frequencies to contradict the arbitrary-block mean.

### B. Positive room-tower operator

Write the exact inverse-limit kernel and prove contraction of interval mass, relative entropy, or room imbalance after a full period-9 twist, while controlling information imported from the next tower level.

### C. Hyperbolic rational-diagonal renewal

Use the solenoid action of `81/64` to prove logarithmic mask energy for every low-height rational character. Generic mixing is not enough; constants must be uniform in rational height.

### D. Exceptional-depth coherence

A depth exceptional across adjacent `81`-adic scales must defeat the valuation-period mean, the frequency-block tail, and the room marginal contraction simultaneously. Expose the resulting coherent carry word and eliminate it.

### E. Direct M1 intersection

Determine whether the symbolic stable leaf meets the ordinary-integer section outside `0` and `1`. EQ does not settle this question.

## Computation boundary

`X-9301` is the only computation in this packet. It uses exact modular arithmetic through `K=80`, `theta<=K^2` to falsify lemma shapes. The next permissible extension is to emit lift-digit paths for existing argmins; increasing the depth bound alone is not progress.

## Review order

1. `claims/L-9307-global-rational-phase-stitching.md`
2. `claims/T-9305-split-collapse-weighted-equivalence.md`
3. `claims/L-9308-complex-bilateral-stitching.md`
4. `claims/T-9306-complex-test-sequence-equivalence.md`
5. `claims/L-9301-moving-character-identity.md`
6. `claims/D-9303-stationary-triadic-mirror.md`
7. `claims/L-9305-triadic-moving-character.md`
8. `claims/T-9304-two-place-crt-factorization.md`
9. `claims/L-9306-full-group-moment-factorization.md`
10. `claims/L-9304-phase-reciprocity.md`
11. `claims/T-9303-valuation-stratified-depth-mean.md`
12. `claims/T-9302-density-one-full-eq.md`
13. `claims/L-9302-weighted-shell-tail.md`
14. `claims/T-9301-polynomial-window-reduction.md`
15. `claims/Q-9302-two-place-room-cusp.md`
16. `claims/D-9302-adelic-natural-extension.md`
17. `PROOF_PROGRAM.md`
18. `../../experiments/X-9301-cusp-scattering/README.md`

## Acceptance boundary

A proof of `C-9301`, together with an independently verified frequency-block mean, would close all-depth EQ and prove quantitative near-emptiness of finite survivors. It would not exclude one exceptional infinite ordinary integer.

A two-place or room proof automatically proves the same original criterion by `T-9305` and `T-9306`; it must not be presented as a separate weaker target.

A nontrivial point in the integer section of `D-9302` would instead supply an M1 witness and, after the chart translation is independently checked, a candidate divergent Collatz orbit. No such point is presented here.