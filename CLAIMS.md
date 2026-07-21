# Claim ledger

Last updated: 2026-07-21  
All mathematical claims on the active research branch await independent review.

| ID | Type | Title | Status | File | Dependencies |
|---|---|---|---|---|---|
| D-0001 | Definition | Shortcut map, parity words, collision and digit conventions | PROPOSED | `NOTATION.md` | none |
| L-0001 | Lemma | Parity-affine formula for a finite shortcut-Collatz word | PROPOSED | `claims/lemmas/L-0001-parity-affine-formula.md` | D-0001 |
| T-0001 | Theorem | Consecutive collision bundles induce partial radix maps | PROPOSED | `claims/theorems/T-0001-collision-bundle-conjugacy.md` | L-0001 |
| O-0001 | Observation | Two-branch supercritical `64 -> 81` chart | PROPOSED | `claims/observations/O-0001-64-to-81-pair-chart.md` | L-0001, T-0001 |
| O-0002 | Observation | Three-branch supercritical `512 -> 729` chart | PROPOSED | `claims/observations/O-0002-512-to-729-triple-chart.md` | L-0001, T-0001 |
| O-0003 | Observation | Six-branch supercritical length-17 chart | PROPOSED | `claims/observations/O-0003-131072-to-177147-six-chart.md` | L-0001, T-0001, X-0001 |
| L-0002 | Lemma | Nine-column carry cycle and finite-horizon stack amplifier | PROPOSED | `claims/lemmas/L-0002-nine-column-stack-amplifier.md` | O-0001 |
| X-0001 | Experiment | Exact enumeration of supercritical consecutive collision bundles through length 17 | EMPIRICAL | `experiments/X-0001-collision-enumeration/` | D-0001 |
| T-0002 | Theorem | Arbitrary finite collision fibers induce partial radix maps | PROPOSED | `claims/theorems/T-0002-collision-fiber-conjugacy.md` | D-0001, L-0001 |
| L-0003 | Lemma | Exact binary recursion for every collision fiber | PROPOSED | `claims/lemmas/L-0003-fiber-recursion.md` | D-0001, L-0001 |
| L-0004 | Lemma | Carry-cycle pumping and universal zero-output stack amplifiers | PROPOSED | `claims/lemmas/L-0004-carry-cycle-pumping.md` | D-0001, T-0002 |
| T-0003 | Theorem | Dual adic/real coding, boundary-flow law, and aperiodicity obstruction | PROPOSED | `claims/theorems/T-0003-adic-real-coding.md` | D-0001, T-0002 |
| T-0004 | Theorem | Exact run-length skeleton and `S`-unit carry-chain equivalence | PROPOSED | `claims/theorems/T-0004-run-length-skeleton.md` | D-0001, T-0002 |
| O-0004 | Observation | Eighteen-branch sparse `4194304 -> 4782969` chart | PROPOSED | `claims/observations/O-0004-4194304-to-4782969-eighteen-fiber.md` | L-0001, L-0003, T-0002, X-0002 |
| X-0002 | Experiment | Complete supercritical collision fibers through length 22 | EMPIRICAL | `experiments/X-0002-collision-fibers/` | D-0001, L-0003 |
| Q-0001 | Open question | Finite-boundary regeneration | IDEA | `OPEN_PROBLEMS.md` | T-0002, T-0003, T-0004 |
| Q-0002 | Open question | Analytic collision-fiber growth | IDEA | `OPEN_PROBLEMS.md` | L-0003, X-0002 |
| Q-0003 | Open question | Carry grammar for the width-three chart | IDEA | `OPEN_PROBLEMS.md` | O-0002, L-0004 |
| Q-0004 | Open question | Multi-chart transition groupoid | IDEA | `OPEN_PROBLEMS.md` | T-0002, O-0001--O-0004 |
| Q-0005 | Open question | Finite versus adic closure criterion | IDEA | `OPEN_PROBLEMS.md` | T-0003 |
| Q-0006 | Open question | Independent verification of the active contribution | IDEA | `OPEN_PROBLEMS.md` | all above |
| Q-0007 | Open question | Vertical macro-tile closure | IDEA | `OPEN_PROBLEMS.md` | L-0004, T-0003 |
| Q-0008 | Open question | Parameterized `S`-unit skeleton schemas | IDEA | `OPEN_PROBLEMS.md` | T-0004 |

## Relationship among the main finite theorems

- `T-0001` is the initial-interval special case of `T-0002`.
- `L-0002` is the `(M,N,D,j,k)=(64,81,{0,1},1,9)` special case of `L-0004`.
- `L-0003` constructs the complete finite collision atlas on which `T-0002` can be applied.
- `T-0003` and `T-0004` constrain the global form of any hypothetical infinite induced orbit.

## Status note

`PROPOSED` means that a complete-looking proof or exact derivation has been
submitted but has not yet received the independent review required by the
repository protocol. It is not a claim of community acceptance or a resolution
of the Collatz conjecture.
