# Fixed ordinary targets, internal mergers, and full-denominator screening

24 November 2026. **PROPOSED research packet with independent scoped reviews and executed finite verification. Collatz remains OPEN.**

This packet attacks the pointwise gaps in unintegrated PRs 192–203. Its strongest positive result applies to **every supplied positive odd target prime to three**, rather than almost every target under an auxiliary measure. The new lower bound is still too small, and has the wrong unresolved clock information, to close the conjecture. The other two lanes identify exactly where successful finite constructions lose a supplied ordinary source.

Throughout, use the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

An odd unit means a positive odd integer not divisible by three. A physical clock counts shortcut steps; a grade counts odd inputs. These are distinct quantities.

## 1. A larger population at one exact clock for each ordinary target

Fix an odd unit \(q\). For every sufficiently large \(X\), one pair of integers \((e,p)\) supports at least

\[
c_q\,\frac{X^{1/5}}{\log X}
\]

distinct odd unit sources \(x\) in \([X/2^{400},X]\) satisfying

\[
T^e(x)=q,\qquad T^e(5x)=5q,
\]

with **the same** number \(p\) of odd inputs on both arms. Their affine offset satisfies \(0\le\beta\le1/2\), where

\[
q=\frac{3^p}{2^e}x+\beta.
\]

The aggregate population over the rows is \(\gg_q X^{1/5}\). The exponent improves PR200's finite paired-tree exponent \(1/9\). This comparison is about paired ancestors; it is not a comparison with the much larger known lower exponents for unrestricted one-arm ancestors. The displayed interval is a very wide fixed multiplicative shell, not a short-interval assertion. Constants and the onset may depend on \(q\).

The proof uses a finite dictionary of 2,276 first-return records and a positive weight depending on a child's residue modulo 81. Exact integer arithmetic verifies its inequality on all 354,294 relevant unit classes modulo \(3^{12}\). A strictly growing ordinary inverse tree converts that inequality to a count at every large scale. One fixed terminal branch makes every final offset at most one half. There are only \(O_q(\log X)\) possible clock/grade rows in the scale window, yielding the individual row.

This theorem uses no external analytic floor or stochastic law for a selected ordinary orbit. Its universal finite inequality is verified by the included Python certificate; that enumeration itself is not a Lean kernel check.

[Complete statement and proof](pressure/WEIGHTED_POINTWISE_ROWS.md) · [Exact checker](pressure/check_weighted_pressure.py) · [Independent review](../../reports/astra-joint-closure-20261124/ordinary/REVIEW_PRESSURE.md)

### A constraint on stronger lower bounds

At offset at most one half, a path to an odd unit \(q>1\) cannot contain a completed lap at \(q\). For paired paths this first-hit property holds also at \(q=1\), since the other endpoint 5 cannot return to itself. Different rows at one fixed target therefore contain disjoint sources. If \(N_{e,p}(q)\) denotes their count and \(G=2^e/3^p\), then

\[
\sum_{H\le G<2H}\frac{N_{e,p}(q)}{G}
\le q+\frac12+\frac1H.
\]

This permits a central bank of order \(\sqrt{\log H}\) rows with pressure of order \(1/\sqrt{\log H}\); a uniformly larger lower bound on every such row is impossible. It neither proves nor refutes PR200's requested subexponential pressure along selected balanced rows.

[First-hit and packing proof](pressure/FIRST_HIT_PACKING.md)

## 2. Every position in long initial odd runs: successes and actual missed sources

For an odd multiple of three \(n\), let \(m=v_2(n+1)\). Its first \(m\) steps are odd. The new construction gives, for every prescribed \(m\) and compatible ternary cylinder, an infinite arithmetic progression of actual sources for which **every position** \(1\le i\le m\) has a smaller representative \(0<u<n/3\) reaching the same endpoint. All these certificates can hold for one and the same \(n\). The competing path takes a block of odd steps followed by halvings; an exact CRT construction provides the progression.

The same mechanism has an unavoidable limit. Every smaller competitor of this form at position \(i\) requires

\[
2^i3^{v_3(n)}<n^{\log_2(3/2)}.
\]

An explicit infinite family for every \(m\) violates this inequality at **all** internal positions, even when the competing clocks are unrestricted. Thus density of successful subprogressions does not imply success for a supplied ordinary integer. More general competing paths pay a proved linear even-step cost obtained by tracking a finite negative shadow; they are not excluded by the one-block obstruction.

For example, 293,654,367 reaches 660,722,327 after two odd steps. The smaller 96,567,295 reaches the same endpoint after fifteen odd steps and six halvings, and is below one third of the original source. This is an ordinary merger, not a congruence-only witness.

[Proof and exact quantifiers](ordinary/README.md) · [Lean core](ordinary/InternalMerge.lean) · [Finite controls](ordinary/check_internal_merge.py) · [Independent review](../../reports/astra-joint-closure-20261124/arithmetic/REVIEW_ORDINARY.md)

## 3. Finite local cycle tests retain the critical entropy exponent

Fix a parity prefix, finitely many congruence conditions, a positive lower bound on every cycle phase, and a near-critical coefficient window. There are still exponentially many primitive positive **rational** cycles satisfying all those conditions. One can force chosen factors to appear and cancel in the numerator and denominator, while different prescribed factors survive in the reduced denominator at every phase.

Their exponential count retains the full near-critical binary-word rate

\[
\exp\bigl(nH(\alpha)+o(n)\bigr),\qquad
\alpha=\frac{\log2}{\log3},\quad
H(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha).
\]

The proof combines the classical rational word formula, the finite affine branch group, valuation-aware CRT, bounded neutral padding and a primitive-word count. It includes its elementary derivations and credits the earlier rational-cycle and modular-group literature; no global priority claim is made. These are deliberately nonordinary cycles. The theorem explains why testing fixed factors, even together with high minima and primitive periods, cannot replace a proof about the **whole** denominator of a supplied word.

The exact 184-step rational control has every phase between its minimum and higher positive values, with minimum strictly between 48 and 49. Its specified phase is congruent to 157 modulo 180. A factor 5 cancels, while 7 remains in its reduced denominator. It is not a counterexample to the integer conjecture.

[Full theorem and proof](arithmetic/README.md) · [Lean arithmetic core](arithmetic/FiniteCycleTests.lean) · [Exact rational orbit](arithmetic/check_cycle.py) · [Independent review](../../reports/astra-joint-closure-20261124/pressure/REVIEW_ARITHMETIC.md)

## 4. Formal and executable evidence

Six successful Lean 4.34.1 compiler executions cover **25 distinct theorem declarations**: seven in the new ordinary core, four in the new finite cycle core, eight from PR202, and six from PR203. The last fourteen retain the frozen proof bodies and replace the umbrella import with available narrow imports. The original PR202 pass emits one unused-binder warning; the working copy only renames that unused binder. All four delivered working modules pass with warnings treated as errors. Printed transitive dependencies use only `propext`, `Classical.choice`, and `Quot.sound`, or no axioms.

This verifies the stated finite kernels. The infinite counting, CRT family, compact padding, entropy and analytic arguments retain their written scope. No Lean theorem asserts universal Collatz convergence, and the external analytic assumptions of PR202/203 have not been proved by compiling their elementary transport lemmas.

[Reproduction instructions and scope](../../reports/astra-joint-closure-20261124/README.md) · [Lean receipt](../../reports/astra-joint-closure-20261124/LEAN_RECEIPT.json) · [Coordinator reconstruction](../../reports/astra-joint-closure-20261124/ROOT_REVIEW.md) · [Frozen source intake](../../reports/astra-joint-closure-20261124/SOURCE_INTAKE.json)

## The first unsupported global step

The positive count applies at every fixed ordinary target, but its selected rows need not have \(p/e\to1/2\), and its exponent remains \(1/5\). Even a much stronger paired lower count would require an incompatible upper bound or a separate component-merging argument. The descent constructions do not cover the displayed high-valuation sources, and the rational-cycle theorem does not provide a prime obstruction for every integer-cycle candidate. None of those missing inferences is assumed here.

The next pointwise task is to control complete paired words at a prescribed ordinary target on the required balanced clocks, or obtain an actual terminating merger for the surviving inputs. Repeating a typical-target theorem or changing the supplied source inside a successful cylinder does not establish either task.
