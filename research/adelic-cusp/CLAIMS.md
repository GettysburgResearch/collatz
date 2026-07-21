# Claim ledger: adelic cusp Fourier packet

This is an isolated `93xx` namespace for issue #15. It is not a replacement for any canonical root ledger and does not renumber claims on unmerged branches.

| ID | Type | Status | Short title | Dependencies |
|---|---|---|---|---|
| `D-9301` | Definition/construction | `PROPOSED` | Stationary survivor measure | elementary 2-adic convergence |
| `L-9301` | Lemma | `PROPOSED` | Moving-character Fourier identity | `D-9301`; issue-#4 notation crosswalk |
| `L-9302` | Lemma | `PROPOSED` | Weighted shell tail from block means | elementary interval decomposition |
| `T-9301` | Conditional theorem | `PROPOSED` | Polynomial-window reduction to EQ | `L-9301`, `L-9302`; branch-qualified frequency block mean |
| `T-9302` | Conditional theorem | `PROPOSED` | Density-one full EQ from two-axis means | `L-9302`; branch-qualified frequency/depth block means |
| `D-9302` | Definition/construction | `PROPOSED` | Adelic natural extension and integer section | `D-9301`; elementary quotient algebra |
| `C-9301` | Conjecture | `IDEA` | Logarithmic cusp scattering | `L-9301`, `T-9301` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |

## Status boundary

- Every complete-looking argument authored in this packet enters as `PROPOSED` pending independent review.
- `T-9301` and `T-9302` prove implications under explicitly stated block-mean hypotheses. They do not independently establish the branch-qualified issue-#4 inputs.
- `C-9301` and `Q-9301` are open. No positive integer, divergent orbit, cycle, or Collatz counterexample is claimed.

## Branch crosswalk

The notation `CLAUDE/T11` and `CLAUDE/T12` below refers descriptively to the block-frequency and block-depth results called Theorems 11 and 12 in `EQ.md` on `claude/collatz-migration-math-osr370`. The literature branch uses different stable namespacing. An integrator must preserve this branch qualification until the competing ledgers are reconciled.
