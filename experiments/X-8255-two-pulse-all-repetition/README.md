# X-8255 — Certified all-repetition two-pulse reduction

**Experiment ID:** `X-8255`  
**Associated claim:** `T-8255`  
**Issue:** #52  
**Agent:** `gpt56-outlier-01`  
**Status:** exact finite certificate for the reduction; `T-8255` remains `PROPOSED / SOURCE-DEPENDENT`

## Research question

Assuming the quoted explicit two-logarithm Matveev bound, can every two-pulse perturbation of every repetition and rotation of the two known ordinary negative accelerated Collatz cycles be reduced to a finite exact certificate?

## Files

```text
run.py                 author-side generator/checker
verify.py              independent implementation; imports no author module
results/canonical.json frozen exact artifact
```

Both programs use only Python arbitrary-precision integers, `fractions.Fraction`, and the standard library.

## Infinite families covered

```text
primitive baselines:
  (1,2),
  (1,1,1,2,1,1,4);

repetition:
  every r>=1;

geometry:
  every primitive rotation,
  every pair of distinct pulse positions up to cyclic rotation;

pulse heights:
  every d_1,d_2>=1.
```

The analytic certificate is uniform in the pulse gap, rotation, and height split.

## Exact reduction

For total pulse height `t=d_1+d_2`, integrality gives a reduced divisor condition with

```text
D=U^r 2^t-Q^r,
0<R<alpha_gap 2^t,
alpha_gap<=c_* 3^floor(k r/2).
```

Consequently

```text
0<Lambda<(2 c_* 3^floor(k r/2))/U^r,
Lambda=(t-r log_2(Q/U))log(2).
```

The scripts certify:

1. explicit Matveev cutoffs;
2. exact Legendre thresholds;
3. continued fractions through the first denominator beyond each cutoff;
4. rejection of every positive multiple of 17 primitive upper convergents;
5. exact rejection of the exceptional `1/5` family;
6. complete all-size eliminant scans in the remaining small repetitions;
7. physical replay of the unique trivial hit.

## Certified cutoffs

```text
negative-three cycle:   r < 100,000,000,000
negative-eleven cycle:  r <  25,000,000,000
```

No loop over either cutoff occurs.

## Frozen output

```text
continued_fraction_rows:              38
primitive_upper_rows_rejected:        18
nontrivial_hits:                        0
trivial_hits:                           1
```

Small exact audit:

```text
P3, r<=5:
  packets:                         30
  positive-denominator pairs:    609
  eliminant identities:        1,218

P11, r=1:
  packets:                         21
  positive-denominator pairs:    289
  eliminant identities:          578
```

Unique hit:

```text
(1,2,1,2) -> (2,2,2,2),
n=1.
```

Master SHA-256:

```text
b60b6c1e4564ac52a52749af8e19f854fb0f3de0c0a6269037e3f452b91278a8
```

## Replay

```bash
python3 -B -m py_compile \
  experiments/X-8255-two-pulse-all-repetition/run.py \
  experiments/X-8255-two-pulse-all-repetition/verify.py

python3 -B experiments/X-8255-two-pulse-all-repetition/run.py \
  --check-results \
  experiments/X-8255-two-pulse-all-repetition/results/canonical.json

python3 -B experiments/X-8255-two-pulse-all-repetition/verify.py \
  experiments/X-8255-two-pulse-all-repetition/results/canonical.json
```

## Source boundary

The Matveev theorem is an external black box and must be reconstructed from the primary paper before `T-8255` can be promoted. Every native inequality and every finite consequence after the quoted lower bound is checked exactly by both programs.

## Limitations

- exactly two pulse locations only;
- only the two known negative-cycle baselines;
- no mixed macro-block architectures;
- no divergent-orbit construction;
- agreement of two programs is not independent mathematical review.
