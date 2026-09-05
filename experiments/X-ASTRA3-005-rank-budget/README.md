# X-ASTRA3-005 — exact rank-budget and unsafe-repayment interfaces

This finite certificate accompanies [the fifth research pass](../../research/astra-three-routes/pass5/README.md).
It does not certify Collatz, a universal unsafe estimate or complete guard coverage.
All arithmetic is standard-library integer or Fraction arithmetic.

```bash
python -B experiments/X-ASTRA3-005-rank-budget/run.py \
  --check experiments/X-ASTRA3-005-rank-budget/results/canonical.json
python -B experiments/X-ASTRA3-005-rank-budget/verify.py \
  experiments/X-ASTRA3-005-rank-budget/results/canonical.json --self-test
python -O -B experiments/X-ASTRA3-005-rank-budget/verify.py \
  experiments/X-ASTRA3-005-rank-budget/results/canonical.json --self-test
```

`run.py --output PATH` writes the deterministic report. The verifier imports
no generator or repository module. It searches rank components until their
ordinary size exceeds the best known rank, computes A by literal shortcut
steps, reconstructs word cylinders bit-by-bit, and uses extended Euclid for CRT.
The generator uses the parent's exact four-entry rank formula, affine modules,
final modular inversion and a differently ordered rank-fiber census.

## Frozen scope

- Six COMPLETE rank balls:1,16,256,4096,65536,16777216. The verifier additionally
  scans every source up to B+1 for B<=65536, using the proved R(n)>=n-1 bound.
- The largest rank ball contains10,195 sources, maximum14,348,908. Their
  trajectories are not declared convergent by this rank census.
- Nine safe-kernel moment rows from an arbitrary finite nonnegative distribution
  on1,311 safe sources. Safe exits are counted separately, not declared killed
  by Collatz convergence.
- Eight moment-spike inputs,45 barrier/repayment inputs,405 reverse-ray entries,
  855 repayment path positions,96 unsafe-switch inputs and1,728 A modules.
- Five explicit monomial-weight failures and four retained residual controls.
- Ten genuine resealed corruptions are rejected, including scope, coverage,
  barrier, unsafe, moment and rank changes.

The infinite-family and global counting statements are the accompanying written
proofs, not extrapolations of these rows. Both implementations have the same
author, so they do not constitute independent mathematical review.

Semantic SHA-256:

    1dc5510f205dd8b4a106a636af68ef8a7252a867fc1e4c10310d93e54567fb5d
