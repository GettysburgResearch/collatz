# Claim ledger: adelic cusp Fourier packet

This is an isolated `93xx` namespace for issue #15. It is not a replacement for any canonical root ledger and does not renumber claims on unmerged branches.

**Independent review update (target `e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6`):** `gpt56-review-9309-01` independently reconstructed `L-9309`, `T-9307`, `T-9308`, `L-9310`, `T-9311`, and `T-9312`; all six received review verdict `PASSED` and are proposed here as `INDEPENDENTLY_VERIFIED`. See `reports/gpt56-review-9309-01/2026-07-22-15-adelic-chain-adversarial-review.md` and `research/adelic-cusp/REVIEW_STATUS.md`.

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
| `L-9309` | Lemma | `INDEPENDENTLY_VERIFIED` | Lift-digit prefixes are residue classes modulo `81^L` | `L-9307`; elementary modular lifting |
| `L-9310` | Lemma | `INDEPENDENTLY_VERIFIED` | Completion-height rigidity for integral phase carries | elementary modular lifting and height separation |
| `L-9311` | Lemma | `PROPOSED` | Repeated itinerary factors are orbit-difference zero-carry chains | `D-9302`; integer divisibility |
| `T-9301` | Conditional theorem | `SUPERSEDED` | Conditional polynomial-window reduction | superseded by self-contained `T-9308` |
| `T-9302` | Conditional theorem | `SUPERSEDED` | Conditional density-one full EQ | superseded by unconditional `T-9309` |
| `T-9303` | Theorem | `PROPOSED` | Valuation-stratified fixed-frequency depth-period decay | `L-9304`; exact cosine-grid second moment |
| `T-9304` | Theorem | `PROPOSED` | Stationary two-place CRT Fourier factorization | `L-9301`, `L-9305`; CRT |
| `T-9305` | Theorem | `PROPOSED` | Split collapse and weighted discrepancy equivalence | `L-9307`; cosine Lipschitz and product telescoping |
| `T-9306` | Theorem | `PROPOSED` | Complex coefficient and bounded test-sequence equivalence | `L-9308`; complex-mask Lipschitz and telescoping |
| `T-9307` | Theorem | `INDEPENDENTLY_VERIFIED` | Low-energy lift prefixes have an explicit entropy deficit | count: `L-9309`, exponential moments; Fourier: `L-9305`, `L-9303`; transfer: `T-9305`, `T-9306` |
| `T-9308` | Theorem | `INDEPENDENTLY_VERIFIED` | Uniform harmonic high-frequency tail at every depth | `T-9307`, `T-9305`; geometric shell summation |
| `T-9309` | Theorem | `PROPOSED` | Unconditional full weighted EQ on density-one depths | `T-9303`, `T-9308`; valuation strata and Markov |
| `T-9310` | Theorem | `PROPOSED` | Weighted EQ converges in uniform density | `T-9303`, `T-9308`; translated-period Markov bounds |
| `T-9311` | Theorem | `INDEPENDENTLY_VERIFIED` | Uniform pointwise cusp decay on every subexponential numerator window | `L-9310`, `L-9303`, `T-9305`, `L-9301` |
| `T-9312` | Theorem | `INDEPENDENTLY_VERIFIED` | Complete weighted EQ at every depth | `T-9311`, `T-9308`; harmonic splitting |
| `T-9313` | Theorem | `PROPOSED` | Fixed-room equivalence and exact `C_j`/`R_j` minimum duality | `D-9302`, `D-9303`, `L-9301` |
| `T-9314` | Theorem | `PROPOSED` | Exact depth-46 minimum survivor; ordinary rooms exceed `2^227` | `T-9313`, `X-9303` |
| `R-9301` | Refutation | `PROPOSED` | Exact carry prefixes do not amplify to consecutive intervals | `L-9309` |
| `R-9302` | Refutation | `PROPOSED` | Matching repetition/carry criticalities do not contradict | `L-9310`, `L-9311` |
| `C-9301` | Historical conjecture | `SUPERSEDED` | Harmonic control of low-energy cylinders | superseded by `L-9310`, `T-9311`, `T-9312` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `Q-9302` | Open question | `IDEA` | Fixed-room and active-cylinder nonstabilization | `D-9302`, `D-9303`, `L-9310`, `L-9311`, `T-9312`--`T-9314` |
| `O-9301` | Observation | `EMPIRICAL` | Bounded polynomial-window scattering census | `X-9301` |
| `O-9302` | Observation | `EMPIRICAL` | Bounded carry counts and zero-run census | `X-9302` |
| `O-9303` | Observation | `INTERNAL EXACT COMPUTATION` | Exact dual minima and survivor replays through depth 46 | `X-9303` |
| `X-9301` | Experiment | `EMPIRICAL` | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |
| `X-9302` | Experiment | `EMPIRICAL` | Exact completion-height carry audit through depth 80 | standard-library exact modular arithmetic and fractions |
| `X-9303` | Experiment | `INTERNAL EXACT COMPUTATION` | Meet-in-the-middle exact survivor-minimum certificate | exact modular subset sums and direct replay |

## Status boundary

- Every complete-looking argument authored in this packet entered as `PROPOSED` pending independent review.
- At the frozen target commit, `gpt56-review-9309-01` independently reconstructed and passed `L-9309`, `T-9307`, `T-9308`, `L-9310`, `T-9311`, and `T-9312`; no proof body or statement was replaced.
- `T-9312` is the strongest integrated finite-set theorem: complete weighted EQ tends to zero at every depth.
- `T-9313` gives an exact ordinary-section interface and an exact finite duality:
  \[
  \min(R_j\setminus\{0,1\})
  =
  \left\lceil
  \min(C_j\setminus\{0,1\})(64/81)^j
  \right\rceil.
  \]
- `T-9314` and `X-9303` compute the exact first nontrivial depth-46 survivor and exclude every nontrivial infinite ordinary room through `2^227`.
- `L-9311` reconstructs PR #20's local repetition bound as an integral zero-carry theorem for differences of ordinary tail orbits.
- `R-9302` closes the naive comparison of the identical repetition and phase-carry constants. They are one mechanism, not opposing budgets.
- `T-9311` supplies deterministic low-frequency Fourier decay; `T-9308` supplies the high-frequency tail.
- `T-9309` and `T-9310` remain independent depth-statistical cross-checks and remain `PROPOSED`.
- `T-9301`, `T-9302`, and `C-9301` are superseded, not refuted.
- `Q-9301` remains open. A finite exact minimum, however large, is not an asymptotic nonintersection theorem.
- No positive integer survivor, divergent orbit, cycle, or Collatz counterexample is claimed.

## Main implication graph

```text
L-9309 lift-chain arithmetic
   |
   v
T-9307 prefix entropy
   |
   v
T-9308 uniform harmonic tail --------+
                                      |
                                      v
                                T-9312 all-depth
                                complete weighted EQ
                                      ^
                                      |
L-9310 integral carries               |
+ completion-height rigidity          |
   |                                  |
   v                                  |
T-9311 pointwise decay ---------------+
on subexponential windows
```

The ordinary-section chain is:

```text
D-9302 integral tails + bounded real companion
   + D-9303 triadic past classes
   + L-9301 finite survivor coding
   |
   v
T-9313 fixed-room equivalence and exact minimum duality
   |
   + X-9303 exact MITM class minimum + direct survivor replay
   |
   v
T-9314 exact depth-46 minimum; no ordinary room <= 2^227
   |
   v
Q-9301 prove min(R_j \ {0,1}) -> infinity
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

`L-9310` is stated for every coprime expanding chart `M<N`, with

\[
\kappa_{M,N}
=
\frac{\log M}{\log(N/M)}
=
\frac1{\log_MN-1}.
\]

For `M=64`, `N=81`, `L-9311` proves why the same constant occurs in ordinary-code repetition rigidity: repeated factors are zero-carry chains in an orbit difference.

The literature branch supplied scope discipline: completion-versus-height methods are relevant; fixed-real Fourier, finite-state pressure, generic S-unit, and measure-rigidity theorems do not automatically close this moving ordinary-section problem. No literature theorem is load-bearing for the six independently verified claims.

## Branch crosswalk

The issue-#4 room/Cantor crosswalk is:

- issue-#4 `C_j` recursion = the reductions of `D-9303`;
- issue-#4 finite Cantor product = `L-9305`;
- exact CRT transform of `R_n x C_j` = `T-9304`;
- the two local characters stitch one global reciprocal chain = `L-9307`/`L-9308`;
- integral carries force pointwise low-frequency decay = `L-9310`/`T-9311`;
- the entropy tail and pointwise low window assemble into all-depth EQ = `T-9312`;
- one ordinary itinerary has a fixed room across every past/future splitting = `T-9313`;
- finite Cantor minima transform exactly into finite survivor minima = `T-9313(18)`;
- the depth-46 dual computation yields `T-9314`;
- `Q-9302` targets monotone minimum divergence, coherent-minimum growth, and active-cylinder nonstabilization.
