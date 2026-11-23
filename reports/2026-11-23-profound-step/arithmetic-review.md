# Independent review of the triadic construction attempt

Date: 23 November 2026. Reviewer: `cycle_arithmetic`, independently
reconstructing the work of `triadic_construction`.

**Verdict: VERIFIED for the new finite identities and the enumerated
written deductions below; SOURCE-QUALIFIED for the imported literature
statements. Universal witness construction remains OPEN.** This review
does not widen the preceding convergence theorem's hypothesis or certify
the complete external proofs.

## Exact reviewed files

| Path | SHA-256 |
|---|---|
| `research/profound-step-20261123/arithmetic/TRIADIC_CONSTRUCTION_ATTEMPT.md` | `92228f5a376d7c6af08ad256fb14ed1f09e155c9c514c49b94568e9d0dadc093` |
| `research/profound-step-20261123/arithmetic/README.md` | `5a9b08d25578345ba6ceb6f567fe087d395c29108a47d26e0eae0956b6c22b8f` |
| `research/profound-step-20261123/arithmetic/lean/TriadicBoundary.lean` | `4cd83febdb3161feb7ad56149e794b8fcb29aa278efb3b912577c63766f5265d` |
| `research/profound-step-20261123/arithmetic/lean/TriadicBoundaryAudit.lean` | `c9712b42bf5b371e00b4c0aeebb474687eac29f8324e258205786c38dde8f28e` |
| `reports/2026-11-23-profound-step/arithmetic-lean-receipt.json` | `72fadfe6859bc8b69846544424d0627ce650f9cdaebef0523412ab5a3a229018` |
| `reports/2026-11-23-profound-step/arithmetic-sources.json` | `c9a65f55e5809903a3ad1754b112616441482869c2b32813500f639ebf765032` |

The author receipt's source and output hashes were checked against the
actual bytes. The independent audit output has the same hash as the
author's audit output. This review binds the listed final source bytes,
not later revisions.

## 1. The candidate and the two boundary recurrences

I reconstructed both carries from the original parity bits and checked
that their powers of three count opposite letters. The ordinary affine
identity is `3^p*n+C=2^K*x_K`. The supplied terminal choices
`c_K=1+e_K` and `d_K=2-e_K` have the complementary and original parities,
respectively.

Backward complementary branches are `z -> 2z` at an original-odd bit and
`z -> (2z-1)/3` at an original-even bit. Both preserve the 2-adic integers
and fix the prescribed input parity. Each inverse branch multiplies a
2-adic difference by a factor with norm one half. The terminal difference
between `c_K` and the true complementary state is even, so pulling back
through K branches proves the claimed `K+1` bits of agreement. This is a
finite-prefix statement about one fixed original input.

For the original terminal candidate, subtracting the actual source
identity gives equation (6), and `x_K-d_K` is even. The same extra bit is
therefore justified.

For each of the four pairs of consecutive parity bits, substitution into
the two carry recurrences gives the stated boundary recurrences (7),
with opposite correction signs. Dividing by `3^b_(K+1)` and
`3^p_(K+1)` gives (8). At a defect the sign has square one, and the sum
of the new odd/even counts is K+1; hence the product in (9) is exactly
`-(4/3)^(K+1)`. This identity is about real increments, not an equality
between limits in two different completions.

The eventual-constancy claim is correctly scoped. Vanishing increments
force eventual alternation. At odd clocks of that tail,
`u_(j+1)-1=(3/4)(u_j-1)`. Positivity and integrality rule out an indefinitely
positive right side, so the original tail reaches 1. Conversely, once
in the standard cycle, the chosen terminal value is the actual dual, so
the backward candidate is constant. This equivalence is not used to
assert that constancy has been constructed.

## 2. The complete reduced denominator

The candidates are nonzero. The terminal value is 1 or 2; the first
inverse branch can vanish only at zero, and the second only at 1/2,
which is outside `Z[1/3]`. This justifies the use of a finite 3-adic
valuation of the numerator.

For a reduced nonintegral `u/3^r`, r>0, the two backward numerators are
`2u` and `2u-3^r`. Both are units modulo three. Thus the exponent remains
r at an original-odd inverse and increases to r+1 at an original-even
inverse. No later backward step restores integrality.

I checked the indexing of the first failure carefully. If the first
failure encountered while moving backward is at j, then `e_j=0` and the
new denominator exponent is one. Continuing backward over positions
j-1 through 0 adds one for each original-even bit. The final exponent
is therefore `1+b_j=b_(j+1)`, exactly as claimed. The number canceled
from `b_K` is the even count in the maximal final suffix whose backward
dual stays integral. If there is no failure, the final exponent is zero.
This characterization does not identify that suffix with the whole
original prefix.

## 3. The determinant does not provide an extra equation

Multiplying the boundary numerator by `3^p` and substituting
`2^K*x_K=3^p*n+C` yields equation (12), with both signs and the factor
`3^K` correct. Substituting the definition of W back into that equation
recovers the ordinary affine identity; it does not yield an independent
cancellation relation.

After their first active letters, C and D are units modulo three: an
active update is three times the old value plus a power of two, and an
inactive update leaves the value unchanged. When p differs from b,
the two summands of W have distinct 3-adic valuations, so their
difference has valuation `min(p,b)`. The qualification that both carries
have already become nonzero is retained. The additional valuation of A
required by the candidate's height budget remains unproved.

## 4. The Subspace normalization and the source-1 control

I independently checked the full three-place product. Once the first
original-even bit has occurred, D is a positive 3-unit, so `(D,3^b)` is
primitive. The archimedean factor is `D*3^b`; the 3-adic factor is
`3^(-b)`; and the remaining 2-adic factor is `|D+3^b*alpha|_2` because
`|3^b|_2=1`. Thus the product is exactly
`D*|D+3^b*alpha|_2`.

The actual complementary affine relation is
`D+3^b*alpha=2^K*Omega(x_K)`. It gives exactly equation (15), including
the residual terminal norm. The forms at each place are independent.
Their algebraicity is a separate unproved premise for a general input;
no circular rationality conclusion is accepted.

For source 1, the actual parity word is alternating. Across each two-step
block the dual carry obeys `D_(2m+2)=3*D_(2m)+2*4^m`, starting at zero.
This gives `D_(2m)=2*(4^m-3^m)`. With `Omega(1)=2`, the residual is
`2*4^m`, whose 2-adic norm is `2^(-2m-1)`. The full product is therefore
`1-(3/4)^m`, not a decaying quantity. Its primitive-vector height tends
to infinity. Every fixed negative-height-power upper bound consequently
fails eventually for this specific raw stream. This does not exclude
other choices of forms or the boundary-corrected candidate stream.

## 5. Primary statement checks and scope

Beyond the author's ledger, I opened the following sources directly:

- Monks--Yazinski, [author PDF](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf):
  inverse-parity formula, autoconjugacy identity, and Theorem 2.1. The
  equivalence for positive inputs concerns absence of divergent orbits;
  it does not prove rationality or exclude every nontrivial cycle.
- Evertse, [The p-adic Subspace Theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf):
  Theorem 1.1 and the restricted-denominator example. The first page was
  also inspected as a rendered image to verify the non-strict parameter
  inequalities and the exponent `r-n-delta`. For two forms in two
  variables this gives the negative-height-power normalization used in
  the note, with algebraic coefficients at each specified place.
- Edgington, [author preprint](https://arxiv.org/pdf/1206.0553):
  Theorem 2. Its lower even-density condition and additional periodic-
  parity condition for identifying the real limit with the 2-adic value
  are retained correctly. At m=3 its threshold exceeds the standard
  cycle's even density of one half.
- Evertse--Schlickewei--Schmidt,
  [author preprint](https://arxiv.org/pdf/math/0409604): Theorem 1.1 and
  the dependence on dimension and group rank were independently read
  during this reviewer's separate cycle attack. A growing number of
  defect terms is not a fixed-dimensional application.

The complete external proofs were not reconstructed. The earlier
finite-height certificate is an explicitly pinned dependency, not an
old theorem re-proved or recompiled in this review.

## 6. Fresh strict execution

I freshly compiled `TriadicBoundary.lean` and `TriadicBoundaryAudit.lean`
into a separate output directory using Lean 4.34.1, Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, `autoImplicit=false` and
warnings as errors. Both exited zero, and the source bytes remained
unchanged. Installed dependency objects were reused.

The audit enumerates all ten authored public theorem declarations,
matching the source inventory in order. Its outputs use only subsets of
`propext`, `Classical.choice` and `Quot.sound`. No `sorryAx`, admitted
proof, native proof shortcut or custom research axiom occurs in this
finite core. The orbit interpretation of the alternating recurrence,
all-time statements and Subspace analysis retain written-proof scope.

Evidence:

- [arithmetic-review-execution.json](arithmetic-review-execution.json)
- [arithmetic-review-compile.log](arithmetic-review-compile.log)
- [arithmetic-review-axioms.log](arithmetic-review-axioms.log)

No correction to the reviewed mathematics was required. The central
construction is still missing: one must prove enough denominator
cancellation and reduced-numerator control for at least one actual
candidate, for every fixed positive input.
