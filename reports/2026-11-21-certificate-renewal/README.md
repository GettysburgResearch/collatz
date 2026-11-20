# Review and execution record: certificate renewal and arithmetic moments

This report supports the [scientific packet](../../research/certificate-renewal-20261121/README.md). The full theorem remains OPEN. Internal mathematical reconstruction, exact finite arithmetic verification, bounded ordinary replay and repository integrity checks are separate evidence levels.

## Mathematical review

| Manuscript and claims | Review record | Scope and result |
|---|---|---|
| `C5_CERTIFIED_BYPASSES.md`, CB1–CB4 | [Independent paired-path reconstruction](REVIEW_C5_BYPASSES.md), plus [root review](ROOT_REVIEW.md) | VERIFIED on the two exact parameter classes; no all-parameter coverage. The independent code imports no production checker. |
| `FIVE_WORD_EXTENSION.md`, FW1–FW5 | [Independent compiler and coefficient review](REVIEW_FIVE_WORD_EXTENSION.md), plus root review | VERIFIED for the enlarged dictionary, all inverse tails, the complete ternary cover and the finite-cutoff energy deduction. |
| `MOMENT_QUANTILES.md`, MQ1–MQ5 and closing implications | [Independent moment review](REVIEW_MOMENT_QUANTILES.md) | VERIFIED relative to the explicitly pinned occupancy proof. The asymptotic moment estimates themselves remain open; cycles are excluded from this implication's scope. |
| `FIXED_ENDPOINT_SUMMABILITY.md`, ES1–ES4 and standalone question | [Endpoint review and contribution disclosure](REVIEW_ENDPOINT_SUMMABILITY.md) | VERIFIED elementary deductions. The reviewer discloses participation in the sharpening of the telescoping bound. The [separate independent telescope review](REVIEW_ENDPOINT_TELESCOPE.md) verifies ES3–ES4 without participation in their derivation. |

Each review records exact manuscript and relevant checker hashes. A verdict does not extend to a different file, future source head or universal closure. No external human review or new proof-assistant build is claimed.

## Actual scientific executions

Four production checkers and one independent C5 reconstruction were executed in the complete working tree, each in normal Python and with `-OO`. All ten executions exited zero. Normal and optimized reports are byte-identical for each checker, and all stderr streams are empty. The exact commands, timestamps, durations and hashes are retained in [scientific-executions.json](scientific-executions.json).

| Replay | Exact retained evidence | Scope |
|---|---|---|
| Paired contractions | [c5-bypasses-report.json](c5-bypasses-report.json) | 76 affine prefix steps, 16 supplied-certificate conversions on eight finite fixtures, six rejected malformed controls; exact exponent congruences and all-lift identities. |
| Expanded five compiler | [five-word-report.json](five-word-report.json) | 40 algebraic instances, 680 paired ordinary replays, 28 complete compiler fixtures, malformed/unresolved controls, and an exhaustive 184-leaf rational coefficient certificate with analytic infinite tails. |
| Arithmetic moments | [moments-report.json](moments-report.json) | Exact primitive representatives and source cylinders; rigorous finite moment enclosures through length 12 including all omitted exponents; finite simple-path diagnostics. No asymptotic estimate is inferred. |
| Endpoint summability | [endpoints-report.json](endpoints-report.json) | Exact telescoping identities, sharp polynomial factorization, finite-source diagnostics and exact geometric tails after reaching one. Infinite-time conclusions follow from the manuscript proof. |
| Separate paired-path code | [c5-independent-report.json](c5-independent-report.json), [code](review_c5_affine.py) | Independently reconstructs the eight affine prefixes, their endpoint constants and contraction parameters. |

For reproduction, from the repository root run:

```sh
python3 -X utf8 -B research/certificate-renewal-20261121/check_c5_certified_bypasses.py
python3 -X utf8 -B research/certificate-renewal-20261121/check_five_word_extension.py
python3 -X utf8 -B research/certificate-renewal-20261121/check_moment_quantiles.py
python3 -X utf8 -B research/certificate-renewal-20261121/check_endpoint_summability.py
python3 -X utf8 -B reports/2026-11-21-certificate-renewal/review_c5_affine.py
```

Adding `-OO` after `python3` leaves all checks active. The moment checker bounds a truncated exponent computation rigorously; it never treats its finite exponent menu as the full sum without the omitted-tail allowance.

## Repository and provenance

The [selected source snapshot](source-snapshot.json) freezes live branch metadata, and [SOURCES.md](../../research/certificate-renewal-20261121/SOURCES.md) specifies mathematical use. The latest PR146 head was included before writing the final comparison. The [content manifest](content-manifest.json) authenticates the scientific files, review records and retained finite outputs.

The [validation record](VALIDATION.md) distinguishes the scientific publication parent from its documentation-only child. Complete-checkout validation and a scientific replay answer different questions. A successful repository check does not prove Collatz or discharge an open mathematical premise.
