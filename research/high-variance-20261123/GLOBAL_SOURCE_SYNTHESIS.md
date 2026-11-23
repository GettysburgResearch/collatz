# Whole inverse clusters as a source-replacement attack

**Status: the closing argument failed.** This pass allowed the entire prefix
of the supplied complete certificate to disappear, replaced it with the whole
legal inverse language on gaps one through three, and allowed a new initial
even exponent. There is no bound on the replacement word length. The original
target and the original complete tail remain fixed.

The useful output is an exact finite-cut consequence of the joint source
minimum, together with the boundary identities of that cut. The proposed
next step was a coercive comparison between consecutive complete inverse
clusters. That comparison is false without further hypotheses. The control
below also tests the mechanism at an actual minimum-grade, maximum-source
interval, using the **complete** predecessor sets. Its target converges; it
does not satisfy the badness assumption of a `JointBadQuery`.

## 1. Sources and normalization

Use the shortcut map `T(n)=n/2` for even `n` and `(3n+1)/2` for odd `n`.
For positive odd integers use

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad
 I_a(v)=\frac{2^a v-1}{3}.
\]

An inverse is used only when its value is a positive odd integer. Then its
forward gap is exactly `a`. A complete word ends at one with every preceding
division legal. The complete grade is

\[
 \Gamma(e,W)=\bigl(\{2e+1\}\text{ if }e>0\bigr)
             \uplus\{2a:a\in W\}.
\]

The source of the joint minimum is PR177 at
`0444986571f09f302cb3687b4bba3552600e4119`,
`research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md`.
It supplies the original-target floor, minimum complete grade, the
maximum-source tie, and the full arbitrary-target lower-grade hypothesis.
Its `WITNESS_CLOSURE_CONTINUATION.md` already permits arbitrary carry lengths
and target-dependent suffix exits; it does not prove that they always succeed.

The preceding PR180 source is
`5e29f56f6d44669a8aa9134e5617b78d65c074c2`,
`research/retained-source-attacks-20261122/LEGAL_DESCENT.md`.
The current all-word reservoir in PR178 was read at
`7e4569476e152f6b8537bdc1711df595ec1ffd89`,
`research/whole-repo-synthesis-20261122/arithmetic/WHOLE_WORD_MERGER_ATTEMPT.md`.
PR176's `WHOLE_SOURCE_DEBT_ATTEMPT.md` was read at
`fdcb137214f4be8ac30dbb025d6eeb6568e22e2a` in
`research/lean-global-resolvent-20261121/overview/returns/`.

This note does not repackage the exponent-three reset. PR177's older
`MERGER_RETAINED_EVEN.md` and `lean/Collatz/RetainedEvenReset.lean`, at the
same current pin, already isolate the cells `q=7 mod9`, `q=19 mod27`, and
nonunits. The result below concerns a removed source prefix and its entire
replacement cluster. No external analytic theorem is needed for the arithmetic
arguments or the finite control.

## 2. A whole deleted prefix buys an entire inverse cluster

For a positive odd `v`, define the set of **ordinary sources**

\[
 \mathcal C_3(v)=\{x>0:x\text{ odd},\quad
   x\xrightarrow{V}v\text{ for some }V\in\{1,2,3\}^{*}\}.
 \tag{1}
\]

The empty word is included. The set is not defined by a prescribed depth,
peak, residue precision, or grammar approximation.

Suppose a supplied complete bounded-four source word splits as `W=P++R`,
the actual prefix `P` ends at `v`, and `P` contains a gap four. For every
`x` in (1), append the **literal** complete tail `R` to its actual word `V`.
For every new initial exponent `0<=f<=3`, this gives a complete powered
source `2^f x` with

\[
 \boxed{\Gamma(f,V\mathbin{++}R)<\Gamma(e,P\mathbin{++}R).}
 \tag{2}
\]

Cancel the common tail grades. At least one grade eight is removed from
`P`, and only grades at most seven are inserted: the new gaps give grades
at most six, and the new initial exponent gives a grade at most seven.
This proves (2) in the original multiset order, even when `V` is arbitrarily
long. No congruence needs to be transported through the deleted prefix.

Consequently a joint bad query at the unchanged target `t` forces

\[
 \boxed{x\in\mathcal C_3(v)\Longrightarrow16x+1<t,
 \qquad
 \mathcal C_3(v)\subseteq
 [1,\lfloor(t-2)/16\rfloor].}
 \tag{3}
\]

If `16x+1>=t`, choose `f=3` and apply the full original lower-grade interval
hypothesis to `t`. Thus every one of these grade-funded clusters is finite
under the bad-query assumption. This deduction applies at **each** literal
cut after a removed prefix containing a four. It does not presume that
arbitrary inverse clusters are finite.

The intended contradiction was to show that at least one such complete
cluster must cross the right side of (3). This would construct an actual
cheaper source, with no restriction on the replacement depth. The next
sections test that proposed global step.

## 3. Exact boundary identities, including the original root

Let `v>1` be a ternary unit with a supplied complete certificate to one,
and suppose `C_3(v)` is finite. The unit condition holds at the nonempty
forward cuts in Section2: the numerator `3n+1` and every power of two
are units modulo three. Its unit vertices form
`F=C_3(v) intersect {n:3 does not divide n}`. They are an ordinary rooted
tree: a repeated forward state before `v` would be a cycle preventing the
given arrival at one. This argument does not assume a general exclusion
of positive cycles.

The complete unit-child table is

| `n mod9` | Legal unit inverse gaps at most three |
| --- | --- |
| 1, 4 | 2 |
| 2 | 1, 3 |
| 5 | 3 |
| 7 | none |
| 8 | 1 |

For every function `f` on the finite tree,

\[
 \boxed{\sum_{n\in F}\left(f(n)-
      \sum_{\substack{1\le a\le3\\ I_a(n)\in F}}f(I_a(n))\right)=f(v).}
 \tag{4}
\]

Each nonroot vertex occurs exactly once in the inner sums. The root does
not. Let `N_r` count vertices of residue `r mod9`. Taking `f=1` gives

\[
 \boxed{N_7=N_2+1.} \tag{5}
\]

Taking `f(n)=n` gives an exact weighted boundary, rather than only an
average offspring count:

\[
\begin{split}
3v={}&3\sum_{n\equiv7(9)}n+
       \sum_{n\equiv8(9)}(n+1)
       -\sum_{n\equiv1,4(9)}(n-1)\\
    &-\sum_{n\equiv2(9)}(7n-2)
       -\sum_{n\equiv5(9)}(5n-1),
\end{split}\tag{6}
\]

with every sum restricted to `F`. The signs do not give an upper bound
on the cluster's largest source; large leaves and large branch vertices
can balance.

There is also an exact flow version. Suppose a nonnegative finite-valued
weight `nu` obeys the ordinary unit inverse equation

\[
 \nu(n)=\sum_{\substack{a\ge1\\ I_a(n)\text{ positive odd unit}}}
              \nu(I_a(n))
\]

on this tree. Summing over `F` and canceling the low-gap internal edges
gives

\[
 \boxed{\nu(v)=
 \sum_{n\in F}\,
 \sum_{\substack{a\ge4\\ I_a(n)\text{ positive odd unit}}}
       \nu(I_a(n)).} \tag{7}
\]

There are finitely many rows, each with finite sum, so this cancellation
does not subtract divergent quantities. The canonical reference may be
substituted only with its upstream existence qualifications; it is not
needed for (1)--(6).

Formula (7) was a possible route to forcing a missing source through the
cut. Its boundary, however, uses gaps **at least four**. Those are exactly
the grades removed to fund the replacement. Positive boundary mass does
not put a large source inside the cheaper cluster. It cannot be moved
across that grade boundary without another arithmetic construction.

## 4. The proposed adjacent-cluster coercivity is not uniform

One attempted next step compared the whole low-gap clusters at `v` and
at its gap-four parent `I_4(v)`. If the cluster before a four could not be
much larger than the cluster after it, (3) might contradict the supplied
large source. The following is a complete all-length obstruction to a
uniform numerical comparison on unrestricted complete sources.

Take positive odd `v=7 mod9`. Then

\[
 r=I_2(v)=(4v-1)/3\equiv0\pmod3,
 \qquad \boxed{\mathcal C_3(v)=\{v,r\}.} \tag{8}
\]

The only available initial gap is two, and its result has no odd
predecessor. Put

\[
 x=I_4(v)=4r+1,\qquad
 y=I_2(x)=\frac{16r}{3}+1=\frac{64v-7}{9}.
\]

For any `L>=1`, impose

\[
 3^{L+2}\mid80v-11. \tag{9}
\]

Then `5y-1=4(80v-11)/9` is divisible by `3^L`. Iterating the gap-three
inverse is therefore legal through `L` steps. Indeed

\[
 5I_3^j(y)-1=(8/3)^j(5y-1),
\]

and divisibility by three at the next step is exactly the required residue
`I_3^j(y)=2 mod3`. These are positive odd integer states. The resulting
source `z=I_3^L(y)` belongs to `C_3(x)` and satisfies

\[
 \boxed{z=(8/3)^L\left(y-\frac15\right)+\frac15
     >\frac{16}{3}(8/3)^L r.} \tag{10}
\]

The smaller cluster in (8) is complete, so (10) disproves every uniform
constant bound of the form
`sup C_3(I_4(v)) <= C max C_3(v)`, if no additional restriction is placed
on the root's supplied tail.

These can be made **complete convergent certificates**, not just rational
word shadows. Choose a positive integer `m` such that

\[
 4^m\equiv113\,80^{-1}\pmod{3^{L+3}},\qquad
 v=(4^m-1)/3.
 \tag{11}
\]

The powers of four enumerate all classes congruent to one modulo three
in this modulus. One elementary proof is
`v_3(4^(3^j)-1)=j+1`, by induction using the binomial expansion at the
next cube; hence the order is exactly `3^(L+2)`. The right side of (11)
is one modulo three. It is not one modulo nine, so a nonzero exponent
exists. Equations (11) imply (9), and hence `v=7 mod9`. Finally `v` has
the actual single gap `2m` to one. Thus

\[
 z\xrightarrow{[3]^L\,++\,[2,4,2m]}1
\]

is a complete positive ordinary certificate for every `L`.

**Boundary of this family.** Its terminal gap `2m` is large. It is not a
family of bounded-four joint counterqueries; the existing high-gap rules
already address that part of the source induction. The family refutes the
unrestricted cluster-coercivity idea, not every estimate restricted to the
canonical bounded-four domain.

## 5. A complete bounded-four, minimum-grade interval control

To test the canonical domain as well, the checker constructs **all**
positive odd sources whose first-hit word to one uses gaps at most four
and at most two occurrences of four. There are exactly

\[
 1+16+1354=1371
\]

such sources. This count has an all-length justification. With no four,
the only first-hit source is one. With one four, the last inverse step
away from one is `I_4(1)=5`, followed by the complete low-gap closure
`C_3(5)`. With two fours, the second gap four attaches at a unit of that
16-element set. The possible new roots are exactly

\[
 37,\quad69,\quad101,\quad133,\quad1093.
\]

Their complete low-gap closures have respectively `808,1,524,2,19`
vertices. They are disjoint because forward iteration and the first-hit
word are deterministic. The checker independently verifies closure under
**every** legal gap one, two and three, and replays every first-hit word.
Its node guard aborts rather than returning a censored answer.

The largest source is

\[
 q=184443431956737,
\]

and its literal word `W` has 24 ones, 28 twos, 32 threes and two fours.
It has 86 odd steps and ordinary clock 184. Its first 80 gaps lie in
`{1,2,3}` and end at 37, followed by the exact tail

\[
 37\xrightarrow4 7\xrightarrow1 11\xrightarrow1 17
 \xrightarrow2 13\xrightarrow3 5\xrightarrow4 1.
\]

Set `e=3`, `S=8q`, and `G=Gamma(3,W)`. Comparison with **every** source
in the complete two-four census and all four initial exponents gives

\[
\begin{aligned}
 \max_{\Gamma<G}S'&=1106660591740424,\\
 \max_{\Gamma=G}S'&=1475547455653896=S.
\end{aligned}\tag{12}
\]

Why does the finite census cover the entire grade comparison? A grade at
most `G` admits no gap above four, at most two fours, and no initial
exponent above three. Any complete certificate differs from its unique
first-hit word only by terminal gap-two padding at one. Such padding
strictly raises the grade and changes no source; it cannot increase either
maximum in (12). In particular a padded certificate of grade exactly `G`
whose first-hit grade is smaller has source at most the first maximum in
(12), which is strictly below the displayed same-grade maximum.

The target

\[
 t=2^{51}-1=2251799813685247
\]

satisfies

\[
 2\max_{\Gamma<G}S'+1<t\le2S+1,
 \qquad S+1<t,\qquad t\equiv3\pmod4.
\]

Thus this is a genuinely minimum-grade capturing certificate, with the
maximum-source tie at that grade. The actual source also has the
canonical complete tail, strictly contracting coefficients on every
nonempty odd prefix, and the original source floor: its maximum
positive-time shortcut value is `737773727826948`, below
`floor((t-1)/2)=1125899906842623`.

Yet deleting the whole prefix through the internal `37 -> 7` step gives
only the complete cluster `{7,9}`. Even the largest permitted new even
exponent yields a powered source at most 72, covering only targets at
most 145. This is a failure of the full cut replacement, with no hidden
bound on new word length.

**The missing badness hypothesis matters.** The chosen target first
descends at shortcut clock 138, to `2089005280842391`, and reaches one
at clock 384. Both are replayed exactly. This example is not a
`JointBadQuery`, does not refute `FloorIntervalStep`, and is not a new
large-range convergence theorem. It shows that the source minimum,
source maximum, floor and all-prefix contractions alone do not force
success of this complete-cluster replacement.

## 6. Exact stopping point

The global attempt removed the local-prefix integrality restriction and
all replacement-length limits. The original complete tail and the complete
grade were preserved. Under a genuine joint bad query, (3) produces actual
finite cuts and (4)--(7) evaluate their boundaries exactly.

I did not prove that one of these cuts must contain a source large enough
to capture the original target. Boundary positivity leaves its mass on
the grade-four-and-higher edges, and uniform adjacent-cluster coercivity
fails in the precise scope of Section4. The bounded-four control shows
why the structural source hypotheses alone do not supply the missing
capture. A successful continuation would need to use the actual target's
failure information to cross the cut, or construct a different legal
source whose full grade pays for that crossing. No such step is supplied
as an axiom or a purported proof.

Reproduce the exact control with:

```text
python research/high-variance-20261123/check_global_source.py
```

The frozen output is [global-source-control.json](global-source-control.json).
Normal and optimized Python runs produced identical output. These are
written arguments and standard-library integer checks; this lane adds no
Lean theorem and makes no kernel-verification claim for the infinite
cluster discussion.
