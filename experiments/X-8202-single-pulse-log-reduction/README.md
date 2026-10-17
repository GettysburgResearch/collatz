# X-8202 — Certified all-repetition single-pulse reduction

**Experiment ID:** `X-8202`  
**Associated claim:** `T-8202`  
**Issue:** #52  
**Agent:** `gpt56-outlier-01`  
**Status:** exact finite certificate for the reduction; `T-8202` remains `PROPOSED / SOURCE-DEPENDENT`

## Research question

Assuming the quoted explicit Matveev lower bound, can every single-pulse perturbation of every repetition of the two known ordinary negative accelerated Collatz cycles be reduced to a finite, exact, independently reconstructible certificate?

## Files

```text
run.py                 author-side generator/checker
verify.py              independent implementation; imports no derivation module
results/canonical.json frozen exact artifact
```

Both programs use only Python arbitrary-precision integers, `fractions.Fraction`, and the standard library.

## Exact objects

The native families are

```text
(A,k,c-values)=(3,2,{5,7}),
(A,k,c-values)=(11,7,{17,25,37,41,55,61,91}).
```

For a repetition `r` and pulse `delta`, integrality requires

```text
D=2^(Ar+delta)-3^(kr) | c(2^delta-1).
```

The scripts certify:

1. the logarithmic proximity forced by this divisibility;
2. the exact quoted Matveev cutoffs;
3. continued fractions of `log_2(9/8)` and `log_2(2187/2048)` through the first denominator past each cutoff;
4. Legendre reduction of every remaining rational approximation;
5. rejection of every positive multiple of all sixteen primitive upper convergents;
6. the exact small cases and the unique trivial `n=1` hit.

## Certified ranges

```text
negative-three-cycle Matveev cutoff:  50,000,000,000
negative-eleven-cycle cutoff:         12,000,000,000
continued-fraction rows:                         35
primitive upper candidates:                      16
```

No loop over either cutoff is performed. The range is represented by exact theorem inequalities and certified continued fractions.

## Commands

```bash
python3 -B -m py_compile \
  experiments/X-8202-single-pulse-log-reduction/run.py \
  experiments/X-8202-single-pulse-log-reduction/verify.py

python3 -B experiments/X-8202-single-pulse-log-reduction/run.py \
  --check-results \
  experiments/X-8202-single-pulse-log-reduction/results/canonical.json

python3 -B experiments/X-8202-single-pulse-log-reduction/verify.py \
  experiments/X-8202-single-pulse-log-reduction/results/canonical.json
```

## Frozen output

```text
certified_continued_fraction_rows:       35
upper_convergent_candidates_rejected:    16
nontrivial_divisibility_hits:             0
trivial_hits:                              1
```

Transcript SHA-256:

```text
3ea78acc77e7d8377c72e2359fa1b190a86eaebdf86b6e7b4afe7fa63c7a10bb
```

The unique hit is

```text
(1,2) -> (2,2), r=1, delta=1, z=-5, n=1.
```

## Exact arithmetic design

The scripts evaluate logarithms using

```text
log(x)=2 sum_(j>=0) z^(2j+1)/(2j+1),
z=(x-1)/(x+1),
```

with an explicit rational tail bound. No floating-point value participates in a proof decision.

The two `alpha` intervals have widths below `2^-574`. Continued-fraction digits are accepted only when both interval endpoints have the same integer part at every reciprocal step.

Huge powers in the final candidate rejection are compared by bit length; they are not materialized.

## Limitations

- The Matveev theorem is external and must be reconstructed independently from the primary paper before `T-8202` can be promoted.
- The experiment covers only the two known negative-cycle baselines.
- It covers one pulse, not arbitrary support size.
- It proves no divergent orbit and constructs no nontrivial positive cycle.
- Agreement of two programs is not independent mathematical review.
