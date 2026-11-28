# Three-hour proof pass: the median collision threshold and semiprimes

**Collatz remains unresolved. The pass is active.** The requested interval is November 28, 2026, 08:52:20–11:52:20 UTC. This packet continues PR #214 at `504d29d399efa941a62006d1ea4635385ce6bb5f` and keeps its analytic and formal dependencies explicit.

The goals are to force the actual median synchronous collision probability to its maximal value \(1/8\), and to identify whether the semiprime work in `gfreund123/factoring-in-p` supplies a missing arithmetic step. Arguments, failed routes, source pins and reviews are kept here rather than in long chat updates.

## First result: an unconditional number-theoretic bridge to full convergence

[Semiprime sufficiency](SEMIPRIME_SUFFICIENCY.md) proves a proposed, source-qualified reduction to
\[
\mathcal S=\{pq:p<q\text{ prime},\ \log(pq)<p\le(\log(pq))^2\}.
\]
Every positive-density Collatz component union contains \(\gg X/\log X\) such semiprimes through \(X\). With the imported positive-predecessor theorem, convergence on this family, or upper relative density one of convergence within it, is equivalent to full Collatz convergence.

The arithmetic step combines the unconditional Matomäki–Teräväinen short-interval semiprime lower bound with actual pair-fusion cylinders and a Brun–Titchmarsh upper bound in each failing residue. This retains the sparse population's normalization. It does not remove RH from the distinct ordered-prime-product independence theorem in recent Paper 233.

The factors of every member of this sufficient family are already findable in polynomial time by trial division. The outstanding task is a dynamical convergence or descent theorem on the family. Factor recovery itself does not discharge it.

The [certifying representative theorem](SEMIPRIME_REPRESENTATIVES.md) makes the reduction concrete: every positive source has an actual finite merger with a semiprime in a fully integer-testable subfamily. A terminating dovetail supplies both ordinary paths, with no proved uniform runtime bound. Seven finite certificates have been independently replayed edge by edge. Sparse sufficient sets themselves are prior work; the specified semiprime family and its unconditional analytic supply are the content here.

## The collision endpoint and its exact open estimate

[The collision threshold](COLLISION_THRESHOLD.md) proves the full countable-series
deficit bound \(1/8-L\ge b(1-b)/4\), including arbitrary nonperiodic mass.
Eight freshly checked Lean roots give the exact maximal-mass equivalence and
its quantitative approximation. This formalizes the endpoint reduction; it
does not prove the missing lower bound.

The reconstructed [boundary zero-one criterion](collision/DYADIC_BOUNDARY_ZERO_ONE.md)
gives a different sufficient condition: the reciprocal sum of the exact
asynchronous component boundary is finite if and only if Collatz holds,
using the positive-predecessor input. It uses both exact branches and avoids
the Gaussian law. Its dyadic stabilization and irrational-dilation proof are already in Lean Assurance Lab, Paper 212 (November 23); this packet gives an equivalent harmonic-boundary formulation and does not claim a new zero-one theorem. An [explicit construction](collision/SHARP_HALVING_BOUNDARY.md)
shows why exact halving and an \(O(X/\log X)\) boundary count alone cannot close it.

The [single-edge calibration](collision/ONE_EDGE_COLLISION_SPLIT.md) changes only the odd transition at 5. Even a one-unit change preserves the complete limiting Brownian descent, its independence from the new minimum and a bounded minimum-clock error, while strictly lowering the median collision constant. Fifteen new audited Lean roots verify the finite actual-map interface. The limiting comparison is a separate source-qualified written proof. This isolates the exact arithmetic input that a successful one-eighth argument must use.

## Positive transfer from the factoring work

The [aggregate coefficient theorem](factoring/AGGREGATE_PROFILE_TRANSFER.md) imports the general prime-power Cartier algorithm from factoring PR #234. A single constant matrix retains joint odd grade, ternary residue and real carry moments. Selected coefficients can be computed at binary clocks with cost polynomial in the numerical modulus, moment degree and precision. Eight new Lean roots verify the finite carry algebra, enumeration, injectivity and first moment. The primary algorithm and complexity proof remain written.

The [full-window resolvent theorem](factoring/JOINT_RESOLVENT_WINDOW.md) proves that a full positive-integer fibre has compact real support and multiplicity one on its exact source lattice. The entire ordinary window can be approximated, to normalized error epsilon+6/X, using O(log^2((B+1)/epsilon)) accurately specified nonreal resolvent queries. The theorem retains the full conductor and small imaginary heights.

The [conductor and stationary transfer](factoring/CONDUCTOR_AND_STATIONARY_TRANSFER.md) provides a sparse exact determinant, a weighted discrete-log formula for the target numerator, and an exact rounding reduction to a biased joint stationary trace. At odd-bit probability 1/8, the scaled trace differs from the actual integer count by at most 1/6; the stated additional probability precision makes nearest-integer recovery exact. The trace still includes the full cylinder, real window and grade. Its required precision has O(h) bits; evaluating that rare joint event efficiently remains unproved. This is a concrete consumer for further factoring methods, not a completed full-conductor algorithm.

## One stationary path and one critical quantile

The [full stationary collision transfer](factoring/STATIONARY_COLLISION_CONSUMER.md) moves the entire joint grade/endpoint law at once, with total-variation error at most E min(R0,X)/X, uniformly in the observation clock. For the fair stationary seed this is O(log X/X). The exact two-copy test is one intersection of a real interval and compatible ternary residues, and it uses precisely the median synchronous clock. The remaining relative probability estimate is stated without discarding the grade correlation.

The [critical negative-grade theorem](arithmetic/CRITICAL_GRADE_TAIL.md) narrows the sufficient target further. At the median clock, let W be the odd-step count minus half the clock, divided by half its square root. For every fixed z>0, its negative-tail limit is

\[
\Pr(W\le-z)\longrightarrow\sum_C d_C\Phi(-z/r_C),
\qquad r_C=\frac{\log2-\alpha_C\log3}{\log2-\tfrac12\log3}.
\]

The known cycle has r=1; every other positive cycle has r at most approximately 0.421701. Escaping paths contribute zero to each fixed strictly negative tail. One lower bound by Phi(-z), for one z>0, would therefore force the known basin to have density one and, with positive predecessors, prove full Collatz. The corresponding stationary event uses one path, no endpoint label, and relative scale X/2^h instead of the two-copy scale X^2/4^h. **That one-copy lower bound is not proved.** The source-qualified mixture, its explicit deficit and the exact stationary consumer have independent written reviews.

The [latest factoring evaluator audit](factoring/LATEST_FACTORING_EVALUATORS.md) reads PRs 361 and 365 at immutable heads, including the nonlinear Fourier evaluator opened during this pass. Its hypotheses are tested on the actual carry circuit. A coefficient row module loses the requested position, while the natural Boolean Fourier lift has exponentially many nondegenerate critical points and fails the supplied nilpotent-Gram class. These are specific import tests; general compact encodings and approximate trace evaluation remain open.

## Other factoring imports and their arithmetic requirements

The [source audit](factoring/FACTORING_BRIDGE.md) and
[pointwise import audit](factoring/POINTWISE_IMPORT_AUDIT.md) inspect twenty
complete files at immutable factoring PR heads. The reversible sampler in PR 296 is
a real arithmetic coverage theorem, but its positions are not actual
Collatz merger certificates. PR 359's \(1/8\) is a total-variation tolerance
for a factoring-equivalent sampler, unrelated to the Collatz collision endpoint.

The [actual multiplier theorem](factoring/MULTIPLIER_CERTIFICATE_RIGIDITY.md)
proves that a multiplier with a prime factor other than two and three has
at most one genuine source per pair of affine word cells. The full bounded-clock
census is at most \((2h+1)2^h\); the unbounded two-adic Haar merger event is
countable and null. These restrictions are compatible with universal
ordinary convergence. Three Lean roots certify the algebra and its actual-path
interface.

The [high-state spectral obstruction](arithmetic/HIGH_STATE_AND_PROFILE_OBSTRUCTIONS.md)
shows that a doubly stochastic sampler certified by actual Collatz paths of
length at most \(L\), staying above \(M\), has Poincaré gap at most
\(C(\eta+L^2/M)\), where \(\eta\) is the remaining transition weight.
Long-range endpoints alone do not create the required expansion. The same note
rules out global inverse supersolutions comparable to a sublinear power, any eventually increasing positive sublinear supersolution, and any finite nonnegative supersolution tending to infinity at all ordinary units. Balanced certificates have the stronger gap bound C(eta + L^2/M^2).

A separate [finite-residue spectral theorem](factoring/FINITE_AFFINE_GAP.md)
tracks the exponent, denominator and translation budgets of native affine
charts. It gives an explicit vanishing-gap regime even after granting extra
sign operations. The factoring sources' pointwise quaternionic estimate,
ordered-product algorithms and analytic integer-zero method still need a
representation of the full ordered Collatz carry together with its real window.

The [native post-minimum analysis](collision/NATIVE_POSTMINIMUM_NO_RENEWAL.md) locates the missing mass in one exact bit: after the true global minimum, the first two parities are 10 for convergence and 11 for nonconvergence. Five new audited roots check the actual finite arithmetic and the explicit minimum premise. The continuation is deterministic given that minimum; a fresh fair-parity restart cannot supply the missing estimate. The [controller attempt](collision/ACTUAL_ODD_EDGE_CONTROLLER_ATTEMPT.md) separately quantifies the unbounded cost of certifying odd-count-changing affine replacements by genuine mergers.

## The moving-target escape problem

The [escape-density identity](arithmetic/DENSITY_ESCAPE_PROFILE.md) identifies the exact limiting defect of predecessor-density decay: it is the largest escaping component density. The qualitative equivalence with absence of escape is prior work and is credited. A fixed-positive-density doubling-gain estimate would exclude escape, but remains unproved.

The [ordinary harmonic atom](arithmetic/HARMONIC_BOUNDARY_ATOM.md) shows why positivity, exact integer inverse harmonicity and linear spikes alone cannot prove that estimate. It is constructed on the unchanged Collatz graph from integers already known to converge. The actual canonical selection excludes this added atom; Haar integral norms alone cannot detect it.

The [Green-tail defect](arithmetic/ANCHOR_GREEN_TAIL_DEFECT.md) evaluates Weaver's existing joint anchor supersolution: its exact uniform normalized word-tail defect equals the largest positive escaping-component weight, with the orbit-packing input explicit. This identifies why a pointwise-to-uniform dominated-convergence exchange would already exclude escape. The [atomic-anchor obstruction](arithmetic/ATOMIC_ANCHOR_MAJORANT_OBSTRUCTION.md) independently rules out a natural countable signed valuation-pole majorant with a finite denominator-height moment; it leaves non-atomic or critical real-dependent constructions outside scope.

The [critically damped atomic-anchor theorem](arithmetic/CRITICAL_DAMPED_ANCHOR_OBSTRUCTION.md) closes the logarithmic-damping escape route within the stated absolutely first-height-summable atomic class. Ordinary positivity forces a positive stationary atomic measure on dyadic anchors, which strict denominator growth excludes. Five newly audited Lean roots prove the finite rational denominator mechanism; the measure and averaging arguments remain written. Non-atomic joint potentials are outside this theorem.

The [predecessor dependency audit](PREDECESSOR_DEPENDENCY_AUDIT.md) pins and checks the original archives and all assembled source hashes. A compatibility probe did not reach the announced theorem roots; it is explicitly not a fresh verification of that external theorem.

## Work in progress

- `collision/`: direct attack on the \(1/8\) lower bound, exact boundary amplification and the distinction between a positive lower bound and the maximal one.
- `factoring/`: source-level audit of the relevant factoring PRs, their reversible coverage constructions, and whether they can be implemented by actual Collatz mergers.
- `arithmetic/`: independent audit and a separate attack on integer inverse profiles and escape.

The separate PR #216, at `1917b07ae5cc8f5d27c79f34cc43a4bcf25efff8`, already supplies near-quadratic widely separated median-clock first meetings and positive conditional density bounds. Its result does not establish \(1/8\); this pass does not claim those counts as new.

## Checkpoints

| Checkpoint | Scientific content | Evidence |
|---|---|---|
| 1 | Uniform sparse semiprime transfer and the resulting sufficient-family theorem | Original input clauses read; independent reconstruction of the weighted failure bound and all quantifiers; complete repository integrity gate before publication |
| 2 | Full collision-series endpoint, reconstruction of the prior summable-boundary equivalence and sharp halving control; cross-repository factoring audit and actual multiplier obstruction; high-state spectral and inverse-envelope obstructions | 24 new Lean roots across four modules, each freshly compiled and separately audited; exact binary controls through 262,144 in normal and optimized Python; three independent written semiprime audits |
| 3 | Certifying semiprime representatives; single-edge collision split; exact escape-density defect and ordinary harmonic atom; stronger envelope obstructions; priority corrections | 18 additional freshly audited roots (42 total in this pass), independent written reviews and 214 independently replayed certificate edges; original predecessor source intake and explicit incomplete-rebuild status |
| 4 | Actual primary-Cartier import; full-window logarithmic resolvent consumer; sparse conductor determinant and exact stationary rounding; native second-bit defect; Green-tail and atomic-majorant analyses | 23 additional freshly audited roots (65 total across ten modules); 544 exact coefficient checks in normal and optimized Python, independent general-matrix/full-fibre guards, and hash-bound mathematical reviews |
| 5 | Uniform full-law stationary transfer and exact two-copy collision cell; one-copy critical negative-grade quantile sufficient for full convergence; critical atomic-anchor obstruction; newest factoring evaluator audit | Five additional audited rational roots (70 total across eleven modules); 130 joint-law and 650 complete two-copy native comparisons, 545,975 exact cell checks in both Python modes; independent source-qualified reviews |

[Intake pins](INTAKE_PINS.json) record source versions and the exact starting heads. The [checkpoint 1 review](../../reports/astra-collision-factor-bridge-20261128/checkpoint01/REVIEW.md) states the review boundary. Repository integrity and finite Lean kernels do not certify imported analytic inputs or a full Collatz proof.
