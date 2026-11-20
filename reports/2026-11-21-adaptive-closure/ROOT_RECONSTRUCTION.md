# Primary-agent mathematical reconstruction and integration boundary

**PROPOSED mathematics with scoped internal reconstruction. No full
Collatz proof, external referee acceptance, or new proof-assistant
formalization is claimed.** The primary agent supplied ideas and
coordinated the three authors; this is not a blind or externally
independent review. Separate agent reviews are listed in the report index.

## Frozen mathematical subjects

| File | SHA-256 |
| --- | --- |
| `AFFINE_SECTION_RECURRENCE.md` | `f033ed30e8468a1235dd5aaee0f9445074d32192b6c4f14357cb28c1ed06379a` |
| `AFFINE_SECTION_ROOT_RETURN.md` | `4079ef1361418368bb81e604b27cb59b02076f2c22c76b71ae9863ddb7619f94` |
| `LINEAR_HORIZON_SIEVE.md` | `cc8102d1a7f6920a7489a2ba32ee15d41fbcc9e38e542300977b539b5956bcf6` |
| `SIMPLE_PREFIX_PRODUCT_SIEVE.md` | `6fcae49f659f8350de25cf56c40a274a82be459f2150f05a7ad0abc82d7689b4` |
| `CRITICAL_NEGATIVE_MOMENT_INTERFACE.md` | `8a78077b651ff2c7791325c458cd513b027325a51452cac36208d95b48ff695c` |
| `VALUATION_ONE_TRANSPORT.md` | `a47dd19445db7cf9f8e3e4522686161b39679866e0701f8ac05ecbda292f3422` |

The author files were imported byte for byte. The root review covers the
mathematical items below and their stated limitations, not every result
in every source PR.

## Exact section recurrence and return synthesis

I reconstructed the rational affine update and its lattice separately
from the checker. On bounded k, the allowed denominators are bounded
powers of three; bounded real carry therefore leaves finitely many
states. This exact lattice fact is essential to properness.

The two-step carry normalization and the lazy martingale were checked
algebraically. The identity `v_2(5*3^k-1)` equals one or two also for
negative k. The listed choices force an active increment within three
steps with probability at least one quarter. Orthogonality of martingale
increments gives the claimed three-step variance. For odd carry, the
reciprocals of the two multipliers sum to `8/3`, so convexity gives the
same square-root contraction as the even-carry endpoint pair.

I reconstructed the Foster function architecture before reading the
final constants, then checked the explicit choices. The logarithmic
second derivative on `|k|>=2003`, the pointwise g-ratio, and the inner
carry threshold give S9–S11 with the stated signs. A stopped nonnegative
supermartingale converges; properness confines an avoiding sample path
to a finite sublevel set, where the positive drift decrement has a
positive minimum. The compensator cannot then have finite total mass.
This proves almost-sure finite-core hitting without irreducibility.

The newly fetched PR146 controller was read in full. Its signed integer
normalization matches the rational section exactly, and its root route
works from every finite-core state. Finite-core recurrence and finitely
many finite control words give a uniform conditional chance of a root
hit; repeated trials close the root communication step. They do not
alter the bits of a supplied ordinary source.

For the pressure consequence, finite mean return would give L2 optional
stopping of k and force zero expected quadratic variation, contradicting
the active step after the initial odd branch. The odd-endpoint selection
dominates that true first-return stopping time, so the expectation
argument does not misuse a lookahead time. The conditional exponential
tail has exact fifth power `243/256<1`, and `32/27>1` pays the positive
log inverse slope on its complement. The infinite inverse-slope moment
then forces unbounded finite-family means through PR167 DC2. Only the
first-successful selections determined through their endpoint bit use
the exact cylinder mass `2^(-L)`.

For ordinary strict descent, the affine intercept is fixed on a finite
cylinder, while the common slope can be below `theta/2`. Thus all large
ordinary lifts in that cylinder have endpoint below `theta*x`. Finite
unions of those periodic cylinder tails approach full measure and give
the uniform-interval density conclusion. No rate or pointwise coverage
follows. Every known convergent source has finitely many root returns;
this is retained explicitly rather than hidden in an almost-sure claim.

## Source-preserving sieve calculations

At the first coefficient crossing, each earlier odd affine contribution
is `c_i/(3c_j)<1/3`; this proves LHS1 directly. The exact rational
height coefficient in LHS2 is below 76, which is below `5X/8` for
`X=128k+1`. The existing directed reduction is an imported interface.
The longer census horizon is not treated as a longer independent binary
sampling horizon.

For a finite simple odd segment, deleting its last q positions ensures
that U^q is injective on the remaining positions. The added q is at most
half the target `Z^(39/40)` allowance. I checked the two original lanes,
the reciprocal-integral identity, the product formula, and the exact
floor margin `3904144k-1081168>0`. The resulting no-horizon criterion is
restricted to a simple input prefix and to the stated large floor.

## Critical arithmetic moment interface

I read PR146's critical interval count and PR169 MQ1–MQ2 at the pinned
heads. The shell saving `(1+h)^(-3/2)` is summable at rho, so the full
critical reciprocal-power sum is finite on one distinct orbit. Keeping
one fixed original source in the exact nonnegative arithmetic moment
gives C4; its negative rho/2 power then sums to C6. The critical quantile
bound counts times only because the hypothetical orbit is nonperiodic.

The old supercritical quantile-excess target implies the new critical
series divergence by contrapositive. The illustrative comparison
sequence shows that the converse need not hold. Neither example is
claimed to describe the actual congruence moments. The fifth-denominator
estimate does not supply the new divergence; its moving-endpoint
comparison array is explicitly separated from actual word constraints.
Nontrivial cycles remain outside the distinct-state inference.

## Valuation-one packet and overlap

I reconstructed the corrections 65 and 325, the source residue, the two
endpoint classes modulo27, each complete geometric fiber sum, and the
finite-cutoff energy subtraction. The forced rank-two residual uses an
actual negative-five shadow followed by exactly three final halvings.
The one-then-threes correction decoder terminates above one, excluding
that balanced prefix architecture only.

The live source refresh showed that V1–V2 had already appeared in
PRs167–169 and that their broader kernels improve on this smaller-domain
coefficient. The author corrected attribution before freezing. The root
integration does not advertise the repeated block as new coverage.

## Evidence limit

The report index and actual execution receipts distinguish proof
reconstruction, finite arithmetic replay, and repository integrity.
None of those events supplies the missing ordinary universal transfer,
actual-label energy estimate, critical arithmetic divergence, or cycle
exclusion.
