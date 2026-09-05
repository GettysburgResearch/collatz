# Reviewer D — exact sources and validation scope

## Frozen state

```text
repository:        GettysburgResearch/collatz
main/cutoff:       cd1b3689e8d37fc4232945072e2faf6bd5ee47bd
main tree:         99f330473ab64fc31f2bc7b194cc482c3c2839ce
main parent:       9704bcf1ff33cc9e2b729e0c40137a1e55b95397
head capture UTC:  2026-09-05T19:43:16Z
head capture local:2026-09-05T22:43:16+03:00 (Asia/Jerusalem)
branch:            reviewer-d/2026-09-05-integrated-main-audit
```

GitHub identified the frozen main as integration #95, committed 2026-09-05T18:30:02Z. Reviewer D's separate branch was created at that exact commit before writing review files. The eventual review commit is a child of that snapshot; no source branch is rebased or rewritten. Publication metadata gives the actual final head. A later-main observation, if different, is a delta outside these verdicts.

## Proof-bearing source manifest

All 16 files were read. Verdicts and exclusions are clause-specific, not a blanket approval of every external comparison or future-work paragraph. The first ten rows use frozen main (M); the next five use S16; the last uses S64.

| Key | Exact path | Git blob SHA |
|---|---|---|
| EXTRACT | `research/integrated/ordinary-extraction/README.md` | `4a3346e6eac6f6697ce5783a4bf8272ac84011e2` |
| GHOST | `research/integrated/completion-ghost/README.md` | `e5c0dea09291d1258a67fa7b3413b507e606e513` |
| PERIODIC | `research/integrated/periodic-tails/README.md` | `53e499f679bc990196e0e4b3a9e07a9ddacbbeca` |
| SC | `research/integrated/coefficient-stopping/README.md` | `8c598a7f87b0c2d18ee8395fdffae432b02530ac` |
| AUT | `research/integrated/finite-safety-automata/README.md` | `6e37079a23906137e7060a60ad9ec3a4b43759eb` |
| RIG | `research/integrated/six-branch-rigidity/README.md` | `e3545c0173e6eac77f3c93572d4621b883150c22` |
| FACTOR | `research/integrated/factor-complexity/README.md` | `fea936f9f202c26b9f11191b6aea83cee7047d49` |
| ROOT-CAP | `claims/lemmas/L-0041-six-branch-root-cap-recurrence.md` | `6b10d8818a0465ac047be34ba2cd7e6b0fb79a2f` |
| ALGEBRAIC | `claims/lemmas/L-0042-syndetic-integral-algebraic-branches.md` | `df11cdfa5b16d276e3f18845cf6af9d7ce646c14` |
| OVERLAP | `claims/theorems/T-0046-two-sided-cap-root-overlap.md` | `58b390b2da759333e4996003b552b959a48f7ca2` |
| NATURAL | `research/adelic-cusp/claims/D-9302-adelic-natural-extension.md` | `2a80d0fd6bb198e1c83d8ea58ed899bf3a836665` |
| DIFFERENCE | `research/adelic-cusp/claims/L-9311-orbit-difference-carry-duality.md` | `0aefa71ff556694e774539092c35a7953b8d1025` |
| CENTERED | `research/adelic-cusp/claims/L-9313-centered-error-full-shift-cylinder.md` | `cddc4825d373ee7234e34b602a7add7feb39e324` |
| POWER | `research/adelic-cusp/claims/T-9315-centered-rational-power-equivalence.md` | `a54fe365aeaf1be9a6459738359a9b8712aeffc1` |
| RECURRENCE | `research/adelic-cusp/claims/T-9316-efficient-recurrence-thue-morse.md` | `6b8b480a2b8dee84ff91a3eb3e67f957943f88a1` |
| AFFINE-SOURCE | `research/six-branch-extraction/claims/T-7402-finite-affine-nucleus-rigidity.md` | `ee026d0dd79d17e32443a76e65559637342be371` |

```text
S16 = 900ba417c968d8a41bc56a30d3ccc941284d8ce2
S64 = 88884c3e590b08aeb2018872987e71e14de1fe7b
```

These source files stay where they were; this review redistributes no source PDF or font and changes no source theorem. The five PR16 bodies remain source-pinned rather than newly imported into main. D-9301's elementary first-bit congruence used by D-9302 was derived from the displayed series, not treated as approval of the unread rest of D-9301. L-9310's reciprocal-phase comparison was not re-reviewed.

## Current integration surfaces inspected at M

| Path | Git blob SHA |
|---|---|
| `README.md` | `eceef4b714af9677f5d56e6c5b9df8d30ff45794` |
| `AGENTS.md` | `0cb56c6f3520e90f0f239441fcf8f130bdfae3c7` |
| `research/integrated/README.md` | `f7c43b556e6894df9e0171e7e3f1c3065697c4cd` |
| `research/integrated/CONVENTIONS.md` | `23a2433aa2842a6486348d8b8e800c7b1466c945` |
| `research/integrated/ERRATA.md` | `e6c9a4acb80be7ab6e02ff99bef088d466c05893` |
| `research/integrated/exceptional-mass/README.md` | `63854347d820b1aa8cea83d53b7a6e53183fe563` |
| `research/integrated/renewal-transport/README.md` | `1658d160c7fe1aad000fd8b44e00b26c86712f26` |
| `research/integrated/rank-merging/README.md` | `c695b95007cafab27b544733c4e2739e35ce50cb` |
| `research/integrated/orbitwise-boundaries/README.md` | `beed564cc1254352e7cd54a2fbd9a86c24033ba1` |
| `tools/check_integration_state.py` | `3df5f1c51c6cbd841e10a6e7091677738918cfce` |
| `tools/check_review_integration.py` | `55a083e775af693bcbfc176c6079f08d8f78bd16` |

These were read for mathematical scope, normalization, proof-versus-reference status and validator logic. Not every local/external link target was fetched. A valid summary is not independent verification of its entire linked corpus. No accepted status changes merely because a proof packet is resident or its bytes are authenticated.

## New exact arithmetic evidence

The standard-library checker is authored for this review. It imports neither the repository's mathematics code nor the previous generators or verifiers. It regenerates the audit report from explicit definitions and exact rational/integer arithmetic; it does not merely verify a supplied hash. Its own finite checks are not a formal proof checker or a second independent review of Reviewer D's prose.

Commands actually run from the locally materialized review root:

```bash
python -B reports/prepublic-2026-09-05/reviewer-d/targeted_checks.py \
  --write reports/prepublic-2026-09-05/reviewer-d/checks.json --self-test
python -B reports/prepublic-2026-09-05/reviewer-d/targeted_checks.py \
  --check reports/prepublic-2026-09-05/reviewer-d/checks.json --self-test
python -O -B reports/prepublic-2026-09-05/reviewer-d/targeted_checks.py \
  --check reports/prepublic-2026-09-05/reviewer-d/checks.json --self-test
```

Both check modes pass with identical output and eight resealed-corruption rejections. All validation predicates raise explicit exceptions; Python optimization cannot remove them.

```text
semantic report SHA-256:
f68f0babd04b680fe9bbd47da82cc5e6014c38ba8b54400426e437db767f6174
```

| Check | Exact scope and result |
|---|---|
| Signed extraction | 2,010 mixed-radix edges, including repeated moduli; the negative integer -4096 with 12 initial zero digits and 28 further maximal digits |
| Parity/periodicity | Every binary word of lengths 1 through 12: 8,190 words, 90,114 rational periodic steps, 24,570 ordinary finite-cylinder lifts |
| Preperiods | Every prefix length 0 through 5 and periodic block length 1 through 6: 7,938 rational inverse/forward prefix pairs; no infinite ordinary realization inferred |
| Coefficient identity | Sources 1 through 512, 64 steps each: 32,768 exact surplus identities; 1,664 finite box/least-source comparisons through depth 12 |
| Safety automata | Every depth 0 through 10, 8,188 ordinary membership checks; independently built and minimized complete canonical DFAs, each with exactly one cyclic SCC of size two |
| Six-branch chart | All 36 ordered pairs, affine-alphabet automorphism test, every type word through length four (1,554), three physical lifts per word (4,662), exact cap brackets |
| Root/quotient regressions | Empty-depth minimum versus residue; correct high-quotient increment 531,441 versus printed 278,628,139,008 at n=1,h=1; one proper-sublanguage identity section |
| Centered/factor interfaces | 510 binary periodic codes through length eight; 512 finite ordinary chart paths and 11,260 repeated-factor divisibility/cone checks; 13 Thue–Morse scales; exact +/-1/81 boundary controls |
| Algebraic lemma interfaces | 200 polynomial divided-difference windows on a bounded-gap integer set; unbounded gaps of square inputs retained as a non-syndetic control. Does not numerically prove Puiseux theory |

Eight mutations change scope, signed integer, trivial realizers, empty-depth minimum, SCC size, branch coverage, constant completion or divided-difference count, then recompute the checksum. Every changed payload is rejected. Mutation rejection establishes this checker's stated evidence contract, not a theorem's truth.

## Explicitly not done / not reviewed

* No filesystem-authenticated complete checkout: direct Git access failed with `Could not resolve host: github.com`. Connector reads/writes worked. **Neither `python tools/check_integration_state.py` nor `python tools/check_review_integration.py` was run on main.** No synthetic fixture is described as a full-tree pass.
* No complete second D review of the newly imported #87/#88/#90/#91/#92 theorem corpus, old full encoded experiments, or Reviewer A/B's review reasoning. Only the listed wrappers, conventions and narrow erratum reasoning were audited here. Historical A/B verdicts were not proof premises for the original resident spine.
* No full review of the thirteen wider source-pinned catalog families, issue-4 chart-to-Collatz translation, T-0044 in every source normalization, all earlier review comments, or post-cutoff changes. No certification of the old exact FC* source-language bridge.
* No external Lean build, 645.7 MB predecessor payload, large orbit/automaton/cycle census, broad literature-priority comparison or redistribution-permission audit. No PDF was analyzed or redistributed in this pass.
* No formal proof assistant. The standard convergent algebraic-Puiseux input is exposed in PROOF_AUDIT; a primary text was checked, not its entire cited book chain.

The existing #67/#68/#69 unreviewed-wave boundary, later source-delta exclusions, source-qualified periodic synthesis and proposed bridge are not superseded by this review. Newly suggested repairs remain proposed. GitHub's eventual branch/PR head authenticates only these review additions, not mathematical acceptance or release readiness.
