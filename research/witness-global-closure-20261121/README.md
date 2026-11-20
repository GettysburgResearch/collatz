# Direct reverse-tripling witnesses and least-failure reductions

**PROPOSED research. The full 512-residue implication remains OPEN.** This
packet continues the [original witness investigation](../witness-closure-512-2026-11-20/README.md)
after reviewing the latest repository reductions. It contains exact new
witness transformations, a sharper height bound for the least direct
reverse-tripling failure, and explicit conditional descent certificates.
It does not supply a universal witness transformer or a counterexample.

## The original problem and an equivalent direct target

Let `E` consist of positive integers with a finite witness

\[
3^r x+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r},
\qquad 0=A_0<A_1<\cdots<A_r.
\]

The empty witness represents 1. Every other witness is exactly a finite
accelerated odd trajectory to 1, with increments
\(a_i=A_i-A_{i-1}\). Terminal exponent-2 loops are allowed. The question is

\[
x\in E,\qquad x\bmod512\in\{129,257,385\}
\quad\Longrightarrow\quad (x+1)/2\in E.
\tag{1}
\]

There is no bound on the length or exponents of the output witness.

The source-pinned reduction in PR146, independently reconstructed in
[RGA-001–002](REDUCTION_AUDIT.md), proves

\[
\boxed{\text{(1)}\quad\Longleftrightarrow\quad
 [\,27m\in E\Rightarrow9m\in E\text{ for every positive odd }m\,]
 \quad\Longleftrightarrow\quad\text{full Collatz convergence}.}
\tag{2}
\]

Write the middle implication as `R(m)`. The elementary reduction of (1)
to the two bridges `P(m)` and `Q(m)` is in the original packet. Their
composition gives `R(m)`. The nontrivial implication from all `R(m)` to
full convergence belongs to PR146: its 71 exact affine cells cover all
20,736 residues coprime to six modulo 62,208. Every path ends at a smaller
ternary unit and uses only ordinary equivalences and eligible reverse
tripling calls. The local checker independently rebuilds every guard,
endpoint and residue-cover assertion from frozen data. The written strong
induction supplies the universal implication. This reduction is credited,
not presented as a new result of this packet.

## Exact transformations of a supplied complete witness

For `N=27m`, let `a` be the first source exponent and `t` the first odd
successor. Then

\[
N=(2^a t-1)/3,\qquad 2^a t\equiv1\pmod{81},\qquad t\in E.
\]

[DRW-001–002](DIRECT_R_WORDS.md) gives every first-letter normal form and
exact target reconstruction. In particular, arbitrary source witnesses
in the following two unbounded prefix languages have explicit solutions:

\[
(2^k,4,b,\ldots)\longmapsto(1,2^k,1,b+2,\ldots),
\tag{3}
\]

\[
(2^k,3,1^\ell,2,b,\ldots)
\longmapsto(1,2^k,1^{\ell+2},b+2,\ldots),
\qquad k,\ell\ge0.
\tag{4}
\]

Superscripts in these words mean repeated letters. Each output witnesses
`9m`, has one more odd step, and preserves the total exponent. The proofs
use exact affine identities and check positive odd legality and the
required nonempty tails. They retain arbitrary terminal padding.

The case `a=4`, equivalently `m=31 mod32`, is therefore completely solved:
`(4,b,...) -> (1,1,b+2,...)`. The two displayed languages are not all
admissible source words.

## A sharper least-failure floor and low-rank consequences

If `R` fails, let `N_*` be its least failing antecedent: `N_*` is a
positive odd multiple of 27, `N_*` has a witness, and `N_*/3` has none.
[RGA-003](REDUCTION_AUDIT.md) extracts the exact maximum query ratio from
the frozen 71-cell reduction:

\[
H=\frac{213597}{23},\qquad G=\frac53H=\frac{355995}{23}.
\]

Strong induction then proves that every positive ternary unit below
`N_*/H` converges, and every positive integer below `N_*/G` converges.
For even inputs, convergence means membership of the odd part in `E`.
These constants concern the least direct-`R` antecedent; they are not
replacements for the constants of a differently defined binary minimum.

[DRW-006](DIRECT_R_WORDS.md) and
[LRF-001–004](LEAST_R_FAILURE.md) deduce the following restrictions on
that same hypothetical minimum:

- Its first source exponent lies in
  \(\{1,2\}\cup\{3,5,\ldots,63\}\cup\{6,8,\ldots,58\}\).
- If the first exponent is 1 or 2, its first successor satisfies
  \(v_2(t+1)\le12\).
- Its first-hit source witness has at least two odd steps.
- If that first-hit witness has exactly two steps, its first exponent
  is at least 5, within the preceding finite set.

The proofs retain the unbounded last exponents. For example the complete
two-letter progressions with first exponents 1, 2 and 3 are respectively
`b=22+162j`, `68+162j`, and `118+162j`. Exact target prefixes reduce them
to powers of three. Height comparison handles all sufficiently large
members by induction; two explicitly stored witnesses, for `3^8` and
`3^25`, handle the remaining finite endpoints. Their full cumulative
tuples and every valuation are checked, not inferred from a census.

These are exclusions from a global least failure. They do not claim that
every member of those families has an unconditional individual transfer
independent of the minimality argument.

## Conditional paths with complete witness reconstruction

[RB-001–003](R_BYPASS.md) gives 27 disjoint infinite affine cells. Every
cell connects the source and target by ordinary equivalences and calls
`R(p)` with strictly smaller positive odd `p<m`. The exact relative
density of these cells among odd parameters is

\[
153468843955/1043677052928\approx0.1470462951.
\]

Ten cells use ordinary equivalences alone. The other 17 retain 29
conditional calls. The finite artifact also explicitly lists its 341
unresolved cells. The checker verifies disjointness and the complete
partition into certified and unresolved cells; it does not relabel the
partial certificate as a complete cover.

The transformer carries the full supplied source witness through the
ordinary moves. Each recursive call receives an already constructed
witness for `27p`. Calls are ordered, and a missing child answer returns
`UNRESOLVED`. No target orbit search occurs inside the transformer.

A separate unbounded conditional family, [RB-004](R_BYPASS.md), is:

\[
p=\frac{3^{k-3}(27m-1)}{2^{2k+1}}\in\mathbb Z_{>0},
\quad p\equiv3\pmod8,\quad k\ge3
\quad\Longrightarrow\quad [R(p)\Rightarrow R(m)].
\tag{5}
\]

Here `p/m < (27/128)(3/4)^(k-3) < 1`. The child source witness has exactly
`k` fewer odd steps and total exponent smaller by `2k+1`. Given a child
target witness, the inverse construction adds those same amounts. Thus
both the integer parameter and the supplied source rank decrease in
this family. Its residue classes have total relative density `1/384`;
they overlap the finite artifact and are not added to its density.

## A further descent that permits a longer child witness

The subsequent [source-zero construction](SOURCE_ZERO_DESCENT.md) gives
another exact direct-`R` reduction:

\[
\boxed{R(m)\iff R\!\left(\frac{2048m-277}{2187}\right)
\quad\text{when }m\equiv50063\pmod{69984}.}
\tag{6}
\]

Writing `m=69984u+50063`, the child is
`p=65536u+46881`, so `0<p<m` for every `u>=0`.
A supplied parent source word converts by
`(a,tail) -> (1,2,1,2,3,1,3,a-2,tail)`, where `a>=5` is forced.
A returned child target word converts by
`(2,1,1,1,1,2,2,1,1,1,c,tail) -> (1,1,2,c-2,tail)`, where `c>=3`
is forced. The proof matches the actual positive integer endpoints and
includes their exact remaining halvings; it does not assume that a
partially divided common endpoint is already odd.

The known child source witness is **seven odd steps longer**, with total
exponent increased by 11. A returned child target witness reconstructs
the parent target by removing seven steps and 11 exponent units. The
decreasing integer `m` justifies this recursion even though source rank
increases. Every prefix guard holds throughout the displayed infinite
cell, and arbitrary terminal padding is preserved.

In particular this reaches parts of both previously uncovered rank-two
families: for first exponent 5 and `b=88+162j`, it applies exactly when
`j=1518 mod2187`, equivalently `b=246004 mod354294`; for first exponent
6 and `b=38+162j`, it applies when `j=1824 mod2187`, equivalently
`b=295526 mod354294`. Complete source witnesses at those enormous
exponents are reconstructed directly from the two supplied letters,
without attempting their target orbits. The other residue classes remain
open under this rule.

## Latest-source audit and the remaining statement

[LATEST_SOURCE_REVIEW.md](LATEST_SOURCE_REVIEW.md) records the further
updates read during this pass, including the newer PR146 head and
PR167–169. Exact source heads are frozen there. Their localization,
energy, arithmetic and certificate statements retain their stated
dependencies and open remainders. None is treated as an unproved premise
of the new direct witness identities.

[PRN-001](POSITIVE_RENEWAL.md) proves a necessary loss for a proposed
positive descent renewal. If positive rows with children below `ck`
retain unit mass on a set of density `beta` inside a domain of density
`delta`, their weighted column norm obeys
`K_s >= (beta/delta)c^(s-1)` for `0<s<1`, and `K_1 >= beta/delta`.
The application explicitly allows genuinely killed rows; their density
has not been bounded for the actual sparse-sieve algorithm. This is a
scoped norm theorem, not an exclusion of all renewal methods.

The first missing mathematical statement remains a successful transfer
for every complete source witness. The current least-failure argument
still permits arbitrarily long source words and unbounded rank-two
families. For example a rank-two word with first exponent 5 has
`b=88+162j`, and its target is equivalent to `2^(89+162j)-1`.
No universal convergence or descent for that entire residual family is
proved here. Allowing longer output witnesses does not remove that
obligation; all the present constructions already permit them.

## Files and replay

| File | Mathematical or executable scope |
|---|---|
| [REDUCTION_AUDIT.md](REDUCTION_AUDIT.md) | Source-qualified global equivalence; independently reconstructed cover; new exact height floor. |
| [DIRECT_R_WORDS.md](DIRECT_R_WORDS.md) | Complete first-letter normal forms and two unbounded word rewrites. |
| [LEAST_R_FAILURE.md](LEAST_R_FAILURE.md) | Least-failure height, first-letter and rank exclusions. |
| [R_BYPASS.md](R_BYPASS.md) | Partial affine descent atlas and unbounded conditional rank-decreasing family. |
| [SOURCE_ZERO_DESCENT.md](SOURCE_ZERO_DESCENT.md) | Strict direct-R parameter contraction with a longer child source witness. |
| [POSITIVE_RENEWAL.md](POSITIVE_RENEWAL.md) | Exact positive-column norm lower bound, with the nonempty-row qualification. |
| [LATEST_SOURCE_REVIEW.md](LATEST_SOURCE_REVIEW.md) | Frozen newest-source audit and interfaces actually used. |

Run the five standard-library replays from the repository root:

```sh
python -B research/witness-global-closure-20261121/check_reverse_cover.py
python -B research/witness-global-closure-20261121/check_direct_r_words.py
python -B research/witness-global-closure-20261121/check_least_r_failure.py
python -B research/witness-global-closure-20261121/check_r_bypass.py
python -B research/witness-global-closure-20261121/check_source_zero_descent.py
```

Repeat each command with `-O`. Explicit checks remain active with assertions
disabled. The replays establish exact finite identities, whole-progression
guards, finite complete witnesses and implementation controls. The written
proofs supply the unbounded quantifiers for the stated families. Neither
the replays nor repository validation proves universal `R`.

The [review and execution record](../../reports/2026-11-21-witness-global-closure/README.md)
keeps internal mathematical reviews and actual command receipts separate
from these scientific statements. No formal proof-assistant execution or
external referee acceptance is asserted.
