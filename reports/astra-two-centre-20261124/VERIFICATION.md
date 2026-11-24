# Fresh verification of the complete-graph and renewal pass

The final scientific source checkpoint **71bedad6b44b35389d3a237e307e8286c11efcb5**, tree **a2aaf8a3496ec74771e88ccd03260e90138715a6**, passed a fresh replay in a clean complete checkout. The later receipt commit adds this record and the preserved logs; it changes no scientific source.

- Replay interval: 2026-11-24T10:02:50.630002+00:00 to 2026-11-24T10:03:06.226745+00:00.
- Lean: `Lean (version 4.34.1, x86_64-unknown-linux-gnu, commit 5045d0056413266e57c625dcd7c365b10e377c52, Release)`.
- Receipt SHA-256: `8d8dd8ed2d7eba04461b4d25c267f0a1c6a0b266fe3eeef2aff0e4ad0a78d0bc`.
- Source repository-validation SHA-256: `be9894c35a90ff6b5f48ec349e0633a4b2a5fc5a45758a65eacd851013415720`.
- Complete source checkout: 581 tracked files. The validator checked the same commit and tree before and after execution.

## Executed checks

Both new Lean modules were compiled from source with fresh output objects and warnings as errors. They import only the bundled Std library. Eight named declarations were audited. No proof admission or custom axiom was accepted; the peak computation uses kernel `decide`.

| Declaration | Transitive axioms |
|---|---|
| `Collatz.BinaryBoundary.transport` | `Classical.choice`, `Quot.sound`, `propext` |
| `Collatz.BinaryBoundary.divisionBudget` | `Quot.sound`, `propext` |
| `Collatz.MixedBoundary.negativeWall` | `Classical.choice`, `Quot.sound`, `propext` |
| `Collatz.MixedBoundary.expenditure` | `Classical.choice`, `Quot.sound`, `propext` |
| `Collatz.MixedBoundary.clearsDenominator` | `Classical.choice`, `Quot.sound`, `propext` |
| `Collatz.PeakCertificate.finite_tree` | none |
| `Collatz.PeakCertificate.local_safety` | `Quot.sound`, `propext` |
| `Collatz.PeakCertificate.lift` | `Classical.choice`, `Quot.sound`, `propext` |

All four Python controls ran in both normal and optimized mode. The replay parsed their syntax trees and rejected any use of an optimization-sensitive assertion. Each normal/optimized pair produced byte-identical output. All checks use exact integer or rational arithmetic and the digit-rank replay has no optimizer dependency.

| Control | Exact scope |
|---|---|
| `rewriting.py` | Full peak closure: 3,402 interior pairs, 1,137 boundary pairs, exact progression period; weighted rank for every source through 1,000,000 |
| `integer.py` | 144 separated blocks, 3,024 odd checkpoints, and complete graph balls at the four stated finite radii |
| `digit_rank.py` | 24 local-feature comparisons; 127 positional return comparisons; 110 full generic 2-by-2 matrix-polynomial comparisons |
| `basin.py` | 3,069 rational telescopes and 1,024 ratio-five first-return lifts |

The repository integrity validator also passed. It checks structure, frozen identities and its selected bounded controls. The optional broad `--regressions` bundle was not rerun; prior scientific packets were unchanged.

The replay checked the full scientific-file hash manifest before and after execution and required an unchanged clean checkout. The [receipt](fresh_replay/receipt.json) contains every command, output hash, object hash, declaration audit and control-pair comparison. The [source validator receipt](fresh_replay/repository-validation.json) records its exact checkout. The accompanying stdout logs preserve the mathematical finite-control outputs.

## What these checks do not establish

The circle-homeomorphism residence proof, full mixed-input/Bellman argument, analytic marked-law singularity and electrical calculations are written proofs with the review boundaries in [ROOT_REVIEW.md](ROOT_REVIEW.md). The matrix replay checks every generic polynomial coefficient, while its interpretation as an obstruction is the written positive-sum argument. The imported analytic results and upstream Lean projects were not rebuilt. This is not a proof of Collatz, the proposed global weighted-duration inequality, or unrestricted smaller-source merger.

To reproduce from a clean complete checkout, run `python -X utf8 -B reports/astra-two-centre-20261124/replay.py --lean /absolute/path/to/lean --output /absolute/path/outside/the/checkout/new-output`. Use the pinned Lean version and a new empty output directory. The preserved receipt is tied to the scientific commit above; a later receipt-only checkout has a different Git identity.
