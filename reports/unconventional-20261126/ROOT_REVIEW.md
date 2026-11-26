# Coordinator reconstruction and remaining proof boundary

**Status: scoped written review, with separate executed finite checks.**
The pass began on 2026-11-26 at 18:52:27 UTC from PR201 head
`94ce06ccbd312ccd0ce4450b567cc514a2f0b54a`. The scientific entrypoint is
[the continuation overview](../../research/unconventional-20261126/README.md).
This report does not assert that all repository papers, all earlier PRs,
or every new analytic appendix received a complete independent audit.
The reviewed files are identified by SHA-256 in the source manifest and,
where a separate review exists, by the review's own explicit source pin.

## 1. What was actually checked

The coordinator read the repository's scientific entrypoints, correction
and replay policies, the starting record-renewal packet, selected current
PR interfaces, and the main arguments of the three new lanes. The thirty-PR
intake in `SOURCE_INTAKE.json` is metadata coverage. The independent lanes
were GPT-6.2 Astra agents; their reports are mathematical reconstructions,
not endorsements by external human reviewers or independent proof kernels.

The coordinator executed the exact ten new Lean files, queried all 53
listed declarations, and replayed seven finite-control scripts both with
and without Python optimization. A subsequent eighth gate-control script
passed the same two modes, as recorded in `GATE_REPLAY.json`.
See `REPLAY_RECEIPT.json` and the raw
axiom logs. These runs verify their stated finite scope. The infinite
analytic arguments below remain proposed written mathematics.

For the two earlier broad-import Lean files, the original compilation
failed on a missing cached dependency. The successful fallback changed
only imports and retained the original proof bodies. Both the failure and
the successful narrower replay are preserved in `BASELINE_LEAN.json`.
They are not an exact-byte build of those original complete files.

## 2. Critical records and the sharp gauge

**VERIFIED at the written argument level:** `renewal/SHARP_GAUGE.md`
(`0dc36211f63059e5be36ea8ddf136602b062032553993ef6c796fa8ac4dea899`)
and `renewal/CRITICAL_GAUGE_ENDPOINT.md`
(`9e55dc5e81e9617b0ced6ef55ebaea135bc9e81b1676aa1ccc19fa2ce5871a50`).

The decisive accounting is the geometric change of measure: a word of
length n and terminal deficit d has mass exp(-Hn+hd). Confinement in a
strip of width f n^(1/3) contributes cost 3 kappa/f^2. Minimizing
hf+3 kappa/f^2 gives the asserted critical constant. Carry projection
does not preserve cylinders injectively, but its multiplicity is bounded
by a polynomial times 2 raised to the deficit range. The inequality
h>log 2 leaves the required exponential gain. The proof cannot omit that
comparison or treat the symbolic and ternary metrics as identical.

At equality, the slowly varying width is
f n^(1/3)(1+1/t+1/(t log t)), t=log n. The second-order expansion leaves
negative slack -1/t^2-1/(t^2 log^2 t), dominating the stated coupling and
partition errors. The coordinator checked the scale of stage length,
shrunk-interval error, and accumulated logarithmic errors. The exponential
moment version of the KMT theorem applies to the tilted geometric law;
it does not require a nonlattice distribution. The primary KMT theorem,
Brownian interval kernel and its scaling were consulted separately.
The exact threshold is therefore a plausible completed auxiliary theorem,
with its independent agent reviews pinned separately. It is not an
ordinary-orbit convergence theorem.

The later upper logarithmic refinement is a separate proposed appendix.
It is not needed for the threshold claim just reviewed. The unrestricted
incoming-set integral test has its own independent review; the
coordinator did not repeat every conditional-measure estimate in that
longer appendix and does not extend this verdict to it automatically.

## 3. Renewal pressure, occupation and actual record flows

**VERIFIED at the written argument level:** the exact first-maximum
factorization and three-term pressure expansion in `renewal/PRESSURE.md`
(`478fb986123f0b36ed7bab565a4ee72a8edb642e9bf8355a5b9c1e87d00f37c1`).
The factorization, tilted convolution profile and irrational-rotation
window average were reconstructed. The final constant includes the
normalization factor from the total renewal mass; dropping it midway
would change the answer. `adelic/REVIEW_RENEWAL_PRESSURE.md` additionally
pins an independent enumeration and a review of the density spectrum.

The coordinator reconstructed `RECORD_FLOW.md` and `BRIDGE.md`: elapsed
odd time supplies tightness without a bounded-gap assumption, while
opposite-end divisibility involves one cleared nonzero integer. One
cannot replace this elapsed-time normalization by ordinary probability
on record indices, or assume that all mass survives when record density
tends to zero. The claimed atomic classification leaves the nonatomic
part open. The opposite-end precision inequality leaves its complete
height term in place.

**VERIFIED at the written argument level:** `RATIONAL_DIAGONAL.md`
(`3b823138448df4579e404f8d145fdbde35ce2f0416cf6352d80b2994a447be90`).
The coordinator also read the precise R1 proof at PR210 head
`592328fecf8ea2cf41736294856d95f890a1ba98`. For odd-numerator,
odd-denominator rational critical endpoints it supplies a purely
periodic backward code, not merely an eventually periodic code. This
distinction is necessary. Compactness gives a uniform finite memory for
the inverse of the shift on a set of purely periodic right tails; its
finite factor graph then has one incoming and one outgoing edge at each
vertex. This makes the omega subshift finite. Bounded distance to records
transfers this conclusion to the native parity word of the supplied
ordinary trajectory. The dyadic argument first forces bounded record
clocks when all cluster points have finite upcrossings. Thus the new
rational-diagonal exclusion applies to one actual escaping ray and to
an arbitrary compact set of rational diagonal limits. It still permits
irrational limits and unequal rational coordinates.

The coordinator reconstructed `RECORD_TEMPLATE_COST.md`
(`15c6e2420745561fb2d3028f118845a76eedc1be68cbe6f04ddd34df54821d76`)
as an application of the fixed-source window theorem. Its order of limits
is essential: a fixed number J of record blocks is grouped first; only
after taking the orbit limit may J increase. No uniform Subspace Theorem
constant in J is assumed. The count of exceptional intervals remains
fixed within each such application. This yields a necessary cost for
template coverage, not a bound asserting that actual orbits have low
template complexity.

The later `MONOTONE_RECORDS.md`
(`9d4deafdcaf39c987f1349da02c0a2e278d5ce8f5c4ecd34d4eacc2c9f4fc547`)
was also reconstructed. Divisibility limits the duration of each repeated
word from its actual fixed start. Summing the overshoot-weighted harmonic
budget gives a coefficient below one for at most nine runs per allowed
length. This forces positive logarithmic density of run starts; the
count of distinct lengths then gives quadratic odd time on a subsequence.
For nondecreasing lengths, dyadic-interval rotation means bound the
inhomogeneous product uniformly and give quadratic time throughout.
Combined with the template-cost theorem this excludes the stated
two-piece ordinary families. Neither theorem says that arbitrary actual
record words have this structural restriction. The separate adelic
review pins both input files.

## 4. Coherent rational cycles and complete denominator accounting

**VERIFIED at the written argument level:** `adelic/COHERENT_SWITCHES.md`
(`2fb70576cb865169e86eaceaed46f7b6f066ca86acc8931c7b665e9851d44767`),
with independent review `operator/REVIEW_COHERENT_SWITCHES.md`.

The coordinator reconstructed the two coprime forcing tracks, their
common-slope affine superposition, the native least-period argument,
the smooth-part cancellation, the surviving denominator factor, and all
three cases of physical pair separation. The positive virtual comparison
system must close at the average macro boundary value. Comparing against
one fixed flag choice instead could introduce a large L/delta shift and
would not prove the stated separation. For identical offsets, coprime
track phases give the 1/(rt) spacing before the controlled error; for
different offsets, the best-convergent bound supplies a macroscopic gap.

The sieve removes the full prime powers in the tested smooth part of the
actual determinant B^(rt)-A^(rt). It does not merely prescribe a numerator
modulo a square-free product. Conversely a separate surviving cyclotomic
factor ensures that the reduced denominator is strictly greater than one.
The construction is therefore not accidentally an ordinary Collatz cycle.

The shorter patch argument in `renewal/CYCLE_SIEVE_REVIEW.md` was
reconstructed: an injective short discrepancy vector and Hölder across
disjoint windows reduce the cost to O(log Y log log Y). The primary Yu
valuation formula was inspected with its prime dependence retained.
Its use supports a prime cutoff below the square-root scale with the
specified logarithmic losses. It gives no control over the full
unrestricted determinant.

The coordinator also reconstructed `FIXED_SOURCE_TOPOLOGY.md`
(`97720745ee0e42520c29c3a194c9e18433416d09dd1170cb583242f23ec8aec0`).
Fixed genuine prefix/suffix words impose the 2-adic and 3-adic contacts;
the patched modulus includes both the desired approximation powers and
the determinant's full valuations at other tested primes. Free
equal-grade blocks vary the real phase by a ratio greater than two,
while the final residue repair is lower order. This constructs different
rational points converging to one prescribed integer at each individual
finite place. It does not converge in the integral neighborhood of the
restricted finite-adèle topology, and supplies no single rational point
with that integer's entire future script.

The finite controls were independently executed, including all 865,445
native transitions of the largest example and the outward-interval pair
separation. That example tests exactly primes 5 and 71. Its arithmetic
does not count as a computation over the asymptotic prime range.

## 5. Physical operators and mixed-coordinate obstruction

The coordinator reconstructed the core branching and Cheeger argument,
the exact hair Schur complement, the stated local-spectrum comparison,
the weighted boundary distinctions, the unit-circle escape eigenstates,
and the diagonal incoming-slope criterion. The finite impedance and
summed-oscillation certificates were replayed. `HEIGHT.md`'s discrepancy
improvement retains a power error; it does not assert a bounded error.

In the boundary results, the maximal form is defined separately on each
actual component. Identifying all ends by a boundary condition would
force a one-dimensional constant space without proving connectivity.
The projection-computability statement retains a computable exponent.
The published .84 predecessor input remains source-qualified; no large
external computation was reproduced here.

`MIXED_EIGENSTATES.md`
(`f956d7efedb3d45b36f9d8d233d35925aa7785d1662cebd379862c04d5340cae`)
was reconstructed. The exact summable modes on dense mixed components
show that Haar contraction does not exclude singular conformal measures.
The later positive-realization appendix retains all affine translations
and still fails the infinite ordinary diagonal. In that model, if the
initial rational real height differs from its dyadic coordinate, its
forward denominator valuation eventually falls by one per native step.
An arbitrarily accurate finite root match does not remove that failure.

The global incoming-slope little-o condition is an exact no-escape
criterion on ordinary integers. No estimate proving that condition has
been established. Replacing it with a pointwise power saving would be a
substantial new theorem, not a consequence of an almost-everywhere
ternary estimate.

**VERIFIED at the written argument level:** `operator/EXIT_GATES.md`
(`a5fc2c44d8e33ad808c7fe5e9b9dae14918df5f28f0f8792051d7bd3f058963e`),
OP-G1 and OP-G2. Retention factors telescope exactly, so transport to a
higher cutoff is substochastic after adding the newly exposed sources.
The augmented total is monotone; the largest individual gate need not be.
For each fixed escaping source, its first exit eventually coincides with
that of a chosen representative of its component. The weight tends to
the inverse homogeneous height to power s. A source truncation with tail
at most twice the ordinary Dirichlet tail upgrades this to total-variation
convergence. Rearrangement then gives the stated component-mass limits.
Every fixed periodic-basin source eventually contributes zero, regardless
of which positive cycle it reaches. This is consequently a criterion for
no escape, not a positive-cycle uniqueness proof. The coordinator read
the full exact script and reran all nine cutoffs through 100,000 in both
interpreter modes. Proving decay of the limiting total remains open.

## 6. Open final obligations and publication scope

The exact Lean theorem `Collatz ↔ NoEscape ∧ CycleUnique` separates the
two universal conclusions still needed. Neither is filled by an axiom,
an omitted proof, a finite enumeration, or a changing-source limit.
The infinite families of rational cycles are counterexamples to some
proposed closing estimates, not counterexamples to Collatz.

The strongest current useful next target is an estimate on the physical
ordinary diagonal that eliminates a positive escaping component, together
with a separate full-denominator positive-cycle exclusion. Stronger local
spectral laws, finer fractal gauges and larger finite prime tests do not
by themselves supply either implication.

All verdicts are restricted to the identified arguments and their stated
dependencies. Later source edits require their own review. The source
manifest authenticates bytes; the clean-checkout validator authenticates
repository integrity. Neither is a theorem of mathematical truth.
