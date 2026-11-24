# Execution and review record — 24 November 2026

**Full Collatz remains OPEN.** This report records actual local execution, exact source identities, and scoped internal reconstruction. It accompanies the [scientific packet](../../research/astra-orbit-cycle-20261124/README.md).

Five GPT-6.2 Astra workers contributed to cycle arithmetic, actual-orbit occupation, ordinary mergers, Lean audit/repair, and independent closing review. Work ran in successive parallel groups within the available concurrency limit. The coordinator reconstructed the main interfaces, integrated the results, reran the final publication files and checked the remote source updates. Multiple agents are a review mechanism, not a proof standard.

## Lean status: compiled, with exact limits

The working environment contained a usable exact toolchain. Its use supersedes an earlier assumption that Lean was unavailable in this session. No formal result is inferred merely from the model or subscription name.

- Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Compiler executable SHA-256 `e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Strict invocations used `-j1 -DwarningAsError=true`; the new kernels also used `-DautoImplicit=false`.
- The auditor checked the eight Mathlib dependency HEADs against the Lake manifest and clean tracked worktrees. A temporary byte-identical shared-library copy was used for some worker runs to reduce host paging. The final repository-path replay used the ordinary pinned Lake environment.

| Checked file | Source PR | Printed declarations |
| --- | --- | ---: |
| CarryBudget.lean | 189 | 6 |
| CarryCocycle.lean | 188 | 6, including two private helpers |
| MahlerCore.lean | 190 | 8 |
| PhasePacking.lean | 182 round 12 | 8 |
| RepeatObstruction.lean | 187 | 8, including two private helpers |
| RepetitionWindow.lean | 182 round 11 | 11 |
| ResidueDefect.lean | 188 | 6 |
| TwoSidedPacking.lean | 191 | 13 |
| **Prior-kernel total** | | **66** |
| CarryOccupation.lean | New packet | 6 |
| RotationalExclusion.lean | New packet | 4 |
| HalfSource.lean | New packet | 7 |
| **Total** | | **83** |

Every reported declaration passed strict compilation. Its transitive axiom set is contained in `{propext, Classical.choice, Quot.sound}`; some declarations have fewer or no axioms. The count includes helper lemmas and must not be read as 83 independently new research theorems.

[AUDIT_SUMMARY.json](AUDIT_SUMMARY.json) checks and collects the final eleven source hashes, declaration counts and completed receipt locations. The combined count was computed from the recorded axiom inventories, and the three new inventories were also compared with their source declarations.

[COMPILE_RECEIPT.json](COMPILE_RECEIPT.json) binds each of the eight old original PR/full-SHA/path/source-hash tuples to its checked copy and all printed axiom sets. The adjacent `.lean.patch` files show every change. [PUBLISHED_PATH_REPLAY.json](PUBLISHED_PATH_REPLAY.json) and [its log](PUBLISHED_PATH_REPLAY.log) record a fresh coordinator replay of these final repository-path files, exit 0, with all 66 hash and axiom-list comparisons passing. The portable replay script itself was executed end to end. A second worker independently rechecked these same final source bytes.

[CARRY_LEAN.json](CARRY_LEAN.json), [CYCLE_LEAN.json](CYCLE_LEAN.json), and [MERGER_LEAN.json](MERGER_LEAN.json) bind the three final new files to actual commands, versions, hashes, exits and full axiom output. The last merger copy adds four helper `#print axioms` commands to the worker's seven-theorem source; its proofs are unchanged and the resulting final bytes were compiled afresh. The cycle copy similarly adds the omitted `amp_append` report and was compiled afresh.

### Exact originals and repairs

[ORIGINAL_REPLAY_RECEIPT.json](ORIGINAL_REPLAY_RECEIPT.json) preserves the actual completed tests of the unchanged upstream source bytes:

| Original source | Actual result | Qualification |
| --- | --- | --- |
| PR187 RepeatObstruction | PASS | Six original public axiom reports; the checked copy additionally audits its two private helpers. |
| PR191 TwoSidedPacking | PASS | All 13 original reports clean. |
| PR182 round 11 RepetitionWindow | PASS | Original source has no axiom-report directives; its checked copy adds all 11. |
| PR182 round 12 PhasePacking | **FAIL** | Two references to unavailable `mul_le_mul_right₀`, downstream diagnostics, and `sorryAx` in error-recovered failed declarations. |
| Other four upstream blobs | No completed original-byte verdict | Their checked copies all passed; do not substitute this for unmodified-original execution. |

The PhasePacking replacement uses the supported cancellation lemma, removes already-solved tactic tails, and uses an existing hypothesis in a nonnegativity proof. All eight theorem statements are retained. CarryCocycle required three strict-linter proof-script cleanups, also without changed theorem statements. Six other files change imports and axiom instrumentation only. Errors and historical comments remain preserved in their original identities.

**The machine-checked boundary is finite.** The general occupation and edit-distance theorems, the analytic two-power bound and all-period cycle classification, the positive-clock merger barrier, and the unbounded additive-overhead theorem are written proofs here. The original actual-scalar convergence criterion is an exact source dependency, not freshly recompiled in this packet. This PR makes no claim that all Lean or all mathematics on twenty-two other PRs was reverified.

## Bounded computations actually executed

Each of the three new programs completed in normal and optimized Python with byte-identical output. Their checks use explicit failures, not optimization-sensitive assertions. Source hashes, actual commands and full outputs are retained.

| Receipt | Coverage |
| --- | --- |
| [CARRY_CONTROLS.json](CARRY_CONTROLS.json) | 500 selected sources; 1,480 injective prefixes; 10,548 past residues; 8,880 Hamming, 7,400 occupation, 128 optimal-fragment and 384 optimal-edit-alignment checks; 708 exceptional occurrences across overlapping sample horizons; adversarial finite carry/reset control. |
| [CYCLE_CONTROLS.json](CYCLE_CONTROLS.json) | Exact Farey/log certificate; 82,202 power-gap comparisons; all 131,070 bit words of lengths 1–16; 13,066 rational rotations; 5,908 block transpositions; failed-strengthening controls. |
| [MERGER_CONTROLS.json](MERGER_CONTROLS.json) | 149 barrier sources below 900; 1,859 actual meetings through inverse clock 32; 225 positive selectors; 24 marked progression certificates; complete indicated inverse-clock layers at 5923; all 1,312 first-hit anchors for E=16. |
| [CONTROL_RECEIPT.json](CONTROL_RECEIPT.json) | Eight old finite replay scripts at the exact pinned source versions. |

The independent reviewer additionally used separately implemented forward/rotation checks, as recorded in the reviews. None of these finite executions decides an unbounded orbit problem. The arbitrary-E overhead proof uses only the finite subset reaching one; the explicit all-anchor certificate is for E=16.

## Written review and live-source boundaries

[INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md) identifies the SHA-256 of each reconstructed initial proof packet. [MERGER_ADDENDUM_REVIEW.md](MERGER_ADDENDUM_REVIEW.md) covers the frozen final merger changes, including the legal signed suffix, bounded positive anchor, no hidden Collatz assumption, explicit threshold, and exact valuation in the marked construction. [REVIEW_NOTES.md](REVIEW_NOTES.md) reconstructs selected prior repetition and packing claims at their pinned files.

[SOURCE_HEADS.json](SOURCE_HEADS.json) retains the initial 20-PR snapshot. The separate [REFRESHED_HEADS.json](REFRESHED_HEADS.json) records the later 22-PR source cutoff. PR189 advanced by an attribution-only README correction: its strict stationary collision deficit already appears in PR180. The Lean source used by this audit is unchanged. The original source pins therefore remain valid and do not silently move.

PR192 and PR193 arrived during the pass. The [PR192 scalar review](ADDENDUM_PR192.md) reconstructs the exact earlier science bytes; the later PR192 head adds formal replay evidence and visibility-port copies without changing that phase proof. Its upstream formal receipt is not counted as a fresh execution by this packet. The [PR192 cycle review](PR192_CYCLE_REVIEW.md) and [PR193 review](ADDENDUM_PR193.md) identify their own exact claims and heads. The latter includes the later coverage limitation and high-complexity rational-cycle controls. The [frontier synthesis](FRONTIER_REVIEW.md) places all these results against their missing global implication.

## Publication integrity

The complete scientific and report files are bound by `FILES.json`, excluding that manifest itself. A clean complete checkout is validated using the repository's required `python -X utf8 -B tools/validate.py` gate. Its five default checks concern structure and selected bounded integrity controls; they do not prove the research mathematics. No workflow or repository setting is changed. The optional old regression bundle is not needed for the new isolated research files.

The publication PR records the exact final remote commit and tree, the final clean-checkout receipt and its hash, and the fresh remote readback. Keeping this self-referential receipt in the PR body avoids modifying the source tree after the checkout whose identity it certifies.
