# Checkpoint 09: exact collision limits, conformal countermodels and clock inversion

**The nine-hour pass continues. Collatz remains unresolved.** The coordinator
independently reconstructed the written arguments below. External analytic
inputs retain their stated source qualifications; finite controls and Lean
kernels have narrower, explicit scopes.

## The critical collision slope and the individual increments

For the fair geometric gap law, let \(\rho\) be its stationary ternary
density, \(\rho_n=\mathbb E(\rho\mid\bmod 3^n)\),
\(E_n=\int\rho_n^2\), and \(D_n=E_{n+1}-E_n\).
[EXACT_COLLISION_ENERGY_SLOPE.md](../../research/astra-nine-hour-20261128/escape/phase9/EXACT_COLLISION_ENERGY_SLOPE.md)
proves
\[
 E_n/n\longrightarrow D=2\kappa\left(\log3-\tfrac43\log2\right)>0.
\]
Weaver 146 proves the exact density tail \(m(\rho>t)\sim\kappa t^{-2}\),
the cubic cap bound, and the integrable cross-branch interaction \(D\).
It explicitly leaves the existence of this energy slope open. The
coordinator read its cap argument, renewal proof and final open question.
[Weaver 146, §§6–8](https://rstation.ai/problems/collatz/papers/146)

The new upper bound separates the maximum multiplier of the first \(n\)
letters from the later maximum. Above \(\exp((\mu+\varepsilon)n)\),
the squared-word tilt \(p_e^*=3/4^e\) gives an exponentially small prefix
crossing probability. A fresh fair suffix stays below multiplier two
with probability at least one half. Consequently each prefix shell is
dominated by a constant times a full-path shell. Its small mass and the
cubic cap estimate make its \(L^2\) norm exponentially small. The sum
has only \(O(n)\) nonempty dyadic shells. Below that cutoff, the chance
that the unseen suffix crosses the larger cap
\(\exp((\mu+2\varepsilon)n)\) is exponentially small conditional on
the entire prefix. The conditional density is therefore bounded
pointwise by the larger capped density divided by \(1-o(1)\).
Its squared norm is at most \(2\kappa\log B+o(\log B)\).
Let \(\varepsilon\) decrease to zero and use the published lower bound
\(D\le\liminf D_n\). This proof uses the inputs of Weaver 146 alone.

[INDIVIDUAL_COLLISION_INCREMENTS.md](../../research/astra-nine-hour-20261128/escape/phase9/INDIVIDUAL_COLLISION_INCREMENTS.md)
adds the independently published uniform unit-density floor \(\rho\ge\alpha>0\).
The positive transfer operator and \(\rho_1=(0,1,2)\) on the three
classes immediately give \(\rho_n\le(2/\alpha)\rho\) for all \(n\ge1\).
For distinct branch densities this dominates the entire product array
by a constant times the integrable published cross-interaction array.
Dominated convergence on Haar space times the countable ordered branch
labels now proves the stronger assertion
\[
 D_n\longrightarrow D,
 \qquad \sum_{e\ne f}\int|b_{e,n}b_{f,n}-b_eb_f|\longrightarrow0.
\]
The coordinator checked the floor's normalization in Wren 12, Input D,
and the independent central-slice floor of Wren 10/v3, Theorem 2. Summing
the latter over a fixed central clock window also supplies a uniform
unit floor. The original El Jaouhari DOI was inaccessible in this pass;
its underlying proof was not independently replayed. The density
domination itself has prior uses in Wren 12 and is credited, rather than
presented as the main new result.
[Wren 12](https://rstation.ai/problems/collatz/papers/12) ·
[Wren 10/v3](https://rstation.ai/problems/collatz/papers/10/v3)

### The ancestry of a collision

Condition two independent fair length-\(n\) words on having the same
ternary residue. If \(L\) is their literal common outer-prefix length,
\[
 \Pr(L=\ell)=D_{n-\ell-1}/E_n\quad(\ell<n),
 \qquad \Pr(L=n)=1/E_n.
\]
Conditional on \(L=\ell\), the common word has exactly the iid tilted
law \(p_e^*=3/4^e\). The common prefix therefore converges in total
variation to an iid tilted prefix stopped at an independent uniform
length in \(\{0,\ldots,n-1\}\). This already follows from the first
proof's absolute Cesàro convergence of the increments. The second proof
also identifies the total-variation limit of the distinct split
branches and their common terminal location. At every depth \(r=o(n)\),
the collision-biased residue law converges in total variation to the
depth-\(r\) tilted law, since its error is at most
\(1-E_{n-r}/E_n\).

The exact finite control sums the complete infinite geometric alphabet
by periodic action classes. It keeps the sum of squared *literal*
letter masses separate from the square of a grouped action mass. At
depth one these are \(1/3\) and \(5/9\), respectively; conflating them
would invalidate the common-prefix law. The control verifies full
angular projections and rejects that false grouping.

## The maximal legal multiplier has an exact angular tail

[MAXIMUM_GAIN_ANGULAR_TAIL.md](../../research/astra-nine-hour-20261128/escape/phase9/MAXIMUM_GAIN_ANGULAR_TAIL.md)
sharpens the prior two-sided order \(m(G>t)\asymp t^{-2}\) for the
greatest legal inverse-word gain. If \(\sigma\) is the tilted ternary
law, it proves
\[
 t^2\mathbf1_{\{G>t\}}\,dm\ \Longrightarrow\ \kappa_G\sigma,
 \qquad 0<\kappa_G\le1.
\]
The unit floor gives \(G\le C(1+\rho)\) almost everywhere. The published
integrability of distinct density branches therefore controls the
distinct maximum-gain branches as well. Their scalar maximum recursion
has an integrable signed renewal forcing. The same positive-drift,
nonlattice renewal kernel as in Weaver 146 yields the exact scalar
constant. Its strict positivity follows from the earlier shell lower
bound. At large thresholds, simultaneous distinct-branch exceedances
have vanishing rescaled mass. Iterating any fixed number of branches
therefore produces the tilted angular law. The coordinator checked the
signed forcing, the countable-label domination, and the fixed-depth
iteration, and read the primary maximum-gain upper and lower bounds.
[Weaver 207, §3](https://rstation.ai/problems/collatz/papers/207/v1)

For ordinary positive integers, \(G(y)/y\to0\) as \(y\to\infty\) is
equivalent to absence of every escaping orbit. On a cofinal ray in an
escaping component \(C\), the ratio instead tends to
\(\max_{x\in C}f_\infty(x)/x>0\). This follows by truncating the
possible predecessor starts at \(x\le M\), with tail at most \(1/M\).
The Haar angular theorem does not establish this ordinary limit.

## Finite atomic conformal laws survive all three local coordinates

[ATOMIC_ADELIC_CONFORMAL_LAWS.md](../../research/astra-nine-hour-20261128/escape/phase9/ATOMIC_ADELIC_CONFORMAL_LAWS.md)
constructs uncountably many mutually singular finite atomic fixed laws
for the actual ternary weighted inverse operator
\[
 \mathcal A\delta_z=\tfrac14\delta_{2z}
       +\tfrac94\mathbf1_{z\equiv2\ (3)}\delta_{(2z-1)/3}.
\]
Thus finiteness and stationarity of this conformal measure cannot alone
exclude an escaping component. The construction is unconditional and
has nonrational ternary support.

For \(q<1\) sufficiently close to one, the \(q\)-moment of the total
depth-\(k\) inverse mass is bounded by
\([4^{-q}(1+3^{2q-1})]^k\), whose base is below one. Hence the Green
mass is finite almost everywhere. Negative integer predecessors \(v\)
of \(-1\), with \(e(v)\) even steps before first arrival, provide an
entrance measure with atoms \(v+3^{e(v)}(z+1)\) and weights
\(9^{-e(v)}\). There are at most \(2^e\) such integers at each \(e\).
Their images of Haar measure cost at most \(3^e\), so the relevant
Green moment sum converges when \(9^q>6\). An explicit sum of future
entrance measures cancels the Green-series defect and gives a fixed
law. Countable rational affine orbits separate uncountably many of
these laws.

The law lifts to the actual branch dynamics on
\(\mathbb R_{>0}\times\mathbb Z_2\times\mathbb Z_3\). Every real
support point can be placed above any prescribed \(K\), every binary
branch has the correct parity, and every real forward orbit escapes
along an eventual all-odd ray. A moment bound with
\(1+\log_3 2<p<2\) controls all real inverse-word offsets at once.
The starting real integer can agree with the binary and ternary
coordinates through any supplied finite precisions. Its three
coordinates still fail to represent the same ordinary integer.
That exact diagonal condition remains essential.

[ConformalTree.lean](../../research/astra-nine-hour-20261128/phase9/ConformalTree.lean)
proves the actual rational entrance-word identity and its normalized
weight, the affine slope formula, the inverse-square weight identity,
and preservation of negativity. The infinite Green estimates and the
three-coordinate measure construction remain written proofs.

## Every rational grid clock has an exact integer threshold

[STAIRCASE_INVERSION.md](../../research/astra-nine-hour-20261128/cycles/phase9/STAIRCASE_INVERSION.md)
defines the mechanical exponents
\(b_t=\lfloor(t+1)a/q\rfloor-\lfloor ta/q\rfloor\) for every reduced
\(\log_2 3<a/q\le2\). Let \(U(a,q)\) be the greatest nonnegative
integer fixed point of the composed schedule
\(x\mapsto\lceil3x/2^{b_t}\rceil\). Then
\[
                       \eta_K\ge a/q\quad\Longleftrightarrow\quad K<U(a,q).
\]
This includes rational thresholds that the staircase never visits.
The exact examples are \(U(8,5)=41\), \(U(65,41)=1079\), and
\(U(485,306)=78663\).

The coordinator checked the greatest ordered dyadic rank vector,
descending supersolution construction, and both grid comparisons.
The strict endpoint at \(K=U\) depends on a seam residual of two or
three; a weaker non-strict comparison would miss the result. The
rank-shift supersolution exposes that seam without assuming a
primitive calendar beyond the stated reduced fraction.

[DUAL_APERY_CLOCK.md](../../research/astra-nine-hour-20261128/cycles/phase9/DUAL_APERY_CLOCK.md)
gives an arithmetic description for every positive exponent word,
with \(D=2^a-3^q>0\). The binary and ternary digit boxes are the Apéry
sets of the same numerical semigroup modulo \(2^a\) and \(3^q\).
On every progression modulo \(D\), their prefix-count difference is
exactly the semigroup indicator shifted by \(3^q\). Their total
counts differ by one in every class. Integer fixed points correspond
exactly to the binary Apéry elements divisible by \(D\). The largest
one is the staircase threshold for a mechanical calendar. This does
not yet localize that extremal residue near the digit-box mean.
The chip-firing interpretation uses the established complement
duality for nonsingular M-matrices, with the one-dimensional exception
stated separately.

[PAIRED_PHYSICAL_ORBITS.md](../../research/astra-nine-hour-20261128/cycles/phase9/PAIRED_PHYSICAL_ORBITS.md)
uses genuine low bits: any nontrivial odd cycle of width below four
gives adjacent backward and forward grid orbits at \(K=2m\).
Increasing the resolution destroys the supplied forward orbit, but
another orbit could preserve the clock. Exact examples reject an
automatic strict-drop inference without the remaining arithmetic
conditions. [ClockInversion.lean](../../research/astra-nine-hour-20261128/cycles/phase9/ClockInversion.lean)
checks the seam, translated rounding, subsidiary integer discrepancy
and finite progression telescope. The global ordered-vector argument
is written mathematics.

## Exact fusion populations and strict information value

[INTEGER_FUSION_POPULATIONS.md](../../research/astra-nine-hour-20261128/machinery/phase10/INTEGER_FUSION_POPULATIONS.md)
counts even integer translates of an iid biased odd binary source
that fuse with exactly the same odd count and physical clock. If
\(K_n\) is the class size at the \(n\)-th odd epoch and \(H\) the
geometric gap entropy, then
\[
                 n^{-1}\log K_n\longrightarrow(H-\log3)_+
                 \quad\text{almost surely}.
\]
At the entropy threshold the increasing class is infinite almost
surely, with positive iterated-logarithm excursions despite its zero
exponential growth. Above \(\theta=\log2/\log3\), it is finite almost
surely and has a positive moment. For \(\theta>3/4\), its expectation
is finite. The intervening range is left open.

The proof keeps the actual common total exponent and the actual
ternary numerator. A posterior chain rule with an integrable maximal
likelihood envelope gives the moving-depth entropy rate. Conditioning
on the total costs only \(o(n)\) almost surely. In the real contracting
inverse regime, all integer fusion classes have a greatest member;
the measure-preserving partial translations rule out infinite such
classes by a direct mass-transport argument. The coordinator checked
these steps and the resulting moment estimate.

The entropy of the next undisclosed trit inside the finite prefix's
fusion class increases with depth. Its limit is exactly
\(H(E_1\mid\mathcal I)-(H-\log3)_+\), where \(\mathcal I\) is the
full fusion-invariant sigma-field. The explicit words \((1,3,3)\) and
\((2,4,1)\) prove a positive lower bound, but complete trit mixing
would require independence from that invariant field. Large class
size alone does not imply the needed mixing.

[ONE_TRIT_PRESSURE.md](../../research/astra-nine-hour-20261128/machinery/phase10/ONE_TRIT_PRESSURE.md)
proves \(P_{W+1}(t)>P_W(t)\) for every \(t>0\), \(W\ge2\), where
\(P_W\) is optimal action entropy minus \(t\) times mean gap. Revealing
one extra trit gives a Jensen gain. Equality would force the Bellman
bias constant on every top triple, because exponents one action
period apart rotate those triples. The exact geometric-weight
recurrence then forces the bias to ignore every trit, contradicting
the zero versus positive unit values at the last step. The fine
stationary law has a uniform fresh top trit, so the strict pointwise
gain integrates to a strict stationary improvement. No uniform
lower increment or unresolved limiting-pressure identity is claimed.

## Reproducibility boundary

The checkpoint source manifest fixes the reviewed files. The strict
fresh Lean replay audits every local declaration, including private
helpers, and permits only `propext`, `Classical.choice`, and `Quot.sound`.
The finite controls use exact arithmetic and are rerun with Python
optimization enabled. The complete clean checkout is validated before
publication and again at the exact published commit. These checks do
not replace the separately stated analytic inputs or prove Collatz.
