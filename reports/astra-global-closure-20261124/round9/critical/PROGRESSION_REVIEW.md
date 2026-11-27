# Independent check of the least-disagreement progression

For $u\ge0$ the ordered certificates have the following exact coefficients.

| Integer | Constant | Coefficient of $u$ |
|---|---:|---:|
| $q$ | 163815229 | 1377495072 |
| $s=(3q-1)/2$ | 245722843 | 2066242608 |
| $z$ | 383076351 | 3221225472 |
| $3q-z$ | 108369336 | 911259744 |
| $T^5(3q)=T^{30}z$ | 414657299 | 3486784401 |

Set $t=1+16u$ in `CriticalCycle.small_multiple`. Then $T^{26}z=s$, $z>0$, $3\mid z$, and $z<3q$. Since $s=16m+11$ for $m=15357677+129140163u$, `CriticalCycle.recentered_meeting` gives $T^4s=T^5(3q)=27m+20$. Thus PR192's smaller-multiples theorem and bad-upper theorem contradict a least disagreement at every $q$ on the row. This implication requires no cycle or bounded-trajectory assumption. [Physical identities](../../../../research/astra-global-closure-20261124/round9/critical/CycleOrder.lean)

The four fixed source exclusions displayed by PR192 are disjoint from the row. Its sources are 5 modulo eight, 29 modulo 32, and 181 modulo 4374. These exclude the rows 7 modulo eight, 1 modulo 128, $-21$ modulo 8192, and 3007 modulo 4374. Also $q=1\pmod9$. For $n=3q$, $v_3(n)=1$, $v_2(n+1)=3$, and $(n+1)/8=3\pmod4$. The corresponding first-run exit parameter is 1 modulo four. PR192's other first-exit ternary conditions fail here, and its second-run theorem requires the first exit parameter to be 3 modulo four. PR205 can recenter this first exit to $s$ but does not resolve the new row through that statement alone. [PR192 source and exit conditions](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/README.md) · [PR205 ordinary path](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/README.md)

Two narrower baseline comparisons can be checked at the first member. In the round-eight elementary forward construction, $p=k+2$ and $r=5p+13\ge23$. Its requirements $171z<Q=(9q+1)/2$ and $z\ge2^r-1$ fail at $q=163815229$, since $Q=737168531<1434451797=171(2^{23}-1)$. For the round-eight guarded anchor $q=a+2^{h+2}t$ with $t>0$, the two actual anchors must reach the $1,2$ cycle by $h$. This forces $3a\le2^{h+1}$, so $a=q\bmod2^{h+2}$ and $0\le h\le25$. Only $h=19,20$, both with $a=237373$, pass the height test. Their ordered clock-$h$ endpoints are $(2971,240614)$ and $(4457,120307)$, respectively. These comparisons concern the specific baseline constructions displayed in their source notes. [Round-eight inverse construction](../../../../research/astra-global-closure-20261124/round8/unit/README.md) · [Round-eight guarded anchor](../../../../research/astra-global-closure-20261124/round8/paired/PAIRED_PREFIX.md)

## Final proposal proof review

The Lean source reviewed has SHA-256 `d5272583018fcdbd0f18986fdd10a50e2c46e2b5d46f0bdc69cc81b562ff050d`. `ReturnCertificate` records a positive ordinary source, a strict safe bound and equality of two actual shortcut iterates. Its two safe alternatives match PR192's `good_cutoff` and `smaller_multiples_good` including strict inequalities. `good_run` transfers basin membership in both directions, so a hypothetical least discrepancy rules out every such certificate. `progressionCertificate` supplies the smaller-multiple alternative and the ordered clocks $(5,30)$ unconditionally for every natural parameter. This proves exclusion as a least discrepancy. The certificate does not itself exhibit an iterate equal to one. [FinalProposal.lean](../../../../research/astra-global-closure-20261124/round9/formal/FinalProposal.lean)

The forward cover implication applies existence of a least discrepancy to any positive counterexample. The reverse implication is vacuous when every positive integer reaches one. The universal cover therefore remains exactly as strong as ordinary Collatz. The strict replay lists the three expected theorem signatures and eight axiom inventories for this file, with every printed dependency among `propext`, `Classical.choice`, and `Quot.sound`. [Lean output](../lean/FinalProposal.log) · [Eight-module receipt](../lean/receipt.json)
