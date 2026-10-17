# X-8001 — negative-cycle two-pulse scan

This exact standard-library experiment accompanies `L-8001`.

It performs:

1. an all-positive-pulse-size scan using the two determinant caps for
   - `(1,2)^r`, `1<=r<=50`;
   - `(1,1,1,2,1,1,4)^r`, `1<=r<=20`;
2. a long near-threshold scan through `r=5000`, at the minimal total pulse
   crossing `D>0` and the next three totals; and
3. `2,432` independent direct-numerator formula audits on small words.

Frozen result:

```text
all-size reduced candidates:       16,445,391
near-threshold reduced candidates:        168
nontrivial exact cycles:                     0
```

The only hit is the trivial all-`2` word obtained from `(1,2)^2` by pulsing
both `1`s once, with start `n=1`.

```text
results SHA-256:
57b6f1217221142269f3331805f8f479450ed442c8c2e34d075c63f5849ea724
```

Replay:

```bash
python3 -B run.py --check-results results/canonical.json
```
