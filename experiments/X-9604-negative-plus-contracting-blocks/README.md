# X-9604 — Negative block plus contracting block powers

**Status:** `EMPIRICAL` exact finite computation  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Associated claim:** `L-9604`

## Family

The word has the compressed form

\[
(1,2)^m v^n,
\]

where `v` is a primitive contracting valuation block. `L-9604` proves that every positive cycle in this family must satisfy

\[
8^m2^{A(v)n}-9^m3^{k(v)n}
\mid
(9^m-8^m)\,\Omega((1,2),v).
\]

For fixed `v,m`, the mixed denominator is strictly increasing once positive. The search therefore stops **all** later `n` as soon as the denominator exceeds the fixed right-hand side.

## Frozen library

```text
1 <= m <= 1,000
1 <= length(v) <= 5
1 <= each valuation of v <= 6
v primitive
2^A(v) > 3^k(v)
v != (2)
```

This gives `9,237` primitive contracting blocks.

## Result

```text
reduced divisibility rows:   761,934
terminal all-later-n cutoffs: 9,237,000
exact cycle hits:                    0
```

```text
results SHA-256:
ac745cf38fea8ddcc5811b0f31d6c1216ed352c3f1bdb8b83650f67d0a89fc63

semantic audit:
56527a8c53041ad4ef02bdafe75edb95aa6a95cbe4c9203645b0e469cdd1854e

run.py SHA-256 used in the authoring replay:
d70a34fad75ec47d345621851f5447f681219550e642af6a349f60fec14865a9
```

## Replay

```bash
python3 -B experiments/X-9604-negative-plus-contracting-blocks/run.py \
  --check-results \
  experiments/X-9604-negative-plus-contracting-blocks/results/canonical.json
```

The authoring replay completed in about 25 seconds with exact Python integers. Resource figures are informational only.

## Boundary

- The negative block is fixed to `(1,2)`.
- Only one contracting block type is repeated after it.
- The contracting-block library is finite.
- Three-type and scale-dependent grammars remain open.
- No counterexample is claimed.
