# H frontier — iteration 12

**Agent:** `gpt56-h-01`  
**Issue:** #17  
**PR:** #19  
**Status:** research checkpoint; no counterexample or termination proof claimed

## External repository inspiration

The immediate model was PR #49's intrinsic primitive-core decoder.  Its key
lesson is that a constructive counterexample should be recoverable from one
ordinary integer, with no trusted future word, carry tape, or auxiliary type
metadata.  The rational-base literature packet in PR #13 reinforces the same
boundary: an exact unbounded root state is mathematical data, not implementation
noise.

Iteration 11 reduced H to a finite renewal type plus one ordinary counter.  The
present iteration removes even that redundancy.

## Exact intrinsic renewal map

At a nonzero renewal, put

```text
Z=(p-4)/4.
```

The single positive integer `Z` forces:

```text
a=v_3(Z),              X=Z/3^a,
R=v_2(Z+1)/3,          U=(Z+1)/8^R,
b=v_2(9^R U-1)/2,     Y=(9^R U-1)/4^b.
```

The domain tests are exactly

```text
a,R,b >= 1,
X=5 mod 6,
U=1 mod 4,
Y=5 mod 6.
```

The next renewal is

```text
Rcal(Z)=3^b Y.
```

The physical H seed is reconstructed by

```text
p=4(Z+1),
n=4Z/3.
```

Thus a positive H counterexample is now exactly one positive integer `Z_0`
whose intrinsic decoder remains defined forever.

## Exact predecessor

Writing `Z=3^a X`, the unique possible renewal predecessor is obtained from

```text
T=4^a X+1.
```

It exists precisely when `v_3(T)=2R_-` is a positive even valuation and

```text
U_-=T/9^R_-,
Z_-=8^R_- U_- -1
```

has positive ternary valuation and residual core `5 mod 6`.  In that case
`Rcal(Z_-)=Z` exactly.

This yields a source gate for a least nonperiodic survivor: its first forward
renewal is expanding, but its possible predecessor is absent or nonexpanding.

## Exact finite audit

`X-9510` checks all

```text
1 <= a,R,b <= 18,
0 <= k <= 127,
```

for 746,496 type/counter states.  It verifies the intrinsic/type-coordinate
crosswalk, every predecessor round trip, and agreement of the two next-renewal
decoders.

Frozen results:

```text
states:                              746496
defined next renewals:                35551
states with no predecessor:          699847
states with expanding predecessor:       24
maximum exact renewal life:               5
```

The longest tested chain starts at

```text
(a,R,b,k)=(11,1,16,121),
Z=4423817593825817031,
```

and exits after five renewals.

Semantic digest:

```text
2934e2bbe9fb0291581f22fe6495774eab3db1c88907d96632d2d49ff7134af2
```

## Current positive atom

The counterexample objective is now fully intrinsic:

```text
find Z_0>0 and an ordinary inductive invariant proving that
Rcal^j(Z_0) is defined for every j>=0.
```

No future itinerary, completed 2-adic address, or trusted type sequence is part
of the certificate.  A solution gives

```text
n_0=4Z_0/3,
N_0=8n_0+1,
```

and therefore an unconditional H and shortcut-Collatz counterexample.

The finite audit did not find such a `Z_0`.  Its role is to validate the new
coordinate and sharpen the source-focused search, not to extrapolate an
infinite conclusion.
