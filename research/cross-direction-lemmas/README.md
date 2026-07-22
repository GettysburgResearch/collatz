# Cross-direction arithmetic lemmas

**Agent:** `gpt56-synthesis-01`  
**Issue:** [#29](https://github.com/gfreund123/collatz/issues/29)  
**Branch:** `agent/gpt56-synthesis-01/29-cross-direction-lemmas`  
**Namespace:** provisional `98xx`  
**Status:** active proof packet; no counterexample claimed

## Purpose

Several active programs reach the same arithmetic boundary in different
notation:

- finite directives select nested congruence cylinders;
- the cylinders determine a unique completion point;
- low digits can be propagated by exact Hensel laws;
- but a Collatz counterexample needs one ordinary positive integer, not only a
  compatible completion point.

This packet collects small, self-contained lemmas that can be reused across
those programs. It does not import another branch's confidence as a proof.
Every branch-qualified source claim is reconstructed or explicitly left as a
dependency.

## Wave reports

- [`initial forge`](../../reports/gpt56-synthesis-01/2026-07-21-29-cross-direction-lemma-forge.md)
- [`wave two`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-two.md)
- [`wave three`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-three.md)
- [`wave four`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-four.md)
- [`wave five`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-five.md)
- [`wave six`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-six.md)
- [`period-four quotient checkpoint`](../../reports/gpt56-synthesis-01/2026-07-22-29-period-four-quotient-checkpoint.md)
- [`wave eight`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-eight.md)
- [`wave nine`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-nine.md)
- [`wave ten`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-ten.md)
- [`wave eleven`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-eleven.md)
- [`wave twelve`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-twelve.md)
- [`wave thirteen`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-thirteen.md)
- [`wave fourteen`](../../reports/gpt56-synthesis-01/2026-07-22-29-cross-direction-wave-fourteen.md)

## Result map

| Result | Lane | What it contributes |
|---|---|---|
| [`L-9801`](claims/L-9801-nested-cylinder-stabilization.md) | all completion/cylinder programs | An inverse-limit point is an ordinary nonnegative integer exactly when its canonical representatives eventually stabilize. |
| [`L-9802`](claims/L-9802-dyadic-logarithmic-bulk.md) | PR #3 collision/Hensel stack | Exact quadratic lift recurrence, exact odometer valuations, and the normalized 2-adic logarithmic limit for every odd base. |
| [`L-9803`](claims/L-9803-completion-height-wedge.md) | PR #16 and PR #20 | One elementary product-formula wedge explains the reciprocal slopes in zero-carry and repetition rigidity. |
| [`L-9804`](claims/L-9804-active-cylinder-digit-recurrence.md) | PR #20 active tower | Exact forward mixed-radix digit and terminal-state recurrence, including automatic positive-cone propagation. |
| [`L-9805`](claims/L-9805-zero-tail-escape.md) | PR #20 active tower | Eventual zero digits force a deterministic valuation orbit and terminal height `2^(Theta(K^2))`; any polynomial-height bound would rule them out. |
| [`R-9801`](claims/R-9801-finite-crt-orthogonality.md) | PR #16/PR #20 bridge | Finite sparse reciprocal carries cannot force an itinerary repeat of logarithmic length, even with one positive primitive integer; a global stabilization hypothesis is essential. |
| [`L-9806`](claims/L-9806-simultaneous-cylinder-recurrence.md) | PR #16/PR #20 diagonal | Exact base-`5184` cylinder digits. For a stabilized positive integer the reciprocal tail is nonzero and 4-periodic, so the combined CRT digit—not the reciprocal digit—is the correct target. |
| [`L-9807`](claims/L-9807-h-first-crossing-reduction.md) | PR #19 H frontier | Reduces the unresolved first expanding-to-contracting crossing to one sharp carry inequality. It does not claim the inequality. |
| [`R-9802`](claims/R-9802-h-carry-rectangle-insufficiency.md) | PR #19 H frontier | Exact abstract countermodel proving that canonical ranges and carry rectangles alone cannot establish the missing H sign. |
| [`L-9808`](claims/L-9808-finite-geometric-bulk-compiler.md) | PR #3 collision/Hensel stack | Compiles every finite inverse-bulk prefix as an explicit geometric polynomial in the positive ordinary bulk, with exact error valuation and minimal depth. |
| [`L-9809`](claims/L-9809-transcendental-bulk-complexity.md) | PR #3 collision/Hensel stack | Mahler's theorem makes the completed logarithmic bulk transcendental; its binary word is nonperiodic and has factor complexity at least `n+1`. |
| [`L-9810`](claims/L-9810-transcendental-counter-address.md) | PR #3 padding counters | An algebraic exponential counter isometry cannot assign a rational 2-adic address to that target; the finite address prefixes are nonperiodic. |
| [`L-9811`](claims/L-9811-isometric-compiler-transport.md) | PR #3 padding counters | Transports finite bulk compilers through counter isometries without precision loss and proves an exact one-bit-per-scale odometer law. |
| [`L-9812`](claims/L-9812-minimum-root-renewal.md) | PR #16 survivor roots | Characterizes plateaus and renewals of the minimum finite survivor by one endpoint residue and one base-`5184` extension digit. |
| [`L-9813`](claims/L-9813-h-offset-barrier-families.md) | PR #19 H frontier | Uses exact ordered offsets to certify strict displacement for positive-density infinite families of genuine first crossings. |
| [`L-9814`](claims/L-9814-h-fixed-suffix-compiler.md) | PR #19 H frontier | Two fixed suffixes, and no single suffix, optimally compile every multiplier phase into a strict first crossing with a uniform margin. |
| [`R-9803`](claims/R-9803-h-finite-return-obstruction.md) | PR #19 H frontier | Proves that post-crossing renormalization retains an unbounded 2-adic tail; phase-only or bounded-carry closure cannot iterate the suffix compiler. |
| [`L-9815`](claims/L-9815-cylinder-successor-gap.md) | PR #16 survivor roots | Defines the exact next surviving cylinder and gives its plateau/renewal law; an internal exact replay extends the minimum root through depth 48. |
| [`L-9816`](claims/L-9816-pade-cyclotomic-gcd.md) | PR #20 Padé lane | Finds exact diagonal and growing cyclotomic common factors, then proves that the full automatic factor sector still falls short of the period-four threshold. |
| [`L-9817`](claims/L-9817-padding-transition-log-compiler.md) | PR #3 padding counters | Gives an exactly valued finite logarithmic compiler for one padding-address scale transition in every physical chart. |
| [`L-9818`](claims/L-9818-synchronizing-successor-gap.md) | PR #12/PR #16 bridge | A bounded synchronizing padded-cylinder router would force exponential successor gaps; regular sanctuary acceptors do not by themselves provide such a router. |
| [`L-9819`](claims/L-9819-two-orbit-successor-rigidity.md) | PR #16 survivor roots | Quantifies how aligned blocks or small Hamming distance between two directive words force exponentially large ordinary separation. |
| [`L-9820`](claims/L-9820-padding-address-quotient-bit.md) | PR #3 padding counters | Recovers the previously missing scale-boundary address bit as one explicit ordinary quotient parity, with no inverse-permutation oracle. |
| [`R-9804`](claims/R-9804-inverse-cylinder-zero-reset-obstruction.md) | PR #12/PR #16 bridge | Constructs the exact base-64 digit/carry transduction, proves its reachable carry set has size `2^n`, and rules out any global zero-reset exact router. |
| [`L-9821`](claims/L-9821-cap-cusp-localization.md) | PR #33/PR #3 cap-chain bridge | Propagates completion height to every head, triple, and terminal input; every hypothetical cap chain forces all 84 canonical triple inputs below square-root cylinder height. |
| [`L-9822`](claims/L-9822-h-compiler-phase-rotation.md) | PR #19 H frontier | Removing the common terminal zero reveals an exact irrational phase rotation with Sturmian branch coding; the actual completed suffix remains contracting. |
| [`L-9823`](claims/L-9823-invariant-component-natural-boundary.md) | PR #6 invariant components | Every eventually periodic finite component coloring is constant; every nonconstant integer coloring has a natural-boundary generating series. |
| [`L-9824`](claims/L-9824-h-phase-fiber-drift.md) | PR #19 H frontier | The renormalized H affine skew product has exact positive fiber drift, preserved fiber differences, and pointwise zero Lyapunov exponent. |
| [`L-9825`](claims/L-9825-central-ternary-kernel-reduction.md) | PR #6 invariant components | Binary automaticity makes the central ternary-dilate spine finite, while an exact translated-state table isolates why Cobham still cannot be applied. |
| [`L-9826`](claims/L-9826-survivor-cantor-full-shift.md) | PR #16 survivor coding | The infinite survivor set is an exact dimension-`1/6` 2-adic full shift; nontrivial ordinary points are divergent and cannot have eventually periodic directives. |
| [`L-9827`](claims/L-9827-h-tail-full-shift.md) | PR #19 H frontier | Each completed compiler suffix is an exact 128- or 8192-to-1 dyadic tail shift and expands within-cylinder 2-adic distances. |
| [`L-9828`](claims/L-9828-pade-prime-power-residual-support.md) | PR #20 Padé lane | Even one exceptional copy at every eligible reduced prime-power order has only `O_G(D^(3/2))` total degree; the dyadic residual budget is globally below the deficit, conditional only at the full-gcd transfer step. |
| [`L-9829`](claims/L-9829-sturmian-tail-information-rate.md) | PR #19 H frontier | Along every forced Sturmian phase orbit, the composed tail shift consumes `kappa_* n+O(1)` bits with an exact universal discrepancy below six. |
| [`L-9830`](claims/L-9830-successor-borrow-signed-carry.md) | PR #16 survivor pairs | Once ordinary addition borrow settles, the exact successor carry difference is a signed chart iterate; future directive agreement is precisely its base-64 valuation. |
| [`L-9831`](claims/L-9831-physical-tail-tuple-uniqueness.md) | PR #19 H frontier | A single mixed-radix congruence selects exactly one physical carry tuple from the exponentially branching abstract H tail tree at every finite depth. |
| [`L-9832`](claims/L-9832-pade-prime-power-small-remainder.md) | PR #20 Padé lane | For odd reduced `p^k` with remainder `s<p`, a residual zero occurs exactly by complement antisymmetry, and its cyclotomic factor is simple. |
| [`L-9833`](claims/L-9833-h-nested-seed-nonordinary.md) | PR #19 H frontier | Every infinite nested `10/30` suffix schedule has a nonordinary 2-adic seed: eventual input stabilization would force an impossible infinite descent of positive endpoints. |
| [`L-9834`](claims/L-9834-signed-difference-full-shift.md) | PR #16 survivor pairs | Survivor-cylinder differences form an exact ternary full shift: there are `3^n` differences, additive energy is `6^n`, and every valuation stratum is explicit. |
| [`L-9835`](claims/L-9835-sturmian-zero-carry-gap.md) | PR #19 H frontier | Every zero-interface run is logarithmic in its starting endpoint; the physical Sturmian carry stream has at least logarithmically many nonzero blocks, but positive density remains open. |
| [`L-9836`](claims/L-9836-fixed-width-translated-ternary-cone.md) | PR #6 invariant components | Every fixed-width translated cone above the central ternary spine has one uniformly finite binary automaton; only unbounded coheight can obstruct Cobham. |
| [`L-9837`](claims/L-9837-h-reset-cylinder-sieve.md) | PR #19 H frontier | A future all-zero H cylinder is reachable after a nonzero reset exactly when its internal dyadic carry matches the finite reset quotient; long cylinders are cofinally excluded. |
| [`L-9838`](claims/L-9838-primitive-ternary-horizontal-cycle.md) | PR #6 invariant components | Every fixed-valuation ternary offset stratum is one exact horizontal binary-kernel cycle, reducing full-kernel testing to one offset-one representative per width. |
| [`L-9839`](claims/L-9839-pade-dyadic-residual-envelope.md) | PR #20 Padé lane | Forced lower dyadic factors halve every actual power-of-two residual budget and give the sharp envelope `D^2/27`; an exact even-macro jet isolates the remaining sheared-derivative/moment transfer obstruction. |
| [`L-9840`](claims/L-9840-finite-suffix-zero-descent-no-go.md) | PR #19 H frontier | Any finite H suffix family with `U_z>=V_z` and `A_z>Y_z` for every suffix has no ordinary nonnegative nested seed; the complementary quotient table gives the necessary design escape. |
| [`L-9841`](claims/L-9841-completed-zero-return-rotation.md) | PR #19 H frontier | The completed suffixes `{30,60,70}` form a closed raw multiplier-return architecture whose two-step phase map is an irrational rotation and whose return suffixes reverse endpoint descent. |
| [`L-9842`](claims/L-9842-escape-decoration-refinement.md) | PR #6 invariant components | Horizontal escape decorations lie in one finite 2/3-automatic alphabet and obey an exact width-refinement incidence recurrence, isolating their ordered lift. |
| [`L-9843`](claims/L-9843-raw-return-fiber-drift.md) | PR #19 H frontier | The `{30,60,70}` raw return has an exactly positive additive fiber cocycle, explicit every-orbit mean drift, preserved fiber differences, and zero Lyapunov exponent. |
| [`L-9844`](claims/L-9844-escape-order-three-state-transducer.md) | PR #6 invariant components | The ordered escape lift is an explicit affine `F_3` permutation generated by a three-state transducer driven by the staying word; unbounded pointed-cycle identity remains open. |
| [`L-9845`](claims/L-9845-raw-return-2adic-invariant-fiber.md) | PR #19 H frontier | The raw return has one inverse-contracting 2-adic endpoint graph of exact valuation nine; branches decode modulo `2^32`, the full-shift fiber is strongly separated, and its Sturmian slice has Hausdorff dimension zero. |
| [`L-9846`](claims/L-9846-ordinary-raw-return-signature.md) | PR #19 H frontier | Any ordinary point on that graph must form an integral valuation-nine macro orbit with explicit linear real growth and an aperiodic Sturmian modulo-`2^32` residue stream. |
| [`L-9847`](claims/L-9847-successor-translation-isolation.md) | PR #11/#14 successor geometry | Every realization of one signed survivor difference is an exact common-translation fiber; a successor representative must avoid two sharp open circular intervals, and repeated equal successor arcs obey an exact packing bound. |
| [`L-9848`](claims/L-9848-pade-dyadic-augmentation-descent.md) | PR #20 Padé lane | An exact characteristic-two doubling descent and augmentation accounting reduce dyadic target zeros to one slack; complete group-ring identities exclude the actual remainder layers `s=4,8`. |
| [`L-9849`](claims/L-9849-finite-core-width-rigidity.md) | PR #6 invariant components | Every horizontal root cycle is either absorbed by one finite binary core or is disjoint from it and intrinsically tagged by its width; ternary-kernel finiteness is exactly eventual absorption. |
| [`L-9850`](claims/L-9850-ordinary-raw-return-packing-obstruction.md) | PR #19 H frontier | Recursive residue decoding and exact drift force more distinct small positive endpoints than the integers can hold, proving that the raw-return invariant graph has no ordinary point. |
| [`L-9851`](claims/L-9851-unique-ergodic-integer-packing.md) | Cross-direction abstraction | Over a compact uniquely ergodic base, normalized integer growth and endpoint multiplicity `M` force the sharp packing inequality `m^(-1) integral R^(-1)dnu<=M`. |
| [`L-9852`](claims/L-9852-residual-bulk-padding-xor.md) | PR #3 collision/padding | A bulk-routed padding prefix is physical exactly on one residual congruence cylinder; its next physical bit is the bulk quotient bit XOR one irreducible residual-defect bit. |
| [`L-9853`](claims/L-9853-zero-run-translation-gap-obstruction.md) | PR #11/#14 successor geometry | Exact width lifts and the full `81`-twist group construct zero-run translation fibers whose pointed gap is exponentially larger than average, refuting uniform gap contraction from multiplicity alone. |
| [`L-9854`](claims/L-9854-sparse-residue-linear-packing.md) | Cross-direction arithmetic | A bounded-multiplicity integer sequence of upper slope `C` occupying `r` classes modulo `q` must satisfy `MrC>=q`; exact valuation nine gives a large-margin alternative exclusion of the raw H graph. |
| [`L-9855`](claims/L-9855-phase-residue-ergodic-packing.md) | Cross-direction abstraction | A finite phase-to-residue decoder refines unique-ergodic packing one arithmetic progression at a time; each decoded fiber obeys its own sharp capacity inequality. |
| [`L-9856`](claims/L-9856-pade-dyadic-four-residue-transition.md) | PR #20 Padé lane | A universal Boolean four-channel Hasse transition proves exact augmentation orders `20,32` and excludes all dyadic targets at actual remainders `s=12,16`. |
| [`L-9857`](claims/L-9857-finite-ordinary-absorption-separator.md) | PR #6 invariant components | Every fixed-width horizontal root has an explicit finite Moore presentation and ordinary-input separator from the finite core; the horizon grows as `2^(Theta(3^k))`. |
| [`L-9858`](claims/L-9858-residual-address-correction-isometry.md) | PR #3 collision/padding | The entire finite residual-to-address correction is a pointed 2-adic isometry: at precision `Q` it permutes all `Q`-bit words, and a sole residual-dependent channel must carry exactly `Q` bits. |
| [`L-9859`](claims/L-9859-pade-dyadic-minimal-residue-state.md) | PR #20 Padé lane | Residue-sum channels close through height `H` exactly when `4*2^(nu_2(M))>H`; sixteen channels are minimal at height `38`, where the exact order `38` excludes every target at `s=20`. |
| [`L-9860`](claims/L-9860-hall-set-valued-residue-packing.md) | Cross-direction abstraction | A partial set-valued phase decoder obeys every sharp Hall no-outlet cut, extending phase-residue packing without pretending that an allowed set is a selected residue. |
| [`L-9861`](claims/L-9861-pade-dyadic-paired-channel-layers.md) | PR #20 Padé lane | An exact eight-pair twisted realization gives augmentation orders `46,52` and excludes every dyadic target at `s=24,28`; the raw even/odd summary is proved nonclosed. |
| [`L-9862`](claims/L-9862-pade-dyadic-first-state-refinement.md) | PR #20 Padé lane | Height `72` forces the first residue-state refinement to thirty-two channels; a universal certificate gives order `72`, slack eight, and excludes all targets at `s=32`. |
| [`L-9863`](claims/L-9863-triangular-normal-form-2adic-isometries.md) | Collision/2-adic structure | Every 2-adic isometry has a unique LSF-triangular Boolean form; finite reductions are rooted-tree automorphisms with exact wreath-product and extension counts. |
| [`L-9864`](claims/L-9864-pade-dyadic-four-step-block.md) | PR #20 Padé lane | Four q-Pascal steps form an exact five-branch filtered operator; its scalar product congruence is sharp modulo `X^8`, isolating the missing endpoint invariant. |
| [`L-9865`](claims/L-9865-survivor-bucket-order-statistics.md) | PR #16 survivor selector | One width lift is an exact 64-bucket stable merge; at most four source-head candidates per bucket determine the live nontrivial minimum and successor. |
| [`L-9866`](claims/L-9866-fractional-hall-residue-allocation.md) | Cross-direction abstraction | Hall no-outlet cuts exactly characterize finite fractional residue allocation; the maximum overload is the unroutable mass, and tight cuts form an impermeable lattice. |
| [`L-9867`](claims/L-9867-finite-section-isometry-transducers.md) | Collision/automata bridge | A 2-adic isometry has a finite synchronous LSF Mealy realization exactly when its rooted-tree section set is finite; the number of sections is the minimal state count. |
| [`L-9868`](claims/L-9868-pade-two-level-block-carry-states.md) | Period-four Padé quotient | Exact two-level blocks, q-Lucas residual states, and the strict prime-power carry gap. |
| [`L-9869`](claims/L-9869-pade-odd-prime-two-jet-bound.md) | Period-four Padé quotient | A two-jet bound which, pending external review, closes every odd prime-power order above the cutoff. |
| [`L-9870`](claims/L-9870-pade-composite-distinguished-block.md) | Composite Padé descent | A carry-optimal block preserving the prime-power valuation budget at residual order `m`. |
| [`L-9871`](claims/L-9871-pade-composite-value-descent.md) | Composite Padé descent | Exact one/two-channel value congruences modulo `Phi_m`. |
| [`L-9872`](claims/L-9872-pade-composite-first-jet-descent.md) | Composite Padé descent | Exact finite descent for values and first derivatives. |
| [`L-9873`](claims/L-9873-pade-composite-all-order-jet-descent.md) | Composite Padé descent | Candidate integral finite-channel interpolation at arbitrary cyclotomic jet order, with its universal degree lemma quarantined for review. |
| [`L-9874`](claims/L-9874-pade-dyadic-boundary-nonvanishing.md) | Dyadic Padé lane | All-order nonvanishing for the two Newton-boundary index families. |
| [`L-9875`](claims/L-9875-pade-dyadic-cartier-kernel.md) | Dyadic Padé lane | Exact Cartier/type-C product, solved scalar kernel, transfer recurrences, and binary clusters. |

| [`L-9876`](claims/L-9876-padding-isometry-infinite-sections.md) | Collision/padding lane | The exponential padding chart exposes a new rooted-tree section at every zero-prefix depth, so neither it nor its inverse address map has a fixed synchronous finite-state realization. |
| [`L-9877`](claims/L-9877-survivor-terminal-jet-selector.md) | PR #16 survivor selector | Arbitrary-width terminal jets compile every suffix block exactly; the two-width selector uses four refined source lists, and every further lift consumes one additional base-64 digit. |
| [`L-9878`](claims/L-9878-h-rounded-deficit-pressure.md) | PR #19 exact H chain | Rounded-critical steps contract transformed height, while every positive exact chain pays at least `log_8(49/37)` positive rounded-deficit mass per step after overshoots and phase costs. |
| [`L-9879`](claims/L-9879-h-critical-core-repulsion.md) | PR #19 critical H chain | Repeated odd cores force exponential completion height; in the critical regime all but `O(log N)` early positions have distinct cores, yielding the sharp residue-capacity constant six. |
| [`L-9880`](claims/L-9880-pade-residual-shadow-layers.md) | PR #20 Padé lane | Exact residual shadows and periodic defect filtration prove augmentation orders `78,86,92,104` and exclude every larger dyadic target at `s=36,40,44,48`. |
| [`L-9881`](claims/L-9881-survivor-one-hot-jet-reachability.md) | PR #16 survivor compiler | One-hot survivor prefixes in one phase realize every finite terminal jet and terminal residue, forcing at least `64^m` residual states at horizon `m`. |
| [`L-9882`](claims/L-9882-h-critical-budget-pressure.md) | PR #19 critical H chain | The discounted critical budget makes relative valuation errors absolutely summable; core capacity forces logarithmic surplus over the sharp deficit baseline at density-one prefixes. |
| [`L-9883`](claims/L-9883-survivor-common-width-exposure.md) | PR #16 survivor selector | Every suffix becomes the unique minimum among all common-width descendants of a suitable one-hot prefix, giving a `2^m` live-head lower bound and an exact block-zero criterion for global promotion. |
| [`L-9884`](claims/L-9884-pade-post-window-phase-dominance.md) | PR #20 periodic Pade lane | After every allocated root window closes, phase zero uniquely controls every tail coefficient and evaluated tail; an unchanged-height period-four repair needs more than `0.064346n` extra cancelled blocks. |
| [`L-9885`](claims/L-9885-centered-renewal-block-digits.md) | PR #16 survivor/centered bridge | The terminal-jet block is literally the base-64 centered renewal string; block zero, unchanged ordinary survival, minimum plateaux, and one-hot promotion become one exact lifetime sieve. |
| [`L-9886`](claims/L-9886-one-hot-predecessor-phase-obstruction.md) | PR #16 survivor selector | Every legal predecessor depth has an exact residue phase. Along exposures of any fixed suffix, lower block-zero lifetimes are unbounded, so no suffix-only promotion bound can work. |
| [`L-9887`](claims/L-9887-cap-chain-two-cell-collar.md) | PR #33/PR #3 cap-chain bridge | Exact height gaps collapse every late hypothetical 256-transition cap stage to its first and last two cells plus one 252-cell arithmetic bridge. |
| [`L-9888`](claims/L-9888-cap-stitch-hensel-isometry.md) | PR #33/PR #3 cap-chain bridge | The remaining two-cell mismatch is an exact Hensel block whose valuation survives Montgomery normalization; conditional on the hypothetical cap chain and its shared cusp-height bound, cusp equality has a `Theta(2^m)` low-bit certificate, while the unrestricted inverse has exponential state cost. |
| [`L-9889`](claims/L-9889-h-full-ghost-boundary.md) | PR #19 H ghost frontier | Classifies every closure boundary as a nonpositive finite-code rational, repairs the ordinary-minimum boundary audit, and restricts the termination-equivalent minimum to the nonzero section. |
| [`L-9890`](claims/L-9890-h-dual-renewal-bridge.md) | PR #19 H renewal frontier | Consecutive nonzero letters share one integer with exact dual `2`/`3` valuations; an integral renewal height obeys a strict nonperiodic sign law, convergent normalization, and subcritical post-Yu gaps. |
| [`L-9891`](claims/L-9891-pade-adjacent-casoratian-rank.md) | PR #20 coupled Pade frontier | Every finite adjacent-order error Casoratian is nonzero. The canonical `q`-order coupling cancels exactly `q-1` blocks, has an exact normalized error valuation, and needs `q>0.07114166n` in the optimistic unchanged-height period-four model. |
| [`L-9892`](claims/L-9892-survivor-nested-rank-obstruction.md) | PR #16 global survivor order | Every suffix has thin exposure phases outside `n=1 mod36` with arbitrarily many lower zero-block competitors at one depth; their exact pure-power geometry gives unbounded global rank, while their selected 2-adic phase refinements have small Haar measure. |
| [`L-9893`](claims/L-9893-cap-middle-triple-cascade.md) | PR #33/PR #3 cap-chain bridge | The 252-cell middle collapses to 84 canonical triple seams. Its physical terminal/head mismatch language has at most 4096 values, so the unrestricted Hensel section lower bound is not bridge-reachable. |
| [`L-9894`](claims/L-9894-h-successive-core-compatibility.md) | PR #19 H renewal frontier | Two adjacent renewal cores obey one exact elimination identity; shared primes lie in multiplicative-order progressions, while a second integral sign law and joint discounted budget constrain successive cores. |
| [`L-9895`](claims/L-9895-pade-opposite-tropical-cofactor-height.md) | PR #20 coupled Pade frontier | Adjacent Casoratians have opposite unique tropical permutations at `2` and `3`; any linear-width canonical cofactor vector has quadratic projective height. |
| [`R-9805`](claims/R-9805-pade-endpoint-factor-cancellation.md) | PR #20 coupled Pade frontier | The same endpoint factors occur in the evaluated numerator and denominator, so the quadratic cofactor obstruction disappears from their reduced ratio at both distinguished primes. |
| [`L-9896`](claims/L-9896-survivor-delayed-one-hot-density-one.md) | PR #16 global survivor order | Full delayed one-hot lifts decorrelate after an exact delay cutoff; lower block-zero competitors have relative ordinary density one and exposed rank diverges in density. |
| [`L-9897`](claims/L-9897-h-fresh-prime-room-dichotomy.md) | PR #19 H renewal frontier | Every transition pays in next-room length or forward prime mass, and no fixed finite prime support can recur infinitely often on a nonperiodic exact H chain. |
| [`L-9898`](claims/L-9898-cap-first-seam-transfer-graph.md) | PR #33/PR #3 cap-chain bridge | Every triple seam is one edge of a 1024-state overlap graph. At scales `12,13`, the first seam has no edge modulo the minimally separating modulus `2048`. |
| [`R-9806`](claims/R-9806-survivor-one-hot-exceptional-cantor-set.md) | PR #16 global survivor order | The formal all-delay avoiding set is a positive-dimensional Haar-null Cantor set, while ordinary depths with fewer than `s` delayed competitors obey a power-saving count. |
| [`R-9807`](claims/R-9807-pade-special-vector-allocation-ceiling.md) | PR #20 period-ten frontier | The summed native vector has exactly the minimum allocated zero window; its exact scalar-allocation functional is uniquely maximized by equal allocation and remains subcritical at period ten. |
| [`L-9899`](claims/L-9899-solution-cone-natural-boundary-rays.md) | Issue #24 solution cone | Extreme rays are component indicators; every proper positive ray has a natural boundary, so continuation of the distinguished ray through one arc is equivalent to Collatz. |
| [`T-9801`](claims/T-9801-ordinary-itinerary-complexity-threshold.md) | PR #16 ordinary/equality bridge | Every nontrivial ordinary binary-chart itinerary has linear factor-complexity slope at least `log M/log(N/M)`; for `64 -> 81` it exceeds 16, giving a finite language certificate that excludes entire low-complexity equality subshifts. |
| [`T-9802`](claims/T-9802-cap-head-final-symbol-rigidity.md) | PR #33/PR #3 cap-chain bridge | The fourth head symbol only translates the correction by cells `(0,3,53,1)Q/64`; at least 192 of 256 words are uniformly large, and every late hypothetical cap chain has at most 64 cusp-admissible head words. |
| [`T-9803`](claims/T-9803-survivor-adjacent-two-hot-tree.md) | PR #16 global survivor order | One-hot and adjacent two-hot events have an exact `1/145` asymptotic correlation; even any fixed library of at most 62 bounded templates leaves a positive-dimensional formal exceptional set. |
| [`T-9804`](claims/T-9804-sparse-pade-casoratian-optimality.md) | PR #20 period-ten frontier | Every sparse scalar order minor is nonzero, but at fixed width and largest order each skipped order incurs an exact 2-adic accuracy deficit; sparse orders cannot evade the adjacent-order period-ten ceiling. |
| [`R-9808`](claims/R-9808-false-four-phase-three-halves-bridge.md) | PR #16 centered-power audit | Refutes the identity `81/64=(3/2)^4`: the submitted four-phase full-`3/2` orbit bridge misses a factor `4^n`; direct-`81/64` results survive only after independent dependency audit. |
| [`T-9805`](claims/T-9805-quantitative-fresh-prime-budget.md) | PR #3 scaled-tail S-unit frontier | For `N` corrected stages with `s_N` distinct boundary primes, `N<=4^256 exp(1542^771(2s_N+2))`; this makes qualitative fresh-prime necessity effective and records the correlated rank `<=2s_N+1`. |
| [`T-9806`](claims/T-9806-cap-head-two-level-cell-hierarchy.md) | PR #33/PR #3 cap-head bridge | After two head symbols are fixed, the last two occupy sixteen distinct cells of width `q_0/64` with offsets split by `(0,3,53,1)` and `(0,33,7,11) mod64`; exact zeros fall to at most 16, although the known cusp is wider than these cells. |
| [`T-9807`](claims/T-9807-dirichlet-floor-blocks-one-phase-elimination.md) | PR #20 period-ten frontier | Elementary p-adic pigeonholing forces every unrestricted `D`-value measure exponent to satisfy `omega>=D+1`; applying the source measure at dimension one gives every scalar family `limsup<=omega_1<17/5<10<=omega_9`, rigorously closing full-measure one-phase elimination. |
| [`T-9808`](claims/T-9808-stage-toll-room-finiteness.md) | PR #3 fixed-room/cap bridge | Separated dyadic toll valuations losslessly decode the full 256-symbol word from the incoming boundary, and the fixed-room law permits at most `4^256` eventual rooms and tails. |

The compact status ledger is [`CLAIMS.md`](CLAIMS.md), and
[`VERIFICATION.md`](VERIFICATION.md) records which source-branch arguments were
independently reconstructed and which conjectural boundaries remain open.

## Highest-leverage next moves

1. For the survivor lane, control cancellation in the exact signed carry
   numerator for the minimum and successor. `R-9804` rules out a global zero
   reset, while `L-9830` identifies the pair-specific common-output length
   exactly with the base-64 valuation of one settled signed-chart iterate;
   `L-9834` closes the ambient pair geometry as a ternary full shift. `L-9847`
   resolves each difference multiplicity as a literal translation fiber and
   gives the exact two-sided isolation test and repeated-arc packing bound for
   successor representatives. `L-9853` then refutes any uniform pointed-gap
   contraction based only on a long zero run: legitimate `81` twists create
   exponentially exceptional points. `L-9865` supplies the live selector for
   one width lift. `L-9877` gives its exact arbitrary-width terminal-jet
   compiler and an actual witness showing that an unrefined two-head bucket
   summary is not closed. `L-9881` proves that every finite jet is reached by
   genuine one-hot prefixes in one phase; `L-9883` exposes every suffix as a
   unique common-width cylinder minimum. `L-9885` identifies its block-zero
   competitors with centered zero-renewal lifetimes, and `L-9886` gives a
   complete predecessor-phase obstruction: even for a fixed suffix those
   lower lifetimes are unbounded across exposing depths. `L-9892` closes the
   later-merger route and goes strictly beyond that phase: outside
   `n=1 mod36`, one exposed representative can have arbitrarily many lower
   block-zero competitors with exact pure-power values and arbitrarily late
   first differences. `L-9896` now classifies the full delayed one-hot lift
   family: every fixed delay has density `64^(-(m+1))`, delays separated by
   `m+1` are exactly independent, and lower block-zero competitors have
   relative ordinary density one in every exposure subphase. The one-hot
   candidate's global rank therefore diverges in density. `R-9806` resolves
   the geometry left behind: the formal all-delay avoiding set is a perfect,
   positive-dimensional, Haar-null Cantor set, while ordinary parameters with
   fewer than `s` delayed competitors have the power-saving count
   `O(T^d(log T)^(s-1))`, `d<1`. It may still contain infinitely many ordinary
   parameters. `T-9803` now adds the adjacent two-hot template and computes
   its exact `1/145` correlation with the one-hot event.  This still does not
   cover the formal tree: every fixed library of at most 62 bounded templates
   leaves a positive-dimensional exceptional set.  The next task is therefore
   an unbounded, delay-growing two-hot library or arithmetic control of the
   first positive block, not another small fixed template list.
2. For the collision lane, propagate the exact compatibility cylinder of
   `L-9852` through the residual grammar. A bulk address routes the physical
   tail through `H` bits exactly when `h congruent V modulo 2^H`, and the next
   bit is the bulk quotient parity XOR the residual defect
   `qbit_H(h-V)`. `L-9858` upgrades this one-bit law: the full correction at
   every precision is a pointed 2-adic isometry and hence a permutation of all
   residual words. A sole residual-dependent channel therefore needs exactly
   one bit per corrected bit. `L-9863` proves that every isometric conjugate
   is automatically LSF-triangular, while `L-9867` proves that bounded state
   is equivalent to finiteness of its rooted-tree sections. `L-9876`
   evaluates that criterion on the actual exponential padding chart: its
   zero-prefix sections have pairwise slope separation
   `nu_2(kappa_l-kappa_k)=r+k`, so both the chart and its inverse address map
   require unbounded synchronous state. The remaining task is therefore to
   prove the physical scale update is isometric on its full domain and
   determine whether the zipper conjugacy cancels this explicit section drift
   through the final `K-H` block; triangular finite lookup alone does not do
   so. Independently, `L-9887`--`L-9888` collapse every hypothetical PR #33
   cap chain to a two-cell collar and show that its final Montgomery block is
   an isometric code of the raw head/terminal mismatch. The cap-chain target
   was a scale-stable nonzero low bit together with the 252-cell bridge.
   `L-9893` now resolves that middle into 84 exact canonical triple seams and
   bounds the physical boundary mismatch language by 4096 values. Generic
   Hensel sections are therefore not bridge-reachable. `L-9898` constructs
   the exact overlap graph: five-symbol triple states give 1024 vertices and
   64 candidate continuations. Its first seam is empty at scales `12` and
   `13`, with `2048` the minimal separating modulus. This is a finite
   two-scale obstruction, not an all-late-scale theorem: the full odd-radix
   carry prevents an autonomous scale update. `L-9821` bypasses that output
   carry on the input side: completion height puts every one of the 84
   canonical triple corrections below the square root of its exact modulus
   and gives finite 256-head and 1024-triple cusp filters. `T-9802` supplies
   the first uniform head reduction: changing the final symbol translates by
   one of four fixed `Q/64` cells, so at least 192 words are too large and a
   hypothetical late cap chain has at most 64 admissible words. `T-9806`
   resolves the last two symbols one level further into sixteen distinct
   `q_0/64` cells per fixed first-symbol pair and reduces exact-zero heads to
   at most 16. Its cell width is nevertheless exponentially below the known
   cusp, so it does not improve the conditional 64-word filter. Refreshed
   `PR3/T-0036` and `T-9808` remove a different apparent freedom: one room
   determines the boundary and full word, and at most `4^256` rooms can support
   eventual tails. The next target is to decode a room first and test its 84
   exact seams and head cell, rather than branch freely over words; closing the
   output carry remains a separate route.
3. For the H lane, design a different return architecture. `L-9822`--`L-9829`
   solve the real phase and exact tail shifts of the `10/30` compiler;
   `L-9831` shows that physicality leaves one nested carry path, and `L-9833`
   proves that path has no ordinary nonnegative seed. `L-9835` nevertheless
   quantifies its carry stream: zero-block gaps are logarithmic in endpoint
   size and nonzero blocks occur at least logarithmically often. `L-9837`
   gives the exact reset-to-future-cylinder congruence and finite-range sieve;
   the remaining issue is a correlation theorem between its two carry
   streams. `L-9840` generalizes the nonordinary-seed obstruction to every
   finite suffix family whose zero-interface maps robustly descend, and gives
   the exact quotient regimes a replacement architecture must reach. Any
   successful return must violate that criterion recurrently. `L-9841`
   supplies the first such finite raw architecture: `{30,60,70}` alternates
   genuine multiplier crossings and avoids uniform descent at every return.
   `L-9843` solves its real affine skew product: normalized fiber drift is
   uniformly positive, with no bounded graph or cycle and no contraction.
   `L-9845` solves the inverse 2-adic fiber exactly: it selects a unique
   valuation-nine graph, recursively decodes its branch address, and makes
   the Sturmian slice zero-dimensional. `L-9846` records the full necessary
   signature of an ordinary intersection: exact linear growth, valuation nine,
   and the prescribed Sturmian pair of low residues. `L-9850` combines that
   drift with decoder-forced distinctness: triangular phase equidistribution
   predicts strictly more than one endpoint per available small integer, so
   the invariant graph has no ordinary point. This closes `{30,60,70}`
   negatively. `L-9851` abstracts the mechanism: any new return with endpoint
   multiplicity at most `M` must satisfy
   `m^(-1) integral R^(-1)dnu<=M`. `L-9854` supplies a cheaper first screen
   from linear growth and sparse residues, while `L-9855` resolves ergodic
   capacity by decoder phase. `L-9860` extends the screen to partial
   set-valued decoders through exact Hall no-outlet cuts. `L-9866` proves
   those cuts are exactly sufficient for fractional transportation and
   identifies the tight-cut lattice. Independently, `L-9878` derives a sharp
   pressure law for the PR #19 block chain, and `L-9879` makes critical cores
   asymptotically injective with residue-capacity constant six. `L-9882`
   combines these with the critical budget: relative valuation errors are
   absolutely summable and excess pressure is logarithmic at density-one
   prefixes, but unit deficits and near-linear distinct cores still fit the
   exponential scale. `L-9889` repairs the full ghost-boundary classification
   and gives a sharper termination-equivalent nonzero-section minimum.
   `L-9890` then identifies every positive-survivor zero room with a high
   `3`-adic entrance and couples consecutive nonzero letters through one
   dual-valuation integer `W_k`, with an exact integral sign law. `L-9894`
   supplies the missing successive-core compatibility: adjacent `W` cores
   satisfy one two-place elimination equation, any reused prime power forces
   a multiplicative-order divisor of `R_k`, and a second sign law shares the
   summable renewal toll. `L-9897` resolves the qualitative
   prime-persistence/fresh-mass dichotomy. A changed reused exponent exactly
   saturates its multiplicative-order valuation tax; every transition pays
   in next-room length or forward quotient mass; and a nonperiodic infinite
   exact chain can use no fixed finite prime support infinitely often. Hence
   globally new primes occur with divergent unweighted logarithmic mass.
   They may still be arbitrarily sparse, so the next target is a quantitative
   S-unit/order bound or a plateau argument that creates positive discounted
   mass or repeats the full central state.
4. For the Padé lane, classify genuinely composite residual multiplicity and
   bound noncyclotomic gcd degree. `L-9816` proves that automatic, reduced-prime,
   and distinct antisymmetric cancellation cannot reach exponent one;
   `L-9828` also removes squarefree reduced prime-power support as a
   quadratic-density rescue, while `L-9832` solves the `p>s` prime-power
   sector exactly and leaves only `p<=s` for odd prime powers. `L-9839` bounds
   the full dyadic residual budget below the deficit conditional on one
   explicit transverse-jet transfer inequality. `L-9848` supplies an exact
   augmentation descent, and `L-9856` extends its universal Boolean
   certificates through `s=16`. `L-9859` proves the exact residue-state closure
   criterion and settles `s=20`; `L-9861` supplies the twisted paired state and
   settles `s=24,28`. `L-9862` crosses the first refinement boundary and
   settles `s=32`. `L-9864` replaces another finite table with an exact
   four-step operator, and `L-9880` finds the missing invariant in
   residual-shadow form. Its symbolic defect filtration settles
   `s=36,40,44,48`, so target residuals are now nonzero in the first twelve
   actual layers. `L-9884` separately closes post-window cross-phase
   cancellation throughout the whole root-product family: equal allocation
   is phase-zero dominated at every surviving block, and sublinear extra
   cancellation cannot repair period four. `L-9891` resolves the entire
   scalar adjacent-order Casoratian rank: `q` neighboring errors cancel
   exactly `q-1` additional blocks, and their normalized valuation is exact.
   Even granting zero cofactor-height cost, the unchanged-height period-four
   model needs `q>0.07114166n`. `L-9895` proves that the canonical cofactor
   vector cannot actually be cost-free: reverse permutation at `2` and
   identity permutation at `3` force quadratic projective height at linear
   width. `R-9805` then closes the naive transfer to the final approximant:
   those endpoint factors occur equally in its evaluated numerator and
   denominator, leaving only constant ratio valuations at `2` and `3`.
   Reduced height must therefore be controlled archimedeanly, at other
   primes, or by a global evaluation resultant. The separate anchor window
   remains degrees `105` through `110`. `R-9807` also closes scalar unequal
   phase allocation: the summed native vector has an exact unique endpoint,
   equal allocation uniquely maximizes its valuation-to-height functional,
   and even the period-ten ceiling is `0.954998217905888...<1`. The live
   directions are therefore coupled Hermite--Pade systems, evaluation
   resultants, and genuine reduced-height savings rather than scalar
   reallocation. `T-9804` also closes sparse scalar order selection: arbitrary
   sparse minors remain nonzero, but consecutive orders uniquely maximize
   normalized accuracy at fixed width and top order.  In light of refreshed
   `PR20/Q-9413`, `T-9807` now closes the full-measure one-phase elimination
   route as well. The elementary Dirichlet floor is `omega_9>=10`, while the
   same Vaananen--Wallisser measure at dimension one bounds every scalar
   approximant family by `limsup<=omega_1<17/5`; the required strict inequality
   is impossible. The live targets are therefore a genuinely directional
   estimate on the native coefficient rays, or a coupled two-dimensional
   `q`-difference/Hermite--Pade construction for the period-ten vector.
5. For the direct centered `64 -> 81` lane, keep the recurrence in its native
   base. `R-9808` finds that `PR16/L-9312` used the false identity
   `81/64=(3/2)^4`; the correct four-sample formula has a growing factor
   `4^n`, while a multiplicative decomposition needs four `3/2` steps and two
   `1/2` steps.  The fixed four-phase full-`3/2` bridge is therefore
   quarantined, although direct-base claims can survive independent audit.
   `T-9801` independently reconstructs the PR #20 complexity floor and adds a
   finite-language interface: every ordinary itinerary has slope at least
   `log 64/log(81/64)=17.6548...`.  Hence any fully audited critical equality
   language with smaller slope is excluded, and binary 2- or 3-uniform
   substitution orbit closures already fail.  The next task is to acquire the
   exact rational-base source theorem and compute its equality language rather
   than route through the invalid schedule.
6. For the corrected PR #3 stage, combine the new arithmetic restrictions.
   `T-9805` turns qualitative fresh-prime necessity into the explicit finite
   tradeoff `N<=4^256 exp(1542^771(2s_N+2))`, using the correlated fixed-word
   rank `2s_N+1` rather than the coarse product rank. `T-9808` simultaneously
   makes the exceptional room set finite and the stage word deterministic.
   The next useful gain is either to exploit the bounded `{2,3}` boundary
   signatures to lower the S-unit rank, or to intersect each decoded room with
   the cap/seam constraints. The constants are structural, not computational.
7. Prove any fixed polynomial-in-`M(m_{K+1})` bound on the active terminal
   context. By `L-9805`, that would exclude eventual cylinder stabilization.
8. Test binary-automatic invariant-component colorings. `L-9823` eliminates
   every finite congruence, Presburger, unary-regular, rational, algebraic, and
   D-finite description. `L-9825` makes the central ternary spine finite, and
   `L-9836` closes every fixed-width translated cone. `L-9838` puts every
   absolute primitive state directly in the original binary kernel and turns
   each positive-valuation stratum into one exact horizontal cycle with exits
   into that fixed kernel. The last test is a one-parameter cumulative family
   of nontrivial central-base cycles over unbounded coheight. `L-9842` makes
   every exit decoration eventually periodic and gives a fixed substitution
   matrix for their counts. `L-9844` resolves the lost cyclic-order
   permutation as a three-state transduction of the staying word. `L-9849`
   resolves root equality: outside one finite section-closed core, the staying
   word makes width intrinsic. `L-9857` turns absorption at every supplied
   fixed width into a finite Moore-equivalence test with an explicit ordinary
   separator. The live issue is uniformity: its horizon grows with width, and
   any nonconstant coloring must have infinitely many unabsorbed widths.
   Independently, `L-9899` identifies the extreme rays of the nonnegative
   solution cone with component indicators and proves that every proper
   positive ray has the unit circle as a natural boundary. Continuation of
   the distinguished `C_1` ray through one boundary arc is exactly equivalent
   to Collatz. The next analytic target must therefore establish regularity
   for that binary extreme ray itself; ambient operator spectra do not suffice.

## Integration boundary

This is an isolated packet. It does not edit the competing root ledgers on
other branches and does not promote any branch-qualified claim. Source labels
are written as `PR3/L-0023`, `PR20/T-9409`, and so on.

## Counterexample boundary

Neither nested cylinders nor an append-only Hensel prefix construct an
ordinary infinite trajectory. `L-9801` makes the missing condition explicit:
canonical representatives must eventually stabilize. None of the results in
this packet proves a nontrivial infinite Collatz orbit, and no `K-####`
candidate is proposed.
