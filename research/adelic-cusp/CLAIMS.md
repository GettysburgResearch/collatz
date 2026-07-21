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
| `T-9301` | Conditional theorem | `SUPERSEDED` | Conditional polynomial-window reduction | superseded by self-contained `T-9308` |
| `T-9302` | Conditional theorem | `SUPERSEDED` | Conditional density-one full EQ | superseded by unconditional `T-9309` |
| `T-9303` | Theorem | `PROPOSED` | Valuation-stratified fixed-frequency depth-period decay | `L-9304`; exact cosine-grid second moment |
| `T-9304` | Theorem | `PROPOSED` | Stationary two-place CRT Fourier factorization | `L-9301`, `L-9305`; CRT |
| `T-9305` | Theorem | `PROPOSED` | Split collapse and weighted discrepancy equivalence | `L-9307`; cosine Lipschitz and product telescoping |
| `T-9306` | Theorem | `PROPOSED` | Complex coefficient and bounded test-sequence equivalence | `L-9308`; complex-mask Lipschitz and telescoping |
| `T-9307` | Theorem | `PROPOSED` | Low-energy lift prefixes have an explicit entropy deficit | `L-9309`; exponential moments; `L-9303` for Fourier corollary |
| `T-9308` | Theorem | `PROPOSED` | Uniform harmonic high-frequency tail at every depth | `T-9307`, `T-9305`; geometric shell summation |
| `T-9309` | Theorem | `PROPOSED` | Unconditional full weighted EQ on density-one depths | `T-9303`, `T-9308`; valuation strata and Markov |
| `R-9301` | Refutation | `PROPOSED` | Exact carry prefixes do not amplify to consecutive intervals | `L-9309` |
| `C-9301` | Conjecture | `IDEA` | Logarithmic cusp scattering / all-depth low-frequency control | `L-9301`, `L-9303`, `T-9308` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `Q-9302` | Open question | `IDEA` | Two-place proof mechanism after target equivalence | `T-9304`, `L-9306`--`L-9309`, `T-9305`--`T-9308`, `R-9301` |
| `O-9301` | Observation | `EMPIRICAL` | Bounded polynomial-window scattering census | `X-9301` |
| `X-9301` | Experiment | `EMPIRICAL` | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |

## Status boundary

- Every complete-looking argument authored in this packet enters as `PROPOSED` pending independent review.
- `T-9301` remains a correct-looking conditional implication, but `T-9308` supplies a stronger self-contained tail and low/high reduction. It is therefore `SUPERSEDED`, not refuted.
- `T-9302` remains a correct-looking conditional density-one synthesis, but `T-9309` proves the same full weighted conclusion without the frequency-block hypothesis. It is therefore `SUPERSEDED`, not refuted.
- `T-9309` is the packet's strongest integrated theorem: the complete weighted EQ criterion holds along a natural-density-one set of depths with no external mathematical hypothesis.
- `T-9308` is uniform in every depth and removes the whole frequency range above any growing cutoff with a power-saving harmonic tail.
- `T-9307` is the combinatorial source of that tail: low-energy lift prefixes occupy at most a fixed fraction `beta^L` of every complete `81^L` block and a power-small fraction of every interval.
- `L-9309` proves exact lift-prefix uniformity and sparsity. `R-9301` refutes only the naive claim that one exact prefix persists on a consecutive neighborhood; approximate-cylinder and harmonic-location arguments remain open.
- `D-9303`, `L-9305`--`L-9309`, `T-9303`--`T-9309`, and `R-9301` are self-contained except where a file explicitly labels a branch-qualified optional consequence.
- `BLOCK_MEAN_AUDIT.md` records why the original uniform partial-product reading of issue #4's Theorem 12 needs valuation correction. It does not change that branch's claim status.
- `C-9301`, `Q-9301`, and `Q-9302` remain open. The all-depth obstruction is now confined to a growing set of the smallest frequencies and the zero-density exceptional depth set.
- No positive integer, divergent orbit, cycle, or Collatz counterexample is claimed.
- `O-9301` is finite empirical evidence only. It is not a premise of any proof-level claim.

## Main implication graph

```text
L-9309 lift-prefix bijection
   |
   v
T-9307 prefix entropy
   |
   v
T-9308 uniform harmonic tail at every depth
   |
   +---------------------------+
   |                           |
   v                           v
all-depth low/high target   T-9303 depth-period low-window mean
                               |
                               v
                         T-9309 unconditional
                         density-one full EQ
```

The direct M1 route remains separate:

```text
D-9301 survivor coding
   |
   v
D-9302 adelic integer section
   |
   v
Q-9301 nontrivial ordinary-integer intersection
```

## Branch crosswalk

The notation `CLAUDE/T11` and `CLAUDE/T12` refers descriptively to the block-frequency and block-depth results called Theorems 11 and 12 in `EQ.md` on `claude/collatz-migration-math-osr370`. The literature branch uses different stable namespacing. An integrator must preserve this branch qualification until the competing ledgers are reconciled.

The average-theorem audit remains useful historically:

- the written `CLAUDE/T11` interface supports the conditional `L-9302`/`T-9301` route, pending independent proof review;
- the displayed `CLAUDE/T12` proof mechanism is not uniform in frequencies divisible by `3`, so `T-9303` replaced that dependency;
- neither external interface is needed by the new `T-9308`/`T-9309` chain.

The issue-#4 room/Cantor crosswalk is:

- issue-#4 `C_j` recursion = the reductions of `D-9303`;
- issue-#4 finite Cantor product = `L-9305`;
- exact CRT transform of `R_n x C_j` = `T-9304`;
- complete-frequency absolute moments = `L-9306`;
- the two local characters are one global rational diagonal and stitch one phase chain = `L-9307`/`L-9308`;
- sub-`64^K` absolute and bounded harmonic complex tests collapse to the original survivor tests = `T-9305`/`T-9306`;
- exact length-`L` lift data are a permutation of residues modulo `81^L` = `L-9309`;
- exact-prefix Euclidean interval amplification is false = `R-9301`;
- low-energy approximate prefixes have an explicit entropy deficit = `T-9307`;
- ordered-position transfer remains branch-qualified for geometric statements, but is not needed for the coefficient and tail theorems;
- `Q-9302` now targets harmonic location of the sparse exceptional cylinders, positive room operators, carry-template inversion, or hyperbolic renewal.