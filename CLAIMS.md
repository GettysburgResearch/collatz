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
| O-0004 | Observation | Eighteen-branch sparse depth-22 chart | PROPOSED | `claims/observations/O-0004-4194304-to-4782969-eighteen-fiber.md` | L-0001, L-0003, T-0002, X-0002 |
| X-0002 | Experiment | Complete supercritical collision fibers through length 22 | EMPIRICAL | `experiments/X-0002-collision-fibers/` | D-0001, L-0003 |
| L-0005 | Lemma | Parity signatures and exact inverse reconstruction | PROPOSED | `claims/lemmas/L-0005-parity-signature-inversion.md` | D-0001, L-0001 |
| L-0006 | Lemma | 3-adic collision-code composition and precision surplus | PROPOSED | `claims/lemmas/L-0006-collision-code-composition.md` | D-0001, L-0005 |
| T-0005 | Theorem | Exponentially large mildly supercritical collision fibers exist | PROPOSED | `claims/theorems/T-0005-signature-tail-amplification.md` | L-0001, L-0005, T-0002 |
| O-0005 | Observation | A 339-branch mildly supercritical depth-44 chart | PROPOSED | `claims/observations/O-0005-339-branch-signature-chart.md` | L-0005, T-0002, T-0005, X-0003 |
| X-0003 | Experiment | Equal-signature classes and odd-tail collision charts | EMPIRICAL | `experiments/X-0003-signature-tail-fibers/` | L-0005, L-0006, T-0005 |
| L-0007 | Lemma | Exact tensor law for inverse-root offset geometry | PROPOSED | `claims/lemmas/L-0007-offset-tensor-law.md` | L-0005, L-0006 |
| L-0008 | Lemma | Arbitrary-precision two-word atomic collision codes | PROPOSED | `claims/lemmas/L-0008-high-precision-atomic-codes.md` | L-0005, L-0006 |
| T-0006 | Theorem | Geometry-preserving collision-code amplification | PROPOSED | `claims/theorems/T-0006-geometry-preserving-amplification.md` | L-0005--L-0008, T-0005 |
| X-0004 | Experiment | Exact offset-tensor and geometry-preservation checks | EMPIRICAL | `experiments/X-0004-offset-tensor/` | L-0007, L-0008, T-0006 |
| L-0009 | Lemma | One-hot suffixes correct arbitrary finite signatures | PROPOSED | `claims/lemmas/L-0009-one-hot-signature-correction.md` | L-0001, L-0005, L-0006 |
| L-0010 | Lemma | Fixed-weight prefixes biject onto every dyadic residue | PROPOSED | `claims/lemmas/L-0010-dyadic-prefix-bijection.md` | L-0001 |
| T-0007 | Theorem | Supercritical fibers with complete projection modulo `2^b` | PROPOSED | `claims/theorems/T-0007-complete-dyadic-projection.md` | L-0005, L-0009, L-0010, T-0002, T-0005 |
| X-0005 | Experiment | Exact complete-dyadic-projection construction through `b=5` | EMPIRICAL | `experiments/X-0005-dyadic-projection/` | L-0009, L-0010, T-0007 |
| Q-0001 | Open question | Finite-boundary regeneration | IDEA | `OPEN_PROBLEMS.md` | T-0002, T-0003, T-0004 |
| Q-0002 | Resolved question | Analytic collision-fiber growth | PROPOSED RESOLUTION | `OPEN_PROBLEMS.md` | T-0005 |
| Q-0003 | Open question | Carry grammar for the width-three chart | IDEA | `OPEN_PROBLEMS.md` | O-0002, L-0004 |
| Q-0004 | Open question | Multi-chart transition groupoid | IDEA | `OPEN_PROBLEMS.md` | T-0002, O-0001--O-0005 |
| Q-0005 | Open question | Finite versus adic closure criterion | IDEA | `OPEN_PROBLEMS.md` | T-0003 |
| Q-0006 | Open question | Independent verification | IDEA | `OPEN_PROBLEMS.md` | all above |
| Q-0007 | Open question | Vertical macro-tile closure | IDEA | `OPEN_PROBLEMS.md` | L-0004, T-0003 |
| Q-0008 | Open question | Parameterized `S`-unit skeleton schemas | IDEA | `OPEN_PROBLEMS.md` | T-0004 |
| Q-0009 | Open question | Structured collision codes and closure-quality geometry | IDEA | `OPEN_PROBLEMS.md` | L-0006, T-0005, O-0005, T-0006 |
| Q-0010 | Resolved question | Growing complete dyadic projection | PROPOSED RESOLUTION | `OPEN_PROBLEMS.md` | L-0009, L-0010, T-0007 |
| Q-0011 | Open question | Convert dyadic correction freedom into vertical closure | IDEA | `OPEN_PROBLEMS.md` | T-0004, T-0007 |

## Relationship among the latest results

- `L-0009` is a universal finite signature-completion mechanism.
- `L-0010` constructs fixed-weight prefixes carrying every residue modulo `2^b`.
- `T-0007` combines them with a finite odd drift tail to produce mildly supercritical collision fibers with complete projection modulo arbitrarily large powers of two.
- The remaining problem is to convert this modular correction freedom into a uniform finite-boundary relay, not merely one-step solvability.

## Status note

`PROPOSED` means complete-looking but not independently reviewed. No claim here resolves the Collatz conjecture.
