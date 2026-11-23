# Every negative odd shadow has a bounded noncontracting prefix

**Status.** The finite selector and its complete physical positive-source
consumer are proved in core Lean4.34.1, with no Mathlib dependency and no
assumption about eventual negative Collatz behavior. The main source theorem
is `CollatzNegativeShadow.physical_negative_return`. The source-rank
composition described below uses the original complete witness and the
existing gap-multiset induction; it does not choose a replacement witness
with uncontrolled rank.

The complete rank consumer is also checked in
`lean/Collatz/SourceOrbitProgress.lean`:
`CollatzSourceOrbitProgress.negative_block_interval_rule`. Its only
recursive premise is the original `Hyp Interval` at the given source grade.

This is a different conclusion from binary-run occupation. It supplies an
actual larger known source after a nonempty supplied ordinary prefix, which
is the direction needed to preserve every target in the source interval.

## 1. Uniform finite selector for all negative odd integers

For an integer `m>0` with `m` odd, start the signed accelerated odd map at
`z_0=−m`. Write its exact gaps as

\[
3z_i+1=2^{a_i}z_{i+1},\qquad a_i\ge1,\qquad z_{i+1}\text{ odd},
\]

and put `A_0=0`, `A_r=a_0+⋯+a_(r−1)`.

### Theorem 1

Every such shadow has a nonempty prefix satisfying

\[
\boxed{1\le r\le3m,\qquad 2^{A_r}\le3^r.}
\tag{1}
\]

Moreover the ordinary clock of that prefix obeys the sharper bound

\[
\boxed{1\le A_r<2r\le6m.}
\tag{2}
\]

This applies to every positive odd `m`, regardless of whether the full
negative trajectory is periodic, unbounded, or has any other eventual
behavior. Only a finite trace of length `3m` is used.

### Proof of the finite selector

Every odd negative integer remains negative after the signed odd map:
`3z+1<0`, and division by its positive power of two preserves the sign.
Each next finite gap exists because `3z+1` is a nonzero even integer.
In particular, the fixed negative shadow `−1` is included and uses gap one.

For a prefix word `W` of length `R`, let `C_W` be its full affine
correction:

\[
C_W=\sum_{i=0}^{R-1}3^{R-1-i}2^{A_i},
\qquad
-3^R m+C_W=2^{A_R}z_R.
\tag{3}
\]

Since `z_R<0`, its correction is strictly bounded:

\[
C_W<3^R m.
\tag{4}
\]

Suppose (1) fails through `R=3m`. Then every nonempty prefix has
`2^{A_i}>3^i`; the empty prefix has equality. Each of the `R` summands
in (3) is consequently at least `3^(R−1)`. Therefore

\[
C_W\ge R3^{R-1}=m3^R,
\]

contradicting (4). This proves (1).

The formal proof avoids rational normalization. Its general inequality is

\[
\Bigl[\forall V\text{ prefix of }W,\quad3^{|V|}\le2^{A_V}\Bigr]
\quad\Longrightarrow\quad
|W|3^{|W|}\le3C_W.
\tag{5}
\]

It is proved by appending one final gap. The correction changes from
`C_V` to `3C_V+2^{A_V}`, so the prefix bound pays exactly for the new
term. Applying (5) to the full length-`3m` trace gives the contradiction
without any division.

For the selected nonempty word, `3^r<4^r=2^(2r)`. Combining this with
`2^{A_r}≤3^r` proves `A_r<2r`, yielding (2). Thus no extra
`ceil(log₂m)` term is needed in the final clock estimate.

### Formal statements

`bounded_negative_prefix` proves (1) directly for every positive odd `m`.
The stronger `noncontracting_prefix` extracts such a literal prefix from
**any supplied signed trace of length `3m`**. Its returned prefix retains
the corresponding signed endpoint and the exact original trace tail.
`noncontracting_clock_bound` proves (2).

## 2. A physical positive-source expansion with a finite guard

Let `n,u,D,m` be natural numbers with

\[
n>0,\qquad m>0\text{ odd},\qquad
n+m=2^D u,\qquad D\ge6m.
\tag{6}
\]

In particular, the actual positive source is `n=2^D u−m`, with a
sufficiently separated negative low block. There is no restriction on the
positive high block `u`; its oddness is unnecessary.

### Theorem 2

There is a nonempty exact odd-gap word `W` and a positive odd integer `n'`
such that

\[
\begin{gathered}
|W|\le3m,\qquad 2^{A_W}\le3^{|W|},\\
0<A_W<6m\le D,\qquad
T^{A_W}(n)=n',\qquad n'>n>2.
\end{gathered}
\tag{7}
\]

All endpoints and clocks in (7) concern the one original positive ordinary
source in (6). No semigroup multiplication or rational merger is substituted
for its ordinary path.

### Proof

Choose the negative prefix from Theorem 1. Its clock `A_W` is strictly
smaller than `D`, so the signed lift compiler gives an actual natural
prefix with endpoint

\[
n'=2^{D-A_W}3^{|W|}u+z_{|W|}.
\tag{8}
\]

This use of the compiler is slightly stronger than the small-magnitude
version used for binary-run occupation. Only the clock `A_W≤D` is needed
to make (8) an integer and compile the prefix. Positivity follows directly
from its complete affine identity

\[
2^{A_W}n'=3^{|W|}n+C_W>0.
\tag{9}
\]

Since `A_W<D`, the high term in (8) is even and the signed low endpoint is
odd. Thus `n'` is odd. Each intermediate boundary is likewise an actual
odd boundary, and the ordinary compiler proves exactly
`T^(A_W)(n)=n'`.

Because the word is nonempty, `C_W>0`. Equation (9) and its noncontracting
coefficient give

\[
2^{A_W}n' =3^{|W|}n+C_W
 >2^{A_W}n,
\]

so `n'>n`. Finally (6) forces `u≥1`. Since `D≥6m≥m+2` and `2^m>m`,

\[
n=2^D u-m\ge4\cdot2^m-m>3m\ge3,
\]

which supplies the required source lower bound. The Lean theorem only
exposes the weaker sufficient conclusion `n>2`.

`physical_negative_return` proves the full statement (7), retaining the
complete natural `Prefix n W n'` as well as its actual ordinary orbit
equality. The natural positivity, nonempty clock, odd endpoint, coefficient,
and strict source growth are all part of its checked conclusion.

## 3. Consumption of the original complete witness

Suppose an interval obligation has complete supplied source

\[
S=2^e n,\qquad\operatorname{Certificate}(n,\tau),
\qquad 0<t\le2S+1,
\]

and the odd part `n` satisfies (6). Theorem 2 gives an actual growing
odd prefix from `n` to `n'`.

It cannot pass through one before reaching `n'`: the ordinary orbit of
one stays in `{1,2}`, whereas `n'>n>2`. Therefore the complete supplied
witness cannot end before that prefix. Exact odd valuations are unique,
so the forced word occurs literally at its beginning:

\[
\tau=W\mathbin{+\!+}\tau',
\qquad\operatorname{Certificate}(n',\tau').
\tag{10}
\]

Equivalently, this can be checked by iterating `ordinary_step` on the
given complete powered certificate. All preterminal steps have a strict
original gap-multiset decrease; the final odd endpoint has initial even
exponent zero. Reattaching the unchanged parent even exponent `e` retains
the same strict comparison.

The new source `S'=2^e n'` is strictly larger than `S`. Its supplied
certificate removes a nonempty prefix while keeping the literal tail and
the original even run:

\[
\Gamma(e,\tau')<\Gamma(e,\tau),\qquad
0<t\le2S+1<2S'+1.
\tag{11}
\]

Thus the original interval induction hypothesis applies to the same
target `t` at the strictly smaller complete-source rank. This is the
existing `coefficient_interval_rule` mechanism, now with a finite selector
available uniformly for every separated negative odd low block.

The new formal consumer does not require a separate unproved prefix-uniqueness
claim. `advance_certificate` iterates the existing `ordinary_step` theorem on
the supplied certificate. `cycle_stays_small` rules out an earlier visit to
one. `odd_growth_interval_rule` proves that any positive-clock larger odd
endpoint captures the whole interval after the initial even grade is
reattached unchanged. `negative_block_interval_rule` composes this exact
certificate operation with Theorem 2.

The source is allowed to grow because the complete witness rank decreases.
There is no inference that `n'` is smaller as an ordinary integer, and no
replacement of the original induction budget by a new convergence witness.

## 4. Illustrative exact prefixes

These short instances illustrate the universal selector; they are not its
proof or a claimed exhaustive list.

| Initial negative shadow | Selected gaps | Odd events `r` | Clock `A` | Coefficient comparison |
|---|---|---:|---:|---|
| `−1` | `[1]` | 1 | 1 | `2≤3` |
| `−3` | `[3,1,1,1]` | 4 | 6 | `64≤81` |
| `−7` | `[2,1]` | 2 | 3 | `8≤9` |
| `−23` | `[2,1]` | 2 | 3 | `8≤9` |

For the second row, the signed trace first reaches `−1` and then repeats
its gap-one loop. The others show that neither convergence to `−1` nor
strict decrease of the negative magnitude is required. For example,
`−23→−17→−25`; its selected negative endpoint has larger magnitude than
the initial one, while the source coefficient has already become
noncontracting.

## 5. Scope of the advance

The finite negative selector is unconditional over **all** positive odd
magnitudes, with no finite debt alphabet and no terminal signed-orbit
assumption. Its positive-source application needs the actual guard
`n+m=2^D u` with `D≥6m`. An individual exact selected word can use the
sharper guard `D>A_W`; the uniform guard is supplied to make the theorem
independent of any future shadow search.

This gives a successful source-rank rule for an unbounded class of complete
witnesses and every target in their active intervals. It does not assert
that every unresolved source, or every future source reachable under the
proof policy, has such a negative low-block decomposition. Positive low
shadows have a different sign in (3) and do not satisfy this contradiction
argument automatically.

The remaining global step is coverage of a successful strict-rank rule.
The present theorem supplies a new finite mechanism that genuinely closes
its covered comparisons, rather than only forcing a complex intermediate
state or giving a total arithmetic transition with an unresolved terminal
case.

### Formal reproduction

```bash
lake env lean -DwarningAsError=true Collatz/NegativeShadow.lean
lake env lean -DwarningAsError=true Collatz/SourceOrbitProgress.lean
```

The nine public theorems are `negative_endpoint`,
`negative_correction_bound`, `correction_prefix_floor`,
`split_signed_trace`, `noncontracting_prefix`, `bounded_negative_prefix`,
`noncontracting_clock_bound`, `source_above_two`, and
`physical_negative_return`.

The four additional public grade-consumer theorems are `cycle_stays_small`,
`advance_certificate`, `odd_growth_interval_rule`, and
`negative_block_interval_rule` in namespace `CollatzSourceOrbitProgress`.

The only imported Collatz facts are the existing exact ordinary prefix and
complete-witness arithmetic. No theorem asserting eventual convergence of
the positive or negative map is imported as an assumption of the selector.
