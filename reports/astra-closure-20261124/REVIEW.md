# Review and execution scope

This checkpoint was developed in four GPT-6.2 Astra research lanes and
integrated by the parent. Reviews below reconstruct the relevant arguments;
they do not promote written analysis to kernel-checked Lean results. Exact
integrated file identities are in `source-manifest.json`.

## Mathematical reconstruction

**Canonical windows (CW1–CW2).** The parent and the cycle and synthesis lanes
independently reconstructed the endpoint congruence and the counting argument.
The charged interval is closed at both endpoints. The final carry contributes
only its indicator, so the argument never assumes a bound on its magnitude.
The normalized physical height removes the final carry from the cumulative
carry estimate. A polynomial upper bound on the canonical prefix maximum
therefore gives only logarithmic total carry and logarithmic window length.
Almost all windows remain clean, which is the precise reason ordinary
injectivity supplies distinct canonical words. The entropy and logarithmic
prefactor arguments remain written. The stationary-law equality criterion
uses fixed-block entropies of empirical laws on the same sequence of clocks.

The early candidate example of a critical mechanical word with sparse changes
was already covered by the upstream R12 criterion. It was replaced by an
oscillating-mean example. No novelty is claimed for the rejected example.

**Sharp carry penalties.** The local exact minimization was reconstructed
from the integer difference `a-b=3c-d`. The ordinary witnesses `3→5→1`
attain the two minima. The combined product has a written multiplication
proof; its factor-`4/3` specialization and the local `27/4` bound are separate
compiled declarations. The source attachment uses the actual infinite scalar
from the pinned PR182 file, not a freely chosen carry sequence. The real
trajectory and changing finite witnesses in `GLOBAL_BRIDGE.md` are explicitly
separated from one all-time ordinary source.

**Cycle filters (CF1–CF7).** The parent reconstructed the exact gap law,
the norm bound, and the physical downward-closure restriction. The scalar
and synthesis lanes independently checked the factorwise resultant argument,
including repeated irreducible factors, integer content, and prime powers of
the modulus. Each factor may choose a different one of the two binomials;
prime valuations, rather than an unjustified single resultant, recover the
whole necessary modulus. The two-convergent argument uses an arbitrary-
coefficient logarithmic-forms bound. A cycle-specific bound was not extended
to arbitrary coefficients.

For noncoprime clocks, the proof uses only the necessary principal factor
`2^a-3^b`. It does not assert a full-denominator root or discard the other
cyclotomic components by a cancellation assumption. Least-period
injectivity supplies the logarithmic upper bound on the cycle correction;
the logarithmic-forms lower bound then bounds the clock gcd polynomially in
the reduced period.

**Translated bands (TB1–TB3).** The scalar lane and parent independently
checked the synthesis proof. The predecessor convergent's best-approximation
bound rules out a zero coefficient on the translated center in the
pigeonhole relation. Powers of two clear wrapping denominators. The
auxiliary resultant is nonzero because at `X=1` one input becomes a nonzero
constant and the other retains its leading coefficient. This remains valid
when specialization lowers the first polynomial's degree. The parent also
reconstructed the asymmetric rectangle estimates in the logarithmic-width
corollary. These statements remain proposed written theorems, with effective
cutoffs and no enumerated finite remainder.

The reviews found no unresolved algebraic or quantifier gap within these
stated scopes. They supply no all-profile support theorem and no universal
upper bound contradicting canonical escape growth.

## External inputs

The parent inspected the primary Simons–de Weger paper, including the odd-step
normalization of its Corollary 2 and Lemma 12 and their reliance on a historical
verification floor. That computation was not rerun. The parent also read
Matveev's Corollary 2.3 in the primary paper to check that the coefficient
quantifiers support the required finite irrationality measure. The papers
and precise uses are cited in `CYCLE_FILTERS.md`. No current unverified
announcement about unrelated conjectures is used.

The upstream R12 whole-orbit counting and bounded correction inputs retain
their written-proof status. Their exact pin and role are recorded in
`CANONICAL_WINDOWS.md` and the packet README.

## Executed evidence

The complete local Lean graph was rebuilt from copied sources in an empty
directory. The newly built directory preceded every Mathlib search path, so
local imports resolve to the new objects. All eleven invocations (ten research
modules and one exact upstream scalar dependency) exited zero with one worker
and warnings as errors. All 41 explicit axiom reports used only standard
axioms. The original per-lane receipts are retained alongside the isolated
replay receipt. The latter's source hashes were checked against the integrated
files.

All three finite control scripts were rerun from the integrated packet under
normal and optimized Python. Each pair was byte-identical and matched its
recorded JSON. See `finite-controls-replay.json` for counts and hashes. These
bounded checks support only the reported samples.

Repository structural validation is recorded separately. Its meaning is
checkout integrity and retained bounded self-tests, not mathematical proof.
