# Checkpoint 2 — all-clock targets and a native singular trace

**Active pass, 28 November 2026. No complete Collatz proof is claimed.**
The requested interval continues through 21:31:15 UTC. This review records
independent reconstruction by the coordinator, not merely agreement with an
author summary. The evidence receipt distinguishes written arguments, finite
controls and locally compiled Lean.

## 1. All-clock arrivals at nearby targets

**Source pin:** arithmetic author commit
`bdc5bad4e078240fc3fd9c08a0abd626923b2cf2`,
`research/astra-global-pursuit-20261128/arithmetic/ALL_CLOCK_ADJACENT_TARGETS.md`,
sections 1–4; imported at `71af86ef84a2d2c07c6395c1a195d314113b7dac`.

**Verdict: VERIFIED as a reconstructed written deduction.** The entire
statement is over positive ordinary sources and distinct ordinary targets.
The coordinator checked the following load-bearing points.

For an initial interval of length R, the synchronous image has at most
C(R 2^(-J/40)+2^J) values. Split parity words at odd fraction 3/5: below
that threshold their endpoints fit in a short interval; above it their
source cylinders have the binary entropy bound. Both strict numerical
inequalities used to weaken the rate to 1/40 are exact integer inequalities.

A union of N complete positive orbits meets an initial interval in at most
M_J(R)+2NJ points. Insert each orbit into the preceding union, decompose
its new points into a transient segment and a cycle or infinite ray, and
delete the last J points of finite transient pieces. The remaining J-step
images are injective and lie in disjoint pieces. They need not stay in the
original height interval: their membership in T^J(I_R), of size M_J(R), is
the counting fact. Every arrival from sources at most S after date J lies
on one of the M_J(S) forward orbits rooted at date J. This gives one bound
for **all later dates together**, including arbitrary intermediate heights.

With J=floor((2/5)log_2 Y), the full late-target set from sources through
3Y^(1.001) has O(log(Y)Y^(.991)) points in a target interval of size O(Y).
Allowing target translations of magnitude Y^(.001) still fits the stated
O(Y^(.995)) exception. For two earlier clocks, distinct affine slopes are
separated by at least 2^(-J). The endpoint equations force
y=O((9/2)^J(1+|h|+|k|)), contradicting y at least Y. This argument is
pointwise in both displacements, so it does not pay another union bound
over the adaptive source displacement. Equal slopes force identical clocks
and odd counts by unique factorization.

For adjacent smaller visitors, the full set of successful words and
orientations therefore transfers to a ternary Haar marked set in total
variation with the claimed polynomial error. Native legality follows from
the full inverse equation and the binary cylinder, not from the ternary
congruence alone. Positivity and the strict source cutoff hold uniformly
for the retained short words; high-gain words beyond J have a summable
entropy tail. The prefix-free reversed language and the probabilities
1/4, 3/4 give the upper bounds 3/5 and 4/15 after the actual target-class
and gain restrictions. This proves that the particular smaller-adjacent-
pair certificate is absent at at least 11/15 of least-failure candidate
positions asymptotically. It does not exclude other smaller visitors or
prove that any candidate is a counterexample.

The coordinator read Weaver Papers 177(v1) and 178(v1), including the
orbit counting and gain-tilt inputs, and reconstructed their elementary
uses here. The paper's provenance section credits these prior results.
The independent-clock exact checker passed normally and under optimization:
312 target/threshold combinations, 59 actual marked visits, and both
reported truncated Haar masses. These are finite controls, not evaluations
of either full infinite mass.

## 2. Locally compiled native determinant envelope

**Source:** `research/astra-global-pursuit-20261128/CenteredDeterminant.lean`,
coordinator implementation; exact source SHA-256 in the evidence receipt.

**Verdict: VERIFIED by fresh local Lean 4.34.1 compilation.** The module
imports only Std and compiles with warnings as errors. Eight displayed
theorem roots have only the standard logical axioms, with no sorryAx.

The integer shortcut map is linked exactly to its centered form. The
two-arm determinant has the stated transport law. A backward linear
envelope bounds every prefix from its terminal bound and bounded correction.
The native version defines the actual iterates and departure counts, proves
count monotonicity, and applies the envelope when the terminal even counts
agree and the terminal values differ by one. A separate coprime-power
argument proves the divisibility and length bound for a nonzero shared-odd
run. The infinite rational generating functions and density transfers are
not Lean theorems in this module.

## 3. A specified native Mellin trace of ordinary cycle basins

**Source pin:** independent author commit
`1e80f01b8fddb9a40ed24268db0d95c77dd76d67`, files
`research/astra-global-pursuit-20261128/wild/CYCLE_MELLIN_RESIDUE.md`,
`UNBOUNDED_CONDUCTOR_TRACE.md`, and `SINGLE_SCALE_POLE.md`.

**Verdict: VERIFIED as a source-qualified written deduction.** The
coordinator read the primary Weaver Paper 19(v2), formulas B1–B6, F2–F13,
S2 and Q7, and Paper 12(v1), formulas 23–29 and 35. The canonical integer
profile, positive atom floor, inverse law, bounded selection identity,
orbit packing and relative landing estimates remain explicit outside
inputs. No outside formal package or analytic theorem was rebuilt here.

For a nonperiodic odd unit a, the published change of inverse measure
implies G_a(1)=delta*d_a with delta=log(4/3)/2. For a cycle, one complete
inverse lap has both selection probability and residual multiplier lambda.
Thus G_a(s)=B_a(s)/(1-lambda^(1-s)). At exponent one, an exit through an
off-cycle parent y contributes exactly delta*d_y: the affine multiplier
cancels against the relative residual. The entrance basins are disjoint.
Their countable sum equals the cycle basin density by the relative
first-landing bound, including the possible nonunit parents. This is not
an unjustified countable sum of individually zero-density sets.

The cycle residue at a is delta*d_C/L_C, where L_C is the sum of
log(1+1/(3x)) around the cycle. At the standard one-cycle this is d_1/2.
Weighting the root residues by those logarithms and summing gives delta
times the density of the entire eventually periodic set. Uniform orbit
packing bounds the nonperiodic contribution; a cyclewise bound by C*d_C
permits summation across cycles. Minimum-tail tightness identifies the
sum of basin densities with the density of their countable union.

The singular observable is also legitimate at every finite ternary
conductor. The new real interval bound follows by stopping the mean-one
multiplier product at y/L, using exponential tails for the killed product
sum on noncrossing paths and the primary uniform interval bound on the
independent tail after crossing. It yields the uniform terminal estimate
|g_(1-u)(x)-rho_1(x)| <= C*x^(-1/4)+C*u^(-4)(1+log x)^2/x.
Peeling all but one ternary digit gives the exact native formula, with
the final digit and strict real cutoff both retained.

For one explicit simultaneous limit, take u=K^(-1/5). Distinct inverse
states and uniform orbit packing make the terminal error average
O(K^(-1/4)+u^(-4)/K). Bounded selection handles the remaining fixed-root
test without a claimed convergence rate. Resolving complete cycle laps
is an exact finite renewal identity. For the sum over all cycles, the
coordinator checked two separate uniform controls: the union of periodic
vertices has a power-sparse height count by synchronous injectivity, and
the weighted forward sum telescopes to O(1/u). The latter bounds all
cycle-exit contributions by C*d_C independently of period. The unbroken
cycle prefixes contribute O(u^(-4)/K). These are the steps that permit
the moving exponent and the unrestricted cycle sum simultaneously.

The result computes unknown basin densities; it does not yet evaluate
the fixed-root limit as 1/2. A proof of that value, together with the
outside positive predecessor-density theorem, would give full Collatz.
This remains an active attempted route.

The exact finite controls passed normally and under optimization: 22,506
word/seed/root tuples, 1,035 singular pullback identities, 480 padded
ordinary laps, 21 finite renewal calendars, and a 2,000-source entrance
census with 1,119 deadline-limited arrivals. They check algebra and
normalization; they do not approximate the stationary law or certify an
asymptotic basin density.

## 4. Wider repository intake and continuing work

The independent concurrent PR221 was read at
`f8602319553c29b7ed11d180369f7ef381fb0c5e`. Its fixed-cone approximation,
spatial excess, conformal pressure and boundary-address notes were shared
with the agents as possible connections, not incorporated as proved inputs
to the statements above. Its authors are working their own nine-hour pass.

Our agents continue toward positive ordinary inverse bounds, evaluation of
the fixed-root trace, and architectures beyond adjacent visitors. The
checkpoint is a durable intermediate result, not completion of the
requested nine-hour interval.
