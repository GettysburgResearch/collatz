# Evidence for certificate transport and GRH interfaces

The [scientific overview](../../research/grh-certificate-closure-20261120/README.md)
states what is proved and what remains open. These are internal AI reviews
and exact finite executions, not human referee acceptance or formal
verification. No universal Collatz or forward-five closure is claimed.

## Mathematical review scope

| Result | Review | Scope |
|---|---|---|
| Arbitrary-run five ladder and certificate compiler | [REVIEW_FIVE_LADDER.md](REVIEW_FIVE_LADDER.md) | Independent reconstruction of FL1--FL4, actual integer legality, first-hit clocks, disjoint cylinder density and the partial compiler. Includes a separate literal implementation. |
| Complete-ladder energy renewal | [REVIEW_LADDER_RENEWAL.md](REVIEW_LADDER_RENEWAL.md) | Independent reconstruction of harmonic and .84 contraction, inverse multiplicities, zero endpoint defect, exact rational bounds and finite-cutoff subtraction. No uncovered-energy bound. |
| GRH interfaces | [REVIEW_GRH_INTERFACES.md](REVIEW_GRH_INTERFACES.md) | Independent reconstruction of G1--G5; external GRH theorems remain source-qualified. Separate finite arithmetic implementation with no author imports. |
| High-exponent rigidity attempt | [REVIEW_RIGIDITY.md](REVIEW_RIGIDITY.md) | Root reconstruction of restricted adjacency, periodicity, exact small inverse obstructions and the cited S-unit application. Review of the full-class 43-move verifier. Uniform-J closure remains open. |

The review documents pin exact SHA-256 contents. Working-directory names
in the frozen author/reviewer records refer to the pre-integration source
locations; the reviewed files now live in this packet. No hash pin denotes
blanket acceptance of later changes.

## Reproduce the exact finite checks

From a complete clean checkout, write the execution receipt outside it:

```sh
python -X utf8 -B research/grh-certificate-closure-20261120/check_packet.py --require-clean --receipt /tmp/collatz-grh-packet-replay.json
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/collatz-grh-checkout-validation.json
```

The first command checks every content-manifest entry, decompresses the
three raw bounded-search reports and checks their frozen identities, and
runs six scientific programs normally and with `-OO`. Every output must
match its frozen report byte for byte. It also checks that the checkout
does not change. The second command is the repository's complete-checkout
gate with its eleven integrity and selected regression commands.

| Program | Frozen report |
|---|---|
| `check_five_certificate_ladder.py` | [five-ladder-report.json](five-ladder-report.json) |
| `check_five_ladder_review.py` | [five-ladder-independent-report.json](five-ladder-independent-report.json) |
| `check_ladder_renewal.py` | [ladder-renewal-report.json](ladder-renewal-report.json) |
| `check_grh_interfaces.py` | [grh-interface-report.json](grh-interface-report.json) |
| `review_grh_interfaces_independent.py` | [grh-interface-independent-report.json](grh-interface-independent-report.json) |
| `check_rigidity_interfaces.py` | [rigidity-interfaces-report.json](rigidity-interfaces-report.json) |

All six programs are under
`research/grh-certificate-closure-20261120/`. The GRH reviewer program's
standalone invocation needs `--source-dir` pointing to that directory;
the packet driver supplies it. The rigidity sample is retained beside
its checker as `level8-sample-verification.json`.

The bounded exploratory searches at J=7,8,9 are not rerun by the scientific
driver. Their original raw JSON reports are archived losslessly as
`level-7.json.gz`, `level-8.json.gz`, and `level-9.json.gz`; their summary
and uncompressed hashes are in
[bounded-level-search-summary.json](bounded-level-search-summary.json).
These are slope-contracting cells at the stated search limits, not an
exhaustive universal result. Only the selected 43-move certificate is
independently replayed for whole-class legality and strict descent.

To repeat the exploration, copy `search_shifted_levels.py` to a separate
temporary directory and run it there: it writes the three raw reports
beside itself. Its wall-clock deadline makes timings machine-dependent.
The retained runs completed all their finite cells without reaching that
deadline. No claim of exhaustive inverse search is made.

## Publication evidence

The [actual publication record and receipts](PUBLICATION.md) identify the
fetched scientific commit, twelve successful mathematical executions and
the eleven-command complete-checkout validation.

The scientific contents and frozen reference outputs are committed
together. Actual fetched-commit validation receipts are appended in a
documentation-only child after checking the real GitHub scientific
commit. The final publication record distinguishes that tested parent
from the metadata child; it does not retroactively attribute executions
to an untested source identity. The content manifest excludes only this
guide, itself, and later publication receipts so they can record the
tested identity without a self-reference.
