# Fixed-height forward power-saving attack

**Date:** 2026-09-03  
**Agent:** `gpt56-fixed-height-01` (`GPT-5.6 Pro`)  
**Base:** `agent/mazur-2026-collatz-import` at `a9abe3509fddc12e22ffa8c559b44fc35adfdb48`  
**Requested target:** prove fixed-height `#B_H^G(X;C)=O_H(X^beta)` with `beta<0.901` for the Syracuse or one-division normalization, and push the result  
**Verdict:** `GAP/BLOCKED` for the requested fixed-height theorem; five narrower results and one executable checker are pushed for review.

## What was proved

1. **`MZ-FH-001`** — an exact one-horizon bound
   \[
   \#\{n\le X:T^k(n)\ge n\ (k\le\lfloor\log_2X\rfloor)\}
   \le6499+2X^{19/20}.
   \]
2. **`MZ-FH-002`** — the binary exponential rate of the corresponding dyadic no-descent kernel is exactly
   \[
   h_2(\log2/\log3)=0.9499555271\ldots.
   \]
3. **`MZ-FH-003`** — a generic repeated power-descent pullback loses the density exponent by `D -> rD`; after the variable number of scales needed to reach fixed height, the saving is no longer a fixed power of `X`.
4. **`MZ-FH-004`** — a uniform positive all-subset fiber gain is impossible by mass conservation; the needed transfer gain must be correlated with the killed survivor set or use cancellation.
5. **`MZ-FH-005`** — a physical descent map with local saving `D` and killed-set decorrelation gain `delta` gives every exponent
   \[
   \beta>\max\{1-D,1-\delta/(1-r)\}.
   \]

## First unsupported inference in the requested proof

The source theorems do not supply a killed transfer estimate

\[
\#\{n\le X:n\notin E_X,\ F_X(n)\in S_H(X^r)\}
\ll_H X^{1-r-\delta}\#S_H(X^r)
\]

with any `delta>0`, where `S_H(X^r)` is the lower-scale set surviving above the same fixed floor for the remaining recursive clock. Their natural/harmonic transport controls full-source passage laws with logarithmic error; it does not prove a power gain after conditioning on this sparse dynamic set.

A superficially stronger estimate for every endpoint subset is impossible: taking the complete image contradicts conservation of the `X-o(X)` source mass.

Without killed-set decorrelation, iteration reaches only a fixed-height density coefficient. It does not retain `X^beta`, `beta<1`.

## Why the one-horizon result cannot close the imported bridge

The exact one-division bound has endpoint exponent `19/20`, and its asymptotic parity entropy ceiling is approximately `0.949955`. It does not itself give fixed-power scale reduction. More strongly, for every one-horizon reduction exponent `r<h_2(log 2/log 3)`, coefficient-supercritical roots force local exceptional saving at most `0.050044...`. The imported inverse exponent requires a forward saving strictly greater than `0.099`.

Thus a successful continuation must either:

- use more than one native parity horizon with non-generic killed transfer;
- handle the no-descent kernel instead of discarding it;
- improve the inverse exponent toward one; or
- prove a joint operator inequality that avoids the maximum of two separate losses.

## Checks actually run

```text
python research/external/mazur-2026/check_fixed_height_attack.py
```

The checker uses exact integer arithmetic for the two exponent enclosures, exhausts parity words and canonical roots through depth 16, checks the cyclic-minimum construction at those depths, and verifies the finite theorem at dyadic cutoffs through `2^16`.

## Evidence not produced

- no proof of killed-set decorrelation;
- no fixed-height exponent `beta<1`;
- no full Lean formalization;
- no replay of the two imported external Lean packages or large predecessor payloads;
- no proof of `SC*`, `FC*`, or Collatz.

## Review order

1. `research/external/mazur-2026/fixed-height-forward-power-saving.md`
2. `research/external/mazur-2026/check_fixed_height_attack.py`
3. `research/external/mazur-2026/fixed-height-check-report.json`
4. `research/external/mazur-2026/CLAIM_MATRIX.md`
5. this report

## Next exact offense

Build a killed source-to-endpoint operator for one power-descent stage and prove a gain beyond the generic fiber scale on the recursively surviving endpoint family. A useful first certificate need not cross `0.901`; it must demonstrate one rigorously positive `delta` while preserving one physical source and a fixed-floor survivor predicate.
