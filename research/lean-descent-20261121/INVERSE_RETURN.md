# A contracting inverse comparison, and its exact use in a half-crossing proof

This is an unconditional finite-word result. It does not provide the universal
half-crossing budget or establish Collatz. The companion Lean file imports the
dependency-free basin definitions from PR 174 at
`7034109ed60a26bc49824e1ed43c239ceca81194`; its new declarations use core Lean only.

Write `T(n)=n/2` for even `n`, `(3n+1)/2` for odd `n`, and let `C` be its basin of 1.
For every integer `t>=0` put

\[
 x=131072t+127657,\qquad q=177147t+172534.
\]

Then `x<q`, and the following identities hold on the entire progression:

\[
 T^{17}(x)=q,\qquad T^{17}(5x)=5q.
\]

The source parity word is `10111111111000010`; the companion word is
`10010011111011101`. Both have eleven odd steps. Their affine formulas are

\[
 T^{17}(x)=\frac{177147x+321869}{131072},\qquad
 T^{17}(5x)=\frac{177147(5x)+1609345}{131072}.
\]

Every step is integral on the displayed class. `InverseReturn.lean` proves the
seventeen ordinary steps on each arm, the two basin equivalences, and the
exclusion of this class from being a globally least failed comparison
`q in C, 5q not in C`. The forward multiplier is `177147/131072>1`; reading
the identity backwards reduces the parameter by an asymptotic factor
`131072/177147`. This direction differs from the forward contracting return
languages in the earlier renewal packets.

## Transfer of the proposed half-crossing budget

For a source `n`, let `p_j(n)` count odd steps before clock `j`, and set
`a_j(n)=3^{p_j(n)}/2^j`. Define the proposed budget by

\[
 \operatorname{HalfBudget}(n):\quad
 \exists j,\quad a_j(n)<\tfrac12\quad\text{and}\quad2p_j(n)\le3n.
\]

The source word above has `a_j(x)>=3/4` at every clock `0<=j<=17`.
Consequently every witness to `HalfBudget(x)` has `j>17`. Remove the first
seventeen steps from such a witness. The suffix from `q` has coefficient

\[
 \frac{a_j(x)}{a_{17}(x)}
 <\frac{1}{2(177147/131072)}<\frac12
\]

and uses `p_j(x)-11` odd steps. Since `x<q`,

\[
 2(p_j(x)-11)\le3x-22<3q.
\]

Thus `HalfBudget(x)` implies `HalfBudget(q)`. This is a written proof of the
coefficient transfer; the companion file formalizes the underlying ordinary
paths and basin implication, not yet the half-budget statement. It can be
used by a strong induction for the budget on this entire ternary class.

## Why an inverse-only completion is insufficient

There are unconditionally arbitrarily large convergent inputs with **no smaller
ordinary ancestor**, even when the ancestor is allowed an arbitrary clock.
Here is the short proof, so a compiler can avoid an impossible global design.

Let `tau(n)` be the first hit of 1, defined for `n in C`, and fix `N>=2`.
Take `H` to be the maximum of the finite collection `tau(n)` for convergent
`n<=N`. That collection is nonempty. The numbers `2^r` converge with
`tau(2^r)=r`, so there is a convergent input with first-hit time greater than
`H`. Choose the least such input `q`. Then `q>N`. If some `x<q` reached `q`
at a positive clock `j`, it would converge. It could not have hit 1 earlier:
the forward orbit of 1 contains only 1 and 2, while `q>N>=2`. Therefore
`tau(x)=j+tau(q)>H`, contradicting the choice of `q`.

In particular, no finite collection of base inputs plus moves exclusively to
smaller ordinary predecessors can cover all convergent sources. Allowing
unequal clocks or paired predecessor searches does not remove this obstruction.
A full proof through this approach must mix in other moves with a justified
terminating order. The half-crossing budget route remains a separate global
target; the displayed inverse rule supplies one valid induction step.
