# Integration, extraction, and PR lifecycle practice

This is a default for work seeking review, extraction, integration, supersession or closure, not a gate on exploratory research. Start with the [research map](RESEARCH_MAP.md), [reviewed catalog](../research/RESULTS_CATALOG.md) and [integrated packet index](../research/integrated/README.md). Status semantics live in the [claim guide](../claims/README.md), historical evidence in the [archive](../archive/README.md).

## Choose and freeze

Choose by mathematical family, dependency value or cleanup need, not a target PR count. State whether the task is new review, a theorem-bearing delta, clean extraction, dependency residency, coherent merge or archive/closure. Freeze current main, the source and review heads, UTC/local time and cutoff. Later pushes belong to a delta record; never rewrite a historical cutoff to include them.

Use `(PR, full SHA, path, claim ID)` throughout. Bare IDs and PR-only aliases can collide within one branch. Preserve original IDs; display aliases are not silent renames.

## Review exact claims and evidence

Identify statement, hypotheses, quantifiers, map, normalization, scope, proof dependencies, review verdict and exceptions. A mixed branch may contain passing, source-qualified, empirical, refuted and blocked claims.

Separate proof inspection, independent reconstruction, artifact inspection, regeneration, checker execution, complete corpus replay, an external build and missing artifacts. A conditional implication does not verify its premise. Old evidence is not a receipt for changed bytes.

Classify later deltas explicitly as editorial, review-only, proposed connection, computation, theorem-bearing or dependency/normalization changes. A prior verdict never transfers automatically.

## Select an action and extract

For each coherent component, choose continued development, deferred review, qualified reference, proof extraction, corrected merge, supersession, or rejection of a monolith with salvage retained. VERIFIED WITH FIXES does not mean automatic merge; REJECTED does not erase useful lemmas and counterexamples.

A durable packet needs readable mathematics: exact statement and scope; proof or exact extract; dependencies and notation; ordinary/2-adic, finite/all-depth and conditional boundaries; failed strengthenings; source/review pins; computation residency and replay state; and the next missing lemma.

Copy reviewed text without mathematical alteration where practical. Preserve a false original beside a separately identified repair. Do not import source registries wholesale or mistake author-stage labels for current independent verdicts.

## Review integrated wording

A byte-identical proof import needs structural and provenance review. A changed statement, normalization, mathematical conjunction or synthesized wrapper needs narrow review of its exact wording. Until then, keep SOURCE-QUALIFIED/PROPOSED and the pending-review flag visible. Correct an erroneous reading surface without pretending the old statement was verified or promoting unrelated theorems.

## Keep status and residency separate

`mathematical_status`, `integration_status`, `promotion_state`, `proof_residency` and `dependency_residency` answer different questions. A verified exact theorem can have a local proof but source-pinned dependencies. Reviewed components can form an accepted reference assembly whose synthesis remains pending. An accepted roadmap is still an open obligation. A locally resident refutation does not make the false source theorem true.

New overlapping review waves belong in separate follow-up records. Do not expand a frozen assignment manifest or weaken its checker to make new work appear previously reviewed. Preserve old core verdicts and exact exceptions together.

## Supersede, archive, and close

Before closure, re-query the source head. Give every valuable component a durable destination: accepted and alternative proofs, refutations, artifacts and evidence ceilings, blocked claims and reasons, open successor questions, and exact review history. Then leave an explicit merged/absorbed/superseded/deferred disposition with links. Closure is repository hygiene, not a mathematical verdict.

Never close a source PR merely because its headline failed, another branch overlaps it, or the queue is long. Do not delete source branches that still carry unique research. Continuing work should start from current main and review its new delta rather than reimport old snapshots.

## Preserve exploratory freedom

No registry entry or lifecycle form is required before exploration. Unconventional approaches, incomplete notes and useful failures are welcome when their map, status, scope, evidence and missing step are intelligible. The stronger contract begins when work seeks accepted mathematics or durable cleanup.

## Validate and leave an executable handoff

Run `python -X utf8 -B tools/validate.py` on a clean complete checkout. [Replay policy](REPLAY_POLICY.md) explains the optional bounded regressions and exact receipt. The original [structural validator](../tools/check_integration_state.py) remains part of this command; preservation rules are not bypassed by the driver.

Use proportionate link, JSON, identity and small exact checks. Hygiene does not justify a broad Collatz search or large replay. New automation requires a separate authorized infrastructure decision and least privilege. Integrity checks are not mathematical verification.

Record the final commit/tree, actual commands and limits. Recheck the source/main heads before merging, and read back the remote after landing. A fresh integrator should be able to see changed dependencies, preserved review boundaries, open targets and executed versus advisory lifecycle actions. Keep detailed receipts backstage; maintain the research map and catalog as the scientific entrance.
