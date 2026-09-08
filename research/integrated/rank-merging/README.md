# Ranks, repayment and physical merging

A lower-rank merger is a finite ordinary certificate: sources n and m, finite shortcut clocks a and b, one endpoint `T^a(n)=T^b(m)`, and a strict decrease in the specified rank from n to m. The witness m need not be the smaller ordinary integer. A complete, terminating selection of such diagrams would support well-founded descent. **No universal successful selector or complete cover is established.**

## The available ranks

The section/global rank `P(n)=(2n+1)^2/3^{v_3(2n+1)}` and the moving-envelope rank `R_*` are different. The latter minimizes an unbounded family of exact valuation ranks but can be evaluated from at most four input-dependent candidates; for `n>=2`, `n-1<=R_*(n)<=n^2`. Its sublevel counts have square-root scale. An input-dependent finite evaluation is not a fixed finite dictionary. [Definitions and clocks](../CONVENTIONS.md) · [Moving-rank proof](../../astra-three-routes/pass4/MOVING_GHOST_RANK.md).

Neither rank decreases at every step. Arbitrary mode switches need not contract, and a safe exit may enter an unsafe state. The two safe-region estimates belong to [transport](../renewal-transport/README.md), not a proof of universal rank descent.

## What the certificate program has established

| Proof route | Surviving result and required limit |
|---|---|
| [Section repayment](../../astra-three-routes/ROUTE_3_RANK_CERTIFICATES.md) and [minimum-rank merging](../../astra-critical-mass/MINIMUM_RANK.md) | Guarded all-parameter families and physical tiles bypass selected long delays. Their initial/limiting rank guards remain essential; the families do not cover every source. |
| [Shared-remainder cancellation](../../astra-critical-mass/REMAINDER_CANCELLATION.md) and [clock defect](../../astra-critical-mass/CLOCK_DEFECT.md) | Equal-clock stripping, phase obstructions and necessary short-clock rigidity. Asynchronous meeting is not synchronous; the specified progression retains its depth-two guard. |
| [Inverse boundary](../../astra-critical-mass/BOUNDARY_FAN.md) and [remaining-depth frontier](../../astra-critical-mass/INVERSE_SHADOW_FRONTIER.md) | Complete radius-two results and lossless pruning for every fixed radius. Recursive boundary-only deletion is separately refuted. |
| [Complete acceleration inverse fan](../../astra-three-routes/pass4/RESONANT_SOURCE_FAN.md) | For a fixed endpoint `y>1`, exact maximality gives all predecessors: an infinite even-source ray when y is odd and a finite odd-source list with at most one deep column. Rank restrictions give finite witness lists, not a temporal cover. |
| [Rank moments](../../astra-three-routes/pass5/RANK_MOMENTS.md) and [alternative rank-spectrum proof](../../astra-three-routes/pass5-spectrum-switch/RANK_SPECTRUM.md) | Computable finite sublevels and square-root counting with their respective constants; these are alternative source arguments, not counts to add. |
| [Merging barriers](../../astra-three-routes/pass5/MERGING_BARRIERS.md) and [plateaus/source lists](../../astra-three-routes/pass5-spectrum-switch/PLATEAUS_AND_SOURCES.md) | Necessary excursions for the stated odd multiples of three, sharp guarded families, equal-rank edges and finite witness enumeration. A peak lower bound does not prove a merger exists. |
| [Unsafe repayment](../../astra-three-routes/pass5/UNSAFE_REPAYMENT.md) and [cross-mode switches](../../astra-three-routes/pass5-spectrum-switch/SWITCH_REPAYMENT.md) | Infinite guarded families can pay back unbounded spikes. The requested next mode is a physical hypothesis, not a consequence of ternary depth alone. |

Complete inverse fans describe every source of a fixed endpoint; they need not be finite. Proper-rank cutoffs give finite candidate witness sets and spatial completeness. Neither supplies temporal meeting or a cap-free search-termination theorem.

## Linear inverse precision and completed-section clocks

The [linear-frontier proof](../../astra-linear-frontier/LINEAR_PRECISION.md), ALF-001–003, bounds the exact negative comparison budget by `floor(r/3)+2<=B_r<=4r+2`. At remaining inverse depth D, at most `4D-2` exits suffice to preserve the full minimum; the search has at most `2*4^D*D!` nodes. This improves the old coarse budget without rejecting its valid shield. It is a finite-radius algorithm, not a guaranteed successful merger search.

[ALF-004–007](../../astra-linear-frontier/SECTION_DEPTH_AND_REPAYMENT.md) give guarded sources for every D with no cheaper P witness in the entire D-by-D box of **completed section returns**, including arbitrarily long odd runs inside each return. The specified bounded-lift repayment sequence has cost `Theta(log n)` for this interface. A separate exponent-lifted family reaches 1 by the compressed physical word `(110)^D0^L`. Its modular certificate is not a literal replay of the enormous path, and the logarithmic-cost assertion is not transferred to that different family.

The same P-hard corridor has an immediate `9/64` decrease in the older component `C(n)=(n+5)^2/3^v3(n+5)`. Both `min(P,C)` and `max(P,C)` nevertheless increase on its first edge. The result motivates a justified switching rule; it does not supply one.

## Expanding-word rank

For a word w with affine data `T_w(n)=(3^q n+A_w)/2^L`, let `Z_w(n)=(3^q-2^L)n+A_w` and `g(z)=z^2/3^v3(|z|)` for nonzero z. The [expanding-word proof](../../astra-tail-transport/expanding-word-rank/PROOF.md), ATT-201–206, defines rho off 1 as the minimum of `g(n),g(n-1),g(n+5)` and **all unreduced** word components with `4*3^q>=5*2^L`; set `rho(1)=0`. It proves `n-1<=rho(n)<=R_*(n)<=n^2`, a strict finite length cutoff `n*2^L<4M` for candidate bound M, and `N_rho(X)<250X^(39/40)`. The 5/4 expansion gap is part of the theorem.

A physically legal minimizing component gives strict decrease of the same rho. Its explicitly guarded `111010` families contract through arbitrarily long old unsafe phases, with global all-word minima proved rather than sampled. But at the even exit the unique minimizing word is illegal, with an unbounded successor-rank jump. Arbitrarily long forward-only delay is also proved; it does not exclude general two-sided diagrams. No universal activation or successful selector follows.

## Actual-prefix rank

With **raw shortcut T**, define for `n>=2`

$$
\Gamma(n)=\min\bigl(\{g(n)\}\cup
\{4^k g(T^k(n)-n):k\ge1,\ T^k(n)\ne n\}\bigr),
\qquad \Gamma(1)=0.
$$

Zero displacements are omitted. Prefix evaluation uses raw T even after a visit to 1; killing is a separate convention for mass and convergence. [APR-001–005](../../astra-linear-frontier/prefix-rank/PROOF.md) prove `n<=Gamma(n)<=n^2`, an exact evaluator using at most `floor(log_2 n)` steps, complete `O(sqrt(M) log M)` sublevels and summability of `Gamma^-s` exactly for `s>1/2`.

A minimizing nonzero **even displacement** rotates to a physical next-prefix certificate, reducing Gamma by at least the factor `1/4` or `3/4`; an even minimizing baseline also gives a drop. [APR-006–008](../../astra-linear-frontier/prefix-rank/PERIODIC_SWITCHING.md) prove unique period-length selection at every phase for every primitive expanding period and every requested finite horizon, on the explicitly constructed ordinary sources. The proof controls all competing prefixes, including the unprescribed future. There is no fixed finite dictionary, no terminal-repayment requirement on this family, and no ordinary infinite-period source: the inputs depend on the horizon.

[APR-009](../../astra-linear-frontier/prefix-rank/SPIKES.md) gives `Gamma(3^H)=3^H` and `Gamma(T(3^H))>(3^H)^(11/10)` for every H>=1. Every lower-Gamma merger must traverse that first spike. Its pure-power and moment counterexamples concern the **raw killed shortcut operator**, not automatically the induced unsafe return. At a hypothetical exceptional-component minimum, every minimizing nonzero displacement must be odd, and a minimizing baseline must be at an odd source. That residual is not excluded.

Rho and Gamma solve different minimization problems; neither replaces P or R_* in an older theorem. The forest's fixed input `1_U/R_*^2` cannot be relabeled with another rank. The [exact source review](../../../reports/post-integration-2026-09-08/CLAIM_MATRIX.md) covers the named components; this guide is not a newly accepted conjunction. [Import and current replay record](../../../reports/integration-2026-09-08/README.md).

## Useful failures

The source **121** has no universally sufficient inverse-only cheaper-ancestor explanation under the stated rank convention: its cheaper merger must first move forward at least **54 shortcut steps**. This rules out a particular universal strategy, not all merging. The control `103 -> 175` refutes an incorrectly assumed next mode. Phase mismatches and failed recursive pruning are further tests for proposed selectors. Their exact statements appear in the linked proofs.

The older complete-tree rigidity theorems rule out specified finite tame self-sections. They do not rule out this moving-index rank or a genuinely unbounded-state selector. Conversely, properness or unbounded indices alone do not make a selector total.

## Next contribution and evidence

[Construct a complete guarded selector](../../open-obligations/README.md#complete-merging), proving both actual physical meeting and strict decrease in one well-founded rank. A total program returning UNRESOLVED outside a guard is not a total successful certificate procedure. New combinations of families remain proposed until coverage and termination are proved.

<details><summary>Exact review, source identity and replay limits</summary>

[P-rank/frontier clause review](../../../reports/prepublic-2026-09-05/reviewer-a/CLAIM_MATRIX.md); [section/moving-rank clause review](../../../reports/prepublic-2026-09-05/reviewer-b/CLAIM_MATRIX.md); [source identities](../../../claims/reviewed-2026-09-05.json). Some files reuse claim numbers; [aliases](../../../claims/aliases.json) preserves path-qualified identities. Finite cover populations overlap and must not be added. Complete encoded censuses without replay retain that limitation. [Replay policy](../../../docs/REPLAY_POLICY.md) separates finite evidence from the universal claims in the written arguments.

</details>
