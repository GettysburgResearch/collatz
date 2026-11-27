# Tenth checkpoint: joint denominators and complete source laws

**PROPOSED research. Collatz remains open.** This is the final mathematical
checkpoint of the six-hour sprint. The [complete report](SIX_HOUR_REPORT.md)
connects it to the earlier work and states the pointwise obligations.
The map is the shortcut map `T(2x)=x`, `T(2x+1)=3x+2`; a physical step
means one application of this map. All new results in this checkpoint are
written arguments. No new Lean module or finite checker is introduced.

## 1. Count all small denominators together

Let \(p=\log_3 2\), \(h_*=H_2(p)\), and \(L(n)=1+\log n\). For each
least physical period \(n\), let \(d_{\min}(n)\) be the minimum full
reduced denominator among all nonzero signed rational cycles of that
least period. The minimum is infinity if there are no such cycles.

[FAREY_CENSUS.md](cycles/phase8/FAREY_CENSUS.md) proves that
\[
 d_{\min}(n)>n^{\theta_F}L(n)^\lambda
\]
holds at a natural-density-one set of period values, for every fixed
\[
 \theta_F=\frac1{2h_*}=0.5263404293\ldots,\qquad
 \lambda<\lambda_F=\frac{3/2-h_*}{2h_*}=0.2895106439\ldots.
\]
In particular \(\lambda=11/38\) is permitted. Both signs and every
word shape are included. The conclusion concerns the complete reduced
denominator, with the actual numerator cancellation retained.

Two reduced rational phases of the same sign, with denominators at most \(D\), magnitudes
in an interval of width \(X\), and the same \(t\) parity bits satisfy
\(2^t\mid ae-bd\). Once \(2^t>D^2X\), distinct phases cannot share
that word. This counts the entire denominator range in one step.

The [endpoint census](cycles/phase8/ENDPOINT_CENSUS.md) supplies a
uniform ballot bound: words with every prefix odd count at least
\(\alpha j-a\), for \(3/5\le\alpha\le2/3\) and \(0\le a\le1\),
number at most \(C2^{H_2(\alpha)t}(1+t)^{-3/2}\). Its elementary
three-piece proof uses two survival bounds and a central binomial atom.
The established ballot exponent is credited to the earlier source.

Set the floor and reciprocal correction parameter to \(100L(D)\),
rounded upward. The earlier finite future-minimum charges now give a
total high-minimum cycle gap at most
\(CD^{2h_*}L(D)^{h_*-3/2}\). For a low-minimum cycle of period in
\([N,2N]\), its at least \(N\) distinct phase numerators force a maximum at
least \(N/D\). Use the entire above-floor excursion, including its
descent. The excursion has length at least
\((8/3)\log_2(N/(2MD))\), which contains the needed parity word
uniformly for \(D\le N^{11/20}\). The same joint count bounds these
cycles without any gap cutoff.

Separating cycle gaps above and below \(L(N)^{-\eta}\), and using
irrational equidistribution for the smaller gaps, gives the result.
No quantitative irrationality theorem or finite convergence floor is
used. Root and rigidity reconstructed the complete proof independently.

**Open:** one integer cycle can still have an exceptional period. The
density-one conclusion does not remove it.

## 2. Complete first-smaller-meeting laws in growing ordinary samples

Let \(\tau_H\) be the first-smaller-meeting clock after \(H\) prescribed
initial odd steps, with zero if a smaller source has already met the
trajectory by that clock. The smaller visitor has no clock restriction.

[CLOCK_LAW_SUPPLEMENT.md](descent/postpeak/stopped/CLOCK_LAW_SUPPLEMENT.md)
proves an actual finite-shell total-variation estimate. Sample uniformly
from \([X,2X)\) in the prescribed cylinder, where
\(400\le H\le\log_2X/120\), and set \(T=\lfloor H/6\rfloor-1\).
The joint law of the first \(T\) postbits and the complete \(\tau_H\),
including infinity, differs from the explicit fair-binary/Haar-ternary
model by
\[
                         O(H^{-1/2}+HX^{-1/450}).
\]
Finite inverse-word comparisons preserve the actual source in each thin
full binary cylinder. Separate bounds handle late physical ancestors
and long profitable inverse words in the Haar model. The last bin is
removed using the existing sharp sibling tail, rather than by asserting
independence at every clock of one fixed ordinary integer.

The limiting clock is almost surely finite with infinite mean. Each
finite-height density-law clock instead has every positive moment
finite. Using the explicitly cited prior exponential tail in Weaver 178,
\(\mathbb E\tau_H^{1/2}\asymp\log H\), and
\(\mathbb E\tau_H^a\asymp_a H^{a-1/2}\) for \(a>1/2\).
Thus its full mean is \(\Theta(\sqrt H)\). Sub-half moments converge
to the limiting moments. The same growing-shell orders hold with the
explicit cap \(X^{1/(100a)}\). An untruncated empirical moment bound
for each finite sample is not claimed. Root and cycles independently
read the supplement.

**Open:** these source-population laws can still omit an individual
positive source with no smaller visitor anywhere on its future.

## 3. A finite-source variance criterion

[SOURCE_VARIANCE.md](descent/postpeak/stopped/SOURCE_VARIANCE.md) defines
\[
 L_X=\lceil\log_2(2X)\rceil^2,\quad
 V_X=\operatorname{Var}_{1\le n\le X}(F_{L_X}(n)/L_X),
\]
where \(F_t\) counts odd departures. Using Mazur's July arbitrary-
diverging-threshold logarithmic arrival theorem and September positive
lower predecessor-density theorem, it proves
\[
       \text{Collatz}\quad\Longleftrightarrow\quad\liminf V_X=0.
\]
If Collatz holds, \(V_X\to0\); any counterexample forces a strictly
positive lower limit. The statement holds for any deterministic clock
with \(L_X/\log X\to\infty\).

The new diagonal lemma makes almost every member of any fixed target's
basin arrive at that target within \(O(\log n)\) raw steps. Its slow
threshold may be noncomputable, as allowed by the imported theorem.
Positive convergent and nonconvergent populations would then have odd
fractions separated by the gap between \(1/2\) and
\(1/\log_2(10/3)\). Root and rigidity independently checked the
argument and source scopes. The cited external formalizations were not
rebuilt here.

**Open:** no proof of variance collapse is supplied. The short-clock
identity \(V=1/(4t)\) at dyadic cutoffs only applies through the binary
coding horizon and does not establish the required superlogarithmic test.

## 4. Boundaries for component and predecessor arguments

[GENERIC_COLORING.md](descent/postpeak/stopped/GENERIC_COLORING.md)
constructs two colors of density one half with exact invariance under
both multiplication by two and by three, and an adjacent disagreement
set of density zero. It uses slowly changing high-frequency waves and
the six-free core. The affine Collatz relation holds only at density
one. This is not an actual component coloring; its purpose is to show
why those relaxed properties do not force a single color. Konieczny's
related prior asymptotic construction is credited. Root and rigidity
read the whole proof.

[ONE_SITE_MUTANT.md](descent/postpeak/stopped/ONE_SITE_MUTANT.md) gives
a sharper boundary test. Change the map at one arbitrarily high known
convergent odd gate to make that gate fixed. Every complete
first-smaller-meeting clock above the maximum of its finite original
future is unchanged, pointwise. The change can avoid any prescribed
finite set of verified traces. Two disjoint positive-lower-density genuine
predecessor basins force separated long-clock odd frequencies under the
modified map. This is a changed-map construction, not an ordinary
counterexample. Its additional density claims concern fixed horizons.
Root and rigidity independently checked it.

[FINITE_SEED_REDUCTION.md](rigidity/phase12/FINITE_SEED_REDUCTION.md)
uses the cited uniform basin bound to show that every fixed positive
predecessor-mass sector lies in the union of finitely many seed orbits.
It is finite if all orbits are bounded; an escaping orbit makes some
such sector infinite. The remaining fixed-mass-floor logarithmic
sibling-share lower bound is therefore equivalent, under the named
inputs, to no escaping orbits. Bounded nontrivial cycles are still
allowed. Weaver's quantitative input and the earlier Valbuena/Wren
qualitative equivalence receive credit. Root checked both source and
derivation.

## Evidence

The cumulative strict root rebuild count remains **57 distinct Lean
modules**; the cumulative dual-mode finite replay count remains
**39 distinct Python programs**. This checkpoint changes written
proofs and synthesis only. Its complete clean local and API-published
science trees are validated separately by all eleven repository
regression commands. Exact commit identities, production file hashes
and execution receipts are archived in
[checkpoint10](../../reports/astra-reciprocal-rigidity-20261127/checkpoint10/).
Those gates verify repository integrity and bounded controls, not the
new asymptotic claims or the Collatz conjecture.
