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

## Second mathematical checkpoint

The next results test the sharpness of the first claims and strengthen the restrictions on actual ordinary pairs and primitive cycles. The asymptotic statements remain proposed written theorems.

| Claim | Statement | Evidence and boundary |
|---|---|---|
| O3: simple paths attain the open bound | For every fixed K, the denominator coefficient K−1 in O2 is optimal even on positive rational paths with no repeated state and a fixed dictionary of powered words. | [Construction and simplicity proof](literature/SHARP_SIMPLE_ARCS.md). The arbitrary-K motif input is the pinned, proved `BlockClock.cover` theorem; an explicit fourteen-start example supplies K≤13 without that general input. |
| O4: every late window has linear description cost | On any one fixed nonperiodic positive integer orbit, every sufficiently late window of length ceil(λt), λ>log₂(3/2), requires linear template cost when the number of powered pieces is fixed. | [Uniform-window corollary](literature/FIXED_SOURCE_WINDOWS.md). This excludes a restricted form of compression; it supplies no universal compression theorem. A simple two-run integer family also rules out a constant additive error in O1. |
| P3: exact bounded-grade spectrum | For a=b=1 and G≥5, let p=floor((G−5)/2). The number of joint sources in [X,2X) is (log₂ X)^(p+1)/(18·3^p·(p+1)!)+O_G((log X)^p). Comparable fixed targets have an exact threshold and orientation factor; incomparable targets give an eventually constant octave count. | [Written count](ordinary/FIXED_GRADE_SPECTRUM.md). G is fixed before X tends to infinity. Physical first-hit comparisons and inverse-calendar residue counts are checked separately. |
| P4: subquadratic unmatched clocks | Uniformly as G→∞, an unmatched odd pair s,3^r s has k=o(G(G+r)). For fixed r and fixed incomparable targets, every unbounded joint-source family has G/sqrt(log₂ s)→∞. | [Sparse-discrepancy proof](ordinary/SPARSE_DISCREPANCY_BLOCKS.md). A two-endpoint S-unit circuit lemma charges each endpoint once. It uses the classical Subspace Theorem and has no effective modulus. The formal elementary quadratic bound remains the explicit certificate. |
| C2: every almost-repeating rotation has sparse low states | At a lag of order M, for 2≤J≤M, the low-state count obeys D_Y≤p/J+(J²−1)s·max(0,floor(log₂(qY)))/6. There are stronger complete-column and geometric-mean bounds. | [Exact rotation occupation](cycles/ROTATION_OCCUPATION.md). The full numerator divisor includes the shared past and future at each date. Its arithmetic kernel is checked in Lean. No maximum-height restriction is imposed. |
| C3: a large balanced-minimum ratio forces all rotations apart | For rational cycles with growing minima and m/m_bal≥1/2+ε, every proper lag satisfies s(log₂ q+log₂ p)≫_ε p. For ordinary cycles, the pinned PR213 sparse-window estimate lowers the threshold to 0.481775+ε. | [Low-envelope proof](cycles/BALANCED_MINIMUM_ROTATIONS.md). The first threshold uses only the stated classical logarithm estimate. The sharpened ordinary threshold has a separate written dependency. Small balanced-minimum ratios remain open. |

The complete formal inventory now has thirty locally authored public roots: thirteen in `AffineOrbit`, five in `PairedClock`, six in `ReferenceDivisibility`, and six in `RotationOccupation`. Each was freshly compiled and imported into a public-root axiom audit using only the standard Lean axioms. The second replay completes the previously interrupted PairedClock check. It does not formalize the Subspace Theorem, the infinite counting asymptotics, or the limiting cycle arguments. The [second coordinating review](../../reports/astra-critical-rigidity-20261128/checkpoint2/REVIEW.md) records the exact distinction and the external motif input.

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

At initial publication, the completed central Lean receipt covered all thirteen public roots of `AffineOrbit.lean`; the PairedClock replay was pending and was then killed under observed shared-memory pressure. Its five-root fresh replay succeeded at the second checkpoint. The original failed receipt and the successful later receipt are both preserved.

## Remaining decisive questions

The new source theorem needs a reason that a hypothetical exceptional trajectory admits the required small-height reference arcs at windows longer than its starting bit length. The pair classification allows the grade to grow and does not prove the desired merger for a specified least counterexample. The full-plateau inequality still permits the short plateaus induced by surviving cycle widths. Work on these missing implications continues in later, separately reviewed checkpoints.
