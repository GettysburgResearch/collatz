# Integration, extraction, and PR lifecycle practice

This is a gentle default for future integration passes. It is not a gate on exploratory research. Contributors may investigate freely; the additional discipline begins when work seeks exact review, durable integration, merge, supersession, archival preservation, or closure.

Start from the [`research map`](RESEARCH_MAP.md), the [`reviewed-results catalog`](../research/RESULTS_CATALOG.md), and the [`integrated packet index`](../research/integrated/README.md). Status semantics live in the [`claim registry guide`](../claims/README.md); frozen evidence is indexed in the [`archive`](../archive/README.md).

## 1. Choose the integration target

Choose work by mathematical family, dependency value, or cleanup need—not by a desire to reduce the open-PR count mechanically. State which job is being attempted:

- review coverage or a theorem-bearing delta;
- clean extraction of a coherent claim packet;
- proof- or dependency-residency repair;
- integration of an independently reviewed result;
- supersession or absorption of duplicated work;
- archival preservation and eventual source-PR closure.

A broad exploratory PR need not satisfy a registry schema. Do not interrupt productive research merely to force it into an integration format.

## 2. Freeze the exact state

At the start of a pass, record:

- UTC and local time;
- current `main`;
- every source PR head in scope;
- the exact reviewed SHA, if any;
- a clear cutoff statement.

Assume contributors may continue pushing. Later activity belongs in a separate delta record; never rewrite a historical cutoff to make new work appear previously reviewed.

## 3. Review exact claims and evidence

For every claim being considered, identify:

- exact statement, hypotheses, quantifiers, notation, and scope;
- source PR, commit, claim IDs, and paths;
- dependencies and external theorem normalizations;
- review report, verdict, and claim-level exceptions;
- proof and computation evidence.

Keep evidence granular: proof inspected, independently reconstructed, artifact inspected, artifact regenerated, checker run, large computation independently replayed, computation not replayed, or artifact missing. A branch-level verdict may contain passing, source-qualified, empirical, refuted, and blocked claims.

## 4. Classify later deltas

Compare the reviewed SHA with the current head and classify the delta as one or more of:

- editorial or metadata only;
- review record only;
- proposed connection or strategy;
- computation or artifact only;
- theorem-bearing;
- dependency or normalization change.

An older verdict never transfers automatically to a later theorem or changed dependency.

## 5. Choose a claim-level repository action

Review status and repository action answer different questions. For each coherent packet, choose among actions such as:

- continue active development;
- defer pending review, dependency, source, or repair;
- preserve as research or reference;
- extract a clean packet;
- merge a coherent packet after reviewed fixes;
- supersede or absorb duplicated material;
- reject a monolithic theorem packet while preserving refutations and salvage;
- archive and later close an exhausted source PR.

`VERIFIED WITH FIXES` is not automatically “merge.” `REJECTED` does not erase useful lemmas, counterexamples, artifacts, or historical value.

## 6. Extract a durable proof packet

Prefer clean extraction over importing a long mixed branch history. A durable packet should contain:

- precise statement and exact scope;
- readable proof or exact proof extract;
- dependencies and notation;
- finite, ordinary, 2-adic, conditional, and all-depth boundaries;
- known exclusions, failed strengthenings, and common misreadings;
- exact source and review provenance;
- artifact and replay state;
- the next missing lemma.

Copy reviewed source text without mathematical alteration when practical. Keep branch-local IDs visible as `PR<number>:<claim-id>`. Preserve a false original beside any repaired theorem; a repair receives its own identity and review boundary.

## 7. Review integrated wording

A byte-identical proof import generally needs structural and provenance review. A synthesized wrapper, corrected statement, changed normalization, or conjunction of several reviewed results needs a narrow mathematical review of the exact integrated wording.

Until that review passes, use a conservative status such as `SOURCE-QUALIFIED` with component results verified at exact SHAs and the integrated statement marked pending review. Do not promote a synthesis merely because all ingredients passed separately.

## 8. Record durable status and residency

Keep these dimensions independent:

```text
mathematical_status
integration_status
promotion_state
proof_residency
dependency_residency
```

Typical durable states are:

```text
exact reviewed theorem with local proof:
  mathematical_status = verified
  promotion_state     = accepted_with_local_proof
  proof_residency     = local_proof_packet
  dependency_residency = local or source-pinned

reviewed components with an unreviewed synthesis:
  mathematical_status           = source-qualified
  component_mathematical_status = verified_at_exact_source_shas
  integrated_statement_status   = pending_narrow_review
  promotion_state               = accepted_reference_record

open or proposed roadmap obligation:
  mathematical_status = open or proposed
  promotion_state     = roadmap_accepted
  proof_residency     = open_obligation
```

Repository residency does not upgrade mathematics. Local proof residency does not imply that every dependency is local or that a large computation was replayed.

## 9. Supersede, archive, and close safely

Before recommending or carrying out closure, re-query the current source head and ensure every valuable component has a durable destination:

- accepted claims and alternative proofs;
- refutations and exact counterexamples;
- artifacts, manifests, and replay status;
- source-qualified or blocked claims with their reasons;
- open questions in a successor issue or PR;
- exact review and cutoff records.

Leave a closure comment stating whether the PR was merged, absorbed, superseded, rejected as a monolith, or simply concluded, and link every durable destination. Closure is repository hygiene, not a mathematical verdict. Never close a source PR merely because a headline failed or because another branch overlaps it.

## 10. Preserve exploratory freedom

Exploration requires only enough discipline to remain intelligible later:

- map and normalization;
- visible status;
- finite-versus-global and ordinary-versus-2-adic scope;
- honest evidence level;
- unresolved step.

No registry entry or lifecycle form is required before exploration. The stronger contract applies only when work seeks review, integration, merge, supersession, archival promotion, or closure.

## 11. Leave an executable handoff

A fresh integrator should be able to determine:

- the previous cutoff and current `main`;
- which heads or dependencies changed;
- which claims remain unreviewed or source-pinned;
- which packets should be extracted or reviewed next;
- which lifecycle recommendations are advisory and which actions were executed;
- what must be preserved before later closure;
- which lightweight checks to run.

Add new dated evidence rather than altering frozen records. Keep current scientific orientation in the research map and catalog; keep detailed historical state in the archive.

## 12. Run only proportionate checks

Run the cheap structural validator:

```bash
python tools/check_integration_state.py
```

Also use link, JSON, formatting, and small packet-specific exact checks when needed. Integration hygiene does not justify a broad Collatz census, proof search, large replay, or new workflow. The validator checks structure and status consistency; it does not verify mathematics.
