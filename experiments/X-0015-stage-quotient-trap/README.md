# X-0015 — Canonical caps and stage-quotient extinction

Experiment ID: `X-0015`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` verification of proposed exact claims `L-0030` and `T-0031`

## Research questions

1. Does the canonical correction of every finite connector chain replay through nonnegative integers?
2. Is its canonical output cap always smaller than three times the complete odd multiplier?
3. Does the corrected stage inequality
   \[
   2^{D_{m+1}}>512\,3^{A_m}
   \]
   hold from the exact exponent formulas?
4. Under these two bounds, is the free stage quotient a strict nonnegative-integer ranking function?
5. Does one complete phase-34 stage satisfy the generic cap theorem at its actual million-bit scale?

## Method

`run.py` uses exact Python integers and the standard library only.

It performs four independent checks.

### Exhaustive small-chain audit

The local corpus consists of every tile

\[
(N,q,C)
\]

with

```text
N in {1,3}
q in {2,4}
-q < C < N.
```

Every chain of length one through four is checked, for a total of

```text
69,904
```

chains. For each chain, the script:

- composes the affine tile exactly;
- computes the canonical correction;
- replays every local division;
- verifies nonnegative intermediate values;
- verifies the final cap bound
  \[
  S<3N.
  \]

### Exhaustive synthetic quotient trap

For odd multipliers `1,3,...,15`, the script chooses the least power of two strictly above `512*N`. It enumerates every cap in `[0,3*N)` and every current quotient residue, constructs the exact next correction, and checks

\[
512Y'<Y+3.
\]

The corpus contains

```text
1,348,608
```

valid synthetic transitions.

### Exact exponent audit

The script checks the integer inequality

\[
3^{41}<2^{65}
\]

and verifies the positive rational numerator in

\[
D_{m+1}-9-\frac{65}{41}A_m
=
\frac{22173699}{5248}2^m-rac{1393}{41}
\]

through `m=64`.

### Full stage reconstruction

Finally, the script reconstructs all 256 local residual connectors of the constant first tower type at scale `m=8`. It uses the incremental cylinder/block recurrence rather than one enormous final modular inverse.

The exact fingerprint is

```text
odd-multiplier bits: 1,092,078
binary modulus depth: 1,088,395
canonical correction bits: 1,088,394
canonical cap bits: 1,092,076
correction low 64 bits: 0x4ec6572007e82554
cap low 64 bits:        0x5b60aa2768a03a3c
```

and the cap satisfies the theorem.

## Command

```bash
python3 -m py_compile experiments/X-0015-stage-quotient-trap/run.py
python3 experiments/X-0015-stage-quotient-trap/run.py
```

## Expected output

```text
verified canonical cap bound on 69904 small chains
verified quotient-trap inequality on 1348608 synthetic transitions
verified exact 512-fold next-modulus gap
verified full m=8 constant-type stage cap: (1092078, 1088395, 1088394, 1092076, '0x4ec6572007e82554', '0x5b60aa2768a03a3c')
all stage-quotient-trap checks passed
```

The checked-in copy is `results/summary.txt`.

## Digests

```text
29a4e03a06b95c8294a798bd58f1d294259736fa3b76ccd49d4f652f129f44b8  run.py
cc4c433c351ac7065800e319421a6fa41523ac11338981ddd81fb6bf3e20f157  results/summary.txt
```

## Interpretation

The experiment supports the new completion-height reduction:

- the canonical stage cap is small relative to the stage multiplier;
- the next stage modulus is vastly larger than that multiplier;
- therefore the quotient above the canonical correction decreases strictly and eventually vanishes;
- every ordinary infinite stage realization must eventually satisfy exact cap-to-correction stitching.

The earlier physical intuition that the free stage quotient might carry the full-stage surplus was incorrect. The raw stage map remains supercritical, but its ordinary completion must move through the canonical corrections rather than through a growing quotient above them.

## Limitations

- The finite checks do not prove that any stitching tail exists or is impossible.
- Only one actual million-bit stage word is reconstructed; type-word universality comes from the theorem, not this sample.
- The experiment does not produce a marked starting integer.
- No counterexample is proposed.
