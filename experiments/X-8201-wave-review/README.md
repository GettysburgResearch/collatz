# X-8201 — Independent review and refund arithmetic

**Agent:** `gpt56-refund-01`  
**Issue:** #43  
**Status:** exact finite corroboration

## Frozen sources

```text
PR #45  5d17926b48e29f94a935f1d433559b0c417cef55
PR #42  94fcd99fe7fb71e0f5a15915ba40e9d74b167a13
PR #34  86fa0aeb35a8b8c3dc405c4507877c3792194608
```

`run.py` imports no repository module. `verify.py` is separately written and does not import `run.py`.

## Coverage

- PR #45 mechanical lower/upper recursion against 6,478 explicitly generated small words;
- exact frozen modulus, 80 sites, 43 swaps, and local-minimum count;
- directed 170-digit real interval, cross-checked by a 240-digit scalar implementation;
- every starting residue through modulus 220 for `T-8601`;
- the exact `3`-power reset through exponent 19;
- refund thresholds through lookahead 32;
- 50,000 exact abstract quotient-growth instances.

## Replay

```bash
python3 -B experiments/X-8201-wave-review/run.py \
  > /tmp/X-8201.json

diff -u \
  experiments/X-8201-wave-review/results/canonical.json \
  /tmp/X-8201.json

python3 -B experiments/X-8201-wave-review/verify.py \
  experiments/X-8201-wave-review/results/canonical.json
```

## Limitations

- The full 802,459,998,516-composition computation behind PR #42 `T-8602` was not rerun.
- Finite modular checks corroborate `T-8601`; the universal proof is mathematical.
- Refund experiments do not construct a coherent infinite ordinary path.
