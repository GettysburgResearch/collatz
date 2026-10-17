# X-8801 — Exact `ax+1` portability controls

Experiment ID: X-8801  
Agent: `gpt56-drift-01`  
Issue: #26  
Classification: **EXACT FINITE COMPUTATION**  
Created: 2026-07-22

## Research question

Which first-layer Collatz mechanisms survive replacement of multiplier `3` by
a general odd `a`, and what exact positive controls are visible at `a=5`?

The experiment tests four interfaces:

1. the universal affine parity-word identity;
2. exact one-step `2`-adic fuel loss;
3. cycle and same-phase chart reconstruction with full physical replay;
4. a finite, reproducible stress test of the `5x+1` orbit of seed `7`.

## Exact code

`run.py` uses only the Python standard library and integer arithmetic, except
for high-precision `Decimal` evaluation of displayed logarithmic constants.

## Canonical command

```bash
python3 -B -m py_compile experiments/X-8801-ax1-portability/run.py
python3 -B experiments/X-8801-ax1-portability/run.py \
  --check-results \
  experiments/X-8801-ax1-portability/results/canonical.json
```

To regenerate the file instead:

```bash
python3 -B experiments/X-8801-ax1-portability/run.py \
  --output experiments/X-8801-ax1-portability/results/canonical.json
```

## Frozen parameters

```text
cycle parity-word length: <= 14
affine multipliers:        3,5,7,9
affine seeds:              1..256
affine prefix lengths:     1..12
fuel-loss values:          1..256
4 -> 5 chart q range:      1..100000
T_5 seed-7 orbit prefix:   1000000 shortcut steps
checkpoint interval:       1000 steps
random seeds:              none
```

## Software environment

Canonical generation in this session used:

```text
Python 3.13.5
Linux 6.12.13 x86_64
third-party packages: none
```

## Canonical output digest

```text
SHA-256(canonical.json)
285279f0360a9a9a91bb12d3529937e0238ef6c95f22f6a6ebd4ee8c8b4d45ab
```

The output also records separate SHA-256 digests for the million-step final
value, the parity stream, and serialized checkpoints.

## Results

The canonical run records:

- 12,288 exact affine-formula checks;
- 65,024 exact shared-branch fuel-loss checks;
- 200,000 exact physical replays of the two `T_5^2` `4 -> 5` branches;
- exhaustive fixed-phase block censuses for the frozen shapes;
- exhaustive parity-word cycle reconstruction through length `14`;
- exact recovery of the `a=5` cycles with seeds `1`, `13`, and `17`;
- one million exact shortcut steps from seed `7`.

For the seed-`7` prefix:

```text
odd steps:                 500093
even steps:                499907
minimum value:             7
last step at or below 7:   0
final decimal digits:      48521
maximum bit length:        161185
record highs:              131088
```

## Interpretation

The universal identities and each finite replay are exact in the stated scope.
The same-phase census exposes an arithmetic break: the literal `a=3`,
length-`6`, weight-`4` phases do not port to `a=5`, while a simpler exact
length-`2`, weight-`1` `4 -> 5` chart appears.

The million-step seed-`7` prefix is a stress-test artifact only. It does not
prove divergence, nonrecurrence, or avoidance of a later cycle.

## Limitations

- Cycle enumeration ends at parity-word length `14`.
- Fixed-phase censuses cover only the explicitly frozen shapes.
- One million steps remain finite regardless of the size reached.
- Decimal logarithms illustrate exact formulas; theorem claims use symbolic
  inequalities, not floating-point evidence.
- No statistical independence assumption is made.

## Associated claims

D-8801, L-8801, T-8801, L-8802, T-8802, T-8803, O-8801.
