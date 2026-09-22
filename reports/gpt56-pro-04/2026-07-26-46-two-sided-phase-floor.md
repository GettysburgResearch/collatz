# Continuation report — two-sided phase floors close fixed-weight pulse cycles through `a=243`

**Agent:** `gpt56-pro-04` (`GPT-5.6 Pro`)  
**Date:** 2026-07-26  
**Branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`  
**Issue:** #46  
**Status:** proposed theorem packet; no counterexample or `K-####` object

## 1. Live-branch reconciliation

While this packet was being derived, the branch advanced from `T-9608` to `L-9610/T-9609`, closing every fixed-weight packet through thirteen `A` letters by terminal residues and exact exceptional congruences.

I preserved that work and moved the new result to fresh IDs:

```text
L-9611  two-sided boundary phase floor
T-9610  fixed-weight cycle exclusion through a=243
X-9614  exact phase and parameter certificate.
```

No existing file or claim ID is overwritten.

## 2. New global mechanism

In the exact coordinate `n=6z+1`,

```text
A: 8z'  = 9z+1,
B: 16z' = 9z.
```

A length-`d` word imposes both:

```text
one source residue modulo its dyadic divisor;
one output residue modulo 9^d.
```

At a macro boundary, the final `d` letters of the previous macro determine the output residue, while the first `d` letters of the next determine the source residue. CRT produces one exact ordinary class. The least positive representative over all suffix-prefix pairs is a universal boundary floor `H_d`.

This is the all-depth extension of `L-9610`'s terminal residue: the one-letter terminal phase becomes a complete past/future boundary address.

## 3. Exact phase floors

The independently reconstructed tables give

```text
H_5  =            26,873,855
H_8  =       195,221,131,263
H_10 =    90,608,969,363,967.
```

The load-bearing depth-ten minimizer is

```text
past suffix   ABBAAAAABB
future prefix AAABAAAAAA.
```

The depth-ten table has exactly

```text
4^10 = 1,048,576
```

ordered suffix-prefix pairs. This is a phase certificate, not a cycle-period or orbit-prefix scan.

## 4. Cycle-minimum bridge

For a contracting fixed-weight macro alphabet,

```text
Q=8^a16^b,
P=9^(a+b),
D=Q-P,
e_max=16^b(9^a-8^a).
```

At a minimum boundary `m`, the next boundary `m+k` satisfies

```text
e_w = Dm+Qk = D(m+k)+Pk,
```

hence

```text
m+k <= e_max/D.
```

If the macro has at least `d` physical letters, the same boundary is at least `H_d`. Therefore

```text
e_max < H_d D
```

excludes every possible cycle over the complete macro alphabet, at arbitrary repetition length.

## 5. Exact parameter closure

`T-9609` supplies the range `a<=13`. For `14<=a<=243`, every macro has at least ten letters.

The ratio

```text
U(a,b)=e_max/D
      =((9/8)^a-1)/(1-(9/8)^a(9/16)^b)
```

decreases with `b` and increases with `a` while `b` is fixed. It is enough to check the least contracting `b=b_0(a)` and one endpoint per constant-`b_0` interval.

`X-9614` certifies:

```text
230 exact parameter rows;
48 monotone endpoint rows;
positive margin through a=243;
first failure of this depth-ten inequality at a=244,b_0=50.
```

Thus every aligned fixed-weight negative-three pulse grammar with `a<=243` is cycle-free, uniformly in `b`, branch choice, and repetition length.

## 6. Verification

```text
X-9614 canonical results match
all independent X-9614 two-sided phase checks passed
```

Digests:

```text
phase pairs d=5:
f3f9b63a193b89327197132feb2495170ec58af3a1bfda038b5206e82847d4fd

phase pairs d=8:
ad0dbcdc9608e3c4e699577ca3bc64760749e1dcd5b55f79a1fa485a6ecaf8f1

phase pairs d=10:
f8dcff96cee68f12563e0fe21876b693dfd20e97d571c9d3760427c99abfa5af

parameter rows:
b0116cde3b111814d35433b4478f524f3e84331edc538b25851c4ec349116390

semantic payload:
296074c8e5f59c11bc1de1c7d0d89084ae79012381ff1d850fb611281fe0cf06
```

## 7. Honest frontier

This is a genuine infinite-class cycle theorem, but it is not an unconditional Collatz counterexample.

The exact next fixed-weight layer is `a=244`. A deeper phase floor may close it. The higher-value theoretical objective is now a parameter-uniform growth theorem for `H_d`; that could eliminate every fixed-weight packet at once.

The separate positive ordinary blocker remains the six-branch least-root decision.
