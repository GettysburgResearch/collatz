# X-8508 — Canonical top-boundary run bound

**Issue:** #43  
**Agent:** `gpt56-cylinder-01`  
**Status:** exact finite-constant audit supporting proposed `T-8509`

## Question

Can a hypothetical infinite ordinary refund path evade the multiplicative top-boundary refund of `T-8508` by taking the canonical lift `ell=0` forever, or for arbitrarily long runs?

## Exact inequality

At a canonical state the primitive core has the absolute cap

```text
log_2(C) < 22*t+559.
```

Every legal core step has the exact lower gain

```text
log_2(C_next/C) > (63*t-121080)/665,
```

using the integer certificate

```text
3^665 > 2^1054.
```

For `r+1` consecutive canonical lifts beginning at height `t`, these bounds require

```text
[r*(63*t-121080)+504*r*(r-1)]/665
  < 22*(t+16*r)+559.
```

## Frozen conclusions

- From height `3760`, `r=470` violates the inequality. Therefore `471` consecutive canonical lifts are impossible and refunded events have lower density at least `1/471`.
- From height `1,140,416`, `r=233` violates it. Therefore `234` consecutive canonical lifts are impossible and the asymptotic lower density improves to `1/234`.
- The asymptotic transition count `233` is the first integer for which the coefficient of `t` is positive:
  ```text
  63*232 <= 665*22,
  63*233 > 665*22.
  ```

Table digest:

```text
a9bac5d31f9d5c2664d627c474941c2c7859c830b729c07567fdbba91daa53ef
```

## Independent implementation

`derive.py` computes the obstruction by one closed integer expression and derives the exact crossing heights.

`verify.py` does not import `derive.py`. It independently compares the raw lower-growth and endpoint-cap integers, scans for the first forbidden run length, recomputes the first multiple-of-sixteen crossing, and checks asymptotic minimality.

## Replay

```bash
python3 -B experiments/X-8508-canonical-run-bound/derive.py \
  --output /tmp/X-8508.json \
  --summary /tmp/X-8508.txt \
  --check-results \
    experiments/X-8508-canonical-run-bound/results/canonical.json

python3 -B experiments/X-8508-canonical-run-bound/verify.py \
  experiments/X-8508-canonical-run-bound/results/canonical.json
```

## Limitations

- Positive density of refunded events is conditional on the existence of an infinite ordinary path.
- The theorem does not construct the first legal state or force any one changing residue.
- The constants are rigorous but not claimed optimal.
- A refunded event may be followed by canonical events; no monotonicity of the top quotient across the entire orbit is asserted.
