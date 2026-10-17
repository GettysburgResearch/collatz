# X-8308 — Physical depth across ten million critical rotations

**Experiment ID:** `X-8308`  
**Agent:** `gpt56-cycle-02`  
**Issue:** #9  
**Associated claim:** `O-8304`  
**Classification:** exact bounded computation; no counterexample

## Research question

After `R-8301` rejected the reported small quotient target, can the rigorous real floor or ceiling of the repaired critical run word supply a chart-compatible replacement under cyclic rotation?

## Frozen scope

The experiment scans the first

```text
10,000,000 run rotations
58,849,491 chart-symbol rotations
```

of the 65-repair word from `X-8304`.

At every chart rotation it transports an outward-enclosed real interval using fixed-scale integer arithmetic, obtains the unique floor, and tests both the floor and ceiling as ordinary paired-chart starts. Every live start is replayed until its first illegal branch.

## Exact result

Legal first-block starts:

```text
floor: 6,730,343
ceil:  6,729,830
```

The deepest floor and ceiling candidates both survive only eight chart blocks.

### Floor record

```text
run rotation:   4,760,645
chart rotation: 28,016,158
x_0:            1,263,100,502,238,270,197,353,429
physical n_0:   2,526,201,004,476,540,394,706,859
word:           10111110
blocks:         8
dyadic depth B: 26
```

It then fails symbol `1` with terminal residue `3 mod8`.

### Ceiling record

```text
run rotation:   6,595,534
chart rotation: 38,814,386
x_0:            1,185,457,427,807,540,176,328,893
physical n_0:   2,370,914,855,615,080,352,657,787
word:           11011111
blocks:         8
dyadic depth B: 25
```

It then fails symbol `0` with terminal residue `12 mod16`.

The word already supplies one base odd-factor level `M|C-ND`. Thus the largest coarse mixed-place totals in the scanned range are only

```text
floor: B+60J=86
ceil:  B+60J=85
```

versus the `L-8310` requirement

```text
A-82=4,992,586,554,927.
```

## Replay

```bash
python3 -B run.py --check-results results/canonical.json
python3 -B verify.py results/canonical.json
```

The verifier imports no author module and independently reconstructs the full ten-million-run census.

## Frozen digest

```text
canonical JSON SHA-256:
9cd7c752e5e7a553856e11e73a2f47d3b9c0d89aa0cabe3304e5f8a33ed62c64
```

## Interpretation boundary

This is a complete finite rotation census on its declared range. It does not bound later rotations, prove global chart extinction, construct a positive cycle, or produce a divergent seed.
