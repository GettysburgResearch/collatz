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
| [Rank moments](../../astra-three-routes/pass5/RANK_MOMENTS.md) and [alternative rank-spectrum proof](../../astra-three-routes/pass5-spectrum-switch/RANK_SPECTRUM.md) | Computable finite sublevels and square-root counting with their respective constants; these are alternative source arguments, not counts to add. |
| [Merging barriers](../../astra-three-routes/pass5/MERGING_BARRIERS.md) and [plateaus/source lists](../../astra-three-routes/pass5-spectrum-switch/PLATEAUS_AND_SOURCES.md) | Necessary excursions for the stated odd multiples of three, sharp guarded families, equal-rank edges and finite witness enumeration. A peak lower bound does not prove a merger exists. |
| [Unsafe repayment](../../astra-three-routes/pass5/UNSAFE_REPAYMENT.md) and [cross-mode switches](../../astra-three-routes/pass5-spectrum-switch/SWITCH_REPAYMENT.md) | Infinite guarded families can pay back unbounded spikes. The requested next mode is a physical hypothesis, not a consequence of ternary depth alone. |

Complete inverse fans bound the candidate sources for a fixed endpoint; complete rank balls give spatial witness completeness. Neither supplies temporal meeting or a cap-free search-termination theorem.

## Useful failures

The source **121** has no universally sufficient inverse-only cheaper-ancestor explanation under the stated rank convention: its cheaper merger must first move forward at least **54 shortcut steps**. This rules out a particular universal strategy, not all merging. The control `103 -> 175` refutes an incorrectly assumed next mode. Phase mismatches and failed recursive pruning are further tests for proposed selectors. Their exact statements appear in the linked proofs.

The older complete-tree rigidity theorems rule out specified finite tame self-sections. They do not rule out this moving-index rank or a genuinely unbounded-state selector. Conversely, properness or unbounded indices alone do not make a selector total.

## Next contribution and evidence

[Construct a complete guarded selector](../../open-obligations/README.md#complete-merging), proving both actual physical meeting and strict decrease in one well-founded rank. A total program returning UNRESOLVED outside a guard is not a total successful certificate procedure. New combinations of families remain proposed until coverage and termination are proved.

<details><summary>Exact review, source identity and replay limits</summary>

[P-rank/frontier clause review](../../../reports/prepublic-2026-09-05/reviewer-a/CLAIM_MATRIX.md); [section/moving-rank clause review](../../../reports/prepublic-2026-09-05/reviewer-b/CLAIM_MATRIX.md); [source identities](../../../claims/reviewed-2026-09-05.json). Some files reuse claim numbers; [aliases](../../../claims/aliases.json) preserves path-qualified identities. Finite cover populations overlap and must not be added. Complete encoded censuses without replay retain that limitation. [Replay policy](../../../docs/REPLAY_POLICY.md) separates finite evidence from the universal claims in the written arguments.

</details>
