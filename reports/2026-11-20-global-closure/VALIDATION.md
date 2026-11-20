# Validation and publication boundary

The manuscripts, certificates, deterministic reports, and separate reviews
are listed in `CONTENT_SHA256.json`. Their agent reconstruction verdicts
are recorded in the four review files. No verdict asserts a full Collatz
proof, external acceptance, or proof-assistant verification.

## Publication execution

Exact clean-checkout publication receipts will be attached after the first
GitHub content commit is created and executed. This initial documentation
does not claim a future command has passed. The final publication update
will identify the executed commit, its complete tree, command counts, and
the documentation-only relationship to the publication head.

## Required commands

```sh
python -X utf8 -B reports/2026-11-20-global-closure/run_bundle.py --receipt /absolute/path/outside-checkout/science.json
python -X utf8 -B tools/validate.py --regressions --receipt /absolute/path/outside-checkout/repository.json
```

The new bundle's manifest comparison, exact deterministic outputs,
independent calculations, and expected optimized-mode rejection are
distinct from the existing repository validator. Both require a clean,
complete checkout and record its actual commit and tree before and after
execution. The receipts preserve actual exit codes and output.

## Interpretation

The all-lift affine legality and coverage checks support the conditional
descent proof. Bounded orbit replays support only their recorded domains.
The transport's infinite omitted-source tail is a proved analytic bound,
not a computation of infinitely many orbits. Passing repository validation
establishes the stated integrity and regression checks, not the mathematical
truth of an unproved global premise.
