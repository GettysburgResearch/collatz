# Least smooth towers and the remaining ordinary merger

**PROPOSED, with Lean-checked partial results. Collatz remains OPEN.** This pass attacks the universal step after the minimum-source excursion result. It changes the quantity minimized: a comparison may rise arbitrarily far in absolute height and still decrease the positive base left after removing powers of two and three. Five new Lean modules contain 34 audited public theorems. Their scope includes two infinite descent constructions and exact tests of proposed closing arguments. It does not include a proof of universal convergence.

Use the ordinary shortcut map
\[
T(2u)=u,\qquad T(2u+1)=3u+2,
\]
and write \(C(x)\) for an actual finite iterate reaching 1. All ordinary claims below use this predicate, rather than an arbitrary invariant coloring.

## The positive rank reduction

If a counterexample exists, choose the least positive base \(w\) supporting any bad \(3^r w\), then the least bad exponent \(r\) at that base. Lean proves that \(w\) is odd and prime to three, \(C(w)\), and \(r>0\). It also proves
\[
 C(2^i3^j b)\quad(0<b<w;\ i,j\ge0),\qquad
 C(3^j w)\quad(j<r).
\]
There is no upper bound on the numbers covered by the first assertion. This is the feature that permits a proof to pass through a large excursion. The case \(w=1\) is retained.

Write the first maximal odd run as
\[
 n=3^r w=2^M a-1,\quad a\text{ odd},\quad M\ge1,\qquad A=3^M a.
\]
The preceding good power proves \(C(a)\) for every relative size of \(M\) and \(r\). If \(2^M>3^r\), the actual bad-tower hypotheses force \(a<w\). Four physical mergers then exclude \(A\equiv3,5,7,9,13,15\pmod{16}\), leaving only 1 or 11 modulo 16 in this regime. Independently, \(r\ge2\) excludes \(n\equiv85\pmod{512}\) by a nine-clock meeting with \(n/9\).

For example, \(111=3\cdot37\) reaches 566 after four odd shortcuts. The paths
\[
566\to283\to425\to638,\qquad
1701\to2552\to1276\to638
\]
meet, and \(1701=7\cdot3^5\) has base \(7<37\). The general family \(n=7\cdot2^{6t+4}-1\) gives comparison inputs arbitrarily large relative to \(n\). These are actual finite path identities, not asserted counterexamples. [Full proof and Lean module](global/README.md).

## Progress inside the short-run case

For **every fixed exponent \(r\ge2\)**, the second construction gives an infinite progression in the short-run case \(2^M\le3^r\). Every constructed source has \(M=1\), a singleton exit, and residue \(113\pmod{512}\), so the preceding exclusions do not cover it.

The physical identity is general. If \(T^h(3^r v)=1\), then for every positive \(t\),
\[
 w=v+4\cdot2^h t,\qquad w'=v+3\cdot2^h t<w,
 \qquad T^{h+2}(3^r w)=T^h(3^r w').
\]
An explicit prime-power congruence supplies reference inputs at each \(r\), including arbitrarily large \(r\). Lean checks the merger and its contradiction with a first bad tower. The construction of the reference inputs for all \(r\) is a written proof, independently reviewed; it is not represented as a fully formalized discrete-log existence theorem. [Construction, scope and replay](descent/CORE_PREFIX.md).

## The exact closing obligation

The Lean proposition `Collatz.SmoothCore.FrontierMerger` asks for a finite ordinary meeting for every source surviving the proved arithmetic exclusions. The destination must be \(3^j b\), where either \(0<b<w\), or \(b=w\) and \(j<r\). Both clocks may be arbitrarily large. This is an assertion about specified positive integers and their actual forward paths; it has no basin-label hypothesis.

Lean proves
\[
 (\forall n>0,\ C(n))\quad\Longleftrightarrow\quad\texttt{FrontierMerger}.
\]
**`FrontierMerger` is unproved.** The two constructions above supply genuine merger certificates on their stated domains. They do not cover every surviving source. In particular, a lower reference prefix need not reach 1 within the number of agreeing binary digits. The remaining task is to construct the required meeting on every surviving ordinary input, or replace this reduction with a complete argument. The equivalence is a formal proposal for that task, not a proof of its premise. [Exact definition and consumer](global/SmoothCore.lean).

## Direct tests of proposed ways to close the gap

| Proposed step | Checked result | Scope retained |
|---|---|---|
| Rank a returned disagreement by the good arm's hitting time or odd count | An ordinary crossing family has a returned source requiring unboundedly more clocks; its finite continuation can be prescribed arbitrarily | Refutes unconditional comparisons inferred from this path shape. It does not refute a theorem making essential use of a hypothetical bad label. [Proof](descent/README.md) |
| Join every high exit to the one smaller smooth tower by an affine identity | An exact invariant bounds all candidate powers and excludes every affine meeting on four convergent controls | Pointwise meetings, other smaller bases and arguments using badness remain open. [Proof](descent/SMOOTH_RAY.md) |
| Exclude every ordered cycle numerator by coprimality | A 41-odd-step rational cycle has numerator/denominator gcd 19, with reduced denominator still greater than one | It is not an ordinary integer cycle. Full divisibility remains the relevant condition. [Proof](cycle/README.md) |
| Repeated inverse shadows must eventually reach a smaller bad multiple | A fixed rational lattice has the least-source cutoffs at every path depth and still no such path | The model uses denominator 13 and a good set containing several basins. It cannot settle the ordinary basin of 1. [Lean proof](cycle/RationalBasin.lean) |

## Evidence and dependencies

The new Lean files are `SmoothCore`, `CorePrefix`, `CrossingRank`, `DecorationControl`, and `RationalBasin`, with respectively 14, 2, 3, 4 and 11 audited public theorems. The imported minimum-source modules are unchanged. There are no project axioms, `sorry`, `admit`, or `native_decide` in the new modules. Written infinite arguments and finite controls retain the distinctions stated above.

[Frozen source map](SOURCES.md) records the latest research inspected and the dependencies actually used. [Root review](../../reports/astra-universal-closure-20261124/ROOT_REVIEW.md) and the two independent mathematical reviews record exact scope. [Replay instructions and receipt](../../reports/astra-universal-closure-20261124/VERIFICATION.md) cover the complete published science checkout.
