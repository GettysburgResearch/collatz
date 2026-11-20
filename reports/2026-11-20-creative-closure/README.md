# Review and replay of the creative-closure packet

The scientific entrance is
[the research overview](../../research/creative-closure-20261120/README.md).
**Collatz remains unresolved.** The reviews below are internal AI
reconstructions at frozen file hashes, not human acceptance or formal
proof-assistant verification.

## Review assignments and evidence

| Lane | Separate review | Distinct reconstruction |
| --- | --- | --- |
| Signed unweighted Hardy flows, CAF-001--006 | [Analytic review](ANALYTIC_REVIEW.md) | [Leaf-current checker](analytic-independent-check.py) follows literal paths forward from leaves; 24 flow cases, 17 exact production vector hashes, 39,496 shortcut edges, 14 finite tail checks, and all 28 antichain support pairs. |
| Mixed-base work, polynomial orders and run energies, CSO-001--005 | [Symbolic review](SYMBOLIC_REVIEW.md) | [Independent affine/moment checker](../../experiments/creative_symbolic_review.py) uses affine evaluations rather than the author's matrix composition; 14 physical edges and 126 moments at degrees 9, 12 and 17. |
| Source-rank carry obstruction, CSR-001 | [Source-rank review](SOURCE_RANK_REVIEW.md) | [Literal-rule block checker](source-rank-independent.py) checks the 54-bit certificate, 18 known first-hit controls and three modular pure-power targets. It does not test target convergence. |
| Physical five blocks and scalar carry controller, C5-001--005 | [Five review](occupation-five-review.md) | [Independent five checker](occupation-five-independent.py) checks 1024 source-cylinder blocks, 171 searched unit lifts, 1000 carry instances, 513 recharge classes and 88,533 finite modular states. |
| Coalescence information and saturated capacity, OCC-001--004 | [Occupation review](five-occupation-review.md) | [Independent occupation checker](five-occupation-independent.py) constructs actual return words differently, reconstructs the full-source entropy gap at return 8 and exactly matches the capacity bounds and finite positive repair. |

The root also read the complete physical-five and occupation proofs and
checked their formulas and scopes. Repeated reading is not counted as an
additional independent implementation.

## Production evidence

| Program | Retained report | Bounded coverage |
| --- | --- | --- |
| [Analytic flow](../../experiments/creative_analytic_flow.py) | [Report](analytic-flow-report.json) | 17 main rational-complex flow cases, eight antichain-root cases, 18,312 macro edges and 82,682 physical shortcut edges; 536 finite coercivity cases; 64 zero-eigenvalue collision pairs; five rejected corruption controls. |
| [Physical five](../../experiments/creative_five_closure.py) | [Report](five-report.json) | 3336 paired block instances, 1001 unit predecessor choices, 25 complete infinite-family instances, 1500 carry branch instances, five known-convergent renewals and six prescribed expansion lengths. |
| [Occupation](../../experiments/creative_occupation.py) | [Report](occupation-report.json) | 23,517 original unsafe atoms through 65,536 for sixteen entropy returns; 2941 originals through 8192 for complete first-hit capacity; 3475 exact flow identities; 200,655 physical shortcut edges. |
| [Symbolic order](../../experiments/creative_symbolic_order.py) | [Report](symbolic-report.json) | 3906 proper words and 7421 local rewrites; 774 carry-controller runs, of which 519 reach 1 and **255 return UNRESOLVED**; 1806 moment identities. |

Finite coverage does not prove the infinite deductions. The analytic
eigenspaces use written geometric-tail proofs. The all-degree polynomial
and all-dimensional triangular exclusions use leading-term deductions.
The physical families use exact all-parameter identities. The saturated
Dirichlet budget imports the explicitly pinned simple-path theorem; the
coalescence budget is proved by nonnegative information accounting.

The occupation decimal enclosures use outward exact integer intervals,
not floating-point comparisons. Capacity calculations use exact rational
mass and bound every omitted original source. Reviewer logarithms use a
different binary scaling and series implementation. No finite source
cutoff is silently substituted for the declared full-support input.

## Reproduce from a clean complete checkout

All nine scientific programs support `--compare` against their frozen
reports. Explicit validation exceptions remain active under optimized
Python. The bundle runs each program normally and with `-O`, checks all
manifest hashes, and verifies that the complete checkout stays clean.

```sh
python -X utf8 -B reports/2026-11-20-creative-closure/run_bundle.py --receipt /tmp/creative-science.json
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/creative-checkout.json
```

Use unused receipt paths outside the checkout. The science bundle refuses
to overwrite its receipt. A content-only audit, with no scientific
execution, is available as:

```sh
python -X utf8 -B reports/2026-11-20-creative-closure/run_bundle.py --manifest-only --receipt /tmp/creative-content.json
```

`CONTENT_SHA256.json` freezes scientific manuscripts, review records,
programs and expected reports. It excludes itself and later execution
receipts and publication narratives. A metadata-only child can therefore
attach actual parent-checkout receipts while preserving every scientific
byte. The receipts identify the commit actually executed; they are never
reassigned to a different head.

## Publication evidence

The [validation narrative](VALIDATION.md) identifies the real GitHub
scientific commit actually executed. Its attached
[scientific-bundle receipt](scientific-bundle-validation.json) records all
18 successful program executions, and its
[complete-checkout receipt](scientific-checkout-validation.json) records
all 11 successful repository checks with regressions. Both identify the
same complete clean 348-file checkout before and after execution.

The metadata child attaches these receipts without changing any of the
31 manifest-covered files. The exact final branch head and its separate
content and repository readback are recorded in the publication PR.
Repository integrity and successful finite replay remain distinct from
mathematical acceptance of the proposed deductions.
