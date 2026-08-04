# X-9301 — Exact cusp-scattering probe

**Experiment ID:** X-9301  
**Status:** EMPIRICAL  
**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Associated claims:** `C-9301`, `L-9303`  
**Date:** 2026-07-21

## Research question

Does the sufficient scattering target `C-9301` fail immediately for polynomial-height numerators? More specifically, for moderate depths `K` and

\[
1\le\theta\le K^2,
\]

how small can the number of levels be at which the normalized signed phase is at least a fixed rational threshold `delta`?

This experiment is designed only to falsify overstrong lemma shapes and identify worst-case carry paths. It is not evidence for an all-depth theorem.

## Exact state

For each `K`, `theta`, and `0 <= t < K`, the program computes the unique signed residue

\[
s_{K,t}(\theta)
\equiv17\theta81^{-(t+1)}
\pmod{64^{K-t}}
\]

in

\[
\left(-64^{K-t}/2,64^{K-t}/2\right].
\]

A level is counted as `delta`-scattered when

\[
|s_{K,t}(\theta)|\ge\delta64^{K-t}.
\]

All comparisons are cross-multiplied integer inequalities. No floating-point Fourier values are computed.

## Command

```bash
python3 experiments/X-9301-cusp-scattering/run.py
```

## Parameters

- depths: `8,12,16,20,24,32,40,48,56,64,72,80`;
- numerator range: `1 <= theta <= K^2`;
- thresholds: `1/146, 1/64, 1/32, 1/16, 1/8`;
- random seeds: none; exhaustive deterministic scan;
- dependencies: Python standard library only;
- replay environment used for the committed output: Python `3.13.5`.

## Output

The frozen output is `results/summary.txt`. The canonical JSON payload internal to the script has SHA-256

```text
61e51931c4d034c5bc5a643c74d48532a2d70fe0fc662a4ff1899d735b21fb83
```

## Empirical observation O-9301

Within the scanned range, the fixed threshold `delta=1/8` has the following minimum scattered counts:

```text
K:       8  12  16  20  24  32  40  48  56  64  72  80
minimum: 4   5   6   9  11  13  20  23  28  33  37  44
```

The weaker threshold `delta=1/146` has minimum counts

```text
7, 10, 14, 17, 22, 28, 36, 44, 51, 56, 66, 74.
```

These finite data are much stronger than the `c log K` count requested by `C-9301`. The minimizing numerators vary substantially with `K` and threshold; no single obvious self-similar exceptional family appears in this small scan.

## Interpretation

The scan suggests two theory priorities:

1. a fixed-threshold scattering theorem is not immediately contradicted even at the relatively demanding threshold `1/8`;
2. the worst numerators should be studied through their exact carry paths, because simple divisibility by one fixed power of `64` or `81` does not explain all argmins.

The data do **not** justify conjecturing a positive-density lower bound. `C-9301` deliberately asks only for logarithmically many scattered positions.

## Limitations

- Only finitely many depths through `80` were scanned.
- Only the polynomial window `theta <= K^2` was tested.
- A sparse exceptional sequence could begin after the scanned range.
- Minimum threshold counts do not directly give the minimum quadratic energy from `L-9303`.
- The experiment does not test the frequency-block or depth-block mean hypotheses.
- No Collatz trajectory or ordinary-integer survivor is constructed.

## Suggested next use

Add an optional mode that emits the complete signed-residue and carry paths for selected argmins, then look for a finite-state or S-unit description. Do not extend the brute-force depth range merely to accumulate more favorable counts; computation should serve a proposed inverse lemma.
