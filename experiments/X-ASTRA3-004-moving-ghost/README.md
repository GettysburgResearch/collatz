# X-ASTRA3-004: moving-ghost finite interfaces

All theorem-level claims are PROPOSED. This experiment is not a Collatz proof
or independent mathematical review. It is standard-library Python and uses
exact integers and Fraction arithmetic; no floating-point proof decision.

From the repository root:

```bash
python -B experiments/X-ASTRA3-004-moving-ghost/run.py \
  --check experiments/X-ASTRA3-004-moving-ghost/results/canonical.json
python -B experiments/X-ASTRA3-004-moving-ghost/verify.py \
  experiments/X-ASTRA3-004-moving-ghost/results/canonical.json --self-test
```

Use run.py --output PATH to regenerate the canonical report. Both programs
fail on a mismatch; they do not repair the submitted report automatically.
The verifier does not import the generator or any repository module.

Frozen coverage:

    ordinary sources:             2..16384 (16383 values)
    literal shortcut positions:   44933
    sampled rank fibers:          10930
    moving-index CRT cases:       88
    backward power-family cases:  16
    inverse endpoints:            2..128
    inverse source cap:           8192
    complete capped inverse edges:504
    ordinary renewal lifts:       576
    complete occupation intervals:4
    resealed tamper cases:        8

The source cap applies ONLY to the finite inverse-comparison experiment.
The theorem's complete fan retains its infinite even ray, and the analytic
occupation/resolvent statements have their explicitly proved infinite tails.
The four occupation intervals include every initial source and every possible
residence length by the exact identity, not by numerically exploring infinity.

The two implementations independently agree on 13458 forward rank drops,
510 additional inverse drops, and 2415 residual labels in the source pilot.
Residual is not nonconvergence. The larger quarter-drop region sends only 128
pilot starts to 1 before becoming unsafe; 16255 terminate at an unsafe input.
This is deliberately not advertised as a complete convergence algorithm.

Semantic SHA-256:

    7ac43379cc79e1cd550a77a72d8587b0e7d9b5cd45ed2bbf10895e16667b9710

The proofs, full scope, counterexamples, and exact source attribution are in
[the fourth-pass entrypoint](../../research/astra-three-routes/pass4/README.md).
