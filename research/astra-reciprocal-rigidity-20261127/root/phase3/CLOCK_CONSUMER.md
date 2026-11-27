# A finite kernel consumer for the common clock-error measure

The [ordinary clock proof](../../rigidity/phase3/CLOCK_DISPERSION.md) constructs
a sequence of finite positive measures on the labels `(component, clock)`.
Every member is supported on labels of integers below one common cutoff.
After a one-step clock shift, every successive discrepancy is bounded
coordinatewise by the **same** positive measure. That shared envelope,
rather than just its total variation norm, is the essential hypothesis.

[ClockEnvelope.lean](ClockEnvelope.lean) checks the finite summation step.
Translate the finitely many relevant integer clocks so that index zero lies
below their common support. For component `c`, write `p c j k` for the mass
at clock `k` after transport step `j`, and `error c k` for the fixed positive
error envelope. Its hypotheses are

\[
 p(c,j,0)=0,\qquad
 p(c,j,k+1)\le p(c,j+1,k)+\operatorname{error}(c,k),
 \qquad \operatorname{error}(c,k)\ge0.
\]

Induction down the clock, while increasing the transport index, gives

\[
 p(c,j,k)\le\sum_{0\le i<k}\operatorname{error}(c,i).
\]

The theorem `component_atoms` permits a different clock to be selected in
every component before the rows are summed. The theorem `component_windows`
permits any set of at most `w` clocks in each component; no interval
assumption is needed. Both bounds use the total mass of the common envelope,
with factor `w` in the latter case. They require no positive density for a
particular component.

These finite theorems were rebuilt with the packet's pinned Lean and mathlib
versions and strict flags. The printed dependency inventories contain only
`propext`, `Classical.choice`, and `Quot.sound`. Their hypotheses do not
include the ordinary synchronization estimate, the simultaneous cycle-cut
bound, or the construction of the real-cutoff measures: those are written
arguments in the linked source. The root independently reconstructed the
prior quantitative synchronization argument in PR146's frozen
`THREE_RAY_UPPER.md`, including its jump walk, holding-time estimate,
contracting boundary returns, and finite absorbing words.

Consequently the ordinary conclusion remains graded as a written theorem
with this finite kernel consumer. It bounds a component's clock atom by
`O(X/sqrt(log X))` in the ambient interval `[1,X]`. It does not force a set
of only `X/log X` ordinary sources to occupy different clocks, nor does it
exclude an escaping component.
