# Claim inventory — residue-cylinder dichotomy

This namespaced inventory reserves `97xx` for issue #31. It is not a competing root `CLAIMS.md`.

| ID | Kind | Title | Status | File | Dependencies |
|---|---|---|---|---|---|
| `D-9701` | Definition | Dyadic boundary tower-cylinder class | PROPOSED | `definitions/D-9701-dyadic-boundary-tower-class.md` | PR3 `L-0016`, `L-0017` interfaces |
| `L-9701` | Lemma | Exact nested cylinders and residue-block recurrence | PROPOSED | `claims/L-9701-cylinder-block-recurrence.md` | self-contained odd-affine algebra |
| `T-9701` | Theorem | Finite-trap contraction forces nonstabilization | PROPOSED | `claims/T-9701-finite-trap-nonstabilization.md` | `L-9701` |
| `T-9702` | Theorem | No ordinary integer in any direct dyadic-boundary directive | PROPOSED | `claims/T-9702-dyadic-boundary-tower-exclusion.md` | `D-9701`, `L-9701`, `T-9701` |
| `Q-9701` | Historical question | Transfer to the composed 256-transition stage | RESOLVED NEGATIVELY BY `T-9705` | `claims/Q-9701-supercritical-stage-transfer.md` | `T-9703`--`T-9705` |
| `X-9701` | Experiment | Exact direct cylinders plus independent physical replay | EMPIRICAL | `experiments/X-9701-dyadic-boundary-cylinders/` | `D-9701`--`T-9702` |
| `L-9702` | Lemma | Canonical composite cap lies below the full odd multiplier | PROPOSED | `claims/L-9702-canonical-composite-cap.md` | elementary canonical-tile algebra |
| `T-9703` | Theorem | Corrected 256-stage nonnegative quotient is eventually exhausted | PROPOSED | `claims/T-9703-stage-quotient-exhaustion.md` | `L-9702`, PR3 `T-0027` interface |
| `Q-9702` | Historical question | Exclude or construct an infinite cap-correction chain | RESOLVED NEGATIVELY BY `T-9705` | `claims/Q-9702-cap-correction-chain.md` | `T-9704`, `L-9704`--`L-9706`, `T-9705` |
| `X-9702` | Experiment | Exact composite-cap and quotient-exhaustion checks | EMPIRICAL | `experiments/X-9702-stage-quotient-exhaustion/` | `L-9702`, `T-9703` |
| `L-9703` | Lemma | Type-uniform normalized stage-offset bound | PROPOSED | `claims/L-9703-normalized-stage-offset.md` | PR3 local residual interface; elementary bounds |
| `T-9704` | Theorem | Cap-chain height uses less than one part in 275 of cylinder precision | PROPOSED | `claims/T-9704-cap-chain-height-collapse.md` | `L-9703`, PR3 stage exponents |
| `X-9703` | Experiment | Exact expanding-offset and cap-chain height checks | EMPIRICAL | `experiments/X-9703-cap-chain-height/` | `L-9703`, `T-9704` |
| `L-9704` | Lemma | Connector-free physical coordinate and fixed 256-term `{2,3}`-unit power sum | PROPOSED | `claims/L-9704-connector-free-stage-coordinate.md` | PR3 `L-0016`, `L-0017`, `T-0027`; `T-9704`, `L-9705` for heights |
| `L-9705` | Lemma | Signed quotient extinction and cap/co-cap dichotomy | PROPOSED | `claims/L-9705-signed-quotient-dichotomy.md` | `L-9702`, `L-9703`, `T-9703`, `T-9704` |
| `L-9706` | Lemma | Evertse-admissible nondegenerate stage tuples | PROPOSED | `claims/L-9706-evertse-admissible-stage-tuples.md` | `L-9704`, `L-9705`; Evertse 1984 Corollary 1 |
| `T-9705` | Theorem | Universal ordinary exclusion for the corrected 256-stage class | PROPOSED | `claims/T-9705-full-stage-ordinary-exclusion.md` | `L-9701`--`L-9706`, `T-9703`, `T-9704` |
| `X-9704` | Experiment | Connector-free, signed quotient, and Evertse-admissibility audit | EMPIRICAL | `experiments/X-9704-connector-free-power-sum/` | `L-9704`--`L-9706`, `T-9705` proof interfaces |

## Theorem chain

```text
L-9701 exact cylinders
  -> T-9703 quotient extinction
  -> L-9703/T-9704 completion-height collapse
  -> L-9704 connector-free 258-term zero sum
  -> L-9705 signed cap/co-cap dichotomy
  -> L-9706 Evertse admissibility and distinctness
  -> T-9705 full corrected-stage ordinary exclusion.
```

`T-9705` proves side A for the complete frozen corrected-stage directive class, including signed ordinary completions. `T-9702` remains a simpler independent negative theorem for the direct connector comparison class.

## Status boundary

`PROPOSED` means complete-looking but not independently reviewed. `EMPIRICAL` experiments check exact finite interfaces; they do not prove the infinite Subspace-Theorem conclusion.

The packet makes no `K-####` candidate claim and does not promote any claim from PR #3, PR #13, PR #16, PR #19, PR #20, PR #32, PR #34, or issue #21.
