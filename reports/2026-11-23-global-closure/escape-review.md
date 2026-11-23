# Independent review of the retained-source pressure/collision attack

Reviewer: `closure_dual`. Date: 2026-11-23.

**Verdict: VERIFIED for the new written deductions in their stated scope,
and VERIFIED for the finite Lean declarations and exact common-source
control.** The inherited harmonic-flow construction remains
SOURCE-QUALIFIED. The required same-law upper collision estimate, escape
exclusion, and full Collatz remain OPEN. This review does not promote the
pressure-law upper bound into an upper bound for the actual time law.

## Exact reviewed snapshot

| File | SHA-256 |
|---|---|
| `research/global-closure-20261123/escape/PRESSURE_COLLISION_ATTACK.md` | `cad066fc49bf987f198e9c1ad3098f05f2575d6f7cb74efa91e1c4483523c8be` |
| `research/global-closure-20261123/escape/README.md` | `f5f2438551fb6bc7a1aba907330cc88e6fcdbb7a4be0aab9c605630141ba77cf` |
| `research/global-closure-20261123/escape/SOURCES.json` | `db7116f866f0e9724e6cc491bd7248de9a9898ac2916737b0f32ee81a849fd2b` |
| `research/global-closure-20261123/escape/lean/PressureCollisionCore.lean` | `a75ca7c479c687b0a4a6c1c3c86979043d7f57111c6372b38162bdf61e5bd3c0` |
| `research/global-closure-20261123/escape/lean/PressureCollisionAudit.lean` | `0aa261103ca7863f397af4a41050088cfb597aa8f624319bae75e6c562486acc` |
| `reports/2026-11-23-global-closure/escape-lean-build.json` | `7d281768089451b990a5885302a954e81d53a47b74763b9f50ddcaeb20882c1f` |
| `reports/2026-11-23-global-closure/escape-lean-audit.log` | `7fdeb7b8e5488f19340b304fc487c31f5dca6ba993fc03ac15f2b79166cbf2a7` |

The review covers these bytes, not an unpinned later revision.

## Independent reconstruction

### 1. Ordinary arithmetic pressure upper

For a positive atomic measure with weights at most `n^(-s)`, `s>1`,
every unequal congruent pair has exactly one representation as the two
orders of `(n,n+lQ)`, with `n,l>=1`. Nonnegativity permits Tonelli, and
`n+lQ>=lQ` bounds the two sums by the product of their convergent zeta
series. This proves the exact constant `2 zeta(s)^2 Q^(-s)` in (6).
Dividing by the square of the actual total mass gives the normalized
version. The ordinary diagonal remains positive and must not be dropped
from the full collision functional. The sharpness control is correctly
restricted to general measures satisfying the atom envelope, not asserted
for every escaping Collatz component.

### 2. Retained-source atoms and density norms

The input law is the literal average of `K^r(q_(r+j),.)`. Determinism of
`U^r` and distinctness of the escaping orbit imply that the atom at `q_j`
comes from exactly its own root `q_(r+j)`. Its mass is
`v_j/(N v_(r+j))`, uniformly at least `c0/N`. No changing source or
stationary replacement enters this calculation.

For the normalized pressure measure, its atom at `q_j` is at most
`1/(S_s q_j^s)`. Multiplying the retained lower mass with that inverse
atom yields (8) and (10). Raising the exact density integral to its
`L^p` form gives the sum of `q_j^[s(p-1)]`. Sorting the `N` distinct
positive integers bounds that sum below by
`N^[s(p-1)+1]/[s(p-1)+1]`. The resulting exponent is exactly
`(s-1)(p-1)`. Infinite norms are allowed and cause no undefined
subtraction.

For (11), the constant term `log(c0 S_s/N)` is eventually negative;
the total retained mass is at most one, so its contribution is bounded
below by that constant itself. On the tail `j>=a`, the sharper lower
mass `c_a/N` multiplies the nonnegative `s log q_j`. Sorting this tail
produces `log((N-a)!)`. The omitted part of the entropy integral is at
least `-1/e`, since the reference measure is a probability and
`t log t>=-1/e`. For each fixed `a`, the resulting coefficient is
`s c_a-1`; then `a` tends to infinity and `c_a` to one. All inequalities
are independent of the inverse clock, justifying the displayed infimum
over that clock. This is not an entropy-continuity argument.

### 3. Critical comparison cost

The imported running-height statement is a bound for every injective
ordinary segment, not a resampled mean. Combining it with (10) yields
`D^2 >= c N^(2s/theta-2) (log N)^(s/theta)`. A critical *full*
collision upper must pay its ordinary diagonal, which is at least
`c0^2/N`; hence it can only be used where `Q<=C N^(1/theta)`.
Because `theta-s<0`, substituting the largest allowed `Q` into
`D^2 Q^(theta-s)` gives the lower bound in (15), with exponent
`s/theta-1>0`.

I also independently reconstructed the coordinating root agent's
subsequent sharpening (12a). Write an unequal congruent pair as
`(n,n+lQ)`. Only the larger atom needs its pointwise envelope
`D/[S_s(n+lQ)^s]`; the outer smaller-atom probabilities sum to one.
Tonelli therefore gives `B_lin=2 zeta(s) D Q^(-s)/S_s`, with one
rather than two density factors. The retained-height lower bound on `D`
and the same scale constraint make all powers of `N` cancel, leaving
`B_lin/Q^(-theta) >= c_(s,A) (log N)^[s/(2 theta)]` for fixed `s>1`.
The fresh logarithmic height gain is essential for this divergence.

The claimed uniformity when the pressure exponent varies is also valid.
Before introducing an `s`-dependent constant, the exact lower bound is
`2 c0 zeta(s) C_A^theta [(c_H/C_A)(log N)^(1/(2 theta))]^s`.
Here `S_s` has canceled, and `c0,c_H,C_A` do not depend on `s`. Once the
bracket is at least one, `zeta(s)>=1` and `s>1` bound this below by
`2 c0 c_H C_A^(theta-1) (log N)^(1/(2 theta))`. This works uniformly
for every `s>1`, including choices approaching one with `N`. Infinite
maximum densities give no finite comparison to begin with.

These are lower bounds on the particular proposed **comparison bounds**
`B` and `B_lin`, not on actual unequal-atom collisions. The note makes
this restriction explicit. They exclude those global maximum-density
transfers; they do not exclude every pressure argument or establish an
upper estimate for the actual retained law.

At review suggestion, the final note also records the elementary diagonal
upper: the distinct roots `q_(r+j)` have disjoint `r`-preimage supports,
so every atom of their uniform mixture is at most `1/N`, and its
ordinary diagonal is at most `1/N`. Thus a sufficiently strong
unequal-atom upper can be combined with this diagonal at the stated
critical scales. This observation does not supply the missing unequal-
atom estimate.

### 4. Actual-word ambiguity and repeated-word scope

The two lists are exact consecutive windows on the single accelerated
orbit from 41. In particular `377 -> 283` has exact gap 2 and
`2429 -> 911` has exact gap 3; both endpoints 425 and 911 are 20 modulo
81. The totals 5 and 6 are below the four-step critical budget because
`2^6<3^4`. All states and the entire common-source prefix are included
in the formal certificate.

For the all-length family, iterating a gap-one edge gives
`F_1^j(x)=(3/2)^j(x+1)-1`. Appending gaps `(2,1)` or `3` yields the two
formulas (16), including the shared constant `-1/4`. Integrality implies
the same endpoint residue modulo the entire `3^m`. Both totals are
critical for `m>=4`. This disproves the attempted inversion from endpoint
residue to past word; it does not assert a spurious repeated orbit.

For an actual consecutive repetition of one affine block, the displacement
`D x-B` is multiplied by `3^m/2^A` at each repeat. The exact finite
integer telescope and coprime cancellation give (17). The note correctly
credits the older arithmetic packet for this mathematical result, and
retains the supplied repeated-edge hypotheses in its new finite Lean
consumer.

## Source boundaries checked

I independently opened the following exact upstream files, beyond reading
the author's source ledger:

- PR185 `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
  `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`:
  the ordinary law, exact retained masses, critical collision lower bound,
  and running-height theorem. The inversion from its bounded-duration
  inequality gives the height exponents used in (13).
- PR177 `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
  `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`:
  the ordinary component measure, positive path product, atom envelope,
  exact conformal identity and Green-integrability boundary.

The new deductions use the pressure atom envelope and positivity, and the
source-qualified positive bounded flow with its retained-source identity.
This review does not certify every analytic dependency in the historical
flow construction. The claims concerning other peer lanes remain
attributed context, not newly imported closure hypotheses.

## Independent execution

I freshly compiled the core and audit to a separate external output
directory with Lean 4.34.1, the pinned Mathlib objects, `autoImplicit=false`
and warnings as errors. Both returned zero, and the audit output matches
the author's recorded SHA-256. The source hashes match the receipt.

[escape-review-execution.json](escape-review-execution.json) records the
new commands and exit codes;
[escape-review-lean.log](escape-review-lean.log) records the actual outputs.
The ten public theorem audits contain only `propext`, `Classical.choice`
and `Quot.sound`. The finite list controls use kernel `decide`, not a
native proof shortcut. Infinite sums, real-power estimates, KL asymptotics,
and (15)--(15b) remain written proofs rather than Lean claims.

No mathematical repair was required. The ordinary diagonal upper bound
was added at review suggestion, and the coordinating root agent's
linear-density and varying-parameter strengthenings were independently
reconstructed before the final scientific snapshot recorded above. The
remaining arithmetic task is the same-law bilinear estimate identified
in the note; neither this review nor the successful finite compilation
establishes it.
