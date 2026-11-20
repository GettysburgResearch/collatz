# Independent narrow review of the elementary prime-height packet

Date: 20 November 2026. Reviewer: `creative_capacity`, separately from the
author and the parent agent's contribution to the variation argument.

## Frozen scope and verdict

Reviewed file:
`research/structural-reset-20261120/adelic/PRIME_HEIGHT_ESCAPE.md`.

SHA-256, read and verified from the filesystem:
`3050ec6438faced2ed9bb45751e0299eb5d96778a4d0a064a8c8f7519e6868e3`.

Input repository head cited by the packet:
`55d8968d2ecbc23a91c9c4733929f34be9bf0d28`.

**Verdict: VERIFIED at the stated file bytes for ADEL-001 through
ADEL-007, with their printed ordinary-domain and non-closure boundaries.**
This review reconstructed the algebra and quantifiers from the written
argument. No numerical census, source factorization experiment, external
analytic theorem, or repository validator was used as mathematical evidence.
The verdict does not extend to later file edits, adjacent files, a
prime-retention claim, or a proof of Collatz.

## 1. Affine and gcd estimate

For `d=j-i` odd accelerated steps and cumulative exponent `B`, independent
iteration gives

\[
2^B n_j=3^d n_i+
\sum_{t=0}^{d-1}3^{d-1-t}2^{B_t}.
\]

The correction is positive and divisible by `gcd(n_i,n_j)`. Because
`B-B_t>=d-t`, its normalized value is at most

\[
\sum_{u=1}^d3^{u-1}2^{-u}=(3/2)^d-1.
\]

Also `B=x_i-x_j+sum b_u<=x_i-x_j+2d`, where
`b_u=log_2(3+1/n_u)`. Combining these gives the asserted strict bound
`log_2 gcd(n_i,n_j)<x_i-x_j+3d`. This includes gcd 1, uses the
complete ordinary affine correction, and places no upper bound on the
individual division exponents.

## 2. Local prime budget and adaptive prime sets

For each chosen prime, select one block index attaining its largest
valuation. At any other index the entire prime power divides the gcd with
that selected state. The two indices may be ordered in either temporal
direction; replacing their height difference by the block range is valid
in both cases. Thus each nonselected prime height is below `R_B+3r`.

Summing over at most `s` primes and using
`M_B<=H_B/r+R_B` yields ADEL-002 with the printed conservative constant.
The companion bound outside the union of the selected indices follows
from the same argument. Repeated maxima and ties cause no difficulty.

Crucially, the inequalities hold separately for **every** prime set of
cardinality at most `s`, with identical right-hand sides. The primes may
therefore be selected after the entire history is seen, and a different
set may be selected at each horizon. The proof does not allow selecting
a different set at each individual orbit state; the packet says this
explicitly. Taking the supremum over the actual prime labels is justified.

## 3. Variation and finite history

Upward increments of `x=log_2 n` are at most 1. If `P,D` are its positive
and negative variations over `N` transitions, then
`P<=N` and `D=P+x_0-x_N`. Since `x_N>=0`, their sum is at most
`2N+x_0`. Large downward divisions are therefore paid for, not discarded.

The internal increments of disjoint consecutive state blocks are disjoint;
their ranges sum to at most this total variation. Summing the local budget
gives, exactly with the stated conservative constants,

\[
Y_N(S)\le (s/r)W_N+sr x_0+5srN+B_{N,r}.
\]

The incomplete terminal block is explicitly retained. The formula also
remains valid when `r>N`, when it is simply a loose inequality.

## 4. Escapes, terminal tail, and both normalizations

A non-eventually-periodic ordinary deterministic orbit has distinct
positive integer states, so it eventually leaves every finite set.
Consequently `x_j->infinity` and `W_N/N->infinity`.

The terminal boundary argument is sound: bounded upward increments imply
`W_N>=R x_N-R(R+1)/2` for every fixed `R` and `N>=R`. Dividing by
`W_N`, taking `N` first and then `R`, gives `x_N/W_N->0`.
The finitely many preceding terminal states are bounded by their own
prefix denominators, proving `B_{N,r}/W_N->0` for each fixed `r`.
This proves the weighted limit uniformly in `S`.

For the count-weighted limit, after an arbitrary fixed floor `h` is
eventually attained, at most `s` selected indices per block contribute
the trivial bound 1. The others contribute at most
`s(R_B+3r)/h`. Variation and block summation give the printed
`s/r+5sr/h`. The finite initial segment and bounded terminal block vanish
in count density. The order of limits, first the orbit horizon, then the
floor, then the block length, is valid and remains uniform over `S`.
The threshold-count conclusion follows directly by comparison with
`epsilon` times the indicator of a counted state.

There is no undefined `0/0` in the escape theorem: an escaping orbit never
hits 1. The fixed-point-1 case occurs only in the separate converse and
cycle-count discussion, where `[1]_S=1=1^epsilon` is handled directly.

## 5. Cycles, counts, and bounded support

Repeating an actual cycle preserves the affine and variation estimates.
Taking horizons divisible by both its period and the chosen block length
removes the terminal term, and division by `NH` gives ADEL-006.
Primitivity supplies distinct positive states, whose product is at least
`m!`; this is enough for `H->infinity` as the period grows.

For the count estimate, at most `floor(2^h)` distinct phases are below
the logarithmic floor. The same selected-index and variation argument
on repeated cycles then gives (21), uniformly in the prime set. Choosing
the block length and floor in the printed order supplies an explicit
finite constant. The fixed point 1 is harmless because it is among the
low states and does not enter a division by its zero logarithm.

If all cycle primes lie in a set of size at most `s`, then `P_S=1`.
Taking `r=2s` yields `H<=20s^2`. The factorial lower bound gives
`m<=e 2^(20s^2)<3 2^(20s^2)`. For each fixed period, cyclic logarithmic
summation gives `sum a_j<=2m`, so only finitely many positive exponent
words remain. Each has a unique rational fixed point at most, because
its slope `3^m/2^(sum a_j)` is not 1. Integrality, positivity, and exact
branch replay can be checked when enumerating. This is an effective
finiteness conclusion uniform over the identities of the primes; it is
not an exclusion of every word or every nontrivial cycle.

## 6. Exact scientific boundary

The strongest verified new statement is uniform dispersion of accumulated
prime height over every bounded number of adaptively selected primes on
any actual ordinary escape, together with the corresponding cycle and
count estimates. Its proof is elementary and does not need a bounded
valuation alphabet.

No contradiction follows until one proves a competing retention or
tightness property on one fixed surviving forward history. The finiteness
of each individual integer's factorization does not give that property.
The packet keeps this gap explicit. Its eventual-periodicity
characterization is a characterization, and its bounded-prime-support
cycle result is a finiteness theorem; neither has been promoted to
universal convergence in this review.
