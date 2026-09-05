# Publication handoff — one review PR, not a research continuation

Intended repository: GettysburgResearch/collatz.
Intended base: `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
Suggested branch: `review/prepublic-2026-09-05-reviewer-b`.
Suggested title: **review: pre-public integration B — PR91/92 mathematics and public reading path**.

No remote review PR was created here. GitHub tool discovery exposed reads but no write action. Plugin discovery found the installed GitHub connector, not an alternative publishing action. Git attempts failed to resolve github.com; `gh` was not installed. No credentials were copied or inferred from download URLs. Source and repository settings were untouched.

The addition-only patch contains only `reports/prepublic-2026-09-05/reviewer-b/`. Its local packaging commit uses an empty local parent solely to package additions; it is NOT claimed to be a descendant of the real main commit. Applying the patch in a real baseline checkout creates a new real branch commit, with a different SHA. A fresh local patch-application test verifies only the review additions, not the full repository validator.

A publishing agent should verify main and both primary heads, apply the patch on a separate branch from the stated base, run the full-checkout validator and review-local checks, commit, and open exactly one review PR. The publisher must record the new remote review head and flag any post-cutoff source change; it must not silently expand the verdict to later heads. No source PR is to be merged or closed by this handoff.

## Proposed PR body

Review-only independent audit of PR91 at `b8c88843726ee7ac11cf91323c69bf911ca50706` and PR92 at `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`, cutoff `2026-09-05T15:52:58Z`. Includes the entire original-to-latest sequence, both fifth-pass rank-budget and spectrum-switch packets, 75-path inventory, 78-row mathematical matrix, dependency/conflict map, public-reading-path checklist and differentiated validation receipt.

Scoped partial-result verdicts: VERIFIED WITH FIXES. Universal unsafe control, full merging/repayment coverage, SC* and cycle exclusion remain GAP-BLOCKED. Identified fixes include duplicate within-PR identifiers/schemas, shared README conflict, missing/misdirected spectrum navigation, an empty A=0 cutoff guard, exact safe-operator domains, optimized-mode checker policy and licensing/provenance decisions. Existing pending synthesis and old unreviewed boundaries remain intact.

Full PR91 and both fifth-pass verifier payloads replayed with 22 resealed corruption rejections; a reviewer-authored all-source finite-time check independently confirms the k19 one-third counterexample. Earlier large #92 protocols were inspected rather than wholly replayed. Full-checkout structural validation was unavailable in the authoring environment and remains an explicit publication prerequisite, not a claimed pass.

Only this review directory is added. No new theorem, repair implementation, canonical promotion, source edit, merge, closure, workflow or settings change.
