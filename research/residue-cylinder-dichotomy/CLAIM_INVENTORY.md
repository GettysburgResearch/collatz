# Claim inventory — residue-cylinder dichotomy

This namespaced inventory reserves `97xx` for issue #31. It is not a competing
root `CLAIMS.md`.

| ID | Kind | Title | Status | File | Dependencies |
|---|---|---|---|---|---|
| `D-9701` | Definition | Dyadic boundary tower-cylinder class | PROPOSED | `definitions/D-9701-dyadic-boundary-tower-class.md` | PR3 `L-0016`, `L-0017` interfaces |
| `L-9701` | Lemma | Exact nested cylinders and residue-block recurrence | PROPOSED | `claims/L-9701-cylinder-block-recurrence.md` | self-contained odd-affine algebra |
| `T-9701` | Theorem | Finite-trap contraction forces nonstabilization | PROPOSED | `claims/T-9701-finite-trap-nonstabilization.md` | `L-9701` |
| `T-9702` | Theorem | No ordinary integer in any dyadic boundary tower directive | PROPOSED | `claims/T-9702-dyadic-boundary-tower-exclusion.md` | `D-9701`, `L-9701`, `T-9701` |
| `Q-9701` | Open question | Transfer to the composed 256-transition stage zipper | IDEA / NARROWED BY `T-9703` | `claims/Q-9701-supercritical-stage-transfer.md` | PR3 `T-0024`, `T-0026`, `T-0027` |
| `X-9701` | Experiment | Exact cylinders plus independent physical replay | EMPIRICAL / EXACT FINITE CHECK | `experiments/X-9701-dyadic-boundary-cylinders/` | `D-9701`--`T-9702` |
| `L-9702` | Lemma | Canonical composite cap lies below the full odd multiplier | PROPOSED | `claims/L-9702-canonical-composite-cap.md` | elementary canonical-tile algebra |
| `T-9703` | Theorem | Corrected 256-stage ordinary quotient is eventually exhausted | PROPOSED | `claims/T-9703-stage-quotient-exhaustion.md` | `L-9702`, PR3 `T-0027` interface |
| `Q-9702` | Open question | Exclude or construct an infinite cap-correction chain | IDEA / PRIMARY | `claims/Q-9702-cap-correction-chain.md` | `T-9703`, PR3 `T-0025`, `T-0027`, `T-0030` interfaces |
| `X-9702` | Experiment | Exact composite-cap and stage-quotient exhaustion checks | EMPIRICAL / EXACT FINITE CHECK | `experiments/X-9702-stage-quotient-exhaustion/` | `L-9702`, `T-9703` |

## Relationship between the two theorem stages

- `T-9702` proves complete nonstabilization for the direct dyadic-boundary
  connector class.
- `T-9703` reaches the genuinely supercritical composed 256-transition class but
  proves a structural reduction rather than nonexistence: every ordinary tail
  must eventually satisfy `Y_m=0` and `S_m=R_(m+1)`.
- `Q-9702` is the remaining all-directive dichotomy at the composed-stage level.

## Status boundary

`PROPOSED` means complete-looking but not independently reviewed. `X-9701` and
`X-9702` check exact finite instances and proof interfaces; neither is a proof
of an infinite theorem.

The packet makes no candidate claim and does not promote any claim from PR #3,
PR #13, PR #16, PR #19, PR #20, PR #32, or issue #21.
