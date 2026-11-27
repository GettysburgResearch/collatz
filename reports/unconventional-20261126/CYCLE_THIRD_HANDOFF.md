# Frozen third-wave source manifest

The hashes below identify author copies. Repository links were adapted during integration; the source map records both hashes.

The two Lean files contain **eleven checked theorem declarations**, six in ModularCarry and five in ResetDepthRatio. The asymptotic, Subspace and squareclass arguments are written proofs. The newly inspected PR192 source head is `1cb3e8496a6bd6092d3d0dc1dd043c3bcd662aca`.

| File | SHA-256 | Scope |
|---|---|---|
| [COMPLETE_MODULAR_CARRY.md](../../research/unconventional-20261126/arithmetic/COMPLETE_MODULAR_CARRY.md) | `257df0db79a096bb8dff8a1bff843a21812a22c7c67149ba0374e884ba6db80f` | MC1–MC3 written modular classification, pointwise switches and full cancellation estimates |
| [ModularCarry.lean](../../research/unconventional-20261126/arithmetic/ModularCarry.lean) | `58b858d9e40a4ab174f153a0708aa28b6b48e769a3fa3ce2cfbefdbcc61400a4` | Six checked Lean theorems for subset sums and carry perturbations |
| [check_modular_carry.py](../../research/unconventional-20261126/arithmetic/check_modular_carry.py) | `00bd4203ab0f3d4fabe7ff1d15353fb03b59db4591d99b3d9f079c0197203373` | Group and integer full-cycle controls |
| [RESET_DEPTH_RATIOS.md](../../research/unconventional-20261126/defects/RESET_DEPTH_RATIOS.md) | `aae9229cefc694c60df8bbec5254ab94d9f658e275508be77dcb987b10cae436` | E1–E2 written ratio rigidity and sharp CRT profile |
| [ResetDepthRatio.lean](../../research/unconventional-20261126/defects/ResetDepthRatio.lean) | `91d17aa9c9a40a10a91d8a53b50de3730db085785c66b5785a3422f54ad0d6b0` | Five checked Lean theorems for divisor transport and positive splitting |
| [check_depth_ratios.py](../../research/unconventional-20261126/defects/check_depth_ratios.py) | `0c644328b1968e1b4b0ad464b19db84f66ea465a9bc343651da53ca4e6a8e970` | Exact true-block and CRT controls |
| [SHIFTED_SQUARECLASS_CLOSURE.md](../../research/unconventional-20261126/defects/SHIFTED_SQUARECLASS_CLOSURE.md) | `e7cdccf47b5c117c633a82739cc07b23d727aac40e8b53b813f52d078b44b17f` | F, fixed-rank cycle finiteness and fixed-orbit characterization |
| [PR192_LATE_HEAD_REVIEW.md](reviews/PR192_LATE_HEAD_REVIEW.md) | `7f68f600562892ec20149300235c6317c7c0215c860571dad01ce82ddc3084b3` | Updated PR192 source comparison and elementary no-successive-squares proof |
| [DURATION_SOURCE_ADDENDUM.md](../../research/unconventional-20261126/defects/DURATION_SOURCE_ADDENDUM.md) | `fcf7614ed459beeab49bafc0da9951011d180463681cb8a000c282329e5bb610` | Independent derivation of the prior signed-fragment duration estimate |
| [REVIEW_RESET_RIGIDITY.md](reviews/RESET_RIGIDITY_REVIEW.md) | `544bf5d3227f714de3d2599b07eff15dc7b907a949a08a1fdf9c551ca0ea36bd` | Independent review of the single-block relative and sharp profile results |
| [REVIEW_PERSISTENT_RESET.md](reviews/PERSISTENT_RESET_REVIEW.md) | `73372194fb344af0f355499f08acc804570db38388ab5a6bd72bd0de0ceb34cc` | Independent review of D and all-phase cyclic gcd retention consequence |

For the elementary two-boundary obstruction, the two positive neighbors of odd M≥3 have gcd two and precisely one has dyadic valuation one. If their product is divisible by 2ᵇ, the other neighbor is divisible by 2ᵇ⁻¹, whence 2ᵇ⁻¹≤M+1. Combined with 2ᵇ−1≥2M+1 this gives equality.
