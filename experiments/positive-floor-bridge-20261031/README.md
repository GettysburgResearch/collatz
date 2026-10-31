# Exact bounded verification of the positive-floor bridge

From the repository root:

```sh
python -X utf8 -B experiments/positive-floor-bridge-20261031/check_positive_floor.py --output /tmp/positive-floor.json
python -O -X utf8 -B experiments/positive-floor-bridge-20261031/check_positive_floor.py --output /tmp/positive-floor-optimized.json
```

The script uses only Python's standard library and imports the recovered
`../beeping-density-swarm-20261031/check_inverse_green.py` helper. Acceptance
checks are explicit exceptions, not assertions disabled by `-O`.

The saved JSON is a deterministic complete output. The report records both
fresh executions and their byte equality. The test computes exact first-letter
and dead-leaf geometric sums, exact ternary laws through depth six,
synchronized-clock frontiers, and finite killed-model Green functions.
Finite models have 16, 32, and 64 odd states and use exact geometric renewal
for cycles; they do not rely on an arbitrary simulation stopping time.

The external infinite-state uniform-floor premise, the existence of canonical
limits, external Lean proofs, and Collatz are **not** verified by these tests.
