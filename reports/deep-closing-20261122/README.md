# Published deep-closing replay

**PASS** on the actual published scientific commit
`81c4de6f77c7b9bf6c72cd1e137f28733ed6be39`, tree
`ac34ecdc38c536569bffebf963be86a0b0817905`.

The complete clean checkout contained 653 tracked files. The external
runner recorded 16 commands, including compilation of the two new Lean
modules, the four certificate executions, and the default repository gate.
It checked clean status, HEAD, tree, all packet inputs and exact copied
source bytes again at completion.

## Results

| Check | Observed result |
|---|---|
| `OriginalSourceEntropy.lean` | PASS, 21 public theorem audits |
| `CycleWordEntropy.lean` | PASS, three public theorem audits |
| Source and review bindings | PASS, eight exact target bindings |
| Arithmetic certificate | PASS normally and under `python -O`; complete 41-gap replacement; six exact permutation differences; two damaged controls rejected |
| Cycle-law controls | PASS normally and under `python -O`; 8,178 words, 43 whole residue laws, 3,611 exact cone comparisons; three damaged controls rejected |
| `python -X utf8 -B tools/validate.py` | PASS on the same complete checkout |
| Checkout continuity | PASS; no source, HEAD, tree or status change |

Lean 4.34.1 commit `5045d0056413266e57c625dcd7c365b10e377c52` was used
with Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
Both modules compiled with warnings treated as errors. Their audited
dependencies are subsets of `propext`, `Classical.choice`, and `Quot.sound`.
No local Collatz theorem, custom axiom, unfinished proof or native
evaluation axiom occurs in the new modules.

The exact machine record is [receipt.json](receipt.json). Command outputs
are preserved byte for byte in [logs/](logs/), with the filenames and
hashes listed in the receipt. Absolute paths in the receipt describe the
actual execution environment; the copied logs here retain their basenames.
The tracked-files log preserves Git's NUL separators.

## Reproduce

From a clean complete checkout of the scientific commit, with the pinned
existing Lean and built Mathlib installations:

```sh
python -X utf8 -B research/deep-closing-20261122/check.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/built/mathlib \
  --build-dir /absolute/path/to/empty-external-build
```

The runner writes all generated compiler inputs, artifacts and logs outside
the checkout. It compiles only the two new independent modules and does
not replay unrelated earlier packets.

This report-only follow-up preserves the tested scientific tree outside
`reports/deep-closing-20261122/`. Its publication does not retroactively
make the receipt a full execution at the report commit. The finite Lean
scope, separately reviewed written limit arguments and remaining open
closing inequalities are stated in the
[scientific packet](../../research/deep-closing-20261122/README.md) and its
[formalization map](../../research/deep-closing-20261122/FORMALIZATION.md).

**No full Collatz proof, escaping-orbit exclusion, or unrestricted positive
cycle exclusion is claimed by this receipt.**
