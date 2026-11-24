# Round-three cycle checks

The mathematical statements and their proofs are scoped individually in the two source notes. The full-denominator transport lower bound is a written proof. The finite signed-product kernel was compiled. The modified-carry model is a written construction on a different map.

| Source in research/astra-global-closure-20261124/round3/cycles | SHA-256 |
|---|---|
| README.md | 0c52480edc174b1cd6addc893797652638e10af7c142e99934264841527b2c75 |
| CyclicFlux.lean | c5076fc5ac18d519ecb6a469d7751f71d84411f74a2ea7da4213f0567a836568 |
| RotationProduct.lean | 7333ffec11fb7b4053b9ae662fa58decadf6f0c6715b4f17dce63aa97438ab13 |
| check.py | 1a29ca92b06dd36ad2d42166bba451337d6e8187cc571e870990e4abfd943c63 |
| CONGRUENCE_MODEL.md | 98eb973ab20fb1fcc4dc5736a3bd145d944ae3229bd0a54b7d96591d0b8af3a7 |

Lean 4.34.1 at commit 5045d0056413266e57c625dcd7c365b10e377c52 and Mathlib at d13f23b723b8a846827a245b89c10fc7d3f11612 compiled RotationProduct.lean with warningAsError enabled. The process exited zero. All three public theorems printed only propext and Quot.sound. The recorded output is [lean.log](lean.log).

Both ordinary and optimized Python ran check.py to completion, each with exit zero. The default bound of 13 covered 1,131 primitive positive contracting necklaces, 12,282 nonidentity rotation products and 13,413 physical-word comparisons. Breadth-first search obtains actual shortest swap distances in each full equal-weight layer. Its labeled words give all alignments with the chosen mechanical reference. The control checks exact signed products, aggregate valuations and the exponential form of the complete denominator inequality using integer arithmetic. [control.json](control.json)


The later CyclicFlux.lean kernel formalizes the core $R^2\le2K$ in the transport estimate. It takes any closed integer walk with increments at most one in absolute value and with total absolute flux at most $K$. It permits two arbitrary arc lengths cut at any point where the flux exceeds or equals its initial value. For potential $V(x)=x|x|$, two applications of the arc bound and closure give $2(V(\max f)-V(\min f))\le2K$. Since $(\max f-\min f)^2\le2(V(\max f)-V(\min f))$, the range bound follows. The written argument in README.md attaches this walk to the swaps by conservation. The module compiled independently with the same pinned toolchain, warnings as errors and exit zero. Its public theorem reports only propext, Classical.choice and Quot.sound. [flux-lean.log](flux-lean.log)
