# X-8502 — Exact complement-quotient audit

**Status:** `EMPIRICAL / EXACT FINITE INTERFACE AUDIT`  
**Issue:** `#43`  
**Claims checked:** `L-8503`, `T-8504`

## Research question

Does the complement identity

\[
M(N-c)=N(M-r)+1
\]

turn every local phase-`-34` connector into one exact ordinary quotient coordinate, and does the resulting deterministic partial map satisfy the claimed growth bound?

## Replay

```bash
python3 -B derive.py \
  --output results/canonical.json \
  --summary results/summary.txt

python3 -B verify.py \
  --check-results results/canonical.json
```

## Frozen derivation

```text
exact complement identities: 120
identity digest:
0324baf8aa4711c72516d407548f44b8e3916e84f1aed94f06f8e451f8df10ab
canonical pair cases: 96
legal lift cases: 288
doubling-growth cases: 144
unique six-bit type cells: 32
growth certificate: N/Q > 9/4, k>=256 => k_next>=2k
payload digest:
0080f0a52318034e24b97b7c0dc90c9b0539464d575aac2588dd157cccdbe2a8
all exact complement-quotient checks passed
```

## Independent checker

```text
independent complement identities: 48
independent canonical pair cases: 48
independent legal lifts: 96
independent growth cases: 64
all independent complement-quotient checks passed
```

`verify.py` does not import `derive.py`. It reconstructs the Bezout pair, source word, target word, next-type residue, and next complement quotient through separately written formulas and uses different heights and lifts.

## Limitations

The experiment does not find or certify a forever-defined quotient. It checks exact finite interfaces only. A modular lasso or long legal prefix remains insufficient for a counterexample.
