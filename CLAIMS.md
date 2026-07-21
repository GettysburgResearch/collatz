# Claim ledger

Last updated: 2026-07-22  
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
| X-0002 | Experiment | Complete supercritical collision fibers through depth 22 | EMPIRICAL | `experiments/X-0002-collision-fibers/` | D-0001, L-0003 |
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
| T-0008 | Theorem | Every collision chart is a negative-template signed rational-base return system | PROPOSED | `claims/theorems/T-0008-negative-shadow-rational-base.md` | D-0001, L-0001, T-0002 |
| T-0009 | Theorem | Renewal-code counterexample criterion and finite complete-code obstruction | PROPOSED | `claims/theorems/T-0009-renewal-code-criterion.md` | D-0001, L-0001, T-0008 |
| T-0010 | Theorem | Fractional-window confinement and normalized aspect ratio | PROPOSED | `claims/theorems/T-0010-fractional-window-aspect-ratio.md` | T-0008 |
| L-0011 | Lemma | Common odd-tail aspect-ratio tax | PROPOSED | `claims/lemmas/L-0011-odd-tail-aspect-ratio-tax.md` | L-0005, T-0005, T-0010 |
| L-0012 | Lemma | Inverse signatures are exactly negative return targets | PROPOSED | `claims/lemmas/L-0012-signatures-are-negative-targets.md` | L-0001, L-0005, T-0008 |
| T-0013 | Theorem | Multi-target negative-return criterion and phase-potential expansion | PROPOSED | `claims/theorems/T-0013-graph-directed-return-criterion.md` | D-0001, L-0001, T-0009 |
| O-0006 | Observation | Exact aspect-ratio audit of the recorded collision charts | EMPIRICAL | `claims/observations/O-0006-recorded-chart-aspect-ratios.md` | O-0001--O-0005, T-0010, L-0011, X-0006 |
| O-0007 | Observation | Four-branch `2048 -> 2187` chart at negative phase `-136` | PROPOSED | `claims/observations/O-0007-negative-136-cycle-chart.md` | L-0001, L-0003, T-0002, T-0008, T-0010, X-0007 |
| X-0006 | Experiment | Negative-shadow, signature-target, renewal, and aspect-ratio checks | EMPIRICAL | `experiments/X-0006-shadow-return/` | T-0008--T-0010, L-0011--L-0012 |
| X-0007 | Experiment | Exact normalized-aspect census through depth 22 | EMPIRICAL | `experiments/X-0007-aspect-census/` | L-0003, T-0010, O-0007 |
| T-0014 | Theorem | Exact synchronous negative-phase coupling and valuation acceleration | PROPOSED | `claims/theorems/T-0014-synchronous-negative-phase-coupling.md` | D-0001, T-0008 |
| T-0015 | Theorem | Cycle-padded one-mismatch return towers | PROPOSED | `claims/theorems/T-0015-cycle-padded-mismatch-towers.md` | T-0013, T-0014 |
| T-0016 | Theorem | Collatz–Kraft martingale and renewal-code pressure | PROPOSED | `claims/theorems/T-0016-collatz-kraft-martingale.md` | D-0001, T-0009, T-0013 |
| O-0008 | Observation | Complement-basin atlas and padded towers of the negative eleven-cycle | PROPOSED | `claims/observations/O-0008-negative-cycle-complement-atlas.md` | T-0014, T-0015, O-0007, X-0008 |
| X-0008 | Experiment | Negative-cycle coupling, padded returns, and Kraft checks | EMPIRICAL | `experiments/X-0008-cycle-coupling-kraft/` | T-0014--T-0016, O-0008 |
| L-0013 | Lemma | Physical parity drives the rounded phase pair | PROPOSED | `claims/lemmas/L-0013-rounded-physical-phase.md` | D-0001, T-0014 |
| T-0017 | Theorem | Phase–Kraft martingale, complete-graph rigidity, and escape transform | PROPOSED | `claims/theorems/T-0017-phase-kraft-escape-transform.md` | L-0013, T-0013, T-0016 |
| X-0009 | Experiment | Rounded phase, phase–Kraft, and escape-transform checks | EMPIRICAL | `experiments/X-0009-phase-kraft-escape/` | L-0013, T-0017 |
| L-0014 | Lemma | Exact finite-interval renormalization and gauge freedom | PROPOSED | `claims/lemmas/L-0014-finite-interval-gauge.md` | D-0001, L-0013 |
| T-0018 | Theorem | Critical ordered-particle completion and ordinary marked spine | PROPOSED | `claims/theorems/T-0018-critical-particle-completion.md` | L-0013, T-0017 |
| T-0019 | Theorem | Exact ordinary-spine escape and growth likelihood identities | PROPOSED | `claims/theorems/T-0019-ordinary-spine-likelihood.md` | L-0001, T-0016--T-0018 |
| X-0010 | Experiment | Finite interval, particle completion, and ordinary-spine checks | EMPIRICAL | `experiments/X-0010-interval-particle-spine/` | L-0014, T-0018, T-0019 |
| L-0015 | Lemma | Regular projection of finite marked intervals and particles | PROPOSED | `claims/lemmas/L-0015-regular-interval-projection.md` | L-0014, T-0018 |
| T-0020 | Theorem | Finite-phase regular marked grammars collapse to regular sanctuaries | PROPOSED | `claims/theorems/T-0020-regular-marked-grammar-collapse.md` | L-0015, L-0014, T-0018 |
| X-0011 | Experiment | Exact regular marked-grammar collapse bridge | EMPIRICAL | `experiments/X-0011-regular-marked-collapse/` | L-0015, T-0020 |
| L-0016 | Lemma | Cycle-padded towers are exact binary-to-ternary tail replacements | PROPOSED | `claims/lemmas/L-0016-tower-tail-replacement.md` | T-0015 |
| L-0017 | Lemma | Universal canonical mixed-radix connector tiles | PROPOSED | `claims/lemmas/L-0017-mixed-radix-connector.md` | L-0016 |
| L-0018 | Lemma | Growing inverse-power prefixes require unbounded memory | PROPOSED | `claims/lemmas/L-0018-growing-inverse-prefix.md` | L-0017 |
| T-0021 | Theorem | Bounded-tail affine counter lanes close at only finitely many heights | PROPOSED | `claims/theorems/T-0021-bounded-tail-counter-obstruction.md` | L-0016, L-0017, LIT-KTHM-0008 |
| L-0019 | Lemma | Nonlinear Hensel escalator for normalized connector prefixes | PROPOSED | `claims/lemmas/L-0019-hensel-escalator.md` | L-0016--L-0018 |
| T-0022 | Theorem | One-connector Hensel prefix and immediate-tail budget window | PROPOSED / PRECURSOR | `claims/theorems/T-0022-hensel-budget-window.md` | L-0017, L-0019 |
| L-0020 | Lemma | Exact 128-step one-connector Hensel staging | PROPOSED / PRECURSOR | `claims/lemmas/L-0020-dyadic-hensel-staging.md` | L-0019, T-0022 |
| L-0021 | Lemma | Seven-bit odometer law in the 128-step precursor stage | PROPOSED / PRECURSOR | `claims/lemmas/L-0021-binary-odometer-prefix-law.md` | L-0019, L-0020 |
| L-0022 | Lemma | Connector seeds are one inverse-prefix stream plus a bounded target digit | PROPOSED | `claims/lemmas/L-0022-connector-truncation-normal-form.md` | L-0016, L-0017, L-0019 |
| O-0009 | Observation | Explicit periodic stage-frontier streams at phase `-34` | PROPOSED | `claims/observations/O-0009-phase34-stage-prefix-streams.md` | L-0016, L-0021, L-0022, X-0012 |
| L-0023 | Lemma | Quadratic Hensel recurrence for the moving stage bulk | PROPOSED | `claims/lemmas/L-0023-quadratic-stage-defect.md` | L-0021, L-0022, O-0009 |
| T-0023 | Theorem | Corrected two-connector residual-stack budget | PROPOSED | `claims/theorems/T-0023-two-connector-stack-budget.md` | L-0017, L-0019, T-0022 |
| L-0024 | Lemma | Exact 256-step residual-stack stage and eight-bit odometer | PROPOSED | `claims/lemmas/L-0024-dyadic-256-stage.md` | L-0019, T-0023 |
| T-0024 | Theorem | Full 256-step stage has exponential precision surplus | PROPOSED | `claims/theorems/T-0024-stage-information-surplus.md` | T-0023, L-0024 |
| L-0025 | Lemma | Exact rational sandwich for the negative-cycle bit margin | PROPOSED | `claims/lemmas/L-0025-exact-cycle-margin-sandwich.md` | none |
| X-0012 | Experiment | Tower replacement, connector, Hensel, residual-stage, and surplus checks | EMPIRICAL | `experiments/X-0012-tower-connector-stack/` | L-0016--L-0025, T-0021--T-0024, O-0009 |
| L-0026 | Lemma | Offset Montgomery precision lifting for connector tiles | PROPOSED | `claims/lemmas/L-0026-offset-montgomery-lift.md` | L-0017, L-0022 |
| L-0027 | Lemma | Cycle-aligned Newton doubling with exact eleven-bit slack | PROPOSED | `claims/lemmas/L-0027-cycle-aligned-newton-slack.md` | L-0016, L-0024, L-0026 |
| O-0010 | Observation | Quadratic stage bulk converges to a 2-adic logarithm | PROPOSED | `claims/observations/O-0010-two-adic-logarithmic-bulk.md` | L-0023, L-0027 |
| T-0025 | Theorem | Uniform finite-word compiler for 256-stage connector control | PROPOSED | `claims/theorems/T-0025-finite-connector-prefix-compiler.md` | L-0022--L-0027, O-0009, O-0010 |
| T-0026 | Theorem | Residual Montgomery zipper criterion | PROPOSED | `claims/theorems/T-0026-residual-montgomery-zipper.md` | L-0017, L-0026, T-0023, T-0025 |
| X-0013 | Experiment | Offset Montgomery, Newton compiler, and logarithmic-bulk checks | EMPIRICAL | `experiments/X-0013-montgomery-newton-compiler/` | L-0026, L-0027, T-0025, O-0010 |
| Q-0001 | Open question | Finite-boundary regeneration | IDEA | `OPEN_PROBLEMS.md` | T-0002--T-0026 |
| Q-0002 | Resolved question | Analytic collision-fiber growth | PROPOSED RESOLUTION | `OPEN_PROBLEMS.md` | T-0005 |
| Q-0003 | Open question | Carry grammar for the width-three chart | IDEA | `OPEN_PROBLEMS.md` | O-0002, L-0004 |
| Q-0004 | Open question | Multi-chart transition groupoid | IDEA | `OPEN_PROBLEMS.md` | T-0002, T-0008, T-0009, T-0013--T-0026 |
| Q-0005 | Open question | Finite versus adic closure criterion | IDEA | `OPEN_PROBLEMS.md` | T-0003, T-0008, T-0016--T-0026 |
| Q-0006 | Open question | Independent verification | IDEA | `OPEN_PROBLEMS.md` | all above |
| Q-0007 | Open question | Vertical macro-tile closure | IDEA | `OPEN_PROBLEMS.md` | L-0004, T-0003, T-0009, T-0018, T-0020 |
| Q-0008 | Open question | Parameterized `S`-unit skeleton schemas | IDEA | `OPEN_PROBLEMS.md` | T-0004, T-0008 |
| Q-0009 | Open question | Structured collision codes and closure-quality geometry | PARTIAL | `OPEN_PROBLEMS.md` | L-0006, T-0005--T-0007 |
| Q-0010 | Resolved question | Growing complete dyadic projection | PROPOSED RESOLUTION | `OPEN_PROBLEMS.md` | L-0009, L-0010, T-0007 |
| Q-0011 | Open question | Convert dyadic correction freedom into vertical closure | IDEA | `OPEN_PROBLEMS.md` | T-0004, T-0007, T-0010 |
| Q-0012 | Open question | Infinite negative-template renewal code beyond finite regular collapse | NARROWED IDEA | `OPEN_PROBLEMS.md` | T-0008, T-0009, T-0014--T-0026 |
| Q-0013 | Open question | Macroscopic aspect-ratio collision systems | IDEA | `OPEN_PROBLEMS.md` | T-0010, L-0011, O-0006, O-0007 |
| Q-0014 | Open question | Finite phase plus cycle-padding stack closure | IDEA | `OPEN_PROBLEMS.md` | T-0014, T-0015, O-0008, T-0017--T-0026 |
| Q-0015 | Open question | Pressure-positive ordinary survivor language | IDEA | `OPEN_PROBLEMS.md` | T-0013, T-0016--T-0026 |
| Q-0016 | Open question | Multi-mismatch complement automaton | IDEA | `OPEN_PROBLEMS.md` | T-0014, T-0015, O-0008, L-0013 |
| Q-0017 | Open question | Arithmetic approximation to the phase escape transform | IDEA | `OPEN_PROBLEMS.md` | L-0013, T-0017--T-0026 |
| Q-0018 | Open question | Marked ordinary-spine rewrite grammar | NARROWED IDEA | `OPEN_PROBLEMS.md` | L-0014, T-0018--T-0026 |
| Q-0019 | Open question | Hensel counter-stack marked sanctuary beyond regular collapse | IDEA / PRIMARY | `OPEN_PROBLEMS.md` | T-0015, T-0020--T-0026 |
| Q-0020 | Open question | Route full-stage surplus into exact residual congruence | NARROWED / PRIMARY | `OPEN_PROBLEMS.md` | L-0026, L-0027, T-0024--T-0026 |
| Q-0021 | Open question | Self-feeding ordinary Montgomery quotient | IDEA / SOLE ARITHMETIC CHANNEL | `OPEN_PROBLEMS.md` | T-0025, T-0026 |

## Relationship among the latest results

- `L-0016`--`T-0024` supply exact padded tower replacements, finite connectors, corrected 256-step staging, positive residual slope, and full-stage information surplus.
- `L-0026` identifies every connector and residual divisibility equation as an offset Montgomery reduction whose quotient is the next precision-lifting state.
- `L-0027` proves the exact cycle alignment `Q_(m+1)=2Q_m-11`; Newton doubling generates the full next inverse prefix and leaves one complete eleven-bit negative-cycle block of slack.
- `O-0010` identifies the quadratic bulk limit as `-(7/4) log_2(3)` and proves exact one-bit-per-stage convergence.
- `T-0025` removes the connector word `W` as an independent infinite object: every frontier, inverse prefix, cap, and odometer word is generated from finite stage data.
- `T-0026` isolates the only uncontrolled channel as the ordinary residual zipper `psi_n + N_n y_n = rho_(n+1) + 2^(D_(n+1)) y_(n+1)`.
- The remaining load-bearing theorem is an ordinary self-feeding Montgomery quotient with one finite marked initialization. Computing the required residues is no longer the issue; physically realizing them forever is.

## Status note

`PROPOSED` means complete-looking but not independently reviewed. No claim here resolves the Collatz conjecture.
