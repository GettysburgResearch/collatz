# Weak scalar orientation collapses the mixed-base digits

**Claim.** Assign each of the seven letters a strictly increasing function
from the ordinary natural numbers to themselves. If all eleven mixed-base
Collatz rules are oriented weakly, the five digit functions are the identity.
This holds for left-outermost and right-outermost function composition.
Thus there is no uniformly strict rule. The deduction of the identity
functions is stronger than the latter conclusion.

The statements `forwardCollapse`, `reverseCollapse`, and `allRulesEqual`
are formalized in [MixedBaseRigidity.lean](MixedBaseRigidity.lean) using
only Lean's standard library. Here capital letters denote the functions
of the corresponding ASCII symbols, composition in juxtaposition is
left-outermost, and the pointwise comparison below points from a right
side up to its left side. The proof uses just five rules:
`bd→gd`, `cg→cab`, `ag→fa`, `af→eb`, and `ce→cb`.
[Authors’ source rule list](https://github.com/emreyolcu/rewriting-collatz/blob/main/rules/collatz-T.srs)

A strictly increasing \(h:\mathbb N\to\mathbb N\) satisfies
\(h(n)\ge n\), and \(h(n+k)\ge h(n)+k\). If it fixes a cofinal family
of arguments, it fixes every argument. Every such function reflects
weak order and has cofinal image.

**Forward composition.** The rules at the two ends give
\(AB\le G\) and \(GD\le BD\). Thus \(A(BD(n))\le BD(n)\),
forcing A to be the identity. The three further rules give
\(F\le G\), \(EB\le F\), and \(B\le E\). It follows that
\(B(BD(n))\le BD(n)\), so B is the identity. Now \(GD\le D\)
forces G to be the identity. The inequalities \(E\le F\le G\)
and extensivity then force E and F to be identities as well.

**Reversed composition.** The same five rules now give
\(G\le B\) and \(BAC\le GC\). Cancelling the strictly increasing B
from \(BAC\le BC\) gives \(AC\le C\), hence A is the identity.
The remaining comparisons are \(F\le G\), \(BE\le F\), and
\(BC\le EC\). From \(BE\le F\le G\le B\) we obtain
\(EC(n)\le C(n)\). Consequently \(BC\le C\), so B is the identity.
Then \(G,F,E\) are all bounded by the identity and are extensive, as
before. Neither delimiter is asserted to equal the identity.

## Source and scope

The published YAH nonexistence theorem for natural matrix
interpretations concerns an earlier *unary* encoding. Their 11-rule
mixed-base system is the system used here. All eleven subsystems obtained
by deleting one rule admit termination proofs in their paper.
[Yolcu–Aaronson–Heule, Theorems 3.8 and 3.17, Sect. 4.3](https://arxiv.org/abs/2105.14697)

Nashida's later preprint and the related natural-matrix literature concern
affine matrices, including dimensions beyond one. The scalar theorem
above permits arbitrary nonlinear strictly increasing functions. It
makes a statement about the digit functions themselves under weak
orientation. It does not cover arbitrary multidimensional nonlinear
maps. The local PR 6 inventory records the earlier method leads without
admitting its missing legacy certificates as proof dependencies.
[Nashida’s companion repository](https://github.com/harappa/collatz-matrix-interpretation-barriers)
[Later natural-matrix discussion](https://rstation.ai/problems/collatz/papers/59)
[PR 6 source inventory](https://github.com/GettysburgResearch/collatz/blob/4810a0771da61a1cb609ef8707dfcf7f0f6e666f/research/termination-frontier/CLAIM_INVENTORY.md)
