# X-0018 — Linear-height quotient-refund audit

Experiment ID: `X-0018`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of the exact finite algebra in `L-0035` and `T-0040`

## Questions

1. Does every one-transition type pair define one canonical ordinary cylinder?
2. Does every overlapping type triple reduce to one affine quotient residue and carry?
3. Are the overlap carries nonnegative?
4. Does the arbitrary-width exponent margin simplify to the formula in `T-0040`?
5. Are the first certified thresholds exactly `3744`, `5600`, `31600`, and `477424` for widths `1`, `2`, `16`, and `256`?
6. Do all positive free lifts grow strictly at the width-one threshold?
7. Does the same mechanism replay on width-two blocks?

## Method

`run.py` uses Python standard-library integers only. It:

- derives the exact odd and binary exponents;
- computes canonical modular inverses for the tower cylinders;
- checks all sixteen one-transition cylinders at height `3744`;
- checks all sixty-four overlapping type triples;
- replays every triple for high lifts `1`, `2`, and `17`;
- constructs every width-two type word at height `5600`;
- checks 256 deterministic representative width-two block overlaps;
- verifies strict quotient growth and the exact physical scaled-tail identities.

The script avoids constructing the enormous powers at widths `16` and `256`; there it checks the exact integer margin that, together with `3^53>2^84`, proves the comparison.

## Replay

```bash
python3 -m py_compile experiments/X-0018-linear-refund/run.py
python3 experiments/X-0018-linear-refund/run.py
```

Expected output:

```text
linear-height quotient-refund checks passed
thresholds={1: 3744, 2: 5600, 16: 31600, 256: 477424}
one_step_triples=64
width_two_words=64 width_two_pairs=256
semantic_sha256=8dac15e86cea91d6d131bb753980cad8549df680e7e9265948372915674ff901
```

A local replay during authoring completed in approximately fifteen seconds in the available container. Timing is informational only.

## Limitations

- Exact finite overlap does not choose one quotient satisfying infinitely many future cylinders.
- The experiment does not prove a one-counter invariant or top-boundary closure.
- A modular cycle without a finite-support or most-significant-boundary proof is not an ordinary witness.
- No positive Collatz counterexample is claimed.