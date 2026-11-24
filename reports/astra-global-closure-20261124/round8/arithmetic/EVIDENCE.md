# Arithmetic execution and scope

The arithmetic manuscript applies Evertse's Corollary 1 on p. 227 to primitive signed nondegenerate integer zero sums. Its first divisor identity and projective pivot divisibility are also finite Lean results. The superexponential outside-prime conclusion is a proposed written theorem using the published result. No computation here establishes an infinite conclusion. The published PDF inspected for the theorem has SHA-256 5b02e0e31c546f7f8c6c34071b2caa4d7137be24f16d11d483cdcc65377b2f6d. [Original paper](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

| Item | SHA-256 |
|---|---|
| Manuscript README.md | 734450af1557edb1a3cbfaba7fc90ae097d4244015711a144bdb826da6a8414f |
| SparseTerminal.lean | 1c52c43b61df48015ab99e2b102045ba37b50613c024c86a2f686e803e38f5b6 |
| SparseTerminal.log | a814740c31cb835a3e9ca8722d62776ab86816e8c52528634c38cad4ce9981b8 |
| check.py | b7e8c8d1ccd45700439eda40454e21a94062db861ea8e12416907c853831d120 |
| controls.json | 2c6afba3b7a74ea1ff763739928bd47487ea0db67b090b6784688ed361e799c4 |

The arithmetic lane compiled the module with Lean 4.34.1, Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612, -j1 and warnings as errors, writing the project object into a fresh temporary directory and reusing the installed library objects. All 12 selected axiom reports use only propext, Classical.choice or Quot.sound. Ordinary and optimized Python independently returned identical bytes for the reported controls. The 624 signed physical tuples check 6,364 full-divisor inequalities as exact divisibilities, including nontrivial content, deletable zero subsums, moving root coefficients and first-hit constructions. [Compiler output](SparseTerminal.log) · [Control output](controls.json)

The closest prior bounded-odd papers are the two arithmetic files in PR192, full commit b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b. Its moving-target note has Git blob 33302d885615164f124af03ad7d47feb932af390. The fixed-rank multiplicative Pell result is PR193, commit bdd4409062bc02416ff6941f8d5690b800068cb3. [Bounded-odd lift result](https://github.com/GettysburgResearch/collatz/blob/b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b/research/astra-global-budget-20261124/arithmetic/README.md) · [Moving targets](https://github.com/GettysburgResearch/collatz/blob/b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b/research/astra-global-budget-20261124/arithmetic/LATEST_CONNECTIONS.md) · [Pell input](https://github.com/GettysburgResearch/collatz/blob/bdd4409062bc02416ff6941f8d5690b800068cb3/research/astra-deep-closure-20261124/arithmetic/README.md)
