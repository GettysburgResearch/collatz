# Claim ledger: adelic cusp Fourier packet

This is an isolated `93xx` namespace for issue #15. It is not a replacement for any canonical root ledger and does not renumber claims on unmerged branches.

| ID | Type | Status | Short title | Dependencies |
|---|---|---|---|---|
| `D-9301` | Definition/construction | `PROPOSED` | Stationary survivor measure on `Z_2` | elementary 2-adic convergence |
| `D-9302` | Definition/construction | `PROPOSED` | Adelic natural extension and integer section | `D-9301`; elementary quotient algebra |
| `D-9303` | Definition/construction | `PROPOSED` | Stationary triadic mirror measure | elementary 3-adic convergence and separation |
| `L-9301` | Lemma | `PROPOSED` | Moving-character survivor Fourier identity | `D-9301`; issue-#4 notation crosswalk |
| `L-9302` | Lemma | `PROPOSED` | Weighted shell tail from frequency-block means | elementary interval decomposition |
| `L-9303` | Lemma | `PROPOSED` | Phase energy controls the survivor Fourier product | `L-9301`; elementary cosine inequality |
| `L-9304` | Lemma | `PROPOSED` | Exact 2–3 phase reciprocity and valuation shift | elementary modular arithmetic; LTE reproved locally |
| `L-9305` | Lemma | `PROPOSED` | Moving-character triadic Fourier identity | `D-9303` |
| `L-9306` | Lemma | `PROPOSED` | Full-group absolute moments factor exactly | `T-9304`; CRT; Parseval for `p=2` |
| `T-9301` | Conditional theorem | `PROPOSED` | Polynomial-window reduction to all-depth EQ | `L-9301`, `L-9302`; branch-qualified frequency block mean |
| `T-9302` | Conditional theorem | `PROPOSED` | Density-one full EQ from frequency blocks and exact depth periods | `L-9302`, `T-9303`; branch-qualified frequency block mean only |
| `T-9303` | Theorem | `PROPOSED` | Valuation-stratified fixed-frequency depth-period decay | `L-9304`; exact cosine-grid second moment |
| `T-9304` | Theorem | `PROPOSED` | Stationary two-place CRT Fourier factorization | `L-9301`, `L-9305`; CRT |
| `C-9301` | Conjecture | `IDEA` | Logarithmic cusp scattering | `L-9301`, `L-9303`, `T-9301` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `Q-9302` | Open question | `IDEA` | Two-place room-cusp decay | `T-9304`, `L-9306`; branch-qualified room-position interface |
| `O-9301` | Observation | `EMPIRICAL` | Bounded polynomial-window scattering census | `X-9301` |
| `X-9301` | Experiment | `EMPIRICAL` | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |

## Status boundary

- Every complete-looking argument authored in this packet enters as `PROPOSED` pending independent review.
- `T-9301` remains conditional on the branch-qualified issue-#4 frequency-block theorem.
- Revised `T-9302` no longer assumes issue #4's depth-block theorem. `T-9303` reconstructs a uniform complete-period estimate with the exact `v_3(theta)` loss; only the frequency-block input remains external.
- `D-9303`, `L-9305`, `T-9304`, and `L-9306` are self-contained. The position-rigidity consequence of `T-9304` is explicitly conditional on the branch-qualified issue-#4 room/CRT comparison.
- `BLOCK_MEAN_AUDIT.md` records why the original uniform partial-product reading of issue #4's Theorem 12 needs valuation correction. It does not change that branch's claim status.
- `C-9301`, `Q-9301`, and `Q-9302` are open. No positive integer, divergent orbit, cycle, or Collatz counterexample is claimed.
- `O-9301` is finite empirical evidence only. It is not a premise of any proof-level claim.

## Branch crosswalk

The notation `CLAUDE/T11` and `CLAUDE/T12` refers descriptively to the block-frequency and block-depth results called Theorems 11 and 12 in `EQ.md` on `claude/collatz-migration-math-osr370`. The literature branch uses different stable namespacing. An integrator must preserve this branch qualification until the competing ledgers are reconciled.

The audit verdict is asymmetric:

- the written `CLAUDE/T11` interface supplies the arbitrary-full-block hypothesis used by `L-9302`, `T-9301`, and `T-9302`, pending independent proof review;
- the displayed `CLAUDE/T12` proof mechanism is not uniform in frequencies divisible by `3`, so `T-9303` replaces that dependency rather than silently strengthening it.

The newest issue-#4 interchange packet defines Cantor classes `C_j`, their transform, and a position-rigid CRT comparison with `R_n`. This packet's crosswalk is:

- issue-#4 `C_j` recursion = the reductions of `D-9303`;
- issue-#4 finite Cantor product = `L-9305`;
- exact CRT transform of `R_n x C_j` = the main theorem `T-9304`;
- complete-frequency absolute moments = `L-9306`;
- transfer from that CRT set to the actual archimedean positions of `R_(n+j)` remains branch-qualified and is used only through an explicit conditional inequality;
- `Q-9302` isolates the remaining short-orbit problem after full-group correlation has factored away.