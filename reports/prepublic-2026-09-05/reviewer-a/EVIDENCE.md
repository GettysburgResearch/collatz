# Evidence ledger and independent-check boundary

## 1. What was read, and what “verified” means here

Read at baseline: `AGENTS.md`, `docs/INTEGRATION_PRACTICE.md`, `docs/RESEARCH_MAP.md`, and the ordinary-extraction, completion-ghost, coefficient-stopping, and periodic-tail resident packets. Their existing verified/source-qualified distinctions are unchanged.

Read and reconstructed at the frozen primary heads: #87's predecessor and natural-density digests, source manifest, local forward/counting arguments and bridge; #88's actual MZ-FH proof; all nine substantive #90 proof/interface files; the complete run/verify code pairs for all eight #90 experiment directories; #87's two checker programs and #88's replacement checker. The source reports, relevant discussion, root/index patches, and selected public formalization files supplied provenance. The [file ledger](file-inventory.csv) marks the remaining standalone ancillary-file and complete-data review boundaries explicitly.

No source generator or source verifier was executed verbatim in this review. Instead, a separately written reviewer program reconstructs the specific exact results listed below. Static inspection is not a claim that all source-generated hashes were reproduced. No external author’s earlier audit is relabelled as this reviewer’s work.

A VERIFIED conditional theorem is accepted only as an implication under its printed, reviewed assumptions. A finite family test does not prove its all-parameter extension; those extensions were assessed from the written algebra, quantifiers, and ordinary-source construction. Review of a later file does not retroactively fix an earlier flawed strengthening.

## 2. Mazur predecessor import

Manuscript: *Certified x^0.90 Lower Bounds for Collatz Predecessor Sets*, v2, 17 July 2026. Import record: 16 pages, 170031 bytes, recorded SHA-256

`cbae5d71ead733b380c3325503e46a7094fb4641244853a37dc220207d133a61`.

The manuscript worktree `0bb368e3b51b980ef5c3b33bb86316e3001c37ac` is not the public checked-source release `5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f`. Both identities must remain visible. The [immutable source snapshot](https://www.proofatlas.ai/sources/collatz-predecessor-090/commits/5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f/) and its public theorem file were inspected. The declaration `predecessor_count_lower_bound_0901` explicitly has a target-dependent positive constant, eventual real cutoffs, positive target, and target not divisible by three. The .90 theorem has unit coefficient after a later cutoff.

The parsed [manuscript](https://www.proofatlas.ai/papers/collatz-predecessor-090/Mazur_Certified_x090_Lower_Bounds_for_Collatz_Predecessor_Sets_v2.pdf), selected proof passages, and selected rendered pages were inspected. Attention went to coefficient directions, time-local functional minima versus a chosen elimination path, adaptive potential decrement, retarded normalization, and the final all-target statement. This is not a page-by-page independent proof certification of the whole external closure.

The public closure records 58 first-party Lean files / 10237 nonblank lines; the tracked release has 64 Lean files including extra entrypoints. Recorded toolchain: Lean `v4.30.0-rc2`, mathlib `5450b53e5ddc75d46418fabb605edbf36bd0beb6`. Generated wrappers contain `native_decide` checks and `include_str` payloads. `AxiomAudit.lean` was read: it contains print-axioms commands, not evidence that those commands were executed here. The import discloses two generated computational assertions in the recorded dependency audit. This is not a kernel-only replay claim.

Recorded payloads: 516560652-byte weight vector and 129140163-byte adaptive potential, total **645700815 bytes**; 129140163 LP rows and 215233605 transitions. The reviewer checked three worked integer rows, all three directed coefficient comparisons, and the exact sign of `5-3 log_2 3` by `3^3<2^5`. The full payload, decoding, and all transition inequalities were **NOT REPLAYED**.

Raw PDF download into the execution runtime failed. The hashes above were therefore **not independently recomputed**, even though the accessible manuscript and source pages were inspected. Source binaries were not redistributed. Source-code licensing does not silently establish redistribution permission for separately supplied PDFs.

## 3. Mazur natural-density import

Manuscript: *Natural-Density Almost-Bounded Collatz Orbits in Logarithmic Time*, v2, 21 July 2026. Import record: 27 pages, 253981 bytes, recorded SHA-256

`08a46dd1cdd9183beb2e09af517361f24d3b7945a6ee00db563a944a4a2373cf`.

Manuscript worktree `f386357d453ac4dcf91242b76252d88a5a729906`; public release `ca3dd0d63920411213403092aecc6946619eb082`. The public [source index](https://www.proofatlas.ai/sources/natural-density-log-time-collatz/) and main Lean theorem surface, recorded evidence, and selected [manuscript](https://www.proofatlas.ai/papers/natural-density-log-time-collatz/Mazur_Natural_Density_Collatz_Orbits_in_Logarithmic_Time_v2.pdf) proof/normalization passages were inspected. The source reports a 599-file, 182625-line first-party closure; it was not independently built or completely line-reviewed here.

The reviewer independently checked the exact clock identity

`1509503/(5000 log 2) = 3*501501/(5000 log 2) + 1/log 2`,

the outward comparisons with 436 and 145, and the margin `5/143 - 6993/200000 = 1/28600000`. The one-division shortcut map, unaccelerated raw map, and odd-to-odd Syracuse map must not share an unqualified clock. The manuscript's fixed target floor is at least two; `log 1` cannot be inserted into its quantitative bound. The typical-orbit conclusion permits an exceptional set and retains one clock constant before the diverging threshold is chosen.

The phase/transport and fixed-target error accounting was inspected at selected load-bearing passages, including the distinction between a moving-scale no-hit term and the bottom fixed-floor term. The complete analytic input chain and its entire formalization are **NOT independently accepted** by this review. The separate detailed Inselmann comparison in #87 remains source-qualified; the abstract fiber-loss algebra is independently checked.

## 4. Reviewer-owned exact reconstruction

Commands actually run, with no upstream/repository imports:

```bash
python -B reviewer_a_exact.py --full-finite --output exact-results.json
python -O reviewer_a_exact.py --full-finite --output optimized-results.json
cmp exact-results.json optimized-results.json
```

Both executions passed and the two reports were byte-identical. Semantic SHA-256:

`ea70e11514698c2581ba44ae4cfcc72864168affd1eb6c2898f78f283d7da716`.

| Independently reconstructed item | Exact coverage / outcome |
|---|---|
| Arithmetic endpoints | 15 integer/rational comparisons, including predecessor coefficient directions, appendix rows, #88 large Chernoff inequalities, clock bounds and .93 recurrence |
| Parity and rotation | 8190 ordinary residues through depth12; full word bijection, affine replay, ballot/no-descent implication and cyclic-minimum existence |
| First passage | Complete AP/source equality at (256,16,8) and (512,32,10): 99 and233 defined sources, unresolved sources retained |
| Cofinal fresh-shell drift | All50 rational bases and all5 shift25 induction ratios; independent radical enclosure for pressure |
| Physical inverse interfaces | 5461 full first-return fans; 1364 complete radius-two comparisons; exact named merger and pruning counterexamples |
| Negative-tree frontier | Entire negative comparison cone through radius10; precision table 2,2,3,4,6,7,13,14,15,16,19; 388 complete/pruned positive-root comparisons |
| 121 obstruction | Complete lower-rank source set, its entire forward closure, no ancestor at any inverse depth; first meeting at shortcut time54 and value40 |
| Phase and finite cycle guard | Opposite eventual phases for13/1 and859/95; all32 five-bit words have no positive T^5 fixed point |
| Green mass | Every enumerated source2..2^18, horizons16/32/64/128/256, one unresolved at256; analytic source tail yields 8.6140<G256<8.9619 |
| Actual transported ensemble | 131072 odd sources in the first shell, 24 complete packets, independent80-bit integer-square-root bounds; proved omitted-source bound2^-216657; scaled masses21<22<23<24 |
| Optimized verifier defect | Isolated source-equivalent X-ASTRA-003 acceptance function rejects a resealed false report normally and accepts it under `-O` |

The last test is **function-level reproduction**, not a claim that the full source verifier was executed. X-ASTRA-004's explicit optimized-mode guard was statically checked and is not the same defect. Reviewer development initially used an insufficiently tight pressure enclosure; replacing it with rigorously outward six-decimal rational bounds made the intended exact comparison pass. This was a reviewer test adjustment, not a source theorem correction.

## 5. Checks not performed

No full external Lean build; no complete axiom-audit execution; no 645.7 MB predecessor replay; no raw PDF-byte rehash; no full external analytic-dependency verification; no exhaustive source-encoded 37/425/263-rule census or all1632 AS7-family report rehash; no exact execution of any upstream run/verify pair; no repetition of source-authored tamper suites; no previous #91/#92 full proof or large-corpus review; no broad novelty audit; no repository-wide validator in an authenticated full checkout; no workflow run.

Ancillary file contents and complete artifact obligations not individually inspected are marked in the file ledger, rather than silently treated as passed. The positive results above are evidence for their stated scope, not permission to cross any of these boundaries.
