# X-8702 — Independent arithmetic audit of PR #33

**Experiment ID:** `X-8702`  
**Agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Status:** `EMPIRICAL` exact-interface audit  
**Frozen PR #33:** `c9d62bce3e93f5785f72e4520bc576863d9379eb`  
**Frozen PR #3 interface:** `f274dfeee3c9c391c48e58d8b57cb9f1759236f8`

## Purpose

Reconstruct the finite arithmetic used by PR #33's proposed universal exclusion of the frozen corrected 256-stage class, without importing author code.

The scripts check:

- stabilized tower anchors and canonical mixed-radix connectors;
- the connector-free coordinate identity;
- stage exponent sums and fixed monomial dictionary;
- signed quotient contraction to cap/co-cap alternatives;
- cap and combined endpoint height ratios;
- primitive gcd cap `216`;
- disjoint projective 2-adic valuation intervals.

The external Evertse Corollary is not executed by code. Its hypotheses and conclusion are reconstructed mathematically in the permanent review report.

## Frozen result

```text
actual connector cases: 32
local conjugacy cases: 16
signed exact continuations: 20,000
primitive core rows: 64
cap ratio: 161341/44508739 < 1/275
endpoint ratio: 6498/346819 < 1/50
Evertse data: n=257, c=1, d=1/50, S0={2,3}
```

## Replay

```bash
python3 -B experiments/X-8702-pr33-evertse-audit/run.py \
  --output /tmp/X-8702.json \
  --check-results experiments/X-8702-pr33-evertse-audit/results/canonical.json

python3 -B experiments/X-8702-pr33-evertse-audit/verify.py \
  experiments/X-8702-pr33-evertse-audit/results/canonical.json
```

## Limitations

- The scripts do not prove Evertse's theorem.
- The infinite exclusion follows from the mathematical application, not finite sampling.
- The result concerns the frozen corrected-stage class only and is not a proof of Collatz.
