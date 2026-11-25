# Actual inverse costs, supplied-hit descent, and the joint-grid boundary

**Status: OPEN. This pass does not prove the Collatz conjecture.** It directly tests three proposed ways of closing the ordinary counterexample reduction. It obtains a stronger necessary condition on an actual bounded bad cycle, a physical descent-or-carry theorem at an actual supplied upper hit, and a lower bound that defeats a bounded-seed enlargement of the proposed joint-grid upper estimate. The positive ordinary row restriction remains essential in the last result.

Use the positive shortcut map
\[
T(2v)=v,\qquad T(2v+1)=3v+2.
\]
Write \(T^h x\) for its iterate, \(Q_h(x)\) for the number of odd departures in that prefix, and `Good x` for reaching 1. All formal statements use the existing definitions in `SourceDeletion` and `MinimumFailure`.

## 1. Every inverse window of an actual bounded bad cycle

Let \(q\) be the least positive odd tripling disagreement. In PR205's bounded alternative, \(s=(3q-1)/2\) is the minimum of the bad cycle, and its odd phases lie below \(8q\). The known basin floors apply to **every positive ancestor**, not just to phases of the cycle. For a native window with \(k\) odd departures and \(A\) shortcut clocks, consider any positive odd predecessor of the same endpoint with the same \(k\), using \(B\) clocks and arbitrary positive valuations.

The new results are
\[
 A\le B+2;\qquad 3\mid z\Longrightarrow A\le B+1;
 \qquad x=s\Longrightarrow A\le B.
\]
At the minimum, after the initial singleton merger, the two exact inverse optima are
\[
 \left(\min B,\ \min_{3\mid z}B\right)=(A,A+1).
\]
Thus the native word is an actual minimum-cost path, and its partner from \(3q=2s+1\) attains the best possible cost from a multiple of three. This is an ordinary-basin condition that the rational order controls from the previous pass do not impose.

The numerical distortion premise is available for every possible primitive period in this bounded alternative. Five preceding valuations give at most 32 odd residue classes modulo 486. Counting the distinct phases in the height strip gives \(p\le s/3\) for \(s\ge729\), hence the full-lap distortion is at most \(9/8\). All smaller possible minima are covered by the explicit finite iteration check. The counting argument is written; the ordinary path comparison and basin implications are Lean-checked.

A concrete application excludes the reverse valuation window

`12212122221212121211`.

Its first 19 reverse steps have a rival with two fewer shortcut clocks and source \(z=(x+1)/4\). The final native symbol makes that rival a multiple of three below \(3q\), contradicting leastness. This exclusion holds throughout the actual strip, although the ideal height range of the word fits inside it.

**What remains:** prove that every nontrivial eligible cycle word violates an inverse test or full-denominator integrality somewhere. One excluded word does not establish this. The supplied ordinary progression passes all of its 1,260 tested subwindows through depth 24 and all 22 tested paired optima. It is a finite trajectory control, not a cycle.

[Cycle proof and scope](cycle/README.md) · [Nine Lean declarations](cycle/InverseClocks.lean) · [Independent mathematical review](../../reports/astra-diagonal-closure-20261125/cycle/TRANSPORT_REVIEW.md)

## 2. A physical drop or a saved suffix at the supplied hit

Suppose the actual upper arm has a supplied certificate
\[
                  T^H(3^j x)=1.
\]
For positive integers \(M,D\), if
\[
 Q_H(x)\le M,\quad
 Q_H(x)\le j+Q_H(3^j x)+D,\quad
 3\cdot3^D<2M,
\]
then some **actual value of the lower trajectory by clock \(H\)** lies strictly between zero and \(M\). There is no replacement certificate or renewed time budget in this conclusion.

If the supplied upper odd work satisfies \(j+Q_H(3^j x)+D\le M\), the alternative to this drop forces a first equal-grade clock strictly before \(H\). At that clock the lower endpoint is strictly larger than the upper endpoint, the remaining upper suffix still reaches 1, and its odd work is strictly less than that of the supplied certificate. The first equal-grade clock cannot itself be a merger: a synchronous equal-grade merger requires a previous strict odd-count overshoot.

An additional arithmetic theorem converts a suitable positive carry into a new ternary pair when the carry has its own hit and the upper endpoint has the necessary binary factor and odd cofactor. Those conditions remain explicit.

The canonical family also gives a decisive limitation on the simplest return mechanism. For the specified ordinary inputs with
\[
                 81x+271=2^H,
\]
the triple's first hit has three odd departures, yet **every lower state through that whole hit** fails to share its next successor with any positive multiple of three. The exact local criterion is that a ternary unit \(n\) has such a shared successor precisely when \(n\equiv10\pmod {18}\). The family and the no-successor statement are proved for all allowed parameters in Lean, not inferred from the four displayed examples.

**What remains:** force the saved positive carry back to an admissible smaller bad source with the retained certificate, and handle upper certificates outside the stated odd-cost bound. The canonical controls are convergent ordinary inputs; they do not refute a theorem that additionally uses genuine badness.

[Transport proof and scope](transport/README.md) · [Eight supplied-hit/carry declarations](transport/FirstCrossing.lean) · [Three canonical declarations](transport/CanonicalDeadline.lean) · [Independent mathematical review](../../reports/astra-diagonal-closure-20261125/transport/JOINT_REVIEW.md)

## 3. The enlarged many-clock estimate fails

The proposed PR197 closing route seeks a sufficiently small joint event on one binary source string, with the same physical seed pair throughout the slab. The new lower bound retains those shared choices and the actual four-trit query formulas.

For each suffix \(0\le u<81\), a checked binary cylinder gives
\[
 T^{14}x=T^{14}(81x+u),\qquad
 Q_{14}(x)=Q_{14}(81x+u)+4.
\]
The identity holds on all positive lifts and all later common clocks. Each adjacent pair of four-trit columns therefore has a fixed positive fraction of matching weighted labels. A finite gluing theorem shows that frequent endpoint mismatch forces a column of large deficiency.

For \(\lambda=\log_3(b/a)>0\), a single admissible large-gap seed pair in the bounded-parameter enlargement gives
\[
             P_d(\lfloor d/3\rfloor)\ge\lambda/4
\]
for all sufficiently large rows, when the required clock fraction is at most \(\lambda/8\). No independence between clocks or between the two arms is used. A diffusive-gap version applies to opening-cell dependent seed choices.

The enlargement still has a lower bound \(\gg d^{-1}\) after retaining a genuine native-survival test. A separately reviewed extension goes further: the seed pair and every completing grid residue can be witnessed by the two actual arms from one positive ordinary parent. **Those parents have unrestricted height and can exceed the required original row.** A different grid completion can use a different positive parent. Neither genuine replies of one invariant coloring nor the original row population is constructed.

**What remains:** an estimate that retains the required row-height realization and/or actual reply feasibility, with the necessary selected-population lower bound still proved for that smaller event. The lower bound refutes the stated bounded-menu upper route; it does not refute the original physical-parent statistic or Collatz.

[Joint proof](joint/README.md) · [Unrestricted-height realization](joint/FEASIBLE_OPENINGS.md) · [Two Lean ingredients](joint/TritChain.lean) · [Independent mathematical review](../../reports/astra-diagonal-closure-20261125/joint/CYCLE_REVIEW.md)

## Evidence and closing proposal

The packet contains four new Lean modules with 22 public theorem audits. Two exact project dependencies contribute 23 additional audited declarations. The all-time analytic grid statements and the written cycle counting assembly are not claimed as Lean theorems. Exact finite controls, independent ordinary-orbit checks, and a complete-checkout replay are recorded separately.

[Final proof proposal and remaining obligations](FINAL_PROPOSAL.md) · [Root review and frozen-source intake](../../reports/astra-diagonal-closure-20261125/ROOT_REVIEW.md) · [Replay driver](../../reports/astra-diagonal-closure-20261125/replay.py) · [Verification receipt](../../reports/astra-diagonal-closure-20261125/VERIFICATION.md)
