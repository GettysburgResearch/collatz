# Claim inventory — residue-cylinder dichotomy

This namespaced inventory reserves `97xx` for issue #31. It is not a competing
root `CLAIMS.md`.

| ID | Kind | Title | Status | File | Dependencies |
|---|---|---|---|---|---|
| `D-9701` | Definition | Dyadic boundary tower-cylinder class | PROPOSED | `definitions/D-9701-dyadic-boundary-tower-class.md` | PR3 `L-0016`, `L-0017` interfaces |
| `L-9701` | Lemma | Exact nested cylinders and residue-block recurrence | PROPOSED | `claims/L-9701-cylinder-block-recurrence.md` | self-contained odd-affine algebra |
| `T-9701` | Theorem | Finite-trap contraction forces nonstabilization | PROPOSED | `claims/T-9701-finite-trap-nonstabilization.md` | `L-9701` |
| `T-9702` | Theorem | No ordinary integer in any dyadic boundary tower directive | PROPOSED | `claims/T-9702-dyadic-boundary-tower-exclusion.md` | `D-9701`, `L-9701`, `T-9701` |
| `Q-9701` | Open question | Transfer to the composed 256-transition stage zipper | IDEA | `claims/Q-9701-supercritical-stage-transfer.md` | PR3 `T-0024`, `T-0026`, `T-0027` |
| `X-9701` | Experiment | Exact cylinders plus independent physical replay | EMPIRICAL / EXACT FINITE CHECK | `experiments/X-9701-dyadic-boundary-cylinders/` | `D-9701`--`T-9702` |

## Status boundary

`PROPOSED` means complete-looking but not independently reviewed. `X-9701`
checks exact finite instances and proof interfaces; it is not a proof of an
infinite theorem.

The packet makes no candidate claim and does not promote any claim from PR #3,
PR #13, PR #16, PR #19, PR #20, or issue #21.
