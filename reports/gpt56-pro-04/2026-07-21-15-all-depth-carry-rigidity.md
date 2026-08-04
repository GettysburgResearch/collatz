# Agent report — completion-height carry rigidity and all-depth weighted EQ

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21  
**Status:** independent theory packet; every theorem-level claim remains `PROPOSED`

## 1. Starting point

Before this session the branch had established:

1. one stationary survivor measure on `Z_2` and one stationary mirror measure on `Z_3`;
2. exact reciprocal phase stitching across every CRT split;
3. an exact lift-prefix/residue-class bijection;
4. an entropy deficit for low-energy prefixes;
5. a uniform harmonic high-frequency tail at every depth;
6. weighted EQ on natural-density-one depths;
7. upper-Banach-zero exceedance sets at every fixed accuracy.

The remaining all-depth wall was formulated as harmonic location of sparse low-energy residue classes among the smallest frequencies.

The user requested a profound step back, a generalization informed by the literature branch, and a pushed theorem-level advance.

## 2. Literature and cross-branch review

The session reviewed the citation-critical literature branch, especially:

- `LITERATURE.md`;
- `literature/LIVE_REPO_REVIEW_WAVE2.md`;
- `LIT-KTHM-0016` — rational-base address and bounded real tail;
- `LIT-KTHM-0017` — cycle-mean potentials;
- `LIT-KTHM-0026` — finite-state tilted transfer bounds;
- `LIT-KTHM-0027` — graph-directed compact attractors and the ordinary-integer non-application;
- topic notes on conditioned operators, measure rigidity, Mahler/FLP, and S-unit boundaries;
- the branch-qualified issue-#4 claim map.

The review reinforced four constraints:

1. fixed real self-similar Fourier theorems do not directly apply to the moving nonarchimedean cusp;
2. finite-state pressure bounds do not automatically survive the growing inverse-limit tower;
3. completion points are not ordinary integers;
4. generic S-unit language is not a theorem when cofactors vary dynamically.

The useful positive idea was the rational-base/Mahler separation between strong agreement in a completion and controlled ordinary height.

The session also reviewed:

- issue #4's room walk and exact inverse-limit tower obstruction;
- issue #4's older pointwise Fourier wall;
- PR #20's new ordinary-code repetition rigidity and factor-complexity barrier.

PR #20 proved the critical constant

\[
\frac1{\log_{64}81-1}
\approx17.6548475770851
\]

for repeated output factors of an ordinary survivor code.

## 3. Approaches considered

### 3.1 Finite-state pressure on the room tower

The first generalization considered a family of tilted transfer operators on growing `81`-adic marginals. This matched `LIT-KTHM-0026`, but the issue-#4 tower does not close at finite modulus. A proof would need a uniform projective contraction across growing state spaces, with exact control of information imported from the next level.

This remains a viable route for sharper mixing statements but was not the highest-leverage path.

### 3.2 Direct harmonic location of exceptional cylinders

The existing `C-9301` route sought a first-moment bound for least positive representatives of low-energy lift cylinders. `T-9307` gives the correct entropy deficit, but cardinality alone cannot exclude one expensive class near `h=1`.

This route remained plausible but appeared to require new distribution input.

### 3.3 Complexity–energy transference from PR #20

The shared recurrence suggested that low-energy phase paths might force repeated factors in the ordinary survivor code. A direct implication was not immediate: one object is a frequency-phase chain and the other is a digit itinerary of a hypothetical ordinary point.

The comparison nevertheless exposed the key structural clue: both problems have the same criticality ratio between powers of `64` and powers of `81`.

### 3.4 Integral phase carries

The decisive step was to stop reading the lift chain only through its base-`81` digit and instead use signed representatives.

For

\[
s_\ell
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}},
\]

put

\[
x_\ell=s_\ell/81^{\ell+1}.
\]

The adjacent relation gives the exact integer

\[
\boxed{
a_\ell=64x_\ell-81x_{\ell+1}\in\mathbb Z.}
\]

This integer quantization closes the gap that a finite-state pressure proof would have approximated.

## 4. L-9310 — general completion-height carry rigidity

The new lemma is stated for every coprime expanding chart

\[
2\le M<N.
\]

For signed phases

\[
s_\ell
\equiv
-chM^{\ell-K}
\pmod{N^{\ell+1}},
\]

with `gcd(c,M)=1` and primitive `M∤h`, define

\[
x_\ell=s_\ell/N^{\ell+1},
\qquad
a_\ell=Mx_\ell-Nx_{\ell+1}\in\mathbb Z.
\]

### Carry energy

If `W` carries are nonzero, then

\[
W
\le
\sum a_\ell^2
\le
2(M^2+N^2)
\sum x_\ell^2.
\]

Hence every nonzero carry has a quantized energy cost.

### Zero-run height squeeze

If `r` consecutive carries vanish, ending `t` phase levels before the terminal end, then

\[
s_{\ell+r}=M^rs_\ell.
\]

The integer

\[
Z=M^{K-\ell}s_\ell+ch
\]

is divisible by `N^(ell+r+1)`.

It is nonzero: `Z=0` would force `M|h`.

The signed-representative bound gives

\[
N^r
\le
\frac12M^{r+t}+|ch|.
\]

Therefore

\[
r
\le
\kappa_{M,N}t+\log_N(2|ch|),
\]

where

\[
\boxed{
\kappa_{M,N}
=
\frac{\log M}{\log(N/M)}
=
\frac1{\log_MN-1}.}
\]

### Terminal chaining

The carry word has `W+1` zero runs. Reading them from right to left gives a recurrence

\[
t_i
\le
(1+\kappa)t_{i+1}+C_h+1,
\qquad
t_W=1.
\]

Thus

\[
K
\le
B_h(1+\kappa)^{W+1},
\qquad
B_h=1+\frac{1+\log_N(2|ch|)}\kappa.
\]

Consequently,

\[
\boxed{
\sum_{\ell<K}x_\ell^2
\ge
\frac1{2(M^2+N^2)}
\left(
\frac{\log(K/B_h)}{\log(1+\kappa)}-1
\right)_+.}
\]

This is pointwise, deterministic, and uniform in depth.

## 5. Specialization to `64 -> 81`

For

\[
M=64,
\qquad
N=81,
\qquad
c=17,
\]

one obtains

\[
\kappa
=
\frac{\log64}{\log(81/64)}
\approx17.6548475770851,
\]

\[
A=1+\kappa
\approx18.6548475770851,
\]

and

\[
C_*=2(64^2+81^2)=21314.
\]

The same `kappa` as PR #20 is now explained: repetition rigidity and zero-carry rigidity are two instances of one completion-height principle.

Neither theorem depends on the other.

## 6. T-9311 — pointwise cusp decay

The mirror coefficient satisfies

\[
F^{(3)}_K(h)
\le
\exp\!\left(
-2\sum_{\ell<K}x_\ell^2
\right).
\]

For primitive `64∤h`, `L-9310` therefore gives

\[
F^{(3)}_K(h)
\le
\exp\!\left[
-\frac2{21314}
\left(
\frac{\log(K/B(h))}{\log(1+\kappa)}-1
\right)_+
\right].
\]

The original survivor coefficient differs by at most

\[
\pi|h|/64^K.
\]

For a general numerator, write

\[
h=64^v h_0,
\qquad64\nmid h_0,
\]

and use exact self-similarity

\[
F_K(h)=F_{K-v}(h_0).
\]

Define

\[
b_*
=
\frac{2}{21314\log(1+\kappa)}
\approx3.2068228850\times10^{-5}.
\]

Then every fixed polynomial window satisfies

\[
\boxed{
\max_{1\le h\le K^R}F_K(h)
\le
C_R
\left(
\frac{\log K}{K}
\right)^{b_*}.}
\]

More generally, every window `H_K` with

\[
\log(2+H_K)=o(K)
\]

has uniform pointwise decay.

## 7. T-9312 — all-depth weighted EQ

Split

\[
E_K
=
\sum_{1\le h<K}
\frac{F_K(h)}h
+
\sum_{K\le h\le2^K}
\frac{F_K(h)}h.
\]

The pointwise theorem gives

\[
\sum_{h<K}\frac{F_K(h)}h
\le
C(1+\log K)
\left(
\frac{\log K}{K}
\right)^{b_*}
\to0.
\]

The uniform entropy tail `T-9308` gives

\[
\sum_{K\le h\le2^K}
\frac{F_K(h)}h
\le
C_{\rm tail}K^{-\delta}
+
\pi2^{-5K}
\to0.
\]

Therefore

\[
\boxed{E_K\to0}
\]

for every depth.

## 8. Why this is a profound generalization

The result does more than solve one exceptional-frequency estimate.

1. It identifies an integer-valued cocycle hidden in the reciprocal phase dynamics.
2. It proves a generic `M -> N` theorem independent of the binary mask.
3. It unifies Fourier phase rigidity with ordinary-code repetition rigidity.
4. It bypasses the non-closing inverse-limit tower without denying that the tower exists.
5. It replaces an average or entropy statement by deterministic pointwise energy.
6. It separates the finite-depth EQ problem from the genuinely harder ordinary-integer realization problem.

The literature-guided pressure, renewal, and self-similar viewpoints remain useful, but the successful proof is exact arithmetic rather than an imported black box.

## 9. Verification performed

The proof-level chain uses no computation.

During development, exact modular checks were performed over bounded depths and numerators to test:

- carry integrality;
- the zero-run divisibility modulus;
- the inequality
  \[
  2N^r\le M^{r+t}+2|ch|;
  \]
- the terminal chaining bound;
- the energy lower bound.

No failures were found. These checks are adversarial validation only and are not premises of any theorem.

Numerical constants were independently recalculated:

```text
kappa = 17.654847577085153
1+kappa = 18.654847577085153
C_* = 21314
b_* = 0.00003206822885025317
```

## 10. Candidate counterexamples

None.

No positive ordinary survivor, nontrivial cycle, divergent ordinary Collatz trajectory, or `K-####` object is claimed.

## 11. Failed or superseded approaches

1. **Finite-state tower pressure as the primary closure.** Not needed for weighted EQ; the integral carry gap is stronger and truncation-free.
2. **Harmonic location of sparse cylinders.** Superseded by pointwise decay.
3. **Exact-prefix Euclidean amplification.** Already refuted by `R-9301`.
4. **External real self-similar Fourier decay.** Still a non-application.
5. **Generic S-unit finiteness.** Not invoked; the proof uses one explicit integer height squeeze.
6. **Density-one convergence as the final theorem.** Strictly strengthened to all depths.

## 12. Potential errors and review requests

Review in this order:

1. In `L-9310`, check that a zero run through level `ell+r` makes
   \[
   M^{K-\ell}s_\ell+ch
   \]
   divisible by `N^(ell+r+1)`.
2. Check that the primitive condition `M∤h` rules out a zero numerator.
3. Check the signed-representative size bound before division by `N^(ell+1)`.
4. Check the right-to-left zero-run recurrence and endpoint `t_W=1`.
5. Check the carry-energy constant `2(M^2+N^2)`.
6. In `T-9311`, check exact `64`-power self-similarity and uniformity of the reduced depth.
7. Reconstruct `T-9307` and `T-9308`, including their arbitrary-interval covering.
8. Check the low/high split in `T-9312`.

## 13. Files changed in this session

New:

- `research/adelic-cusp/claims/L-9310-completion-height-carry-rigidity.md`
- `research/adelic-cusp/claims/T-9311-uniform-subexponential-cusp-decay.md`
- `research/adelic-cusp/claims/T-9312-all-depth-weighted-eq.md`
- this report

Updated:

- `research/adelic-cusp/claims/C-9301-logarithmic-cusp-scattering.md`
- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/README.md`
- `research/adelic-cusp/PROOF_PROGRAM.md`
- draft PR #16 metadata and cross-branch handoff comments

## 14. Claims affected

Added:

- `L-9310` — `PROPOSED`
- `T-9311` — `PROPOSED`
- `T-9312` — `PROPOSED`

Superseded:

- `C-9301`

Strengthened but retained:

- `T-9309`
- `T-9310`

No claim in issue #4, PR #13, or PR #20 is promoted or weakened.

## 15. Next research frontier

The full weighted EQ wall is proposed closed. The direct ordinary-section problem remains.

The best next theorem is a **complexity–carry incompatibility** for a hypothetical ordinary survivor. It should combine:

1. PR #20's mandatory factor-complexity slope;
2. `L-9310`'s completion-height carry criticality;
3. `D-9302`'s bounded real tail and integer section;
4. issue #4's exact chart congruences and room-wrap coding.

The target is to prove that no one infinite binary itinerary can simultaneously:

- inject the required amount of fresh symbolic information;
- keep every shifted `2`-adic sum integral;
- obey the chart congruences;
- and remain compatible with the bounded real companion coordinate.

That is now the packet's most direct path toward M1.