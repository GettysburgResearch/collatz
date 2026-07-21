# Claim ledger: adelic cusp Fourier packet

This is an isolated `93xx` namespace for issue #15. It is not a replacement for any canonical root ledger and does not renumber claims on unmerged branches.

| ID | Type | Status | Short title | Dependencies |
|---|---|---|---|---|
| `D-9301` | Definition/construction | `PROPOSED` | Stationary survivor measure on `Z_2` | elementary 2-adic convergence |
| `D-9302` | Definition/construction | `PROPOSED` | Adelic natural extension and integer section | `D-9301`; elementary quotient algebra |
| `D-9303` | Definition/construction | `PROPOSED` | Stationary triadic mirror measure | elementary 3-adic convergence and separation |
| `L-9301` | Lemma | `PROPOSED` | Moving-character survivor Fourier identity | `D-9301`; issue-#4 notation crosswalk |
| `L-9302` | Lemma | `PROPOSED` | Conditional weighted shell tail from frequency-block means | elementary interval decomposition |
| `L-9303` | Lemma | `PROPOSED` | Phase energy controls the survivor Fourier product | `L-9301`; elementary cosine inequality |
| `L-9304` | Lemma | `PROPOSED` | Exact 2–3 phase reciprocity and valuation shift | elementary modular arithmetic; LTE reproved locally |
| `L-9305` | Lemma | `PROPOSED` | Moving-character triadic Fourier identity | `D-9303` |
| `L-9306` | Lemma | `PROPOSED` | Full-group absolute moments factor exactly | `T-9304`; CRT; Parseval for `p=2` |
| `L-9307` | Lemma | `PROPOSED` | Global rational diagonal and bilateral phase stitching | `L-9301`, `L-9305`, `T-9304`; circle reciprocity |
| `L-9308` | Lemma | `PROPOSED` | Complex bilateral phase stitching | `L-9307`; local character conventions |
| `L-9309` | Lemma | `PROPOSED` | Lift-digit prefixes are residue classes modulo `81^L` | `L-9307`; elementary modular lifting |
| `L-9310` | Lemma | `PROPOSED` | Completion-height rigidity for integral phase carries | elementary modular lifting and height separation |
| `L-9311` | Lemma | `PROPOSED` | Repeated itinerary factors are orbit-difference zero-carry chains | `D-9302`; integer divisibility |
| `T-9301` | Conditional theorem | `SUPERSEDED` | Conditional polynomial-window reduction | superseded by self-contained `T-9308` |
| `T-9302` | Conditional theorem | `SUPERSEDED` | Conditional density-one full EQ | superseded by unconditional `T-9309` |
| `T-9303` | Theorem | `PROPOSED` | Valuation-stratified fixed-frequency depth-period decay | `L-9304`; exact cosine-grid second moment |
| `T-9304` | Theorem | `PROPOSED` | Stationary two-place CRT Fourier factorization | `L-9301`, `L-9305`; CRT |
| `T-9305` | Theorem | `PROPOSED` | Split collapse and weighted discrepancy equivalence | `L-9307`; cosine Lipschitz and product telescoping |
| `T-9306` | Theorem | `PROPOSED` | Complex coefficient and bounded test-sequence equivalence | `L-9308`; complex-mask Lipschitz and telescoping |
| `T-9307` | Theorem | `PROPOSED` | Low-energy lift prefixes have an explicit entropy deficit | `L-9309`; exponential moments; `L-9303` for Fourier corollary |
| `T-9308` | Theorem | `PROPOSED` | Uniform harmonic high-frequency tail at every depth | `T-9307`, `T-9305`; geometric shell summation |
| `T-9309` | Theorem | `PROPOSED` | Unconditional full weighted EQ on density-one depths | `T-9303`, `T-9308`; valuation strata and Markov |
| `T-9310` | Theorem | `PROPOSED` | Weighted EQ converges in uniform density | `T-9303`, `T-9308`; translated-period Markov bounds |
| `T-9311` | Theorem | `PROPOSED` | Uniform pointwise cusp decay on every subexponential numerator window | `L-9310`, `L-9303`, `T-9305`, `L-9301` |
| `T-9312` | Theorem | `PROPOSED` | Complete weighted EQ at every depth | `T-9311`, `T-9308`; harmonic splitting |
| `T-9313` | Theorem | `PROPOSED` | Ordinary survivors are fixed-room coherent past/future paths | `D-9302`, `D-9303`; exact tail iteration |
| `T-9314` | Theorem | `PROPOSED` | Exact depth-44 certificate excludes ordinary rooms through `2^217` | `T-9313`, `X-9303` |
| `R-9301` | Refutation | `PROPOSED` | Exact carry prefixes do not amplify to consecutive intervals | `L-9309` |
| `R-9302` | Refutation | `PROPOSED` | Matching repetition/carry criticalities do not contradict | `L-9310`, `L-9311` |
| `C-9301` | Historical conjecture | `SUPERSEDED` | Harmonic control of low-energy cylinders | superseded by `L-9310`, `T-9311`, `T-9312` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `Q-9302` | Open question | `IDEA` | Two-place and room mechanisms for the ordinary-section frontier | `D-9302`, `T-9304`, `L-9306`--`L-9311`, `T-9305`--`T-9314` |
| `O-9301` | Observation | `EMPIRICAL` | Bounded polynomial-window scattering census | `X-9301` |
| `O-9302` | Observation | `EMPIRICAL` | Bounded carry counts and zero-run census | `X-9302` |
| `O-9303` | Observation | `INTERNAL EXACT COMPUTATION` | Exact past-class minima through depth 44 | `X-9303` |
| `X-9301` | Experiment | `EMPIRICAL` | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |
| `X-9302` | Experiment | `EMPIRICAL` | Exact completion-height carry audit through depth 80 | standard-library exact modular arithmetic and fractions |
| `X-9303` | Experiment | `INTERNAL EXACT COMPUTATION` | Meet-in-the-middle past-class minimum certificate | exact modular subset sums |

## Status boundary

- Every complete-looking argument authored in this packet enters as `PROPOSED` pending independent review.
- `T-9312` is the packet's strongest integrated finite-set theorem: the complete weighted EQ criterion tends to zero at **every** depth.
- `T-9313` is the new exact ordinary-section interface. A hypothetical ordinary point is one fixed-room coherent path whose reversed past lies in `C_j`, whose future remains in the survivor attractor, and whose standard representative stays in an `O((81/64)^j)` window.
- `T-9314` is a genuine but finite ordinary-section exclusion: subject to exact replay, every nontrivial ordinary room exceeds `2^217`.
- `L-9311` reconstructs PR #20's local repetition bound as an integral zero-carry theorem for differences of ordinary tail orbits.
- `R-9302` closes the naive plan of comparing the identical repetition and phase-carry criticality constants. They are the same completion-height mechanism, not opposing budgets.
- `T-9311` supplies the deterministic low-frequency Fourier input; `T-9308` supplies the complementary high-frequency tail.
- `T-9309` and `T-9310` remain independent quantitative depth-statistical cross-checks.
- `T-9301`, `T-9302`, and `C-9301` are superseded, not refuted.
- `BLOCK_MEAN_AUDIT.md` records why the original uniform partial-product reading of issue #4's Theorem 12 needs valuation correction.
- `Q-9301` remains open. The finite lower bound in `T-9314` is not an asymptotic nonintersection theorem.
- No positive integer, divergent orbit, cycle, or Collatz counterexample is claimed.
- `X-9303` is exact finite computation; it is not an asymptotic proof.

## Main implication graph

```text
L-9309 lift-chain arithmetic
   |
   v
L-9310 integral carries + completion-height rigidity
   |
   v
T-9311 pointwise decay on subexponential windows
   |
   +--------------------------------+
   |                                |
   |                         L-9309 lift-prefix bijection
   |                                |
   |                                v
   |                         T-9307 prefix entropy
   |                                |
   |                                v
   |                         T-9308 uniform harmonic tail
   |                                |
   +---------------+----------------+
                   |
                   v
             T-9312 all-depth
             complete weighted EQ
```

The ordinary-section chain is now:

```text
D-9302 integral tails + bounded real companion
   + D-9303 triadic past classes
   |
   v
T-9313 fixed-room past/future equivalence
   |
   + X-9303 exact depth-44 class minimum
   |
   v
T-9314 no nontrivial ordinary room <= 2^217
   |
   v
Q-9301 asymptotic fixed-room nonintersection
```

The cross-program method audit is:

```text
L-9311 orbit-difference zero-carry chain
   + L-9310 reciprocal-character zero-carry chain
   |
   v
R-9302 identical criticality does not double-count
```

## Generalization and literature crosswalk

`L-9310` is stated for every coprime expanding chart `M<N`. Its criticality constant is

\[
\kappa_{M,N}
=
\frac{\log M}{\log(N/M)}
=
\frac1{\log_MN-1}.
\]

For `M=64`, `N=81`, `L-9311` proves directly why the same constant occurs in ordinary-code repetition rigidity: repeated factors are exact zero-carry chains in an orbit difference.

The literature branch supplied the correct methodological boundaries:

- rational-base address identities and completion-versus-height decoupling are reusable infrastructure;
- finite-state tilted transfer bounds apply only after a frozen truncation;
- fixed real self-similar Fourier theorems do not directly control the moving cusp;
- generic S-unit language does not apply without fixed multiplicative cofactors.

The new fixed-room theorem remains exact native arithmetic.

## Branch crosswalk

The notation `CLAUDE/T11` and `CLAUDE/T12` refers descriptively to the block-frequency and block-depth results called Theorems 11 and 12 in `EQ.md` on `claude/collatz-migration-math-osr370`. An integrator must preserve branch qualification until the ledgers are reconciled.

The issue-#4 room/Cantor crosswalk is:

- issue-#4 `C_j` recursion = the reductions of `D-9303`;
- issue-#4 finite Cantor product = `L-9305`;
- exact CRT transform of `R_n x C_j` = `T-9304`;
- complete-frequency absolute moments = `L-9306`;
- the two local characters stitch one global reciprocal chain = `L-9307`/`L-9308`;
- sub-`64^K` harmonic tests collapse to the original survivor tests = `T-9305`/`T-9306`;
- exact lift data are a permutation of residues modulo `81^L` = `L-9309`;
- low-energy approximate prefixes have an entropy deficit = `T-9307`;
- integral carries force pointwise low-frequency decay = `L-9310`/`T-9311`;
- the entropy tail and pointwise low window assemble into all-depth EQ = `T-9312`;
- one ordinary itinerary has a fixed room across all past/future splittings = `T-9313`;
- depth-44 exact minimization yields the bounded ordinary-room exclusion = `T-9314`;
- ordered-position transfer remains branch-qualified for downstream geometric statements;
- `Q-9302` now targets asymptotic fixed-room exclusion, active-cylinder nonstabilization, and sharper ordinary-section couplings.
