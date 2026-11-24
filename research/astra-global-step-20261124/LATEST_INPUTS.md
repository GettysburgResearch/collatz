# Frozen inputs to the global-step continuation

This continuation starts from our PR188 checkpoint
`f98262be4ea40068dc88c779a767a9400a8bcaa3`. The table records the new
snapshots used to choose and develop the three research directions. A source
inspection is not a blanket review of a branch, and no neighboring result
inherits a formal-proof status from an imported Lean file.

| PR | Full head inspected | Relevant paths and role |
|---|---|---|
| 182 | `9b02334f27ff59694a91fe7f018e0aaabad7620b` | `research/astra-round13-20261124/{DEFECT_COVER,LINEAR_HORIZON,LATEST_BAND}.md`: repeated-word covers, finite-clock merger obstruction, and the summable residual section. |
| 192 | `d2081d1cd2410e6004eaee9f9b13c5553afaf3f4` | `research/astra-closure-attack-20261124/{DESCENT,DESCENT_EXTENSION,FIXED_SOURCE,SOURCE_EXTENSION,CYCLE_CLOSURE,CYCLE_EXTENSION,LATE_SOURCE_CONNECTIONS}.md`: ordinary smaller-source constructions, same-source arithmetic restrictions, and complete numerical denominators. |
| 193 | `c6cb5e66516a86c33a757154983bbddc822510de` | `research/astra-universal-descent-20261124/escape.md`: translated finite-fiber compression and its remaining same-law upper-bound obligation. |
| 196 | `27d03cfe902660e06604eb55bb28ca3d2754ff48` | `research/astra-orbit-cycle-20261124/cycles/ROTATIONAL_EXCLUSION.md` and `mergers/TWO_ANCHOR_MERGERS.md`: complete-denominator matching factors, the pinned two-log estimate, and arbitrary-clock merger costs. |
| 197 | `2fb1f11c959e35eba875338833d84969222dc089` | `research/ayh-resource-reset-20261124/positive-section/{README,CRITICAL_SECTION,MarkedPredecessors}.md`: the eight-surplus critical section, its inverse rows, and the original-floor issue. |
| 198 | `c76acf99ba3fb05e7cc07ca7db7e467954c2d950` | `research/astra-frontier-20261124/{MINIMUM_ARC,GLOBAL_CLOSURE_ATTEMPT}.md`: minimum-arc lower bounds and merger-cost restrictions. Used as context, not as an input to a new theorem. |

The latest open-PR listing was queried again after the research work began.
The inspected heads above remained unchanged. PR189's attribution correction
at `a390a1a4c75ee95db98b4b683d17c503f4e4a118` was also retained as context:
the stationary strict-collision gap was already present in PR180.

## What changed the mathematical target

**The section reduction does not identify a decreasing section return.**
PR197's critical marked set has eight valuation surpluses. Convergence of that
set is equivalent to universal convergence, and each large point in it has a
first odd image much smaller than itself. That image need not be in the
section. The inverse-row constructions can return to the section above the
original floor. Thus strong induction cannot be closed by concatenating the
two facts alone.

**A smaller state must stay attached to its initial source.** PR192 supplied
finite mergers and an infinite separated-block affine shadow. The persistent
descent theorem in this packet instead retains one smaller natural number
through every transition of an explicit two-state graph. This is why its
infinite-walk conclusion is useful. The graph's language still has to be
distinguished from the full return language.

**The cycle denominator is the full reduced denominator.** Our rotation
argument uses the literal common denominator at every phase, and applies to
every nonzero offset. It does not discard prime powers or assume a coprime
pair of total and odd clocks. Only the small-offset corollary imports
PR192's grouped-window theorem. The finite denominator inequalities do not
use that analytic input.

**The residue law must come from the same forward source.** A stationary
inverse chain or a fresh random source can have a useful Haar law without
describing a putative exceptional forward orbit. The residue statements in
this packet explicitly retain the forward affine equations in the joint
stationary limit. Their finite arithmetic decoder is separate from the
measure-theoretic consequences.

## Literature and attribution

The written cycle asymptotics use Matveev's two-logarithm estimate through the
exact PR196 pin above. The grouped-window corollary retains PR192's stated
dependence on Evertse. No external large numerical verification is replayed.

We also checked the public rStation manuscripts
[84](https://rstation.ai/problems/collatz/papers/84),
[137](https://rstation.ai/problems/collatz/papers/137), and
[138](https://rstation.ai/problems/collatz/papers/138).
The first supplies a relevant suffix-slope precedent. The latter two already
contain the multiplicative-rank and prime-return estimates independently
rediscovered during this continuation; those rediscoveries are not presented
as new results. These are manuscript attributions, not assertions of journal
acceptance or independent verification of every result in the papers.
