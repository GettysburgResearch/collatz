# X-9703 — Exact cap-chain height checks

**Experiment ID:** `X-9703`  
**Status:** `EMPIRICAL / EXACT FINITE CHECK`  
**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Associated claims:** `L-9703`, `T-9704`, `Q-9702`

## Research question

Do the finite arithmetic interfaces behind the cap-chain height collapse replay
exactly?

1. Do the PR #3 exponent formulas give the exact elementary upper and lower
   stage-multiplier bounds used in `T-9704`?
2. For local expanding tiles satisfying
   `-q<C<N` and `N/q>1`, does every finite composite obey
   `|C_composite| < length*N_composite`?
3. On exact artificial cap-correction chains with multiplier greater than 257,
   does the shifted height inequality
   `R_next+257 < Lambda*(R+257)` hold and iterate correctly?

The experiment does not prove that a PR #3 cap-correction chain exists or does
not exist. It checks exact finite theorem interfaces only.

## Files

- `derive.py` — formula-based coefficient audit, exhaustive expanding-tile
  compositions, and deterministic cap paths;
- `verify.py` — independently written checker using different bases, radices,
  composition lengths, and cap paths;
- `results/canonical.json` — frozen exact payload;
- `results/summary.txt` — compact reproducibility summary.

## Commands

From the repository root:

```bash
python3 -B -m py_compile \
  experiments/X-9703-cap-chain-height/derive.py \
  experiments/X-9703-cap-chain-height/verify.py

python3 -B experiments/X-9703-cap-chain-height/derive.py \
  --output experiments/X-9703-cap-chain-height/results/canonical.json \
  --summary experiments/X-9703-cap-chain-height/results/summary.txt

python3 -B experiments/X-9703-cap-chain-height/verify.py \
  --check-results experiments/X-9703-cap-chain-height/results/canonical.json
```

## Frozen derivation results

```text
stage coefficient rows: 25
expanding local tiles: 286
expanding composite chains: 82082
expanding-offset digest: d10277bb12607155787016b103ee9606e85c051d4e45273826d76f752e3c8196
artificial cap paths: 32
artificial cap steps: 224
cap-path digest: fb0dec43c31f26f71777a1c9f8d262f2b85094b7d509ecc63cff24ebe9ea65ac
asymptotic height ratio: 161341/44508739
payload digest: 7131a6e74497002b4edd008deb4c3ff3adf5072b33995b21e88d13bd8f5d30b5
all cap-chain height derivation checks passed
```

## Independent checker

```text
independent expanding chains: 11403
independent expanding digest: 61041190ca494e2d24542be04dd3a395444617683c6313823ac5d3ff94fc6a82
independent cap paths: 27
independent cap steps: 162
independent cap digest: 16d771a442ed8f27e0f67b884ad3f5063ab1723e849bd3b3105d1cc8791077e9
committed payload digest: 7131a6e74497002b4edd008deb4c3ff3adf5072b33995b21e88d13bd8f5d30b5
all independent cap-chain height checks passed
```

## Separation of implementations

The derivation enumerates all singles and pairs in one 286-tile family and
constructs rounded exact macro caps. The checker uses a different tile family,
direct composition formulas, a deterministic slice of length-three systems,
and separately generated cap chains. It does not import `derive.py`.

## Environment

- Python 3 standard library only;
- exact integers and `fractions.Fraction` only;
- no floating-point value or random seed on the critical path.

## Interpretation

The exact checks support the finite arithmetic behind:

```text
|beta_m| < 256 Lambda_m,
R_(m+1)+257 < Lambda_m(R_m+257),
limsup log_2(R_m+257)/D_m <= 161341/44508739 < 1/275.
```

The universal theorem remains mathematical. The final cap-correction existence
question remains open.

## Limitations

- no full PR #3 million-bit stage offset is recomputed;
- no sampled mismatch is promoted to a universal obstruction;
- no p-adic logarithmic-form lower bound is proved;
- no finite marked Collatz initialization is supplied.
