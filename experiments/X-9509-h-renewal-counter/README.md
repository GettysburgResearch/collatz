# X-9509 — exact H renewal one-counter and refund-graph audit

**Status:** `INTERNAL EXACT COMPUTATION`; finite search only.

This experiment verifies the exact one-counter normal form for successive
nonzero renewals of the H block map and searches the first finite boxes of its
nondecreasing ("refund") transition graph. It does **not** claim an infinite
ordinary orbit.

## Exact state

A renewal type is

```text
(a,R,b)
```

where `R>=1` is the current nonzero block letter, `a>=1` is the preceding
zero-room length, and `b>=1` is the following zero-room length. The bridge
variables satisfy

```text
3^a X + 1 = 8^R U,
4^b Y + 1 = 9^R U,
X,Y = 5 mod 6,
U = 1 mod 4.
```

For a fixed type there is one canonical arithmetic progression

```text
X = x0 + 3*2^(3R+2b+1) k,   k>=0.
```

The script derives `x0,U0,Y0` exactly.

For a target type `(b,S,c)`, put `q=3S+2c`. The transition domain and update
are

```text
k  = eta + 2^q t,
k' = zeta + 3^(2R+a) t,
t>=0.
```

The script verifies this formula against direct valuation decoding at two tail
values for every transition cylinder in the finite box.

An edge is called a refund edge when

```text
3^(2R+a) >= 2^q,
zeta >= eta.
```

Then every ordinary point in the edge cylinder obeys `k'>=k`.

## Frozen run

The canonical run uses

```bash
python3 run.py --max-type 15 --output results/canonical.json
```

It covers every type and target parameter with

```text
1 <= a,R,b,S,c <= 15.
```

Exact totals:

```text
types:                         3,375
transition cylinders:        759,375
refund edges:                353,835
refund self-loops:                42
zero-increment refund edges:       1
refund SCCs:                       34
largest refund SCC:               594
```

The finite transition Kraft sum is

```text
1798996753703415041853 / 37778931862957161709568,
```

approaching the exact full sum `1/21`.

The longest canonical-root refund chain in this box has four transitions. It
starts at

```text
type = (1,8,7),
k    = 133973,
X    = 220957479840077141,
U    = 39510276289,
Y    = 103807851565277,
p    = 2651489758080925696,
n    = 883829919360308564.
```

Its type/counter chain is

```text
(1,8,7), 133973
 -> (7,4,3), 65999254
 -> (3,2,1), 3699285805175
 -> (1,2,1), 31602883030933
 -> (1,1,2), 59996098254038
 -> undefined.
```

This is an exact rejected construction candidate, not a counterexample.

Semantic digest:

```text
95d98ad1b0b915ec0905235e567779c99a9d971e4ac73f596ef089c25f80697d
```

## Scope boundary

The large refund SCC shows that the positive construction lane is not empty at
the finite-state projection. But a modular SCC or an abstract 2-adic path is
not an ordinary witness. A counterexample requires one explicit finite tuple
`(a,R,b,k)` whose deterministic decoder is proved defined forever.
