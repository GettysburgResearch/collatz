# Claim inventory — centered forced-tail PDR

| ID | Type | Status | Short statement | Dependencies |
|---|---|---|---|---|
| `D-8701` | Definition/construction | `PROPOSED` | Exact centered forced-tail map and base-64 carry transducer | verified centered interfaces from PR #37 |
| `L-8701` | Lemma | `PROPOSED` | `B+4e mod 17` is invariant; every positive legal step grows; carry is at most 17 | `D-8701` |
| `L-8702` | Lemma | `PROPOSED` | Exact affine first-height-crossing atlas; every legal crossing survivor renews within 18 steps | `D-8701`, `L-8701` |
| `T-8701` | Theorem | `PROPOSED` | The fixed-precision existential PDR kernel is exactly the binary de Bruijn cylinder graph | `D-8701`; cylinder algebra |
| `R-8701` | Refutation | `PROPOSED` | A fixed-modulus modular lasso is not an ordinary positive witness | `T-8701` |
| `Q-8701` | Open construction | `IDEA` | Add a proof-carrying top-boundary/height coordinate and construct or exclude an ordinary infinite path | `D-8701`--`R-8701` |
| `O-8701` | Observation | `EMPIRICAL` | No seed `B<=10^6` survives more than four forced steps | `X-8701` |
| `X-8701` | Experiment | `EMPIRICAL` | Independent PDR/de Bruijn/carry/seed audit | standard-library exact arithmetic |
| `X-8702` | Experiment | `EMPIRICAL` | Independent finite arithmetic audit of PR #33's Evertse closure interfaces | standard-library exact arithmetic |
| `X-8703` | Experiment | `EMPIRICAL` | Exact streamed height-renewal atlas at `H=64^18`, all binary words through first crossings `t<=18` | `L-8702`; standard-library exact arithmetic |

## Status boundary

- `T-8701` and `R-8701` are uniform mathematical statements; their finite experiments are only replay/counterexample diagnostics.
- `L-8702` has a uniform elementary proof in its claim file but remains `PROPOSED` pending independent review. Its `X-8703` canonical counts are finite computation only.
- `O-8701` is bounded evidence and has no universal implication.
- No positive ordinary seed, `K-####` candidate, Collatz cycle, or divergent Collatz initialization is asserted.
- PR #33 claim statuses are not changed in this namespace; the separate review report recommends promotions within its exact frozen scope.
