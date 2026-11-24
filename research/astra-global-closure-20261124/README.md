# Ordinary mergers, finite-state rigidity, and physical gap series

**Collatz remains OPEN.** This packet records a three-lane research attempt on
the repository frontier of 24 November 2026. It supplies a constructive family
of genuine smaller-source mergers, an obstruction to a broad uniform affine
repair strategy, a written transcendence extension, and executed Lean checks.
None of the restricted results supplies the universal descent or reverse
closure still needed for the conjecture.

**Latest continuation:** [round seven](round7/README.md) adds Lean-checked
directed unit-tripling criteria, a single-suffix head-series reduction,
determinant bounds on full cancellation along one ordinary escape, and
completed paired constructions with their exact endpoint cost. It also records
sparse-edit and tripling constraints. The conjecture remains open; the earlier
rounds below retain their original scope and publication history.

The checkout base is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The [frontier report](../../reports/astra-global-closure-20261124/audit/FRONTIER.md)
and [live metadata snapshot](../../reports/astra-global-closure-20261124/audit/pr146-191.json)
freeze PRs #146–191. All 46 were open and unmerged at that snapshot. The report
identifies exact directions, hypotheses, source heads and missing premises in
the principal closure, scalar, collision, denominator, substitution and shadow
routes. This is selected load-bearing source review, not an independent proof
audit of every statement in all 46 PRs.

A prepublication readback found three concurrently published packets, #192–194,
and an attribution update to #189. They received separate focused reviews at
their new frozen heads; the [comparison below](#5-concurrent-frontier-comparison)
records what changes and what overlaps. The original snapshot remains intact.

## 1. A genuine smaller partner beyond an arbitrarily long local obstruction

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

For every positive integer \(k\equiv148\pmod{256}\) and positive integer \(u\),
put

\[
n=2^{33k}u-17,\qquad m=2^{21k}u-1.
\]

**CS1.** If \(1024\mid T^{33k}(3n-1)\), then

\[
0<m<n,\qquad T^{33k+10}(n)=T^{21k+10}(m).
\]

This is an actual ordinary merger on the stated input, with different forward
clocks on its two arms. It gives a strong-induction step: convergence of the
smaller integer implies convergence of this integer. It does not independently
prove that the smaller integer converges.

The mechanism uses the negative cycle through \(-17\), the negative rail from
\(-52\), and the fixed point \(-1\). They produce positive endpoints \(X\),
\(Y\), and \(X+16\), with
\(3^{k-1}(X+17)=Y+7\). The guard forces \(X\equiv52\pmod{1024}\).
The ordinary ten-step paths from 52 and 68 meet, and both have three odd steps,
so every corresponding lift also meets. The Lean theorem `ten_even_bridge`
checks the broad divisibility-guard version; it does not assume higher digits
of the endpoint or its subsequent convergence.

For the narrower family

\[
3^{22k-1}u=2^e+7,\qquad e\ge10,
\]

the member arm has an explicit certificate
\(T^{33k}(3n-1)=2^e\), so the guard holds. A single unit congruence modulo a
power of three constructs such integers on #174's original section
\(n=27j+1,\ 4\nmid j\), while prescribing arbitrarily many ternary digits.
These are different constructed sources at different precisions; no selector
for every preassigned source is claimed.

**CS2.** The written mixed-adic proof resolves both local points \((-17,0)\)
and \((-17,1)\). With the prescribed binary and ternary precision, *every*
ordinary walk of that length, including legal inverse moves, fails to reach a
smaller positive integer. Choosing precision \(33k\) in the constructed
family gives, for its shortest ordinary walk length \(D(n)\),

\[
33k<D(n)\le54k+20.
\]

Choosing the exponent in one complete discrete-logarithm period gives
\(D(n)=\Theta(\log\log n)\) on this sequence. Thus long local obstructions
and explicit longer successful mergers occur on the same witness-bearing
ordinary sources. The all-walk statement and this asymptotic are written
proofs; the Lean source verifies the lifting, signed-rail separation, finite
tables, endpoint certificate and actual merger.

**CS3–4.** A fixed small menu of periodic offsets does not cover all remaining
parameters. For off-cycle signed offsets the necessary bound is stronger:
in the specified equal-slope partner architecture an endpoint offset must obey

\[
b\ge\frac{(2187/2048)^{3k}}{(63k+1)^{1/6}}.
\]

This excludes a bounded menu of off-cycle offsets for arbitrary \(k\) within
that architecture, even with growing shadow lengths. Different slopes,
changing offsets and other merger constructions remain available.

**Sources:** [full construction and proof](structural/README.md),
[off-cycle bound](structural/OFFSET_BOUND.md),
[Lean](structural/CycleShadows.lean),
[independent written review and replay](../../reports/astra-global-closure-20261124/analytic/REVIEW_STRUCTURAL.md).

## 2. Arbitrary finite causal storage cannot remove the affine residue guard

For the accelerated odd map, let the ordered gap blocks be \(L=(2,1)\) and
\(P=(1,4)\). Their boundary equations are

\[
8q'=9q+7,\qquad32q'=9q+5.
\]

PR #191 gives a smaller affine shadow \((60q+5)/83\) on
\(q\equiv-7\pmod{83}\). We investigated whether a richer uniform shadow
could remove that restriction.

**AR5.** Let a finite deterministic causal machine admit both L and P from
every reachable state. Assign affine shadows \(h_s(q)=aq+b_s\) with a common
\(0<a<1\), satisfying the coefficient identities for output blocks with
the original per-letter clock and two odd steps. If any shadow at an integer
input is integral, then \(83\mid q+7\).

There is no bounded-memory, commuting-transition or synchronizing-state
assumption. The written proof combines odd-denominator rigidity, a translation
obtained from the two affine residue maps, the order-82 action modulo 83, and
a reduction of the remaining 3-primary denominators to finite past memory.

The bounded-past reduction and its complete six-row classification are fully
proved in Lean for arbitrary memory length. A second Lean file checks the
residue and arithmetic lemmas used in the general finite-state argument.
AR5 itself, fixed-size reblocking, and general pure lookahead remain written
theorems. The general theorem has a separate reconstructed review.

This result blocks a proposed *uniform same-clock affine construction*. It
does not rule out an ordinary orbit in another residue class. An orbit-specific
rule, changing clocks, infinite state, or other carry languages could still
work. Finite ordinary witnesses occur in every residue class and at every
prescribed finite horizon; those witnesses do not imply an infinite exception.

**Sources:** [statements and proofs](audit/SHADOW_RIGIDITY.md),
[bounded-memory Lean](audit/MemoryShadow.lean),
[residue Lean](audit/ResidueOrbit.lean),
[independent AR5 review](../../reports/astra-global-closure-20261124/structural/REVIEW_AFFINE.md).

## 3. Heavy machinery with a precise input requirement

For one ordinary positive odd orbit write
\(2^{g_j}q_{j+1}=3q_j+1\), \(A_n=\sum_{j<n}g_j\), and

\[
F_q(z)=\sum_{n\ge0}2^{A_n}z^n.
\]

**GS1.** Eventual periodicity of the odd orbit, eventual periodicity of its
gap word, rationality of \(F_q\), and D-finiteness of \(F_q\) are equivalent.
The nontrivial function-theoretic implication uses Bell–Smertnig's theorem
on D-finite series with coefficients in a finitely generated multiplicative
group. The elementary uniqueness and periodicity extraction have Lean proofs.

Every ordinary source already satisfies \(F_q(1/3)=-3q_0\) in \(\mathbb Q_2\).
That single rational value does not provide a differential equation for the
whole series. A nonphysical specialization counterexample is supplied to mark
this inference boundary. Even universal eventual periodicity would still
require exclusion of nontrivial positive cycles for full Collatz.

**GS2.** For an aperiodic word generated from a growing prolongable letter of
a reducible, nonerasing binary substitution, attach positive rational affine
inverse multipliers with strictly positive 2-adic valuations and distinct
fixed points. The written proof shows that its 2-adic completion is
transcendental. It handles the nonuniform triangular and Jordan cases left
outside #190's primitive hypothesis. The proof uses an exact functional
equation, Padé approximation, and algebraic-height inequalities. In the Jordan
case, approximation over \(\mathbb Q(Y)\) lets the slower coordinate absorb
an unrestricted degree before the fast scale tends to infinity.

Combined with the separately qualified primitive theorem of #190, this covers
pure binary morphic words generated from growing prolongable letters, not
arbitrary coded larger-alphabet words or unrestricted Collatz itineraries.
Earlier positive-rational parity results, including the displayed scalar
Jordan example, are explicitly credited; no priority claim is made. The
transcendence theorem is written and cross-reviewed, not formalized in Lean.
No result in this packet assumes GRH.

**Sources:** [complete analytic argument and literature comparison](analytic/README.md),
[Lean finite core](analytic/GapSeries.lean),
[execution scope](analytic/CHECKS.md),
[independent GS2 review](../../reports/astra-global-closure-20261124/audit/REVIEW_ANALYTIC.md).

## 4. Formal replay and the remaining universal obligation

Eight finite Lean kernels from the pinned #182 and #187–191 sources are
copied with attribution and proof-script repairs under [formal/](formal/).
All **62 inherited public theorem statements and hypotheses are preserved**.
Strict Lean 4.34.1 replay succeeds on all eight files and prints each public
theorem's transitive axioms. The only reported axioms are `propext`,
`Classical.choice` and `Quot.sound`. These are inherited results made executable
here, not 62 new mathematical discoveries.

| Evidence | What was actually checked |
|---|---|
| Eight inherited finite modules | Exit 0 with warnings as errors; 62/62 public-theorem axiom reports; final source hashes unchanged during replay. |
| Four newly authored Lean modules | All compile with warnings as errors; 27 selected theorem axiom reports, including the principal claims; standard axioms only. |
| CS1–4, AR5 and GS2 prose | Cross-agent reconstruction at frozen source hashes, with explicit dependencies and exclusions. |
| Finite Python controls | Exact integer/rational checks with recorded finite ranges; never used as an all-depth proof. |
| Repository validation | Separate clean-checkout integrity gate; this does not establish any mathematical theorem. |

See [formal provenance](formal/PROVENANCE.md),
[strict replay driver](formal/replay.py),
[final replay receipt](../../reports/astra-global-closure-20261124/formal/final-replay.json),
and the [integration review](../../reports/astra-global-closure-20261124/ROOT_REVIEW.md).
The compiler used cached library oleans at the recorded Mathlib revision;
no fresh rebuild or independent-kernel replay of Lean/Mathlib is claimed.

The remaining target is still an actual smaller ordinary partner for **every**
eligible marked source, with correctly matched clocks, or the universal
reverse-closure implication of #174:

\[
\forall j\ (4\nmid j),\qquad
\operatorname{Basin}(3(27j+1)-1)\Longrightarrow
\operatorname{Basin}(27j+1).
\]

The construction here discharges one unbounded guarded family. The finite-state
obstruction explains why extending one recent affine route needs a different
ingredient. The analytic route requires global structure of the actual source
series that has not been proved. Those are the first unsupported steps; none
is silently promoted to a theorem in this packet.

## 5. Concurrent frontier comparison

| Later source | Reconstructed gain | Relationship to this packet and remaining gap |
|---|---|---|
| #192, `be783656f0e889fe0d5318a2f7a9140099cb94b5` | Actual-scalar separation bounds; convergent ordinary witnesses for every finite canonical word; superpolynomial survival after polynomial cancellation. | The witness varies with the word. Separation does not imply the required uncentered scalar triadicity, and numerical gcd cancellation remains distinct. |
| #193, `52beff703fd3ce798c430e5af8199eb58d41bf93` | Another guarded smaller-partner construction; translated interval synchronization at a common odd clock; a necessary complete-denominator inequality. | Its guarded sources are disjoint from the entire #174 section \(n\equiv1\pmod{27}\) reached by CS1–2. Synchronization leaves the least member of each fiber unresolved. No low-complexity cycle scale is guaranteed. |
| #194, `764f3a9f539febf3d2661a9ca4acc1b10827878c` | Improved carry-entropy and height restrictions; injective-set occupation; the reducible binary substitution extension. | Its substitution theorem substantially overlaps GS2, and its fixed-word version removes finite prefixes. GS2 is corroborating work, with no priority claim. GS1 and the checked physical-tail consumer have a separately identified scope. |

For #193 the disjointness is exact: positive ternary height makes its source
divisible by three; height zero forces \(n\equiv40\pmod{81}\), hence
\(n\equiv13\pmod{27}\). Its valid construction and the present construction
therefore cover different guarded inputs. Its count of interval fiber minima
does not certify descent for a prescribed minimum.

For #194 the improved height requirement still lacks an opposing upper bound,
and the occupation theorem requires injectivity on the whole invariant set.
Its explicit inverse tree blocks extending that charging proof to the whole
predecessor basin. The common substitution result does not force substitution
structure on an arbitrary ordinary itinerary.

The same upstream finite kernels were also made executable in #194. The
formal replay here supplies independent standalone repairs and source-bound
execution evidence; it is not claimed as the first compilation.

The focused reports provide precise claims, source blobs, exclusions and limited
independent arithmetic controls: [#192](../../reports/astra-global-closure-20261124/late/REVIEW_PR192.md),
[#193](../../reports/astra-global-closure-20261124/late/REVIEW_PR193.md),
[#194](../../reports/astra-global-closure-20261124/late/REVIEW_PR194.md).
