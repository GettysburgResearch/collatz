# Effective occupation bounds from bounded-height ternary coefficients

**Status: written quantitative consequence of the pinned S-unit return
theorem, with a new elementary finite arithmetic core. No entropy lower
bound or escape exclusion is proved.**

The positive target was to force enough entropy in one actual escaping
orbit to contradict PR185's entropy ceiling. The argument below instead
obtains a source-independent, effective finite-time upper bound on visits
to integers with a fixed number of binary one-runs. Unlike a qualitative
use of the S-unit ratio set, its constants do not depend on unknown
heights of S-unit solutions.

## 1. Statement

Let `U(n)=(3n+1)/2^v2(3n+1)` on positive odd integers. Write `R(n)` for
the number of maximal binary one-runs. Consider an injective actual
segment

\[
q_0,q_1,\ldots,q_{N-1},\qquad q_{i+1}=U(q_i).
\]

Fix an integer `S >= 1`, and put

\[
m(S,L)=4S+L,
\quad E(S,L)=3L+4S(4S+3L),
\quad M(S,L)=2^{E(S,L)}.
\tag{1}
\]

Let `H_S` be the finite exceptional-separation set from PR177's
`LITERATURE_ARITHMETIC_RETURN.md`, and write `B_S=|H_S|`. For every
integer `L >= 1`,

\[
\boxed{
\#\{0\le i<N:R(q_i)\le S\}
\le (B_S+1)(N/L+1)+L M(S,L).
}
\tag{2}
\]

The quotient on the right is real. An integer form with
`ceil(N/L)` in place of `N/L+1` also follows from the proof.

In particular, for all sufficiently large `N` depending only on `S`,

\[
\boxed{
\#\{0\le i<N:R(q_i)\le S\}
\le16(12S+3)(B_S+2)\frac{N}{\log_2 N}.
}
\tag{3}
\]

One sufficient threshold is

\[
N\ge2^{64(S+1)^2}.
\tag{4}
\]

These bounds are uniform in the initial source and in the position of
the segment. Every segment of an escaping positive orbit is injective.
The main bound (2) also applies to injective prefixes of terminating
orbits before their first repetition. It is not a statement about a
randomly sampled integer or an independent gap process.

The S-unit solution-count theorem gives an explicit upper bound for
`B_S`. For example, with

\[
Q_S=(24S)^{12S}(8S+1),\qquad
\mathcal B_S=(4S)^3 2^{4S}3^{Q_S},
\tag{5}
\]

one may replace `B_S` by the computable integer `mathcal B_S` everywhere.
These constants are very large; no practical numerical efficiency is
claimed.

## 2. The actual relation has a bounded ternary coefficient height

PR177 uses

\[
3^h n+C=2^A m,\qquad
C=\sum_{i=0}^{h-1}3^{h-1-i}2^{A_i},
\quad A_i=\sum_{j<i}a_j,
\tag{6}
\]

for an actual `h`-odd-step segment from `n` to `m`. If both endpoints
have at most `S` binary one-runs, their signed binary expansions and
the `h` positive correction terms give a signed relation of at most
`4S+h` terms.

Every term has the special form

\[
\varepsilon_i3^{j_i}2^{k_i},
\qquad \varepsilon_i\in\{-1,1\},\quad
0\le j_i\le h,\quad k_i\ge0.
\tag{7}
\]

The ternary exponents in (7) are bounded by the actual odd-step
separation. This additional information is absent from a general
finite-rank S-unit equation and is the reason an effective ratio bound
is available here.

### Dyadic separation lemma

Suppose a nondegenerate zero relation has at most `d` terms of the form
(7). Nondegenerate means that no nonempty proper subset of its signed
terms sums to zero. Then

\[
\boxed{
\max_i k_i-\min_i k_i\le(d-1)(d+2h).
}
\tag{8}
\]

**Proof.** Sort the terms by their binary exponents, retaining repeated
exponents as separate terms. Suppose two consecutive exponents `u<v`
satisfy `v-u>d+2h`. The sum `Z` of all terms below this gap is a nonempty
proper subsum. Every remaining term is divisible by `2^v`, so (7)'s
zero relation makes `Z` divisible by `2^v`. On the other hand,

\[
|Z|\le d3^h2^u\le2^{d+2h+u}<2^v,
\]

where `d <= 2^d` and `3^h <= 2^(2h)` were used. Thus `Z=0`, contrary
to nondegeneracy. Every consecutive exponent gap is at most `d+2h`.
There are at most `d-1` such gaps, which proves (8). Repeated exponents
have gap zero and cause no exception. ∎

The application needs a **local** refinement of this span bound. Choose
in the selected cluster the correction term with greatest sorted
index. Write its exponent as `k`, and let `b` be the exponent of the
chosen initial endpoint term. If `k >= b`, no positive exponent
separation needs to be bounded. If `k < b`, every term after that
correction up to the chosen initial term is an endpoint term. There
are at most `4S` endpoint terms, so at most `4S` adjacent gaps need to
be crossed. Thus

\[
b-k\le4S(d+2h).
\tag{8a}
\]

The last correction in sorted order also handles repeated exponents:
all terms after its index are endpoint terms, regardless of ties.
Charging only these endpoint terms changes the effective core's
exponent from quadratic to linear in the time separation `h` for
fixed `S`.

## 3. An explicit finite core at every nonexceptional separation

Set

\[
d=4S+h,\qquad
T=4S(d+2h)=4S(4S+3h),\qquad Q=3^h2^T.
\tag{9}
\]

Choose the minimal zero subset of the full relation (6) that contains
the largest initial endpoint term

\[
\Lambda=3^h2^{b}>3^h n.
\]

As in PR177, minimality makes this subset nondegenerate. If
`h notin H_S`, the subset contains a correction term `c`: an
endpoint-only subset would have a cross-endpoint ratio of ternary
valuation `h` and would put `h` in `H_S`.

Choose `c=3^j2^k`, `0 <= j < h`, with greatest sorted index among
correction terms in the selected subset. Its actual cardinality is at
most `d`; apply the local refinement (8a) with this enlarged gap budget.
If `k >= b`, the same one-sided bound is automatic. In either case,
`b-k <= T`, so

\[
\frac c\Lambda
=3^{j-h}2^{k-b}\ge3^{-h}2^{-T}=\frac1Q.
\]

Consequently

\[
\boxed{3^h n\le Q C.}
\tag{10}
\]

The exact ordinary correction identity gives, if every odd input on
this segment is at least an integer `Y >= 1`,

\[
\frac{C}{3^h n}
=\prod_{i<h}\left(1+\frac1{3q_i}\right)-1
\le\frac{2^h-1}{3Y}.
\tag{11}
\]

Take `Y=2^h Q=6^h2^T`. Equations (10) and (11) conflict. Thus every
such segment contains an actual odd input below

\[
\boxed{M_0(S,h)=6^h2^{4S(4S+3h)}.}
\tag{12}
\]

This replaces the unknown minimum of a general S-unit ratio set by an
explicit bound. For `1 <= h <= L`, (12) is at most the `M(S,L)` in
(1), because `6^h <= 2^(3h)` and the displayed nonnegative exponent
is increasing in `h`.

## 4. Packing by the number of exceptional separations

Partition the `N` time indices into consecutive blocks of length `L`,
with a possibly shorter final block. Call a block bad if it contains
a state below `M=M(S,L)`.

There are at most `M` bad blocks. Indeed, the segment is injective,
and fewer than `M` positive integers lie below `M`; assign one such
state to each bad block. The blocks are disjoint.

In a good block, any two low-run times differ by a separation in
`H_S`: otherwise their actual connecting segment would contain a
state below `M` by (12). If the low-run times in that block are
`t_1<...<t_r`, the `r-1` distinct positive differences `t_i-t_1`
all belong to `H_S`. Thus `r <= B_S+1`.

Good blocks therefore contribute at most
`(B_S+1) ceil(N/L)` low-run times. Bad blocks contribute at most
`ML`. This proves (2).

This argument uses **the cardinality** of `H_S`, never its largest
element. That distinction is essential: an explicit bound on the
number of S-unit solutions does not bound their heights or the largest
exceptional separation.

## 5. The explicit logarithmic rate

Put `K=12S+3`, `u=log_2 N`, and `L=floor(u/(4K))`. Under (4),
`u >= 64(S+1)^2`, so `L >= 1` and `L >= u/(8K)`. The exponent in
(1) satisfies

\[
E(S,L)=16S^2+KL\le u/4+u/4=u/2.
\]

Hence `M(S,L) <= sqrt(N)`. Also `L^2 <= u^2 <= 2^(u/2)=sqrt(N)`
in the range (4), so `L M(S,L) <= N/L`. Substituting into (2), and
using `N/L >= 1`, gives

\[
\#\{R(q_i)\le S\}
\le2(B_S+2)N/L
\le16(12S+3)(B_S+2)N/\log_2N.
\]

No escape-rate estimate or orbit-dependent threshold is used.

## 6. Why the constants are effective without effective S-unit heights

For each arity `2 <= ell <= 4S`, normalize a nondegenerate signed
`{2,3}`-unit relation by one coordinate. The normalized tuple lies in a
group of rank `2(ell-1)`. Evertse–Schlickewei–Schmidt Theorem 1.1
bounds the number of such tuples for a fixed sign pattern by

\[
\exp\big((6(\ell-1))^{3(\ell-1)}(2\ell-1)\big).
\]

There are at most `2^(4S)` sign patterns per arity, at most `(4S)^2`
coordinate ratios per tuple and at most `4S` arities. Replacing `e`
by `3` and enlarging the integer exponent gives (5). The arity-two
case contributes only the ratio one and fits the same coarse bound.

The effective count controls only `B_S`. The effective core (12) comes
from the separate dyadic separation lemma and bounded ternary
coefficient heights. No effective height bound for arbitrary
many-variable S-unit solutions has been inferred.

## 7. What this does and does not advance

The prior qualitative conclusion already forces divergent run-weight
averages on each escaping orbit. The new result supplies a uniform
finite-time modulus for every fixed run cutoff, independently of the
ordinary starting source and its escape speed. It can be applied before
taking an original-source sum or a moving-window limit.

It does not force positive metric entropy. A sequence may visit only
integers with large binary-run count while having low entropy in its
time coding. It also does not supply the run-weighted terminal-energy
upper bound or a sibling-current lower bound. Quantitative ESS grows
very rapidly with `S`; choosing `S` to grow with `N` yields only a very
slow effective growth scale, not a power-law gain in ordinary height.
The full entropy/escape exclusion sought in this lane remains open.

## Frozen inputs and primary source

- PR177, `e4ca639326bac73da8c2a698dec8a749e5efbe68`,
  `research/lean-exact-witness-global-20261121/LITERATURE_ARITHMETIC_RETURN.md`,
  Sections 2–5: signed endpoint representation, finite exceptional
  separation set, and the selected minimal zero relation.
- PR185, `980d40fc4afeaaf8f2a9256f322acf3e4568e013`,
  `research/deep-closing-20261122/ACTUAL_ORBIT_ENTROPY.md`:
  the actual ternary time-law entropy ceiling motivating this attack.
- J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt,
  *Linear equations in variables which lie in a multiplicative group*,
  Annals of Mathematics **155** (2002), Theorem 1.1:
  <https://annals.math.princeton.edu/2002/155-3/p04>,
  <https://arxiv.org/pdf/math/0409604>.

## Formalization boundary

The companion `lean/Collatz/DyadicCluster.lean` proves the elementary
finite arithmetic core from explicit hypotheses on a supplied sorted
integer relation. It proves the adjacent binary-exponent gap, total
span, interval and nearby-coordinate spans, endpoint/correction monomial
comparison, and
correction denominator. It also derives the required prefix
nonvanishing from full indexed nondegeneracy, allows the natural
coefficient bound `abs(c_i) <= 3^h`, and proves the finite-floor
contradiction and descent implication when the ordinary correction
estimate is supplied. A separate finite-set theorem proves the
cardinality-only anchor-difference packing step. A finite index-interval
lemma bounds the index distance to the last correction from the number
of endpoint indices.

The complete actual-orbit statement (2), the logarithmic rate (3), and
the ESS count (5) are written mathematics. The Lean file does not
formalize ESS, select and sort the minimal cluster from the signed
binary endpoint expansion, establish the actual correction identity,
or formalize the block decomposition and real-logarithm optimization.
It introduces no opaque proposition or unproved axiom in place of
those steps. The audit lists every public theorem and its kernel
dependencies. No proof of Collatz is claimed.
