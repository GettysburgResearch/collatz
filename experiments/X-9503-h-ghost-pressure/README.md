# X-9503 — H ghost pressure and first-crossing threshold audit

**Experiment ID:** `X-9503`  
**Agent:** `gpt56-h-01`  
**Issue:** #17  
**Status:** `EMPIRICAL / EXACT FINITE CHECK`  
**Associated claims:** `L-9513`, `L-9514`

## Questions

1. Does the finite H ghost residue set decompose into exact-valuation branches
   and obey the plastic recurrence?
2. Does the exact intermediate-state threshold from `L-9513` fail on a broad
   finite family of first-contracting crossings?

## Command

```bash
python3 -B -m py_compile experiments/X-9503-h-ghost-pressure/run.py
python3 -B experiments/X-9503-h-ghost-pressure/run.py \
  --output experiments/X-9503-h-ghost-pressure/results/summary.json
```

The script uses the Python standard library only.

## Frozen parameters

- ghost precision: `K <= 24`;
- expanding-prefix length: at most `6`;
- prefix letters: `0,...,8`;
- final contracting letter: `0,1,2`.

## Results

The exact ghost residue counts were

```text
1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21,
28, 37, 49, 65, 86, 114, 151, 200, 265, 351, 465, 616.
```

The script checked:

- 21 instances of `N(K)=N(K-2)+N(K-3)`;
- 92 exact branch partitions and valuation labels;
- 22,244 first-contracting extensions;
- 3,511 zero-carry crossings;
- 18,733 positive-carry crossings;
- zero threshold failures.

The smallest observed safety ratio was

\[
\frac{N}{N_u^*(r)}
=
\frac{31922527}{36067}
\approx885.0896,
\]

for the word `(4,0)`, with zero final carry and intermediate state `N=4921`.

Frozen digest:

```text
ab52939e289eb2489f3a9c032d89aed07a649e36c7c1fc0870b76ef54134b578
```

## Limitations

- The recurrence and threshold checks are finite computations, not universal
  proofs.
- The large finite safety margin does not exclude a later near-critical
  counterexample.
- The IFS theorem in `L-9514` is proved separately; this experiment only audits
  its finite residue consequences.
