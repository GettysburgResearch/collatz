# Reviewer D — final report and integrator handoff

**Finalization pass, not a new research wave.** Repository: `GettysburgResearch/collatz`. Review PR: **#98**. Branch: `reviewer-d/2026-09-05-integrated-main-audit`.

```text
Reviewed main M:      cd1b3689e8d37fc4232945072e2faf6bd5ee47bd
Original review D1:   0ce01f9cff107745abc3dabb8b1faa27ab6acfd4
Original cutoff:     2026-09-05T19:43:16Z / 22:43:16 Asia/Jerusalem
Second-pass capture: 2026-09-05T20:21:41Z / 23:21:41 Asia/Jerusalem
```

At second-pass capture, main and #98 still had those exact heads; #98 was open, draft and unmerged. Its discussion contained no comments or review submissions in the retrieved timeline. The publication receipt identifies the final child commit. A later source change is outside these verdicts, not retroactively included.

The six D1 files remain byte-identical. This pass adds only this handoff, `final_checks.py`, and `final_checks.json`. Read this file first, then [the original 44-row matrix](CLAIM_MATRIX.md) and [the proof reconstruction](PROOF_AUDIT.md). The [original source manifest](SOURCES_AND_VALIDATION.md) still fixes every first-pass claim and evidence boundary.

## 1. Final assessment

**The original seven resident packets' core mathematical arguments survive this audit at their stated scopes. Six localized findings require correction or qualification. No additional failure of those core theorems was found in the finishing pass.** This is not certification of every file on main, every old review, or every recent imported theorem.

The finishing pass adds three useful details:

1. The PR16 files implicated by FD-04/05 are byte-identical at the newer source commit used by the results catalog. Their warnings belong at both the resident dependency interface and the catalog entry, not only at the older pin.
2. FD-05 also requires care about **open** error cylinders: invariance of an open interval does not guarantee a nonempty infinite nested cylinder. The valid arbitrary-code statement uses the closed strip and its explicit convergent series.
3. The catalog's algebraic-extension reference still leads to a source with previously recorded constant-branch, finite-difference and coefficient-field repairs. These old review conditions must be carried forward. They are not new discoveries of D and are not removed by the sound syndetic-polynomiality lemma.

There is also an operational handoff requirement: the current supplemental integration manifest and its checker encode **A/B's disjoint source assignments**, not an extensible list of every later reviewer. Record D's overlapping audit separately rather than appending it to that frozen assignment list or weakening its integrity checks.

All proposed replacements, including the expanded wording below, remain **PROPOSED pending review of the exact replacement text**. Rejecting a false auxiliary sentence does not reject a valid theorem beside it; reconstructing a valid theorem does not validate the whole source file.

## 2. Complete correction/action list

All main paths here are at M. S16 is `900ba417c968d8a41bc56a30d3ccc941284d8ce2`; S16-CAT is `87478352e65c7b816dfc8b3b30894b71fb50f662`. Exact original locators and blob hashes remain in the first-pass manifest.

| ID / priority | Exact source and disposition | Required integrator action / acceptance test |
|---|---|---|
| **FD-01 / correction** | M, `research/integrated/ordinary-extraction/README.md`, adversarial example 4. **REJECTED** nonordinary conclusion. The signed stabilization theorem is **VERIFIED**. | Add a scoped erratum: infinitely many nonzero appended digits exclude a nonnegative ordinary value, but an eventual maximal tail can represent a negative integer. Test `-2^J` for arbitrary J by its exact residue formula; do not weaken either stabilization theorem. |
| **FD-02 / correction** | M, `research/integrated/periodic-tails/README.md`, the positive-realization code block. **REJECTED** as a general criterion requiring a nontrivial cycle. | Relabel it a nontrivial-positive-cycle certificate or remove nontriviality from the general realization criterion. Preserve `10 -> 1`, `01 -> 2`, the zero word, signed realizers, the full denominator and actual preperiod replay. For controller use, explicitly require deterministic finite-state evolution and an infinitely productive concatenation of fixed finite parity blocks. |
| **FD-03 / correction** | M, `claims/lemmas/L-0041-six-branch-root-cap-recurrence.md`, (10) and the sentence after (7). **VERIFIED WITH FIXES** as a packet; the two erroneous clauses are separately rejected in D-034/035. | State `m_0=1`, `R_empty=0`; restrict the minimum-over-canonical-roots formula to n>=1. A lifted pre-final value changes by `P^n Q h`, its high quotient by `P^n h`, and its output by `P^(n+1)h`. Keep the correct append/output recurrence. |
| **FD-04 / dependency warning** | S16 and S16-CAT, `research/adelic-cusp/claims/T-9316-efficient-recurrence-thue-morse.md`, section 2's unrestricted appended-block conclusion. **REJECTED** without a nonconstant restriction. | At the resident factor-complexity dependency table and the centered/adelic catalog entry, retain the verified recurrence cone but state the zero-completion exception. Constant codes have efficient repeats and zero appended blocks. The nonconstant repair and Thue–Morse applications survive. Do not blanket-import this whole file as VERIFIED. |
| **FD-05 / dependency warning** | S16 and S16-CAT, `research/adelic-cusp/claims/L-9313-centered-error-full-shift-cylinder.md`, sections 2–3. **REJECTED** strictness for every nonconstant current tail; the closed-strip, uniqueness and cylinder clauses remain **VERIFIED**. | Preserve the weak strip for arbitrary codes. Restrict strict all-time statements to codes not eventually constant, or to separately justified positive ordinary centered orbits. Include `1000...` and `0111...`, endpoint errors +/-1/N, and constant codes with zero error. Do not use open-interval invariance as infinite-cylinder existence. Section 3 below gives the exact reason. |
| **FD-06 / application block** | M, `claims/lemmas/L-0042-syndetic-integral-algebraic-branches.md`, consequence for extraction schemes. Main polynomiality lemma **VERIFIED**; unqualified rigidity transfer **GAP-BLOCKED**. | Keep rational polynomiality separate from full-tail integrality, positivity, all-six-child coverage and exact section laws. `f(x)=x/2` on even inputs is not integer-affine on every integer. A proper-sublanguage self-section is not a counterexample to the full-tree theorem. Do not promote the application by citing the polynomiality lemma alone. |
| **Overlap clarification / open target** | M, `claims/theorems/T-0046-two-sided-cap-root-overlap.md`, section 5; D-038 **VERIFIED WITH FIXES** for the conditional target, not an exclusion theorem. | Quantify over each fixed candidate initial source and every feasible integer overlap length at the selected times. Correct limiting ratios alone are insufficient. Retain past-root stabilization and physical compatibility. Section 4 below gives proposed explicit wording. |
| **Historical PR65 repairs / preserve debt** | S65 `2183dc7e66162684e464913a4ae1a222b41b30f3`, `research/six-branch-extraction/claims/T-7501-finite-algebraic-section-rigidity.md`. **VERIFIED WITH FIXES**, not blanket approval of its printed proof. | Keep the old review's constant-branch, finite-difference rigor, semialgebraic coefficient-field and Puiseux-source qualifications visible before importing this extension. Use a path-qualified identity; do not identify it with every colliding `T-7501`, or assume it is the unlocated `T-0044` normalization. |

Suggested home for the corrections is a separately reviewed addition to `research/integrated/ERRATA.md`, with short warnings or links at the affected active reading surfaces. Preserve the original source bytes and old exact-SHA verdicts. A corrected proof body or registry entry should have its own explicit replacement identity and review, not an unexplained edit to a pinned original. These destinations are recommendations, not changes made by this PR.

## 3. Additional endpoint check: closed support is not open support

The source's exact real companion gives

```text
u_n = (e_n - x_(n+1))/N,    0 <= x_(n+1) <= 1.
```

Thus `|u_n|<=1/N` for every binary code. The code `1000...` has `x_1=0` and `u_0=1/N`; its complement has `u_0=-1/N`. Their current tails are nonconstant. A code that is not eventually constant has every future companion strictly between zero and one, so its errors are nonzero and strictly inside the strip. The positive ordinary all-time bridge has its own proof excluding zero and endpoint errors; that bridge remains valid.

There is a related logical caveat in section 3. For `rho=M/N` in (0,1), repeatedly choosing the same-sign inverse branch `g(r)=rho r` produces the open cylinders

```text
(0, rho^k/N),  k=0,1,2,... .
```

Every finite cylinder is nonempty and each is contained in the preceding one, but their infinite intersection is empty. Their **closures** intersect at zero. Equivalently, a positive forward magnitude following that branch forever would grow by `(N/M)^k` and leave the strip. Consequently an assertion of arbitrary infinite support **within the open strip** is false. The closed-strip full-code construction by the displayed series is sound. This is a clarification of FD-05, not a new objection to the resident nonconstant factor-complexity theorem.

The new finite tests check exact eventual-constant codes and endpoint classifications; they do not infer the infinite-intersection statement numerically. The geometric argument above supplies that conclusion.

## 4. Explicit quantifiers for the overlap handoff

Write the two proved bounds in T-0046 as `L_n(x)<=x_n<=U_n(x)` for one fixed candidate x. Let

```text
E_n(x) = {ell>=1 : [Q^(ell-1),Q^ell) intersects [L_n(x),U_n(x)]}.
```

An all-time ordinary source, after `Q^n>x`, must give an actual bridge in `B_(n,ell)` for its actual `ell=1+floor(log_Q x_n)`, which belongs to `E_n(x)`.

A sufficient cofinal exclusion contract therefore has the order:

```text
for each fixed candidate x>0,
  at cofinally many n after its past-stabilization threshold,
    exclude B_(n,ell) for every ell in E_n(x).
```

That is proposed clarification of the existing open target, **not a proved emptiness theorem**. Selecting just one ell per n whose ratio ell/n tends to the right constant need not cover the actual ell. Unrelated finite bridge pairs do not give one compatible ordinary all-time source.

## 5. The old algebraic repair boundary is still operative

The complete S65 source was read in this finishing pass, along with the relevant portions of its prior review at `591a06ad914b63dddfd65ee658dbec36291ffbc0`, path `reports/gpt56-cartographer-01/2026-08-01-pre-public-review-pr64-pr65-pr66.md`. The older review already classified it VERIFIED WITH FIXES and listed the following conditions. D does not claim priority for them.

**Constants.** The printed hypotheses permit constant branches, while the degree argument later assumes nonconstancy. A positive integer constant C would require `P C+a_(pi(j))` divisible by Q for all six children. The six digits are distinct modulo Q, so at most one can work. This supplies a short proposed completion of the case, but it must appear in the reviewed replacement rather than be silently assumed.

**Finite differences.** Choose a positive integer d greater than the growth exponent and use the derivative estimate with

```text
Delta^d f(n) = integral_[0,1]^d f^(d)(n+t_1+...+t_d) dt.
```

Then integer finite differences tend to zero and hence eventually vanish. This avoids an unsupported interchange of an infinite Puiseux series and differences. The analytic input still needs its exact stated hypothesis and primary reference.

**Coefficient field.** An arbitrary real-semialgebraic branch is not automatically algebraic over Q(X). Either narrow the claim to the stated coefficient field or supply the separate real-semialgebraic argument before invoking the Q(X) lemma. This is distinct from the syndetic-domain problem in FD-06.

The original main RIG packet is the narrower affine/rational result and is not refuted by any of these points. The catalog should retain the extension as a repaired/qualified source slice. Later algebraic deltas remain outside both the old review and this read of S65.

## 6. Supplemental verdict/evidence matrix

The original matrix remains 44 rows. The following six finishing rows supplement it; evidence-only rows must not be counted as newly verified theorems.

| ID | Exact item | Verdict | Evidence and scope |
|---|---|---|---|
| D-F01 | S16-CAT L-9313 and T-9316 | VERIFIED | **Identity only:** their complete blob IDs equal the S16 files already reviewed. This extends FD-04/05 to those two exact catalog-pinned bodies, not to every file at S16-CAT or the current PR16 head. |
| D-F02 | S16 L-9313 section 3, arbitrary infinite support construed inside the open strip | REJECTED | Nested same-sign cylinders have empty open intersection. The closed-strip series/full-code construction remains valid; this refines FD-05. |
| D-F03 | S65 T-7501 algebraic-section packet | VERIFIED WITH FIXES | Intended full-tail, complete-tree core reconstructed; constants, finite-difference justification and the broader semialgebraic field transfer need the previously recorded fixes. No canonical or broad source-file promotion. |
| D-F04 | Current research map, catalog, open-obligation index and replay-policy boundaries | VERIFIED | **Reading-path inspection only:** original and new status tiers, old unreviewed-wave boundaries and unperformed replay ceilings remain explicit. Add the source warnings in the action table; no full new review of thirteen catalog families. |
| D-F05 | `claims/reviewed-2026-09-05.json` and `tools/check_review_integration.py` | VERIFIED | **Contract inspection and internal self-test only:** assignments expect exactly A/B and the five source PRs. The byte-matched checker rejects eight invalid fixtures. This is not a repository scan. |
| D-F06 | Full-tree structural execution, all unreviewed main/source corpus and external builds | GAP-BLOCKED | These are not completed by D. The authenticated full-checkout execution gate and the explicit exclusions below remain for the integrator/other reviews. |

D-042 and D-043 in the first matrix were likewise explicitly inspection-only. Their VERIFIED labels never meant mathematical acceptance of all linked source claims or an executed full-tree validator.

## 7. Source identities added or cross-checked in this pass

| Ref | Path | Exact Git blob |
|---|---|---|
| S16-CAT | `research/adelic-cusp/claims/L-9313-centered-error-full-shift-cylinder.md` | `cddc4825d373ee7234e34b602a7add7feb39e324` |
| S16-CAT | `research/adelic-cusp/claims/T-9316-efficient-recurrence-thue-morse.md` | `6b8b480a2b8dee84ff91a3eb3e67f957943f88a1` |
| S65 | `research/six-branch-extraction/claims/T-7501-finite-algebraic-section-rigidity.md` | `f43db5aab077f2e5c809274041ac45c1e9035cb6` |
| M | `docs/RESEARCH_MAP.md` | `8f1cb0aba97e0a359e36ed5583706db4e1161a9f` |
| M | `research/RESULTS_CATALOG.md` | `660e040b5125d776872f7631246ac4a9986ccda8` |
| M | `research/open-obligations/README.md` | `c8e03f429fd3b10bfc5c20bb1648d286c3b53d4c` |
| M | `docs/REPLAY_POLICY.md` | `830793dc4e34bfc857fcb71d3dfde5548874c4e9` |
| M | `claims/reviewed-2026-09-05.json` | `ff5c2a5937f8f62935707b1c8ec67116f8b8c942` |
| M | `tools/check_review_integration.py` | `55a083e775af693bcbfc176c6079f08d8f78bd16` |

The 16 original proof-bearing files plus S65 make **17 distinct proof-bearing bodies read across D's two passes**, with all clause-level exclusions retained. Re-identifying two identical blobs at S16-CAT is not two new proof reviews. A search result returning no files was not used to prove absence of an older source. Bare L-0040/T-0044 cross-references still require exact source resolution before importing their purported complete statements; S65 is a named comparison, not an asserted alias.

## 8. Validation actually performed

The supplied first-pass bundle was extracted, all six blob IDs matched its published D1 identities, and both original check commands were rerun unchanged:

```bash
python -B reports/prepublic-2026-09-05/reviewer-d/targeted_checks.py \
  --check reports/prepublic-2026-09-05/reviewer-d/checks.json --self-test
python -O -B reports/prepublic-2026-09-05/reviewer-d/targeted_checks.py \
  --check reports/prepublic-2026-09-05/reviewer-d/checks.json --self-test
```

Both passed with identical output and the original semantic digest:

```text
f68f0babd04b680fe9bbd47da82cc5e6014c38ba8b54400426e437db767f6174
```

Both again rejected the original eight genuine resealed corruptions. The first-pass coverage counts in SOURCES_AND_VALIDATION remain unchanged.

New finishing commands:

```bash
python -B reports/prepublic-2026-09-05/reviewer-d/final_checks.py \
  --check reports/prepublic-2026-09-05/reviewer-d/final_checks.json --self-test
python -O -B reports/prepublic-2026-09-05/reviewer-d/final_checks.py \
  --check reports/prepublic-2026-09-05/reviewer-d/final_checks.json --self-test
```

Both passed with identical output:

```text
semantic SHA-256:
e0563b820b0cd7c24c6ba159af5a944209bb101693fc4d4b8584144685991ddb
35 coprime parameter pairs; 8,820 eventual-constant codes;
53,760 exact error positions, including 8,400 endpoint and 17,220 zero positions;
6 constant-parent residue classes; 128 even-domain / 128 odd-control values;
24 negative ordinary digit-face cases; 8 resealed corruptions rejected.
```

The final checker uses standard-library rational arithmetic and imports no prior checker or source module. It compares canonical serialization, so a boolean substituted for integer 1 is not accidentally accepted. The two D checkers have the **same author**; their existence is not a second independent mathematical review of D's report.

I also materialized the exact 11,510-byte `tools/check_review_integration.py`, verified its Git blob `55a083e775af693bcbfc176c6079f08d8f78bd16`, and ran its **internal `--self-test` only**, in normal and optimized Python. Both returned:

```text
SELF-TEST PASS: 8 invalid fixtures rejected; no repository scan or mathematical verification performed
```

That test uses the checker's temporary fixtures. It does **not** authenticate main's full tree or run the live link/subtree audit. Direct `git ls-remote` again failed with `Could not resolve host: github.com`. No authenticated full checkout was available. Neither full-tree structural command below was executed against main in either D pass.

## 9. Integrator acceptance checklist

- [ ] Review FD-01–06, the overlap quantifiers, and the closed/open-strip distinction; approve any exact replacement text separately. Preserve the valid used dependency clauses and rejected extensions as different objects.
- [ ] Add short active warnings at the affected packets/dependency table and centered/adelic catalog entry; retain exact original bytes and source identities in the durable archive or frozen references.
- [ ] Keep PR65's preexisting constant/finite-difference/field/source repairs and all later-delta boundaries visible. Resolve bare historical references before using them as dependencies.
- [ ] Record D in a **separate follow-up review/errata record**. Do not append D to the frozen A/B primary assignment list in `claims/reviewed-2026-09-05.json`: the checker deliberately requires roles `{A,B}` and the original nonoverlapping assignments. Do not change A/B matrices or pinned subtrees to simulate earlier review coverage.
- [ ] Preserve the eight canonical and three roadmap status boundaries unless an authorized, separately reviewed change explicitly replaces them. In particular do not promote the periodic synthesis, old FC-language bridge, E-INTEGRATION-001 or the four recent assemblies by citing inspection-only D rows. D-041 reviews only the stated A=0 endpoint reasoning.
- [ ] Run `python -B tools/check_integration_state.py` and `python -B tools/check_review_integration.py` on an authenticated **complete** checkout of the proposed integration head. Save the SHA, commands, exit codes and outputs. Rerun both D checkers and their tamper tests there. A self-test or a six-file materialization does not satisfy this gate.
- [ ] When introducing a deliberately reviewed status or source-pin change, update the validating policy together with that change; do not disable the hard-coded protections merely to get a green output. Their present constraints preserve the existing pending flags and original evidence snapshots.
- [ ] Before merging any follow-up, compare against the last recorded main, classify all later deltas separately, and confirm the resulting diff changes no unrelated source theorem, workflow, permission or visibility setting.

## 10. Explicit remaining exclusions and disposition

This finishes D's requested review contribution. It does not claim a full second mathematical review of the newly imported PR87/88/90/91/92 corpus, all thirteen source-pinned catalog families, issue-4 physical chart translation, every older source/review artifact, unlocated L-0040/T-0044 variants, external Lean proofs or large payloads. The #67/#68/#69 first-wave unreviewed boundary and later theorem-bearing deltas remain intact. No PDF redistribution, licensing clearance, security/visibility decision or external-priority claim is supplied.

SC*, FC*, nontrivial-cycle exclusion, fixed-floor survivor mass, actual unsafe-return control, and a complete terminating lower-rank cover remain unresolved by this review. No finite test here upgrades an all-depth or ordinary-extraction claim.

**Recommended disposition:** retain the scoped core results; use this report to prepare localized, separately reviewed errata and the full-checkout validation receipt. Do not withdraw sound theorems because an ancillary sentence is false, and do not treat the review as blanket public-release clearance. No main/source edits, merges, closures, settings or workflow changes were made by D.
