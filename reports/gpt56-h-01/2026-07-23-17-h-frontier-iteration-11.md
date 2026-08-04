# gpt56-h-01 — issue #17, iteration 11

Date: 2026-07-23

## Objective

Refocus the H program on a positive ordinary counterexample certificate rather
than on completion-level compatibility. The neighboring quotient-refund work
showed the correct target shape: one finite integer state and one deterministic
unbounded counter update proved defined forever.

## Main result

Successive nonzero H renewals admit exactly that shape.

A type is `(a,R,b)`, where `R` is the current nonzero letter and `a,b` are the
adjacent zero-room lengths. Every exact bridge of that type is one arithmetic
progression

```text
X=x_tau+3*2^(3R+2b+1) k,
k>=0.
```

For a target type `(b,S,c)`, the exact transition is

```text
k = eta + 2^(3S+2c) t,
k'= zeta + 3^(2R+a) t.
```

The next type is uniquely recovered by the two exact valuations, so this is a
deterministic partial one-counter map.

A positive infinite H orbit exists exactly when one finite tuple
`(a,R,b,k)` remains in this decoder domain forever. The ordinary initial H
state is reconstructed explicitly from the tuple. This is the strongest
integer-first counterexample interface obtained for H so far.

## Renewal pressure

For a fixed source type, the next-type cylinders are disjoint and have total
relative Haar measure

```text
sum_(S,c>=1) 2^(-3S-2c)=1/21.
```

After conditioning, the tail map has odd slope and is a `Z_2` bijection. Thus
survival for `h` full renewals has exact relative measure `21^(-h)`.

## Refund graph

An edge is nondecreasing for every ordinary tail exactly under the sufficient
criterion

```text
3^(2R+a)>=2^(3S+2c),
zeta>=eta.
```

Then

```text
k'-k=(zeta-eta)+(3^(2R+a)-2^(3S+2c))t>=0.
```

A forever-defined path using refund edges is therefore a direct positive
construction architecture. Unlike the former `10/30` compiler, the bounded
type projection contains substantial positive SCC structure.

## Exact finite audit X-9509

The frozen box `1<=a,R,b,S,c<=15` checked:

```text
types:                       3,375
transition cylinders:      759,375
refund edges:              353,835
refund self-loops:              42
refund SCCs:                     34
largest refund SCC:             594
```

The longest canonical-root refund chain has four steps. It starts from

```text
(a,R,b,k)=(1,8,7,133973)
n=883829919360308564
```

and ends undefined after the exact type/counter path recorded in the canonical
JSON. It is a rejected candidate, not a counterexample.

Digest:

```text
95d98ad1b0b915ec0905235e567779c99a9d971e4ac73f596ef089c25f80697d
```

## Current positive atom

Exhibit one explicit tuple `(a_0,R_0,b_0,k_0)` and an inductive invariant proving
that the deterministic renewal decoder is defined forever. This single object
would prove an infinite positive H orbit and, by the existing `N=8n+1` lift, a
Collatz counterexample.

No such tuple is claimed in this iteration.
