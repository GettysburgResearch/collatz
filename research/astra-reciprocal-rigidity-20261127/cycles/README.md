# First exit and complete cycle arithmetic

The universal positive Collatz problem remains **OPEN**. We used the shortcut map and, for the explicit prime-weight controls, its ordinary odd-to-odd acceleration.

* [All-shift whole-denominator theorem](ALL_SHIFT.md) proves an order-independent logarithmic bound, 42/134 source-qualified numerical corollaries, and a same-clock merger criterion on arbitrary actual paths. [AllShift.lean](AllShift.lean) proves the full finite synchronized length theorem from actual numerator recurrences, the centered pair comparison, and exact numerical cutoff arithmetic. The circular assembly, small-order refinement, and asymptotics are written proofs. [Lag spectrum](LAG_SPECTRUM.md) further restricts which clocks can have few mismatches, with an explicit cubic counting bound.
* [Infinite-horizon first exit](FIRST_EXIT.md) gives a SOURCE-QUALIFIED cofinite agreement theorem with an ineffective height threshold. The complete finite ordinary-orbit consumer, including the repetition argument, is in [FirstExit.lean](FirstExit.lean).
* [Complete denominator and shifted products](ARITHMETIC.md) gives an interpolation theorem, exact ordinary weighted paths defeating fixed translated prime tests, reciprocal identities at zero and minus one, and a positive rational two-run construction with forced cancellation at prescribed prime powers. [ShiftBalance.lean](ShiftBalance.lean) proves interpolation and the two-shift obstruction. The three-shift obstruction uses [an exact sparse witness](three_shifts.tsv).
* [check_cycles.py](check_cycles.py) checks the three-shift certificate without numerical optimization, replays the 20 steps in the smaller illustration, tests 208 positive two-run parameter pairs at every rotation, and checks first exit independently for the 19,999 starts from 2 to 20,000. Bounded checks do not supply the asymptotic inputs.

* [check_all_shift.py](check_all_shift.py) verifies the rational cutoff certificates and every proper shift of 585 primitive positive rational necklaces of period at most 12, including the centered ratio at every clock.

## Frozen repository references

The checkout base is ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. We used its AGENTS.md, README.md, docs/RESEARCH_MAP.md, research/RESULTS_CATALOG.md, research/integrated/periodic-tails/README.md and scoped ERRATA.md, especially E-D-002 on the trivial cycle, all-zero endpoint, and ordinary replay.

| PR | Head | Relation to this packet |
|---:|---|---|
| 175 | 67664c6bf555bf7f7fcec987acb79500071dce4b | risk26/cycles/POSITIVE_GAP_FULL_FIBER.md proves equivalence of all rotated prime-power tests. |
| 178 | 398b3a04da071e96362005792417bd5cf8cc6497 | research/reassessment-20261123/cycles/PRIME_POTENTIAL_AND_FULL_CLOSURE.md supplies the previous single-product genuine-edge control. |
| 185 | 2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d | EFFECTIVE_FIXED_BLOCK_CYCLES.md treats one-parameter fixed linear block schemas. |
| 188 | f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d | CYCLE_FILTERS.md obtains full-factor tests for structured residue profiles. |
| 191 | 37b3916633cd32a0c173b20bb18ec3a7ec290a63 | two-sided-cycle-packing-20261124/README.md gives common reduced denominator and two-sided packing for specified blocks. |
| 192 | ae48a04cca29abe5fc8273bcda45e7eee0874896 | RATIONAL_ORDERS.md constructs nonordinary controls for simultaneous cyclic orders. RECIPROCAL_OPERATOR.md treats a different reciprocal operator. |
| 193 | aa6868996f6f30b12d91c367f7c6edcfd93784b2 | STRIP_ENTROPY.md already gives the elementary width exponent. CYCLE_OCCUPATION.md derives actual ordinary spread. CYCLE_CLOSURE.md bounds common gcds on proper arcs. |
| 195 | 3fa7ef4a0011b35447a70f587b400878d5ea8ebe | astra-six-hour-20261127/cycles/README.md treats the bounded least-disagreement alternative and marked good neighbors. |
| 196 | 27d03cfe902660e06604eb55bb28ca3d2754ff48 | ROTATIONAL_EXCLUSION.md excludes close rotations under a complete-determinant bound and records its logarithm inputs. |
| 200 | eb91086951b66923787f696801f0c3ca52a0077d | ALL_PLACE_PRIMITIVE_CYCLE_APPROXIMATION.md and ROUGH_DENOMINATORS.md construct rational controls. UNRESTRICTED_PHYSICAL_ODD_OCCUPATION.md gives a physical high-occupation alternative. |
| 210 | 592328fecf8ea2cf41736294856d95f890a1ba98 | critical-record-rational-rigidity-20261125/README.md treats rational limits of the ternary record set for injective paths. |

The versioned primary external sources and their exact usages live in [the first-exit proof](FIRST_EXIT.md) and [the whole-denominator proof](ALL_SHIFT.md). These are scope comparisons, not independent review verdicts on entire PRs.

## Replay

Run both exact integer diagnostics in this directory.

    python -B check_cycles.py
    python -B check_all_shift.py

Both also run with Python optimization enabled. For Lean run the following with a Lean 4.34.1 executable and the checked-out mathlib at d13f23b723b8a846827a245b89c10fc7d3f11612 with its built package dependencies.

    python replay_lean.py --lean /path/to/lean --mathlib /path/to/mathlib4

The build uses warnings as errors. All three Lean files print their proof dependencies. The checked declarations use only propext, Classical.choice and Quot.sound. No custom axiom is installed.
