# Demand tree and stationary ghost stages

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Branch:** `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
**Status:** third isolated `94xx` packet; theorem-level claims `PROPOSED`

## Why this packet exists

The first two packets showed that ordinary survivor codes require high factor
complexity, but also showed that a Sturmian stack directive can manufacture
quadratic raw complexity merely by emitting longer zero runs.  Raw word counts
therefore reward padding that may contain no fresh carry information.

This packet switches to the exact regeneration residue itself.  The invariant
is finite-quotient distinguishability per stack stage.

## Demand tree

The exact context demanded by a stage of height `m` is

```text
D(m)=17*81^(-(9m+2))-81^(-1) in Z_2.
```

`L-9405` proves

```text
v_2(D(n)-D(m))=4+v_2(n-m).
```

Therefore `D/16` is an isometry and permutation of `Z_2`.  At base-64 depth
`j`, the demand map is a bijection

```text
m mod 2^(6j-4)
  <->
residues divisible by 16 mod 64^j.
```

Every parent demand has exactly 64 children at the next depth, and the 64
stage lifts realize the 64 possible next digits once each.  This is the
six-bit lift law.

## Stationary matching tree

For a fixed context `x=15 mod 16`, compare the unsteered supply

```text
81^(9m)*(81x+1)
```

with `D(m)`.  `T-9407` proves that their difference, divided by 16, is another
`2`-adic isometry.  Hence:

- one matching stage class exists at every finite depth;
- the first digit keeps one of four stage classes;
- each deeper digit keeps exactly one of 64 lifts;
- the nested classes determine one `2`-adic stage `m_*(x)`.

The inverse matching context is

```text
X(m)
 =17*81^(-(18m+3))
  -81^(-(9m+2))
  -81^(-1).
```

This is a scaled isometry from `Z_2` onto `15+16Z_2`.

For every ordinary stage `m>=0`, however, `X(m)<0` in the real embedding.
Thus a positive ordinary context has arbitrarily deep finite matching stages,
but their compatible limit is not an ordinary nonnegative stage.  It is a
**ghost stage**.

## Residue novelty without padding

For any stage schedule with increments at most `C`, `T-9408` proves that at
depth `j` every

```text
floor((2^(6j-4)-1)/C)+1
```

consecutive demands are distinct.  Under the active `17/18` increment bound,
this gives no-reuse windows of length `15`, `911`, `58,255`, ... at depths
`2`, `3`, `4`, ... .

This count is per stage and ignores how many zeros a stage emits.

## What is closed

- The conditioned stationary agreement histogram is now an exact theorem, not
  a genericity measurement.
- A fixed positive context cannot close at one ordinary stationary stage.
- Compatible finite stationary matches are proved to converge to a nonordinary
  `2`-adic stage.
- Bounded state tables cannot reuse exact demand templates inside the explicit
  exponential windows.

## What remains open

Active steering changes the context after every stage.  The high quotient may
transport the next demanded lift.  The next target is the exact transition on

```text
(current context,
 current stage,
 demanded lift digit,
 high quotient,
 next stage).
```

A successful obstruction would show that the high quotient merely transports
preloaded inverse-limit data; a successful construction would show how an
ordinary initial quotient regenerates the six new demand bits at every level.

## Claims and experiment

- `D-9403` — frozen supply/demand interface;
- `L-9405` — demand-tree isometry and six-bit lift law;
- `T-9407` — stationary matching isometry and ghost-stage theorem;
- `T-9408` — bounded-increment residue novelty;
- `X-9403` — exact finite replay.

Canonical `X-9403` SHA-256:

```text
1a2908bab06d6ae0db096a9516b87b953eb4f96823fdb2ea0ab71fa0686d1962
```
