# Focused promotion-boundary audit for PR #84

## Status of this audit

This is an **integrator’s focused source-and-scope audit**, not independent review of PR #84. It checks that the eight selected records are responsibly presented for review. It does not promote them and does not re-prove their mathematics.

At the continuation observation:

```text
PR #84 branch head at start: 390969210c5c168c52ba2795b7c3400e57a6d2e8
main:                       0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84
source PR heads changed:    none
```

## Promotion boundary

The registry now uses four orthogonal dimensions:

1. `mathematical_status` — status of the statement at its reviewed source SHA;
2. `integration_status` — intended repository role such as `canonical` or `roadmap`;
3. `promotion_state` — whether the record is merely selected in a draft or accepted on main;
4. `proof_residency` — frozen-source reference versus a local proof packet.

For this draft:

```text
eight initial records:
  integration_status = canonical
  promotion_state    = candidate_in_draft_pr
  proof_residency    = frozen_source_reference

roadmap records:
  integration_status = roadmap
  promotion_state    = roadmap_candidate_in_draft_pr
```

The source claim headers remain untouched. Several correctly still say `PROPOSED`; PR #37’s refutation/repair files say `REFUTED` or `PROVED`. Repository acceptance is not back-written into author history.

Only a later independently reviewed merge of PR #84 may change a candidate to `accepted_reference_record`. A later proof import may change `proof_residency` to `local_proof_packet`.

## Record-by-record audit

### IC-EXTRACT-001

**Source/path check:** matched.

```text
PR57 @ f12e6ec45a88da98b64ef97bdfd25c3c7d48b435
  L-7601-signed-stabilization.md
  T-7601-bounded-minimum-extraction.md

alternatives:
  PR3:T-0043
  PR56:T-7801
  PR60:T-7401
```

**Scope check:** the candidate wording matches the reviewed single-chain signed boundary and nested positive-set minimum theorem. It does not assert nonemptiness or boundedness for a Collatz-derived family.

**Review still required:** confirm that the combined summary is exactly equivalent to the two PR #57 statements and that alternative proofs are aliases rather than additional canonical claims.

**Evidence check:** symbolic proof only; no computation is implied.

### IC-GHOST-001

**Source/path check:** matched.

```text
PR57:T-7602
research/ordinary-extraction/claims/T-7602-supercritical-ghost-schedules.md
```

**Scope check:** the record uses only the explicit `1110` specialization and the finite parity-cylinder theorem. It says the unique completion is `-19/11 in Z_2 \ Z`; it does not call this a positive orbit or counterexample.

**Review still required:** only the specialization/wrapper and terminology.

**Evidence check:** small exact replay is described as supporting arithmetic, not as a large proof-producing computation.

### IC-PERIODIC-001

**Source/path check:** matched.

```text
PR61:T-7401 @ 8a85b6c96d677143e08568477c26a232d56263a9
PR62:T-7701 @ 20a4d5d7ba9d9a2b5e7a4dfecb83f6220bb7da36
PR63:L-7501/T-7501 @ 3011e6a78bd572c0c15a5b6112904f9c492ef29a
```

**Scope check:** the candidate wording keeps the whole denominator `2^L-3^s`, exact parity replay, and the raw-parity/fixed-block restriction.

**Correction boundary:** the all-zero endpoint is separated. The frozen source package verdicts remain `VERIFIED WITH FIXES`.

**Review still required:** this is a synthesized corrected theorem. An independent reviewer must validate the exact merged statement, especially the all-zero word, finite preperiod and controller-symbol scope.

**Evidence check:** the cited X-7710 audit was small. The record does not imply a period census or expensive search.

### IC-SC-001

**Source/path check:** matched.

```text
PR77 @ 3efcbfb2e38f02b04eb6bba35eb258ec552d655c
  T-6709-supercritical-implies-divergence.md
  T-6710-SC-star-inverse-stopping-equivalence.md
  L-6711-canonical-low-band-source-endpoint-bound.md
```

**Scope check:** one fixed positive ordinary source; moving compatible sources and completion ghosts are excluded.

**Correction boundary:** the candidate record uses “coefficient-stopping finiteness,” avoiding the stronger literature equality conjecture. It does not include the current unreviewed `M-6712`.

**Review still required:** check the terminology wrapper and ensure the record does not state SC* itself as proved.

**Evidence check:** symbolic; no large finite verification is claimed as replayed.

### IC-AUT-001

**Source/path check:** matched.

```text
PR14 @ 9e3d90f50a6bf908401d2a2556513077daca3eb4
  D-9201-finite-safety-language.md
  L-9201-cofinite-tail-obstruction.md
```

**Scope check:** fixed depth, LSD-first canonical encodings, terminal two-state canonical tail, and exact power-of-two nonclosure witness. No inter-depth sanctuary is claimed.

**Review still required:** structural import review only.

**Evidence check:** the bounded automaton artifact is not extrapolated.

### IC-RIG-001

**Source/path check:** matched.

```text
PR64 @ 88884c3e590b08aeb2018872987e71e14de1fe7b
  D-7401
  L-7401
  T-7401
  T-7402
  T-7403
  T-7404
```

**Scope check:** exact `P=3^12`, `Q=2^19` six-branch chart; complete-tree/full-tail finite affine/rational control and semilinear value-space scope.

**Exclusions check:** the candidate record excludes PR #65’s algebraic extension, the PR #45 physical crosswalk and the open least-root decision.

**Review still required:** verify the manifest does not merge the distinct theorem scopes more strongly than their conjunction.

**Evidence check:** only small table checks are reported; no large computation.

### IC-REF-001

**Source/path check:** matched.

```text
PR37 @ a518db7feece37513ddcda729553e8b8c4c4d657
  T-9318-factor-complexity-cylinder-barrier.md
  R-9304-t9318-constant-word-counterexamples.md
```

**Scope check:** the original unrestricted screen remains refuted by `0^infinity` and `1^infinity`; unaffected ordinary-itinerary portions are not described as refuted.

**Repair boundary:** the refutation is permanent and is not overwritten by IC-REP-001.

**Review still required:** structural preservation and collision-safe identifier handling.

**Evidence check:** exact counterexamples prove the result; the finite scan is corroboration only.

### IC-REP-001

**Source/path check:** matched.

```text
PR37:T-9319 @ a518db7feece37513ddcda729553e8b8c4c4d657
dependencies: PR16:T-9316, PR16:L-9313, PR16:T-9315
```

**Scope check:** nonconstant words, strict slope inequality and the induced `64→81` section only.

**Review still required:** verify exact dependency filenames/SHAs during import and preserve the strict/nonconstant boundary.

**Evidence check:** symbolic theorem; no computation required.

## Report and provenance audit

The report paths and report commit SHAs in the registry agree with the frozen review-coverage ledger. Key source and report blobs were fetched directly during this continuation. No verdict is extended beyond its `reviewed_sha`; current-head additions such as PR #57 `L-7610`, PR #61 `O-7401`, PR #65 `L-7502`, PR #77 `M-6712` and PR #83 `L-6916` remain outside older verdicts.

## Independent reviewer checklist for PR #84

### Repository structure

- [ ] Confirm the original `2026-08-01` snapshot is not rewritten by the lifecycle continuation.
- [ ] Confirm all 45 source PRs appear exactly once in `pr-lifecycle.json`.
- [ ] Confirm each lifecycle row has a disposition, action, prerequisites, closure criterion and durable destination.
- [ ] Confirm current heads were re-queried and post-cutoff observations are separate from frozen review facts.
- [ ] Confirm no lifecycle recommendation is presented as an executed merge or closure.

### Promotion semantics

- [ ] Confirm all eight initial records are `candidate_in_draft_pr`, not accepted on main.
- [ ] Confirm roadmap records use a roadmap-candidate state.
- [ ] Confirm mathematical status, integration role, promotion state and proof residency are independent.
- [ ] Decide whether merge of PR #84 is sufficient for `accepted_reference_record`, or whether selected records need individual acceptance exceptions.

### Mathematical scope

- [ ] Recheck IC-EXTRACT-001’s combined signed/nested statement.
- [ ] Recheck the `1110` specialization in IC-GHOST-001.
- [ ] Independently review the corrected synthesized wording of IC-PERIODIC-001.
- [ ] Recheck IC-SC-001’s terminology and fixed-source quantifiers.
- [ ] Recheck IC-AUT-001’s fixed-depth/canonical-language scope.
- [ ] Recheck that IC-RIG-001 is exactly the conjunction of the reviewed PR #64 claims.
- [ ] Verify that IC-REF-001 preserves the false statement and exact counterexamples.
- [ ] Verify that IC-REP-001 is separate and keeps the nonconstant/strict-slope hypotheses.

### Dependencies and evidence

- [ ] Confirm every source SHA, source path, review SHA and report path.
- [ ] Confirm source-qualified assumptions remain named and pinned.
- [ ] Confirm no large computation is described as independently replayed when it was only inspected.
- [ ] Confirm finite artifacts are not used as all-depth evidence.
- [ ] Confirm aliases do not identify merely related but non-equivalent statements.

### Roadmap bridge

- [ ] Review `RD-BRIDGE-001` as a proposed normalization/crosswalk theorem.
- [ ] Confirm the least-counterexample no-descent argument, Lane A/Lane B partition and cycle-minimum rotation.
- [ ] Confirm current definitions of SC* and FC* exactly match the two lanes.
- [ ] Confirm the trivial cycle and every possible nonconvergent positive orbit are handled.
- [ ] Do not describe the architecture as established exhaustive until this checklist item passes.

### Lifecycle and owner decisions

- [ ] Review the proposed #74 supersession trigger and durable closure comment.
- [ ] Review Wave A and Wave B ordering.
- [ ] Confirm every proposed source-PR closure has a durable content destination.
- [ ] Confirm exploratory contributors remain free to use broad research PRs.

## Result

The eight records are suitable **candidates for independent integration review**. This audit found no new source-path mismatch or obvious statement inflation, but it intentionally leaves the synthesized periodic statement, promotion decision and SC*/FC* bridge crosswalk for an independent reviewer.
