# X-8260 — Certified all-repetition three-pulse reduction

**Experiment ID:** `X-8260`  
**Associated claim:** `T-8260`  
**Issue:** #52  
**Agent:** `gpt56-sol-04`  
**Status:** exact proved finite computation; the all-repetition conclusion is
`PROPOSED / SOURCE-DEPENDENT`

## Scope

The computation covers exactly three distinct positive valuation pulses, with
arbitrary positive heights, over every repetition and rotation of

```text
P3  = (1,2),
P11 = (1,1,1,2,1,1,4).
```

It extends the two-pulse architecture of `X-8255`.  PR #51's `X-8002` is a
consistency scout only: it scans the minimum denominator-crossing total pulse
and three adjacent totals, so it does not certify arbitrary pulse heights.

## Exact reduction

Rotate a largest of the three cyclic support gaps to the end.  With normalized
support

```text
0 = p1 < p2 < p3 < kr,
```

the largest-gap choice gives

```text
p3 <= floor(2kr/3).
```

After removing a factor coprime to the odd denominator, the exact distributed
pulse correction has decreasing positive weights `w1>w2>w3`:

```text
R = w1(X1-1) + w2 X1(X2-1) + w3 X1 X2(X3-1)
  = -w1 + (w1-w2)X1 + (w2-w3)X1X2 + w3X1X2X3.
```

Writing `t=d1+d2+d3`, `Xi=2^di`, and

```text
D = U^r 2^t - Q^r,
```

gives `0<R<w1 2^t` and therefore, for a divisor hit,

```text
0 < 1-exp(-Lambda)
  < c_* 3^floor(2kr/3) / U^r.
```

The exact rational certificates establish:

```text
Matveev-conditional cutoffs:
  P3:  r < 200,000,000,000
  P11: r <  50,000,000,000

Legendre ranges:
  P3:  r >= 10
  P11: r >= 3

direct transition exclusions:
  P3:  r = 4,...,9
  P11: r = 2
```

Certified continued fractions reject 17 ordinary upper-convergent families.
The sole exceptional row is `1/5`; here `(r,t)=(5m,m)`, and three positive
pulses force `m>=3`.  Its exact first-case margin is

```text
75388584689551 / 281474976710656 > 0,
```

while the left side increases and the right side decreases.  The remaining
finite repetitions are thus `P3: r=2,3` and `P11: r=1`; `P3: r=1` has fewer
than three positions.

## Arbitrary-height finite proof

For each normalized packet, the scripts reconstruct `C-zD=G R`, with
`gcd(G,D)=1`, and all three L-8201 resultants

```text
Ei = U Si Ri^- + Q Ri^+.
```

They verify the Bézout identity, exact `2`-adic valuation, coefficient-norm
bound, and coordinate cap for every coordinate.  Every power-of-two tuple in
the resulting cap box is then enumerated.

Frozen totals:

```text
raw rotation/support configurations:      293
normalized support packets:                45
finite height tuples:                  53,808
resultant identities:                 161,424
continued-fraction rows:                   38
primitive upper families rejected:         18
nontrivial hits:                             0
trivial hits:                                1
```

The sole hit was discovered by the exhaustive computation:

```text
P3, r=3, rotation=0, support=(0,2,4), heights=(1,1,1)
(1,2)^3 -> (2,2,2,2,2,2)
D=3367, R=3367, n=1.
```

It replays valuation by valuation.

## Certificate files

```text
run.py                         author-side generator/checker
verify.py                      independent implementation; imports no run.py
test_run.py                    regression and tamper tests
results/canonical.json         analytic, coverage, cap, and packet records
results/finite-tuples.jsonl.gz one exact record for each of 53,808 tuples
```

The compact tuple rows contain packet/height coordinates, `D`, and the
remainders of `R,E1,E2,E3`, plus the reconstructed start for a hit.  The
independent verifier regenerates every row and checks both compressed and
uncompressed digests.

```text
tuple certificate SHA-256 (uncompressed):
434114f43e00f3de35946581dd3984dc3cfff9484d111fab4422e44a10587ae4

master transcript SHA-256:
3ecc48c9b33c99f9395cb61e28fed61ad9cd8f5ed48b3eac246a97cc1f7655cc
```

## Replay

```bash
python3 -B -m py_compile \
  experiments/X-8260-three-pulse-repetitions/run.py \
  experiments/X-8260-three-pulse-repetitions/verify.py \
  experiments/X-8260-three-pulse-repetitions/test_run.py

python3 -B experiments/X-8260-three-pulse-repetitions/run.py \
  --check-results \
  experiments/X-8260-three-pulse-repetitions/results/canonical.json

python3 -B experiments/X-8260-three-pulse-repetitions/verify.py \
  experiments/X-8260-three-pulse-repetitions/results/canonical.json

python3 -B -m unittest \
  experiments/X-8260-three-pulse-repetitions/test_run.py
```

## Source boundary

The scripts independently certify the finite computation and every native
inequality after the quoted logarithmic-form lower bound.  They do not
reconstruct Matveev's theorem from the primary paper.  Consequently the finite
result is unconditional, but the claim over all repetitions remains explicitly
source-dependent.
