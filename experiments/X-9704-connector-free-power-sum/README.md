# X-9704 — Connector-free stage and Evertse-admissibility audit

**Experiment ID:** `X-9704`  
**Status:** `EMPIRICAL / EXACT FINITE CHECK`  
**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Claims audited:** `L-9704`, `L-9705`, `L-9706`, `T-9705` proof interfaces  
**Dependencies:** Python 3 standard library only  
**Randomness:** none

## Purpose

The experiment checks the finite arithmetic interfaces behind the full corrected-stage exclusion theorem without treating computation as proof of Evertse's Subspace-Theorem input.

1. Reconstruct the four stabilized phase-`-34` tower cores from the original recovery congruences.
2. Verify the connector-free coordinate
   ```text
   H_(t_(j+1)) Z_(j+1)=N_(t_j) Z_j+b_(i_j)
   ```
   on every stabilized type triple and signed quotient lift.
3. Verify the direct physical cofactor identity and adjacent gcd restriction.
4. Reconstruct the complete 256-term `{2,3}`-unit power-sum dictionary at two consecutive scales.
5. Exhaust exact small signed quotient continuations and check convergence to quotient `0` or `-1`.
6. Check the primitive gcd cap `216`, the combined endpoint-height gate
   ```text
   6498/346819 < 1/50,
   ```
   and the projective valuation separation used in the Evertse reduction.

## Commands

```bash
python3 -B -m py_compile \
  experiments/X-9704-connector-free-power-sum/derive.py \
  experiments/X-9704-connector-free-power-sum/verify.py

python3 -B experiments/X-9704-connector-free-power-sum/derive.py \
  --output experiments/X-9704-connector-free-power-sum/results/canonical.json \
  --summary experiments/X-9704-connector-free-power-sum/results/summary.txt

python3 -B experiments/X-9704-connector-free-power-sum/verify.py \
  --check-results experiments/X-9704-connector-free-power-sum/results/canonical.json
```

## Frozen result

```text
local coordinate cases: 256
physical cofactor cases: 256
adjacent gcd cases: 256
prime turnover cases: 256
stable dictionary rows: 256
modular stage checks: 4
signed quotient integral cases: 4704
primitive gcd cap: 216
endpoint product ratio: 6498/346819 < 1/50
projective separation rows: 9
payload digest:
f3a4fd8a6f5074c488bd1a0d46a420a3f6f4425aaf30bef8245d5512a995a858
all independent connector-free checks passed
```

## Independence

`verify.py` does not import `derive.py`. It reconstructs the finite cores from recovery congruences, uses independently written connector and exponent loops, repeats the signed quotient exhaustion, and separately checks every numerical gate in the almost-`S`-unit reduction.

## Nonconsequence

The finite audit does not prove Evertse's theorem and does not independently reconstruct every million-bit physical stage. The infinite conclusion is the mathematical argument in `T-9705` using the displayed external theorem.
