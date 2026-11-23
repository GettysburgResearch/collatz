# Repository reassessment and three direct attacks

23 November 2026. Parent: c91b80a3156e640ad471cf30c47721145ae21eb1.

**Full Collatz remains OPEN.** This checkpoint records a whole-repository
reassessment, three parallel attempts at the missing global implications,
new scoped deductions, and independent reviews. The attempts did not produce
a universal accepting candidate, the required actual-source collision
upper bound, or an exclusion of all nontrivial positive cycles.

The main results classify an entire global additive-potential class, exclude
every finite time normalization of the proposed unchanged escaping graph as
a conservative minimal process, and force a quantitative real-growth gap
for the existing canonical candidate stream. These are restrictions on
prospective proof methods and counterexample behavior, not a full proof.

## 1. Repository scope and maps

[REPOSITORY_REASSESSMENT.md](REPOSITORY_REASSESSMENT.md) relates seven proof
architectures and their actual remaining implications. The pinned
[repository snapshot](../../reports/2026-11-23-reassessment/REPOSITORY_SNAPSHOT.json)
covers all 145 open and closed PR records fetched in this pass. We revisited
the integrated map, open obligations, older merger and rewrite routes, and
the changed construction, actual-law and complete-denominator interfaces.
This does not claim a fresh proof audit of all 145 branches.

Throughout, the shortcut and odd accelerated maps are

\[
T(n)=
\begin{cases}
n/2 & n\text{ even},\\
(3n+1)/2 & n\text{ odd},
\end{cases}
\qquad
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

All ordinary sources in the new deductions are positive integers.
Hypothetical escaping components and nontrivial cycles are assumptions,
not asserted examples. Each lane ledger pins the source commit and exact
file used; peer PR descriptions are orientation rather than proof sources.

## 2. Global additive potentials: an exact classification

The [cycle packet](cycles/PRIME_POTENTIAL_AND_FULL_CLOSURE.md) uses the primary
Applegate–Lagarias semigroup theorem to prove the following written result:

> Let \(F\) take values in an ordered abelian group and be completely
> additive: \(F(ab)=F(a)+F(b)\). If \(F(T(n))\le F(n)\) for every positive
> integer \(n\), then
> \[
> F(n)=v_3(n)c\quad\text{for some }c\ge0.
> \]
> Conversely every such \(F\) satisfies those inequalities.

For the odd accelerated map, the same classification holds on the odd
integers. Under monotonicity just on odd sources prime to three, the
potential is zero on all those sources. The proof preserves that source
restriction using the sign of the three-adic valuation of every semigroup
generator. It does not mistake a multiplicative representation for a
chronological trajectory.

The classification includes finite lexicographic vectors of completely
additive features. Every such global potential is zero on every positive
periodic orbit. This excludes a broad potential class as a means of
distinguishing or excluding those cycles. It does not classify nonlinear
ranks, weights depending on the state, or potentials required to decrease
only above an arbitrary verified floor.

A separate exact certificate uses the actual paths

\[
25\to19\to29\to11,\qquad55\to83\to125,
\qquad25\cdot55=11\cdot125.
\]

Their five additive edge changes sum to zero. If all five are nonpositive,
all are zero. The five edges, full prime-product balance, and this finite
obstruction are Lean-checked. This is not a cycle: the two paths are open.
The minimum source is 19 and the minimum endpoint is 11; no arbitrary-floor
conclusion is asserted.

The semigroup theorem and the global classification are **source-qualified
written mathematics**, not part of the new Lean formalization.

## 3. Finite normalization: universal explosion and exact missing flux

The [collision packet](collision/FINITE_CLOCK_AND_FIXED_SOURCE.md) starts
with one hypothetical escaping ordinary eventual-meeting component \(E\),
its original successor \(U\), and a positive harmonic flow

\[
\nu(q)=\sum_{Un=q}\nu(n).
\]

For **any** positive finite rates \(c(n)\) such that

\[
M=\sum_{n\in E}\frac{\nu(n)}{c(n)}<\infty,
\]

every fixed source satisfies the exact infinite-series bound

\[
\boxed{\sum_{j\ge0}\frac1{c(U^j n)}\le\frac M{\nu(n)}.}
\]

The minimal process with those exponential holding rates and the unchanged
ordinary successor therefore makes infinitely many jumps in finite time,
almost surely. Its expected lifetime is at most \(M/\nu(n)\).
The probability \(\pi(n)=\nu(n)/(Mc(n))\) satisfies the coordinate balance
equations, but the minimal process killed at explosion loses all its mass
as time tends to infinity. Thus it is not stationary under \(\pi\).
This excludes every finite normalization in this proposed construction,
not only power-law clocks.

If the spine flow tends to a finite capacity \(C\), its indicator \(f\)
and finite truncations \(f_J\) exhibit the precise flux defect:

\[
\int Qf\,d\pi=C/M,\qquad
\int Qf_J\,d\pi=0,
\]
\[
\|f_J-f\|_{L^1(\pi)}\to0,\qquad
\|Qf_J-Qf\|_{L^1(\pi)}=C/M.
\]

Here \(Qf\) denotes the pointwise rate expression. Generator-domain
membership is not inferred from its integrability. Nonminimal conservative
extensions may add entrance or resurrection behavior at infinity; they
require an additional boundary law and are not ruled out by this theorem.

The deterministic infinite-series core is Lean-checked. The process
consequence and flux identity are independently reviewed written proofs.
No replacement actual stationary collision upper bound is constructed.

## 4. The canonical candidate stream has a real-growth gap

The [construction packet](construction/REAL_GROWTH_GAP.md) retains the
repository's existing canonical boundary stream \(\eta_k\) for one unchanged
positive source \(n\). Put

\[
N=\operatorname{bl}(n),\qquad
M_K=\max_{0\le j\le K}|\eta_j|,\qquad
\alpha=\frac{\log(4/3)}{\log3}.
\]

If \(K\ge N\) and the actual shortcut orbit avoids \(\{1,2\}\) through
time \(K\), the new finite estimate is

\[
\boxed{
M_K>
\frac1{2\,3^{N/2}}
\left(\frac{2^{K+1}}{n+1}\right)^{\alpha/2}.
}
\]

The proof combines the full-carry jump at a parity defect with the maximum
possible length of the final alternating block from that same source.
Thus a nonconvergent source forces exponential growth of the running
maximum. Boundedness, or subexponential growth, of this literal stream is
equivalent to reaching the core.

**The required upper estimate remains unproved.** The simultaneous-carry
attempt supplies no such upper bound. The estimate concerns a running
maximum, not every individual candidate, and is not an upper bound on the
earlier optimized certificate height. Its stronger escape-only version
retains the additional Monks–Yazinski source theorem; it is not applied to
a hypothetical nontrivial cycle.

The note also relates these same defect symbols to Monks's polynomial
\(q\)-analog. It does not deduce finite transformed support from the finite
binary representation of the original input. This lane is reviewed written
mathematics; it adds no Lean wrapper for the unresolved upper estimate.

## 5. Uniform repeat budget, and the direct gaps that remain

A second result in the collision packet is uniform over all exact gap
templates. If a positive odd source \(p\) begins with \(k\ge2\) copies
of a word of length \(d\) and total gap \(A\), then either \(U^d(p)=p\),
an actual cycle, or

\[
2^{(k-1)A+1}\mid U^d(p)-p,\qquad
2^{(k-1)A+1}<(3/2)^d(p+1).
\]

In particular, an exact prefix square \(ww\) at a nonperiodic source
requires \(p+1>2(4/3)^d\). At a later window of the same source, the
preperiod factor and the condition that the window source is not already
periodic must both be retained. Independent review caught and repaired
this condition before the checkpoint was frozen.

This is a necessary height payment, not an actual collision upper:
equal residues do not yet force exact repeated words with a violated
source/time budget. The packet states the same-source, same-limit
effective-box-mass bound which would close that comparison, with all
source quotients, full carries and cross-box terms retained.

The complete-cycle lane also records the exact failed cancellation target.
For a hypothetical nontrivial primitive positive integer cycle of period \(K\),
let \(b\) be its even count and let \(C_*\) be its complete numerical
complementary carry. The retained capacity result gives

\[
q=\frac{2^K-3^b}{\gcd(2^K-3^b,C_*)}>K/2.
\]

An opposing bound would follow from

\[
\gcd(2^K-3^b,C_*)\ge\frac{2(2^K-3^b)}K.
\]

**This inequality is open.** The new bilinear identity does not establish
it because its complementary integer numerators themselves depend on \(q\).
No selected factor replaces the complete gcd.

## 6. Verification and boundaries

The [report index](../../reports/2026-11-23-reassessment/README.md) records
frozen source hashes, primary-source ledgers, and independent reviews.

- The collision and cycle Lean modules each passed author and independent
  reviewer builds in separate output directories.
- Across the two lanes, all **14 authored theorem declarations** were
  audited. The axiom union is only propext, Classical.choice, and
  Quot.sound; no sorryAx was reported.
- Builds used Lean 4.34.1, compiler commit
  5045d0056413266e57c625dcd7c365b10e377c52, with
  autoImplicit=false and warningAsError=true, against mathlib
  d13f23b723b8a846827a245b89c10fc7d3f11612.
- Existing dependency objects were reused. The older proof corpus was not
  rebuilt, and these builds do not formalize the written classification,
  stochastic argument, flux, growth gap, or repeated-word theorem.

The repository's required integrity validation is a separate release gate
on the complete clean checkout of the new commit. Its receipt belongs to
the PR record after that exact commit exists; it is not mathematical
verification of the full Collatz conjecture.
