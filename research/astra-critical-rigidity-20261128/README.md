# Ordinary-source rigidity and complete rotation plateaus

**Collatz remains unresolved.** This exploratory packet studies actual ordinary trajectories, the cost of following several rational reference arcs, and the full rotation plateaus used to compare positive cycles. It records precise written proofs and their formal kernels. It does not claim that the remaining coverage hypotheses hold for every positive integer.

The map throughout is the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

Native time counts these steps. Grade counts odd departures. On positive rationals with odd denominator, parity is the residue modulo two. The main repository was frozen at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; the [intake](../../reports/astra-critical-rigidity-20261128/INTAKE_PINS.json) records forty open research heads, without claiming to verify every historical proof.

## First mathematical checkpoint

| Claim | Statement | Evidence and boundary |
|---|---|---|
| O1: sharp source height | A physical prefix of length D, encoded by a bounded number of powered words with total template length o(D), has liminf log₂(source)/D ≥ 1 unless a piece starts at its exact affine fixed point. | [Written proof](literature/POWERED_WORD_HEIGHT.md), using the classical rational Subspace Theorem. The actual word formula and all changes of reference are checked in Lean. The asymptotic argument is not formalized. |
| O2: open rational arcs | For at most K separated reference arcs of height exp(o(D)), a reduced positive source A/q, gcd(q,6)=1, satisfies liminf [log₂ max(A,q)+(K−1)log₂ q]/D ≥ 1. | [Written proof and complete denominator ledger](literature/OPEN_ARC_HEIGHT.md). The interiors may be arbitrary actual words. Universal low-height reference covers remain open. |
| P1: joint predecessor classification | Fixed positive targets a,b have arbitrarily large odd joint predecessors s and 3s with a bounded total grade iff both targets are ternary units and one visits the other. | [Written classification](ordinary/PAIRED_SOURCE_GRADES.md). It distinguishes forward comparability from merely sharing a future. The explicit family proves sufficiency; the formal clock bound proves the obstruction used for necessity. |
| P2: an unmatched pair cannot hide its clock | For odd s, if Tᵗ(s) and Tᵗ(3ʳs) stay distinct through k, then k ≤ [2(G+r)+1]G, where G is their total grade through k. | [Connected Lean proof](ordinary/PairedClock.lean), including the actual map, affine intercepts, exact ternary-unit cancellation, and a nonzero integer discrepancy. No external theorem is used. |
| C1: full plateau pressure | A relative plateau of the integer tripling ceiling has bounded cutoff ratio, asymptotically below 38, even if every periodic component is replaced. A positive relative width forces a strict exponent loss in the reduced clock denominator. | [Written proof](cycles/COMPLETE_PLATEAU_PRESSURE.md), finite directed rational quadrature, and BLS's two-logarithm estimate. This does not yet improve the prior ordinary-cycle width bound three. |

The source-height result concerns the full dyadic precision at the original source, including long downward stretches. For a fixed run count, the least positive realizer of a long parity word has logarithm asymptotic to its full length. The onset is ineffective: small words can have much smaller realizers. The general arc version preserves the complete additive cancellation at every join; independently choosing convenient endpoints would not satisfy its hypotheses.

For the paired-source result, incomparable targets obey the explicit finite bound

\[
s\le\max(a,b)\,2^{(2G+3)G}.
\]

Oddness matters. Doubling an existing witness adds only even departures, so unrestricted even sources could grow without a larger grade. In the comparable case, the ordinary family `s=23+32t` supplies the common five-step endpoint `20+27t`, after which a congruence modulo 81 sends both arms to a prescribed ternary-unit target with one extra odd departure each.

The plateau result applies to the **complete cutoff interval**, rather than the lifetime of one fixed component. Its angle-conditioned entropy bound is retained at both endpoints. A clock with denominator `p=L^(1−o(1))` forces the relative plateau width to tend to one. The known general lower bound on the period is much weaker, leaving the ordinary-cycle obstruction open.

## Attribution and proof boundaries

PR212 already proves the closed-cycle `1/K` denominator rate for moving low-height reference arcs and stronger clock-sensitive statements. O2 recovers that result but does not claim it as new. PR213 already gives the native extinction equivalence, a width-three obstruction, pooled periodic density decay, and an asymptotic factor-two lifetime for one unchanged ceiling component. The present C1 argument addresses replacement of those components. P1 develops the fixed-target question and ordinary control from PR201; the earlier two-ray mechanism and supplied-source merger formulas remain credited in its note.

The [primary-source refresh](literature/PRIMARY_SOURCE_REFRESH.md) distinguishes recent manuscript reports, finite computations and the exact external inputs used here. No announcement of progress on another problem is treated as a Collatz lemma. The [coordinating review](../../reports/astra-critical-rigidity-20261128/checkpoint1/REVIEW.md) records the independent reconstruction and current evidence.

## Replay

Use Lean 4.34.1 and Mathlib source `d13f23b723b8a846827a245b89c10fc7d3f11612` with its compiled dependencies. The runner builds every selected packet module into a fresh temporary directory, then imports those objects into a fresh public-root axiom audit:

```sh
python -X utf8 -B research/astra-critical-rigidity-20261128/check_lean.py \
  --lean /path/to/lean --mathlib /path/to/mathlib \
  --receipt /path/to/lean-receipt.json
python -X utf8 -B research/astra-critical-rigidity-20261128/literature/check_open_arc_height.py
python -X utf8 -B research/astra-critical-rigidity-20261128/cycles/check_complete_plateaus.py
python -X utf8 -B tools/validate.py
```

The exact checkers use explicit guards and produce the same results with optimized Python. Their finite scope is recorded in the receipts. Cached third-party objects are reused; a cold Mathlib rebuild and an independent LeanChecker replay are not claimed.

At initial publication, the completed central Lean receipt covers all thirteen public roots of `AffineOrbit.lean`. The author compilation and coordinator main-root check of `PairedClock.lean` preceded shared-memory pressure; the separate central fresh replay of all five public roots is pending. The [checkpoint review](../../reports/astra-critical-rigidity-20261128/checkpoint1/REVIEW.md) keeps these evidence boundaries explicit.

## Remaining decisive questions

The new source theorem needs a reason that a hypothetical exceptional trajectory admits the required small-height reference arcs at windows longer than its starting bit length. The pair classification allows the grade to grow and does not prove the desired merger for a specified least counterexample. The full-plateau inequality still permits the short plateaus induced by surviving cycle widths. Work on these missing implications continues in later, separately reviewed checkpoints.
