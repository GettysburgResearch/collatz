# Connected Lean project

This project imports five byte-identical implementation modules from OpenAI's November 24 release and connects them to ordinary integer arithmetic and two frozen Collatz proof interfaces. It does not import challenge placeholders, assume Collatz, or build the entire OpenAI library.

## Reproduce

Install the toolchain in `lean-toolchain`, then run from this directory:

```sh
lake exe cache get Mathlib.LinearAlgebra.Matrix.Rank Mathlib.LinearAlgebra.TensorProduct.Matrix Mathlib.RingTheory.Flat.Basic Mathlib.LinearAlgebra.Dimension.Constructions Mathlib.Algebra.Order.Field.Basic Mathlib.Tactic.SplitIfs Mathlib.Data.Matrix.Mul Mathlib.LinearAlgebra.Matrix.DotProduct Mathlib.Algebra.BigOperators.Fin Mathlib.Algebra.Order.Pi Mathlib.Data.Finset.Card Mathlib.Tactic.Ring Mathlib.Tactic.NormNum Mathlib.Tactic.Linarith
python -X utf8 -B check.py --receipt /tmp/collatz-openai-lean.json
```

The cache is optional: `lake build` can compile dependencies from source. `lake exe cache get` without module arguments obtains the full pinned Mathlib cache. Lake obtains missing packages from the checked-in `lake-manifest.json`, which records all resolved revisions. Retain that manifest when reproducing the reported build. Lean and Lake must both be on PATH.

For the clock proof alone, Mathlib is unnecessary:

```sh
python -X utf8 -B ../clock/check_lean.py
```

For a fresh build of this packet while reusing a Mathlib cache, use a fresh checkout with no local `.lake/build` objects, install the pinned packages and run the same checker. A cached upstream Mathlib library and newly compiled packet sources are different evidence; the execution report identifies both.

## Dependencies and actual uses

| Frozen input | Use in the connected proof |
|---|---|
| `OAI.LinearAlgebra.SpectralBooks.BlockDiagRank` | Add the ranks of two independently tagged batches; compare with their actual integer endpoints. |
| `OAI.LinearAlgebra.FiniteFourier.BatchedTimeShift` | Bound the rank cost of deleting transfer states, retaining the same source and readout. |
| `OAI.LinearAlgebra.SpectralBooks.KroneckerRank` | Dependency of the batched Fourier interface. |
| `OAI.Optimization.LinearProgramming.Farkas.Basic` and `.Sparse` | Turn finite potential inequalities into exact primal or sparse dual certificates. |
| Three PR192 files | Original ordinary `run`, `Good` and `SmoothCore.FirstTower`; the final merger theorem uses these definitions. |
| Six PR206 files | Original shortcut map, odd-gap clock, crossing and cycle interfaces; the clock bounds and controls use these definitions. |

OpenAI sources, totaling 22,442 bytes, are recorded with SHA-256 hashes in [UPSTREAM.json](UPSTREAM.json), under the accompanying Apache-2.0 [license](OPENAI-LICENSE). Their upstream commit is `3344da59991ed94f9ba711217b29c1d760badfa6`. PR192 sources are recorded in [ORIGIN.json](../tensor/pr192/ORIGIN.json); PR206 hashes are enforced by [the standalone checker](../clock/check_lean.py). The latter nine files retain the Collatz repository's existing MIT license. These are frozen copies, not merges of those branches or assertions that their entire programs are accepted.

## Proof surfaces

`CollatzOpenAI.lean` imports the complete packet. `Audit.lean` requests axiom dependencies for every public theorem in its eight new mathematical modules and seven relevant imported declarations. The checker permits only `propext`, `Classical.choice` and `Quot.sound`; a theorem depending on `sorryAx` or a new research assumption fails that audit. Hypotheses in a theorem remain hypotheses: the audit does not prove that a proposed transfer matrix satisfies them.

The native terminal theorem is `Collatz.TensorBridge.unbounded_guarded_tower_exclusions`. The clock bound is `Collatz.Itinerary.ClockBridge.exponentially_sparse_clock`. `Collatz.OpenAIFourier.count_labeled_disagreements` exposes the unproved diagonal-representation premise explicitly. `Collatz.OpenAIPotential.potential_or_sparse_obstruction` is a finite rational alternative; it supplies no global graph for Collatz.

The frozen `FixedGate.lean` uses a deprecated `if_false` name and emits one warning on this compiler. Its bytes are preserved. The new audit file is compiled with warnings treated as errors.

The exact matrix exponent, full Fourier lower bound, sunflower theorem, hierarchy separation and strongly polynomial RAM algorithm were inspected as source-qualified results. None is counted as independently rebuilt here. The direct imports are small genuine proof implementations, and their actual use is visible in the bridge files.
