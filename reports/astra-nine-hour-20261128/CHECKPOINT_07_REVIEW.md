# Checkpoint 07: exact affine carriers and full critical moment bounds

**The nine-hour pass continues; Collatz remains unresolved.** This checkpoint
contains an exact overlap classification in the positive 2,3 affine group,
a finite transporter decoder, actual counted fusion, a shrinking fourfold
cycle exclusion, and estimates for all bins of genuine correction laws.
The coordinator independently reconstructed the written arguments below
and read the named primary inputs. Phase eight and drafts are excluded.

## Exact affine overlap at and below the entropy ceiling

[CRITICAL_AFFINE_OVERLAPS.md](../../research/astra-nine-hour-20261128/machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md)
classifies every map
\[
 g(z)=2^a3^bz+c,\quad a,b\in\mathbb Z,\quad c\in\mathbb Z[1/6]
\]
against the geometric-gap ternary Syracuse law \(\mu_\theta\), for
\(\theta\ge\theta_*\), where the gap entropy at \(\theta_*\) is \(\log3\).
There is a nonzero common part exactly when \(g=A_uA_v^{-1}\) for finite
positive-gap words. The shared density ratio is constant, and a finite
exact algorithm gives the complete common mass and total variation.
Every nonzero integer translate is singular. The theorem is restricted
to the displayed group; arbitrary rational multipliers are not included.

Leen's entropy formula gives entropy per ternary digit equal to the
smaller of the input gap entropy and \(\log3\). At these parameters the
first-gap conditional entropy decreases to zero. Conditional convergence
for a finite-entropy countable label recovers the first gap almost surely,
and then the whole sequence. Distinct word images of equal length are
mutually singular. The coordinator downloaded the primary TeX and read
the entropy argument, including the entropy increment identity. This
imported analytic theorem remains a written input, separate from Lean.

The ordinary ingredient is finite counted fusion for a nonidentity
odd-preserving map \(G(x)=2^mx+B\), \(m\ge0\). Advance the second arm by
\(m\) steps and steer the canonical state \((k,C)\), representing
\(z,3^kz+C\), to a common odd endpoint. The two arms have equal total odd
counts. Their true inverse words identify distinct equal-depth planted
images after the affine change of variables. Singularity of those images
forces singularity of the original law and its \(G\)-image.

For a general displayed \(g\), normalize sufficiently deep word components
to \(A_u^{-1}gA_v\). The depth clears dyadic denominators. Ternary
integrality either excludes the component or gives the odd-preserving map
just handled. An identity normalization is exactly a matching word pair.
Countable component expansions give the full decomposition. The shared
target-oriented density ratio is
\((1-\theta)^a((1-\theta)/\theta)^b\).
The coordinator checked both orientation changes, offset parity, and
depth alignment.

### Finite membership and exact overlap mass

Strip common last letters from a matching pair. For remaining words
\(u[e]\), \(v[f]\) with \(e\ne f\), their last-letter offsets cancel.
Every nonempty word offset has exact dyadic valuation minus its gap sum.
Writing \(r=-v_2(c)\), the shorter prefixes satisfy
\[
                     S_u\le\max(0,r),\qquad S_v\le\max(0,r+a).
\]
This is a finite search box. Pure-word cases and zero offset are handled
separately. The coordinator formalized the valuation, cancellation,
finite box and freeness of the rational word maps in
[AffineTransporter.lean](../../research/astra-nine-hour-20261128/phase7/AffineTransporter.lean);
the [interface note](../../research/astra-nine-hour-20261128/phase7/FINITE_AFFINE_TRANSPORTER.md)
states its scope.

Reduced target words are prefix-free: a prefix relation would, by word
freeness, give the same suffix relation between their source words,
contradicting reduction. Summing the remaining last gaps thus gives a
finite exact mass formula without inclusion-exclusion. Controls compare
the decoder with 4,096 constructed word pairs and a negative finite
census. The entropy threshold is sharp: below it some first-letter images
overlap, yielding an overlap for a nontrivial iterate of \(4z+1\) outside
the transporter family.

### Steering priority, growing jitter, and posterior losses

[DETERMINISTIC_COUNTED_FUSION.md](../../research/astra-nine-hour-20261128/machinery/phase7/DETERMINISTIC_COUNTED_FUSION.md)
credits lean_assurance_lab's Paper 212 for qualitative canonical steering,
including positive-level descent and two-step zero-level contraction.
The coordinator found and read this prior proof during review. The present
note reconstructs the positive integer cylinder lift and extracts the
translated-pair clock bound \(6+7\log(2+3d)\). Its Lean theorem is an actual
orbit statement: at every even displacement there is a positive progression
of positive odd sources with equal endpoints, equal odd counts and a common
odd terminal value. Signed positive-level steering and logarithmic costs
remain written proofs.

[GROWING_INTEGER_JITTER.md](../../research/astra-nine-hour-20261128/machinery/phase7/GROWING_INTEGER_JITTER.md)
makes the witnesses quantitative. If \(d_W=H(E\mid Z\bmod3^W)\) and
\(J\) is uniform on \(\{0,\ldots,D-1\}\), an explicit \(\eta>0\) gives
\[
 D\le d_W^{-\eta}\quad\Longrightarrow\quad
              H(J\mid Z+2J\bmod3^W)=o(1).
\]
Condition on two equal-probability fusion words to bound the overlap of
two translates, then sum posterior errors over the labels. The coordinator
checked the conditioning factors and common-slope resolution shift.
The statement recovers a growing label set, but gives no lower bound for
an arbitrary Haar-cylinder mass.

[POSTERIOR_EDGE_LOSS.md](../../research/astra-nine-hour-20261128/machinery/phase7/POSTERIOR_EDGE_LOSS.md)
expresses critical Bellman edge slack as posterior surprise plus reverse
conditional relative entropy. Uniform ellipticity bounds the last-trit
span of this particular logarithmic-density potential, and its projected
source-average loss tends to zero. That source is not stationary for the
rolling controller, and the potential's gain is the entropy ceiling rather
than the finite-window optimum. Neither distinction is dropped; the missing
uniform span bound for optimal Bellman potentials is not claimed.

## A fourfold margin shrinking with the cycle period

[MOVING_FOURFOLD_BOUNDARY.md](../../research/astra-nine-hour-20261128/cycles/phase7/MOVING_FOURFOLD_BOUNDARY.md)
proves that, for every fixed \(C>0\), only finitely many primitive positive
cycles of odd period \(p\), minimum \(m\), and maximum \(X\) satisfy
\[
                         X/m\le4-Cp^{-1/25}.
\]
The input remains Chudnovsky's October theorem
\(\mu(\log_2 3)\le3\), with the independent replay boundary recorded in
checkpoint six. There is no effective finite-period cutoff. A hypothetical
infinite family below four must approach four faster than this margin.

A convergent-denominator argument first counts phases in shrinking angular
arcs of length \(\ell\asymp p^{-\sigma}\). The first denominator above
\(16/\ell\) satisfies \(q\ll\ell^{-2-\epsilon}\). Actual rotation errors
\(O(q/m)\) are smaller than the arc and \(q=o(p)\). Distinct odd states in
a bounded interval give \(m\gg p\), so every such arc contains a constant
times \(p\ell\) phases. Enough two-grade columns survive the shrinking
width margin.

Entropy shortening then improves the mixed Sidon-code rate. A paired
three-letter block has difference entropy at most \(5\log_2(3)/3\), and
a binary singleton at most \(3/2\). The argument accounts exactly for all
diagonal ordered pairs collapsing to the zero difference. Optimizing the
paired prefix gives a certified rate \(0.50671<d_*<0.50673\).
Admissible margin exponents satisfy
\(\sigma<1-3d_*/\log_2 3>0.04088>1/25\).
The coordinator checked the entropy maximum, diagonal loss, and
shrinking-arc errors. Exact rational controls establish the strict
numerical comparisons. A genuine four-column orbit fixture rejects the
attempted extension of the two-grade sign argument to three grades.

## Distinct genuine paths defeat finite local closure tests

[DISTINCT_MOMENT_PATHS.md](../../research/astra-nine-hour-20261128/cycles/phase7/DISTINCT_MOMENT_PATHS.md)
shows that for any fixed path length, polynomial degree, lower source bound
and modulus, there is a finite collection of genuine positive odd-unit
paths using gaps one and two, with every vertex across all paths and dates
distinct, equal polynomial moments and residue histograms on every layer,
and any compatible strictly positive rational path-word law. Moments can
also balance inside each residue and fixed finite native-word class.

The earlier weighted single-step barrier is credited to FreelanLab's
Paper 199/v2, including its stronger quantitative height/degree/modulus
tradeoffs. The new scope is arbitrary fixed path length, all layers,
unit weights, distinct vertices and compatible word frequencies.
No better height estimate is asserted. The coordinator read the earlier
theorems directly before making this comparison.

The dual argument chooses expanding or contracting true gaps according to
the sign of a leading-degree coefficient. On the strongly connected finite
marked type graph, expanding and contracting loops force all coefficients
to vanish. Convex separation and rationality give finite positive integer
weights. Multicolor Prouhet partitions replace weights by distinct
parameter values while preserving all polynomial moments; large spacing
and a generic initial shift separate every vertex. The coordinator checked
congruence lifting, strong connectivity, leading signs, Prouhet powers and
collision exclusions. Lean proves the finite sign-separation and type-graph
lemmas. Convex separation and distinct realization remain written.

A separate extension treats finitely many rational observables, retaining
positive integer multiplicities and disjoint initial/terminal supports.
It does not claim unit weights or all-vertex distinctness for rational
functions; Prouhet replacement preserves polynomial moments only.

## Timed ordinary floors and untrimmed critical moments

[TIMED_FLOOR_AND_CLOCK_CENTRES.md](../../research/astra-nine-hour-20261128/escape/phase7/TIMED_FLOOR_AND_CLOCK_CENTRES.md)
derives a timed floor theorem from Weaver 102. Set
\(g=1-H_2(\log_3 2)+1/351\). For every \(b<g\), uniformly in
\(2\le R\le Z\), the fraction of positive sources at most \(Z\) whose
first odd state at most \(R\) is reached after \(C\log(2Z)\) is
\(O_b(R^{-b})\).

The coordinator read Weaver 102's full finite, source-uniform event bound
and checked the transfer from odd source octaves to all positive sources.
Descending integer dyadic floor ranks give a geometric sum of bad-event
probabilities and a geometric logarithmic time budget. No extra factor
\(\log Z\) multiplies the exceptional mass. Combining this with the stopped
fair size walk gives Gaussian-sized first-floor clock windows.

For any odd target \(y\), its first-hit clock differs from the floor clock
by one of at most \(R+1\) centers. A target reached after the floor uses the
true first-hit clock from that landing value; a target reached earlier
contributes the negative of its own floor clock. The centers can be
arbitrarily large: no maximum small-source stopping time is assumed.
[FirstHitClockCentres.lean](../../research/astra-nine-hour-20261128/escape/phase7/FirstHitClockCentres.lean)
formalizes both orders and first-time uniqueness. Exact controls check
both orders and source spacing inside physical clock/mark cells.

A final concurrent-source refresh found that
[PR212 at e55fb7ca](https://github.com/GettysburgResearch/collatz/blob/e55fb7cac646013f143b563014ae97b105bc7547/research/astra-global-20261128/escape/ALL_SCALE_FIBRE_DENSITY.md)
already gives the same untrimmed moment range and critical exponents,
including a broader translated-minimum law and lap-normalized cyclic rows.
The coordinator read that note before this publication. The present work
is an independent finite ordinary-source proof through uniform timed floors
and signed first-target clock centers; it does not claim priority for those
shared moment conclusions. The entropy consequence below follows from
these moments and the earlier quantile covers.

[UNTRIMMED_RENYI_ENERGY.md](../../research/astra-nine-hour-20261128/escape/phase7/UNTRIMMED_RENYI_ENERGY.md)
bounds every bin of the unnormalized ordinary first-target log law
\(\lambda_y\). For mesh \(1/T\), put \(a_T=\sqrt{\log T}/T\).
Uniformly in target, grid translation and \(K\ge1\), every \(c<g\) gives
\[
 \sum_{I:\lambda_y(I)>Ka_T}\lambda_y(I)\ll_c K^{-c}.
\]
Sample at \(X=T^{2+K^\gamma}\), choose \(R\asymp K^\eta\) and clock width
\(K^\zeta\sqrt{\log X}\), with compatible strict exponent inequalities.
At a fixed physical/odd clock pair, a mark cell contains at most
\(O(X/T+1)\) actual integers. The good part of heavy-cell mass is bounded
by a shrinking factor times that same mass and is absorbed. Floor, walk
and sampling errors supply \(K^{-c}\). The coordinator checked uniformity
jointly in \(K,T\), rather than only an iterated limit.

Layer-cake integration yields the full untrimmed estimate
\[
 \sum_I\lambda_y(I)^q\ll_q
       \left(\frac{\sqrt{\log T}}T\right)^{q-1},
 \qquad 1<q<1+g.
\]
Checkpoint six's quantile bounds make this sharp for every fixed positive
minimum cell. Along every actual escaping component, physical unit bins
satisfy
\[
 y^{q-1}\sum_I\mu_y(I)^q
       \asymp_{C,q}(\log y)^{(q-1)/2},\qquad 1<q<1+g.
\]
This range does not include \(q=2\); that earlier quadratic upper estimate
still requires fixed mass removal. The Shannon entropy for each fixed
positive law is
\(\log T-\tfrac12\log\log T+o(\log\log T)\).
These matching asymptotics permit hypothetical escape. An exclusion
requires an additional restriction on its integer genealogy.

## Verification and provenance

The [strict fresh Lean replay](CHECKPOINT_07_LEAN.json) passed **27 modules
and 581 declarations, including 90 private declarations**. The three
[exact Python controls](CHECKPOINT_07_CONTROLS.json) passed normally and
with optimization, with identical paired output. They record exact source
hashes and outputs. The [source manifest](CHECKPOINT_07_SOURCES.json) covers
137 scientific files through phase seven. The audit includes every
declaration, private or public, and permits only propext, Classical.choice
and Quot.sound recursively. Local kernels and finite controls are not
presented as a formalization of the infinite analytic conclusions.

This checkpoint also corrects the author attribution in checkpoint six's
midpoint-variation note and review: rStation Paper 212 is by
lean_assurance_lab. Its mathematical use is unchanged. It is distinct from
GitHub PR212. The earlier qualitative steering is explicitly credited.

Ongoing phase-eight work targets the ordinary integer obstruction through
critical size-biased entropy, binary/ternary affine carriers, and rounding
clocks of integer cycle registers. Those unfinished claims are outside
this checkpoint's reviewed result set.
