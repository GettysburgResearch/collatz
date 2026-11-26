# Unconventional Collatz research: exact gauges, rational-cycle stress tests, and physical operators

**Collatz remains OPEN.** This is a three-hour research continuation of PR201,
starting from `94ce06ccbd312ccd0ce4450b567cc514a2f0b54a`. Three GPT-6.2 Astra
lanes developed different attacks and then reconstructed one another's arguments.
The coordinator checked the main interfaces and executed the finite formal and
computational packet. These are proposed written research results with scoped
reviews, not a complete formal proof of Collatz or an exhaustive priority claim.

Throughout, the native shortcut map is

\[
T$n$=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Odd-step clocks, native clocks, rational denominator conditions, and actual
ordinary sources remain separate in each proof.

## 1. The two universal obligations remain visible in Lean

[FinalProposal.lean](FinalProposal.lean) defines the ordinary conjecture using
the actual natural-number map. Its checked conclusion is

```lean
theorem exact_final_obligations : Collatz ↔ NoEscape ∧ CycleUnique
```

`NoEscape` says that some two native states repeat on the orbit of each fixed
positive integer. `CycleUnique` says that each actual positive periodic point
reaches 1. **Neither proposition has been proved here.** The theorem explicitly
retains them as hypotheses in the forward proof of convergence. They are
definitions, not declared axioms or concealed assumptions in a theorem named
as a solution.

The operator route identifies a concrete no-escape target. At an ordinary
terminal $y$, let $B$y$$ be the greatest principal slope $3^p/2^k$ over
all genuine incoming paths. The empty path is included. Then

\[
 B$y$/y\longrightarrow0\quad(y\to\infty,\ y\in\mathbb N)
 \quad\Longleftrightarrow\quad\text{no ordinary escaping component}.
\]

There is also a finite version with an exact limit. For $s>1$, send each
source $x<X$ to its first exit $y\ge X$, retaining the weight
$(C_{\tau}(x)/y)^s$, where $C_{\tau}$ is its true principal multiplier.
Erase a source if it repeats before exiting. This is a terminating finite
computation. The decreasingly sorted exit weights converge in $\ell^1$ to
one positive mass per escaping ordinary component. Their sum, augmented by
$\sum_{x\ge X}x^{-s}$, decreases to the total escape mass. Proving that this
limit vanishes would establish `NoEscape`. The finite calculations do not
prove that vanishing. [Physical exit gates](operator/EXIT_GATES.md)

The cycle route retains the entire denominator: a word of length $n$, grade
$p$, and carry $A_w$ gives the rational fixed point
$A_w/(2^n-3^p)$. An ordinary positive cycle requires
$2^n-3^p\mid A_w$. The new estimates do not establish this exclusion.

## 2. An exact critical Hausdorff threshold

Put $\alpha=\log_2 3$,

\[
H=\alpha\log\alpha-(\alpha-1)\log(\alpha-1),\qquad
\theta=H/\log3=H_2(\log_3 2)=0.949955527\ldots.
\]

The full backward critical tree consists of positive gaps $e_j$, with
$S_j=e_1+\cdots+e_j<\alpha j$ at every positive depth. Its ternary image is

\[
\mathcal R=\left\{\sum_{j\ge1}3^{j-1}2^{-S_j}\right\}\subset\mathbb Z_3.
\]

Let $u=1-1/\alpha$, $h=-\log u$, $\sigma^2=\alpha(\alpha-1)$, and

\[
K_* =\frac{(81\pi^2\sigma^2 h^2/8)^{1/3}}{(\log3)^{1/3}}
     =4.375844909866716\ldots.
\]

For $g_K(r)=r^\theta\exp[K(\log(1/r))^{1/3}]$, the proposed, independently
reviewed written result is

\[
\mathcal H^{g_K}(\mathcal R)=
\begin{cases}0&K<K_*,\\\infty&K\ge K_* .\end{cases}
\]

The strict sides follow from geometric tilting, Brownian interval survival,
and a carry-overlap bound that preserves the sharp constant. The equality
case uses a slowly varying strip and the KMT strong approximation. It is a
later theorem with its own source and review pin; the earlier strict-side
proof is preserved. A further logarithmic refinement has its own scope.

[Elementary proof](renewal/GAUGE.md) · [Exact constant](renewal/SHARP_GAUGE.md)
· [Equality case](renewal/CRITICAL_GAUGE_ENDPOINT.md)
· [Strict-side review](operator/REVIEW_SHARP_GAUGE.md)
· [Endpoint review](operator/REVIEW_CRITICAL_ENDPOINT.md)

The related unrestricted incoming-slope exceptional set has a different
gauge law. Its dimension is also $\theta$, but for an eventually
nondecreasing doubling function $\psi$, its gauge
$g(3^{-n})=3^{-\theta n}\psi$n$$ has zero or infinite measure according
as $\sum_{\ell}\psi(4^\ell)/2^\ell$ converges or diverges. In particular
the square-root logarithmic correction already has infinite measure.
This set contains no positive ordinary integer. Its geometry is an exact
description of an auxiliary ternary exceptional set, not an escape proof.

[Unrestricted set](operator/UNRESTRICTED_GAUGE.md)
· [Integral test](renewal/INCOMING_GAUGE_TEST.md)
· [Independent review](operator/REVIEW_INCOMING_GAUGE.md)

## 3. Record laws without a bounded-gap assumption

For the first-ladder counts $N_m$ and bounded-alphabet dimension $d_J$,
the prior first-order estimate sharpens to

\[
(\theta-d_J)J\log3=
\tfrac12\log J+\log\log J+\log(h\sigma\sqrt{\pi/2})+o(1).
\]

This follows from an exact first-maximum factorization, a local
irrational-rotation coefficient profile, and a moving-window average.
No independent-randomness law is assigned to an actual orbit.

For actual strict coefficient records, occupation normalized by elapsed
odd time is tight even with unbounded record gaps. Its atomic ternary part
can only lie on negative signed rational periodic record phases. There the
dyadic coordinate is the same rational and the real logarithmic phase is
Haar distributed. The nonatomic part remains possible. Positive-density
record flows have an explicitly smaller-dimensional support described by
the pressure spectrum; zero-density record sequences are not excluded.

A further actual-orbit theorem rules out **all-rational diagonal cluster
sets**, without bounded record gaps or a finite list of possible limits.
If every dyadic record limit were a signed periodic point with a finite
coefficient upcrossing, compactness would bound record clocks. The native
parity omega subshift would then consist entirely of purely periodic
tails; compact invertibility forces it to be finite, contradicting an
escaping ordinary source. PR210's rational critical-trace classification
turns this into the paired-coordinate exclusion. Unequal rational pairs
and irrational limits remain possible.

The fixed-source periodic-window theorem also accumulates across record
blocks: if native time is comparable to the sum of logarithmic record
heights, at least $\log_3 2$ of the bits must lie outside any supplied fixed
periodic library with a fixed number of exceptional intervals per record.
This excludes the earlier two-run quadratic-growth symbolic control as
an ordinary positive trajectory. It does not assert low complexity for an
actual hypothetical escape.

Combining this with exact divisibility during repetitions excludes a
larger family: two-piece first-ladder words cannot form an escaping
ordinary itinerary with eventually nondecreasing lengths. In arbitrary
order, when lengths tend to infinity, an escaping realization would have
to revisit infinitely many distinct lengths on at least ten separated
runs. The theorem uses the actual fixed source at every repetition;
it is not a claim about all unrestricted record sequences.

[Three-term law](renewal/PRESSURE.md) · [Actual record flow](renewal/RECORD_FLOW.md)
· [Density spectrum](renewal/DENSITY_SPECTRUM.md)
· [Opposite-end precision](renewal/BRIDGE.md)
· [Long gaps and denominators](renewal/LONG_GAPS.md)
· [Independent pressure review](adelic/REVIEW_RENEWAL_PRESSURE.md)
· [Rational diagonal exclusion](renewal/RATIONAL_DIAGONAL.md)
· [Independent diagonal review](operator/REVIEW_RATIONAL_DIAGONAL.md)
· [Repeated template cost](renewal/RECORD_TEMPLATE_COST.md)
· [Repeated-word harmonic cost](renewal/MONOTONE_RECORDS.md)
· [Independent template review](adelic/REVIEW_MONOTONE_RECORDS.md)

## 4. Rational cycles surviving strong ordinary-looking tests

For every fixed $0<a<1/2$, the coherent-switch construction supplies
primitive positive rational cycles with native least periods $n\to\infty$
and constants $\eta,\kappa>0$ such that

\[
1<d,\qquad \log_2 d\ll n^{1-\eta},\qquad
\min_{i\ne j}|x_i-x_j|\gg n^\kappa,
\]

while all states tend to infinity and the reduced denominator has no prime
factor at most $n^a$, or in any additionally prescribed finite prime set.
A diagonal construction reaches the cutoff
$\sqrt n/(\log(2n))^{3/2+\varepsilon}$, with $\log d=o$n$$ and
pairwise separation tending to infinity. These are rational cycles with
**nontrivial** denominators throughout.

The construction combines two periodic forcing tracks, long coherent
equal-grade motifs, a sparse-character Fourier patch, the actual smooth
part of the full determinant, and a positive averaged real system for
checking every physical offset. It repairs a real limitation of the earlier
short switches: synchronized $01/10$ choices force a pair of phases less
than $1/3$ apart. The restricted integer cycle obstruction is formalized
in [AlignedCycles.lean](AlignedCycles.lean).

The exact high-minimum denominator-weighted pressure is
$(\theta-s)_+$, including at genuine least periods, also when every
pairwise gap is required to exceed any fixed bound. Consequently neither
these exponential pressures nor the growing-prime sieve isolates the
denominator-one row.

[Cycle index and denominator bounds](adelic/CYCLE_INDEX.md)
· [Shorter congruence patch](renewal/CYCLE_SIEVE_REVIEW.md)
· [Primitive forcing](adelic/PRIMITIVE_PRESSURE.md)
· [Coherent construction](adelic/COHERENT_SWITCHES.md)
· [Independent review](operator/REVIEW_COHERENT_SWITCHES.md)
· [Fixed-source topology](adelic/FIXED_SOURCE_TOPOLOGY.md)

The largest executed coherent control checks all **865,445 native steps**,
closure, least period, and outward rational intervals for all phases.
Its minimum phase has floor 51,552,628; its certified minimum pairwise gap
is at least 2.752799; its reduced denominator has 271,974 bits. The tested
prime set is exactly **{5,71}**, and the entire $5^3\cdot71=8875$ factor
of its determinant is cancelled. This finite fixture does not itself
verify the asymptotic growing-prime statement.

## 5. What the physical operators distinguish

The ordinary graph consists of a branching 3-unit core and attached
half-lines. The core has a uniform Cheeger gap; the full graph is amenable.
An exact Schur complement gives a $t^{-3/2}$ core heat law. All ordinary
components nevertheless share the same essential spectrum for the bounded
local operators under consideration. A local spectral distinction cannot
separate an unknown component from the known basin.

A different weighted composition operator has exact unit-circle
eigenvectors precisely on escaping components. Every point of that circle
already belongs to continuous spectrum on the known component, with explicit
good-basin approximate eigenvectors. Global norm lower bounds therefore
cannot settle its remaining exact-kernel question.

Arithmetic resistance makes each component's end completion compact and
gives a trace-class positive inverse in a suitable weighted space. The
physical maximal form keeps components separate. Wiring all ends together
would impose a one-dimensional kernel by definition; it is not evidence
of convergence. Dense mixed-adic components also support exact atomic
conformal measures and eigenvectors, demonstrating why the ordinary
diagonal must remain in a proposed closing argument.
Even a globally positive, proper real height obeying every affine
translation can coexist with those mixed components. Their rational
heights then acquire unbounded dyadic denominators. An exact infinite
integrality condition is still required.

[Core heat](operator/CORE_HEAT.md) · [Local spectrum](operator/LOCAL_SPECTRUM.md)
· [Impedance and height](operator/IMPEDANCE.md) · [Weighted boundaries](operator/WEIGHTED_BOUNDARY.md)
· [Escape operator](operator/ESCAPE_SHIFT.md) · [Mixed descent obstruction](operator/HYBRID_DESCENT.md)
· [Ordinary diagonal criterion](operator/TERNARY_TRANSFER.md)
· [Mixed exact eigenstates](operator/MIXED_EIGENSTATES.md)
· [Positive real realization](operator/POSITIVE_REALIZATION.md)

## Verification, prior work, and scope

The first complete new replay compiled **53 declarations in ten Lean files**
from their exact checked-in bytes, with warnings treated as errors. All
queried axioms were among `propext`, `Classical.choice`, and `Quot.sound`.
Eight finite-control programs matched their complete published JSON in
normal and optimized Python, with identical output bytes; the eighth has
a separate supplementary receipt. This formalizes
selected finite arithmetic, order, and semantic interfaces, not the whole
analytic packet. [Exact replay and scope](../../reports/unconventional-20261126/README.md)
lists every file, source hash, and printed theorem.

The broad intake covered metadata for the latest thirty PRs and selected
current packets; it was not a line-by-line audit of the whole repository.
PR193 supplies an important predecessor for the source-retaining Subspace
argument. The independently reconstructed occupation bounds here are weaker
than the claims of rStation paper 28/v3, and the superlogarithmic dictionary
corollary is weaker than paper 15/v2. Those sources are credited rather than
treated as new results of this pass. The operator's .84 extension separately
invokes the published Krasikov–Lagarias computation. No external formal
release was rebuilt in this pass.

[Coordinator review and exact limits](../../reports/unconventional-20261126/ROOT_REVIEW.md)
· [Source intake](../../reports/unconventional-20261126/SOURCE_INTAKE.json)
· [Scoped correction to the preceding packet](../../reports/unconventional-20261126/ERRATUM.md)

The remaining mathematical task is a restriction on **one fixed ordinary
source for its entire future**, together with exclusion of denominator-one
positive cycles. Finite local realizations, exact auxiliary fractal laws,
and the new rational cycles do not supply those two conclusions.
