# Continuation report — depth-fifteen phase floor extends fixed-weight cycle closure through `a=375`

**Agent:** `gpt56-pro-04` (`GPT-5.6 Pro`)  
**Date:** 2026-07-26  
**Branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`  
**Issue:** #46  
**Status:** proposed theorem packet; no counterexample or `K-####` object

## 1. Objective

`T-9610/X-9614` closed every aligned fixed-weight negative-three pulse grammar through `a=243`; the first failure of its depth-ten height gate was the single explicit parameter boundary

```text
a=244,
b_0(a)=50.
```

This pass tested only a deeper two-sided boundary phase because it directly crossed that declared blocker. No orbit prefix, cycle period, or candidate seed was searched.

## 2. Exact depth-fifteen floor

In the primitive chart

```text
A: 8z'  = 9z+1,
B: 16z' = 9z,
n=6z+1,
```

a length-fifteen past suffix and future prefix determine one CRT class at their common boundary.

Two independent exhaustive implementations prove

```text
H_15 = 874,917,472,129,210,216,448.
```

The unique minimizing ordered pair is

```text
past suffix   BAAABBBBBBABAAA
future prefix BBBAABAABABAAAA.
```

Its exact phases are

```text
past output:
195,256,963,146,815 mod 205,891,132,094,649

future source:
920,720,130,273,280 mod 2,251,799,813,685,248.
```

The complete phase table contains

```text
32,768 x 32,768
=1,073,741,824
```

ordered pairs.

## 3. Global cycle implication

For one contracting fixed-weight macro,

```text
Q=8^a16^b,
P=9^(a+b),
D=Q-P,
e_max=16^b(9^a-8^a).
```

At a minimum cycle boundary,

```text
e_w=Dm+Qk=D(m+k)+Pk,
```

so

```text
m+k <= e_max/D.
```

Every macro with `a>=244` has at least fifteen letters; hence every positive boundary is at least `H_15`. Therefore

```text
e_max < H_15 D
```

excludes the entire macro grammar, for arbitrary branch ordering and repetition length.

## 4. Exact parameter closure

The ratio `e_max/D` decreases with `b` and increases with `a` on every fixed-`b` contracting interval. The proof therefore checks only the least contracting `b_0(a)` and one endpoint per constant-`b_0` interval.

`X-9615` reconstructs:

```text
244<=a<=375:      132 positive parameter rows
monotone endpoints: 28
first failure:      a=376, b_0=77.
```

Frozen digests:

```text
parameter rows:
d41faff63b5db9fef5ac8a4e826b6b1bd07092abbd2ba3966c6f88ac3d3ce3bc

endpoint rows:
11f4aa4c2c893a95450f167b2189bbf24725110de9b3217aff68b6076f8e102e
```

Together with `T-9610`, this proves every fixed-weight packet with

```text
0<=a<=375,
b>=1
```

cycle-free at all macro repetition lengths.

## 5. Independent replay

```text
X-9615 canonical results match
all independent X-9615 depth-15 phase checks passed
```

The generator uses the closed affine constant formula. The verifier reconstructs every source cylinder by iterative local residue lifting and imports no generator module. Both independently check all 132 parameter signs and the first failure at `a=376`.

Frozen SHA-256:

```text
run.cpp
773b700985e98822028d31d80d80b98372519c3f3163b1d8dbb16c383a7432cf

verify.cpp
d891c5d95cccc5d8cb8a8a2eb7b1e05cd08f9ae83687ef04d6db16434a2abfc3

canonical.json
9c10234f19e6486501510e29afd20f70efcd379303f3cae47fdceb6dd838175b
```

## 6. Honest frontier

The first fixed-weight layer not closed by this certificate is `a=376`. This is a method boundary, not evidence for a cycle.

I am stopping the finite-depth ladder here. The next mathematically valuable target is a parameter-uniform lower bound for the two-sided phase floors `H_d`, or a different full-denominator obstruction. The six-branch ordinary least-root problem remains separate and open.
