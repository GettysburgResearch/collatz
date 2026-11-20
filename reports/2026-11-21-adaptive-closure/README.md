# Execution and scoped internal review

The scientific overview is in
[the research packet](../../research/adaptive-closure-20261121/README.md).
All new mathematics remains PROPOSED; the full Collatz theorem is OPEN.
The proofs state which existing source reductions are imported.

## Review coverage

| Subject | Reconstruction | Scope |
| --- | --- | --- |
| Exact affine-section Foster theorem | [Witness review](REVIEW_AFFINE_SECTION_RECURRENCE.md) | State lattice, conditional drift, properness, finite-core hitting, density qualifications |
| Root returns and pressure | [Witness review](REVIEW_AFFINE_ROOT_RETURN.md) | PR146 controller, root recurrence, ordinary density, infinite mean, endpoint-bit guard, PR167 averaging |
| Valuation-one V1–V5 | [Sieve review](REVIEW_VALUATION_ONE_TRANSPORT.md) | Ordinary paths, two-class renewal, residual and decoder obstruction; repeated-block attribution |
| Valuation-one V1–V4 | [Separate energy review](VALUATION_ONE_INDEPENDENT_REVIEW.md) | Independent written reconstruction and separately implemented finite checker; V5 excluded |
| All three routes and synthesis | [Primary-agent reconstruction](ROOT_RECONSTRUCTION.md) | Listed frozen manuscripts, specific algebra and quantifiers; coordination disclosed |

The latest-source audit corrected overlap with PRs167–169 before freezing.
The root integration summaries also received a final scoped read from
the witness and sieve agents. Their two wording suggestions—endpoint-bit
normalization and the exact rejected prefix pattern—were incorporated.
These are internal AI-agent reviews, not external referee acceptance or
formal proof-assistant verification.

## Frozen finite checks

Five programs have frozen normal and optimized reports. They use actual
ordinary maps and exact integer/rational arithmetic; no random sample
is treated as a proof of an infinite probability statement.

| Program | Normal report | Optimized report |
| --- | --- | --- |
| `check_affine_section_recurrence.py` | [Affine sections](affine-section-check.json) | [Optimized](affine-section-check-optimized.json) |
| `check_linear_horizon_sieve.py` | [Linear sieve](linear-horizon-report.json) | [Optimized](linear-horizon-report-optimized.json) |
| `check_simple_prefix_product_sieve.py` | [Simple prefixes](simple-prefix-product-report.json) | [Optimized](simple-prefix-product-report-optimized.json) |
| `check_valuation_one_transport.py` | [Valuation-one transport](valuation-one-check.json) | [Optimized](valuation-one-check-optimized.json) |
| `check_valuation_one_review.py` | [Independent implementation](valuation-one-review-check.json) | [Optimized](valuation-one-review-check-optimized.json) |

The sieve reviewer additionally reran the author valuation-one program;
its [normal](witness-cross-review-normal.json) and
[optimized](witness-cross-review-optimized.json) outputs are retained.
Those two are independent executions, not an independent implementation.

All five author/reviewer report pairs were actually generated before
integration and are byte-identical within each pair. The affine report
includes the two final manuscript hashes. Exact scientific file identities
and command mappings are frozen in [the manifest](manifest.json).

From the repository root, run the complete frozen scientific replay with
an outside-checkout receipt path:

```bash
python -X utf8 -B research/adaptive-closure-20261121/replay.py --receipt ../adaptive-scientific-replay.json
```

The driver executes each of the five programs normally and with `-OO`,
checks exact output bytes against the reports, verifies every manifest
entry, and confirms that the complete checkout remains clean and at the
same head. `--manifest-only` checks identities without rerunning science.

The critical negative-moment interface is a source-qualified analytic
deduction. No finite program is advertised as verifying its infinite
series criterion. The sieve checkers do not revalidate the imported
71-path cover. Repository integrity is a separate required gate, not
mathematical verification of the new or imported theorems.

## Publication receipt boundary

Actual remote-head execution and clean-checkout receipts are added after
the scientific commit is created and fetched. No preliminary local run
is retroactively attributed to a future commit. The publication note
will identify the exact scientific commit and any documentation-only
child separately.
