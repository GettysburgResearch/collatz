# Round-seven publication record

**Collatz remains OPEN.** The scientific continuation and its execution evidence were pushed to the existing draft PR195 on 24 November 2026.

| Identity | Value |
|---|---|
| Owned branch | research/astra-global-closure-20261124 |
| Prior published head | fbe68bf1b13b797843691080d782f4262a5c4468 |
| Local scientific candidate | 6d62c23d00fdccced7d84a18477da79c10dc9145 |
| Published scientific commit | 43a1588fda26860b530d6886d83f41da769c2089 |
| Identical local and remote scientific tree | a133fbd0a5619321ff5fb29e3b8749ef0a58f602 |
| Complete scientific checkout | 671 tracked files |
| Frozen manifest | 49 file entries, excluding itself and later publication receipts |

The GitHub tree was compared with the locally prepared tree before its commit was created. The branch update was a non-forced fast-forward with the previous full head as a compare-and-swap condition. A fresh PR readback returned the published scientific commit, open draft status and the existing branch.

The exact remote commit was fetched and checked out in a complete clean verification worktree. The default repository validator passed all five commands there, as it had on the identical local candidate. The [published scientific receipt](published-science-validation.json) records its exact commit, tree, file count and observed command output. Every manifest entry was also compared against both the working and fetched scientific checkouts.

## Mathematical and execution scope

The five local Lean modules were rebuilt from source into an empty project output cache, using Lean 4.34.1 and Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612. The build used warnings as errors and retained 40 selected transitive axiom inventories; only propext, Classical.choice and Quot.sound were allowed. The project sources did not change during compilation. Existing Mathlib and package objects were reused.

Five exact finite checkers were run in both ordinary and optimized Python, giving ten matching executions with active explicit guards. The controls address literal finite trajectories, affine covers, full-divisor arithmetic and their stated finite samples. Proposed written asymptotic results and named external analytic inputs are outside these finite formal checks.

[Lean receipt](lean/receipt.json) · [Finite replay](CONTROL_REPLAY.json) · [Source manifest](SOURCE_HASHES.json) · [Coordinator reconstruction](ROOT_REVIEW.md) · [Overview](../../../research/astra-global-closure-20261124/round7/README.md)

## Final readback

This record and the scientific-checkout receipt are publication-only additions. Their publication commit does not change the frozen science. The exact final head and its complete-checkout receipt are recorded in the [PR195 description](https://github.com/GettysburgResearch/collatz/pull/195) after the final remote readback.
