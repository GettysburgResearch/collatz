# X-9504 — H ordinary-section finite minimum

**Experiment ID:** `X-9504`  
**Agent:** `gpt56-h-01`  
**Issue:** #17  
**Status:** `EMPIRICAL / EXACT FINITE CHECK`  
**Associated claims:** `L-9516`, `T-9510`, `Q-9506`

## Research question

For each binary precision `K`, what is the least positive ordinary integer

```text
P >= 16,  P == 1 mod 3
```

whose residue modulo `2^K` lies in the H ghost closure?

The resulting monotone minimum `nu_K` diverges if and only if there is no
positive infinite exact H orbit. A finite checkpoint does not prove divergence.

## Replay

The default run stops at precision 40. The frozen result uses precision 50:

```bash
python3 -B -m py_compile \
  experiments/X-9504-h-ordinary-section-minimum/run.py

python3 -B experiments/X-9504-h-ordinary-section-minimum/run.py \
  --min-precision 3 \
  --max-precision 50 \
  --output experiments/X-9504-h-ordinary-section-minimum/results/canonical.json
```

The program uses exact Python integers and the standard library only.

## Frozen result

At precision 50, the full ghost residue set has

```text
922111
```

classes, and

```text
nu_50 = 10205790208.
```

One decoded visible prefix for the minimizing residue is

```text
(6,1,0,1,0,0,1,0).
```

The sequence has finite plateaus; it is monotone but not strictly increasing at
every precision. Selected checkpoints are:

```text
K=16   nu_K=9472
K=24   nu_K=25888
K=32   nu_K=1864132
K=40   nu_K=78198100
K=48   nu_K=9310162948
K=50   nu_K=10205790208
```

Frozen digest over all records from precision 3 through 50:

```text
2e6a51a8c9707d876ef35200baaa9554bfce619abf416fb27946638a52820280
```

## Limitations

- The computation is finite and does not prove `nu_K -> infinity`.
- Residue `0` belongs to the compact ghost closure and can minimize at low
  precision; it cannot represent a fixed positive ordinary survivor at every
  precision.
- The decoded word records only the branch path visible at the specified
  precision.
- The result does not use or prove contracting-cylinder descent.
