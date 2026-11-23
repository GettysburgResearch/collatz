# The full ordinary pressure maximum and the cost of an integral word repair

Date: 2026-11-23.

**Status: written deductions at the actual escaping component, with a Lean
check of the finite repair inequalities. No escape exclusion or complete
Collatz proof.** This attack combines the full ordinary component minimum
with the newly available pressure maximum. It proves that the maximum can be
taken over **all** positive odd members of the component, including multiples
of three. It also obtains an unrestricted lower bound on the span of a
same-length, same-clock integral word repair. Neither a gap alphabet nor the
depth of the supplied word is bounded.

The closing construction attempted here was to contradict the maximum by
changing the actual forward word into another legal word with the same
coefficient and a smaller positive initial integer. The required arithmetic
change must be nonlocal: a repair beginning after `i` odd steps must replace
more than `1.7095 i + 2.7095` odd steps. The missing step is to construct such
a nonlocal repair, or a coefficient-improving ancestor, for every hypothetical
escaping component. The bound does not construct either one.

## 1. Sources and normalization

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\]

and its positive odd acceleration

\[
U(n)=(3n+1)/2^{a(n)},\qquad a(n)=v_2(3n+1)\ge1.
\]

The following heads were read directly.

| Source | Use in this attempt |
|---|---|
| PR182 `b78819e95ee7d39f02022de991b42217821e7590`, `research/closure-round2-20261123/SOURCE_CLOSURE.md` | The single pressure maximum, its coefficient identities and its original unit-domain restriction |
| PR177 `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`, HE2 | The elementary escaping-orbit count and positive product |
| Same PR177 head, `HIGH_VARIANCE_WITNESS.md` | Complete finite source boundary and the fact that a source optimizer alone does not force target entry |
| PR178 `4e204f54136c79cf8c9393b34e3330594f99ae0a`, `research/global-closure-20261123/duality/TRIADIC_RANK.md` | The full triadic-dual rank and its missing candidate construction |
| Same PR178 head, `ORDER_CONSTRUCTION_ATTEMPT.md` | Limits of direct strictly monotone ordinal interpretations |
| PR146 `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/{LEAST_FAILURE_SIEVE,THREE_RAY_ONE_SIDED,THREE_RAY_SMALLER}.md` | Actual least-failure and directed tripling reductions; no uniform ordinary meeting clock is assumed |
| Published PR180 base `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, `research/deep-machinery-20261122/ARITHMETIC_RIGIDITY.md` | Prior whole-prefix splice and bounded-gap sibling-repair restrictions; the new bound below has a different same-endpoint hypothesis and no bound on edited gaps |

Let `E` be the **whole positive odd eventual-meeting component** of one
hypothetical escaping positive integer. Every trajectory in `E` is injective.
The set includes odd multiples of three that feed into its unit part. If the
original integer `t` is the least nonconvergent positive integer and its
component escapes, then `t` is odd and `min E=t`. A nontrivial periodic
component is not covered by the positive-product argument.

## 2. Extending the maximum to all ordinary odd sources

For every `n in E` put

\[
\Lambda(n)=\prod_{j\ge0}\frac{3U^j(n)}{3U^j(n)+1},
\qquad r(n)=\Lambda(n)/n.
\tag{1}
\]

The elementary HE2 proof applies unchanged to the set of odd states of this
trajectory: its cylinder count uses positive odd sources, exact valuations,
and injectivity; none of those steps needs `3` not to divide the initial
source. Alternatively, the sole possible initial multiple of three has a
unit image, so positivity follows directly from the unit construction.
Consequently

\[
0<r(n)\le1/n,\qquad 2^{a(n)}r(n)=3r(Un).
\tag{2}
\]

As in PR182, choose any `p in E`. Every `n>1/r(p)` has `r(n)<r(p)`.
There are therefore finitely many candidates for a global maximum. Choose
the **least ordinary integer** `m` attaining that maximum, now on all of `E`.
This is a new selection on the enlarged domain, not a claim that the
previous unit maximizer remains maximal.

Every actual nonempty forward odd prefix from `m`, of length `h` and total
gap `A`, obeys

\[
2^A<3^h.
\tag{3}
\]

Every actual nonempty incoming odd prefix ending at `m`, from **any**
positive odd source, obeys

\[
3^h<2^A.
\tag{4}
\]

Both statements follow by telescoping (2) and comparing with the same
maximum. Equality is impossible for nonempty positive-gap paths.

In particular `a(m)=1`, so `m=3 mod 4`. If `m=2 mod 3`, its positive odd
parent `(2m-1)/3` is now in the domain, even when that parent is a multiple
of three. Its weight is `3r(m)/2`, a contradiction. Thus

\[
\boxed{m\bmod12\in\{3,7\}.}
\tag{5}
\]

This does **not** invalidate PR182's unit residue class `23 mod 36`.
That unit root can have a larger incoming atom at a ternary leaf, which the
unit optimization did not include. For the enlarged optimization, the
remaining alternatives are a maximizing ternary leaf (`3 mod 12`) or a
unit maximum (`7 mod 12`). Neither is eliminated here.

The same elementary count and component floor `t=min E` also give

\[
t\le m\le t\exp\!\left(\frac{160}{3}t^{-1/40}\right).
\tag{6}
\]

The selected `m` need not equal `t`. In particular one must not silently
give `m` the assertion that all smaller positive integers converge.

## 3. What the maximum forces at every future state

Write the actual first `k` odd steps as

\[
2^{A_k}q_k=3^k m+C_k,\qquad C_k>0\quad(k>0).
\tag{7}
\]

Any other positive odd source `n` reaching that same `q_k` in `h` odd steps
and clock `B` belongs to `E`. Equation (2) gives the complete incoming
coefficient barrier

\[
\boxed{3^h2^{A_k}\le3^k2^B.}
\tag{8}
\]

Equality forces `h=k` and `B=A_k` by unique factorization. Then `r(n)=r(m)`
and the least-maximizer convention gives `n>=m`. If the competing word has
correction `C`, its exact endpoint identity gives

\[
n=m+(C_k-C)/3^k,\qquad C\le C_k.
\tag{9}
\]

Thus the actual word maximizes the affine correction among **all legal
positive-source words with the same endpoint, length and total clock**.
There is no cutoff on a competitor. The tempting next step is to rearrange
some gaps to make a larger correction while preserving the source integer.
The following obstruction quantifies the cost of that actual repair.

## 4. Exact carry range for an arbitrary positive-gap window

For a word `W=(a_1,...,a_l)` of positive gaps, let

\[
B=\sum a_j,\quad s_0=0,\quad s_j=a_1+\cdots+a_j,
\quad C(W)=\sum_{j=0}^{l-1}3^{l-1-j}2^{s_j}.
\tag{10}
\]

Its physical affine identity is `2^B y=3^l x+C(W)`. Every `C(W)` is odd.
For fixed `l>=1` and `B>=l`, the minimum puts all excess clock in the last
gap, and the maximum puts it in the first gap. Indeed

`j<=s_j<=B-l+j` for `1<=j<l`, and both endpoints can be attained
simultaneously. Therefore

\[
C_{\min}=3^l-2^l,
\]

\[
C_{\max}=3^{l-1}
 +2^{B-l+1}(3^{l-1}-2^{l-1}),
\]

\[
\boxed{C_{\max}-C_{\min}
 =2(2^{B-l}-1)(3^{l-1}-2^{l-1}).}
\tag{11}
\]

These are bounds for the full positive-gap language. Some extremizing
words may fail integrality at a specified endpoint; using the whole language
only enlarges the available range and keeps the necessary bound valid.

## 5. An integral repair beginning late must also end late

Take an actual forward word from the maximum `m`. Keep its first `i` odd
gaps unchanged. Replace its next `l>=1` gaps by another positive-gap word
of the **same length and the same total `B`**. Keep any later suffix
unchanged. Require the new complete word to reach the same endpoint from
a different positive odd integer `n`.

Let `A_i` be the total clock in the unchanged prefix, and `C,D` the old
and new window carries. Composition of the three affine pieces gives

\[
\boxed{n-m=2^{A_i}(C-D)/3^{i+l}.}
\tag{12}
\]

The common later suffix cancels completely. Since both initial sources
are integral, `3^{i+l}` divides `C-D`; since the carries are odd, the
nonzero difference is a multiple of `2*3^{i+l}`. Combining with (11),

\[
\boxed{
2\,3^{i+l}\le |C-D|
\le2(2^{B-l}-1)(3^{l-1}-2^{l-1}).}
\tag{13}
\]

In particular,

\[
\boxed{3^{i+1}<2^{B-l}.}
\tag{14}
\]

This lower bound on the number `B-l` of even steps inside the window uses
no bound on any individual edited gap. But the actual prefix from `m`
still obeys (3):

\[
2^{A_i+B}<3^{i+l},\qquad A_i\ge i.
\tag{15}
\]

Multiplying (14) by `2^{i+l}` and using (15) gives the entirely integral
necessary condition

\[
\boxed{2^{i+l}<3^{l-1}.}
\tag{16}
\]

Writing `alpha=log_2 3`, this is

\[
\boxed{l>\frac{i+\alpha}{\alpha-1}
       =1.7095\ldots\,i+2.7095\ldots.}
\tag{17}
\]

It excludes every nontrivial same-clock adjacent-gap swap, and every
bounded-span same-clock window repair sufficiently far from the initial
source. A sparse repair is not excluded: its first and last edited positions
define a long window that may retain many internal gaps. Nor does this
argument exclude changed total clocks, changed odd counts, changed endpoints,
or a completely nonlocal construction.

## 6. Where the full attempt stops

For a fixed finite word, one can test whether a same-coefficient competitor
has larger carry and a positive integral source. The intended global argument
needs to prove that **some** actual forward prefix of the selected maximum
always has such a competitor, or has an incoming path violating (8).
No such all-prefix construction was obtained.

The finite source optimizer of PR177 does not produce it: that optimizer is
defined even for convergent targets, whereas (3), (8), and (9) use the actual
hypothetical escaping component. The triadic-dual rank of PR178 would finish
the original target once its complementary rational trajectory was
constructed, but neither the enlarged pressure maximum nor the congruence
(12) supplies that trajectory. The generic monotone ordinal construction
blocked in PR178 likewise does not pay for this repair.

The first unsupported step is therefore explicit: existence of an integral,
positive, pressure-improving nonlocal comparison at one actual maximum root.
The new inequalities restrict a direct attempt to make that comparison; they
do not assert its existence or treat the restriction as a proof of convergence.

## 7. Formal scope

`lean/ArithmeticRepair.lean` checks the natural-number implications from the
explicit nonzero divisibility and full carry-range hypotheses in (13) to
(14), and then from the physical prefix coefficient bound to (16). It also
checks the integer span consequence `i+1<l`, a weaker convenient
corollary. The carry formulas, actual affine composition, full-domain pressure
selection and logarithmic form (17) are the written deductions above; they
are not promoted to Lean axioms or claimed fully formalized.

No historical theorem suite or bounded orbit census was rerun for this
argument. The only new formal inputs are the explicit finite arithmetic
premises shown in the declarations.
