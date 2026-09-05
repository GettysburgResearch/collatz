# Pre-public integration review A — Collatz

**Reviewer:** reviewer-a. **Mode:** frozen-source review and extraction planning, not a research wave.

**Decision:** do not merge #87, #88, and #90 as an undifferentiated proof package. Extract the independently reconstructed narrow results in the order below, retain the external results as source-qualified, and fix the identified release defects. No complete Collatz argument, fixed-floor power saving, uniform Green bound, or total lower-rank merging cover has been established.

## Frozen scope

Cutoff: **2026-09-05 15:52:28 UTC / 18:52:28 Asia/Jerusalem**.

| Source | Full frozen SHA |
|---|---|
| Baseline main | `9704bcf1ff33cc9e2b729e0c40137a1e55b95397` |
| PR #87 | `e9adc409031a61f3801c4ee1e1e6deeb34188eb7` |
| PR #88 | `c28922fb6d1c070bf86a76192f40bc9ea3edd67c` |
| PR #90 | `78ac7c8489f1df81230402808b1f4b77b18fae73` |

Issue #89 supplies the research mandate and six progress comments, not a proof dependency. The [inventory](INVENTORY.md) includes all eight #90 commits, including `BOUNDARY_FAN.md` and `INVERSE_SHADOW_FRONTIER.md`, which its description and research README omit. The [file ledger](file-inventory.csv) lists all **69 primary PR/file instances**. It explicitly identifies ancillary files not separately content-reviewed and complete artifacts not replayed; it is not a claim that every numerical row or external dependency was verified.

The [claim matrix](CLAIM_MATRIX.md) supplies source, scope, dependencies, evidence, corrections, and destination for each entry. It is authoritative for scope. A `VERIFIED` conditional implication does not verify its antecedent. Unreviewed full artifacts and external proof closures have separate `GAP-BLOCKED` entries rather than inheriting nearby verdicts.

## Main findings

### PR #87 — faithful external dossier, useful local lemmas, no exponent crossing

The imported predecessor endpoint is **c_b X^0.901**, for each fixed positive target not divisible by three. The unit-coefficient conclusion is X^0.90 after a target-dependent cutoff. The forward theorem is natural-density typicality for diverging thresholds with explicit clocks; its fixed-floor upper count remains linear in X. These two results cannot be combined by density language alone.

The endpoint-one exponent-race implication, SC-language entropy argument, forward-minimum sparsity, and abstract dyadic bootstrap pass in their stated narrow scopes. The `0.949955...` exponent applies to SC sources or forward minima, **not an inverse basin**. The actual contraction required for a fixed-floor count is open.

The external manuscripts, source releases, selected proof passages, public declarations, and recorded formal evidence were inspected to the extent detailed in [EVIDENCE.md](EVIDENCE.md). Full Lean closures and 645,700,815 bytes of predecessor payload were not rebuilt/replayed. Recorded PDF hashes were not independently recomputed. Keep **EXTERNAL SOURCE-QUALIFIED**; do not relabel this as independent formal verification.

### PR #88 — correct intended bootstrap, stacking and endpoint corrections

The explicit native-horizon `6499+2X^(19/20)` count and sharp entropy rate pass. So do the abstract exponent-collapse and all-subset mass-conservation obstructions. The useful hypothesis is survivor-specific fiber saving, not a uniform saving for every endpoint subset.

The positive-exponent application of MZ-FH-005 is sound. Its unrestricted wording omits the positivity needed when summing dyadic shell bounds into a timed global count: the proof does not justify all nonpositive beta endpoints. **RP-A1**, an explicit positive-beta restriction or separately proved endpoint treatment, is a proposed correction requiring its own review; it does not retroactively verify the printed unrestricted statement.

#88 is stacked on the original #87 import, not its current follow-up. Comparing frozen #87 to #88 gives **ahead 3 / behind 1**, with merge base `a9abe3509fddc12e22ffa8c559b44fc35adfdb48`. Both branches change the same checker/report/index paths. Preserve both packets until deliberate claim-level reconciliation; do not overwrite one with the other.

### PR #90 — substantial narrow results; no uniform or total closure

The critical weighted-mass bridge, correctly killed inverse criterion, finite-time Green enclosure, ordinary first-passage compiler, scoped weight obstructions, ordinary fresh-shell drift, and physical lower-rank merging arguments pass as delimited in the matrix.

The fresh-shell average cannot be iterated on the actual transported ensemble. The source's counterexample is real, and the reviewer independently reproduced the scaled increases at steps 21–24 with the omitted-source tail accounted for. Moreover `MINIMUM_RANK.md` shows that the proposed signed discrepancy budget is comparable to occupation mass itself: its telescoping identity supplies no automatic cancellation.

The later inverse work must be retained. Radius-two boundary minimization is valid, but its naive recursive extension is false. Remaining-depth-aware inverse-shadow pruning repairs the finite-radius search under explicit precision guards. It is not an all-source termination theorem. The all-depth inverse-only failure at **121** and the exact minimum forward meeting clock **54**, attained at 40, have a finite exhaustive witness-pool proof independently replayed here. Forward motion cannot be omitted from the remaining complete-cover problem.

## Release defects versus mathematics

**Release blockers:** (1) #87/#88 shared-path stack conflict; (2) duplicate T-ASTRA-030–034 identifiers in two different #90 files and stale front doors; (3) the X-ASTRA-003 verifier loses its acceptance checks under `python -O`; (4) exact versus floating diagnostic language in the import checker; (5) #88 report regeneration is not immutable artifact verification; (6) complete aggregate counts and external computations must retain their unreplayed evidence labels. See [ACTION_MAP.md](ACTION_MAP.md).

**Mathematical blockers:** actual fixed-floor survivor contraction, uniform Green control, transported discrepancy control, basin stability, and a total physical lower-rank merging cover remain unproved. The nonpositive-beta endpoint also needs correction or proof. These do not invalidate separately verified conditional/local statements.

**Ordinary future research:** stronger inverse exponents, better weights, deeper finite searches, and coverage of remaining residue classes. They are not prerequisites for publishing accurately scoped partial results.

## Independent evidence and limits

The reviewer-owned [exact check script](reviewer_a_exact.py) imports no source or repository code. It independently reconstructs key arithmetic, all 50 cofinal bases, the finite Green calculation through 2^18 and time256, the transported counterexample, physical inverse interfaces, the radius10 negative precision table, and 121's entire lower-rank witness pool. Normal and optimized executions produced identical [results](exact-results.json):

`ea70e11514698c2581ba44ae4cfcc72864168affd1eb6c2898f78f283d7da716`.

The unsafe optimized verifier finding is an **isolated acceptance-function reproduction**, not a claimed execution of the full upstream program. Complete canonical source-report hashes, large rule censuses, external builds/payloads, and the repository-wide validator were not replayed. No scientific repair was inserted into a source branch.

#91's needed section/fan definitions were followed and rederived within #90; its other results are not assumed. #92 is outside this assignment and has authoring history in this conversation: this review does **not** constitute independent acceptance of #92. No canonical status, source PR, setting, or workflow is changed.
