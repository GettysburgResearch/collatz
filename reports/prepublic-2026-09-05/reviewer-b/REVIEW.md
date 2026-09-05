# Pre-public integration review B — Collatz

**Review only; no new research wave and no canonical promotion.**

| Boundary | Frozen value |
|---|---|
| Baseline main | `9704bcf1ff33cc9e2b729e0c40137a1e55b95397` |
| PR #91 | `b8c88843726ee7ac11cf91323c69bf911ca50706` — 9 added files |
| PR #92 | `7bb6d36d3bc37dd09b52aa9a23c8e33973032359` — 66 added files, including both fifth-pass packets |
| Review cutoff | `2026-09-05T15:52:58Z` / 18:52:58 Asia/Jerusalem |

## Verdict and recommendation

**PR #91: VERIFIED WITH FIXES as a scoped partial-results packet.** Its exact section return, complete inverse fan, summable charged weight, nonresonant entrance bound, conditional source-height estimate and guarded repayment families survive reconstruction. The Schur/resolvent result is valid on its stated dominated positive cone; it is not a uniform unsafe-return bound. The universal charge budget and complete selector remain **GAP-BLOCKED**.

**PR #92: VERIFIED WITH FIXES, claim by claim, not a monolithic proof.** The orbitwise counting/SC-tail arguments, exact continuation constraints, finite-feature obstructions, computable proper moving rank, spectrum, safe-region estimates, resource barriers and guarded switch repayment survive in the scopes recorded in [the matrix](CLAIM_MATRIX.md). The global bias, unsafe transport, complete temporal merging cover and total successful selector remain **GAP-BLOCKED**. Explicitly false strengthenings are **REJECTED**, while their correctly scoped refutations are verified separately. No full Collatz proof is supplied by either PR.

**Public integration: GAP-BLOCKED pending the specific editorial, namespace, provenance and operational items below—not because an open research project must solve Collatz before publication.** Recommend clean extraction by mathematical subject, not a wholesale acceptance of the branch histories. No source PR should be closed merely because a headline remains open.

## Findings that must govern integration

1. **The two fifth-pass packets are not interchangeable.** `pass5/` and `pass5-spectrum-switch/` reuse several T-A3 identifiers and the schema name `X-ASTRA3-005/v1` for different statements/data. Even `PR92:T-A3-1051` is ambiguous. Use `(PR, full SHA, path, claim ID)` until reviewed integrated aliases exist. Their safe sets differ: quarter-drop versus all nonincreasing moving-rank steps. Different geometric/polynomial safe tails are therefore not contradictory.
2. **The public reading path omits current content.** Both PRs add different versions of `research/astra-three-routes/README.md`. The frozen #92 root index and PR description stop at the rank-budget packet. The separate spectrum importer preserves the later work, but the spectrum experiment README links to `pass5/README.md`, the other packet. Preserve historical texts; create a neutral active index and correct the active link.
3. **One explicit endpoint guard needs a local wording fix.** In `pass2/SC_TAIL_AND_ECHO.md`, T-A3-453's cutoff involving `log2(ceil(A/P))` is undefined for the valid first-crossing word `0`, where A=0 and the displacement interval is empty. Treat that case first, or state A>0 for that cutoff. The full CRT/half-space argument otherwise survives. This report proposes the repair; it does not rewrite the original or call the changed wording independently reviewed.
4. **Keep operator domains visible.** #91's safe weighted-supremum resolvent assumes a dominated input and retains the unbounded endpoint charge Q. #92's distribution-free safe moment estimate assumes a finite moment at safe entry. The infinite unsafe moment counterexample shows why that premise cannot be propagated for free. Safe absorption means reaching an unsafe/resonant set or 1, not reaching 1 alone.
5. **Physical and quantitative boundaries are sound when retained.** CRT provides positive ordinary sources separately for each finite parameter choice, not one all-time source. Complete finite rank balls bound witness endpoints, not path length or intermediate rank. Necessary peak/clock lower bounds do not guarantee a meeting. Repayment guards check future physical words; ternary depth does not force the next mode.
6. **The SC crosswalk is a useful new reviewed component, not cycle exclusion.** The actual distinct-state orbit has bounded reciprocal correction; its coefficient sequence tends to infinity and attains a global minimum, giving one actual SC-infinite tail. Conversely periodic positive tails have a block coefficient below one. Thus the stated SC*/eventual-periodicity equivalence survives. A nontrivial positive cycle still must be excluded using the full denominator and ordinary replay. Neither resident pending synthesis is automatically promoted.
7. **Checker evidence needs differentiated labels.** Full #91 and both fifth-pass verifier payloads were independently replayed here, with 22 resealed tamper tests in total. The earlier #92 protocols were inspected, not fully rerun. An independently authored small audit additionally reconstructs the entire H=64, time-19 cone and confirms the one-third failure. Early assertion-only validation is unsafe under optimized Python; later explicit-error checkers are materially stronger. See [validation](VALIDATION.md).
8. **Rights and provenance need owner resolution.** No root license was present in the inspected baseline listing; no PDFs/binaries are added by these two PRs. Do not interpret a hosting permission, author attribution, or an exact source pin as blanket redistribution permission. Retain external papers as references until the relevant permission is recorded. This is an unresolved evidence item, not a legal finding of infringement.

## Independent review scope

Every final proof-bearing file and both generator/verifier implementations in all packets were read; all 75 changed paths are listed in [INVENTORY.json](INVENTORY.json), including documentation and artifact-interface evidence. PR histories and available discussion were checked; publication receipts are not mathematical approvals. The large earlier numerical row sets were not all independently recalculated. External theorem builds, broad literature priority, old source PRs, and the full #90 research chain are explicitly outside this verdict.

The mathematical conclusions here come from reconstructing hypotheses, algebra, quantifiers and dependencies at the frozen heads, not from inheriting author labels or prior conversation enthusiasm. Previous Astra work in #90 is used only for interface comparison; this is not represented as an independent full review of that work.

## Public front door

The baseline already says Collatz is unsolved and separates accepted local proofs, source-qualified synthesis, open obligations and archive evidence. Preserve that structure. Its dated archive and compatibility pointers are appropriate; do not replace them with an active pass log. Add subject-oriented records for the new reviewed subsets and adjacent statements of what is not proved. The [checklist](INTEGRATION_CHECKLIST.md) gives exact edits, owners, destinations and acceptance checks.

The baseline structural validator was read in full, but **not run on a full checkout**: no authenticated full checkout was available and Git failed DNS resolution. Its current curated checks do not validate the new proof claims, duplicate IDs, schemas, live heads, rights or semantic link destinations. A passing structural validator would not verify mathematics. The missing full-checkout run remains an operational item.

## Publication boundary

Only files below `reports/prepublic-2026-09-05/reviewer-b/` are proposed. No original theorem, registry, source PR, workflow or setting is modified. No new repair or cross-PR synthesis is admitted by this report. Publishing was attempted through tool discovery and Git access, but no write action was exposed and DNS failed. **No remote review PR or remote review head was created in this session.** The delivery contains one review-only patch and a local packaging commit, clearly distinguished from the intended baseline and source heads.
