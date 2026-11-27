# Actual path budgets and the ordinary-source boundary

This checkpoint continues [the first packet](README.md). Collatz convergence,
exclusion of escaping positive integers, and exclusion of nontrivial positive
cycles remain **OPEN**. The strongest new formal result is an explicit
reciprocal bound for every finite simple ordinary segment above a supplied
floor, followed by a comparison of two actual paths to the same endpoint.
The other results distinguish properties of an infinite symbolic script from
properties that would decide its realization by one positive integer.

## A kernel-checked statement on arbitrarily long finite paths

Write \(T(x)=x/2\) for even \(x\), and \(T(x)=(3x+1)/2\) for odd \(x\).
Suppose \(x,T x,\ldots,T^L x\) are all distinct and at least \(2^{71}\).
The two new counting modules prove

\[
 \sum_{i=0}^{L}\frac1{T^i x}<\frac{249}{250},
 \qquad
 \sum_{\substack{0\le i<L\\T^i x\ {\rm even}}}\frac1{T^i x+1}<\frac14.
\]

There is no restriction on \(L\), no assumption that the source terminates,
and no condition modulo three. The statements include the final site in
the simplicity and floor hypotheses. They do not apply to an indefinitely
repeated cycle.

The proof counts actual sites in each height shell. A site with a low odd
count after a chosen number of steps maps injectively into a lower shell.
The other sites occupy different exact parity cylinders. A rational
binomial-tail bound and a finite kernel evaluation supply a summable
infinite reserve. In particular, the proof does not enumerate trajectories
up to a stopping-time cutoff.

* [Actual orbit counting](coupling/FloorCounting.lean)
* [Complete rational certificate](coupling/FloorCertificate.lean)
* [Written proof and stronger literature comparison](coupling/FINITE_FLOOR.md)
* [Independent exact rational control](coupling/floor_bound.py)

The high-floor condition is an explicit hypothesis inside Lean. Connecting a
visit below this floor to convergence uses the separate published finite
verification of Barina; that computation is not part of these Lean modules.
The reciprocal and residue estimates of Nikzad, Frinkle and Bagherzadeh are
stronger in their stated normalization. We do not claim a new numerical
record. [Barina 2025](https://doi.org/10.1007/s11227-025-07337-0) ·
[Nikzad–Frinkle–Bagherzadeh, Lemma 2.20](https://hexagonmath.org/pdf/2611.00033)

## An ordinary inverse minimum, with no completed escape hypothesis

Let \(q\) count odd departures on the reference prefix of length \(n\).
The new [OrdinaryGeodesic module](OrdinaryGeodesic.lean) proves the exact
residue identity and, under the preceding simple-path hypotheses,

\[
  3^q x\ \le\ 2^nT^n x\ <\frac32\,3^q x.
\]

Now suppose a positive integer \(y\) reaches this same endpoint in \(m<n\)
native steps and has the same odd-departure count \(q\). Its own exact
residue is at least one, without a simplicity or floor assumption on that
second path. Thus \(2\,3^q y\le2^nT^n x<\tfrac32\,3^q x\), which
in particular gives \(y<x\). The theorem
shorter_same_grade_is_smaller checks this comparison on the actual
CoreBranching.run and PeakRigidity.grade.

Consequently, a least positive source of a hypothetical escaping component
would minimize the division clock at every odd depth from its own initial
grade. This is a consequence of a finite statement; it does not assert
that every truncated suffix is minimum-cost. Corrected-height minimization
and deeper all-horizon comparisons were already developed in PR192 and
PR197. The present contribution is a direct ordinary finite-path
formalization using the new checked budget.

## What the inverse-path analysis establishes

[TROPICAL_SIBLINGS.md](escape/TROPICAL_SIBLINGS.md) expresses the ordinary
fixed-source posterior through the minimum inverse clock \(m_n(y)\).
Its lateral branches satisfy a weighted summability constraint. A sufficiently
frequent cheap sibling would violate that constraint, but no such comparison
has been proved for the required one fixed positive source. The note
credits stronger existing all-horizon and branch-gain statements.

[GEODESIC_POSTERIOR.md](escape/GEODESIC_POSTERIOR.md) proves a uniform
exponentially decaying excess-clock tail for every infinite gap script on
\(\{1,2\}\) without consecutive twos. The proof controls every excess
clock, every depth, and the original geometric law. It counts alternative
integer affine offsets using a dyadic cylinder estimate and a real
localization identity. Its general version requires a uniform cost defect
on **all consecutive subwords**, not just on initial prefixes.

The local recurrence, finite telescoping identity and localization
inequality are checked in [GeodesicPosterior.lean](escape/GeodesicPosterior.lean).
The full infinite counting argument is a written proof. Positive ordinary
realization of an entire eligible infinite script is not established.

## Entropy and arithmetic results, with their exact scope

| Result | What it proves | Remaining boundary |
|---|---|---|
| [Finite decoder entropy](escape/FINITE_DECODER_ENTROPY.md) | Finite exact ternary predictor tables attain entropy arbitrarily close to the geometric maximum under mean gap below \(\log_2 3\). | The construction gives stationary symbolic systems, signed rational periodic points and changing finite positive realizers. |
| [Universal table](escape/UNIVERSAL_TABLE.md) | One finite table works on the specified low-entropy state portion for every stationary inverse law with the supplied mean bound; an exact finite search is described. | Source-qualified on PR200 O15; the proposed linear-program search was not executed. |
| [Reset front](arithmetic/RESET_FRONT.md) | For one positive ordinary source, the excess division clock divided by \(\log(i+2)\) tends to infinity; a version applies to algebraic two-adic sources. | The ordinary conclusion is weaker than existing Paper 174. The Subspace-Theorem argument is written, with only its finite identities formalized. |
| [Haar modulus](arithmetic/HAAR_MODULUS.md) | Independent cubic rotations give a convergence/oscillation dichotomy according to \(\sum x_i^{-2/3}\). | The physical embedding is not a random Haar embedding; neither case excludes its ordinary orbit. |

The [root review](../../reports/six-hour-20261127/ROOT_SECOND_REVIEW.md)
reconstructs the arguments and records their boundaries.
The reproducible compilation/control entry point is
[replay_second.py](../../reports/six-hour-20261127/replay_second.py).
Its receipt records exact source hashes, compiler and dependency pins,
audited declarations, and complete normal/optimized control comparisons.

The next constructive packet studies explicit lower canonical parents and
long physical returns for remaining Mersenne exponent classes. It has a
separate review and publication boundary.
