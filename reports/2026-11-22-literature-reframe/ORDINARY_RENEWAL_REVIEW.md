# Independent review: ordinary minimum moments and weighted renewal

**Verdict:** the direct antichain construction and the subsequent
conditional implications are mathematically sound at their stated scope.
The note proves a useful reduction of every possible ordinary escape to a
critical first-moment obstruction, **conditional on the exact population
hypothesis (PDU)**. It does not prove (PDU), the summable weighted defect
(R15), or exclusion of additional positive cycles. No Lean validation is
claimed for this analytic reduction.

## Exact sources and review scope

The reviewed file is
`research/literature-reframe-20261122/ORDINARY_RENEWAL.md`, SHA256
`519f3e5ade92d0d39158a08b7a47bd1e83e292a9bab77ae0bbf94c6bafbe5139`.

I independently fetched the frozen repository source
[PR180, GLOBAL_RENEWAL_ATTACK.md](https://github.com/GettysburgResearch/collatz/blob/d0349de2108abb7c8fb8393c086610e3372df116/research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md)
at commit `d0349de2108abb7c8fb8393c086610e3372df116`. Its §5 states
precisely the unit-source inequality (PDU) used here: absolute positive
constants, every positive unit target, source cutoff at least a constant
times the target, and a lower count proportional to `X/a`.
Its §8 is the separate source of the ordinary first-power inverse
envelope used in R17. This review checks that those interfaces have been
quoted accurately. It does **not** certify the new joint-clock analytic
argument on which that source bases its population assertion, or import
that argument as a published theorem.

I also independently opened Tao's
[published text](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F),
checking Theorem 3.1 and Proposition 1.11 at their actual statements. The
former has the uniform logarithmic survivor bound used in R12. The latter
has the two logarithmically sampled source annuli, the power bound on
non-passage, and the logarithmic total-variation error used in §6.
It does not state the weighted defect estimate R15.

## 1. Ordinary state space and population normalization

The accelerated map preserves the positive odd integers not divisible by
three. Every positive shortcut orbit reaches this state space after
removing its initial factors of two and, if required, one accelerated odd
step. A shortcut hit to an odd target is an accelerated hit. Thus PDU
applies to exactly the ordinary basins `B(a)` used in the note.

Partial summation is correct, including its endpoint term:

\[
\sum_{n\le X,\ n\in B(a)}\frac1n
=\frac{A_a(X)}X+\int_1^X\frac{A_a(t)}{t^2}\,dt.
\]

Dropping nonnegative terms and integrating the PDU lower bound only from
`C_u a` to `X` gives R1. One fixed finite family can always be treated
at a common cutoff. The proof never applies a target-dependent onset
simultaneously to an infinite unbounded family.

Normalization by `log X` is consistent throughout. The two residue
classes 1 and 5 modulo 6 have counting density `1/3` and harmonic mass
`(1/3)log X+O(1)`. No conditional normalization by the density of the
state space has been inserted. This explains the factor `1/3` in the
reciprocal basin budget and in R17.

## 2. Off-orbit basins and the exact minimum identity

An injective orbit in the positive integers tends to infinity. Its
successive suffix minima are attained, strictly increase, and have
increasing occurrence clocks. The next suffix minimum is at most the
immediate successor of the previous one. Therefore
`t_(j+1)+1 <= (3/2)(t_j+1)`, proving R2 without assuming the whole
trajectory is monotone.

The powers of two run through all six unit classes modulo nine. Exactly
two exponents in `1,...,6` produce positive odd unit parents of each
`t_j`. At most one parent can be on the original injective orbit: any
such occurrence must be its unique immediately preceding state. Hence
an off-orbit parent `b_j` always exists, and
`b_j < (64/3)t_j` is the correct uniform bound.

The whole basins `B(b_j)` are disjoint, not just selected pieces of
them. If a source hit two distinct parents, after its first parent hit
its next state would be on the original orbit. It could never then hit
another off-orbit parent. This proves disjointness without counting nested
ancestor levels as separate populations.

Taking `r_j=min B(b_j)` is essential. Each `B(r_j)` is a subset of
its respective `B(b_j)`, and the roots are distinct. Every state before
the trajectory reaches `b_j` remains in `B(b_j)`, so its value is at
least `r_j`. The trajectory actually visits `r_j`. After `b_j`, it
visits `t_j` and remains in the suffix on which all states are at least
`t_j`. This proves exactly

\[
n\in B(r_j)\quad\Longrightarrow\quad
m(n)=\min(r_j,t_j)\ge r_j/(64/3).
\]

In particular, this is an all-time minimum bound for every source being
counted. It is stronger than a finite-time or typical-future assertion.

## 3. First-moment divergence and the limit order

For each fixed finite selection of `N` roots, multiplying the minimum
bound by the harmonic population bound cancels `r_j`. Each basin
contributes at least `c_u/(64/3)` to the lower limit of the normalized
first moment. The proof takes the lower limit in the source cutoff while
`N` is fixed, then lets `N` grow. This correctly proves an infinite
lower limit; it does not exchange an infinite sum and a lower limit
without justification.

Consequently, finite lower limit of the first moment excludes every
injective orbit under PDU. Once every orbit is eventually periodic,
distinct merger components have distinct cycles. For any finite choice
of components, let `s_i` be their least positive odd unit members. On
`B(s_i)` the full minimum is exactly `s_i`. These basins are disjoint
and contribute at least `c_u` each. Thus the same finite-family argument
proves that a finite first-moment lower limit `L` allows at most
`L/c_u` components.

This yields a finite global periodic attractor. It does not identify that
attractor with the cycle through one. Conversely, a bound on all ordinary
minima immediately bounds the normalized first moment. The distinction
between a finite attractor and the Collatz attractor is preserved.

## 4. The reciprocal survivor tail and its constant

If `r_j>K M`, with `K=64/3`, R4 gives `m(n)>M` on `B(r_j)`.
Applying R1 to a finite subfamily, taking the cutoff lower limit, and
then enlarging the finite subfamily proves R9. Using a limsup in the
definition of `tau(M)` only weakens the lower bound. All-source counting
of the same disjoint basins gives
`c_u sum_j 1/r_j <= 1/3`, so the reciprocal sums used subsequently are
finite.

For the increasingly sorted roots, at least `k+1` unsorted roots lie
below `K t_k`. Therefore
`rho_k <= K(t_0+1)(3/2)^k`. With
`h_k=rho_k sum_(l>=k)1/rho_l`, the recursion is exactly

\[
h_k=1+(\rho_k/\rho_{k+1})h_{k+1}.
\]

If eventually `h_k<=H<3`, then `H>1` can be chosen, and multiplying
the rearranged recursion forces root growth at least
`(H/(H-1))^(N-J)` up to a fixed factor. This base is strictly larger
than `3/2`, contradicting the preceding root bound. Hence
`limsup h_k>=3` as stated.

The chosen threshold `M_k=ceil(rho_k/K)-1` is strictly below
`rho_k/K`, even when that quotient is an integer. It tends to infinity
and `M_k/rho_k -> 1/K`. All roots in the reciprocal tail starting at
`k` therefore qualify for R9, giving

\[
\limsup_{M\to\infty}M\tau(M)
\ge3c_u/K=9c_u/64.
\]

This verifies both the strict floor condition and the numerical constant.
Tao's logarithmic survivor upper bound remains compatible with this
reciprocal lower bound. It cannot be substituted for the required
`o(1/M)` upper bound.

## 5. Weighted first-passage recursion and what is unproved

On successful first passage below `x`, every earlier state is above
`x`, while the attained endpoint is at most `x`. The global minimum
is therefore unchanged by removing the prefix. This proves R13 exactly.
The successful endpoint laws are subprobabilities; retaining the failed
source costs `Q_i` gives the displayed identities for `L`.

Subtracting those identities, using `m(u)<=u`, and dropping only the
nonpositive term `-Q_1` proves R14. The failed-source contribution
`Q_2` cannot be dropped. The revised note also distinguishes these
subprobabilities from Tao's convention of assigning a failed passage an
artificial value of one. Removing that atom changes total variation by
at most the sum of the two failure probabilities, which does not change
the stated crude total-variation order.

If R15 held, R14 would bound the annular expectations uniformly along
`x_j=x_0^(alpha^j)`. Their annuli cover the interval up to `x_J`.
Multiplication by each annulus's harmonic mass converts its expectation
back to the actual source sum. The sum of those masses is `O(log x_J)`;
shared endpoints are harmless positive overcounts and have bounded total
harmonic weight. Restriction to odd units decreases the sum. This proves
FM along that subsequence, which is enough for the stated lower-limit
criterion.

The limitations of the published bounds are accurately stated. Direct
comparison of the observable `u` costs a factor up to `x`, yielding
`x/(log x)^c`. A failed source has a minimum bounded only by its starting
value under this crude argument, so the other cost is at most
`x^(alpha^3-c)`. Those estimates do not establish summability of the
defect. The first unsupported renewal step remains R15.

One notation issue found in review has been fixed in the pinned version:
R12 already sums over all positive odd inputs, so the meaning of `U,m`
on that domain is now stated before R12, rather than only in §6.

## 6. Ancestor padding and the first-power envelope

Given the quoted exact quotient identity, R16 follows by comparing both
integer floors with `2^h`. It retains the original source after the
ancestor arrives there; the ancestor's large size is not an independent
replacement for post-arrival binary precision. The example showing that
cofinal arithmetic-progression intersection alone need not imply positive
density is also valid, and is correctly presented only as a logical
comparison of statement strengths.

For R17, the first-power ordinary operator is kept separate from the
compact squared operator. The actual predecessor edge is one nonnegative
term in `P F`, giving exactly the ratio inequality displayed in the
note. Applying PDU to off-orbit parents at every orbit state gives
`sum_j 1/n_j <= K/(3c_u)`. Since
`log(1+1/(3n_j)) <= 1/(3n_j)`, the product of the edge ratios is
positive, proving the stated lower bound for `F(n_j)/n_j`.

This conclusion is conditional both on the qualified population input
and on the separate ordinary envelope input. It is compatible with the
available linear upper bound on a nonperiodic target. Decay along inverse
exponent rays of a fixed target concerns different points and cannot be
substituted for uniform sublinearity along the escaping orbit.

No complete Collatz theorem or unconditional ordinary renewal estimate is
certified by this review. No Lean process was run for it.
