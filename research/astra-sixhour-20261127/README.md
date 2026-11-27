# Six-hour continuation: original canonical minima and physical integer constraints

**Six-hour research packet, 27 November 2026. Collatz remains open.** This packet
continues owned PR192 from `ed7a6fe30b8602407f77855ceb74ce0489ce9c10`.
The pass began at 22:45:41 UTC on 26 November, with a six-hour endpoint at
04:45:41 UTC on 27 November. The first checkpoint is retained alongside
the later original-source and actual-history results. Three concurrent GPT-6.2 Astra agents were explicitly configured
at `ultra`, with separate arithmetic, descent, and transport assignments.
The coordinating agent independently reviews proofs and owns integration.

The live frontier was refreshed repeatedly, including the changed heads of
PRs 193, 195, 200, 201 and 206. Exact heads and source locations are retained in
the [initial snapshot](../../reports/astra-sixhour-20261127/FRONTIER_SNAPSHOT.json)
and [midnight snapshot](../../reports/astra-sixhour-20261127/MIDNIGHT_FRONTIER_SNAPSHOT.json),
the [01:50 snapshot](../../reports/astra-sixhour-20261127/SECOND_FRONTIER_SNAPSHOT.json),
the [03:02 snapshot](../../reports/astra-sixhour-20261127/THIRD_FRONTIER_SNAPSHOT.json),
and the [04:01 snapshot](../../reports/astra-sixhour-20261127/FINAL_FRONTIER_SNAPSHOT.json).
Those snapshots do not confer a review verdict on every file at those heads.

The [closing-status report](CLOSURE_STATUS.md) gives the attempted full-proof
route, the strongest retained results, and the exact implications still open.
The [final verification report](../../reports/astra-sixhour-20261127/FINAL_VERIFICATION.md)
identifies the immutable replay and its scope.

## Main mathematical results

Use the shortcut map `T(n)=n/2` for even `n` and `(3n+1)/2` for odd `n`.
On positive odd integers, `S(n)=(3n+1)/2^e(n)` removes the entire even coast.
Unless a note explicitly says otherwise, every source and endpoint is an
ordinary positive integer, and every valuation is its actual valuation.

| Result | Statement and evidence | Remaining boundary |
|---|---|---|
| [Four-phase relations from one actual cycle](arithmetic/HISTORY_TRADES.md) | Under the stated bounded-branch and quoted logarithm-ratio inputs, unequal past and future windows force at least `p-ceil(p^(199/200))` independent four-phase identities. A refined construction gives one sublinear retained set of earlier ranks and a large-area rectangle for every other rank. The identities hold throughout the same actual bilateral windows. | The finite-window relation space has not been shown invariant under all shifts. Its additive reconstruction does not produce a smaller physical ancestor. |
| [The original canonical minimum](descent/ORIGINAL_CANONICAL_FLOOR.md) | In the bounded alternative, the original least bad `z ≡ 17 mod 48` with good triple is the least bad integer in that class outright. A Lean-checked orientation theorem applies to every `y ≡ 1 mod 16` in an explicit interval, including off-cycle sources. The original source also gives the least bad `10 mod 27` row value. | A smaller canonical ancestor would now suffice by itself. The proof does not establish one. Any off-cycle return from the distinguished cycle must first cross the original ceiling. |
| [Every gap of the same actual upper](descent/ORIGINAL_UPPER_GAPS.md) | The original certificate reduces to a good `a` beside the bad `2a+1`. If the lower odd states stay below `8s` until the actual upper endpoint, an explicit iterated-exponential recursion bounds the protected floor at each fixed upper odd rank. Arbitrary fixed peak ratios also admit fixed-rank bounds. | The upper odd rank is unbounded. Off-cycle originals may make larger lower excursions. Exact ordinary controls exhibit sign recovery after real upper overshoots. |
| [All-depth inverse-floor tests](transport/ORIGINAL_FLOOR_SIEVE.md) | A countable-cylinder argument gives ternary density-one survivors of all the specified fixed-word floor comparisons. An actual-source version forces inverse depth growing logarithmically with ternary precision. The ordinary source 353 gives exact global predecessor minima, certified in Lean. | The good controls are not bad sources. Native-cycle constraints and further forward motion are additional information. The result limits these particular inverse tests rather than excluding a counterexample. |
| [Ordinary inverse rows at the same source](transport/PARENT_ROWS.md) | Each row of binary cost `n` contains one representative of every odd residue modulo `2^n`, and a whole ordinary integer interval. The limiting real window is a one-fold integer tile of measure one. On an escaping component only polynomially many row endpoints can return to the original odd grade, compared with `2^(n-1)` total endpoints. | Row convergence requires existence of the indicated arithmetic mean. Positive component returns at other grades do not yet pay for a smaller original source. |
| [Every individual full-mask moment](synthesis/FULL_MASK_MOMENTS.md) | Exact 512-letter population and pair-collision certificates, combined with the earlier upper population certificate, give a source-cost boundary above one third for every fixed real absolute moment `q>1` in the full three-layer mask. A separate agent reconstructed the proof; Lean checks the rational joining inequalities. | This rules out that unweighted individual-norm estimate. Joint common-frequency products and genuinely smaller source families remain available. The new external fifth-moment result for a smaller strip is compatible with this boundary. |
| [Physical strips forced by an escape](transport/UNIT_STRIPS.md) and [common correction gaps](transport/GLOBAL_CORRECTION_GAPS.md) | Under the named inverse-law and singularity inputs, one fixed ordinary escape forces arbitrarily long intervals with large mass in every unit subinterval at actual later targets. All simple positive paths share a compact null correction set. | The forced centres can lie in that null set. The required upper bound at those actual centres is unproved; stationary averaged estimates do not supply it. |
| [Complete denominator with unbounded markers](arithmetic/SHARED_BACKGROUND.md) | For a fixed number of repetitions of one ordered background, separated by unequal positive markers, the full reduced denominator grows at least as `2^((2-log₂3-o(1))k)`. Background and marker exponents may grow independently. The half-turn rate improves to `2^((1-o(1))k)`. Written proof using an external multivariable gcd theorem; exact finite interfaces in Lean. | The number of background copies is fixed. The threshold is ineffective. This does not exclude unrestricted integer cycles. |
| [All-shift denominator bound](arithmetic/SHIFT_DENOMINATORS.md) | The positive-center comparison controls the complete denominator at every shift order, and also compares distinct positive rational cycles with different grades. Published cycle and range bounds give at least 42 mismatches at every nontrivial shift of an integer cycle. | A complex word can still have denominator one; the theorem is a necessary restriction. The published large computations are imported. |
| [Marked ordinary inverse trace](transport/MARKED_TRACE.md) | The full critical inverse measure at each fixed ordinary unit target has asymptotically independent geometric initial gaps. A direct application of Paper 48/v2 retains a positive fraction of the odd depth, with an unevaluated absolute fraction. The original logarithmic-horizon proof uses an exact geometric deconvolution. | The target is fixed in the first limit. Moving-target conclusions retain an explicit past-grade condition. Imported mixing and shell estimates are analytic inputs, not Lean theorems in this packet. |
| [Every fixed paired target](transport/POINTWISE_CRITICAL.md) and [its marked improvement](transport/MARKED_TRACE.md) | Every individual synchronized paired grade layer tends to zero as its grade tends to infinity, with all positive ancestors included. A complementary estimate controls large ordinary targets with a good upper arm. Together they give `c₀` on the indicated target/grade set. | Individual-layer convergence does not establish convergence or smallness of the sum over all grades. |
| [Unrestricted upper-word reduction](descent/UPPER_WORDS.md) and [distortion](descent/DISTORTION.md) | Every actual upper certificate admits a full physical signed reduction after explicitly paid cycle laps. On simple high paths an exact occupancy certificate gives correction below `6/5`, eliminating the padding for the stated application. | The integer signed exit can be negative. Its magnitude and binary reserve do not force a smaller positive canonical source. |
| [All-rank paired interval compression](descent/PAIRED_INTERVALS.md) | In every translated interval, all but `Oε(N^(H₂(log₃2)+ε))` members of any canonical subset have an earlier member whose two arms have actual counted mergers by a prescribed logarithmic clock. | The exceptional set may contain the specified least defect. |

The written proof reviews, external input boundaries and independent
reconstructions are recorded in [the root review ledger](../../reports/astra-sixhour-20261127/ROOT_REVIEW.md).
A Lean kernel checks exactly its displayed finite identities and implications;
it does not certify the surrounding imported analysis.

Additional source-specific results include [integral small filters](arithmetic/SMALL_FILTER.md),
[actual rank spacing](arithmetic/RANK_SPACING.md), and recovery across
[finitely many missing physical blocks](arithmetic/PUNCTURED_WINDOWS.md).
The filters preserve the complete odd denominator, but do not automatically
preserve the actual Collatz branch. The spacing estimate holds at the one
actual scale while its exceptional-scale measure estimate is only metric.
The missing-block theorem retains integer endpoints and separated valuation
bands, using an external Subspace Theorem with an ineffective onset.

## Direct closure investigations

The central target remains a proof about the original least hypothetical
counterexample. The previously established canonical reduction leaves a
source `z ≡ 17 mod 48` whose upper `3z` reaches one. The new work has not
proved that its lower `z` also reaches one. Equivalently, an architecture
that separates the alternatives must exclude both positive escape and every
nontrivial positive integer cycle.

The [original signed current](transport/ORIGINAL_CURRENT.md) now identifies
the very first negative parent row and the exact good/bad split at
`p=(z+3)/4`. A positive fraction of the distinguished cycle supplies a
reciprocal-weight deficit of order its period divided by its minimum.
The exact accounting retains a nonnegative flux through the height boundary.
Neither that flux nor the later current has been bounded tightly enough
to contradict the deficit.
The [residual measure](transport/RESIDUAL_CURRENT.md) retains one ordinary
component in an exact two-dilation balance. Its fixed-grade measures remain
singular while averages over many grades approach Haar measure; separate
dilation invariance does not follow.

The transport attack now retains an entire ordinary escaping component,
its integer grade and its corrected height. [Ordinary translations](transport/ORDINARY_TRANSLATES.md)
give vanishing one-step errors but prove that the corresponding cumulative
loss would be nonsummable. [The smaller-parent analysis](transport/GRADE_PARENT.md)
uses a strictly smaller ordinary parent, describes the fixed-grade real
distortion spectrum, and isolates the required physical obstruction.
These are conditional restrictions on an actual escaping component. No
moving finite witnesses are identified with a fixed ordinary counterexample.

The arithmetic attack keeps the complete reduced denominator throughout.
[Prime-to-six flows](arithmetic/CORE_FLOWS.md) expose the exact branch lock
that a positive connected flow can miss. The shared-background theorem
handles all exceptional translated subtori in its stated fixed-dimensional
family. The remaining unrestricted denominator-one case has not been
reduced to that family.

The [full physical strip transfer](arithmetic/PHYSICAL_STRIP_TRANSFER.md)
gives `p ≤ C_theta s^theta` for every `theta>23/60` in the bounded
least-disagreement branch, with its finite energy certificate independently
replayed at the first checkpoint. This remains above the one-third
threshold associated with the explicitly quoted irrationality input.

The descent attack uses the actual upper certificate, the original lower
floor, and both transported orbit labels. [Paired charge](descent/PAIRED_CHARGE.md)
gives a complete contextual criterion at convergent controls; its
construction cannot be applied to a bad lower without supplying the
missing access to one. [Cut-walk depth](descent/CUT_WALK_DEPTH.md) shows that
even fixed-rank good controls can require unbounded original-cut walks.
The live search is therefore not restricted to any fixed finite word bank.
The [first distortion record](descent/DISTORTION_RECORDS.md) yields a
strict half-unit comparison with an integral merger criterion, while the
late-record controls expose a genuine source-height loss.
[Two physical lap classes](descent/TWO_LAP_CLASSES.md) remove an upper-clock
budget from a counted two-arm completion theorem, but its smaller partners
need not be canonical. None of these qualifications replaces the original
minimum by a more convenient one.

## Controls that changed the direction of the search

- [Biased Hellinger decay](transport/HELLINGER.md) and [hold pinning](transport/HOLD_PINNING.md)
  control a two-path affinity. Mass present on only one side contributes
  zero affinity, so the estimates cannot be used as a one-arm loss bound.
- [Certified-rank tails](transport/CERTIFIED_RANK.md), [height budgets](transport/HEIGHT_BUDGET.md),
  [ordinary antichains](transport/ORDINARY_ANTICHAIN.md), and
  [fixed floors](transport/FIXED_FLOOR.md) retain the height and source
  costs of inverse steering. Those costs do not automatically cross the
  original source minimum.
- [The reciprocal departure operator](synthesis/RECIPROCAL_OPERATOR.md)
  has spectral radius `1/2` for a reason that remains valid if an escaping
  orbit exists. The displayed spectral gap therefore cannot prove Collatz.
  Its finite product and invariance corrections are checked in Lean.

## Reproducibility

The [replay driver](../../reports/astra-sixhour-20261127/replay.py) requires
a clean complete checkout and a new object directory outside that checkout.
It rebuilds every new Lean module and the imported project module `Portal`,
uses warnings as errors and disables automatic implicit variables, and
checks every public theorem's transitive axiom inventory against
`propext`, `Classical.choice`, and `Quot.sound`.
It rejects unchecked proof tokens and runs the declared exact Python
controls with and without optimization, comparing their complete outputs
and each complete retained JSON payload.
The repository regression validator is a separate integrity gate.

The pinned environment is Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
The driver compares fresh dependency sources with the cached dependency
source tree before reusing dependency objects. Every project object is
rebuilt. Final replay receipts identify the exact source commit and tree;
agent-local receipts are preliminary evidence only.
