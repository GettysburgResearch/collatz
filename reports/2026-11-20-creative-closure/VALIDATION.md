# Actual scientific-checkout validation

**All declared finite execution gates passed. Collatz remains OPEN.**
This record concerns actual execution of the real GitHub scientific commit
below, not a hypothetical checkout or a source inspection.

## Exact input

| Field | Value |
| --- | --- |
| Scientific commit | `4e0df37cfaa8cba74ca0baaa18217937eca0c128` |
| Scientific tree | `28efdf8c7f14d0fc02d269dd8144e150245ce346` |
| Parent main | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` |
| Complete tracked files | 348 |
| Manifest-covered files | 31 |
| Content-manifest SHA-256 | `b805fad33f205f341c7e021fca936107e4227b4a2c7ce5e365bbac1599fa9b69` |

The GitHub tree created from the new files matched the local full index
tree exactly. The published commit metadata was read back, its raw Git
commit object was reconstructed and verified against its GitHub SHA, and
that exact object was checked out in a separate complete worktree.
Both runners confirmed the same commit, tree and file count before and
after execution. The worktree and index were clean, including untracked
files, and no sparse/skip-worktree input was used.

## Actual commands and receipts

```sh
python -X utf8 -B reports/2026-11-20-creative-closure/run_bundle.py --receipt /workspace/scratch/56e7a5765d0c/creative-closure-publication/scientific-bundle-validation.json
python -X utf8 -B tools/validate.py --regressions --receipt /workspace/scratch/56e7a5765d0c/creative-closure-publication/scientific-checkout-validation.json
```

The commands ran from the exact scientific checkout. Receipts were written
outside it and copied here only after completion. Their absolute execution
paths are historical metadata; a later checkout can use any unused external
receipt paths.

| Gate | Actual outcome | UTC execution interval | Receipt SHA-256 |
| --- | --- | --- | --- |
| [Scientific bundle](scientific-bundle-validation.json) | All 31 hashes matched; nine programs each passed normally and with `-O`: **18 successful executions** | 2026-11-20 20:53:47.967645–20:54:27.791353 | `cb5d9fa8b4f70305bb2aeae6a38c3cf0ee8a2a0bc53024a9dd22942a79c8aa21` |
| [Complete repository validation](scientific-checkout-validation.json) | All **11 commands** passed, with regressions enabled | 2026-11-20 20:53:47.953596–20:53:53.155621 | `f07496417fff49ba80fcc9752febaa2ebed2dd8fcd220ec074759fec59f92902` |

The scientific runs include all four production programs, the four separate
lane reconstructions, and the additional source-rank block reconstruction.
Every expected report matched its frozen content. The optimized runs
retain their explicit validation gates. The occupation review's earlier
missing terminal receipt is not used to infer this execution: the bundle
ran its independent program again, normally and optimized, and recorded
both successful completions directly.

Before the content commit, the staged whitespace check passed and a local
Markdown-link check found all 45 actual relative links. Inline code and
displayed mathematics were excluded from the link parser, so expressions
such as a function applied to `x` were not misread as file links.

## What these checks mean

The complete-checkout gate covers repository integrity and the retained
regression suite. It does not certify the new mathematics. The scientific
bundle checks exact local identities, physical paths, stated bounded
corpora, all-source tail enclosures at the declared cutoffs, complete
finite residuals, and damaged-control rejection.

The universal deductions use the written proofs and their stated inputs:
geometric square tails for the infinite Hardy flows; all-parameter affine
and valuation identities for physical families; leading-term and
first-superdiagonal arguments for the excluded order classes; the marked
token invariant for scheduling-independent carry lower bounds; and
nonnegative source accounting for entropy and saturated capacity. The
quantitative spatial exponent retains its pinned PR153 dependency.

No human referee acceptance, formal verification of these new manuscripts,
external Lean rebuild, or complete replay of another research PR is claimed.
The latest-source audit is a written comparison at exact heads, through
PR161. The full forward-five law, a sufficient original-source carry
allowance, and the temporal occupation upper estimate remain unproved.

## Documentation child and final head

The following child of the executed commit adds this narrative and the two
actual receipts, and updates the report guide. No manifest-covered scientific
or review file is changed. The manifest and every covered file are checked
again on that child, and the required complete-checkout repository gate is
run separately on the exact final GitHub head. That final head and its actual
validation receipt are recorded in the PR, avoiding a claim that this
parent receipt executed a later commit.
