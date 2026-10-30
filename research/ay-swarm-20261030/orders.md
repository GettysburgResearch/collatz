# Boundary-sensitive orders and the single `ag` frontier

## Status and exact scope

**PROPOSED, with complete elementary proofs below and bounded independent
checks in `experiments/ay-swarm-20261030/orders.py`.** These are method and
normalization results, not a proof of Collatz. The published result that every
one-rule deletion of the Aaronson–Yolcu–Heule system terminates is prior work.
The contribution here is an explicit positional ordinal rank for one deletion,
an exact reset budget, and a concrete regular-language quotient on which to
search for richer orders. No claim of external priority is made for the
general rewriting lemmas.

The frozen external system is `emreyolcu/rewriting-collatz` at
`8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340`, `rules/collatz-T.srs`:

```text
ad -> d       bd -> gd
ae -> ea      af -> eb      ag -> fa
be -> fb      bf -> ga      bg -> gb
ce -> cb      cf -> caa     cg -> cab
```

On proper words `c {a,b,e,f,g}* d`, read digits from left to right starting
at 1: `a(x)=2x`, `b(x)=2x+1`, `e(x)=3x`, `f(x)=3x+1`,
`g(x)=3x+2`. The two rules ending in `d` implement the shortcut Collatz
map, stopped at 1; the other nine preserve the represented integer.
The all-word results below concern the literal string system, including
improper words. Proper-word restrictions are stated where used.

Sources: [Yolcu, Aaronson and Heule, *An Automated Approach to the Collatz
Conjecture*, arXiv:2105.14697v3](https://arxiv.org/html/2105.14697v3),
especially the interpretation definitions, mixed-base system and one-rule
deletions; [frozen rule file](https://github.com/emreyolcu/rewriting-collatz/blob/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340/rules/collatz-T.srs).
Local context: the current [rewrite frontier](../RESULTS_CATALOG.md#rewrite-termination-and-method-obstruction-frontier)
and [finite safety obstruction](../integrated/finite-safety-automata/README.md).

## O1. Total context-compatible orders are impossible

**Theorem.** There is no strict total well-founded order `>` on all finite
strings that is compatible with both left and right concatenation and orients
even the two rules

```text
bd -> gd,     cg -> cab.
```

**Proof.** Totality and context compatibility reflect `bd > gd` to `b > g`:
the alternative `g > b` would imply `gd > bd`. Similarly, `cg > cab`
forces `g > ab`. Therefore `b > ab`. Prefixing successively by `a` produces

```text
b > ab > aab > aaab > ...,
```

contradicting well-foundedness. Equivalently, the concrete two-step derivation
`cbd -> cgd -> cabd` defeats any order with the usual subsequence/simplification
property. The two-rule subsystem itself terminates; failure of this order
class is a property of proof representation, not evidence against Collatz. ∎

**Interpretation corollary.** No interpretation into one well-ordered carrier
can strictly orient every rule if every symbol acts as a strictly increasing
self-map and string comparison is pointwise. This includes natural scalar
polynomials with positive degree and nonnegative coefficients, and also
strictly monotone ordinal or finite lexicographic carriers of arbitrary size.

For clarity, pointwise comparison of functions need not be total, so this
corollary has its own direct proof. Every strictly increasing self-map `A` of
a well-order is inflationary. If a least `x` with `A(x)<x` existed, then
`A(A(x))>=A(x)` by minimality and `A(A(x))<A(x)` by strict monotonicity, a
contradiction. Write `A,B,C,D,G` for the interpreted symbols, using the
paper's function-composition convention. `CG(x)>CAB(x)` and strict
monotonicity of `C` imply `G(x)>A(B(x))>=B(x)` for every `x`; evaluating at
`D(y)` contradicts `BD(y)>GD(y)`. ∎

This does **not** exclude partial matrix orders, weakly monotone dependency
pair algebras, semantically labeled systems, orders only on a restricted
language, or direct rankings whose validity is checked on each contextual
rewrite. It explains why simply replacing natural numbers by larger ordinals
while retaining strict monotonicity of every symbol cannot fix the problem.

## O2. An explicit positional ordinal rank for ten rules

Let `W` be the system with just `ag -> fa` deleted. For any word `w` over
the seven symbols define nonnegative integers:

- `E(w)`: the number of `e` and `f` symbols;
- `F(w)`: the number of adjacent occurrences `cb` or `cg`;
- `A(w)`: the number of `a` symbols;
- `Q(w)`: sum, over every `b`, of one plus the number of symbols to its right;
- `J(w)`: the number of ordered pairs of positions carrying `a` and then
  either `e` or `f`.

Order the vector

\[
\rho(w)=(E(w),F(w),A(w),Q(w),J(w))\in\mathbb N^5
\]

lexicographically, with the leftmost differing coordinate decisive. Equivalently,
use the ordinal `omega^4 E + omega^3 F + omega^2 A + omega Q + J` below
`omega^5`.

**Theorem.** Every rewrite by `W`, in every pair of contexts, strictly decreases
`rho`. The omitted rule changes it by exactly

\[
\Delta(E,F,A,Q,J)=(1,0,0,0,\alpha),
\]

where `alpha` is the number of `a` symbols before that redex.

**Proof by exact contextual differences.** For a rewrite `u l v -> u r v`,
put `alpha=#a(u)`, `beta=#b(u)`, `epsilon=#e(v)+#f(v)`, `h=|v|`, and
`delta=1` if `u` ends in `c`, otherwise 0. Differences mean output minus input:

| Rule | Delta E | Delta F | Delta A | Delta Q | Delta J |
|---|---:|---:|---:|---:|---:|
| `ad -> d` | 0 | 0 | -1 | `-beta` | `-epsilon` |
| `bd -> gd` | 0 | 0 | 0 | `-(h+2)` | 0 |
| `ae -> ea` | 0 | 0 | 0 | 0 | -1 |
| `af -> eb` | 0 | 0 | -1 | `h+1` | `-epsilon-1` |
| `ag -> fa` | +1 | 0 | 0 | 0 | `alpha` |
| `be -> fb` | 0 | `-delta` | 0 | -1 | 0 |
| `bf -> ga` | -1 | 0 | +1 | `-(h+2)` | `epsilon-alpha` |
| `bg -> gb` | 0 | 0 | 0 | -1 | 0 |
| `ce -> cb` | -1 | +1 | 0 | `h+1` | `-alpha` |
| `cf -> caa` | -1 | 0 | +2 | `beta` | `2 epsilon-alpha` |
| `cg -> cab` | 0 | -1 | +1 | `beta+h+1` | `epsilon` |

Each row follows by counting the affected symbols, adjacent pairs, and
cross-context ordered pairs. The first nonzero entry is negative for all
ten `W` rows, and positive for `ag`. The lexicographic order on `N^5` is
well-founded, so `W` terminates on **all strings**. ∎

The rank is deliberately positional and boundary sensitive. Its comparison
on arbitrary pairs of strings is not a context-compatible reduction order.
For example `rho(g)<rho(ab)` but `rho(cg)>rho(cab)`. This is permissible:
the table checks all actual rule instances directly. There is no conflict
with O1 and no assumption that a solver may cancel boundary symbols.

## O3. A polynomial budget in the number of `ag` events

**Theorem.** Every finite rewrite sequence of the full eleven-rule system
starting with a word of length `L`, and containing `k` uses of `ag -> fa`,
has length at most

\[
54(L+k)^2+18(L+k).
\]

The sharper state-dependent bound below is preferable in an implementation.
This bound is unconditional, for arbitrary strings and arbitrary rewrite
schedules. It does not bound `k`.

**Proof.** Let initial values have subscript 0, and let `N_xy` count the
rule whose left side is `xy`. Exact symbol and pair balances from the table
give

\[
N_{bf}+N_{ce}+N_{cf}\le E_0+k=:D,
\]

\[
N_{cg}\le F_0+N_{ce}\le F_0+D=:C,
\]

\[
N_{ad}+N_{af}\le A_0+N_{bf}+2N_{cf}+N_{cg}
\le A_0+2D+C=:U,
\]

\[
N_{bd}+N_{bf}\le B_0+N_{af}+N_{ce}+N_{cg}
\le B_0+U+D+C=:V,
\]

where `B_0=#b(w_0)`. Only `cf` and `cg` increase word length, so every
intermediate length is at most `M=L+D+C`. In the `Q` balance, only
`af,ce,cf,cg` have positive contributions, each at most `M`; in particular
`beta+h+1 <= |u|+|v|+1 < |u cg v| <= M`. Hence

\[
N_{be}+N_{bg}\le Q_0+M(U+D+C)=:S.
\]

The only potentially positive contributions to `J` come from
`ag,bf,cf,cg`; their sum is at most `M(k+2D+C)`. Thus

\[
N_{ae}\le J_0+M(k+2D+C)=:R.
\]

Covering the eleven rule counts (with harmless slack because `V` also
bounds the `bf` count already covered by `D`) gives total length at most

\[
U+V+D+C+S+R+k. \tag{1}
\]

Writing `H=L+k`, we have `D<=H`, `C<=2H`, `U<=5H`, `V<=9H`,
`M<=4H`, `Q_0,J_0<=H^2`; therefore `S<=33H^2`, `R<=21H^2`.
Equation (1) gives the asserted bound. The empty-word case has no rewrites. ∎

**Consequence.** An infinite derivation must contain infinitely many `ag`
events; more quantitatively, there is no arbitrarily long computation with
bounded starting length and bounded event count. This re-proves one published
relative-termination consequence with an explicit budget, and isolates one
precise replenishment mechanism. It supplies no upper bound on the number of
replenishments for a fixed positive source.

## O4. A regular-language frontier and a ranking compiler

All left sides start in `{a,b,c}` and end in the disjoint set `{d,e,f,g}`.
There is therefore no proper overlap between two redexes. Two distinct
one-step rewrites commute in a single step, preserving the labels of both
rules. This proves the diamond property for the full system and for `W`.
Since `W` terminates, it has a unique normal form, denoted `N(w)`.

On proper words the `W` normal forms are precisely

```text
cd
or
c ((a|b)* a g (e|f|g)*)+ d.
```

To verify this grammar, a nonempty interior must start with a binary digit
(the `c` boundary rules forbid ternary digits), must end with a ternary digit
(the dynamic rules forbid final binary digits), and every binary-to-ternary
transition must be `ag`. These conditions are also sufficient.

Define a frontier edge by choosing any occurrence of `ag` in a normal form,
replacing it by `fa`, and applying `N` again. Both the domain grammar and the
normalization algorithm are exact and computable; O3 with `k=0` gives a
polynomial bound for each normalization call.

**Theorem (ranking compiler).** If a well-founded rank `r` on these normal
forms strictly decreases on every frontier edge, then the full system
terminates on proper words. Conversely, full termination gives termination
of the frontier relation.

**Proof.** Existing `ag` redexes cannot overlap any `W` redex and persist
through `W` normalization. Commuting each `W` step past such a redex gives
`N(w) ->ag z ->W* N(v)` whenever `w ->ag v`; uniqueness of `W` normal
forms supplies the final equality. Every `W` step leaves `N(w)` unchanged.
Consequently the lexicographic pair

\[
(r(N(w)),\rho(w))
\]

strictly decreases on every full step: its first coordinate decreases on
`ag`, and its second on `W`. The lexicographic product of two well-founded
orders is well-founded. The converse holds because every frontier edge is
a nonempty finite full derivation. ∎

This is a usable compiler criterion, not an existence claim for `r`.
Its advantage is that `r` only has to compare completely normalized frontier
words, and needs no context compatibility. Its first unsupported step is
constructing such an `r` for all frontiers.

### Deterministic three-symbol slice

From a binary starting word, `N(w)` uses only `{a,b,g}` internally. Choosing
the **leftmost** `ag` at each frontier preserves this property, so this
deterministic process stays in

```text
cd
or
c ((a|b)* a g+)+ d.
```

**Proof.** Initially `bd` creates only `g`, which can move left across `b`
but stops at `a`. At a frontier, the first `g` is preceded solely by binary
symbols. Applying the leftmost `ag` creates one `f` and no `e/f` occurs
elsewhere. During `W` normalization, that single `e/f` carrier either moves
left across binary digits, becomes `g` through `bf`, or is removed at `c`
through `ce/cf`. It cannot be trapped behind a pre-existing `g` to its left,
because no such `g` exists. No `W` rule increases `E`, so the resulting
frontier again has `E=0`. ∎

Moreover, a terminating derivation of this nonoverlapping string system
forces all derivations from the same word to terminate with the same length
and the same count of each rule. The elementary proof inducts on one
terminating derivation: any competing first step commutes with its first
step to a common successor; apply the induction hypothesis to that successor.
For a derivation of length one, a distinct redex would survive into the normal
form, which is impossible; length zero is immediate.
The two paths use the same two rule labels. Thus success of this deterministic
frontier strategy for every binary source would suffice; it is not necessary
to establish every possible frontier scheduling choice separately.

For the deterministic three-symbol frontier, each macro begins and ends
with `E=0` and has exactly one `ag`. Thus exactly one of `bf,ce,cf` occurs.
Also `F_0<=1` on a proper word, so `N_cf+N_cg<=2`. Every frontier macro
therefore increases string length by at most 2, although its represented
integer and the number of dynamic Collatz steps may increase substantially.
This bound is a restriction on the frontier grammar, not a global descent.

## O5. Administrative bursts have their own two-coordinate order

In the deterministic three-symbol slice, let `G(w)=#g(w)` and let `p(w)`
be the position of its first `g` (positions counted from zero).

**Theorem.** If `G(w)>=2`, its next leftmost frontier macro performs no
`ad` or `bd` rule, preserves the represented integer, and strictly decreases
`(G(w),p(w))` lexicographically. If `G(w)=1`, its next macro performs at
least one `ad` rule.

**Proof.** Write `w=c u a g v d` with `u` binary and the displayed `g`
the first one. When `G>=2`, the suffix `v` is nonempty, is already
`W`-normal internally, and ends in `g`. Replacing the displayed `ag`
leaves `c u f a v d`. The newly created `a` protects the entire suffix:
its pair with the first symbol of `v` is either binary/binary or `ag`,
and no `W` left side ends in `a`. All normalization therefore occurs
strictly to its left. In particular the final `gd` is untouched and no
dynamic rule can fire.

There is one `e/f` carrier to the left of the protecting `a`. It either
reaches `c` and disappears by `ce/cf`, or disappears by `bf` and leaves
one `g`. That `g` either disappears at `c` or stops at an earlier `a`.
In the first alternatives the total `g` count drops by one; in the last
it is unchanged and its first position strictly decreases. All rules
used are value-preserving conversion rules. If `G=1`, instead `v` is
empty and the new `ad` is a redex; it persists through all disjoint
normalization steps until used. ∎

Consequently every administrative burst ends at the single-`g` section

```text
c u a g d,     u in {a,b}*.
```

It is impossible for an infinite derivation to hide in the conversion
bursts between visits to this section. Its values are exactly `6m+2`
for positive integers `m`; the word `cu` is the canonical binary word
for `m`. Each value therefore has a unique single-`g` representative.
The next return to this section, or arrival at `cd`, is a total computable
operation: perform one single-`g` macro and then the finite administrative
burst. Totality of each return operation does not prove termination of its
iteration.
This gives a second, exact normalization layer: search for a return order
only after collapsing the bursts. It exposes an ordinary arithmetic
return section, related to the repository's earlier run/section programmes;
the collapse itself is not a new Collatz descent theorem.

## What this changes in the search

The full local rules cannot be handled by a total concatenation-compatible
order, however large its ordinal carrier. A concrete alternative is now
available: keep the five positional coordinates for free normalization, and
search for a partial or typed order on the regular `ag` frontier. The unresolved
condition concerns actual successive frontiers of one source, not finite
residue realizability or average digit drift.

The companion [carry analysis](carry-geometry.md) should be read when present:
the event `ag` has an exact digit/carry meaning, but one event can create
unbounded popcount debt. Therefore a constant credit per event is not
justified. Unbounded corridor lengths or an exact transported positional
profile must remain part of the state.

## Reproducibility and boundaries

The committed default run reports 35,739 exhaustive contextual rule checks,
2,000 longer random contexts, 781 proper mixed words normalized in two orders,
and 22,781 arbitrary-word prefix budget checks. Binary sources 1 through
1,024 generated 30,534 frontier edges and 184,308 literal rewrite steps;
all reached `cd` in that bounded test. For sources 1 through 128, leftmost,
rightmost, and frontier schedules gave identical counts for every rule.
Of the frontier edges, 18,202 were the value-preserving administrative type
and 12,332 started on the single-`g` section; all passed the O5 checks.
The maximum observed event count was 139 at source 937; this is only a
sample statistic.

Simple frontier orders already fail on exact small edges:

| Candidate statistic | Literal frontier edge | Failure |
|---|---|---|
| Length; binary count; multiset of binary-block lengths | `caggd -> caaagd` | length 5 to 6, binary count 1 to 3, block multiset `{1}` to `{3}` |
| Numeric value; `g` count; multiset of `g`-run lengths | `caagd -> caggd` | value 14 to 26, `g` count 1 to 2, run multiset `{1}` to `{2}` |
| Number of `ag` barriers | `cbabaggd -> cbagaagd` | one barrier becomes two |

Here each displayed arrow is one `ag` event followed by complete `W`
normalization, not a single literal SRS step. These examples retain actual
ordinary realization (sources 7, 9 and 27, respectively). They rule out the
listed single-statistic strict ranks, not all combinations or block orders.

Run from the repository root:

```text
python -X utf8 -B experiments/ay-swarm-20261030/orders.py
```

The accompanying script checks the exact difference table in bounded
contexts, checks the overlap condition, compares normalization strategies,
checks the frontier grammar and budgets, and retains failures of simple
frontier statistics. These are bounded software checks supplementing the
symbolic proofs above. Neither their range nor the global repository
validator is a proof of the missing frontier rank.

External one-deletion termination is attributed to the paper. The finite
experiment is not used to infer all-time Collatz termination. All ordinary
inputs are finite positive binary strings; no 2-adic completion is silently
treated as a positive integer.
