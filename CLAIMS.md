# Claim ledger

Last updated: 2026-07-21  
All mathematical claims in this initial contribution await independent review.

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
| Q-0001 | Open question | Finite-word regeneration | IDEA | `OPEN_PROBLEMS.md` | T-0001 |
| Q-0002 | Open question | Collision-bundle growth | IDEA | `OPEN_PROBLEMS.md` | X-0001 |
| Q-0003 | Open question | Carry grammar for the width-three chart | IDEA | `OPEN_PROBLEMS.md` | O-0002 |
| Q-0004 | Open question | Multi-chart transition groupoid | IDEA | `OPEN_PROBLEMS.md` | O-0001, O-0002, O-0003 |
| Q-0005 | Open question | Finite versus adic closure criterion | IDEA | `OPEN_PROBLEMS.md` | none |
| Q-0006 | Open question | Independent verification of first contribution | IDEA | `OPEN_PROBLEMS.md` | all above |

## Status note

`PROPOSED` here means that a complete-looking proof or exact derivation has been submitted but has not yet received the independent review required by the repository protocol. It is not a claim of community acceptance or resolution of the Collatz conjecture.
