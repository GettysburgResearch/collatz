# Global counterexample map — reviewed pass-3 replacement

**Agent:** `gpt56-cartographer-01`  
**Issue:** #36  
**Cutoff:** 2026-07-22T20:28:06Z  
**Replaces for current-state use:** pass-3 head `7c9afd20c2db60d95a74fc69a422d2b1bedeca60`

## Reason for replacement

The user requested an independent quality check of the preceding pass. The audit found that its mathematical core was mostly sound, but its repository integration was incomplete:

- exact SHAs were missing for several load-bearing sources;
- the primary map, crosswalk, diagrams, and PR body remained at pass 2;
- `ACL-P036` was duplicated as `ACL-P038`;
- the exact phase-1 secret reduction in issue #39 was omitted;
- novelty and logical distance were conflated in the priority ranking.

The replacement records these findings in `PASS_3_QUALITY_AUDIT.md` rather than silently rewriting history.

## Work performed

- froze exact current heads for every material PR;
- re-read PR #44's claim matrix, PR #42's bounded cycle theorem, PR #45's critical compiler, PR #47's one-pulse theorem, PR #13 wave 7, PR #19 iteration 8, issue #39, issue #40, and issue #43;
- independently rederived the distributed-pulse affine formula and suffix-change identity;
- separated frozen-source independent verification from native-ledger integration;
- updated the primary global map, crosswalk, atom index, Mermaid, Graphviz, and PR description;
- reconciled atom IDs and marked the old pass-3 files superseded for current use;
- split priorities into logical distance and architectural leverage.

## Main corrected findings

1. PR #33 `T-9705` is independently verified at its frozen source, but integration remains pending and the scope is only the corrected 256-transition doubling-scale class.
2. Fixed-modulus centered PDR is exactly the periodic cylinder ghost. The positive centered target is a height/top-boundary one-counter invariant.
3. A permanent issue-#39 phase-1 tail is shifted ordinary Collatz, not a new amplifier.
4. A positive cycle remains the shortest certificate. Serious search must operate at critical continued-fraction scale and solve the full denominator.
5. The distributed-pulse algebra is correct, but low-scale pulse scans are controls; the research target is critical-scale cross-prime coupling.
6. Linear-height quotient refund is the clearest new divergent architecture and is canonically `ACL-P036`.
7. PR #19 iteration 8 now proposes no H cycle through `2,479,700,524` blocks and adds entropy/return barriers; H construction must use delayed novelty or reset renewal.
8. No unconditional counterexample exists at the cutoff.

## Files

- `PASS_3_QUALITY_AUDIT.md`
- `ANALYSIS_SNAPSHOT_PASS_3R.md`
- `CARTOGRAPHY_PASS_3_REVIEWED.md`
- revised `GLOBAL_COUNTEREXAMPLE_MAP.md`
- revised `cartography/CROSSWALK_AND_PRIORITIES.md`
- revised `ATOMIC_COUNTEREXAMPLE_LEMMAS.md`
- `cartography/ATOMS_PASS_3_REVIEWED.md`
- revised Mermaid and Graphviz sources
- this report

## Validation

The replacement was checked for:

- balanced Markdown code fences;
- unresolved placeholder markers;
- duplicate canonical `ACL-*` identifiers in the current atom index;
- Graphviz parse/render to PNG and SVG;
- exact source-head consistency;
- scope wording around frozen-source review;
- phase-1 secret-reduction wording;
- distributed-pulse prefix indexing.

## Counterexample status

No explicit positive nontrivial cycle, divergent seed, regular sanctuary, positive H orbit, centered survivor, or exact third-component witness was found.

The two highest-value positive targets are:

```text
full-denominator critical-scale cycle synthesis;
causal linear-height quotient-refund invariant.
```
