# Directed residue closure, interior width budgets and ordinary color variation

**Collatz remains OPEN.** This checkpoint proves a complete, directed finite localization into \(11\bmod32\), hence \(17\bmod48\), and derives new constraints on actual ordinary head disagreements. The arithmetic localization has a full Lean proof. The original-source counting, probability and color-complexity theorems have written proofs and independent reviews, with their finite formal ingredients separated below.

We use the positive shortcut map \(T(2n)=n\), \(T(2n+1)=3n+2\). A binary label \(f\) is invariant when \(f(Tn)=f(n)\). An actual tripling defect is an ordinary positive \(x\) with \(f(x)\ne f(3x)\). Such a label can be the indicator of the basin \(C\) of 1. None of the estimates substitutes finite nonmerger for actual unequal labels.

## 1. A complete finite directed replacement

For either ordered pair \(a\ne b\), let \(D_{r,m}^{a,b}(X)\) count the defects through \(X\) with \(x\equiv r\pmod m\) and labels \((a,b)\). The new certificate proves

\[
D_{1,16}^{a,b}(X)\le1007D_{11,32}^{a,b}(H X),
\qquad H=\frac{574854143371}{219537}<2618500.
\]

Every output is given by an injective positive-slope affine map on one original source progression. The same finite menu therefore transfers unweighted reciprocal sums at constant cost. The exact ordinary identities

\[
(f(32t+11),f(96t+33))
=(f(48t+17),f(144t+51))
\]

give the corresponding conclusion at \(17\bmod48\). The earlier logarithmic moment loss is no longer needed for this localization.

The search found 116 cylinder motifs containing 88 distinct ordinary comparison paths. All added comparisons go **forward** from \(32s+11\) to its triple. The remaining ordinary edges may be traversed in either direction. The permitted continuation words have counts

\[
1,3,9,25,54,65,58,27,8,1,0
\]

from length zero through ten. There is consequently no uncovered length-ten word. An independent replay checks all \(3^{10}=59049\) complete original cylinders, their midpoint congruences and the 1,007 possible first-hit query positions. The kernel checks the path interpretation, all numeric rows, all midpoint inclusions, the finite word cover and the resulting unrestricted pointwise theorem `DirectedEleven.localize`.

[Complete proof and quantitative return](BOUNDED_DIRECTED_ELEVEN.md) · [Literal data](Directed11Motifs.json) · [Source accounting replay](check_directed11.py) · [Independent complete-cylinder replay](check_cylinders.py) · [Finite kernel certificate](DirectedEleven.lean) · [Ordinary localization](DirectedElevenLocal.lean).

### The global arithmetic consequence

Combining the new localization with the earlier directed descent gives

\[
\bigl(\forall n>0,\ n\in C\bigr)
\quad\Longleftrightarrow\quad
\bigl(\forall z\equiv17\pmod{48},\ 3z\in C\Rightarrow z\in C\bigr).
\]

The full ordinary statement is formalized in [Residue17Closure.lean](Residue17Closure.lean), using a [byte-exact copy of PR146's descent module](vendor/ReverseBasin.lean). The analogous forward implication at every such \(z\) is also sufficient, by the pinned written forward theorem of PR146. The new directed localization preserves both orientations; the complete global kernel consumer here proves the reverse equivalence displayed above. Neither basin implication is asserted without its hypothesis.

Under a counterexample, PR146's bounded two-sided reduction from all odd defects to \(1\bmod16\) now transfers the full \(0.84\) lower population exponent to \(17\bmod48\), without loss. This lower bound counts the union of the two orientations; it does not assert that each orientation attains that exponent. In particular, the contrary upper estimate \(D_{17,48}(X)=o(X^{0.84})\) would close that route. Its proof is still absent. Unweighted summability on this residue also suffices under the previously named fixed-target positive-density input M. The finite localization and the displayed Lean equivalence require no such analytic input. The newer PR195 unit-only certificate is credited as prior work; its bounded reduction already improved the earlier unit moment criterion.

## 2. Actual smaller witnesses on the original source octave

For every actual tripling defect in the original octave \([X,2X)\) outside the stated exceptional set, an ordinary witness with the following height is available in each target residue. For the basin indicator, that witness has labels \((0,1)\): its source is outside the basin and its triple is inside. For a general binary invariant, its labels are \((1-f(1),f(1))\).

| Original exceptional count | Height of the ordinary directed witness | Meaning |
|---|---|---|
| \(O(X^{49/50})\) | \(O(X^{24/25})\) | A visible strict power contraction. |
| \(O(X^{19/20})\) | \(O(X^{(94/149)\log_2 3})\) | A smaller exception; the height exponent is still strictly below one. |
| \(O_q(X^{h_2(\log_3 2)}/\sqrt{\log X})\) | At most \(qX\), for any fixed \(0<q<1\) | Arbitrary prescribed fixed contraction at the native entropy threshold. |

The proof counts parity words of both original rays \(x\) and \(3x\) at the same fixed clock, then applies the finite directed descent and localization. It never restarts a random law at an endpoint. The parity calculation builds on the resident native no-descent method. [Fixed-factor refinement and proof](STRICT_RETURN_REFINEMENT.md).

The remaining return problem is exact: different original sources may share a witness, and a smaller witness may lie in the next exceptional set. The exponent \(h_2(\log_3 2)\simeq0.949956\) still exceeds \(0.84\). These counts do not establish universal or indefinitely repeatable descent.

## 3. Interior comparisons must repeatedly lose width

Put \(R=81^j\), \(d=\log_2R\). On the one original coarse binary grid, the signed difference of two native grades is a fair process until its first tie. Killing it at that tie preserves its expected width. Strictly interior head intervals occupy one residue class of grades modulo four and leave a definite amount of width unused. This gives a conditional contraction \(1-c/\sqrt V\) per generation at lag \(O(V)\).

The argument accounts for the bounded future lookahead needed to certify a genuine regeneration. On genuinely discordant sources under the pinned ordinary regeneration and projection input R, outside \(O_A(Rd^{-A})\) original children, a suitable actual schedule forces **every** choice of true four-trit heads to have at least \(c\,d/(\log d)^{10}\) adjacent transitions with a grade tie, failure of the endpoint margins, or a reversal of the intervening cut order during certification. A separate version groups consecutive cuts into fixed wider blocks and removes the local reversal alternative. The two statements have distinct witness scopes.

The delayed-tie estimate also handles native pairs that tie and reopen: for fixed \(B>3\), all but an arbitrarily small fixed fraction of late clocks have no native tie at ages between \((\log d)^B\) and \(d/(2\log d)\), outside superpolynomially small original mass. This does not remove early ties or prove that the forced failures above have small total mass.

[Width budget, stopping rule and original four-trit version](INTERIOR_GRADE_BUDGET.md) · [Delayed native ties](DELAYED_NATIVE_TIES.md) · [Seven finite Lean identities](InteriorGradeBudget.lean).

## 4. Persistent selected populations force ordinary color oscillation

Suppose a chosen set of good discordant originals has normalized weight \(w\ge d^{-P}\), for a fixed \(P\). The set may prescribe either original orientation. Keeping one coarse coordinate and its actual source multiplicity, a predictable modal-reply test forces a chronological binary tree of genuine ordinary color answers. The tree has depth

\[
\gg \frac{(d\log d)^{1/4}}{\sqrt{\log\log d}}.
\]

A finite shattering argument selects a common list of queries in different time blocks. All answer patterns occur among actual sources in the same opening cell, with at least \(\exp(c\sqrt{d\log d})\) distinct coarse integers for each pattern. The features have partial domains: each represented source actually reaches every specified query. No reply is invented at an unvisited feature.

The query arguments are monotone in this common ordinary parameter. If \(V_i\) counts actual changes across consecutive sites of the fixed ternary progression in window \(i\), every \(r\)-subset obeys

\[
\sum_{i\in E}V_i\ge2^r-1.
\]

One can choose a common ternary depth \(u\) and a number of windows \(k\), both \(\gg(d\log d)^{1/8}/(\log\log d)^{1/4}\). At least half of these disjoint windows each contain \(\gg2^{k/2}/k\) genuine color changes at the same fixed gap \(3^u\), and at least as many ordinary adjacent color changes. Their lengths are at most \(2^{C\sqrt{d\log d}}\). The intermediate transition sites need not themselves be query outputs.

The polynomial lower bound on \(w\) is a hypothesis. The \(0.84\) population theorem alone does not supply it. Under the source-qualified input M, a counterexample would make the full normalized head-disagreement series diverge. Since \(d\) is proportional to the row index, some rows then have mass at least \(d^{-2}\); a finite pigeonhole retains one suffix and orientation on a subsequence, and the good-envelope discard preserves inverse-polynomial mass. This supplies a conditional trigger for the theorem. A contrary upper estimate in these same selected intervals remains open; macroscopic density and existing single-query bounds do not provide one.

[Selected populations and chronological tree](SELECTED_TRIT_CELLS.md) · [Common fixed questions](FIXED_TRIT_PATTERNS.md) · [Actual variation count](SELECTED_COLOR_VARIATION.md) · [Finite source arithmetic](LocalColorCells.lean) · [Finite inventory identity](FixedTritFeatures.lean).

## Proof and evidence boundaries

The new arithmetic theorem and its complete reverse-basin consumer are separate from the written analytic statements. The head geometry and selected-color statements retain the source-qualified native merger input P and ordinary regeneration/projection input R. The strict-return parity count and finite source localization require neither P nor R. The Lean modules for the analytic arguments check finite identities, not their full probability estimates. M appears only in the imported summability consumer and the explicitly conditional polynomial-population trigger. The published \(0.84\) predecessor exponent, the optional two-logarithm separation and the shattering literature are attributed in [the source discussion](LITERATURE_AND_BOUNDARIES.md) and [exact source ledger](SOURCES.json).

[Reviews, fresh execution and preserved evidence](../../../reports/ayh-resource-reset-20261124/directed-return/README.md) distinguish executed kernel checks, exact arithmetic replay, written reconstruction and open conclusions. No prior research manuscript has been silently upgraded to a complete Collatz proof.
