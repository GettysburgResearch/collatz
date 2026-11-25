# Fresh complete-checkout verification

**PASS for the named scope. A complete Collatz proof is not claimed.**

Science checkpoint: `07f866baecc749c39ef86a10edef69e6d76a94a6`.

Science tree: `7a7a508775db4599fc1fc5ac6ccf5dd3ebb45d11`, with 1,031 tracked files. This exact commit was fetched into a new clean complete checkout. The replay started at 2026-11-25 18:29:37 UTC and finished at 18:30:28 UTC. All 18 manifest source hashes matched before and after replay. The publication child adds reports only and preserves those sources.

## Kernel checking

- Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Strict flags: `-j1 -DwarningAsError=true -DautoImplicit=false`.
- Six new modules, **32 new public theorem audits**: 14 carry, 11 source and 7 cycle.
- Two exact project dependencies, 23 additional public theorem audits.
- All eight project modules rebuilt into a newly created empty object directory. Pinned Lean and Mathlib dependency objects were reused.
- Each public theorem has exactly one named transitive axiom audit. All **55** reports use only subsets of `propext`, `Classical.choice` and `Quot.sound`.
- No `sorry`, `admit`, custom axiom or `native_decide` occurs in the checked proof sources.

## Deterministic controls

Each of the four controls ran normally and with Python `-O`. All four stdout/stderr pairs were byte-identical. Every control uses explicit guards, with no Python `assert` statements that disappear under optimization.

| Control | Executed coverage |
|---|---|
| Carry | 1,798 low-reference pairs/clocks and 35,960 supplied upper suffixes; 28 ordinary chains at seven prescribed depths through 32; 17,000 affine paths, 968 qualifying inverse bounds and 2,400 sharp minima; exact fixed-input discrete logarithms and separate moderate-clock double-arm paths |
| Cycle | 3,072 supplied ordinary windows through depth 384 at eight endpoints; 2,918,106 candidate progressions and 8,834,817 completed odd transitions; 47,571 actual rational-source pairs; exact large-integer arithmetic for the 301,971-bit denominator and four-lap packing example |
| Source | 2,050 actual first-passage trajectories; nonvacuous contracting-block classes; adjacent starts with distinct landing clocks; exact base-81 boundary controls through eight generations |
| Independent carry review | 66 direct double-arm trajectories at depths 1 through 11, with exact inverse-row division, endpoints and odd counts |

The large fixed-input carry exponents were checked modulo their required ternary precision; their astronomically large ordinary trajectories were not executed. The large rational cycle's entire inverse tree was not enumerated: the recorded packing range follows from the written theorem and the exact arithmetic certificate. All ordinary progression tests concern finite depth and changing sources, with no badness or periodicity claim.

## Repository integrity and receipts

`python -X utf8 -B tools/validate.py --regressions` completed all 11 commands in the clean complete checkout. Its identity and cleanliness were unchanged after replay. Repository integrity is separate from mathematical proof of the written asymptotic statements.

[Full machine receipt](fresh_replay/receipt.json) records command arguments, exit codes, log hashes, project-object hashes, source hashes and all 55 public axiom reports. [Repository validator receipt](fresh_replay/repository-validation.json) records the regression commands and checkout identity. The 38 JSON/log receipts are in [fresh_replay](fresh_replay/). [Replay driver](replay.py)

The previous PR description is preserved in [PREVIOUS_PR_DESCRIPTION.json](PREVIOUS_PR_DESCRIPTION.json). The final report-only publication commit is checked in a second complete checkout before the owned branch is fast-forwarded with an expected-head lease. Its final head and that validation are recorded in the updated PR description.

The full first-passage/head recurrence, global inverse-basin label construction, and published number-theory applications remain written mathematics. Their independent reviews and exact limitations are in [ROOT_REVIEW.md](ROOT_REVIEW.md) and [FINAL_PROPOSAL.md](../../research/astra-literature-closure-20261125/FINAL_PROPOSAL.md).
