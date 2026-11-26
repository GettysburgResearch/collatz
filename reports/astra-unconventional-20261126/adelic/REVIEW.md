# Squareclass lane replay and review boundary

The research claims A1–A9 are in the [squareclass packet](../../../research/astra-unconventional-20261126/adelic/README.md), [growth and mixed-place proofs](../../../research/astra-unconventional-20261126/adelic/GROWTH.md) and [fixed-orbit character analysis](../../../research/astra-unconventional-20261126/adelic/CHARACTERS.md).

## Executed checks

The three Lean 4.34.1 files were each compiled directly from their visible source, reusing prebuilt Mathlib dependencies. The compiler reported commit `5045d0056413266e57c625dcd7c365b10e377c52`. Each command exited zero without diagnostics; the output consisted only of the requested `#print axioms` inventory. There are fifteen audited public theorems. `growth_carry` uses `propext, Quot.sound`; the other fourteen inventories are `propext, Classical.choice, Quot.sound`.

| Module | Kernel-checked content |
|---|---|
| `SquareclassDescent.lean` | Definition of the physical odd map and its clock, growth carry, forced integer square at a dependent physical growth triple, one- or three-step physical descent and eventual hit under the quantified local condition; specified dyadic-character clock lower bound and its actual-orbit prefix sum. |
| `MixedSquareGrid.lean` | A single ternary unit after denominator clearing, residue of the elementary symmetric polynomial, and strict inequality between each of the three Taylor grid numerators and the corresponding candidate square root. |
| `ShortRelations.lean` | Seven nonempty subsums of three binary selectors over thirteen positions have a member of weight at most seven. The nonzero and even hypotheses reduce its weight to 2, 4 or 6. |

`python -I -B research/astra-unconventional-20261126/adelic/check.py` and `python -I -O -B` with the same file exited zero and produced identical JSON. The controls use explicit exceptions. They cover 50,001 odd sources, 25,000 actual growth triples and 75 dependent growth triples; 70 square-to-square Pell pairs; both terminal-power controls for each of 511 parity words, with 7,172 shortcut transitions; all 5,018 selected even subsets of sizes 2, 4, 6 on two thirteen-row high-source fixtures; the three exact Taylor constants, the external-base interface integer and 10,000 dyadic inequalities. They check instances of the written identities rather than the universal quantifiers.

## Claims left in written mathematics

A1–A5 are written proofs. For A6, the seven square-subproduct alternatives in `Dependent` are the elementary integer formulation of rational squareclass dependence, and Lean proves the local-condition consumer on the literal accelerated map. For A7, the full Laurent approximation, norm bounds and complete rank-seven implication are written; two finite-index algebraic kernels are separately checked above. The finite base is Barina's published computation, not a local rerun. For A8 and A9, the harmonic clock upper bound, probability argument and all-time conclusions are written. Only the finite physical dyadic lower bound and its sum are also checked in Lean.

The operator lane independently reconstructed A8–A9. Its review checked subgroup sign domination, the common-character Hölder bound, low-window and boundary losses, geometric-grid summability and the three-character residue formula. The coordinating lane independently reconstructed the Runge constants and physical rank-two and mixed-place rank-seven arguments. These reconstructed reviews do not turn the remaining absence of a named-character transfer or all-period cycle exclusion into a theorem.
