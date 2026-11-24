# Provenance of the eight inherited Lean modules

These files carry forward 62 public theorem statements from six open GettysburgResearch/collatz pull requests. Each URL identifies the exact source commit and path. The local module keeps the original namespace. Source status, hypotheses and downstream limits are audited separately in [the independent correspondence review](../../../reports/astra-global-closure-20261124/audit/REVIEW_FORMAL.md).

| Local module | Frozen upstream code | Public theorems |
|---|---|---:|
| PhasePacking.lean | [#182 · research/phase-packing-round12-20261124/PhasePacking.lean](https://github.com/GettysburgResearch/collatz/blob/cbec52dde5bed390a693310dd04e911033ba0cc9/research/phase-packing-round12-20261124/PhasePacking.lean) | 8 |
| RepetitionWindow.lean | [#182 · research/fixed-source-repetition-round11-20261124/RepetitionWindow.lean](https://github.com/GettysburgResearch/collatz/blob/cbec52dde5bed390a693310dd04e911033ba0cc9/research/fixed-source-repetition-round11-20261124/RepetitionWindow.lean) | 11 |
| RepeatObstruction.lean | [#187 · research/fixed-source-repeat-obstruction-20261124/RepeatObstruction.lean](https://github.com/GettysburgResearch/collatz/blob/099058f3f2602a48e109c964899f0a9a2a223338/research/fixed-source-repeat-obstruction-20261124/RepeatObstruction.lean) | 6 |
| CarryCocycle.lean | [#188 · research/scalar-carry-cocycle-20261124/CarryCocycle.lean](https://github.com/GettysburgResearch/collatz/blob/beed685ab713923191ae40c9559bf7400298d2d3/research/scalar-carry-cocycle-20261124/CarryCocycle.lean) | 4 |
| ResidueDefect.lean | [#188 · research/scalar-carry-cocycle-20261124/ResidueDefect.lean](https://github.com/GettysburgResearch/collatz/blob/beed685ab713923191ae40c9559bf7400298d2d3/research/scalar-carry-cocycle-20261124/ResidueDefect.lean) | 6 |
| CarryBudget.lean | [#189 · research/stationary-carry-rigidity-20261124/CarryBudget.lean](https://github.com/GettysburgResearch/collatz/blob/a0be70b1ffa075cbc50755ac76036108c028d120/research/stationary-carry-rigidity-20261124/CarryBudget.lean) | 6 |
| MahlerCore.lean | [#190 · research/mahler-physical-scripts-20261124/MahlerCore.lean](https://github.com/GettysburgResearch/collatz/blob/ba58227c5a047ff3859a148a5fdaac4fd1451e4c/research/mahler-physical-scripts-20261124/MahlerCore.lean) | 8 |
| TwoSidedPacking.lean | [#191 · research/two-sided-cycle-packing-20261124/TwoSidedPacking.lean](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/TwoSidedPacking.lean) | 13 |

## File identities

Both values in each row are SHA-256 of raw file bytes. The upstream byte strings were read by git show from the commit in the preceding table. The packet hashes bind the exact sources selected for strict replay.

| File | Upstream SHA-256 | Packet SHA-256 |
|---|---|---|
| PhasePacking.lean | `b10dbf602c9afcc8491cba3b6b0c326103f1f4e6599a73204c7454574bdecbe5` | `25d0f02e1faaa3540a755d794c86a45dc5ddc3db9dc047732b25e0607ef1dd03` |
| RepetitionWindow.lean | `313e434abb73b2027311145c40e6aed3262a82ec1a2ba688b48d411e64e305d2` | `3c6eb159c12d047cf2eff381cce733b55deb7a499976d6e6cb6f91ca548b2b0c` |
| RepeatObstruction.lean | `d73158ea82188a40b16c64e77da2033b5a5b6373d3aaa23921c551a29a5b2e13` | `424e5841662aa6f8c2264ebbe8bc62191d77493bea2ee85ae38eed5ee3a982ee` |
| CarryCocycle.lean | `a42133eddf0bb81288b3a27e6b43774e92137bab481f9748f93b261ce602a878` | `7d17a1d4d0f393bd509cb523886c83054101d19fd9babc7727b457dec273757a` |
| ResidueDefect.lean | `a2f47b41e37fe60e5ee024395cb95b791f134516ba6a7fd9a5551fe9b8e7d2b2` | `9eae4f15bb0be0474a904db8c4e92f2bd18f1f5e1c6d304a3cd861ad1eeced8d` |
| CarryBudget.lean | `aa84500b5fd73eb4daa49d62237f3d3a0d42be8d454d35b323823f73ef406097` | `c064083c19bdee7797bc8fd57826cc0622f639a58e19e6c1dcb370ca6a39cd0f` |
| MahlerCore.lean | `0ebc5c02a28db6af93e81eb4cb55c65386774501b3e1e02277d866ade6b550f5` | `8f15a4a6ce4032f0342f143604cad5f21ab0815f37b087c76fc778bf4b172a25` |
| TwoSidedPacking.lean | `ec4af1d8258372c4be091f649c572517214344e952d22fcfea6e43075c28a273` | `3ffbcbc49dcc194effd518a56c458da5d0aea7042f6e494212f0b100a8890181` |

## Adaptations

The eight modules use explicit imports, disable automatic implicit parameters and print an axiom report for every inherited public theorem. CarryBudget uses Std and spells the natural-number type Nat. The other seven import selected Mathlib modules. PhasePacking uses mul_le_mul_iff_left₀ for two positive right-factor cancellations, drops two ring tactics after field_simp already closes its goals, and obtains nonnegativity of a squared rational from the existing lower bound. Three CarryCocycle proof sequences use a semicolon in place of all-goals sequencing to pass strict lint. The finite-word, arithmetic and algebraic statement boundaries are inherited. The original source bytes remain accessible at the commit links.

## Replay

Use replay.py in this directory with the Lean 4.34.1 compiler and a locally built Mathlib checkout at d13f23b723b8a846827a245b89c10fc7d3f11612. The implementation records individual source hashes, axiom reports, subprocess exit codes and log hashes. Read the [execution receipt](../../../reports/astra-global-closure-20261124/formal/final-replay.json) for this run. A complete successful receipt must cover all eight rows above and all 62 public theorem names.
