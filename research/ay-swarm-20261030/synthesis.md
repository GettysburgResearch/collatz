# A guarded microscopic ordinal order and the remaining critical returns

**Status: PROPOSED, with a complete conditional-domain proof.**
This combines the two new positive ranks without identifying their different
clocks or assuming that their domains cover all integers.

## SYN-01: one explicit order on mixed representations

Let `s=c w d` be any proper AYH word, `n=Val(s)`, and write

\[
n=2^q m,\qquad m\text{ positive odd}.
\]

Use the two functions constructed in the companion notes:

\[
K(m)=\binom{\operatorname{popcount}(m)}2+\nu_2(m+1),
\]

and

\[
H(s)=\sum_{\text{ternary digit positions }j}
 \operatorname{bitlength}(\text{positive prefix value before }j).
\]

Define

\[
\mathcal R(s)=(K(m),q,H(s))\in\mathbb N^3
\tag{1}
\]

with lexicographic comparison, or the ordinal

\[
\omega^2 K(m)+\omega q+H(s)<\omega^3.
\]

Every coordinate is computed from the **current finite string**. No future
trajectory or stopping time enters the definition. The order is well founded
because it is a fixed finite lexicographic product of natural-number orders.

Let `P(n),M(n)` be the signed singleton-run counts in
[carry-geometry.md](carry-geometry.md), evaluated at an odd source. Define

\[
G(n):\quad P(n)<M(n)\quad\text{or}\quad
 [P(n)=M(n)\text{ and }\nu_2(n+1)\ge2].
\tag{2}
\]

**Theorem.** The rank (1) strictly decreases under:

1. every one of the nine value-preserving rules, including `ag -> fa`;
2. every even dynamic rule `ad -> d`;
3. every odd dynamic rule `bd -> gd` whose actual source satisfies (2).

These assertions hold in every proper mixed representation and under any
schedule. Moreover, for a nonterminal odd dynamic edge, (2) is exactly the
condition for (1) to decrease.

**Proof.** An auxiliary rewrite fixes `n`, hence `m,q`, and reduces `H`
by exactly one (SRS-01). On an even dynamic edge, `m` is unchanged and
`q` decreases by one, so the third coordinate is immaterial. On an odd
dynamic edge, the odd part of `T(n)` is exactly `U(n)`. By CG7, (2) is
equivalent to `K(U(n))<K(n)`, allowing both lower coordinates to reset.

For necessity on an odd edge, suppose `K(U(n))>=K(n)`. A larger value
increases the first coordinate. If it ties, the source has `q=0`, and
the output has `q>=0`. A positive output `q` increases the second coordinate;
if it is zero, SRS-02 increases `H` by `bitlength(n)-1>0`. Thus the
rank cannot decrease. The killed state `n=1` has no dynamic edge. ∎

This is a direct state-dependent ordinal ranking. It is not an interpretation
requiring every alphabet symbol to be strictly monotone on one well-order;
the total-order obstruction O1 therefore does not apply.

### Exact limitation

The guard is not universal. For example,

\[
9\longrightarrow_T14,\qquad U(9)=7,
\]

and `K(9)=2`, `K(7)=6`. Thus the microscopic odd edge raises the first
coordinate. The theorem proves termination of the guarded rewrite relation,
and therefore a full execution reaches 1 or encounters an excluded odd
source. It is not a proof that every full execution reaches 1.

## SYN-02: two complementary decompositions, with distinct clocks

The five-component rank `rho` in [orders.md](orders.md) decreases on all
rules except `ag -> fa`. Rank (1) decreases on all auxiliary rules, and
its exceptional edges are precisely the bad odd sources in (2). This yields
two concrete ways to locate the outstanding work:

| Description | Proved decreasing part | Remaining obligation |
|---|---|---|
| Literal SRS, positional `rho` | Every rewrite except `ag` | A rank across normalized `ag` returns |
| Proper words, ordinal `R` | All auxiliary and even rules; exact guarded odd sources | Repayment after an excluded odd source |

The ranks cannot be freely switched. A decrease in one can accompany an
increase in the other; a mode change needs its own common well-founded
budget. Merely covering every individual rule by one of two ranks is not
a termination theorem.

The `ag` count in CG5 is the count during a specifically normalized **single
odd arithmetic macro**. The frontier in O4 instead normalizes all ten other
rules, which can include several dynamic steps. These clocks are not identified.
Their exact connection is the literal SRS and the positive integer represented
at each boundary. Schedule-independent complete rule counts do not justify
substituting one partial-window count for the other.

## The best remaining order target

Let `W` omit `ag -> fa` and let `N` be its unique, polynomially computable
normalizer. Starting from a binary source, the deterministic leftmost-`ag`
strategy remains in

```text
cd  or  c ((a|b)* a g+)+ d.
```

The next rank should live on these **ordered blocks**, retain their exact
lengths and low-to-high carry state, and strictly decrease under an event
followed by complete `W` normalization. A rank for every frontier edge
automatically lifts through O4; a proof for the deterministic binary-start
strategy suffices through the nonoverlap/random-descent argument.

O5 further proves that every burst with at least two `g` symbols preserves
the integer and decreases `(#g, first-g position)` lexicographically. Such
bursts terminate at a single-`g` section `c u a g d`, representing `6p+2`
with `p=Val(c u d)>=1`. A single-`g` event performs at least one dynamic
halving. Therefore one may group a single-`g` event and the subsequent finite
administrative burst into a total computable section-return operation.
A rank for this induced iteration would suffice. The iteration's termination
is open; an equality with another programme's first-return map is not assumed.

Three proved obstructions constrain its form:

- O1 excludes the tempting total context-compatible or strictly monotone
  well-order interpretations.
- DAG-03 excludes all nonnegative additive digit costs even after exact
  complete-fibre minimization and the popcount/run tie breaker.
- CG8 shows that one critical event can create arbitrarily much popcount
  debt. Its carry interval must carry positional information; a fixed event
  credit does not suffice.

The exact run transducer supplies ordinary binary odd-macro transitions even
for symbolically huge run lengths. It does not directly evaluate an entire
section return; the distinction between these clocks remains part of the
proof obligation. The quotient DAG supplies complete finite representation
fibres when comparing alternative charts. Correlated state must survive any
pruning. The finite-chart exposed-winner criterion is a second concrete
global target, but the current published Example 4.3 chart has the proved
Fibonacci obstruction and cannot simply be patched by a polynomial penalty.

## SYN-03: each complete section return has a polynomial literal budget

For a proper word with `m` interior digits, the prefix before the `j`th digit
is less than `2*3^(j-1)<=2^(2j-1)`. Its bit length is therefore at most
`2j-1`. Summing over ternary positions gives

\[
H(s)\le\sum_{j=1}^{m}(2j-1)=m^2.\tag{3}
\]

Start from a single-`g` section word of total length `L`. Apply its one
`ag` event and normalize `W`. O3 bounds this by
`1+54L^2+18L` literal rewrites, and O4 bounds the resulting length by
`L+2`. If it is already terminal or single-`g`, the return is complete.
Otherwise O5's following administrative burst contains only auxiliary
rewrites. Each one, including `ag`, reduces `H` by one. Its starting word
has at most `L` interior digits, so (3) bounds this entire burst by `L^2`.

Thus the exact section-return operation uses at most

\[
\boxed{55L^2+18L+1}
\tag{4}
\]

literal SRS rewrites. This is a bound for one return computed from its actual
finite source. It neither bounds the number of returns nor asserts a decrease
of their lengths. It strengthens the constructive normalization interface
without inserting a hypothetical stopping-time oracle.

**First unsupported step:** no decreasing rank for all critical returns, and
no universally exposed winning family of charts, has been constructed.
Neither the new representation compiler nor the exact partial ordinal order
fills that gap. The work leaves a precise executable search problem and
reusable proved reductions, not a complete solution.
