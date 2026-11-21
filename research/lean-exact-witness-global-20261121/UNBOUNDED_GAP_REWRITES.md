# Unbounded source-gap rewrites with one well-founded order

**Full Collatz and the original residue implication remain OPEN.** This
checkpoint removes the fixed insertion-length restriction from our source-gap
induction and constructs genuinely unbounded arithmetic rewrite families.
It does not assert a successful rule for every recursive obligation.

Use the ordinary shortcut map `T(n)=n/2` for even `n` and `(3n+1)/2` for odd
`n`. A supplied odd certificate is its entire positive exponent word, ending
at one. Its unchanged tail is preserved by the constructions below. The
source and target of a comparison are ordinary positive integers throughout.

## 1. Rank complete exponent multisets, without choosing a base

For finite lists `new, old`, declare `new ≺ old` when there is an exponent
`a` whose multiplicity decreases and every multiplicity above `a` is
unchanged. Equivalently, inspect the largest exponent at which the two
histograms differ. This is the usual multiset extension of the natural
order, expressed directly through multiplicities.

`Collatz/GapMultiset.lean` proves this relation well founded in Lean core.
For words with entries below `h`, their histograms form a finite nested
lexicographic product of natural numbers, highest coordinate first. A
decreasing word stays below the same `h`. Each initial finite word supplies
such an `h`, so no global bound on exponents or word lengths is needed.

Consequently one removed exponent `a` can pay for **any finite number** of
inserted exponents strictly below `a`. Arbitrary common prefixes and tails
cancel; permutations do not matter. More generally a nonempty removed bag
can pay for an inserted bag when each inserted exponent is below some
removed exponent. No assertion about an infinite output witness is used.

To include an even source `n=2^e q`, where `q` carries the supplied odd
certificate `(a_1,...,a_r)`, use the graded multiset

\[
 \Gamma(e;a_1,\ldots,a_r)
   =\begin{cases}\varnothing&e=0,\\\{2e+1\}&e>0\end{cases}
      \uplus\{2a_1,\ldots,2a_r\}.
\]

Every ordinary step before reaching one decreases this same multiset.
An even step decreases the initial even-run grade. An odd step removes
`2a_1` and, if `a_1>1`, inserts `2a_1-1`; the rest of the certificate stays
unchanged. In particular, ordinary source consumption and the longer
replacements below can share one induction.

The declarations `PoweredCertificate`, `ordinary_step`, `close`, `one_query`,
and `collatz_of_complete` retain actual full certificates. `Complete` is an
explicit, **unproved** coverage hypothesis. Well-foundedness alone supplies
no missing move. `Collatz/GapComparison.lean` additionally uses an arbitrary
pair `(known source, wanted target)` as the query type. This is necessary to
put reverse tripling, forward tripling, and the psi resets below into one
induction without silently treating different goals as interchangeable.

## 2. An arbitrary-length pump in the high-gap family

This construction concerns the directed comparison

\[
 R(m):\quad \operatorname{Basin}(27m)\Longrightarrow
                  \operatorname{Basin}(9m).
\]

Fix any `j≥0`. Choose positive integers `m,p` satisfying

\[
 \boxed{3^{j+7}p+554\,4^j=4096\,4^j m+81\,3^j.}\tag{U1}
\]

Suppose the supplied source certificate for `27m` begins with `a≥5`, so
`81m+1=2^a q` for the odd endpoint `q` represented by its remaining tail.
The new source word replaces that first exponent by

\[
 W_{j,a}=(\underbrace{2,\ldots,2}_{j},1,1,3,2,3,1,3,a-2).\tag{U2}
\]

It starts at `27p` and ends at the **same** `q`. Thus

\[
 \operatorname{Certificate}(27m;(a)\Vert w)
 \Longrightarrow
 \operatorname{Certificate}(27p;W_{j,a}\Vert w),\tag{U3}
\]

with the exact supplied tail `w`, however long it is and however large its
exponents are. Every new exponent is strictly below `a`, so the new source
certificate decreases in `Γ`, for every `j`.

### Exact source and target identities

For a gap word `v`, write `L(v)` for its length, `B(v)` for its sum and
`C(v)` for its standard affine correction. The unadjusted word `W_{j,5}`
satisfies

\[
 L=j+8,\qquad B=2j+17,\qquad C+3^{j+8}=48970\,4^j.\tag{U4}
\]

Changing its last exponent from `3` to `a-2` adds `a-5` to `B` and leaves
`C` unchanged. Substitution of U1 then gives the source prefix identity
in U3. Its ordinary legality follows from the positive-gap identity and
coprimality of powers of two and three; it is not inferred from sample
trajectories.

Set `t=(81m+1)/32`. The parent target `9m` reaches `9t+2` along
`(1,1,2,1)`. The child target `9p` reaches that same endpoint along

\[
 V_0=(3,1,1,1,1,2,2,1,1,1,3),
\]
\[
 V_j=(1,\underbrace{2,\ldots,2}_{j-1},4,1,1,1,1,2,2,1,1,1,3)
       \quad(j\ge1).\tag{U5}
\]

These words satisfy

\[
 L(V_j)=j+11,\quad B(V_j)=2j+17,\quad
 C(V_j)+3^{j+10}=702874\,4^j.\tag{U6}
\]

The common target endpoint may be even. The ordinary basin equivalence
includes all subsequent halvings. Hence `Basin(9p) ↔ Basin(9m)`, and a
solution of the strictly lower-ranked child comparison `R(p)` reconstructs
the original comparison `R(m)`.

### A finite selector for this infinite family

There is a precise guard, not a search over an unknown length. Put
`L=4096m-554>0`. U1 is equivalent to

\[
 j=v_3(L)-4\ge0,\qquad
 u=L/3^{j+4},\qquad 4^j u\equiv-1\pmod{27},
 \qquad p=(4^j u+1)/27.\tag{U7}
\]

This selector is a written integer-arithmetic consequence of U1; the Lean
rewrite theorem uses U1 directly. For each `j`, there is exactly one
residue class for `m` modulo `3^{j+7}`. Combining it with `m≡15 mod32`
gives an infinite progression of positive ordinary parents. Different
`j` have distinct exact valuations in U7, so their ternary cylinders are
disjoint. Their total ternary measure is

\[
 \sum_{j\ge0}3^{-j-7}=\frac1{1458}.
\]

This is the coverage of this particular infinite family within the
high-gap binary class. It is not a proportion of Collatz proved.

### Why the unrestricted multiset order matters here

Every member of this family has `p>m`. More precisely U1 gives
`3^j p>4^j m`, since `m≥1`. Thus its source expansion factors are
unbounded as `j` grows. Its new ordinary source clock is larger by exactly
`2j+12`, and its number of source gaps is larger by `j+7`. These claims
follow directly from U1 and U2; they are not termination heuristics.

For fixed `a`, the `j` copies of gap `2` eventually defeat every fixed
energy base `sum C^gap`, however large the fixed finite `C` is. They also
defeat source-height descent and source-clock descent. The largest changed
exponent is nevertheless always `a`, whose multiplicity drops by one.
The complete inherited tail cancels.

The theorems `whole_witness_rewrite`, `rewritten_sizes`,
`exponential_expansion`, `fixed_base_prefix_failure`, and `apply_reverse_rule`
are proved in `Collatz/HighGapPump.lean`. In particular, at `j=3c` the child
exceeds `2^c` times its parent, and at `j=C^3` the fixed-base prefix energy
inequality reverses. These are unbounded Lean statements.

The standard-library generator
[`gap-search/high/unbounded_pump.py`](gap-search/high/unbounded_pump.py)
constructs the exact progression for any requested `j≥0,a≥5` and replays
both affine paths for every parameter in that progression. It verifies
the actual parity and divisibility conditions at each step. The Lean
module is `Collatz/HighGapPump.lean`; execution receipts distinguish its
unbounded proof from the generator's selected replay indices.

## 3. Arbitrary low-gap loops and an even-source reset compiler

### Two unbounded low-gap loops

`Collatz/LowGapLoops.lean` treats every complete source word of the form

\[
 \operatorname{Certificate}
  (3n;(\underbrace{2,\ldots,2}_{k},3,
        \underbrace{1,\ldots,1}_{\ell},4)\Vert w),
 \qquad k,\ell\ge0.
\]

Peeling that prefix supplies the actual tail `Certificate(u,w)`. An exact
ordinary target prefix gives `Basin(n) ↔ Basin(3u)`. Thus a forward-tripling
query `Basin(u) → Basin(3u)` suffices to reconstruct the reverse-tripling
parent. The source rank decreases by consuming a nonempty prefix; `u` need
not be smaller than the parent. Both loops and every inherited tail are
quantified without a cutoff. Activation of that forward-tripling query is
explicit; its universal truth is not assumed.

### A compiler accepting any valid finite entrance

`Collatz/UnboundedGapReset.lean` starts from the broad reset of PR176 at
`ad9a0611d22b48c0fd0c1da31091179654ba31a9`,
`research/lean-global-resolvent-20261121/lean/Collatz/OddReset.lean`.
Its former ordinary-height argument needed loop depth at least seven.
The new graded source-exponent rank admits every depth `ℓ≥0`, and an
arbitrary entrance word satisfying the following exact identities.

Let `W,V` be positive-gap words of the same length `r` and total `B`, with

\[
 C(V)=2C(W)+3^r+2^B.\tag{U8}
\]

This is a checkable finite condition. Whenever the source entrance sends
`m` to `x`, the target entrance sends `2m-1` to `2x+1`. All intermediate
integer divisions are derived from the full polynomial identities.

Choose ordinary positive `m,w,P`, an arbitrary `ℓ≥0`, and `e≥3` such that

\[
 4\mid P,\qquad 2P=9\,3^\ell w+1,
 \qquad 3^r m+C(W)=2^B(2^{\ell+1}w-1).
\tag{U9}
\]

Assume every entry of `W` is at most `e`. From any supplied powered source
certificate `P/2=2^e q`, `Certificate(q,tail)`, the compiler constructs

\[
 \operatorname{Certificate}
 (m;W\Vert(\underbrace{1,\ldots,1}_{\ell},3,e)\Vert tail).
\tag{U10}
\]

The entire new prefix has gaps at most `e`. Its grades are at most `2e`,
strictly below the removed initial even-run grade `2e+1`, regardless of
its length. The target `2m-1` follows an ordinary path to `P-1`.
Consequently the child psi comparison reconstructs the parent psi comparison
in the same multiset order as the reverse-tripling pump.

The original entrance is `W=(1,2,5)`, `V=(6,1,1)` and needs `e≥5`.
A new entrance lowers that requirement to `e≥3`:

\[
 W=(1,2,1,2,1,2,3,3),\qquad
 V=(5,1,1,1,1,1,2,3).
\]

Here `r=8`, `B=15`, `C(W)=15397`, `C(V)=70123`, and U8 holds exactly.
At depth zero, one certified example transforms the known source
`358216=2^3·44777` into `1590267`, with the same supplied odd tail from
`44777`; the child target reaches the parent target `716431`. Source height
increases. The Lean theorem `low_depth_zero_reset` checks this instance;
`compiled_certificate_reset` proves the entire word-parametric construction.

The exit `(3,e)` still requires `e≥3` for this rank argument. Neither the
compiler's existence nor its two concrete entrances establishes a valid
entrance for every parent.

## 4. Interaction with the latest forward-section work

PR173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec` proves that every
ordinary positive orbit reaches an odd `x` for which

\[
 (d+1)(x-2^d)\le70\,2^d,\qquad d=\lfloor\log_2 x\rfloor.
\]

It also proves unbounded expansion at the first positive return. We
investigated transferring descent from the low offset `x-2^d` and using
the latest survivor moments to control subsequent returns. Neither
argument supplies complete descent: the offset can retain coefficient
growth throughout its available shared bits, and forcing a source to
visit a sparse set does not remove that source's fixed positive mass from
the survivor moment.

The induction domain also matters. A least failed ordinary source need
not itself be marked; its first marked iterate can be larger. A least
failed marked source supplies a floor only for smaller **marked** sources.
The present checkpoint uses neither of those invalid floor transfers.
It instead carries the actual known convergence certificate in every
recursive obligation, as U3 demonstrates.

## 5. Remaining universal obligation

The high-gap pump and the additional reset family do not cover every
source exponent pattern and every activated child. The low-gap cases,
uncovered ternary guards, and any finite entrance conditions must belong
to one complete sound dispatcher. No such dispatcher is proved here.

The generic mixed interface is `CollatzGapComparison.Complete`, with the
required psi or deep reverse-tripling pairs explicitly activated. The
specialized interface `CollatzGapMultiset.Complete` remains available for
the earlier comparison types. Proving a complete sound cover would finish
the full theorem through the existing Lean equivalence with the user's
increasing-exponent statement. No assumption that either cover exists has
been added to Lean.
