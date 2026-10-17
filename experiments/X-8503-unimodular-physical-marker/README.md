# X-8503 — Unimodular physical marker and prime-turnover audit

**Agent:** `gpt56-cylinder-01`  
**Issue:** #43  
**Claims:** `L-8504`, `T-8505`  
**Status:** exact finite interface audit; not an infinite proof

## Questions

1. Does the complement pair form an exact `SL_2(Z)` basis?
2. Does the physical integer intrinsically recover height and type?
3. Does every exact local connector satisfy the predicted valuation jump?
4. Does every adjacent boundary gcd divide the `{2,3}`-unit toll?
5. Are the four boundary residues incompatible with `{2,3}`-smooth words?
6. Is the projective 2-adic ratio sufficient to separate stage scales?

## Implementations

- `derive.py` evaluates full exact connector integers, physical markers, gcds,
  and projective valuations at four large heights.
- `verify.py` is separately written, imports no author module, uses a different
  Bezout parametrization, different lift values, and a different test height.

## Replay

```bash
python3 -B experiments/X-8503-unimodular-physical-marker/derive.py \
  --output experiments/X-8503-unimodular-physical-marker/results/canonical.json \
  --summary experiments/X-8503-unimodular-physical-marker/results/summary.txt

python3 -B experiments/X-8503-unimodular-physical-marker/verify.py \
  experiments/X-8503-unimodular-physical-marker/results/canonical.json
```

## Frozen result

```text
unimodular rows:              4
exact connector cases:        192
intrinsic marker cases:       192
adjacent gcd cases:           192
projective valuation rows:    64
smooth residue obstructions:  4

semantic digest:
320b667d3c82007624e7bb3ccbb3738aa31503afea3718058f9e23613b7940df
```

Independent checker:

```text
exact connector cases:      32
intrinsic marker cases:     32
adjacent gcd cases:         32
smooth residue gates:       4
all independent checks passed
```

## Limitations

The code validates the elementary arithmetic gates only. It does not prove
Evertse's theorem, construct a forever-defined complement counter, or produce a
Collatz counterexample.
