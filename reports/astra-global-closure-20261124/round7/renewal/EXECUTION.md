# Central fibers and short suffixes

The standalone module compiled in a fresh temporary project output directory with Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The invocation used `-j1 -DwarningAsError=true -o <temporary>/ShortSuffix.olean`, the provisioned Mathlib and package oleans, and the native shared library directory. No project olean was imported. The compiler exited 0. All 12 selected axiom inventories use only `propext`, `Classical.choice` and `Quot.sound`, each on the subset shown in [the compiler log](ShortSuffix.log).

The checked declarations cover the affine word identity for physical inputs, preservation of parities and both labeled arm translations, full ternary congruence for equal words, the halving lower bound, suffix rigidity at a small original endpoint, the linear deadline at a nonperiodic target, the stronger deleted-tail obstruction, the dyadic-cell height gap, the physical terminal checks for 1 and 5, and generic edgewise invariance/separation for a partial parent. The external F and H floors, the asymptotic pigeonhole, PR146's general steering bounds, and the claimed completed counts are written mathematics.

Both commands below exited 0 and produced byte-identical JSON. The checker uses explicit exceptions for failed conditions.

```bash
python -X utf8 -B research/astra-global-closure-20261124/round7/renewal/check.py
python -X utf8 -O -B research/astra-global-closure-20261124/round7/renewal/check.py
```

The four exact rows at ordinary targets 1, 5, 7 and 11 had 317 eligible first-arm starts in the stated unit class and half-offset window. Eight nonroot companion fibers supplied 70 simultaneous lifted starts. The checker traced both arms, verified equal counts and the full fine-cell gap, and parsed the entire path through completed marks for each. It also checked 8,316 suffix comparisons and both terminal coalescences. At target 1 the row $(e,p)=(68,34)$ includes seven selected starts whose companions land at 2 with 31 odd inputs. Their common extension ends, with 37 odd inputs on both arms, at target $1062937790459668787$ and its fivefold multiple. The exact dyadic center is $767/67108864$. [Complete finite output](controls.json)

| File | SHA-256 |
|---|---|
| Research README.md | `fe45e78f43544529a4cb25dcf283728490bce6ec29f9de5e534c5a90cd860ca6` |
| ShortSuffix.lean | `ad6268d02bcd5cbd01331203d36df7ed3204038bf3d952e58dc701b0a0695637` |
| check.py | `894ea14c5c7e6405bc0d1043735555a6388d041f34d975dfe15069ac208da137` |
| controls.json | `07480918557116f67ebc20d8217395e0db72d6ccadbcffc574d11d911f2fae16` |
| ShortSuffix.log | `2da2be06eb422650b1f979242e7bc0ad663fda4b315336b6384517e6991c21ed` |

These are local execution receipts for the round-seven renewal lane. The manuscript's standard and formal references are scoped in the [research note](../../../../research/astra-global-closure-20261124/round7/renewal/README.md).
