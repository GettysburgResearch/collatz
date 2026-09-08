# Scoped extraction and integration handoff

This is an actionable plan based on the exact mathematical review, not a completed merge. Use current main as the starting tree; the review used `421d570d6ffb917c9090b9e8ca3c2aa58e26647c`. Recheck for subsequent changes. Do not merge an old research branch wholesale over later MIT/onboarding edits.

## Extraction units and order

| Unit | Copy from frozen source | Why it stands alone / dependency order |
|---|---|---|
| Critical tails | PR105 `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`: root files of `research/astra-tail-transport`, X-ATT-001, author report 01 | Old moving rank and exact acceleration are resident dependencies. Keep ATT-006's escape and cycle parts distinct. Apply F01 to the active verifier after preserving source identity. |
| Repeated-spike clearance | Same head: `research/astra-tail-transport/repeated-spikes`, X-ATT-002, author report 02 | Follows the old-R/tail definitions. Preserve the forest's positive all-future residual and all outside-ball vertices. Do not replace ATT-001–006 by this later packet. |
| Expanding-word rho | Same head: `research/astra-tail-transport/expanding-word-rank`, X-ATT-003, author report 03 | Independent rank program; does not mathematically depend on the numerical forest. Retain its exact illegal-minimum and forward-delay refutations. Apply F01 to its verifier. |
| Linear P-frontier | PR106 `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`: root files of `research/astra-linear-frontier`, X-ALF-001, author report 01 | Depends on the old exact inverse shield. Linear precision improves, rather than invalidates, the older coarse bound. Keep both guarded repayment and compressed convergent families. |
| Actual-prefix Gamma | Same head: `research/astra-linear-frontier/prefix-rank`, X-ALF-002, author report 02 | The core rank proof is local and does not depend on ALF's hard-family theorem or ATT's forest. Retain general primitive-period selection, its unprescribed-prefix proof, and the separate spike paper. |

[inventory.json](inventory.json) lists every one of the 46 paths. Their added path sets are disjoint. Preserve all experiment reports and author/publication receipts, including historical statements that a write had not happened at the author's cutoff. Later verified publication belongs in the integration receipt, not in a rewritten author history.

## Four ranks and four clocks must stay separate

| Object | Exact interpretation |
|---|---|
| P | `(2n+1)^2/3^v3(2n+1)`, with the specified section domain and absorbing convention. ALF's box uses completed first returns to the positive `1 mod3` section. |
| R_* | The previously integrated moving-component rank and maximal repeated `1^a0` acceleration A. ATT's B/H is the **quarter-unsafe** return/operator, not the enlarged-safe return. |
| rho | Minimum over unreduced formal expanding-word forms plus three base forms. It can select a physically illegal word; the 5/4 gap and strict length cutoff are indispensable. |
| Gamma | Minimum over **actual, nonzero** prefix displacements of raw T. A visit to 1 does not redefine subsequent raw iterates in this rank; Gamma(1)=0 is a separate convention. Its safe operator is killed on unsafe entry as well as 1. |

A raw shortcut clock, a section-return count, a maximal repeated-word module and an unsafe-return count are not interchangeable. Rank minima, rank spectra and initial measures cannot be transferred without a new theorem.

**Separate proposed review observation, not a new accepted comparison theorem:** bounded exact computations give `(rho(7),Gamma(7))=(12,49)` and `(rho(14),Gamma(14))=(75,48)`. Thus neither prospective global pointwise ordering can simply be assumed. Rho's proved comparison with R_* does not establish one for Gamma. The forest input `1_U/R_*^2` and its residual cannot be relabeled `1/rho^2` or `1/Gamma^2`.

## Cumulative scientific destinations

Extend existing guides; do not create a latest-wave dashboard or relocate the older proof spine.

- **Exceptional mass:** add the sharp source/fixed-clock tail distinctions, the two measure defects and the forest certificate's fixed positive residual. Keep the native no-descent, source-qualified predecessor and fixed-floor programs visible. New tail theorems do not supply the missing predecessor-basin estimate.
- **Renewal and transport:** place ATT's one-return fractional bound next to the failure of envelope renewal, and the forward-closed forest next to its genuine no-feedback hypothesis. Put the all-J l1 norm-one obstruction beside the positive fixed-input bound. Gamma's raw moment counterexample must not be labeled an induced-return obstruction.
- **Rank merging:** add linear precision and completed-section box bounds; describe rho and Gamma separately with properness, computation, positive families and failure modes. Keep the older complete inverse fan, resource bounds and 121 controls accessible. Do not overwrite either new rank with the other.
- **Results catalog / research map / status:** carry the exact reviewed source claims and explicit open targets. A useful cumulative headline is the finite actual-prefix evaluator and all-primitive-period finite-horizon theorem, not “all unsafe orbits now contract.” Continue to display earlier accepted results and all later restrictions.
- **Evidence:** keep this review, source identities and execution ceilings behind the scientific entry points. Author-stage PROPOSED headers may remain in exact imports with a clear claim-level review overlay. No existing canonical or A/B/D manifest should be repurposed to pretend this work was reviewed earlier.

The optional SC* interpretation should point explicitly to the existing distinct-orbit theorem `T-A3-451` in `research/astra-three-routes/pass2/SC_TAIL_AND_ECHO.md` (current resident blob `c388be4b4aa6b9293fcf1c973742c8e6648c0375`) as well as its Mellin input. It does not promote the older pending periodic synthesis or SC*/FC* roadmap wording. Neither an external predecessor exponent nor background Lyapunov/ergodic literature is a premise of the new core proofs.

Newly written joint arguments, theorem reformulations or stronger consequences require their own narrow review. Copying the exact source proofs and adding faithful navigation is not a new theorem. Do not require a broad repeat review of unaffected older mathematics.

## Apply the prepared software repair on the candidate branch

After extracting the exact source files, from the repository root:

```bash
python -B reports/post-integration-2026-09-08/prepare_checker_fixes.py --root .
python -B reports/post-integration-2026-09-08/prepare_checker_fixes.py --root . --apply
python -B reports/post-integration-2026-09-08/prepare_checker_fixes.py --self-test
python -O -B reports/post-integration-2026-09-08/prepare_checker_fixes.py --self-test
```

The first command is a nonwriting exact-source preflight. Preserve the two originals by their source SHA/blob and record the two new verifier blobs. The canonical source artifacts should remain byte-identical. Extend the actual verifier self-tests with resealed integer/boolean/float substitutions; a no-op test must compare canonical encodings rather than Python numeric equality for these cases. The helper's isolated tests do not substitute for executing the patched full verifier against its artifact.

## Candidate-tree acceptance checks

Run the five native generators in `--check` mode and both normal/optimized verifiers with `--self-test`, using the commands in their experiment READMEs. ATT-003 uses `--check`, not a made-up generator `--output` interface. Do not count newly written code as having inherited an older execution receipt.

Run the complete-checkout structural command on the exact staged commit:

```bash
python -X utf8 -B tools/validate.py --regressions --receipt ../collatz-integration-validation.json
```

Preserve stdout, stderr, exit codes and the commit/tree; inspect any failure without weakening frozen source/status protections. The new source programs use standard-library arithmetic but should still run in an isolated environment without repository secrets. A green result is not a Collatz proof or a new external-certificate replay.

Recheck #105 and #106 heads, main and all newly linked paths before merge. Review subsequent head deltas separately. Use a normal integration PR and the project's core-review process; no visibility, membership, workflow, license or branch-rule change is needed. Only after actual landing and preservation should source PR lifecycle decisions be made, with exact destinations and continuing open obligations documented.

## Scientific work still worth doing

The smallest useful continuation for Gamma is to analyze the residual odd-minimizing-displacement states or prove a genuinely reusable estimate for their induced return, not to assume periodic guards renew. For the forest route, a theorem forcing a cofinal family of certified clearances is the genuine global step. For the linear frontier, a rank-specific bounded-box obstruction is a reason to study a justified switching interface, not a reason to reject all merging. These remain open research, distinct from the mechanical integration checks above.
