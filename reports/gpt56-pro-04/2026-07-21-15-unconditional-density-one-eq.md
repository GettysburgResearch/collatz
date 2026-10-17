# Agent report — prefix entropy, uniform harmonic tail, and unconditional density-one EQ

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Starting hypothesis

The preceding session proved that every dyadic/triadic CRT split is merely a different cut of one reciprocal phase chain. The leading all-depth strategy was then an exceptional-frequency amplification lemma: one low-energy frequency should force too much nearby block mass.

The starting hypothesis for this session was that exact carry prefixes might provide that local persistence. The exact analysis refuted the naive interval version but exposed something stronger: lift prefixes are a base-`81` bijection, so low-energy prefixes admit a uniform entropy estimate. That estimate closes the high-frequency tail without any branch-qualified block theorem and, combined with the valuation-period theorem, yields unconditional density-one full EQ.

## Approaches attempted

1. Derived the exact lift-digit recurrence for reciprocal residues.
2. Reconstructed a frequency from its terminal lifted residue.
3. Proved the full lift-prefix/residue-class bijection modulo `81^L`.
4. Tested the proposed consecutive-neighborhood amplification and found it structurally impossible for exact prefixes.
5. Replaced exact-prefix persistence by an approximate-cylinder counting problem.
6. Built a uniform exponential moment for the prefix quadratic energy using shifted `81`-point grids.
7. Converted the moment bound into an explicit low-energy entropy deficit.
8. Converted exceptional counts and nonexceptional coefficient decay into a dyadic-shell harmonic-tail theorem.
9. Combined the uniform tail with `T-9303`'s depth-period estimate to remove the final external average hypothesis from density-one EQ.
10. Reorganized the claim ledger, README, and proof program around the new theorem chain.
11. Replayed the entropy count independently on complete residue systems at the first nontrivial depths; the finite counts were well below the proved envelope. These checks are not proof dependencies.

## New results

### L-9309 — lift-digit cylinder bijection (`PROPOSED`)

For fixed depth `K`, define

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}},
\qquad
0\le q_\ell<81^{\ell+1}.
\]

The lift digit

\[
d_\ell(h)
=
\left\lfloor
\frac{q_{\ell+1}(h)}{81^{\ell+1}}
\right\rfloor
\in\{0,\ldots,80\}
\]

satisfies

\[
q_{\ell+1}
=
(64q_\ell\bmod81^{\ell+1})
+d_\ell81^{\ell+1}.
\]

The map

\[
h\pmod{81^K}
\longmapsto
(q_0,d_0,\ldots,d_{K-2})
\]

is a bijection onto `(Z/81Z)^K`. Every length-`L` prefix is exactly one residue class modulo `81^L`.

This gives an exact, finite state model for the phase chain and explains the complete-block uniformity underlying issue #4's Markov decomposition.

### R-9301 — exact-prefix interval amplification refuted (`PROPOSED`)

One exact length-`L` carry prefix is the arithmetic progression

\[
h\equiv h_0\pmod{81^L}.
\]

No two consecutive integers share a nonempty exact prefix, and every interval shorter than `81^L` contains at most one representative.

This refutes only the naive proposal that one exact prefix persists on a consecutive Euclidean neighborhood. Approximate-cylinder unions and arithmetic-progression transference remain alive.

### T-9307 — low-energy prefix entropy (`PROPOSED`)

Define

\[
\mathcal E_{K,L}(h)
=
\sum_{\ell<L}
\left\|
\frac{q_\ell(h)}{81^{\ell+1}}
\right\|^2.
\]

Put

\[
\beta=rac{17\sqrt2}{27}<1,
\qquad
\eta=-\log_{81}\beta>0.
\]

Every interval of `81^L` consecutive frequencies contains at most

\[
81^L\beta^L
\]

frequencies satisfying

\[
\mathcal E_{K,L}(h)
\le L/64.
\]

Every arbitrary interval of length `H`, with `L=floor(log_81 H)`, contains only

\[
O(H^{1-\eta})
\]

such frequencies.

Outside that exceptional set, the triadic mirror coefficient satisfies

\[
|\widehat\nu(h/81^K)|
\le
\exp(-L/32),
\]

a fixed power saving in `H`.

The one-level input is elementary. At least `40` of the `81` points in every shifted grid have circle distance at least `1/4`. Choosing the exponential-moment parameter `s=16 log 4` gives one-level contraction `17/27`, and Markov's inequality yields `beta^L`.

### T-9308 — unconditional uniform harmonic tail (`PROPOSED`)

Let

\[
\gamma=rac1{32\log81},
\qquad
\delta=\min\{\eta,\gamma\}>0.
\]

On every dyadic frequency shell `[X,2X)`:

- exceptional frequencies contribute `O(X^-eta)` after harmonic weighting;
- nonexceptional frequencies contribute `O(X^-gamma)`.

Summing shells gives, uniformly for every depth and cutoff `81<=M<=2^K`,

\[
\sum_{M\le h\le2^K}
\frac{F_K(h)}h
\le
C_{\rm tail}M^{-\delta}
+
\pi2^{-5K}.
\]

This removes the exponential frequency range without the branch-qualified frequency-block theorem.

The all-depth EQ criterion now reduces self-containedly to the weighted mass below any growing cutoff:

\[
E_K
\le
\sum_{h<M_K}
\frac{F_K(h)}h
+
C_{\rm tail}M_K^{-\delta}
+
\pi2^{-5K}.
\]

### T-9309 — unconditional density-one full EQ (`PROPOSED`)

Choose

\[
H_m=81^{\alpha m},
\qquad
0<\alpha<\log_{81}\sqrt2.
\]

`T-9303` and valuation-stratum summation show that, in each depth annulus `[P_m,P_(m+1))`, all but an exponentially small fraction of depths have low-frequency mass

\[
O\!\left(
81^{-\frac12(\log_{81}\sqrt2-\alpha)m}
\right).
\]

`T-9308` removes the rest of the frequency range uniformly with contribution

\[
O(81^{-\alpha\delta m}).
\]

Therefore

\[
\boxed{
E_K\to0
\quad\text{along a natural-density-one set of depths.}
}
\]

This theorem has no branch-qualified mathematical input. It is the strongest integrated result of the packet.

## Superseded claims

### T-9301

The earlier conditional polynomial-window reduction is superseded by `T-9308`, which gives the high-frequency tail and low/high reduction without a frequency-block hypothesis.

### T-9302

The earlier conditional density-one theorem is superseded by `T-9309`, which replaces its last external input with `T-9308`.

Both are `SUPERSEDED`, not `REFUTED`; their historical full proofs remain in Git history.

## Candidate counterexamples

None.

No positive ordinary survivor, nontrivial cycle, divergent ordinary Collatz trajectory, or `K-####` object is claimed.

The direct candidate format remains the integer-section intersection in `D-9302`. The density-one theorem does not decide that exceptional existence question.

## Failed approaches and negative findings

1. **Exact-prefix consecutive amplification.** Refuted by `L-9309`/`R-9301`.
2. **Frequency-block theorem as necessary high-tail input.** Superseded; `T-9308` is self-contained.
3. **Counting exceptional prefixes as sufficient for all-depth EQ.** Rejected. A power-small set can still concentrate at harmonically expensive small integers.
4. **Density-one EQ as a solution of M1.** Explicitly rejected. The exceptional depth set may be infinite, and finite-set equidistribution does not rule out one infinite ordinary point.
5. **Optimizing constants as the central task.** Rejected. The structural gap is harmonic location of exceptional cylinders, not the small numerical value of `delta`.

## Potential errors and review requests

Review in this order:

1. `L-9309`: terminal inversion and prefix/residue bijection.
2. `T-9307`: shifted-grid `41/40` count, conditional expectation, and Markov direction.
3. `T-9308`: arbitrary-interval application, largest-shell condition `L<=K`, and shell summation.
4. `T-9303`: subgroup filtration and valuation loss.
5. `T-9309`: valuation-stratum summation, Markov fraction, and natural-density count.

Specific checks:

- verify
  \[
  \beta=(17/27)e^{(16\log4)/64}=17\sqrt2/27<1;
  \]
- check that an open semicircle contains at most `41` points of a shifted `81`-grid;
- check the arbitrary-interval covering constant in `T-9307`;
- check that `floor(log_81 X)<K` throughout the EQ range `X<=2^K`;
- check the survivor/mirror harmonic transfer error `pi*2^K/64^K=pi*2^-5K`;
- confirm that no theorem silently promotes density-one convergence to all-depth convergence.

## Verification performed

- Every proof-level statement is exact finite combinatorics, modular lifting, elementary exponential moments, or geometric/harmonic summation.
- Independent small-depth checks counted the exact low-energy residues for complete blocks at `L=1,2,3`; the observed exceptional fractions were approximately `0.259`, `0.099`, and `0.043`, all far below the proved envelopes `beta^L`.
- These checks use floating-point evaluation only as adversarial validation of the finite inequality; no computation is a mathematical dependency.
- No large search, random sampling, external solver, or imported harmonic-analysis theorem is used.
- The existing exact modular experiment `X-9301` remains unchanged and is not a premise of `T-9307`--`T-9309`.

## Files changed

New:

- `research/adelic-cusp/claims/L-9309-lift-digit-cylinder-bijection.md`
- `research/adelic-cusp/claims/R-9301-exact-prefix-interval-amplification.md`
- `research/adelic-cusp/claims/T-9307-low-energy-prefix-entropy.md`
- `research/adelic-cusp/claims/T-9308-uniform-harmonic-tail.md`
- `research/adelic-cusp/claims/T-9309-unconditional-density-one-eq.md`
- this report

Updated:

- `research/adelic-cusp/claims/T-9301-polynomial-window-reduction.md`
- `research/adelic-cusp/claims/T-9302-density-one-full-eq.md`
- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/README.md`
- `research/adelic-cusp/PROOF_PROGRAM.md`
- draft PR #16 metadata
- issue #15 and issue #4 handoff comments

## Claims affected

Added:

- `L-9309` — `PROPOSED`
- `T-9307`, `T-9308`, `T-9309` — `PROPOSED`
- `R-9301` — `PROPOSED`

Superseded:

- `T-9301`
- `T-9302`

No issue-#4 claim status is changed.

## Recommended next actions

1. Independently reconstruct the five-step chain `L-9309 -> T-9307 -> T-9308 -> T-9303 -> T-9309`.
2. Define the exceptional set in `[1,H]` and attack its **harmonic location**, not merely its cardinality.
3. Use the terminal congruence
   \[
   h\equiv-17^{-1}64^{K-L+1}q_{L-1}\pmod{81^L}
   \]
   to study least positive representatives of low-energy terminal residues.
4. Stratify by `v_3(h)`, first nondegenerate level, and carry template.
5. Compare the resulting exceptional classes with the positive room-tower dynamics.
6. Preserve the direct M1 integer-section route in parallel.

## Organizational improvement ideas

1. Promote theorem chains, not isolated headlines: the five load-bearing files should be reviewed as one dependency path.
2. Mark stronger replacement theorems as `SUPERSEDED` rather than leaving stale conditional claims active.
3. Distinguish exceptional-set **count**, **harmonic mass**, and **pointwise maximum**; they solve different interfaces.
4. Require all “almost every” statements to name the averaging variable and to state whether the exceptional set can be infinite.
5. Record methodological refutations such as `R-9301` without overinterpreting them as evidence about Collatz.