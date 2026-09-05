# Reviewer D integration — disposition and evidence

This is a user-authorized localized integration, not another Collatz research wave or public-release clearance. The repository remains unsolved.

## Frozen inputs

- Main reviewed and edited: `cd1b3689e8d37fc4232945072e2faf6bd5ee47bd`, tree `99f330473ab64fc31f2bc7b194cc482c3c2839ce`.
- D final PR98 head: `1c7744bcb9ded9336036919ffc7a19b5576ea58e`; first review `0ce01f9cff107745abc3dabb8b1faa27ab6acfd4`.
- The nine-file D directory is copied unchanged with tree `7f6ea329c06af44e836e7e2d88ad694654bd0d55`. Its historical publication statements and all 44 original plus six finishing rows remain intact.

Read [D's final handoff](../reviewer-d/FINAL_HANDOFF.md), [the separate follow-up record](../../../claims/followups/reviewer-d-2026-09-05.json), and [the active errata](../../../research/integrated/ERRATA.md). A/B's matrices, assignment manifest and checker are not extended to include this overlapping review. D's evidence-only rows do not become mathematical approvals.

## Complete finding disposition

| Finding | Implemented integration action | Retained boundary |
|---|---|---|
| FD-01 / E-D-001 | Correct the signed-digit adversarial example; display `-2^J`. | Signed stabilization core unchanged; nonzero digits alone exclude nonnegative, not all ordinary, values. |
| FD-02 / E-D-002 | Separate positive realization from a nontrivial-cycle certificate; specify deterministic, fixed-block, productive control. | `10` and `01` remain trivial positive realizers; the exact periodic synthesis is still pending narrow review. |
| FD-03 / E-D-003 | Separate `m_0=1` from `R_empty=0`; correct the high-quotient increment. | The positive-depth root/cap recurrence survives; no least-root escape is established. |
| FD-04 / E-D-004 | Warn at both factor dependency and centered/adelic catalog surfaces. | The constant-code zero-completion exception does not refute the ordinary recurrence cone or nonconstant repair. |
| FD-05 / E-D-005 | Keep closed-strip support and show endpoint/open-cylinder counterexamples at both surfaces. | Positive ordinary bridge survives; the factor screen still needs only nonconstancy. |
| FD-06 / E-D-006 | Remove the unqualified polynomiality-to-rigidity application; list the missing section hypotheses. | Polynomiality survives; the unsupported application remains GAP-BLOCKED. |
| Overlap / E-D-007 | Quantify the OPEN target over each fixed source and every feasible length. | No universal emptiness or extraction theorem is claimed. |
| Old PR65 debt / E-D-008 | Preserve the previously recorded constant, finite-difference, coefficient-field and Puiseux-source qualifications. | Neither a new D discovery nor an implemented proof repair; no broad algebraic-branch promotion. |

All eight items have an active destination. The replacement prose is explicitly **PROPOSED pending narrow independent review of its exact wording**. Old erroneous statements are preserved as history, not left as unqualified current guidance. [Seven pre-correction source bodies](../../../archive/reviewer-d-2026-09-05/README.md) remain byte-identical, with original and active Git blobs in the follow-up record. The only theorem-page edits are those localized above; there is no wholesale proof rewrite.

## Validation actually executed

D's two exact Python programs were materialized and their Git blob hashes matched the published originals before execution. Their regenerated reports also matched the original Git blobs, not just a printed digest. Both then passed `--check --self-test` normally and under optimized Python. Each suite rejected its eight specified resealed corruptions in each mode; this is 16 distinct mutation cases replayed in both modes, not a new independent review of D's mathematics.

```text
targeted report: f68f0babd04b680fe9bbd47da82cc5e6014c38ba8b54400426e437db767f6174
final report:    e0563b820b0cd7c24c6ba159af5a944209bb101693fc4d4b8584144685991ddb
```

The follow-up-owned [scoped checker](check_followup.py) passed in both modes: seven exact active files, seven exact archived originals, all eight dispositions, 1,584 signed residues, 81 quotient/output identities and 64 exact overlap-band boundary cases. It rejects eight altered scoped fixtures in each mode. These finite checks support the edit contract, not universal theorem correctness. See [the execution record](validation.json) and [logs](logs/).

From a complete checkout, replay with:

```bash
python -B reports/prepublic-2026-09-05/reviewer-d/targeted_checks.py --check reports/prepublic-2026-09-05/reviewer-d/checks.json --self-test
python -O -B reports/prepublic-2026-09-05/reviewer-d/final_checks.py --check reports/prepublic-2026-09-05/reviewer-d/final_checks.json --self-test
python -B reports/prepublic-2026-09-05/integration-d/check_followup.py --self-test
```

## Operational and scientific ceilings

**No complete authenticated checkout was available in this session:** direct Git failed at DNS resolution. The executions above used byte-authenticated D programs/reports and the exact affected-file surface, not a disguised full repository fixture. Neither `tools/check_integration_state.py` nor `tools/check_review_integration.py` is claimed to have run against the full final checkout. GitHub tree/diff readback during publication is separate from those executions. Run both existing commands on a pristine complete checkout and retain the final commit and outputs in [launch issue96](https://github.com/GettysburgResearch/collatz/issues/96).

PR97's onboarding/security contribution is separately inventoried and not absorbed here. Its Windows executable-mode report does not authorize weakening A/B's preservation contract; its earlier validation/security receipts are not this final-tree receipt. Licensing/provenance, privacy/security, visibility and branch-policy decisions remain with the owner. No license, workflow, setting, permission, visibility or history change is made.

The original eight canonical and three roadmap records retain their statuses. The old periodic synthesis and bridge, E-INTEGRATION-001/002, the four newer reference assemblies, external proof/certificate ceilings and unreviewed #67/#68/#69 boundaries are unchanged. No large corpus, external Lean build, PDF/payload replay, complete recent-source re-review or Collatz closure is asserted.

## Lifecycle

The publication PR and its post-merge receipt identify the actual integration and final main commits. After verifying D's entire frozen directory resident and rechecking its head, the review-only PR98 may be closed as absorbed with a destination comment. No mathematical source PR is closed or rewritten by this follow-up. New source deltas require their own review.
