# X-9409 — Primitive period-four reduced-height census

Experiment ID: X-9409  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: R-9403, Q-9411, O-9401  
Classification: exact bounded computation; no asymptotic theorem

## Research question

The universal L-9410 estimate misses irrationality at period four by only
`0.6286%` on the logarithmic scale. Do the first exact reduced approximants of
primitive `{17,18}` period-four words exhibit a common-factor or height saving
large enough to suggest that the same family is rescued after reduction?

## Environment

- Python 3.11 or newer;
- standard library only;
- exact sparse integer-polynomial arithmetic;
- no network, solver, randomness, or external data.

## Replay

```bash
python3 -B -m py_compile experiments/X-9409-period-four-height/run.py
python3 -B experiments/X-9409-period-four-height/run.py \
  --check-results experiments/X-9409-period-four-height/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9409-period-four-height/run.py \
  --write-results experiments/X-9409-period-four-height/results/canonical.json
```

Canonical SHA-256:

```text
bf85a00cc1b34aef1d85f5b7e483547b1200ac10e53c02375333447bb1c31546
```

The frozen run takes roughly half a minute on a typical contemporary machine.

## Primitive cyclic representatives

Up to cyclic rotation and complementing `17 <-> 18`, the frozen census uses

```text
17,17,17,18;
17,17,18,18;
17,18,18,18.
```

The alternating word `17,18,17,18` is deliberately omitted because its minimal
period is two and T-9414 already excludes it.

## Exact results

| word | order | gcd bits | reduced height bits | error `v_2` | exponent |
|---|---:|---:|---:|---:|---:|
| `17,17,17,18` | 1 | 16 | 158,139 | 159,150 | 1.006393109859 |
| `17,17,17,18` | 2 | 48 | 631,224 | 631,284 | 1.000095053420 |
| `17,17,17,18` | 3 | 89 | 1,419,265 | 1,416,402 | 0.997982758681 |
| `17,17,18,18` | 1 | 9 | 160,314 | 161,310 | 1.006212807366 |
| `17,17,18,18` | 2 | 17 | 640,157 | 640,140 | 0.999973444015 |
| `17,17,18,18` | 3 | 25 | 1,439,528 | 1,436,490 | 0.997889586031 |
| `17,18,18,18` | 1 | 16 | 162,704 | 163,740 | 1.006367391091 |
| `17,18,18,18` | 2 | 93 | 649,439 | 649,536 | 1.000149359678 |
| `17,18,18,18` | 3 | 87 | 1,460,349 | 1,457,388 | 0.997972402487 |

All three primitive classes are below exponent one by order three. The observed
cleared gcd sizes are tiny compared with million-bit reduced heights.

## Interpretation boundary

The census is a bounded negative observation, not an asymptotic gcd theorem.
It shows that an immediate large common-factor rescue is absent at the first
three orders tested. It does **not** prove:

```text
- that all later reduced exponents remain below one;
- that no different period-four determinant works;
- that period-four values are rational;
- anything about the balanced nonperiodic directive;
- the Collatz conjecture.
```

The correct next task remains Q-9411: prove or refute a quadratic-scale height
saving, rather than extrapolating these finite records.
