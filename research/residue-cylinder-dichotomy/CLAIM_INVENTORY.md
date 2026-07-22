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
| `X-9701` | Experiment | Exact cylinders plus independent physical replay | EMPIRICAL | `experiments/X-9701-dyadic-boundary-cylinders/` | `D-9701`--`T-9702` |
| `L-9702` | Lemma | Canonical composite cap lies below the full odd multiplier | PROPOSED | `claims/L-9702-canonical-composite-cap.md` | elementary canonical-tile algebra |
| `T-9703` | Theorem | Corrected 256-stage ordinary quotient is eventually exhausted | PROPOSED | `claims/T-9703-stage-quotient-exhaustion.md` | `L-9702`, PR3 `T-0027` interface |
| `Q-9702` | Open question | Exclude or construct an infinite cap-correction chain | IDEA | `claims/Q-9702-cap-correction-chain.md` | `T-9703`, `T-9704`, PR3 `T-0025`, `T-0027`, `T-0030` interfaces |
| `X-9702` | Experiment | Exact composite-cap and stage-quotient exhaustion checks | EMPIRICAL | `experiments/X-9702-stage-quotient-exhaustion/` | `L-9702`, `T-9703` |
| `L-9703` | Lemma | Type-uniform normalized stage-offset bound | PROPOSED | `claims/L-9703-normalized-stage-offset.md` | PR3 local residual interface; elementary bounds |
| `T-9704` | Theorem | Cap-chain ordinary height uses less than one part in 275 of cylinder precision | PROPOSED | `claims/T-9704-cap-chain-height-collapse.md` | `L-9703`, PR3 stage exponents |
| `X-9703` | Experiment | Exact expanding-offset and cap-chain height checks | EMPIRICAL | `experiments/X-9703-cap-chain-height/` | `L-9703`, `T-9704` |

## Relationship among the theorem stages

- `T-9702` proves complete nonstabilization for the direct dyadic-boundary
  connector class.
- `T-9703` reaches the genuinely supercritical composed 256-transition class and
  proves every ordinary tail must eventually satisfy `Y_m=0` and
  `S_m=R_(m+1)`.
- `T-9704` proves that any such cap-correction tail has ordinary representative
  height asymptotically below `D_m/275`, where `D_m` is the complete cylinder
  precision.
- `Q-9702` is the remaining all-directive dichotomy at the composed-stage level.

`Q-9701` is preserved as the historical broad transfer question; `T-9703` and
`T-9704` provide its current narrowing.

## Status boundary

`PROPOSED` means complete-looking but not independently reviewed. `EMPIRICAL`
experiments check exact finite instances and proof interfaces; they do not prove
an infinite theorem.

The packet makes no candidate claim and does not promote any claim from PR #3,
PR #13, PR #16, PR #19, PR #20, PR #32, or issue #21.
