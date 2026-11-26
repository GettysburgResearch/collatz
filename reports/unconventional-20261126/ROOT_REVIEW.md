# Root review of the first-wave proof packet

## Identity and review scope

Baseline: PR200 at `8e6add443b13acbcfd553676898c120183f07377`.
The exact new source byte identities and any integration edits are in
[FIRST_WAVE_SOURCE_MAP.json](FIRST_WAVE_SOURCE_MAP.json). Paths in that map
are relative to the repository. This review covers those bytes, not arbitrary
later changes or all claims in neighboring PRs.

The root independently reconstructed the arguments listed below. The three
authoring workers also exchanged separate reviews, preserved under
[reviews](reviews/). Their reports retain their original hashes and paths.
Where an author later corrected a bibliography or added audit commands,
the root checked the delta. Review agreement is not a substitute for the
reconstruction described here. These are project-internal written-proof
verdicts; no external acceptance or historical priority is asserted.

The intake froze the recent working heads in [INTAKE_SNAPSHOT.json](INTAKE_SNAPSHOT.json).
The broad comparison included the main research map and scoped errata, then
the relevant work on PRs 192, 193, 195, 197, 200, 201, 206 and 210. Reviewing
selected proofs and current PR descriptions does not certify every file on
those branches. No claim is made that the repository has become solved.

## Arithmetic and actual trajectories

**VERIFIED, M1:** the effective simultaneous mechanical approximation bound.
I checked the bilateral affine normalization, the strict terminal dyadic bit,
integrality and positivity of the recovered past, uniform truncation at
$(\log X)^2$, and exclusion of repeated states by the two-logarithm lower
bound. Equal mechanical words occupy one ordinary phase interval, including
the cut at zero; the interval width and the *even* difference of the two odd
terminals give the claimed real spacing and logarithmic saving. Wu–Wang's
stated published estimate supplies any exponent greater than 4.1163051;
4.117 is used, not 3.117. Constants are effective but not numerically evaluated.

**SOURCE-QUALIFIED, M2:** I checked the implication from Weaver Paper 140's
uniform theorem, including both boundary conventions, to the claimed
two-place bound at the oldest actual integer state. I read the primary
statement but did not independently reconstruct its complete preceding
analytic dependency chain. The new transport is valid conditional on that
input. It does not multiply two unrelated one-place estimates.

**VERIFIED, R1:** the primitive congruence construction and full mechanical
denominator. The upper convergent and its difference from the preceding
lower convergent form an integer basis. The two chosen coefficients are
coprime and satisfy the prescribed clock congruences. The lcm estimate,
determinant lower bound on the positive error, and the two neighboring Farey
intervals justify both size estimates and both local agreements. I checked
the rotation argument that the *entire* denominator is reduced, rather than
only selected factors. The depth-192 inverse screen remains qualified to its
upstream theorem and is not relabeled as an all-depth minimum result.

**VERIFIED, T1–T2:** the source-uniform joint clock and bounded-clock rational
finiteness. The two positive truncated sums have exactly the asserted
ternary denominators. Equality forces matching powers of three, then odd
terminal parity forces matching powers of two and a literal common state.
Otherwise their cleared integer difference pays the next union date. The
number of union intervals is at most $2K-1$. For the periodic corollary the
selected leg's *entire* first-$K$ gap word has bounded sum; finitely many
such words and repeat locations give finite sources, not only denominators.

**VERIFIED, J1:** the paired-cycle construction, arbitrary finite-prime
avoidance and concentration at one reduced denominator. I independently
computed the three affine intertwinings, checked physical parity through
the odd-denominator ring, and reconstructed the unique-marker and prefix
code argument for distinct primitive cycles. The raw denominator congruence
passes to every reduced divisor. The divisor-count pigeonhole and the
bounded interval for the marked rational force the selected reduced
denominator to grow. Induction excludes previously selected primes without
requiring uniformity in a growing modulus.

I additionally checked the later reciprocal identity and the strict
comparisons proving the marked phases are the unique odd cycle minima.
The four finite least-model claims were fully replayed by the root. Their
checker exhausts every required odd numerator, treats common factors by an
exact invariant, and resolves all remaining deterministic fates by entering
a recorded fate or closing a distinct cycle. A cap exit fails the run.
Stripping powers of two and invariance of the reduced denominator justify
the stated all-depth basin inference in the prime-to-six domain. This does
not establish full leastness for the infinite arbitrary-prime family.

**VERIFIED, centered-return Theorems 1–2:** the finite-rank return proof and
uniform mismatch-clock density. I read the complete proof and checked ESS
Theorem 1.1 in its primary statement. The first correction with least
dyadic valuation must share the nondegenerate block with both endpoints;
real domination prevents the initial term from cancelling without the
terminal. The actual high division exponent is controlled using the true
terminal state, not a bounded-exponent assumption. At the first small state
the unpaired final low term is necessary and is present. Matched prehistory
is bounded by ternary divisibility; an eventual matched future forces zero
displacement and cannot support unbounded qualifying nonzero endpoints.
The uniform result uses a cardinality bound for possible first-mismatch
states, not a uniform height bound for arbitrary groups. Both excluded
cases—zero displacement and zero mismatches—are essential.

**VERIFIED, shifted-smooth Theorem 3 and Corollary 4:** I checked Yu's original
Theorem 1 and equations (1.2), (1.5), (1.8), (1.9) on printed pages 337–339.
The fixed field $\mathbb Q(\zeta_3)$ meets the dyadic field hypothesis.
The variable base contributes only its logarithmic height; the remaining
bases are fixed primes. Equal and unequal dyadic valuations and $V=0$
are handled. I reconstructed both exact coefficient updates, including the
last reset's additional factor of two, and the iterated height estimate for
all intermediate states. The first-descent bound remains conditional on a
first descent existing. No practical numerical cutoff follows from this
asymptotic theorem.

**VERIFIED, one-reset classification:** the exponential classification and
the actual-path bridge were inspected and then rebuilt. Arbitrary lengths
before and after the reset are quantified. The only physical cases are the
two stated paths. This is not a classification of paths with arbitrarily
many resets.

## Operator proofs

**VERIFIED, O1–O2 and finite computability.** I reconstructed the clock lift
which unrolls cycles before transplanting finite norm witnesses. Equality
of affine germs implies equality of both value and lifted clock; residue
congruences preserve every legal branch and periodic coefficient. Monks's
2006 arithmetic-progression theorem supplies arbitrarily high copies in
each ordinary component. Disjoint copies give essential norm equality;
faithful C* representations then give spectral permanence. The assertion
is about the specified generated algebra, not all finite-propagation
operators. The component-label distance proof also survives arbitrary
compact perturbations.

For effective spectral computation I checked the forward empirical
partition, Hellinger/commutator bound, degree-three ball count and the
finite affine-type enumeration. Local matrices retain *all* output rows.
Lower norms give a spectral-distance algorithm for selfadjoint operators;
general nonnormal spectral computability is not claimed.

**VERIFIED, O3–O4.** The long divisible dyadic chains give the circle of
characters. Covariance forces every periodic diagonal character to select
the zero residue. Under nonzero height weighting, the odd diagonal's
isolated eigenvalues recover coordinate projections; branch paths recover
matrix units within each component. Conversely the weighted branches
differ compactly from constant multiples of the original branches. This
proves the split algebra description without proving the compact ideal
simple. The final Monks citation was corrected to the solo 2006 paper.

**VERIFIED, O5–O7.** The funnels are actual ordinary paths into powers of two.
Their predecessor cones have one residual edge and are disjoint. Finite
anchors remove only finitely many cones, with no convergence assumption
on those anchors. The rooted gap criterion uses the killed root and the
full codomain of the residual where necessary. For local corrections,
the endpoints approach the selected nonsingular limits at 2 and 3. At
other primes the remaining exponent orders are pure powers of distinct
primes, so CRT applies even when those primes divide the initial order
multiplier. Compactness outside the excluded balls gives uniform bounds.
Bounded composition on the entire space is not assumed for arbitrary
weights; the specified closed spans are in the residual's domain.

**VERIFIED, O8.** I checked the carry bound and word injectivity, the
homogeneous operator's disjoint-column estimate, and compactness of the
actual weight correction. Outside the disk a Fredholm operator of index
zero has no eigenvectors by pointwise forward growth, hence is invertible.
Inside, two distinct ordinary inverse arms give adjoint approximate
eigenvectors. For $p=1$ the dual is $\ell^\infty$; disjoint supports give
norm separation, which is the needed contradiction to a finite-dimensional
kernel and closed range. Weak convergence is not incorrectly assumed.
The strong-stability estimate for summable powers is independent of
whether an ordinary component converges.

**VERIFIED, O9.** I read Béhani's exact quotient, coefficient norm, operator
direction, Proposition 2.1, Question 4.1 and Proposition 4.2 in the primary
paper. The inverse slope is $(j+1)/(a+1)$, not its reciprocal. Each word
has the claimed residue count and gives a distinct positive ordinary source
at sufficiently high endpoints. The analytic average therefore yields the
lower bound. The upper table's positivity and all 177,147 actual lifted
inequalities were checked by a separate root implementation, independent
of the search and its maximum-over-lifts implementation. Three corrupted
cases were rejected in normal and optimized Python. The exact radius
remains open. The earlier unweighted Haar average is credited, rather than
presented as a new general method.

**VERIFIED, O10.** The explicit weight is at most $n$, giving holomorphic
coefficient-space elements, and has the correct doubling ratio. The dense
nilpotent approximation works on any ordinary orbit because an odd step
eventually occurs and thereafter every state is a ternary unit. The
contracting right inverse yields mixing and dense periodic vectors. I
checked the bilateral Gaussian series's index shift, square summability,
full support and factor-map mixing. The adjoint equivalence uses the killed
coordinates and separately excludes eigenvalue zero by surjectivity.

## Execution and formal limits

The root rebuilt every project module from fresh output, with the pinned
Lean 4.34.1 and Mathlib checkout. All 70 local declarations, including private
lemmas, passed transitive axiom checks with only the three standard axioms
allowed. The 46 earlier baseline declarations also replayed exactly.

The original two uncompiled candidates remain unchanged. Repaired copies
fix genuine proof/API problems, retain all theorem statements and global
premises, and have a separate identity. Adding the remaining axiom print
requests to the three arithmetic modules did not change a proof body.

All five primary control outputs matched their complete stored JSON in
normal and optimized Python. Five independently authored supplemental
programs were also executed. For three assertion-based supplements, the
integrated copy adds an explicit optimized-mode rejection; the original
and integrated hashes are recorded in [REVIEW_SCRIPT_MAP.json](REVIEW_SCRIPT_MAP.json).

Passing these checks does not prove the operator theory, imported
Diophantine theorems or Collatz in Lean. The new written proofs do not
exclude general ordinary cycles or escaping trajectories. An unrestricted
ordinary merging/descent or trace estimate remains missing.
