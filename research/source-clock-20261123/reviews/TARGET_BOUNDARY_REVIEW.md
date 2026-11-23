# Independent review: actual-law real boundary geometry

Reviewer lane: target descent. Date: 2026-11-23.

**Verdict: PASS within the explicitly source-qualified scope.** The reviewed
written argument proves almost-everywhere upper local dimension one for the
specified actual real boundary law, assuming its stated analytic inputs.
The four reviewed Lean statements match the finite inequalities for which
they are cited. This review does not certify the external manuscripts or
the infinite theorem in Lean.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| `research/source-clock-20261123/BOUNDARY_OVERLAP.md` | `086640abba47b80e1c6d9baee8b2e6bb003e8fd320fe5afb2cd202e7b10838c4` |
| `research/source-clock-20261123/lean/BoundaryMass.lean` | `e2ff0677e2df2f20e2fcf9376dd881787479d886349a3fadf644a92903ea48e3` |

The parent source inspected for the common-law comparison was PR #180,
`04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
`research/high-variance-20261123/ANALYTIC_GLUING.md`, including its actual
whole-path law, coherent coordinate, and bounded positive trace tilt.
The collision target was read at PR #185,
`2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
`research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`.

## 1. Mathematical checks

**Whole-cone floor.** The inverse cylinder weight `omega` satisfies both
`F(n) >= alpha*omega` and `omega*u/n >= delta`. Therefore the claimed
`u >= (alpha*delta/B)n` follows at a low-profile endpoint. This is a bound
for every ancestor in the cone. The argument does not substitute a bound
on a typical continuation.

**Tail shadow.** Applying the reciprocal estimate above this cone floor
gives the product bound used in equation (11). The identity
`a_r*n = q-R_r <= q` gives exactly the exponent `rho` in the tail scale
`D*a_r^rho`. No valuation tail moment is assumed in this step.

**Good-return subsequence.** The full-path-event quantifier in the
selection identity licenses applying reverse Fatou on the event that the
upper low-profile frequency falls short. The proof claims upper frequency
only. Choosing the latest low-profile time before each sufficiently rich
prefix yields `L_r >= theta_B*r/4` eventually along the chosen subsequence.
The two distinct short unit parents then cap every selected edge by
`1-p_B`; multiplying the original edge probabilities yields the displayed
exponential multiplier bound. No lower-frequency assertion is needed.

**Fixed-total packing.** At depth `r` and total `A`, two different legal
gap words have different odd endpoints: the deterministic forward history
from an endpoint recovers the word. Hence offsets `q-a*n` differ by at
least `2a`. A cell of width `t` can receive the boundary images of at most
`t/a+1` retained prefixes, because their offsets must lie in an interval of
length `2t`. Each such prefix keeps its actual mass at most `Ba/F(q)`.
This proves equation (17). The probability law is not changed to a
uniform distribution over endpoints.

**Heavy cells.** The enlarged closed intervals used in equation (18)
overlap at most four times, including their endpoints. Their total
reference mass is therefore at most four, for any fixed probability
measure `eta`. Together with (17), this gives the stated factor
`8B/F(q)`. The independence of the choice of `eta` from the sampled path
is stated at the correct point.

**Summing totals and local dimension.** The sum over all large enough
totals is geometric, with ratio `2^(-rho*(1-s))`. Its leading term is at
most `exp(-c*r*rho*(1-s))`. Borel--Cantelli therefore applies along the
good-return depths without a cutoff on `A`. The sign of the dimension
inequality is correct: dividing `log eta(ball) <= s*log t` by the negative
`log t` yields a ratio at least `s`. The dyadic-cell proof of the universal
upper bound one is also correct for the stated bounded-support marginal.

**Countable-root transfer.** Equation (21) permits a fixed reference
measure different from the fixed-root real marginal. Applying it to the
affine pushforward of the *original* component law `mu_E` is consequently
legitimate. The conditional ordinary and trace path laws are equivalent
under the pinned comparison. Null sets may depend on the root; the roots
form a countable set, so conditioning and summing loses no mass. This
avoids a weak-limit substitution. The positive tilts used in the source
are bounded above and below, so their ball masses differ by fixed factors.

The separate nonatomicity proof in Section 6 is consistent with these
checks. Its depth-minimum `H_r` diverges because a fixed ordinary integer
cannot hit a nonperiodic root at two different depths, and there are
finitely many integers below each bound. The full-event selection identity
is essential in its final step and is explicitly retained.

## 2. Lean statement checks

This lane inspected the declarations and their proofs. It did not rerun
the compilation already performed by the parent.

| Declaration | Match to the written use |
|---|---|
| `cone_floor_of_path_term` | Correct cross-multiplied cone floor. The written application has `B > 0`, permitting division to obtain the numerical floor. |
| `selected_prefix_product` | Multiplies the actual probability bounds at the selected departures; it does not impose a replacement law. |
| `cylinder_multiplier_bound` | Uses the correct telescoping identity `a*fEnd = fRoot*product` and the positive endpoint floor to bound `a`. |
| `heavy_cell_mass` | Correct finite reference-mass budget, with independent actual and reference weights. In the written application its parameters are `K=4`, `M=(2B/F(q))*t`, and `h=t^s`. |

The Lean file does not claim to formalize endpoint separation, countable
measure sums, the external trace construction, Borel--Cantelli, or local
dimension. Its header accurately limits the formal scope.

## 3. Test against the central target

An ordinary integer root and integer finite endpoints do not make the
inverse-boundary distribution countably supported: the boundary is a limit
along infinite paths, and those paths need not form a countable set. Thus
nonatomicity or full dimension does not by itself contradict the retained
integer root.

Nor does full upper local dimension force the required collision upper
bound. The separate `COLLISION_TRANSFER.md` gives an explicit nonatomic
probability with *exact* local dimension one almost everywhere and
collision at least `c*sqrt(m)*3^(-theta*m)`. It also shows that the exact
moving-root law in PR185 retains a fixed positive mass on high-profile
forward-spine states, uniformly in its inverse clock. Those calculations
use the central law rather than a replacement source distribution.

Accordingly, this review accepts the new actual-law dimension theorem as
stated and does not infer escape exclusion from it. A same-law, same-clock
concentration estimate remains an additional theorem to prove.
