# Completed-mark routing checks

The [mathematical note](../../../../research/astra-global-closure-20261124/round6/renewal/README.md) gives the exact regular degree, Haar change of variables, Fourier conductor decomposition and pointwise scalar factor separating the true dictionary mass from the inverse sampling law. Korobov's Theorem 4 is the external input for the growing-precision bound. I read its original English statement and displayed sum on journal pages 671–672, and compared Vandehey's Theorem 2.4. The applied form uses an unspecified positive absolute exponent constant and a strict subrange shared by both formulations. The short ordinary replay does not test the large-\(k\) asymptotic, the analytic theorem, PR146's marked renewal tail, or PR200's pressure certificate.

The [Lean file](../../../../research/astra-global-closure-20261124/round6/renewal/MarkedRouter.lean) was compiled from source with Lean 4.34.1, revision `5045d0056413266e57c625dcd7c365b10e377c52`, using `-j1 -DwarningAsError=true`, an empty project output directory, and the previously built Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612` and its package dependencies. Exit status was zero. Its seven selected declarations verify trace composition, the first six-clock return over its entire cylinder, the padded pair of physical paths, ordinary intermediate divisibility and the full arbitrary-length paired reconstruction from the final affine congruence and target residue. The [axiom inventory](MarkedRouter.log) consists of subsets of `propext`, `Classical.choice`, and `Quot.sound`. The module does not claim a formal Haar or exponential-sum theorem.

Python 3.12.14 executed the [finite checker](../../../../research/astra-global-closure-20261124/round6/renewal/check.py) with `-X utf8 -B` and again with `-O -X utf8 -B`. Both runs returned zero, with byte-identical [JSON output](controls.json). Explicit exceptions enforce all conditions in both modes.

| Arithmetic coverage | Executed result |
| --- | --- |
| Every odd-unit class of the parent modulo 243, with \(N=162\) | 324 complete two-block trajectories, including every intermediate odd mark, the true clocks, counts and both endpoints |
| Every four-block label sequence at \(N=162\) | 26,244 integer carries, covering exactly 13,122 unit classes modulo \(3^9\), twice each |
| Five supplied ordinary roots at ternary precision two | All 180 descendants distributed equally across the six unit classes, with 15 full 994-clock paired paths replayed |
| Three supplied roots at precision three | All 17,496 descendants distributed equally across the 18 unit classes, with 9 full 4,407-clock paired paths replayed |
| Appending one six-clock elementary word at precision three | 1,944 legal outcomes among 17,496, exactly the predicted \(1/9\) fraction |
| First-return renewal on every odd binary cylinder through a 14-clock horizon | 16,384 odd cylinders, 1,169 positive mark visits, 36 nonempty completed rows and 14 exact convolution equations |

The two moderate-precision checks use complete periods chosen for their indicated conductor, so the observed equipartition is exact there. Their parameters do not purport to attain the limiting short-sum regime. No trajectory data were reused as a uniform-in-height proof.

| File | SHA-256 |
| --- | --- |
| Mathematical note | `ab8e342e3b4d95bc509fefcf0dfdfc72f369b33741f644a6856e503e73174558` |
| Lean source | `049f1726d9cadd9049183b059ea465d4e69009abc3a01086384cd3dca30d53d2` |
| Lean output | `346678b1b3e4c60724f5ec306179a19ae43c2389e86475ac42b69f87d791d7fb` |
| Python source | `83048558581904efb0a3a8a9b0bb8e56b9000e7d2e18351ec4fcbf8bb4ab74cf` |
| Python output | `e336079cce323bded3f02ab023e8ad3c475422364cf34db98f5a1d94bb474312` |

The accompanying [independent arithmetic check](ARITHMETIC_REVIEW.md) identifies its two source hashes, imports and verified clauses separately.
