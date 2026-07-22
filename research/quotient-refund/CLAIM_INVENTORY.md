# Claim inventory — linear quotient refund

This isolated `85xx` namespace belongs to issue #43. It does not edit any canonical root ledger.

| ID | Kind | Title | Status | Dependencies |
|---|---|---|---|---|
| `D-8501` | Definition | Linear-height phase-34 connector-refund class | PROPOSED | PR3 `L-0016`, `L-0031` |
| `L-8501` | Lemma | Every fixed linear stage width eventually refunds the next radix | PROPOSED | `D-8501`, PR3 scaled-tail identity |
| `L-8502` | Lemma | Ordinary inverse carry and six-bit connector normal form | PROPOSED | `D-8501` |
| `T-8501` | Theorem | Deterministic expanding one-counter counterexample criterion | PROPOSED | `L-8501`, `L-8502` |
| `T-8502` | Theorem | Quadratic cylinder pressure and zero-dimensional completion set | PROPOSED | `D-8501` |
| `T-8503` | Theorem | Eventual periods through 58 are irrational and nonordinary | PROPOSED / SOURCE-DEPENDENT | Väänänen–Wallisser 1991 |
| `Q-8501` | Open question | One forever-defined ordinary residual | OPEN | `T-8501` |
| `X-8501` | Experiment | Exact refund, carry, decoder, and cutoff audit | EMPIRICAL | all elementary interfaces above |

## Logical chain

```text
PR3 physical tower identity
  -> D-8501 exact local residual system
  -> L-8502 causal inverse/cell compiler
  -> T-8501 deterministic next type + automatic doubling growth
  -> Q-8501 one finite forever-defined seed
  -> explicit positive unbounded Collatz orbit.
```

`L-8501` proves that quotient refund already begins at width one. `T-8502` and `T-8503` are construction filters: finite symbolic abundance and short periodic controllers do not provide the missing ordinary seed.
