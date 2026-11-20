# Publication validation

The scientific files have completed the ten executions recorded in `scientific-executions.json`: four production checkers and a separate paired-path reconstruction, each in normal and optimized Python, all successful with matching mode outputs.

The publication procedure freezes these scientific bytes in a commit, runs the repository's complete-checkout gate on that actual remote commit, and then records its receipt in a documentation-only child. The completed receipt and exact published parent will be added by that child. This preparation text makes no claim of a repository-gate execution before it occurs.

The required command is:

```sh
python3 -X utf8 -B tools/validate.py --regressions --receipt /absolute/path/outside/checkout.json
```

No remote CI execution, external referee acceptance or formal verification is claimed by the local checks.
