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
| `R-9301` | Refutation | `PROPOSED` | Exact carry prefixes do not amplify to consecutive intervals | `L-9309` |
| `C-9301` | Historical conjecture | `SUPERSEDED` | Harmonic control of low-energy cylinders | superseded by `L-9310`, `T-9311`, `T-9312` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `Q-9302` | Open question | `IDEA` | Two-place and room mechanisms for the ordinary-section frontier | `D-9302`, `T-9304`, `L-9306`--`L-9310`, `T-9305`--`T-9312` |
| `O-9301` | Observation | `EMPIRICAL` | Bounded polynomial-window scattering census | `X-9301` |
| `O-9302` | Observation | `EMPIRICAL` | Bounded carry counts and zero-run census | `X-9302` |
| `X-9301` | Experiment | `EMPIRICAL` | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |
| `X-9302` | Experiment | `EMPIRICAL` | Exact completion-height carry audit through depth 80 | standard-library exact modular arithmetic and fractions |

## Status boundary

- Every complete-looking argument authored in this packet enters as `PROPOSED` pending independent review.
- `T-9312` is the packet's strongest integrated theorem: the complete weighted EQ criterion tends to zero at **every** depth.
- `T-9311` supplies the formerly missing deterministic low-frequency input: every subexponential numerator window has uniform pointwise decay.
- `L-9310` is the arithmetic source. Signed reciprocal phases have integral carries; few nonzero carries force long zero-carry runs, and every such run violates a completion-height bound beyond a logarithmic threshold.
- `T-9308` remains the complementary high-frequency theorem, uniform in every depth.
- `T-9309` and `T-9310` remain useful independent average and translated-block consequences. They are logically weaker than `T-9312`, but preserve quantitative information about depth statistics and provide adversarial cross-checks.
- `T-9301` and `T-9302` remain correct-looking historical implications but are superseded by stronger self-contained results.
- `C-9301` is superseded, not refuted: the harmonic-location conjecture is replaced by the stronger pointwise carry-rigidity theorem.
- `L-9309` proves exact lift-prefix uniformity and sparsity. `R-9301` refutes only the naive claim that one exact prefix persists on a consecutive neighborhood.
- `BLOCK_MEAN_AUDIT.md` records why the original uniform partial-product reading of issue #4's Theorem 12 needs valuation correction. It does not change that branch's claim status.
- `Q-9301` remains open. All-depth finite-set EQ does not automatically decide whether the infinite `2`-adic attractor contains one ordinary positive integer.
- No positive integer, divergent orbit, cycle, or Collatz counterexample is claimed.
- `O-9301` and `O-9302` are finite empirical evidence only. Neither is a premise of a proof-level claim.

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

The independent depth-statistical chain remains:

```text
T-9303 translated depth-period mean
   + T-9308 uniform harmonic tail
   |
   v
T-9309 natural-density-one EQ
   |
   v
T-9310 uniform-density EQ
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

## Generalization and literature crosswalk

`L-9310` is stated for every coprime expanding chart `M<N`, not only `64 -> 81`. Its criticality constant is

\[
\kappa_{M,N}
=
\frac{\log M}{\log(N/M)}
=
\frac1{\log_MN-1}.
\]

For `M=64`, `N=81`, this is the same constant independently found in PR #20's ordinary-code repetition rigidity. The two proofs share one product-formula mechanism: excessive completion agreement plus controlled rational height forces equality, and the primitive numerator excludes equality.

The literature branch supplied the correct methodological boundaries:

- rational-base address identities and completion-versus-height decoupling are reusable infrastructure;
- finite-state tilted transfer bounds apply only after a frozen truncation;
- fixed real self-similar Fourier theorems do not directly control the moving cusp;
- generic S-unit language does not apply without fixed multiplicative cofactors.

`L-9310` stays inside those boundaries and uses only exact native arithmetic.

## Branch crosswalk

The notation `CLAUDE/T11` and `CLAUDE/T12` refers descriptively to the block-frequency and block-depth results called Theorems 11 and 12 in `EQ.md` on `claude/collatz-migration-math-osr370`. An integrator must preserve branch qualification until the ledgers are reconciled.

The issue-#4 room/Cantor crosswalk remains:

- issue-#4 `C_j` recursion = the reductions of `D-9303`;
- issue-#4 finite Cantor product = `L-9305`;
- exact CRT transform of `R_n x C_j` = `T-9304`;
- complete-frequency absolute moments = `L-9306`;
- the two local characters stitch one global reciprocal chain = `L-9307`/`L-9308`;
- sub-`64^K` absolute and bounded harmonic tests collapse to the original survivor tests = `T-9305`/`T-9306`;
- exact lift data are a permutation of residues modulo `81^L` = `L-9309`;
- low-energy approximate prefixes have an entropy deficit = `T-9307`;
- integral carries force pointwise low-frequency decay = `L-9310`/`T-9311`;
- the entropy tail and pointwise low window assemble into all-depth EQ = `T-9312`;
- ordered-position transfer remains branch-qualified for downstream geometric statements;
- `Q-9302` now concerns whether the room/adelic representation helps with the remaining ordinary-integer section, sharper rates, or cross-program complexity rigidity.