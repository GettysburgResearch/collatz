# Next two integration waves

## Operating rule

Each wave begins by recording:

- current UTC and Asia/Jerusalem time;
- current `main`;
- every open source PR head;
- the previous lifecycle-ledger version;
- every changed head classified as editorial, review-only, proposed, computation-only or theorem-bearing.

Never rewrite the `2026-08-01` snapshot. Create a new dated continuation and update `docs/integration/CURRENT.md`.

---

# Wave A — coverage and delta repair

## Scope

### A1. Review the three unreviewed source PRs

```text
#67  centered height-renewal atlas
#68  bounded transported run-core closure
#69  q=71 reset-pattern spine
```

For each:

1. freeze the current head;
2. reconstruct the uniform symbolic claim separately from the bounded artifact;
3. audit dependencies on #44, #53/#51, or #12;
4. classify proof, checker, regeneration and full-replay states separately;
5. assign a mathematical verdict and lifecycle disposition.

### A2. Review post-review theorem/proposal deltas

```text
#13  proposed PR19 source repair
#57  L-7610
#61  O-7401
#65  L-7502
#77  M-6712
#83  L-6916
```

The older package verdict remains frozen. Review only the delta unless the base changed materially.

Priority:

1. #83 `L-6916`, because it is theorem-bearing in the active FC* lane;
2. #57 `L-7610`, because #57 is a primary proof source;
3. #65 `L-7502`, because the algebraic packet overlaps PR #3;
4. #13’s proposed source repair, because PR #19’s blocked source claim depends on it;
5. #61 `O-7401`;
6. #77 `M-6712`.

### A3. Reconcile heads changed after the continuation observation

If any source PR moves:

- preserve the old current-head observation;
- compare old/current SHAs;
- classify the delta;
- do not inherit the previous verdict;
- update only the new lifecycle continuation, not the frozen snapshot.

## Wave A completion criteria

Wave A is complete when:

- #67/#68/#69 have exact-SHA verdicts;
- all six named post-review additions have exact verdicts;
- every source PR current head has a delta classification;
- `pr-lifecycle.json` has no `UNREVIEWED` row unless a newly opened source PR is explicitly added to a later population;
- every theorem-bearing delta is either reviewed, reverted, split or explicitly deferred;
- the promotion audit is updated if any candidate-canonical dependency changed;
- a new post-cutoff observation records `main` and open-PR state.

## Wave A outputs

```text
docs/integration/<new-date>/
  CURRENT_HEADS.md
  REVIEW_DELTAS.md
  pr-lifecycle.json
  PR_LIFECYCLE.md
  HANDOFF.md
```

No source PR is closed merely because Wave A assigns a verdict.

---

# Wave B — clean extraction and repository cleanup

## B1. Import the initial proof packets

Use `PROOF_IMPORT_PLAN.md` in this order:

```text
IC-EXTRACT-001
IC-GHOST-001
IC-AUT-001
IC-PERIODIC-001
PR #76 base -> IC-SC-001
IC-RIG-001
PR #16 centered ordinary-section dependencies
IC-REF-001 -> IC-REP-001
```

Every import has a manifest with source PR/SHA, source IDs, review report, dependencies, evidence and closure-safe provenance.

## B2. Extract the mixed packets

Required clean extractions:

```text
#11  rejected monolith:
     preserve exact refutations and freshly reviewed narrow salvage

#19  H packet:
     exact native core; source/computation-qualified claims separate

#34  cross-direction forge:
     verified claim subsets and PR81-required full-order interfaces

#42  cycle packet:
     passing symbolic claims, artifact manifests, blocked headlines separate

#47  integer-first packet:
     extraction firewall and reviewed full-denominator claims separate
```

Also complete planned extractions from #3/#16/#32/#35/#45/#50/#56/#60/#61/#62/#63/#72 as recorded in the lifecycle ledger.

## B3. Resolve dependency debt

At minimum:

- move accepted PR #82 statements needed by PR #81 into an active clean packet;
- pin exact PR #34 sources needed by PR #81;
- land PR #76 before PR #77;
- import PR #64 before PR #66 and before any algebraic extension;
- import PR #16/PR #33 before PR #44;
- import PR #48 corrections before PR #49/#51;
- stabilize PR #53 before PR #70 and any accepted #68 material;
- resolve all bare-ID collisions through canonical manifests and aliases.

## B4. Review synthesized clean statements

A clean import that merely copies a reviewed file needs structural review. A synthesized or corrected statement needs narrow mathematical review, particularly:

```text
IC-PERIODIC-001
IC-EXTRACT-001 combined wrapper
IC-SC-001 terminology wrapper
RD-BRIDGE-001
any PR #11 salvage
any merged PR #34/#42/#47 theorem packet
```

## B5. Reduce the open-PR count safely

Only after durable imports:

### Close as absorbed/superseded

Likely candidates:

```text
#3, #14, #16, #19, #32, #34, #35, #37, #38,
#42, #44, #45, #47, #50, #56, #57, #60, #61,
#62, #63, #64, #72, #74, #77
```

The exact final set depends on Wave A and whether active questions move to successors.

### Merge after fixes

Likely candidates:

```text
#6, #20, #33, #48, #66, #76, #79
```

### Keep open for active research

Current advisory set:

```text
#12, #13, #49, #51, #53, #70, #80, #81
```

This set should shrink when stable cores are imported and active questions move to focused successors.

### Rejected closure

```text
#11
```

Only after refutations and any newly reviewed salvage are durable.

### PR #74 trigger

Close as organizationally superseded only after:

1. PR #84 is independently reviewed and merged;
2. unresolved public-launch/security/licensing/settings work has a dedicated owner issue or checklist;
3. the closure comment points to PR #84, the lifecycle ledger and the owner work item.

## Wave B completion criteria

Wave B is complete when:

- every initial candidate-canonical record has a local proof packet or an approved explicit exception;
- every mixed packet has a claim-level extraction manifest;
- no accepted theorem depends only on an unmerged source PR or a closed unmerged PR;
- all source-ID collisions have branch-qualified aliases;
- every large artifact has an honest replay state;
- every recommended closure has a durable destination and comment;
- source PRs selected for closure are actually closed only after a final head re-query;
- the lifecycle ledger records the executed action and resulting main commit;
- exploratory research remains free to continue in broad or focused PRs.

## What the next integrator updates

After each wave:

1. create a new immutable dated directory;
2. update `docs/integration/CURRENT.md`;
3. advance registry promotion/proof-residency states;
4. update lifecycle current heads, dispositions and executed actions;
5. record merges/closures with exact commits and comments;
6. refresh the next-integrator handoff;
7. run the cheap structural checker and any small packet-specific checks;
8. do not run expensive searches merely for integration hygiene.
