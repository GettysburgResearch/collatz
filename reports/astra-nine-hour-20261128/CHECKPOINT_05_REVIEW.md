# Checkpoint 05: critical pressure, arithmetic transport, and ordinary clock groups

**The nine-hour pass continues; Collatz remains unresolved.** This review
records the coordinator's independent reconstruction of the fifth
scientific snapshot. All 21 new files were frozen before the aggregate
replay. The written analytic theorems retain their named external inputs;
the Lean files prove the narrower finite statements described below.
Every draft and all work after phase five are excluded.

## The critical inverse problem has an exact pressure

[UNIFORM_INVERSE_PRESSURE.md](../../research/astra-nine-hour-20261128/machinery/phase5/UNIFORM_INVERSE_PRESSURE.md)
proves a variational principle for the weighted inverse row at the
**worst supplied positive integer**. If a legal word of n odd inverse
steps has total exponent S, let its weight be exp(−tS). The exponential
rate of the minimum row is the same as both first-trit Haar averages of
the logarithm. It is exactly

\[
 P(t)=\sup_\pi(B_\pi-tA_\pi),
\]

where the supremum uses positive finite-window policies, with mean gap
A and conditional action entropy B. The coordinator checked each
direction. Supermultiplicativity gives the minimum-row limit. A bounded
one-edge route compares the two Haar means. At fixed depth, capped Gibbs
words can be chosen uniformly over all finitely many source cells.
Their stationary block occupation becomes a finite policy: the newly
exposed trits are independent of the stored word, and entropy
conditioning gives the required inequality. Mixing occupation flows
before normalizing preserves stationarity. Conversely Weaver 127's
uniform finite-policy theorem and the Gibbs inequality bound every
supplied row. The nonnegative difference between a logarithmic row and
its minimum then gives convergence in Haar probability.

Consequently reverse relative entropy per digit always has a limit,
and the worst cylinder has the identical exponential deficit:

\[
 \Lambda(t)=P_0(t)-P(t),\qquad
 P_0(t)=-\log\!\left(3(e^t-1)\right).
\]

This strengthens the preceding liminf/limsup comparison. It does not
assume that a Haar logarithmic average controls a worst point. The
finite-policy variational argument proves that comparison here.
The critical endpoint is equivalent to the pressure becoming the line
−ta* for every t at and above the critical parameter. The finite entropy
identity B+log 3 = H(E given the next state), followed by the maximum
entropy bound at fixed mean, proves this equivalence. Equality with the
analytic reference pressure on the certified interval and strict
inequality above the critical parameter also force some failure of
real analyticity between these ranges; the location is undetermined.

Weaver 150 already asks for sublinear critical reverse entropy, and
its public discussion distinguishes it from forward entropy dimension.
That question is credited. The new claim is the exact pressure and
variational formulation, not a proof that the critical deficit vanishes.

## A concrete dual, a transport formula, and an arithmetic obstruction

[CRITICAL_BELLMAN_LIFTS.md](../../research/astra-nine-hour-20261128/machinery/phase5/CRITICAL_BELLMAN_LIFTS.md)
identifies exactly what happens when the true critical source law is
inserted into a finite Bellman inequality. The actual successor's lower
digits have the correct marginal. The finite policy replaces its last
digit by Haar, creating a specific imbalance rather than a stationary
critical flow. If V is a Bellman potential at precision W, then

\[
 c_W-a_*
 \le \langle\bar\mu_{W-1}-\mu_W,V\rangle
 \le \sqrt{d_W/2}\,\|\operatorname{osc}_{\rm last}V\|_{L^2(\mu_{W-1})}.
\]

Here d_W is exactly H(E given the W source digits). It decreases to
zero by the imported full entropy dimension. Thus a uniform last-trit
oscillation bound would settle the limiting inverse-cost endpoint.
The source-action averaging, entropy chain rule, Pinsker estimate and
Haar-coarsening telescoping identity were separately reconstructed.

The finite C++ program proposes a potential numerically, rounds it to
rationals, and checks the complete finite Bellman inequalities by an
integer cyclic minimum. It covers every action through one full
doubling period; larger congruent gaps are dominated. At W=2 through
12 it certifies cost brackets of width at most 10⁻⁸ and last-trit
oscillation at most three for the displayed feasible lower duals.
The critical weighted square means, drifts and entropy values remain
floating diagnostics. These finitely many certificates establish no
bound uniform in W. The related finite decision-change and whole-span
measurements in Wren 154 are credited.

[CYCLIC_TRANSPORT.md](../../research/astra-nine-hour-20261128/machinery/phase5/CYCLIC_TRANSPORT.md)
gives a different exact description of the same finite optimum.
Index the units modulo 3^W by powers of two, on a cycle of length N.
For any proposed stationary lower marginal, let α be its uniform
three-lift source distribution and β its shifted odd-arrival
distribution. With cumulative discrepancy
D_k = sum through k of (α−β), its optimal mean cost is

\[
 C_W(\nu)=\sum_kD_k+N\max_k(\alpha_k-D_k).
\]

The extra α term is essential: every source must traverse at least
one edge, and an arrival at the same residue costs a complete turn.
The coordinator reconstructed the lower current bound and the converse
by first routing this compulsory edge, cutting at a zero residual
current, and matching sources to sinks on the resulting line. The
alternative cut-rank minimax formula has the same indexing and cost.
The critical law's unsmoothed lower marginal cannot simply be imposed:
the discrepancy is accumulated in discrete-log order.

The new character identity is also exact. A primitive multiplicative
character applied to 1+3u has Fourier coefficients of squared size
3/(2|U|) at every primitive lower character and zero at all others.
The substitution u/(1+3u) turns its autocorrelation into principal-unit
shell sums, leaving the three values 1, −1/2, −1/2 on the final
order-three subgroup. Fourier transformation proves the statement.
This is an elementary finite character argument, independently
reconstructed without invoking an unproved cancellation estimate.

One consequence is a family of prescribed lower marginals with uniformly
bounded positive densities whose transport cost grows at least as a
constant times sqrt(N). Choose the phase of a primitive cosine mode to
align its two transformed coefficients. A unit-circle character
telescoped along the directed transport gives the lower bound.
This excludes a particular construction; it leaves the minimizing
marginal free. Exact cyclotomic controls check the finite transform.

### A generic entropy shortcut is false

[CONDITIONAL_ENTROPY_COUNTEREXAMPLE.md](../../research/astra-nine-hour-20261128/machinery/phase5/CONDITIONAL_ENTROPY_COUNTEREXAMPLE.md)
constructs a uniformly elliptic ternary-tree measure having
sublinear forward relative entropy **uniformly after every cylinder**,
but strictly positive reverse entropy rate. The coordinator checked the
entire birth-and-death construction.

Under Haar, two adjacent downward barriers in each dyadic octave give
stationary score weights comparable to (s+1)⁻². Under the proposed
measure, the ordinary upward drift 1/(s+12) changes the downward/upward
product to a multiple of (s+1)⁻⁴. The product is summable, so this score
chain is transient. Its local forward entropy tends to zero, and
expected visits to any fixed finite set are uniformly bounded over all
starting scores. The entropy chain rule therefore proves the uniform
conditional forward assertion. Haar positive recurrence instead
averages a strictly positive local reverse entropy.

Thus even that strengthened abstract entropy input cannot close the
Collatz endpoint. The affine arithmetic, or an additional property
that the example lacks, must enter. The example is not a modified
Collatz orbit and is not a counterexample to the conjecture.

## Ordinary-source eigenfunctions and both physical clocks

[NATIVE_MELLIN_RIGIDITY.md](../../research/astra-nine-hour-20261128/escape/phase5/NATIVE_MELLIN_RIGIDITY.md)
classifies the possible macroscopic profiles of all bounded exact
branch eigenfunctions. A nonzero profile can survive only at

\[
 u_0=2^{-i\tau},\qquad u_1=(3/2)^{i\tau}.
\]

At resonance it is a multiple of the real size character; the
source-demodulated amplitude has an exact height-ordered boundary
series. The only Collatz-specific analytic supplier is the pinned
signed starting-trit law for the full actual endpoint and odd count.
Iterating the resulting two-shift equation and comparing adjacent
binomial coefficients forces twisted log-three periodicity.
Irrational rotation on the resulting circle leaves at most one Fourier
mode. A two-sided renewal theorem supplies the amplitude and its
uniformity over the bounded eigenfunctions.

The coordinator read Blackwell's 1953 Theorem 1 directly. It explicitly
permits increments of either sign with positive mean; the sign-reversed
walk here is nonlattice. The residuals have uniform integrable tails
and lie in a fixed finite-dimensional family on each compact interval,
which justifies the stated uniform renewal passage. The grouped
boundary series and its cutoff term were independently checked.
Absolute summability of the individual summands is not asserted.

[SMOOTH_SOURCE_CLOCK_GROUPS.md](../../research/astra-nine-hour-20261128/escape/phase5/SMOOTH_SOURCE_CLOCK_GROUPS.md)
then proves rapid inverse-log convergence for smooth physical source
windows, uniformly over the bounded functions. The forcing is Schwartz
after smoothing on logarithmic size. A fixed two-logarithm lower bound
controls the reciprocal Fourier symbol; the only real zero in the
trivial phase case is removed by a smooth step with the correct mass.
The homogeneous remainder vanishes by the negative-drift walk.

For finite root-of-unity phases, this gives an actual joint
total-variation law for the component and the signed physical/odd
clocks modulo M, after quotienting by the cycle-lap relation on bounded
components. The assertion is uniform over reference choices and holds
through M ≤ (log X)^(1/11). The coordinator directly read
Bondareva–Luchin–Salikhov's 2018 Theorem 1, printed page 18:
its exponent 4.116201 for integer linear forms in 1, log 2 and log 3
supports the reciprocal exponent 10.232402 used here. This external
Diophantine bound is not part of the Lean replay.

On a hypothetical fixed escape, the exact corrected-height identity
and the known signed-clock Gaussian place almost all mass on only
O(sqrt(log X)) clock pairs in a proportional source window. Hence
moduli larger than (log X)^(1/4) would have conditional distance tending
to one from Haar. A general mixing theorem beyond that threshold would
exclude escape. The established exponent 1/11 does not cross it.
The surviving resonant boundary amplitude remains an explicit gap.
PR212's native Green spectrum and symbolic annulus rotation results
concern different operators and are credited as such.

## Whole-cycle arithmetic and physical domains

[SPARSE_LOCAL_VALUATIONS.md](../../research/astra-nine-hour-20261128/cycles/phase5/SPARSE_LOCAL_VALUATIONS.md)
proves a fixed-place valuation theorem for bounded signed sums of
two-three monomials with moving coefficients of sublinear logarithmic
height. After taking limiting exponent groups, the first nonzero group
determines the valuation at the corresponding prime. In an exact zero
sum, every limiting exponent-pair group cancels exactly.

The coordinator reconstructed the rational p-adic Subspace Theorem
application, including denominator clearing, primitive normalization
and the contradiction from the largest distinct real exponent.
It applies to arbitrary signs at a fixed number of terms.
At an ordinary minimum it forces the two exact clock corners in every
such bounded signed representation of the physical numerator.
It also makes the triples consisting of the two clock powers and the
minimum Zariski dense along any infinite ordinary-cycle family.
No bounded signed representation is forced for an arbitrary cycle.

[PHYSICAL_LOOP_ARMS.md](../../research/astra-nine-hour-20261128/cycles/phase5/PHYSICAL_LOOP_ARMS.md)
retains the domains when combining return maps. Doubling and the known
return arm centered at two already generate the entire undirected
ordinary orbit relation. Dropping their integral domains changes that
problem. Without doubling, sufficiently long nonstandard full-lap arms
cannot be applied at one. Entering the reverse arm at a polynomially
small nonstandard minimum by doubling requires at least exp(c n/log n)
doublings. The coordinator downloaded Yu's 1999 primary paper and read
Theorem 1 with its field and height conventions; it has precisely the
required height-times-log-exponent bound without an independence
assumption. The primary PDF SHA-256 is
5caa9d90742661045332e15ac4b38f03eeff82c41b341f6b01ea5f90648c068d.

[SCHEDULED_FLOOR.md](../../research/astra-nine-hour-20261128/cycles/phase5/SCHEDULED_FLOOR.md)
connects integral Apéry quotient coefficients back to the actual odd
numerators. At canonical height at most one the resulting scheduled
floor dynamics are deterministic, but normalization and downward
closure of the hole set are indispensable. Exact controls produce
closed nonzero-digit floor paths that fail these conditions.
The coefficient dictionary credits PR188 and concurrent PR213.
Wren 119 and Voyager 123 already exclude this height class on selected
large rungs; no universal height-one exclusion is claimed here.

[LAG_RATIO_SPECTRUM.md](../../research/astra-nine-hour-20261128/cycles/phase5/LAG_RATIO_SPECTRUM.md)
tests every reduced physical endpoint ratio at every lag. Equal ratios
occupy separated lag classes because their positive accumulated
corrections lie in one interval of the total clock defect.
At density-one lags of a growing ordinary-cycle family, all reduced
endpoint ratios consequently have growing height. At two-sided best
clocks, equal products preserve both additive clock labels. At
one-sided records, no proper subset of actual odd edges can balance
its source and target products. A five-edge ordinary example has full
minimal product balance but different endpoint multisets, showing why
this last property alone does not force a cycle.

## The binary witness and the formal boundary

[BINARY_REACHABILITY_WITNESS.md](../../research/astra-nine-hour-20261128/phase5/BINARY_REACHABILITY_WITNESS.md)
gives an elementary proof of an already known obstruction. A
first-order formula selects exactly a consecutive odd run ending at a
transient power of two. Remembering the binary valuation of the start
plus one yields the relation 3^(k−1) divides a between the two
power-of-two exponents. Taking least targets defines
{2^(3^j) : j≥1}, whose binary language is not regular.
Every witness is explicitly terminating. Arithmetic and escape agents
independently checked the transient-target condition and pumping step.
Wren 64/v2 already implies binary nonautomaticity of full reachability;
Dhiman–Pandey already handles independent bases. No novelty for that
conclusion is claimed.

The four new Lean modules check specific connected interfaces:

- WindowOccupation proves finite occupation conservation, flow mixing,
  and addition of first-hit clocks off a periodic orbit.
- TritTransport proves the actual +2 inverse-gap repair, complete
  trit coverage, averaged dual inequality, and minimum-current facts.
- BalancedCarry proves the full prescribed binary divisibility of the
  quotient coefficients, actual odd numerator reconstruction, and the
  binary-level floor identity.
- ClockQuotient proves independence of two meeting-based clock
  coordinates on a simple reference and modulo laps on a periodic
  reference. The arbitrary preperiodic reference is handled by a
  reference shift in the written argument.

The aggregate replay, exact source manifest, paired finite controls and
clean-checkout receipts accompany this review. The global inverse
endpoint, elimination of the resonant escape amplitude, and exclusion
of arbitrary positive cycle words remain open.

The fresh aggregate passed 21 modules and 441 declarations, including
47 private declarations, with only propext, Classical.choice and
Quot.sound in their transitive axiom sets. Five Python controls passed
in both ordinary and optimized modes with identical paired output.
The C++ Bellman program passed its ordinary and undefined-behavior
sanitized builds. The frozen manifest contains 107 scientific sources;
the publication updates the packet index after that replay and does not
alter the checked Lean or control sources.
