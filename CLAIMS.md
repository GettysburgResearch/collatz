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
| O-0007 | Observation | Four-branch `2048 -> 2187` chart at the negative cycle phase `-136` | PROPOSED | `claims/observations/O-0007-negative-136-cycle-chart.md` | L-0001, L-0003, T-0002, T-0008, T-0010, X-0007 |
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
| Q-0001 | Open question | Finite-boundary regeneration | IDEA | `OPEN_PROBLEMS.md` | T-0002--T-0020 |
| Q-0002 | Resolved question | Analytic collision-fiber growth | PROPOSED RESOLUTION | `OPEN_PROBLEMS.md` | T-0005 |
| Q-0003 | Open question | Carry grammar for the width-three chart | IDEA | `OPEN_PROBLEMS.md` | O-0002, L-0004 |
| Q-0004 | Open question | Multi-chart transition groupoid | IDEA | `OPEN_PROBLEMS.md` | T-0002, T-0008, T-0009, T-0013--T-0020 |
| Q-0005 | Open question | Finite versus adic closure criterion | IDEA | `OPEN_PROBLEMS.md` | T-0003, T-0008, T-0016--T-0020 |
| Q-0006 | Open question | Independent verification | IDEA | `OPEN_PROBLEMS.md` | all above |
| Q-0007 | Open question | Vertical macro-tile closure | IDEA | `OPEN_PROBLEMS.md` | L-0004, T-0003, T-0009, T-0018, T-0020 |
| Q-0008 | Open question | Parameterized `S`-unit skeleton schemas | IDEA | `OPEN_PROBLEMS.md` | T-0004, T-0008 |
| Q-0009 | Open question | Structured collision codes and closure-quality geometry | PARTIAL | `OPEN_PROBLEMS.md` | L-0006, T-0005--T-0007 |
| Q-0010 | Resolved question | Growing complete dyadic projection | PROPOSED RESOLUTION | `OPEN_PROBLEMS.md` | L-0009, L-0010, T-0007 |
| Q-0011 | Open question | Convert dyadic correction freedom into vertical closure | IDEA | `OPEN_PROBLEMS.md` | T-0004, T-0007, T-0010 |
| Q-0012 | Open question | Infinite negative-template renewal code beyond finite regular collapse | NARROWED IDEA | `OPEN_PROBLEMS.md` | T-0008, T-0009, T-0014--T-0020 |
| Q-0013 | Open question | Macroscopic aspect-ratio collision systems | IDEA | `OPEN_PROBLEMS.md` | T-0010, L-0011, O-0006, O-0007 |
| Q-0014 | Open question | Finite phase plus cycle-padding stack closure | IDEA | `OPEN_PROBLEMS.md` | T-0014, T-0015, O-0008, T-0017--T-0020 |
| Q-0015 | Open question | Pressure-positive ordinary survivor language | IDEA | `OPEN_PROBLEMS.md` | T-0013, T-0016--T-0020 |
| Q-0016 | Open question | Multi-mismatch complement automaton | IDEA | `OPEN_PROBLEMS.md` | T-0014, T-0015, O-0008, L-0013 |
| Q-0017 | Open question | Arithmetic approximation to the phase escape transform | IDEA | `OPEN_PROBLEMS.md` | L-0013, T-0017--T-0020 |
| Q-0018 | Open question | Marked ordinary-spine rewrite grammar | NARROWED IDEA | `OPEN_PROBLEMS.md` | L-0014, T-0018--T-0020 |
| Q-0019 | Open question | Counter-stack marked sanctuary beyond regular collapse | IDEA / PRIMARY | `OPEN_PROBLEMS.md` | T-0015, T-0018, T-0020 |

## Relationship among the latest results

- `L-0014` identifies the physical Collatz state with the length of a finite interval.
- `T-0018` realizes the auxiliary phase pressure as an ordered particle completion with one distinguished ordinary spine.
- `T-0019` separates unmarked population likelihood from the fully marked ordinary lineage.
- PR #13 imports the regular-transduction, closure, safe-kernel, and short-witness infrastructure; PR #12 implements the exact sanctuary verifier.
- `L-0015` proves that regular finite endpoint/population descriptions project to regular ordinary marker languages.
- `T-0020` proves that finite phases and fixed regular Collatz blocks compile to a one-step regular sanctuary.
- The route is genuinely new only when it uses an unbounded counter/stack, variable block lengths, or a nonregular ordinary survivor.

## Status note

`PROPOSED` means complete-looking but not independently reviewed. No claim here resolves the Collatz conjecture.
