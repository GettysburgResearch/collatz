# Trit-chain checks

Both public theorems in `research/astra-diagonal-closure-20261125/joint/TritChain.lean` passed Lean 4.34.1 (commit `5045d0056413266e57c625dcd7c365b10e377c52`) with mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, `-j1 -DwarningAsError=true -DautoImplicit=false`. The local `SourceDeletion.lean` dependency was rebuilt first in a private output directory under the same flags. The new module was then compiled against that freshly built olean. The build exited zero. The two public declarations reported

```text
'Collatz.TritChain.fourTritCylinder' depends on axioms: [propext, Classical.choice, Quot.sound]
'Collatz.TritChain.forcedColumn' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The fixed table predicate uses ordinary kernel `decide` on all 81 suffixes at clock 14. The first public theorem proves equality of the two ordinary endpoints and the required difference of four odd counts for every member of each class and every common clock at least 14. The second proves a forced-deficiency statement for an arbitrary finite set and arbitrary length chain. The probability calculation on the entire shared grid is a written proof. The compiled module contains no admitted result, native decision procedure or user-declared axiom.

| Compiled source | SHA-256 |
| --- | --- |
| `research/astra-minimum-source-20261124/arithmetic/SourceDeletion.lean` | `21227f38df7f95b29613ec322a1e48f3fc0e423155fb12867c9dfcf546699af0` |
| `research/astra-diagonal-closure-20261125/joint/TritChain.lean` | `4fa03706c357d68ea146ffadfe342dcadf90cc8a7f908b312db27fb351c24a95` |

The kernel results and the written asymptotic result concern finite arithmetic labels. Establishing how often high-gap formal opening cells come from actual original parents at the late clock is a separate open question. No unconditional convergence theorem was checked.
