# Ordered cycle gap verification

**VERIFIED locally for the six Lean declarations and two exact rational controls.** Lean 4.34.1 accepted the cycle module without warnings. The six axiom reports use only standard axioms. The sorted rotation for arbitrary positive ordinary cycles in the exceptional strip is a written input from the frozen PR192 proof. The Wu–Wang application, uniform pointwise stretch bound and construction of rational cycles with both orders and linear variation are written arguments.

| Replay from the repository root | Result |
| --- | --- |
| Lean on the cycle module with the supplied Mathlib search path | Exit 0. Six axiom reports. |
| Python 3 on the cycle control script | Exit 0. Both rational controls passed. |
| Python 3 with optimization enabled on the same script | Exit 0. Identical output. |

The 41-phase control has seven sorted changes, seven high odd phases, 30 high physical phases and nine high strict records. The new 306-phase control has 103 sorted changes, 51 high odd phases, 75 high strict records and reduced denominator of bit length 476. An independent reconstruction of the integer carries and sorted orders reproduced the 306-phase counts.

The checked arithmetic theorem assumes an increasing lifted rank list and its affine recurrence. It proves the complete scale budget by deriving the adjacent gap relation and its divisibility, rather than taking divisibility as a hypothesis. Showing that every remaining ordinary cycle violates that budget is open. The written rational construction supplies no ordinary least bad source. [Module](../../../research/astra-ultra-closure-20261125/cycle/RankGaps.lean) · [Proof and hypotheses](../../../research/astra-ultra-closure-20261125/cycle/README.md) · [Exact controls](../../../research/astra-ultra-closure-20261125/cycle/check.py)
