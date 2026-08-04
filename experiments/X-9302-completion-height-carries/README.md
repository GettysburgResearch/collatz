# X-9302 — Exact completion-height carry audit

**Experiment ID:** X-9302  
**Status:** EMPIRICAL / ADVERSARIAL VALIDATION  
**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Associated claims:** `L-9310`, `T-9311`, `T-9312`  
**Date:** 2026-07-21

## Purpose

This experiment replays the raw finite identities used by the new completion-height theorem. It is designed to catch indexing, signed-representative, divisibility, and endpoint errors.

It is **not** a proof of any universal claim and is not a dependency of `L-9310`--`T-9312`.

## Exact state

For each primitive numerator

\[
1\le h\le K^2,
\qquad
64\nmid h,
\]

and each

\[
0\le\ell<K,
\]

the script computes the signed residue

\[
s_\ell
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}}
\]

in

\[
\left(-81^{\ell+1}/2,81^{\ell+1}/2\right].
\]

It then computes

\[
a_\ell
=
\frac{64s_\ell-s_{\ell+1}}{81^{\ell+1}}
\in\mathbb Z
\]

and the exact rational energy

\[
\mathcal E_K(h)
=
\sum_{\ell<K}
\frac{s_\ell^2}{81^{2\ell+2}}.
\]

## Assertions

For every audited numerator, the script checks:

1. every carry is integral;
2. the exact carry-energy inequality
   \[
   \#\{a_\ell\ne0\}
   \le21314\mathcal E_K(h);
   \]
3. every zero-carry run has a nonzero ordinary height numerator;
4. a run beginning at `ell` with length `r` gives divisibility by
   \[
   81^{\ell+r+1};
   \]
5. the exact integer height squeeze
   \[
   2\cdot81^r
   \le
   64^{r+t}+34h;
   \]
6. on the large-run branch `81^r>34h`, the critical inequality
   \[
   81^r<64^{r+t}.
   \]

All arithmetic in these assertions is exact. No floating-point Fourier coefficient is used.

## Command

```bash
python3 experiments/X-9302-completion-height-carries/run.py
```

## Frozen parameters

- depths: `8,12,16,20,24,32,40,48,56,64,72,80`;
- primitive numerators: `1 <= h <= K^2`, excluding multiples of `64`;
- dependencies: Python standard library only;
- replay environment used for the committed output: Python `3.13.5`.

## Frozen output

The committed output is `results/summary.txt`.

The canonical JSON payload internal to the script has SHA-256

```text
1709c4445fef96882653d51e82cae3842e7415ad6f8b288247481f942cd7a7ae
```

## Observations

No asserted identity failed.

Within the bounded polynomial scan, the minimum number of nonzero carries was already close to the full `K-1` transition count. The longest zero-carry run was only `3`, attained in the `K=72` scan.

These empirical values are vastly stronger than the theorem's logarithmic lower bound. They are recorded only as adversarial diagnostics; the proof deliberately uses much weaker exact inequalities.

## Limitations

- Only finite depths through `80` are audited.
- Only the window `h<=K^2` is scanned.
- The observed density of nonzero carries is not claimed universally.
- The script does not prove the right-to-left asymptotic chaining step.
- The script does not verify `T-9308`'s high-frequency entropy tail.
- No ordinary survivor or Collatz trajectory is constructed.
