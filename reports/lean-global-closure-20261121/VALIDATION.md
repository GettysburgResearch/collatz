# Actual clean-checkout validation

The scientific checkpoint fetched directly from GitHub and checked was:

- Commit: `1d207aebe504e66ecdebd4ffcaaf57f10595d0ec`.
- Tree: `e9b652e03aa390eb58d1b46cb2252a047c6ca5a0`.
- Complete tracked checkout: **350 files**, with no sparse or missing paths.

## Lean execution

[`clean-build.json`](clean-build.json) records an actual `lake build` from a
fresh project output directory. All four proof modules and the package
entrypoint were compiled afresh. Only the external pinned mathlib and its
dependency caches were reused. Tracked inputs stayed clean throughout.

Lean **4.34.1**, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` were used. Warnings were errors.
The process exited zero. All **45 printed axiom reports** contain only
`propext`, `Classical.choice`, and `Quot.sound`, or subsets of that set.

The five project source hashes match the earlier four-module execution
receipt and the files retained in the receipt commit:

| Source | SHA-256 |
|---|---|
| `EndpointSteering.lean` | `a6373e87e097874c11b348198d7cf68bf9944a174654047678df4bc961263c3a` |
| `LocalProfileObstruction.lean` | `a391ef70a09001d7882ecf3dc1eef52c90c6db6fa149d038c9d199e747a7813f` |
| `RelativeParityBarrier.lean` | `1c2406c9096d19758dccab97a307aba80a0c26ec963e8869c354ede7e919b355` |
| `SiblingRigidity.lean` | `7b3c9626626b70548fa0cc062e958b65fdfd1ba783ca5aeaab94e6fcbb00b72e` |
| `CollatzGlobalClosure.lean` | `8985a7aa06364679f885189f23175e72d67ead13286a7bcffd5a8b8b0f678f8f` |

The actual outputs establish the stated Lean theorems and implications.
`RelativeBudgetReturns` remains a defined, unproved universal proposition;
no custom axiom or `sorry` fills it. No full Collatz proof is claimed.

## Repository gate

[`clean-repository.json`](clean-repository.json) records
`python -X utf8 -B tools/validate.py` on the same remote scientific commit.
All five required commands passed. The checkout identity was unchanged.
Optional historical research regressions were not rerun.

Repository integrity and the finite implementation controls in the search
reports are separate from mathematical proof checking. The numerical rank
search produced no successful global certificate. The final ordinary
candidate rejections are reported as exact failures of those candidate
ranks, not failures of Collatz convergence.

This receipt commit adds validation records and documentation. The Lean
sources, pinned dependencies, and search programs are unchanged from the
scientific checkpoint. The final remote head is checked again for repository
integrity and identified in the PR description.
