# Claim ledger: adelic cusp Fourier packet

This is an isolated `93xx` namespace for issue #15. It is not a replacement for any canonical root ledger and does not renumber claims on unmerged branches.

| ID | Type | Status | Short title | Dependencies |
|---|---|---|---|---|
| `D-9301` | Definition/construction | `PROPOSED` | Stationary survivor measure | elementary 2-adic convergence |
| `L-9301` | Lemma | `PROPOSED` | Moving-character Fourier identity | `D-9301`; issue-#4 notation crosswalk |
| `L-9302` | Lemma | `PROPOSED` | Weighted shell tail from block means | elementary interval decomposition |
| `L-9303` | Lemma | `PROPOSED` | Phase energy controls the Fourier product | `L-9301`; elementary cosine inequality |
| `L-9304` | Lemma | `PROPOSED` | Exact 2–3 phase reciprocity and valuation shift | elementary modular arithmetic; LTE reproved locally |
| `T-9301` | Conditional theorem | `PROPOSED` | Polynomial-window reduction to EQ | `L-9301`, `L-9302`; branch-qualified frequency block mean |
| `T-9302` | Conditional theorem | `PROPOSED` | Density-one full EQ from frequency blocks and exact depth periods | `L-9302`, `T-9303`; branch-qualified frequency block mean only |
| `T-9303` | Theorem | `PROPOSED` | Valuation-stratified fixed-frequency depth-period decay | `L-9304`; exact cosine-grid second moment |
| `D-9302` | Definition/construction | `PROPOSED` | Adelic natural extension and integer section | `D-9301`; elementary quotient algebra |
| `C-9301` | Conjecture | `IDEA` | Logarithmic cusp scattering | `L-9301`, `L-9303`, `T-9301` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `O-9301` | Observation | `EMPIRICAL` | Bounded polynomial-window scattering census | `X-9301` |
| `X-9301` | Experiment | `EMPIRICAL` | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |

## Status boundary

- Every complete-looking argument authored in this packet enters as `PROPOSED` pending independent review.
- `T-9301` remains conditional on the branch-qualified issue-#4 frequency-block theorem.
- Revised `T-9302` no longer assumes issue #4's depth-block theorem. `T-9303` reconstructs a uniform complete-period estimate with the exact `v_3(theta)` loss; only the frequency-block input remains external.
- `BLOCK_MEAN_AUDIT.md` records why the original uniform partial-product reading of issue #4's Theorem 12 needs valuation correction. It does not change that branch's claim status.
- `C-9301` and `Q-9301` are open. No positive integer, divergent orbit, cycle, or Collatz counterexample is claimed.
- `O-9301` is finite empirical evidence only. It is not a premise of any proof-level claim.

## Branch crosswalk

The notation `CLAUDE/T11` and `CLAUDE/T12` refers descriptively to the block-frequency and block-depth results called Theorems 11 and 12 in `EQ.md` on `claude/collatz-migration-math-osr370`. The literature branch uses different stable namespacing. An integrator must preserve this branch qualification until the competing ledgers are reconciled.

The audit verdict is asymmetric:

- the written `CLAUDE/T11` interface supplies the arbitrary-full-block hypothesis used by `L-9302` and `T-9302`, pending independent proof review;
- the displayed `CLAUDE/T12` proof mechanism is not uniform in frequencies divisible by `3`, so `T-9303` replaces that dependency rather than silently strengthening it.