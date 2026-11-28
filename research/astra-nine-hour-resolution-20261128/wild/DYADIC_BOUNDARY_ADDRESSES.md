# Dyadic addresses of a persistent unlike pair

**Written, elementary.** Use the shortcut Collatz map on positive integers.
Let `f(n)` be any binary coloring with `f(T(n))=f(n)`. In particular, take
the indicator of reaching 1. If a nonconvergent positive integer exists,
this coloring is nonconstant and some adjacent pair has opposite colors.
All claims below concern the literal integer iterates of this coloring.
They use no external density or formalization result.

## From one edge to a forbidden-factor language

If `f(n) != f(n+1)`, the two endpoints of the doubled interval retain their
colors. Exactly one of the edges at `2n,2n+1` has unlike endpoints; it has
the same orientation. Choosing it forever defines its persistent boundary
address. In real coordinates this bisects `[n,n+1]`; use the actual
sequence of binary child digits, retaining its chosen expansion even at a
dyadic endpoint.

A length-`k` binary word read in the usual most-significant-digit order is
a forbidden factor if every adjacent pair in its residue modulo `2^k`
merges. Indeed, once such a block finishes in the child digits, the lower
endpoint at that depth has just that residue. A sufficient finite test is
that at residue representative `w` the trajectories from `w,w+1` agree
after `k` shortcut steps with equal odd counts. Under every source lift by
`2^k b`, both endpoints then increase by the same `3^q b`.

For every integer `k>=1` the suffixes below force exact counted merger
after `k+2` steps:

| parity of k | binary suffix of length k+2 |
| --- | --- |
| odd | `10` followed by `k-1` ones and a zero |
| even | `00` followed by `k-1` ones and a zero |

Write the lower endpoint as `n=2^k b-2` with odd `b`. After `k`
steps the two values are `A-1,3A-1`, with `A=3^(k-1)b`; they have
respectively used `k-1,k` odd departures. The indicated residue gives
`A=3 mod 4`. After a common halving, the first branch takes an odd step
and the second another halving. Both attain `(3A-1)/4`, with equal total
odd counts. In particular `100` is forbidden. After a first one, a zero
cannot be followed by another zero. Between successive later zeros,
there cannot be a positive even number of ones either: the preceding one,
the first zero, that even run and the next zero would give the odd-`k`
forbidden word. Thus every recurrent zero of the tail lies on the same
parity of binary positions. Constant and eventually constant tails are
included separately.

After discarding a finite prefix and choosing a pairing phase, every
nonconstant tail therefore has its binary pairs among `10,11`. The
ambient set of such possible addresses has Hausdorff dimension at most
`1/2`, before further dynamical restrictions. It is an ambient bound;
there are only countably many actual addresses for any fixed coloring
because each initial nonzero edge has one persistent child. There is a
strict improvement even in the ambient bound. The 12-bit word
`101110101110` gives a counted merger at time 12, with both endpoints
equal to 533 and both odd counts 6 (the exact replay checks both inputs). In the paired alphabet this forbids the fixed word
`10|11|10|10|11|10`. In aligned disjoint chunks of six pairs there are
at most 63 of the 64 unconstrained choices. Thus the Hausdorff dimension
of the full necessary address language is at most `log2(63)/12 < 1/2`.
Countable finite prefixes and the two pairing phases do not change this
upper bound.

## Exact ternary transport

Extend the coloring to positive dyadic rationals by `F(a/2^j)=f(a)`.
This is well defined. If `a` is odd, the map

    Phi(a/2^j) = (3a+1)/2^j

preserves its color. It also commutes with doubling. In the mesh
`h=2^(-j)`, the images of the endpoints and midpoint of the current
interval `[nh,(n+1)h]`, divided by `h`, are

    L = 3n + 2^v2(n),   M = 3n+2,   R = 3n+3+2^v2(n+1).

When `n` is odd, `L<M<R`. When `n=2 mod 4`, `L=M<R`, so the
actual next child is forced right. These two cases cover the persistent
tail after any initial zeros, because `100` is forbidden. The image
intervals are nested, have opposite endpoint colors and, if the address
is nondyadic, shrink to three times that address. Both dyadic endpoint
denominators then tend to infinity.

At a left-child choice (a zero) from an odd `n`, the new image interval
is the single adjacent mesh edge with lower index `p=3n+1`. If the next
zero comes after `r` ones, `r` is odd. Its new single-edge index is

    p' = 2^(r+1) p + 2^r - 2.

Indeed after those ones the original interval has left endpoint
`(n+1/2-2^(-r-1))h`. Its primitive numerator is odd. Applying the
formula for the next left choice gives the displayed index. The
corresponding new image interval within the previous one has left
coordinate `1/2-2^(-r)` and width `2^(-r-1)`. The intervening
binary address block is `0` followed by `r-1` ones and another zero.
Thus every pair of consecutive image blocks has a double zero at its
junction. If infinitely many blocks have positive runs of ones, the
actual image digits contain `100` infinitely often. Its canonical
dyadic brackets at those dates have *equal* endpoint colors, even though
the marked adjacent brackets after each whole block have opposite endpoint
colors. If every sufficiently late block has `r=1`, the image address
terminates in zeros and the corresponding source is eventually alternating.

This proves nested, genuinely unlike marked intervals at the ternary image
and identifies intermediate failures of persistence. It does not prove
that the collection of persistent addresses is invariant under
multiplication by three. In particular the hypotheses of a topological
times-two/times-three rigidity theorem have not been obtained. A possible
stronger attack must account for the compensating opposite boundaries
born inside intervals whose coarse endpoints agree, or rule out the
explicit run language by additional ordinary merger restrictions.
