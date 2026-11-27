# Complete visitor clocks on selected ordinary Collatz targets

The two notes prove lower bounds for the proportion of positive sources having *no* smaller positive visitor at the listed targets, even when visitors may use arbitrary finite clocks. All maps use the positive shortcut convention. An ordinary orbit may still meet a smaller orbit later, and upward escape remains possible.

| Result | Sources and targets | Quantifiers |
|---|---|---|
| [Growing scaled target range](SCALED_TARGETS.md) | More than one third of all starts in an integer shell protect every integral \(Y=2^\delta(3/2)^j(n+1)-1\) with \(2^\delta(3/2)^j\le X^{1/50}\). More than one quarter of the shell consists of protected multiples of three. | Both fractions are asymptotic lower bounds with the explicit larger rational constants in the note. Every listed target is protected for the same source. |
| [Maximal postpeak classification](POSTPEAK_VISITORS.md) | For \(H\ge600,\ |w|\le H/100\), an equally long, same-offset word with more odds gives every start in \(O^H w\) a smaller visitor at the endpoint. On a maximal word more than one third of the source cylinder has no smaller visitor through that endpoint. | Both fixed-cylinder density and a uniform finite-shell statement for \(H\le(\log_2 X)/100\) are proved. In the uniform range more than one quarter of each maximal cylinder consists of protected multiples of three. |

The proofs combine the preceding exact common-scale counts and signed rigidity with Weaver's long-arrival method. Weaver's prior results include complete-orbit transfer, first-meeting laws, and the numerically stronger protection proportion above \(0.510269713938\) on a pure odd ascent. PR201's earlier common ternary event covers a broader family of affine shifts on deep divisibility cylinders. PR192 supplies earlier specific compensated word collisions. The new claims here concern all-clock protection on a growing simultaneous scale range and the classification of every prescribed postpeak word in a linearly growing range, including uniform finite shells. [Weaver 177/v1 §§7–8](https://rstation.ai/problems/collatz/papers/177/v1) · [Weaver 178/v1 §§2,7](https://rstation.ai/problems/collatz/papers/178/v1) · [PR192/PR201 provenance in the postpeak classification](../POSTPEAK.md) · [Common-scale proportions](../../../root/phase5/COMMON_PROTECTION.md)

These density theorems are written mathematical deductions. The signed trap, native equal-offset criterion, sharp cone and finite signed origins have separate kernel-checked components. The accompanying standard-library program verifies exact entropy margins, source-cylinder arithmetic, all 511 words through clock eight in the stated finite sample, and 253 signed stopped prefixes in its displayed finite range. It does not infer an all-clock statement from these samples. Run the command below from this directory. [Finite controls](CONTROLS.txt) · [Verifier](check_allclock.py)

~~~sh
python -O -B check_allclock.py
~~~
