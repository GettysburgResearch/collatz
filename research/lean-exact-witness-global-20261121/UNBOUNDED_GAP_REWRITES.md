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

### Continuation: the same affine guard handles a low first gap

After the first unbounded checkpoint was published, the same guard U1
yielded a second, distinct source language. For every `j≥0,b≥4`,
`Collatz/LowGapPump.lean` proves

\[
 \operatorname{Certificate}(27m;(1,b)\Vert w)
 \Longrightarrow
 \operatorname{Certificate}
 (27p;(2^j,1,1,3,2,3,1,2,2,b-2)\Vert w),\tag{U11}
\]

where `2^j` in this word denotes `j` repetitions of the gap `2`, not one
exponent of value `2^j`. Every inserted exponent is strictly below `b`,
so replacing the removed pair `(1,b)` strictly decreases the same complete
graded multiset for every length `j`. The source length increases by `j+7`
and its total ordinary clock by `2j+12`, exactly as in the high-gap pump.

For the unadjusted second gap `b=4`, the child source word has length
`j+9`, total `2j+17`, and correction

\[
 C+3^{j+9}=155102\,4^j.
\]

The common partial source endpoint is `t=(243m+5)/32`. Parent target
`9m` reaches `t+1` along `(2,2,1)`. At `j=0`, the child target word is
`(3,1,1,1,1,2,2,1,4,1)`; each pump replaces its initial gap `v` by
`(1,v+1)`. Its correction is the child source correction plus
`2^(2j+17)`, proving the common target endpoint and all integer step
conditions. For general `b`, extend the final child source gap by `b-4`
and retain the entire original tail.

This handles the different binary cell `m≡25 mod32`. When the second gap
is exactly four, the odd endpoint further refines it to `m≡57 mod64`.
The ternary guard is still U1/U7; it has not disappeared. The comparison
wrapper `CollatzGapComparison.low_gap_pump_rule` places this family in the
same mixed induction. The independent affine replay generator is
[`unbounded_low_pump.py`](gap-search/high/unbounded_low_pump.py).

## 3. Arbitrary low-gap loops and an even-source reset compiler

### A universal handoff for every reverse-tripling first gap at least three

The continuation also obtained a rule with **no supplementary congruence
guard**. `Collatz/GapHandoffs.lean` proves that every certificate
`Certificate(3n,a::w)` with `a≥3` supplies an ordinary positive `p` with

\[
 3n=4p+1,\qquad
 \operatorname{Certificate}(p;(a-2)\Vert w),\qquad
 \operatorname{Basin}(n)\iff\operatorname{Basin}(2p+1).
\]

The same supplied tail is retained, and replacing `a` by `a-2` strictly
decreases the graded source multiset. This reduces the entire first-gap
branch to the fixed comparison type
`Hplus(p): Basin(p) → Basin(2p+1)`. It does **not** assert that all Hplus
queries close. For that type, the module proves source one directly,
consumes a first gap one into another Hplus query on the literal suffix,
and closes a first gap two by an ordinary merger. Larger Hplus gaps remain
part of the coverage obligation.

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

`Collatz/LowGapToPsi.lean` removes the need to treat forward tripling as an
unrelated auxiliary kernel. For any odd `u>1`, put
`s=T(u)=(3u+1)/2`. Then `3u=2s-1`. One ordinary source step gives the
actual certificate for `s`, with strictly smaller graded multiset, so
`Basin(u) → Basin(3u)` transfers to `Basin(s) → Basin(2s-1)`.
The source-one query is closed by the explicit certificate `[1,4]` for
three. `low_loop_to_psi` combines this step and the loop-prefix deletion
under the same original induction hypothesis.

The newly obtained `s` is `2 mod3`, whereas U9 below forces the symmetric
reset's parent known source `P/2` to be `1 mod3`. The asymmetric reset
proved later in this continuation supplies a compatible residue family.
Its guard still does not place every forward-tripling query inside a
proved reset family.

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

### An asymmetric reset on the residue reached by forward tripling

`Collatz/AsymmetricPsiReset.lean` proves a further arbitrary-length family
directly between psi-forward comparisons. Let `S=2^e q` with `e≥3` and
retain any supplied certificate for `q`. For any `j≥0` and integer `m`
satisfying

\[
 3^{j+13}(m-1)=4^j(2^{24}S-75116642),\tag{U12}
\]

the child source word is

\[
 (\underbrace{2,\ldots,2}_{j},
   1,2,2,3,1,3,2,1,2,3,2,3,e-1)\Vert tail.\tag{U13}
\]

It starts at `m` and ends at the identical `q` before continuing along the
entire original tail. The actual last gap is `e-1≥2`. Every inserted gap
is at most `e`, so the removed initial even-run grade `2e+1` pays for all
of them. The new prefix has `j+13` odd steps and total ordinary clock
`2j+e+24`.

The child target `2m-1` takes the word

\[
 (\underbrace{2,\ldots,2}_{j},8,
   \underbrace{1,\ldots,1}_{10},2,2,3)
\]

to `3S-1`. The parent target `2S-1` reaches this same endpoint in one
odd step. These are complete ordinary prefix identities. Thus the rule
proves

\[
 \operatorname{Basin}(2m-1)\iff\operatorname{Basin}(2S-1),
 \qquad \Gamma(0;\text{U13})\prec\Gamma(e;tail).
\]

The source correction satisfies
`C+3^(j+13)=75116642·4^j`; the paired target has one additional odd
step, total `2j+25`, and correction
`C_target+2^(2j+25)=6C+3^(j+14)`. These identities are proved for every
`j`, and the affine identity supplies the legality of every intermediate
division. `whole_witness_reset` and `apply_psi_rule` integrate the result
with the same complete comparison induction. `exponential_expansion`
proves `m>2^c S` whenever U12 holds at `j=3c`.

U12 forces `S≡2 mod3`, precisely the residue reached by the
forward-tripling handoff. A checked depth-zero guard is
`S=20136632=8·2517079`, `m=211899691`. The theorem remains conditional
on the supplied certificate for the odd part; this arithmetic fixture
does not silently assume any convergence result.

Coverage is explicit: for a given `j`, integrality requires

\[
 S\equiv75116642(2^{24})^{-1}\pmod{3^{j+13}}.
\]

These cells are **nested**, so increasing pump depth supplies longer
valid rewrites but no additional parent coverage beyond the depth-zero
cell. The generator
[`asymmetric_psi_reset.py`](gap-search/high/asymmetric_psi_reset.py)
combines this condition with the exact initial even valuation and
replays the source and target identities for an entire affine progression.

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
