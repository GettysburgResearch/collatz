# Frozen source and latest-repository boundary

This packet starts from main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, tree
`1c25c17df24491de6187445f1a1d355d5a7660c3` (315 tracked files).
The existing integrated qualifications and scoped errata remain in force.
Only the explicitly identified deductions are reused. A PR description,
a mathematical source read, a separate reconstruction, and a replay are
different evidence events.

## Proof dependencies and direct comparisons

| Source | Full frozen commit | Files and claim scope actually inspected |
|---|---|---|
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146) | `6863d298187af8b2619efbf78cc4b0aa8e627393` | `research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md`: one-sided basin closure criteria. Motivation and comparison for GCM-001/002; the new directed certificate is checked here. |
| [PR148](https://github.com/GettysburgResearch/collatz/pull/148) | `55d8968d2ecbc23a91c9c4733929f34be9bf0d28` | `research/focused-forward-20261120/pressure/PROOF.md`, H1--H3 and O1--O2; adjacent README. Root-potential normalization and open uniform pressure obligation. |
| [PR149](https://github.com/GettysburgResearch/collatz/pull/149) | `92c0129e794dde3ec55ceec470a12d51ba3f7e2f` | `research/forward-inverse-defect/PROOF.md`: rational inverse potential, its forward defect, and stopping-grade context for the uniform-word obstruction. No additional global closure is imported. Exact reused attribution is to PR150's pinned LC-1 below. |
| [PR150](https://github.com/GettysburgResearch/collatz/pull/150) | `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9` | `research/pointwise-closure-20261120/STOPPING_BURDEN.md`, SB1--SB5; `LOCAL_CERTIFICATE_GRADE.md`, LC-1--LC-3; `GROWING_COMPLEXITY.md`, finite inequality (1) and growing-threshold theorem; `SPARSE_RETURN_SPECTRUM.md`, SR-1. GCL-003's constant-error equivalence is already SB5, not a new claim of this packet. |
| [PR152](https://github.com/GettysburgResearch/collatz/pull/152) | `2391a9c1e4a7f77233b951d2eb6da92e76652e7c` | `research/gemini-global-closure-20261120/ACTUAL_TRANSPORT.md`, AT2--AT3; `FIXED_SOURCE_DRIFT.md`. Actual acceleration, quarter-safe return, additive gauge budget, and fixed original input. Inherited moving-rank qualifications are retained. |
| [PR153](https://github.com/GettysburgResearch/collatz/pull/153) | `eb04a5d79020cefa0ba46794095b5766c5ff66a4` | `research/fixed-integer-descent/drift.md`, FID-DRIFT-001/002/005, supplies the translated simple-path theorem used by GCT-004. Its SHA256 is `d73a93d8a803996bde7b15f33e307d28385c8ffe2f9b99f449dfea35140c3338`. The arithmetic comparison uses the scope of RC-1--RC-5 in the neighboring `arithmetic.md`; neither its six-run guard nor its replay is changed. |
| [PR154](https://github.com/GettysburgResearch/collatz/pull/154) | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0` | `research/structural-reset-20261120/component/PROOF.md`, CR-001/002; `component/REDUCED_LAWS.md`; `adelic/PRIME_HEIGHT_ESCAPE.md`, ADEL-001--ADEL-006; `adelic/CLOSING_ATTEMPT.md`, sections 1--6. The new certificate strengthens the specified component criterion, and the new legal finite blocks test the arithmetic proposal. |

PR151 at `02a9f6ad17e5f1904cb4ff806fd0217d199e8437` was also inspected
at the PR-description/context level for physical-merger work. This is
not represented as a proof audit or a new execution of that PR.

## Concurrent additions inspected before publication

The latest-repository read was extended to PR155 and PR156 after the four
manuscripts were frozen. Neither supplies the missing premise of this
packet. These are bounded source and overlap reviews, not replays of the
other contributors' suites. Later changes are outside these pins.

### PR155: spatial invariant-label coercivity

At [commit 92f499b9d340d1ff8cc643c3eef3477d61b477c1](https://github.com/GettysburgResearch/collatz/commit/92f499b9d340d1ff8cc643c3eef3477d61b477c1),
the transport author fully read:

- [`ORDINARY_DIRICHLET_COERCIVITY.md`](https://github.com/GettysburgResearch/collatz/blob/92f499b9d340d1ff8cc643c3eef3477d61b477c1/research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md), OD1--OD4, five-ray comparisons (19)--(24), and section 8's PR146 dependency reconstruction. SHA256: `d5229d794b97ba4c7663f105388ed597251d34fd678cc2189c39ebf0c7b43c74`.
- [`ENDPOINT_BOUNDARY.md`](https://github.com/GettysburgResearch/collatz/blob/92f499b9d340d1ff8cc643c3eef3477d61b477c1/research/gemini-dirichlet-global-20261120/ENDPOINT_BOUNDARY.md), E1--E5 and the complement argument. SHA256: `033a47875fa6f84b2cca73f59e23635df99d244f18f79ad4ba6392ee291276d3`.

Those theorems compare spatial weighted norms of ordinary invariant
labelings and their tripling/five-ray defects, with the variation mechanism
credited there to PR146. Our original source, its transported iterates,
and the gauge are not invariant labelings. Our Poisson corrector has a
nonzero coboundary, not invariance. The source-weighted smaller-charge
Green bound therefore does not supply PR155's still-missing unweighted
component or boundary upper bound. Conversely, PR155 supplies no actual
reciprocal-psi occupation estimate. Its endpoint profile limit also permits
a sparse nonempty exceptional component.

### PR156: physical guards and changing horizon survivors

At [commit c5cb84502c7289705d59a8781a65fd845b9b6b14](https://github.com/GettysburgResearch/collatz/commit/c5cb84502c7289705d59a8781a65fd845b9b6b14),
the merger author fully read the following files under
`research/global-rigidity-20261120/`:

| File | Git blob SHA |
|---|---|
| `README.md` | `1e0606a395763408dba78f3a7a2f7ce86851c58c` |
| `Q_SECTION_GUARDS.md` | `5793d3c2d7529f3ac82449493ff343f6bbc9377a` |
| `REVIEW_Q_SECTION_GUARDS.md` | `51cdb4180000792526af0e9df157f189fb89db4e` |
| `SOURCE_BOUNDARIES.md` | `b3cc075424aba8e183b77067ee078f932f842a15` |

Its QG1--QG4 give orientation-aware physical guards, two exact smaller
tripling comparisons, and a changing horizon-survivor family
`a=2^H t-2`. The odd-part version has its printed parity restriction on
`t`; the compatible original code is the signed integer `-2`, not a
positive ordinary survivor. Fixed-source eventual guard success remains
open. The new forward-five sufficiency theorem is not supplied by these
claims. Their obstruction to uniformly bounded **ordinary** guard programs
reinforces the distinction already stated in GCM-001: the uniform size of
our conditional proof graph is not an ordinary physical clock bound.

## External primary source

Applegate and Lagarias, [*The 3x+1 Semigroup*](https://arxiv.org/abs/math/0411140),
version 2, Theorem 1.1; *Journal of Number Theory* 117 (2006), 147--159.
The source was read for the multiplicative semigroup statement. It does
not establish the pointwise forward-five basin law. Products of ratios
from unrelated trajectories do not by themselves concatenate into an
ordinary orbit. No broad literature-priority claim is made.

## Exact boundaries of our reviews

The four review files pin the manuscript and executable SHA256 values and
state what was independently reconstructed. In particular, the positive
occupation proofs remain source-qualified to the actual return/rank and
simple-path interfaces; those qualifications are not converted into a
claim of formal verification by this source index.
