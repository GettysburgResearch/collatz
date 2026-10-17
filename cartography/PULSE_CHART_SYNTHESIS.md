# Negative-three ordinary chart — full run core and divisible-seven subchart

**Agent:** `gpt56-cartographer-01`  
**Source:** PR #51 at `9c0753db8543a99247ed55beefbce75ca8f2b507`  
**Classification:** cartography synthesis from exact proposed source interfaces; source claims retain their native status  
**Full-objective role:** one positive all-time chart path is an unconditional Collatz counterexample

## Pass-5 scope correction

Pass 4 derived the correct fixed map

```text
x -> 9x/8        if x=0 mod8,
x -> (9x+1)/16  if x=7 mod16,
n=42x-5.
```

The derivation remains valid. The new PR #51 state shows that it is not the whole negative-three chart: it is the invariant divisible-seven section of the larger ordinary chart below.

## 1. Full ordinary block chart

The negative-three-cycle chart is

```text
A: z=8q    -> 9q,
B: z=1+16q -> 1+9q,
physical n=6z-5.
```

Each legal edge replays an exact accelerated Collatz block. The fixed `z=1` is the trivial physical state `n=1`. Any other positive ordinary path defined forever is therefore a complete counterexample: a repeat gives a nontrivial cycle; a nonrepeating positive integer path is unbounded.

## 2. Divisible-seven invariant subchart

Put

```text
z=7x.
```

For edge `A`, `7x=8q` forces `x=8s`, giving `x -> 9s`. For edge `B`, `7x=1+16q` forces `x=7+16s`, giving `x ->4+9s`. Hence

```text
G(x)=9x/8        if x=0 mod8,
G(x)=(9x+1)/16  if x=7 mod16,
undefined       otherwise,
n=42x-5.
```

The trivial cycle is absent from positive integral `x`. The pass-4 exhaustive cylinder frontier through depth 31 remains an exact finite result for this subchart:

```text
least x surviving 31 blocks:
24643395416689283212736

physical n:
1035022607500949894934907
```

It exits on the next block. This is finite evidence only.

## 3. Full maximal-run quotient

The stronger chart groups a maximal run of `A` edges followed by one `B`. Immediately after a `B` edge, write

```text
z=2^(3r)u,
u odd,
9^r u=1 mod16.
```

The macro `A^r B` is

```text
z_next=(9^(r+1)u+7)/16.
```

For each ordered run pair `(r,s)`, exact valuation and legality of the next `B` edge place `u` in one residue class modulo

```text
2^(8+3s).
```

Writing

```text
u=a_(r,s)+2^(8+3s)k
```

leaves one ordinary quotient. A third run `t` imposes one changing-modulus condition on `k`, and the successor quotient is affine in the free lift.

Thus `(r,s,k)` is a deterministic ordinary state. The future run label is an output of the current quotient, not preloaded control.

## 4. Run-five highway

The exact macro difference is

```text
16(z_next-z)
 =(9^(r+1)-2^(4+3r))u+7.
```

For `r<=4`, the macro decreases except for the trivial fixed state. For every `r>=5`, it strictly increases, using

```text
9^6>2^19.
```

Therefore one explicit finite state `(r_0,r_1,k_0)` whose deterministic run decoder is defined forever and emits only runs at least five gives an unconditional positive unbounded Collatz orbit. This is `ACL-P042`.

## 5. Reset highways are finite controls, not witnesses

For every positive `m=0 mod6`,

```text
z_m=(2^(m+4)-7)/9
```

is an ordinary integer with exact prefix

```text
z_m --B--> 2^m --A^(m/3)--> 9^(m/3).
```

These seeds prove unbounded finite survival depth by a closed formula. They do not prove one infinite path; the post-tail state must still re-enter the changing exact cylinders forever.

## 6. Relation to H and the common refund form

The divisible-seven subchart grouped between `B` edges yields the toll-one renewal

```text
p_next=[3^(2r+2)/2^(3r+4)]p+1,
p=16x.
```

The full run-core quotient and H iteration 11 now both have the affine cylinder form

```text
q=rho+2^E ell -> q'=sigma+3^G ell.
```

The shared missing theorem is ordinary top-boundary recurrence, not finite compatibility or drift.

## Atomic decisions

Positive:

```text
find one explicit full-chart quotient state
whose deterministic decoder is defined forever
and eventually emits only runs r>=5.
```

Negative:

```text
prove every ordinary quotient eventually fails,
or prove every infinite compatible completion is nonordinary.
```

A modular lasso, arbitrary-depth run word, reset family, or isolated `2`-adic point is not a witness.
