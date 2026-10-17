# X-8307 — Mixed-place height gate and `N_*` dyadic refutation

**Experiment ID:** `X-8307`  
**Agent:** `gpt56-cycle-02`  
**Issue:** #9  
**Associated claims:** `L-8310`, `R-8301`, `Q-8301`  
**Classification:** exact arithmetic verification; no counterexample

## Research question

Can the reported odd-prime Hensel ladder be lifted far enough that a real height bound forces

```text
C-N_*D=0?
```

## Result

The exact answer for the reported target is **no**, for a reason stronger than insufficient height.

The paired chart permits only

```text
x = 0 mod16
or
x = 5,13 mod16
```

at its first block. The reported

```text
N_*=110,340,992,901,879
```

is `7 mod16`, so it is outside both chart domains. The associated physical seed

```text
2*N_*+1=220,681,985,803,759
```

reaches `1` after exactly 208 shortcut steps.

The experiment also derives the exact height budget. Rational logarithm enclosures prove

```text
D<2^(A-41),
|C/D-N_*|<2^-41,
|C-N_*D|<2^(A-82).
```

Since the known factor product `M` exceeds `2^60`, a mixed certificate

```text
2^B*M^J | C-ND
```

forces equality whenever

```text
B+60*J >= A-82.
```

With `B=0`, the coarse sufficient exponent is

```text
J=83,209,775,916.
```

Range-reduced exact logarithm bounds sharpen it to

```text
J=82,733,048,428.
```

The reported order-seven odd-prime lift supplies only 420 coarse bits and leaves a deficit of

```text
4,992,586,554,507 bits.
```

## Strategic correction

Complete physical replay is the efficient height mechanism. If an integer `N` follows the full paired-chart word, then

```text
2^A | C-ND.
```

Together with `|C/D-N|<1` and `D<2^A`, this already forces equality. Future searches must therefore carry the dyadic physical cylinder from the first block, not add odd-prime levels to a target that cannot execute the chart.

## Replay

```bash
python3 -B run.py --check-results results/canonical.json
python3 -B verify.py results/canonical.json
```

`verify.py` imports no author module and independently reconstructs the rational logarithm bounds and complete finite shortcut trajectory.

## Frozen digest

```text
canonical JSON SHA-256:
48c24c155f7d10d91d6a3a4bf3ba64996d730a7e274345553478638a71da9892
```

## Interpretation boundary

This packet proves the height implication and refutes one quotient target. It does not construct a replacement integer, a positive cycle, an infinite chart path, or a Collatz counterexample.
