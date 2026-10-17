# X-9412 — Väänänen–Wallisser measure comparison

Experiment ID: `X-9412`  
Agent: `gpt56-complexity-01`  
Issue: #18  
Associated claims: `L-9413`, `L-9414`, `R-9408`, `Q-9413`  
Classification: exact symbolic comparison plus high-precision source-formula replay

## Research question

Can the published quantitative Väänänen–Wallisser measure for the first nine
phases be combined with the scalar Padé exponent of one additional phase?

The source exponent is

```text
theta(gamma,D)
 =1+(2D-1+sqrt(1+4D^2))
      /(2-gamma*(2D+1+sqrt(1+4D^2))),

gamma=1-log(64)/log(81).
```

The scalar phase exponent is

```text
tau=9/log_2(81).
```

## Replay

```bash
python3 -B -m py_compile experiments/X-9412-vw-measure/run.py
python3 -B experiments/X-9412-vw-measure/run.py \
  --check-results experiments/X-9412-vw-measure/results/canonical.json
```

To regenerate:

```bash
python3 -B experiments/X-9412-vw-measure/run.py \
  --write-results experiments/X-9412-vw-measure/results/canonical.json
```

Canonical SHA-256:

```text
b1f82225c0c8dc5013d5c709e00f924ca5e9e0c178d2c438bf252bfe3add4458
```

## Frozen scope

The script evaluates the source formula for every admitted dimension
`1<=D<=9`. It records the source threshold, the positive denominator, and the
translated valuation exponent.

The exact proof does not rely on decimals:

```text
tau<3/2
```

because `81>2^6`, while

```text
theta(gamma,D)
 >=theta(gamma,1)
 >(3+sqrt(5))/2
 >5/2.
```

Selected values:

| `D` | published `theta(gamma,D)` |
|---:|---:|
| 1 | `2.882180476090808...` |
| 5 | `22.855871484435403...` |
| 8 | `136.301150022255480...` |
| 9 | `2318.657271149257799...` |

The scalar value is

```text
tau=1.419591945535779... .
```

## Interpretation boundary

The replay validates the transcription and finite numerical table. The
universal method closure is the exact inequality in `R-9408`.

This experiment does not prove that the published measure is optimal, does not
rule out a special-vector or two-dimensional `q`-difference argument, and does
not prove or disprove period-ten irrationality, an ordinary M1 witness, or the
Collatz conjecture.
