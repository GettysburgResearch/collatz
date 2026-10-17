# Product-formula roadmap for the PR #3 room two-block filter

## Exact native frontier

For a stabilized three-symbol prefix `(a,b,c)`, PR #3 gives:

```text
rho_m=[-tau_m N_m^(-1)]_(M_m),
widehat_rho_m=rho_m+M_mh_m,
0<=h_m<64.
```

A late room requires

```text
q_m=floor(64rho_m/M_m)=0,
[-N_mh_m]_64 in {5,30,20,56}.
```

Thus the same modular inverse must have:

```text
six zero high bits below M_m,
then a six-bit lift producing an allowed output type.
```

## Exact rational equation

The lifted congruence is an equality

```text
N_m(rho_m+M_mh_m)+tau_m=64M_mk_m
```

for one integer `k_m`.

The zero-cell condition gives

```text
0<=rho_m<M_m/64.
```

The allowed output fixes `k_m mod64` after the known unit factors are removed.

Every quantity in this equality is an explicit finite sum or product of powers of `2` and `3`, with one of only 64 three-symbol prefixes.

## Completion-safe proof object

A viable proof should use the same exact equality at all places:

```text
real place:
  fixed-room defect expansion and size of rho_m;

2-adic place:
  six zero bits and the next Hensel lift;

3-adic place:
  output type / scaled-boundary valuation;

ordinary height:
  full numerator and denominator of the equality.
```

Do not compare an unrelated real limit with a `2`-adic completion value.

## Two routes

### Route A — Newton-carry contradiction

Derive a recurrence for the adjacent pair `(q_m,h_m)` under `m -> m+1`, retaining the growing high quotient. Prove that a zero lower cell and allowed upper cell force a nonzero ordinary numerator divisible by more powers of two than its global height permits.

### Route B — finite-state exponential equation

For each recurring prefix or overlap state, rewrite the equality as a fixed finite-term equation in a finite-rank multiplicative group. Audit every proper vanishing subsum. A nondegenerate family is then eligible for S-unit finiteness; a two-term degeneracy is eligible for explicit `2`-adic logarithmic-form bounds.

## Why the finite-room theorem helps

At most 64 eventual rooms/tails can survive. This does not enumerate them, but it eliminates an uncountable symbolic search. A cofinal contradiction for every moving two-block state closes the fixed corrected-stage architecture.

## Finite evidence boundary

The filter is empty at scales 12 through 19. This is a regression suite and a target-discovery tool, not an asymptotic theorem.
