# The universal extremal-source clock proposal is false

Date: 2026-11-22.

**Result:** even a globally largest complete powered source at a given
complete grade does not make every newly covered interval target descend
within that source's full physical clock. The counterexample is

\[
S=1092=4\cdot273,\qquad K=23,\qquad n=2047.
\]

The previous globally largest powered source at a strictly smaller grade
is `820`. The target is genuinely new:

\[
2\cdot820+1=1641<2047\le2185=2\cdot1092+1.
\]

Nevertheless, its first strict descent is at shortcut clock `58`, not
by `23`. This disproves the full-interval source-clock proposal. It does
not refute the narrower remaining psi-head-three proposal restricted to
`q=256j+173`, and it is not a Collatz counterexample.

## 1. Exact certificate policy

Use the repository's shortcut map `T`, `GapTrace`, `PoweredTrace`,
`sourceGrades`, and `GradeDrop` from
`research/whole-repo-closure-20261122/lean/vendor/WitnessSynthesis.lean`.
A complete powered source is

\[
S=2^e q,\qquad q>0,\qquad
\operatorname{GapTrace}(q,1,w),\qquad e\ge0.
\]

The complete grade list is

\[
g(e,w)=
\begin{cases}[]&e=0,\\[2e+1]&e>0\end{cases}
\mathbin{++}[2a:a\in w].
\]

Grade comparison uses multiplicities: at the largest grade whose count
differs, the smaller grade has fewer occurrences. Equality means equality
of all grade multiplicities, not literal word equality.

All complete certificates are admitted in the claims below, including
`e=0`, every possible initial even exponent, and any number of final
`1 -> 1` gap-two padding steps. There is no source-height cutoff,
word-length cutoff, restriction to an inverse subtree of eleven, or
selection of just one certificate per source in the maximality proof.

## 2. The two actual complete certificates

The odd source path is

\[
273\xrightarrow{2}205\xrightarrow{3}77\xrightarrow{3}29
\xrightarrow{3}11\xrightarrow{1}17\xrightarrow{2}13
\xrightarrow{3}5\xrightarrow{4}1.
\]

Thus

\[
w=[2,3,3,3,1,2,3,4],\qquad e=2,\qquad
K=e+\sum w=23.
\]

Let `G=g(2,w)`. Its nonzero grade multiplicities are

| Grade | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `G` | 1 | 0 | 4 | 1 | 2 | 0 | 1 |

Removing the first actual gap gives the complete certificate

\[
820=4\cdot205,\qquad
w_0=[3,3,3,1,2,3,4].
\]

Its grade `G_0=g(2,w_0)` differs from `G` only by having one occurrence
of grade four instead of two. Hence `G_0<G` in the exact `GradeDrop`
relation, with largest differing grade four.

## 3. Maximality among every complete certificate of grade at most G

The existing kernel-checked theorem `WitnessGlobal.single_four_language`
classifies the entire one-four complete language, with arbitrary final
gap-two padding. Its finite source set is

\[
\mathcal A=\{5,3,13,17,11,45,7,29,9,19,77,25,51,205,33,273\}.
\tag{1}
\]

The theorem is based on backward closure for all legal low-gap parents,
not a finite-depth enumeration. We use that established theorem in the
following written all-certificate argument.

Consider any complete certificate `(S',e',w')` whose grade is either
strictly below `G` or equal to `G` as a multiset.

1. **No grade above eight occurs.** Every multiplicity of `G` above
   eight is zero. A positive multiplicity there would make the new
   grade larger, so every gap of `w'` is at most four and `e'<=3`.

2. **There is at most one gap four.** Two gap fours would already exceed
   `G` at grade eight. If there is no gap four, all gaps are at most
   three; `WitnessGlobal.low_complete_is_one` gives `q'=1`. Consequently
   `S'=2^e'<=8` in this case.

3. **If there is one gap four, the initial exponent is at most two.**
   The grade-eight multiplicity is now equal to `G`. Initial exponent
   three would introduce a grade-seven occurrence while `G` has none,
   making the new grade larger. Thus `e'<=2`.

4. **The one-four language is exactly covered by (1).** Split the word
   at its unique gap four. Its remaining suffix has only gaps at most
   three, so `low_complete_is_one` makes the state immediately after
   that gap equal to one. Every complete low-gap trace from one to one
   consists of gap-two steps: apply `low_complete_is_one` to each
   remaining suffix and use `3*1+1=2^a*1`. Hence the complete word has
   the form `front ++ [4] ++ replicate r 2` with `front` low. The
   arbitrary-padding theorem `single_four_language` puts `q'` in (1).

It follows that `q'<=273`, and therefore

\[
S'=2^{e'}q'\le4\cdot273=1092.
\tag{2}
\]

The certificate in Section 2 attains equality. Thus **1092 is globally
largest over all complete certificates whose grade is at most G**.

## 4. Maximality at strictly smaller grades, including every padding

Only the possibility `q'=273,e'=2` can exceed `820` in (2): all other
members of (1) are at most `205`, and `q'=273,e'<=1` gives `S'<=546`.

The full gap word starting at `273` is forced up to its first hit on one:
it is exactly `w` from Section 2. Indeed, every intermediate source in
a complete `GapTrace` is odd. A nonempty next edge has positive gap and
therefore forces its source to be odd; the terminal endpoint is one.
Consequently each displayed gap is the full two-adic valuation of
`3q+1`, and the ordinary odd trajectory determines it uniquely.
After its first hit on one, the only possible additional complete edges
are gap-two padding. Every complete certificate of `273` therefore has
word

\[
w\mathbin{++}\operatorname{replicate}(r,2),\qquad r\ge0.
\]

At initial exponent two, padding zero gives exactly grade `G`.
Positive padding leaves every multiplicity above grade four unchanged
and raises the grade-four multiplicity from two to `2+r`, so its grade
is strictly larger than `G`. Neither case is strictly below `G`.

Thus every complete powered certificate at strictly smaller grade has

\[
S'\le820.
\tag{3}
\]

The complete `820` certificate in Section 2 has grade `G_0<G`, so the
bound is attained. **820 is the global maximum at all strictly smaller
grades**, including certificates with alternate initial exponents and
arbitrary allowed padding. No sorting convention in a record census is
used to establish (2) or (3).

## 5. Exact failure at the original queried target

The complete source reaches one in clock 23:

\[
T^{23}(1092)=1.
\]

The new interval target instead satisfies

\[
T^{23}(2047)=283763,
\qquad
\min_{1\le k\le57}T^k(2047)=2134>2047,
\qquad
T^{58}(2047)=1067<2047.
\tag{4}
\]

The full finite orbit through the first descent is

```text
2047, 3071, 4607, 6911, 10367, 15551, 23327, 34991,
52487, 78731, 118097, 177146, 88573, 132860, 66430,
33215, 49823, 74735, 112103, 168155, 252233, 378350,
189175, 283763, 425645, 638468, 319234, 159617, 239426,
119713, 179570, 89785, 134678, 67339, 101009, 151514,
75757, 113636, 56818, 28409, 42614, 21307, 31961,
47942, 23971, 35957, 53936, 26968, 13484, 6742,
3371, 5057, 7586, 3793, 5690, 2845, 4268, 2134, 1067.
```

The obstruction survives the strongest source selection suggested in
this attempt: there is no larger complete powered source at lower or
equal grade to invoke when the target fails to descend through clock
23. Such a source would contradict (2). This is the actual failure of
the proposed contrapositive, not merely a failure at a nonmaximal
certificate selected by a finite census.

## 6. Written and Lean scope

`ExtremalSourceClock.lean` imports the repository's `WitnessSynthesis`.
Its eight audited declarations check the two concrete complete
certificates, their literal `GradeDrop` comparison, the source clock,
the new-interval membership, the target value at the source clock, the
entire finite no-descent interval, and the first descending endpoint.
The all-word maximality proof in Sections 3--4 is written, using the
already kernel-checked one-four language classification. It is not
included in the eight new Lean declarations.

The failed assertion was the **universal interval** source-clock bound.
The narrower psi frontier, whose query is specifically `8q-1` with
`q=256j+173`, remains open after this counterexample. No bounded record
census is presented as a theorem, and no full Collatz claim follows.
