# Agent report — adelic cusp Fourier program

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-21

## Starting hypothesis

The issue-#4 EQ frontier looked artificially nonstationary: a new finite measure and modulus appeared at every depth, while the literature audit correctly warned that fixed real self-similar Fourier theorems did not apply to that triangular array. The starting hypothesis was that the whole array might be the restriction of one fixed object on a completion or solenoid, and that the harmonic weight in the EQ discrepancy sum might make most of the exponential frequency range irrelevant.

## Approaches attempted

1. Read the repository operating constitution and mapped the active draft branches, issues, claim ledgers, latest reports, and negative results.
2. Read the literature-audit branch, especially the non-application audit for real self-similar Fourier decay, measure rigidity, and Mahler analogies.
3. Reconstructed the `64 -> 81` coding as one infinite Bernoulli series in `Z_2`.
4. Evaluated its fixed Fourier transform at the rational characters `theta/64^K` and matched the result exactly to the finite products in issue #4.
5. Treated the proposed frequency-block mean as an abstract hypothesis and derived a weighted shell estimate.
6. Combined the proposed frequency-block and depth-block means to derive full weighted EQ along density-one depths.
7. Built a `{2,3,infinity}` S-arithmetic natural extension joining the real and 2-adic codings and isolated the ordinary-integer section.
8. Replaced a brittle fixed-threshold target by a quadratic phase-energy formulation.
9. Ran one limited exact modular probe through `K=80`, `theta<=K^2` to test whether the proposed scattering shape failed immediately.

## New results

### D-9301 — stationary survivor measure (`PROPOSED`)

The survivor attractor is the image of one continuous injective coding

\[
\pi_2(\varepsilon)
=\sum_{t\ge0}\frac{17\varepsilon_t64^t}{81^{t+1}}
\]

and carries one fixed fair Bernoulli self-similar measure `mu`.

### L-9301 — moving-character identity (`PROPOSED`)

For every integer `theta` and depth `K`,

\[
\widehat\mu(\theta/64^K)=2^{-K}S_K(\theta).
\]

Thus the changing finite-group products are exactly one fixed `Z_2` Fourier transform sampled along an adelic cusp.

### L-9302 — weighted shell tail (`PROPOSED`)

A uniform mean bound `a^r` on every block of `81^r` consecutive frequencies implies

\[
\sum_{\theta\ge81^M}\frac{F_K(\theta)}\theta
=O(a^M)
\]

uniformly in the top frequency.

### T-9301 — polynomial-window reduction (`PROPOSED`, conditional)

Under the frequency block mean, full EQ follows from any uniform estimate

\[
\max_{1\le\theta\le K^A}F_K(\theta)\le K^{-b}
\]

with fixed positive `A,b`. The apparent pointwise burden drops from exponentially many numerators to a polynomial window.

### T-9302 — density-one full EQ (`PROPOSED`, conditional)

Assuming both branch-qualified block means from issue #4, the complete weighted EQ sum tends to zero along a natural-density-one set of depths. For the proposed constants, a direct union bound supports any polynomial-window exponent below approximately `0.06615` on the good depths.

### D-9302 — adelic natural extension (`PROPOSED`)

The shared real/2-adic coding is one orbit in

\[
(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)/\Delta\mathbb Z[1/6]
\]

under multiplication by `81/64`. Ordinary integer survivors are exactly intersections with a rigid section having third coordinate zero. If `A>=2` is such an integer point, the induced orbit satisfies the exact real identity

\[
A_k=(81/64)^k(A-x_\infty)+x_\infty(\sigma^k\varepsilon)
\]

and diverges.

### L-9303 — phase-energy product bound (`PROPOSED`)

The normalized product obeys

\[
F_K(\theta)
\le\exp\!\left(-2\sum_t x_{K,t}(\theta)^2\right).
\]

Therefore logarithmic total squared phase distance is already enough for polynomial decay.

### C-9301 — logarithmic cusp scattering (`IDEA`)

The flagship open lemma asks only for `c log K` uniformly nondegenerate phases, or equivalently a logarithmic lower bound for the more stable phase energy, throughout one polynomial numerator window.

### O-9301 / X-9301 (`EMPIRICAL`)

The exact bounded scan found no immediate failure of the fixed-threshold shape. At threshold `1/8`, the minimum scattered count over `theta<=K^2` rose from `4` at `K=8` to `44` at `K=80`. This is finite evidence only and is not used by any proof-level claim.

## Candidate counterexamples

None.

No positive integer in the survivor attractor, nontrivial cycle, divergent ordinary Collatz trajectory, or `K-####` object is claimed.

The solenoid section supplies a candidate **format**: any explicit nontrivial point of `Phi(Omega) cap I` in a valid chart class would become an induced divergent orbit and then a candidate Collatz counterexample after the existing chart translation is independently checked.

## Failed approaches and negative findings

1. **Direct import of real self-similar Fourier decay.** Rejected. The literature branch is right that the relevant characters escape 2-adically and the available real theorems do not directly supply uniform cusp estimates.
2. **Pointwise attack on all `2^K` frequencies.** Shown to be overkill for the weighted target by `L-9302` and `T-9301`.
3. **Generic measure-rigidity invocation.** Rejected. One integer witness does not automatically generate a positive-entropy jointly invariant measure, and the symbolic leaf has a special zero 3-adic coordinate.
4. **Positive-density scattering conjecture.** Not adopted. The proof needs only logarithmically many losses; a stronger claim would add risk without improving the qualitative conclusion.
5. **Treating density-one EQ as all-depth EQ.** Explicitly rejected. The exceptional zero-density depth set remains the central obstruction and may still contain an M1 witness.

## Potential errors and review requests

1. Check the additive-character sign and the issue-#4 digit order in `L-9301`. A conjugate sign does not affect absolute values, but the complex identity should be exact.
2. Check that the proposed issue-#4 frequency block mean holds for every consecutive full block, not just one alignment. `L-9302` exposes this quantifier.
3. Check that the depth block mean is uniform in `theta` and every complete consecutive period before applying `T-9302`.
4. Reconstruct the base-`81` partition of the final incomplete shell in `L-9302`.
5. Audit the natural-density calculation in `T-9302`, especially the tiling of `[P_m,P_(m+1))` into exactly `80` periods.
6. Check the solenoid quotient section: the argument uses the third coordinate to force the diagonal representative to be zero.
7. Check the induced map/chart convention before importing the divergence conclusion from `D-9302` into ordinary Collatz coordinates.
8. The exact experiment was replayed locally, but a reviewer should run it independently and confirm the committed SHA-256.

## Verification performed

- Every proof was written from explicit definitions with branch-qualified dependencies.
- The character identity was checked at `K=1`, `theta=0`, and under exact `64`-power self-similarity.
- The weighted shell proof was checked at empty-complete-shell and final-partial-shell boundary cases.
- The density-one proof was audited without assuming independence across frequencies or depths.
- `X-9301` was run with Python `3.13.5` using only exact modular integer arithmetic:

```bash
python3 experiments/X-9301-cusp-scattering/run.py
```

- Frozen result digest:

```text
61e51931c4d034c5bc5a643c74d48532a2d70fe0fc662a4ff1899d735b21fb83
```

No large search, orbit scan, external solver, or floating-point Fourier census was used.

## Files changed

### Research packet

- `research/adelic-cusp/README.md`
- `research/adelic-cusp/CLAIMS.md`
- `research/adelic-cusp/PROOF_PROGRAM.md`
- `research/adelic-cusp/claims/D-9301-stationary-survivor-measure.md`
- `research/adelic-cusp/claims/L-9301-moving-character-identity.md`
- `research/adelic-cusp/claims/L-9302-weighted-shell-tail.md`
- `research/adelic-cusp/claims/T-9301-polynomial-window-reduction.md`
- `research/adelic-cusp/claims/T-9302-density-one-full-eq.md`
- `research/adelic-cusp/claims/D-9302-adelic-natural-extension.md`
- `research/adelic-cusp/claims/C-9301-logarithmic-cusp-scattering.md`
- `research/adelic-cusp/claims/L-9303-phase-energy-product.md`

### Limited experiment

- `experiments/X-9301-cusp-scattering/README.md`
- `experiments/X-9301-cusp-scattering/run.py`
- `experiments/X-9301-cusp-scattering/results/summary.txt`

### Report

- this file

## Claims affected

Added in isolated namespace:

- `D-9301`, `D-9302`;
- `L-9301`, `L-9302`, `L-9303`;
- `T-9301`, `T-9302`;
- `C-9301`, `Q-9301`;
- `O-9301`, `X-9301`.

No existing branch claim is promoted, weakened, or renumbered.

## Recommended next actions

1. Independently reconstruct `L-9301` and `L-9302` first; they are the load-bearing stationary and tail reductions.
2. Audit the exact quantifiers of the issue-#4 Theorems 11 and 12 against `T-9302`.
3. Prove a low-energy inverse theorem: low phase energy should yield either exact `64`-power reduction, an impossible low-height `{2,3}`-unit chain, or enough neighboring bad numerators to contradict the frequency block mean.
4. Extend `X-9301` only by emitting exact carry paths for current argmins. Do not spend computation merely increasing the depth bound.
5. Keep the direct M1 integer-section problem alive in parallel; EQ cannot rule out one exceptional infinite integer.

## Organizational improvement ideas

1. Add branch-qualified theorem interfaces to research packets. A conditional theorem should quote the full quantifiers it needs, not just a colliding claim ID.
2. Separate *stationary bridge*, *average theorem*, *maximal theorem*, and *integer-existence theorem* in the EQ ledger. They have different review burdens.
3. Require all Fourier experiments to state whether they test frequency averages, depth averages, pointwise maxima, or weighted discrepancy; these are not interchangeable.
4. Preserve the isolated `93xx` namespace until the canonical claim-ledger collision is resolved.
5. Index exact implication-only results such as `T-9301` separately from verification status of their imported hypotheses.
