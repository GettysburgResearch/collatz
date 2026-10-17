# X-8506 — Eight-block primitive-core compiler audit

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Claim:** `L-8506`  
**Status:** exact finite interface audit

## Question

For every finite core state, do the four binary target cells split into exactly two admissible ternary source lifts, and does each resulting ordinary block realize the claimed high-tail replacement?

## Implementations

- `derive.py` exhausts every finite state and target at two large heights, both ternary lifts, and three high-tail values.
- `verify.py` is separately written and uses a different height and tail set.

## Replay

```bash
python3 -B experiments/X-8506-core-block-compiler/derive.py \
  --output experiments/X-8506-core-block-compiler/results/canonical.json \
  --summary experiments/X-8506-core-block-compiler/results/summary.txt

python3 -B experiments/X-8506-core-block-compiler/verify.py \
  experiments/X-8506-core-block-compiler/results/canonical.json
```

## Frozen result

```text
finite core states:          24
target binary blocks:        96
admissible ternary lifts:    192
exact block replays:         576
170-bit growth checks:       576

semantic digest:
cf101f17607a6c9f0c42c4723cc72968ee93acdeb8114ce20e3d3770107c827c
```

Independent checker:

```text
finite states:              12
binary target blocks:       48
ordinary block replays:     192
all independent checks passed
```

## Limitations

The compiler proves every local branch exactly. It does not prove that an output block belongs to a legal block at every later scale.
