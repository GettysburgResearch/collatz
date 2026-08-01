# Durable proof-import plan for the initial candidate-canonical records

## Purpose and repository layout

The eight initial records in PR #84 are **candidate canonical reference records**. Their underlying mathematics was reviewed at exact source SHAs, but the proof-bearing files are still resident only on source PR commits. Exact-SHA references preserve provenance; they should not be the sole long-term proof home.

Use this lightweight layout:

```text
claims/integrated/<canonical-id>/
  MANIFEST.md
  statement.md
  source/
  alternatives/
  reviews/
  artifacts/
```

Rules:

1. Source files are copied byte-for-byte when possible. Editorial wrappers may explain status, namespace and scope, but must not silently alter the proof.
2. A synthesized corrected statement receives its own clean file and a narrow independent review. It is not declared reviewed merely because its ingredients were reviewed.
3. Branch-local IDs remain visible as `PR<number>:<claim-id>`.
4. Refuted statements are preserved beside, not replaced by, their repairs.
5. `proof_residency` advances from `frozen_source_reference` to `local_proof_packet` only after the packet is on main.
6. A source PR may close only after its unique accepted content, review evidence, artifact state and open questions have durable destinations.

## Import order

```text
1. IC-EXTRACT-001
2. IC-GHOST-001
3. IC-AUT-001
4. IC-PERIODIC-001
5. PR #76 coefficient-gate base, then IC-SC-001
6. IC-RIG-001
7. PR #16 centered ordinary-section dependencies
8. IC-REF-001, then IC-REP-001
```

The ordering is about durable dependencies, not mathematical importance.

---

## IC-EXTRACT-001 — ordinary extraction by stabilization

### Primary source

PR #57, frozen `f12e6ec45a88da98b64ef97bdfd25c3c7d48b435`:

```text
research/ordinary-extraction/claims/D-7601-nested-legal-cylinder-tree.md
research/ordinary-extraction/claims/L-7601-signed-stabilization.md
research/ordinary-extraction/claims/T-7601-bounded-minimum-extraction.md
```

Review:

```text
research/positive-coefficient-gate/reviews/PREPUBLIC-PR56-PR57-PR60.md
@ 1c25b5e4be25a7c73b78e80b505c54879f02d8f1
```

### Alternative proofs to preserve

```text
PR #3  @ caa775e85a3618a6cce0bbad345300aaefeab640
  claims/theorems/T-0043-universal-ordinary-extraction-barrier.md

PR #56 @ 53ed4e49be522052405e6aa2c11b2b810a01bf2a
  research/global-extraction/claims/T-7801-ordinary-extraction-dichotomy.md

PR #60 @ 1221ef5639bd89b56a0583a58f0b2fc63af52931
  research/global-blocker-review/claims/T-7401-archimedean-tightness-extraction.md
```

### Import decision

- Copy the PR #57 definition/lemma/theorem files without mathematical alteration.
- Put alternative proofs under `alternatives/PR3`, `alternatives/PR56` and `alternatives/PR60`, or preserve exact links in the manifest if copying would duplicate too much.
- Do not create four canonical theorem IDs.
- Add a manifest explaining that the canonical summary combines the signed single-chain and nested-set statements.

### Review required

`REVIEW REQUIRED`: compare the integrated summary sentence-by-sentence with `L-7601/T-7601`, especially the negative boundary, positivity, nesting and minimum quantifiers. This is a narrow equivalence/scope review, not a new Collatz proof review.

### Closure gates

- PR #57 cannot close until IC-EXTRACT-001 and IC-GHOST-001 are local and `L-7610` has a verdict.
- PR #3 cannot close until its unique algebraic/firewall claims are separately imported.
- PR #56 cannot close until `R-7801` has a separate durable packet.
- PR #60 cannot close until `R-7401` and its historical review note are preserved.

---

## IC-GHOST-001 — explicit `1110` completion ghost

### Source

PR #57 at `f12e6ec45a88da98b64ef97bdfd25c3c7d48b435`:

```text
research/ordinary-extraction/claims/T-7602-supercritical-ghost-schedules.md
```

Accompany with the finite parity-cylinder definitions proved in that file; `D-7601` is useful context but not a load-bearing dependency of the explicit arithmetic.

### Import decision

Copy the source theorem unchanged. Add a short canonical manifest identifying the particular `1110` corollary used by IC-GHOST-001.

### Evidence boundary

The theorem is symbolic. Small exact replay was reported; no large computation is involved. Do not label it an empirical or computational theorem.

### Review required

`REVIEW REQUIRED`: verify only that the manifest’s specialized wording follows from the source theorem and that `-19/11` is described as a 2-adic integer but not an ordinary integer. Do not infer anything about arbitrary schedules.

### Closure gate

Shares PR #57’s closure gate with IC-EXTRACT-001.

---

## IC-AUT-001 — fixed-depth cofinite-tail obstruction

### Source

PR #14 at `9e3d90f50a6bf908401d2a2556513077daca3eb4`:

```text
research/safety-quotient/claims/D-9201-finite-safety-language.md
research/safety-quotient/claims/L-9201-cofinite-tail-obstruction.md
experiments/X-9201-sink-stripped-safety/
```

Review:

```text
reports/gpt56-pro-03/2026-08-01-prepublic-review-pr3-pr14-pr16-pr19.md
@ 3d2b0a3c7e873388c42f00c5cbb4f09cf9897391
```

### Import decision

Copy `D-9201/L-9201` without mathematical alteration. Import the experiment only as a bounded artifact with replay instructions and its declared depth cap.

### Review required

No new theorem synthesis is needed. A structural review should check that canonical-word conventions, inclusive depth and the empty continuation remain intact.

### Closure gate

PR #14 may close after the proof packet, bounded artifact manifest and exact review pointer are on main.

---

## IC-PERIODIC-001 — periodic tails and the complete denominator

### Sources

```text
PR #61 @ 8a85b6c96d677143e08568477c26a232d56263a9
  research/periodic-extraction/claims/T-7401-eventual-periodicity-full-denominator.md

PR #62 @ 20a4d5d7ba9d9a2b5e7a4dfecb83f6220bb7da36
  research/ordinary-extraction/claims/T-7701-eventually-periodic-supercritical-firewall.md

PR #63 @ 3011e6a78bd572c0c15a5b6112904f9c492ef29a
  research/ordinary-extraction-review/claims/L-7501-periodic-shortcut-fixed-point.md
  research/ordinary-extraction-review/claims/T-7501-no-eventually-periodic-divergent-parity.md
```

Review:

```text
reports/gpt56-crossmodel-audit-01/2026-08-01-prepublic-pr61-pr63-review.md
@ e85a9bb709da369852d2b0044a76005082a82897
```

### Import decision

This record is a **corrected synthesis**, not a verbatim copy. Create:

```text
claims/integrated/IC-PERIODIC-001/statement.md
```

with the all-zero endpoint separated explicitly, and copy the three source proof families unchanged under `source/`. Preserve PR #63’s least-positive-root escape formula as a stronger companion theorem.

### Review required

`REVIEW REQUIRED`: independently review the precise synthesized statement, including:

- `w` nonempty;
- `s=0` all-zero endpoint `x=0`;
- sign of `2^L-3^s`;
- full-denominator divisibility;
- exact parity replay;
- finite preperiod positivity;
- accelerated/controller symbols only after a fixed parity-block emission theorem.

The earlier source reviews do not by themselves certify the new merged wording.

### Closure gates

PRs #61/#62/#63 may close only after the corrected statement receives this narrow review, source proofs are local, and PR #61’s post-review `O-7401` has a verdict.

---

## IC-SC-001 — divergence and coefficient-stopping/source-escape equivalence

### Source chain

First import the corrected base from PR #76:

```text
PR #76 @ 2ee4a6cb04b23cc0c602e5bd3d18908fe7b97dcf
  research/positive-coefficient-gate/D-6701...
  research/positive-coefficient-gate/T-6708...
```

Then PR #77 at `3efcbfb2e38f02b04eb6bba35eb258ec552d655c`:

```text
research/positive-coefficient-gate/T-6709-supercritical-implies-divergence.md
research/positive-coefficient-gate/T-6710-SC-star-inverse-stopping-equivalence.md
research/positive-coefficient-gate/L-6711-canonical-low-band-source-endpoint-bound.md
```

Review:

```text
reports/gpt56-complexity-01/2026-08-01-pre-public-review-76-77-79.md
@ 046eeda2268b4ac1b90a9618a4ed2460a111a0e5
```

### Import decision

- Land the PR #76 fixes first.
- Copy PR #77 theorem files without changing proof bodies.
- Put terminology corrections in an integration wrapper or a separately reviewed clean copy: use “universal finite coefficient stopping,” not the stronger literature equality conjecture.
- Do not import current PR #77 `M-6712` until its own review.

### Review required

`REVIEW REQUIRED`: check the wrapper’s terminology and that the candidate record combines two distinct statements without implying SC* itself:

1. all-supercritical ordinary orbit implies divergence;
2. source escape is equivalent to universal finite coefficient stopping.

### Closure gates

PR #76 must merge or be imported first. PR #77 may close only after IC-SC-001/RD-SC-001 are local and `M-6712` has a verdict.

---

## IC-RIG-001 — finite tame six-branch sections

### Source

PR #64 at `88884c3e590b08aeb2018872987e71e14de1fe7b`:

```text
research/six-branch-extraction/claims/D-7401-six-branch-minimal-word-system.md
research/six-branch-extraction/claims/L-7401-high-quotient-section.md
research/six-branch-extraction/claims/T-7401-affine-section-rigidity.md
research/six-branch-extraction/claims/T-7402-finite-affine-nucleus-rigidity.md
research/six-branch-extraction/claims/T-7403-finite-rational-nucleus-rigidity.md
research/six-branch-extraction/claims/T-7404-no-semilinear-sanctuary.md
```

Review:

```text
reports/gpt56-cartographer-01/2026-08-01-pre-public-review-pr64-pr65-pr66.md
@ 591a06ad914b63dddfd65ee658dbec36291ffbc0
```

### Import decision

Copy all six files together; they form one dependency packet. Keep `T-7401` etc. as source IDs inside the files and use `IC-RIG-001` only in the manifest. Do not silently add the PR #65 algebraic extension or the PR #45 physical Collatz crosswalk.

### Review required

A structural review should confirm that the manifest retains:

- the exact `P=3^12`, `Q=2^19`, six-digit chart;
- complete-tree/full-tail hypotheses;
- finite-control and eventual-integrality hypotheses;
- semilinear-set scope;
- no claim about least-root boundedness or escape.

### Closure gates

PR #64 may close after the packet is local and PR #66/PR #65 point to it. PR #65’s extension remains separately reviewable.

---

## IC-REF-001 — preserved refutation of `T-9318`

### Source

PR #37 at `a518db7feece37513ddcda729553e8b8c4c4d657`:

```text
research/adelic-cusp/claims/T-9318-factor-complexity-cylinder-barrier.md
research/adelic-cusp/claims/R-9304-t9318-constant-word-counterexamples.md
reports/gpt56-review-9315-01/
```

### Import decision

- Preserve `T-9318` in its refuted form without correcting its theorem body.
- Import `R-9304` as the exact counterexample record.
- Resolve the `R-9304` collision only through branch qualification/canonical manifest, not by erasing the source ID.

### Review required

No new mathematics is needed, but the import review must ensure the original and counterexample remain linked and the evidence does not depend on the finite scan.

### Closure gate

PR #37 cannot close until both the refutation and the distinct repair are local.

---

## IC-REP-001 — nonconstant factor-complexity repair

### Source

PR #37 at `a518db7feece37513ddcda729553e8b8c4c4d657`:

```text
research/adelic-cusp/claims/T-9319-nonconstant-factor-complexity-cylinder-barrier.md
```

Dependencies from PR #16 at `87478352e65c7b816dfc8b3b30894b71fb50f662`:

```text
research/adelic-cusp/claims/T-9316-...
research/adelic-cusp/claims/L-9313-...
research/adelic-cusp/claims/T-9315-...
```

Use the exact filenames recorded in the PR #16 claim index when constructing the import packet.

### Import decision

Import only after the centered ordinary-section dependency packet. Copy `T-9319` unchanged and link it to IC-REF-001.

### Review required

The existing independent review covers the theorem. The import review should verify dependency filenames/SHAs, nonconstancy, strict slope inequality, and the induced `64→81` scope.

### Closure gate

Shares PR #37’s closure gate with IC-REF-001.

---

## What may be wrappers, and what may not

Allowed without mathematical re-review:

- manifests;
- provenance tables;
- branch-qualified aliases;
- evidence/replay labels;
- links to exact reports and artifacts;
- a statement that a source file retains author status.

Requires narrow mathematical review:

- merged statements assembled from multiple source theorems;
- corrected all-zero or endpoint clauses;
- terminology changes that could affect quantifiers;
- dependency substitutions;
- any statement stronger than a verbatim reviewed source.

## Completion criterion for the proof-import program

The initial reference layer is operationally complete when every candidate-canonical record has:

1. an accepted repository promotion state;
2. a local proof packet or an explicit temporary exception approved by the integrator;
3. exact dependency pins;
4. review and artifact evidence on main;
5. a closure-safe provenance manifest for every absorbed source PR.
