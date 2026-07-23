# X-8203 — Canonical absorption and affine-run value audit

**Agent:** `gpt56-refund-01`  
**Date:** 2026-07-23  
**Status:** exact finite/interface audit

## Frozen sources

```text
PR #49  210b1e204aa82947bab086b020bf2bd53805d84e
PR #51  c7f1c75d0a71a63b32ef3e23306c23f1d0a60bfa
external  Amou–Matala-aho–Väänänen 2007, Theorem 5.1
          DOI 10.4064/aa127-4-2
```

## Questions

1. Do PR #49's canonical-run and permanent-refund constants replay exactly?
2. Do its generated-stack comparison constants replay exactly?
3. Does an affine run schedule reduce to one scalar Tschakaloff value with the claimed parameters?
4. Does the primary-source height parameter remain independent of the affine slope?

## Results

Exact PR #49 arithmetic:

```text
471-canonical contradiction: 124585 > 0
234-canonical contradiction:    593 > 0
absorption threshold:          t=5632
q(5632):                       2
288-depth margin:              84263/63840
233-depth margin:              27453/36102185
```

For every tested affine schedule

```text
r_n=R+d*n,
0<=R<=8,
1<=d<=5,
```

the independently derived finite prefix is exactly

```text
v_0
 =-sum_(j<N) 2^A_j/9^B_(j+1)
  +(2^A_N/9^B_N) v_N,
```

and the infinite selected value has normalization

```text
v_0=-9^(-(R+1))*F_q(z),
q=(8/9)^d,
z=2^(3R+3d+4)/9^(R+d+1).
```

The source parameter is

```text
lambda=-(2/3)log_2(3),
```

independent of `d`. The exact hypothesis margins are

```text
30^2*2086-1369^2 = 3239 > 0,
2^8-3^5          =   13 > 0.
```

The source theorem itself is not computationally proved here; its statement and parameter mapping are in `R-8202`.

## Coverage

```text
affine schedules:               45
coefficient/ratio checks:     1,755
backward finite identities:     225
functional coefficient checks:  900
```

## Replay

```bash
python3 -B experiments/X-8203-absorption-affine-run/run.py \
  --output /tmp/X-8203.json \
  --check-results experiments/X-8203-absorption-affine-run/results/canonical.json

python3 -B experiments/X-8203-absorption-affine-run/verify.py \
  experiments/X-8203-absorption-affine-run/results/canonical.json
```

## Digests

```text
run.py       21f5194aaea770df47b6336221637700574adb3405d8d6ebb39ad7d033c93b32
verify.py    0e219582730f9cdeb10928bb44156489652673958ee82ce4df5a297940587881
canonical    c063994c758ccd54c9d841772c52159f08aeeacc5578f824c3aa8104c66fbfbe
semantic     f21d9538600020fbc330e3413f9bbbd09351d8574e523e05d508cec0b2f3fff7
```

## Limitations

- Finite identities corroborate the exact normalization; irrationality uses the cited primary-source theorem.
- The exclusion applies to eventually affine positive-slope schedules, not nonlinear/adaptive schedules.
- No ordinary counterexample is constructed.
