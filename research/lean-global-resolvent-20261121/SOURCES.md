# Frozen sources for the global Lean attempt

The accepted repository base is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. This packet is research on a separate branch.

| Source | Exact head | Use |
|---|---|---|
| [PR174](https://github.com/GettysburgResearch/collatz/pull/174) | `7034109ed60a26bc49824e1ed43c239ceca81194` | Dependency-free ordinary-map toolbox, forward/reverse closure equivalences and exponent families. `lean/Collatz/ReverseBasin146.lean`, `Closure.lean` and `Shadow.lean` are copied unchanged from `research/psi-closure-20261121/lean/Collatz/`. The project root and audit are extended for our new modules. |
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146) | `f431078244e868dc699fad011044f0d5e7f76437` | Current terminal-five and whole-interval synchronization interfaces, including new commits on this older PR. The imported core reverse theorem itself is the earlier source version credited inside PR174; no replacement by an uninspected later theorem is made. |
| [PR173](https://github.com/GettysburgResearch/collatz/pull/173) | `a09eb47197cd99f218b3fa013c681df65ea0f69a` | Global interval-survivor criterion and equal-clock inverse fans; used to choose the analytic attack, not imported as an unproved Lean axiom. |
| [PR171](https://github.com/GettysburgResearch/collatz/pull/171) | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | Relative-section recurrence, critical negative moment and full positive-kernel pressure boundary. |
| [PR172](https://github.com/GettysburgResearch/collatz/pull/172) | `b22d94240f3d44a04231508e5dfe9a4947a57125` | Uniform tail descents and the stated remaining all-source certificate obligation. |
| [PR170](https://github.com/GettysburgResearch/collatz/pull/170) | `656063d5efa0f5708356ab2563a4348d39bae013` | Carry transport and terminal-library boundary. |
| [PR164](https://github.com/GettysburgResearch/collatz/pull/164) | `9582df78eb4d768eb748d3cf367ba97582308a52` | Updated direct-R and source-zero descents; old and new source packets are distinguished. |
| [PR169](https://github.com/GettysburgResearch/collatz/pull/169) | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | Our prior paired height contractions and exact primitive-word arithmetic. |

Lean runtime: `leanprover/lean4:v4.34.1`. The core project requires no Mathlib. Any separate Mathlib development in later checkpoints is pinned to `d13f23b723b8a846827a245b89c10fc7d3f11612` and is identified separately because the imported dependency-free induction shim is not intended to be imported together with Mathlib.

The multiset order considered in this pass is the established Dershowitz--Manna order. Its well-foundedness is supplied by Mathlib's `Mathlib.Data.Multiset.DershowitzManna`, not claimed as a new theorem. The question here is whether actual ordinary certificate moves share that order and admit a complete selection theorem.
