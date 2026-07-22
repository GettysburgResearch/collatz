# Global counterexample map — reviewed pass-3 replacement

**Agent:** `gpt56-cartographer-01`  
**Issue:** #36  
**Final cutoff:** 2026-07-22T20:46:30Z  
**Supersedes for current use:** pass-3 head `7c9afd20c2db60d95a74fc69a422d2b1bedeca60`

## Verdict on the prior pass

The mathematical core was mostly sound, including the distributed-pulse indexing, but the pass was not audit-grade: provenance, primary map integration, atom IDs, the phase-1 secret reduction, priorities, and live H state were incomplete. The replacement records the defect in `PASS_3_QUALITY_AUDIT.md` rather than silently rewriting history.

## Final live refresh

The repository advanced during the audit. The replacement now includes:

- PR #34 wave 25 (`b7eec65`): seven-non-`2` valuation support floor, lossless cross-prime compiler, additive one-counter obstruction, and exact arbitrary-pulse remainder;
- PR #48 (`4f75cca`): independent pass of PR #45 and `T-8601`, explicit non-reproduction of PR #42 `T-8602`, refund growth, and selector sparsity;
- PR #49 (`e77a2ac`): width-one refund threshold, causal inverse-carry compiler, deterministic expanding decoder, and the exact sole gap of infinite definedness;
- PR #47's later head and the active two-pulse offense.

## Main corrected findings

1. PR #33 `T-9705` is independently verified at its frozen source, with native integration pending.
2. PR #45's critical compiler and rejected near-candidate are independently passed at the frozen source.
3. PR #42 `T-8602` remains source-proposed/source-computed; PR #48 did not reproduce the full census.
4. Every nontrivial positive cycle needs at least seven non-`2` valuations at proposed wave-25 status.
5. Distributed pulses have an exact full-denominator remainder and a one-variable fixed-total two-pulse congruence.
6. Refund is atomic at width one. PR #49 already provides unique decoding, physical initialization, positivity, and exponential residual growth when defined.
7. The strongest constructive question is now one finite residual with an all-time decoder-domain invariant.
8. Fixed-modulus centered PDR and additive one-counter control are closed witness mechanisms; richer top-boundary state is necessary.
9. Permanent issue-#39 phase 1 is shifted ordinary Collatz.
10. PR #19 iteration 8 supplies a 2.479-billion-block H cycle barrier plus entropy/return filters.
11. No unconditional counterexample was found.

## Validation

- exact source SHAs frozen through PR #49;
- source-status and frozen-review wording audited;
- distributed-pulse formulas rederived and updated to the wave-25 remainder form;
- canonical atom IDs checked (`ACL-P036`; `ACL-P038` retired);
- Markdown fence and placeholder checks passed;
- Graphviz rendered to PNG and SVG;
- primary map, crosswalk, atom index, diagrams, and PR body synchronized.

## Highest-value positive target

```text
Find one finite PR #49 state (t,i,j,z), t>=3744, z>=1,
whose exact deterministic decoder is defined forever.
```

Under the proposed theorem chain, the corresponding explicit physical Collatz orbit is positive and unbounded.
