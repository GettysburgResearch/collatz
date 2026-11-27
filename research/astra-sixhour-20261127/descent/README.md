# Original-source descent at unrestricted upper rank

The unresolved source is a least positive \(z\equiv17\bmod48\) with \(3z\) in the basin of one and \(z\) outside it. PR197 supplied the quantitative return and the earlier progress for two-odd upper words. This packet uses the given \(z\) and its actual upper word throughout.

| Result | Quantifiers and status |
|---|---|
| [Full signed reduction and its limits](UPPER_WORDS.md) | Every finite upper hit at every positive ordinary source admits full physical signed reduction after at most one upper lap per existing odd departure, unless the lower already hits one. Six related time, height, and lifting assertions appear in [SignedCenter.lean](SignedCenter.lean), with the all-rank ordinary application in [LapBudget.lean](LapBudget.lean). Fixed convergent suffixes furnish unbounded negative exits at each first-hit rank at least four. |
| [High simple-trajectory distortion](DISTORTION.md) | All odd entries at least \(2^{71}\) on any simple trajectory have reciprocal sum less than \(0.53\). A simple prefix above this floor has multiplicative correction below \(6/5\). This yields unpadded full original-word lifting, binary reserve larger than \(\log_2 z-41\) at a least nonperiodic defect, and a negative exit after one genuine upper lap. The occupancy recurrence is an explicit proof with a finite integer/rational certificate. |
| [Paired translated intervals](PAIRED_INTERVALS.md) | On every interval of length \(N\), all but \(O_\epsilon(N^{H_2(\log_3 2)+\epsilon})\) members of any chosen set of canonical parents have an earlier member in that set with actual counted meetings on both arms. The common prescribed deadline is \(O_\epsilon(\log N)\). The first-passage arithmetic kernel is [FirstPassage.lean](FirstPassage.lean). |
| [Positive cut-walk depth](CUT_WALK_DEPTH.md) | At every fixed original upper first-hit rank at least three, actual positive parents require an unbounded number of steps even to encounter any smaller canonical query. A source-qualified growing-rank sequence costs a fixed proportion of its upper first-hit clock and log-height. |
| [Charge, minimality paths, and fixed-target multiplicity](PAIRED_CHARGE.md) | The shifted charge exactly characterizes ordinary contextual paths using a prescribed list of smaller canonical jumps at convergent data. Every length is obstructed at 65. Every convergent canonical pair beyond 161 permits a construction using three seed types. The finite control obstruction is in [Charge.lean](Charge.lean). |
| [Fixed-endpoint finiteness and exact cycle hit costs](FIXED_RANK_LAWS.md) | Every actual positive terminal has finitely many inverse words of bounded leading cost. In the bounded alternative, two sets of good tripling queries strictly below the original global floor have the same total first-hit clock excess and specified odd-count excesses. These are written theorems. |

**Remaining implication.** The strict positivity of the original lower endpoint \(2^d+c\), the reserve \(d\), and the sparse number of least paired representatives do not force a positive smaller canonical representative for a *specified* least bad lower. The complete contextual word construction for convergent controls uses access from that lower to one. No such access has been established for a hypothetical least defect.

## Replay

From the repository root run the five independent checks below. Their outputs are the five JSON receipts in [the report directory](../../../reports/astra-sixhour-20261127/descent). They use explicit guards and work identically with Python optimization enabled.

~~~sh
python -B research/astra-sixhour-20261127/descent/check_pairs.py
python -B research/astra-sixhour-20261127/descent/check_upper.py
python -B research/astra-sixhour-20261127/descent/check_distortion.py
python -B research/astra-sixhour-20261127/descent/check_cut_walk.py
python -B research/astra-sixhour-20261127/descent/check_cut_depth.py
~~~

Use Lean 4.34.1, Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`, and `-DwarningAsError=true -DautoImplicit=false`. Build the preexisting `research/astra-unconventional-20261126/descent/Portal.lean` to a fresh object directory. Add that directory and the pinned Mathlib dependency paths to `LEAN_PATH`. Compile `FirstPassage.lean`, then `Charge.lean`; independently compile `SignedCenter.lean`, then `LapBudget.lean`. The independent `AffineDepth.lean` checks the geometry of arbitrary bounded numerical ordinary words. All public theorems carry axiom inventories. [Independent fresh compiler receipt](../../../reports/astra-sixhour-20261127/descent/lean-audit.txt) The dependency on the previous packet is the positive Collatz map, clocks, grades, and their elementary concatenation identities from `Portal`.
