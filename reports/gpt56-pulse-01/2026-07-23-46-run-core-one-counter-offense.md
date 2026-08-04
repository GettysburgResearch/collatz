# Run-core one-counter counterexample offense

**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Branch:** `agent/gpt56-pulse-01/46-two-pulse-offense`  
**Date:** 2026-07-23

## Starting hypothesis

The most direct positive object in the previous packet was the exact
negative-three-cycle chart

```text
A: z=8q    ->9q
B: z=1+16q->1+9q,
physical n=6z-5.
```

Any nontrivial positive ordinary all-time path would already disprove Collatz.
The goal of this session was to replace the vague phrase “one-counter
invariant” by the smallest exact deterministic arithmetic state, then attempt
to construct it.

## Repository refresh

The live repository moved during the session.

- PR #49 reduced the linear phase-34 refund architecture to one deterministic
  complement quotient; infinite definedness is its sole positive gap.
- PR #34 wave 25 independently extended the centered sparse-cycle exclusion
  through six non-`2` valuations and proved an additive/fixed-residue
  one-counter periodic-output obstruction.
- PR #50 excluded accelerated cycle length 185 conditionally on the cited
  92-local-minimum theorem.

Accordingly, local `T-8001` is retained as an independent five-defect proof,
but it is no longer described as the cycle frontier. The live sparse frontier
begins at seven defects.

## New exact mathematics

### 1. Maximal-run section and one quotient

Every infinite path contains infinitely many `B` edges. Immediately after a
`B`, a continuing state is

```text
z=2^(3r)u,
u odd,
9^r u=1 mod16.
```

The macro `A^r B` is

```text
z+ = (9^(r+1)u+7)/16.
```

If the next run is `s`, the core relation is

```text
2^(4+3s)u+ = 9^(r+1)u+7.
```

The next core is forced to be `1 mod144` for even `s` and `89 mod144` for odd
`s`.

For every ordered pair `(r,s)`, one residue `a_(r,s) mod 2^(8+3s)` encodes
both exact valuation and next-`B` legality. Writing

```text
u=a_(r,s)+2^(8+3s)k
```

leaves exactly one unbounded ordinary quotient. A third run `t` imposes one
class

```text
k=rho_(r,s,t) mod 2^(4+3t),
```

and a general lift has exact successor

```text
k+=sigma_(r,s,t)+9^(r+1) ell.
```

This is `L-8002`. It is an exact changing-modulus quotient-refund system, not
an externally supplied directive.

### 2. Pointwise expanding highway

The macro difference is

```text
16(z+-z)=(9^(r+1)-2^(4+3r))u+7.
```

It is nonpositive at `r=0`, strictly negative for `1<=r<=4`, and strictly
positive for every `r>=5`, because

```text
9^6>2^19.
```

Therefore one finite ordinary state whose deterministic macro is defined
forever and emits only runs at least five gives an explicit positive unbounded
Collatz orbit. This is `T-8002`.

The homogeneous average threshold is

```text
log(16/9)/log(9/8)=4.884949192...
```

but the theorem uses the cleaner pointwise condition `r>=5`.

### 3. Explicit reset highways

For every `m=0 mod6`,

```text
z_m=(2^(m+4)-7)/9
```

is an ordinary positive integer satisfying

```text
z_m --B--> 2^m --A^(m/3)--> 9^(m/3).
```

If `d=m/3`, exactly

```text
floor((3+v2(d))/4)
```

consecutive `B` edges then occur. This follows from

```text
B^j(9^d)=1+9^j(9^d-1)/16^j,
v2(9^d-1)=3+v2(d).
```

The post-`B` state re-enters `A` exactly when

```text
v2(d)=1 mod4,
oddpart(d)=3 mod8.
```

Thus ordinary finite survival depth is unbounded by a closed formula. This is
`L-8003`, not an infinite extrapolation.

## Exact computation

`X-8005` checks:

```text
legal local edges:              93,750
maximal-run macros:             35,716
two-macro quotient identities:  2,555
reset seeds through m=1200:        200
maximum frozen actual depth:       402
```

The first even run indices with `u=1` producing next-run valuations
`4+3s`, `s=0,...,6`, are

```text
0, 6, 214, 1622, 8790, 66134, 918102.
```

A bounded search for a pure-power reset or second exact reset finds only the
trivial exponent `1`. This is bounded evidence only.

Both author and independent scripts replayed the frozen result exactly.

## Construction attempts that did not close

1. **Fixed run schedules.** Constant and short periodic high-run schedules
   select periodic completion points; no ordinary nontrivial state appeared.
2. **Simple exponential highways.** Small templates of the form
   `A*2^(dm)+B` did not close under the chart in bounded symbolic searches.
3. **Least high-run cylinders.** Beam and exhaustive small-depth searches over
   runs `5..10` produced arbitrary long finite prefixes but no least
   representative that continued with another high run without adding a new
   top block.
4. **Pure-power regeneration.** The reset family did not map back exactly to a
   power of two or to another reset seed in the declared bounded search.

These failures are not universal theorems and are not promoted as claims.

## Main conclusion

The direct positive objective is now exact:

```text
find one finite (r0,r1,k0)
whose deterministic changing-modulus quotient map is defined forever
and emits r_j>=5 for all j.
```

That one object gives the explicit physical seed

```text
z0=2^(3r0)(a_(r0,r1)+2^(8+3r1)k0),
n0=6z0-5,
```

and `T-8002` supplies positivity and unboundedness automatically.

The additive one-counter obstruction in PR #34 does not close this target:
the update multiplies by `9^(r+1)`, performs exact division by a changing
power of two, and reads a canonical unbounded valuation/top boundary.

## Files changed

- `research/integer-first-offense-independent/claims/L-8002-*`
- `research/integer-first-offense-independent/claims/T-8002-*`
- `research/integer-first-offense-independent/claims/L-8003-*`
- `experiments/X-8005-run-core-highways/`
- packet README and this report

## Recommended next actions

1. Independently reconstruct the full modulus `2^(8+3s)` in `L-8002`; using
   only the exact-valuation modulus loses the next-`B` condition.
2. Freeze a small high-run alphabet, but retain the exact quotient and changing
   modulus. Search for a nonlinear inductive class, not a residue-only lasso.
3. Derive the Hensel recurrence of the reset-family re-entry quotient and test
   whether its source exponent refunds the growing top boundary.
4. Compare the quotient transition directly with PR #49's complement-counter
   map; a common nonlinear top-boundary lemma could close both positive lanes.
5. Continue the finite cycle offense at seven or more centered defects in
   parallel.

## Organizational improvement

The project should label one-counter claims by **observation power**:

```text
additive + zero/fixed residues,
exact multiplicative quotient,
changing-modulus remainder,
canonical most-significant boundary.
```

Calling all four “one-counter” obscures the precise line already excluded by
`PR34/L-9915` and the stronger line still capable of constructing a witness.