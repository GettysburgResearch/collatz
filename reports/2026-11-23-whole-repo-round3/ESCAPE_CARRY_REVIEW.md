# Independent review: complete carries and actual source boxes

Reviewer: `source_surgery` (separate from the author, `escape_rigidity`).
Date: 2026-11-23.

**Verdict: VERIFIED in the finite and explicitly conditional written
scope below.** No critical collision upper, harmonic-flow construction,
or Collatz closure is certified by this review.

## Exact reviewed bytes

| File | SHA-256 |
|---|---|
| `research/whole-repo-round3-20261123/CarryFibers.lean` | `9fd194724b6c2c101bfe837dcd198199f4618911c7cf608ff425c8bac31818e3` |
| `research/whole-repo-round3-20261123/ACTUAL_COLLISION.md` | `eb8a352d3ad072e601637c0d2beff2992317252ff4ca58b830100074a1b17709` |
| Imported `research/high-variance-20261123/CycleWordAlgebra.lean` | `fc42bf2a602592c7f7ebbe42ca3c21bb96b58f7ce2dc93aed2cafdbac47f984e` |

I read the complete sixteen-declaration module and the complete written
note, reconstructed their arithmetic, and checked that the inherited
chronological carry definition agrees with the actual odd-gap encoding.
Development compilation was reported separately by the author. Fresh
compiler replay and declaration-dependency auditing belong to the
parent checkpoint; this report does not substitute source inspection
for those execution receipts.

## 1. Full-carry decoding and both clocks

The imported recursion is

`C_(b::w)=3^(ones w)*b+2*C_w`.

Modulo two, the carry determines the first bit. The supplied equal
total odd counts then determine the same remaining odd count on both
sides. Subtracting the identical leading term and cancelling two
recovers the remaining carry. Induction on the common length therefore
recovers the whole word.

Both clock hypotheses are retained. In particular the module does not
silently infer the word length from a carry: trailing zeroes can leave
that carry unchanged. The endpoint consumer uses the full chronological
identity `2^A*q=3^m*p+C_w`, including the original ordinary source.

The quotient/remainder lemmas recover the complete carry exactly.
For quotients in a translated interval `[b,b+R)`, subtraction of `b`
produces an injection into `range R`; the lower bound is retained,
so natural-number subtraction does not erase a distinction. Arbitrary
large interval offsets are permitted. The zero-modulus edge cases of
the generic quotient lemmas cause no incorrect division inference;
the residue-sum theorem separately requires a positive modulus.

## 2. The actual source quotient removes repeated occurrences

At fixed `A,m`, two equal endpoint residues modulo `3^m` give equal
carry residues. Equal carry quotients therefore give equal complete
carries and equal words. Subtracting the two full affine identities
gives

`2^A*(q-q')=3^m*(p-p')`.

Coprimality of the two powers forces equal source residues modulo
`2^A`. Equal source quotients then give `p=p'`, and cancellation of
the positive factor `2^A` gives `q=q'`.

This proves the written source-box claim with **one fixed odd count
`m`**, as well as the three stored values `(A, carry quotient, source
quotient)`. On one injective ordinary orbit, equality of sources implies
equality of occurrence indices. The Lean statement proves equality of
the words and both values from explicit finite identities; orbit
injectivity and the occurrence interpretation are correctly left in
the written application.

The interval-width extension is also valid. Sources of one repeated
word are separated by a multiple of `2^A`, hence an interval of width
`H` contains at most `1+floor(H/2^A)` of them. This count concerns the
original sources and does not replace their interval by an endpoint
height bound.

## 3. Weighted collision accounting

For the written application, endpoints are distinct ordinary points and
the occurrence weights are nonnegative. Combining the weights of each
repeated word gives the exact identity

`sum_w p_w^2 = sum_j t_j^2 + sum_(j!=h,W_j=W_h) t_j*t_h`.

Cauchy's inequality over a residue fiber of at most `R` distinct words
gives the stated upper bound. In an exact carry-quotient channel, the
residue map on distinct words is injective, so the collision is exactly
the diagonal plus the repeated-word term. In a full source box the
occurrence map is injective, so only the ordinary diagonal remains.

The Lean weighted statements are valid for arbitrary ordered-field
weights: their Cauchy bounds use squares and do not silently assume a
probability law. The probabilistic interpretation in the note separately
retains nonnegative weights and the actual submeasure.

Every occurrence of one word has the same endpoint residue, since
`2^A` is invertible modulo `3^m`. Thus selecting any one occurrence as
the source/endpoint representative in the finite distinct-word theorem
does not change the residue projection of its combined original weight.

The wider source-interval estimate uses `t_j<=1/N` correctly: each
combined word mass is at most its multiplicity divided by `N`, giving
`sum p_w^2 <= (multiplicity/N)*sum p_w`.

Most importantly, the complete law is aggregated with the Euclidean
triangle inequality. Equations (20)--(21) square the **sum of the group
norm bounds** and retain every cross-group term. The note does not
replace this by a sum of squared bounds or assume independent boxes.
Thus the new finite injection does not smuggle in the missing global
collision estimate.

## 4. Physical carry width

For each actual prefix, multiplying the exact odd-step identities gives

`2^a_i/3^i = p/(x_i*product_(h<i)(3*x_h/(3*x_h+1)))`.

Each product factor belongs to `(0,1)`, so the prefix product is at
least the supplied complete finite product `kappa`. With
`B=max_i p/x_i`, every summand is bounded by `B/kappa`.
The complete carry divided by `3^m` is exactly one third of the sum
of these prefix coefficients. This proves (18), including its initial
term. The resulting quotient interval has the stated width.

This is a finite, actual-path estimate. The optional common infinite
product floor remains source-qualified; no new ordinary least-root
property or fresh distribution is assumed in the finite calculation.

## 5. Exact law and the ordinary diagonal

Conditional on the explicitly retained positive harmonic flow and its
finite limiting spine value, the displayed law identities reconstruct.
An endpoint has exactly one forward image at a fixed odd clock. Hence
the inverse supports of the distinct roots are disjoint, the spine atom
is exactly `v_j/(N*v_(r+j))`, and every ordinary atom is at most `1/N`.

The retained spine atoms give `D>=c_0^2/N`; normalization and the maximum
atom give `D<=1/N`. The selected endpoint submeasure uses its original
weights. Its positive remainder includes all omitted early windows and
all inverse branches, with the stated mass bound. Bounding its residue
vector norm by that mass is valid.

The final rate-free remainder paragraph explicitly retains the whole
available window `I={m,...,M}`. At fixed precision its omitted early
mass is at most `m/N`, which vanishes together with `eta_M`. Additional
trimming still pays its omitted original mass. This scope clarification
was requested by the separate cycle reviewer and is included in the
final reviewed bytes.

I also fetched PR185 at `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
`research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`, blob
`803d6ba2a3827c6ef94cb31fb838e3d416b92090`, to check the exact imported
critical exponent and precision range against Theorem 3. The note
retains its fixed-source, fixed-flow dependencies and all finite
inverse clocks. This source comparison does not certify the separate
construction of that harmonic flow.

For a full collision upper `o(sqrt(m)*3^(-theta*m))`, the diagonal lower
bound forces

`N*sqrt(m)/3^(theta*m) -> infinity`.

The final note uses little-omega for the equivalent growth statement.
The earlier notation `N >> 3^(theta*m)/sqrt(m)` was corrected because
standard Vinogradov notation would express only a constant-factor
lower bound. No substantive theorem required a change.

## 6. Remaining boundary

The finite core and the written implications above pass. They do not
control the number, masses, or residue alignment of source boxes occupied
by the same long trajectory. The inherited flow, its analytic existence,
the all-clock critical lower bound, and the missing upper comparison
remain separately scoped. No finite execution range, weighted identity,
or within-box injection is promoted to escape exclusion or universal
convergence.
