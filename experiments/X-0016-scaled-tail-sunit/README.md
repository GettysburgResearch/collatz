# X-0016 — Scaled-tail telescoping and S-unit applicability audit

Experiment ID: `X-0016`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of the exact finite algebra in `L-0031` and the native applicability interfaces of `T-0032`

## Research questions

1. Do the stabilized phase-34 tower anchors have the exact form
   \[
   64A_i(t)=2^{11(t+1)}p_i,
   \qquad
   64B_i(t)=3^{7(t+1)}p_i+b_i?
   \]
2. Does the scaled connector equation reduce to
   \[
   3^{7(t_j+1)}X_j+b_{i_j}
   =2^{11(t_{j+1}+1)}Y_j?
   \]
3. On actual canonical residual cylinders, does the ordinary scaled tail obey
   \[
   2^{11(t_{j+1}+1)}W_{j+1}
   =3^{7(t_j+1)}W_j+b_{i_j}?
   \]
4. Does finite-chain composition give the positive `{2,3}`-unit toll sum of `L-0031` exactly?
5. Are the corrected-stage exponent formulas and the scale-separating toll-coordinate ratio exact?

## Method

The dependency-free script uses exact Python integers only. It:

- reconstructs all four phase-34 tower types from the original finite-core formulas;
- verifies the stabilized anchor table at padding heights `0`, `16`, and `32`;
- checks
  ```text
  p = (5,30,20,56)
  b = (9,54,36,24)
  ```
  and the factorizations `b_i=2^(alpha_i)3^(beta_i)`;
- constructs four nontrivial ten-tower words at heights `160,176,...,304`;
- computes every canonical connector, residual tile, complete path correction, and cap;
- replays each complete path with three independent ordinary high tails;
- verifies 96 local scaled-tail recurrences;
- verifies the exact finite positive toll formula for every replay;
- checks the corrected 256-stage odd and binary exponent sums for scales `m=12,...,24`;
- verifies that the ratio of the first two toll coordinates distinguishes all tested scales.

The experiment does **not** re-prove the Evertse--Schlickewei--Schmidt theorem used by `T-0032`. It checks the native equation, positivity, fixed term count, and injective scale interface to which that black-box theorem is applied.

## Command

```bash
python3 -m py_compile experiments/X-0016-scaled-tail-sunit/run.py
python3 experiments/X-0016-scaled-tail-sunit/run.py
```

## Expected output

```text
verified stabilized two-prime tower anchors
verified 96 actual scaled-tail connector transitions
verified 256-stage exponents and scale-injective toll ratios
all scaled-tail S-unit checks passed
```

The checked-in output is `results/summary.txt`.

## Interpretation

The connector seed/cap data are not independent arithmetic noise. After the ordinary scaling

\[
W=p_i+64h,
\]

they telescope into one positive toll chosen from

\[
9,54,36,24.
\]

Consequently a fixed 256-symbol source word gives one 257-term positive multiplicative equation. Positivity resolves the proper-subsum problem completely.

The remaining obstruction to an unrestricted S-unit proof is exactly the prime support of the two ordinary endpoint words. `T-0032` turns that obstruction into a theorem: an infinite corrected-stage path must introduce infinitely many fresh primes.

## Limitations

- Finite checks do not prove the imported S-unit finiteness theorem.
- Infinite fresh prime support is necessary, not impossible.
- The real fixed-room convergence in `T-0033` is proved analytically; it is not inferred from this finite audit.
- No cap-stitch tail, marked initialization, or positive-integer counterexample is constructed.
