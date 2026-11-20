# Review and execution index

The [scientific entrance](../../research/closure-frontier-20261121/README.md)
states the results, dependencies, and remaining gaps. All mathematics in
this packet remains PROPOSED. The reviews below reconstruct specified
claims; they do not establish full Collatz convergence, external acceptance,
or formal proof-assistant verification.

| Scientific note | Separate reconstruction | Author replay | Independent replay |
|---|---|---|---|
| [Five returns](../../research/closure-frontier-20261121/FIVE_RETURN_LANGUAGE.md) | [FR1--FR5 review](FIVE_RETURN_REVIEW.md) | [Frozen output](five_return_report.json) | [Frozen output](five_independent_report.json) |
| [Witness descent](../../research/closure-frontier-20261121/NEGATIVE_TEMPLATE_GRAMMAR.md) | [NT1--NT3 review](REVIEW_NEGATIVE_TEMPLATES.md) | [Frozen output](negative_template_report.json) | [Frozen output](review_negative_templates_report.json) |
| [Finite conductors](../../research/closure-frontier-20261121/FINITE_CONDUCTOR_RIGIDITY.md) | [FC1--FC6 review](FINITE_CONDUCTOR_INDEPENDENT_REVIEW.md) | [Frozen output](finite-conductor-report.json) | [Frozen output](independent-quotient-report.json) |
| [Ternary boundary](../../research/closure-frontier-20261121/TERNARY_STATIONARY_BOUNDARY.md) | [TM1--TM6 review](TERNARY_INDEPENDENT_REVIEW.md), [TM7 review](BOUNDED_ERROR_REVIEW.md) | [Frozen output](ternary-stationary-report.json) | [Frozen output](ternary-independent-report.json) |

The witness review found and corrected a wording issue: the clock change
is the change in the cumulative final exponent, not the final individual
gap. The bounded singular-template search claim was removed because its
scope was unnecessary to the proved result. The five report distinguishes
binary-cylinder density from the density after imposing ternary units.

Every checker uses exact integer or rational acceptance conditions and
explicit failures that remain enabled under optimized Python. Any decimal
display is explanatory. The source programs and independent programs use
different constructions where material: direct exponent congruences and a
different rounding grid for renewal; direct positive affine tables for the
template grammar; quotient-kernel powers for dyadic decorrelation; and
rational linear equations for stationary weights.

## Replay

From a clean complete checkout:

```sh
python -X utf8 -B reports/2026-11-21-closure-frontier/run_bundle.py --receipt /tmp/frontier-science.json
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/frontier-repository.json
```

The [bundle runner](run_bundle.py) checks every entry in the
[content manifest](CONTENT_SHA256.json), runs all eight scientific and
independent programs normally and with `-O`, and requires exact equality
with their frozen reports. It records the actual commit, tree, complete
tracked-file count, execution intervals, and clean before/after state.
It refuses a dirty checkout and a receipt path inside that checkout.

The repository validator is a separate integrity and bounded-regression
gate. Passing it does not verify the mathematical universal claims.
Publication-time receipts distinguish the scientific commit from any
later documentation-only child; none is inferred from a tree read or
from an earlier checkout.
