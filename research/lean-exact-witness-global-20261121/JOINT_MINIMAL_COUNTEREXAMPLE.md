# One counterquery with the original target and source induction resources

## Result

`lean/Collatz/JointMinimalCounterexample.lean` proves a global reduction that
puts the existing source-grade induction and the new original-target floor
on **one and the same supplied source certificate**.

If any positive integer fails to reach one, `joint_counterexample` returns a
single `JointBadQuery` with all of the following properties:

\[
\begin{gathered}
t>1105,\qquad t\equiv3\pmod4,\qquad \neg B(t),\\
\forall,0<y<t,\quad B(y),\\
S=2^e q,\qquad 1\le e\le3,\qquad P\ne[],\qquad
\operatorname{Prefix}(q,P,11),\\
W=P\mathbin{+\!+}[1,2,3,4],\qquad
\operatorname{Certificate}(q,W),\qquad \forall a\in P,\ a\le4,\\
S+1<t\le2S+1.
\end{gathered}
\]

In addition, the same query carries:

- The **original full** `Hyp Interval (grades e W)`, including queries at
  arbitrary new targets, rather than only the fixed target t.
- A full arbitrary-target hypothesis for every strictly larger source at
  the **same** complete grade multiset.
- The ordinary source floor
  `∀k, T^(k+1)(S)≤floor((t−1)/2)`.
- Strict coefficient contraction of **every nonempty literal prefix** of W.

The selected source has minimum grade among all complete sources capturing
t, and then maximum numerical value among captures at that same grade.
The canonical tail is obtained by decomposing its original supplied word;
it is not selected independently and substituted afterward.

The checked closing statement is

\[
\boxed{\text{Universal Collatz}\quad\Longleftrightarrow\quad
       \operatorname{FloorIntervalStep}.}
\]

`FloorIntervalStep` is explicitly defined and remains unproved. The new
result justifies all of its simultaneous induction resources. It does not
assert universal target return or convergence.

`original_residue_iff_floor_interval` also connects this exact frontier to
the user's original certificate implication:

\[
x\in\mathcal E,\quad x\bmod512\in\{129,257,385\}
\quad\Longrightarrow\quad (x+1)/2\in\mathcal E.
\]

It composes the repository's already proved unrestricted-witness
`original_iff_collatz` with the new equivalence. It neither restricts the
available witnessing tuple nor imposes a bound on output certificate length
or exponents.

## 1. Least bad target, then minimum supplied source grade

Assume a positive counterexample exists. Ordinary strong induction supplies
a least one, t. Thus every positive y<t is already in the basin.

The existing canonical source-selection theorem supplies at least one
complete source whose interval contains t. Consider **all** complete
powered source certificates satisfying

\[
0<t\le2S+1.
\]

Well-foundedness of the existing grade order supplies a minimal grade among
these certificates. This uses exactly

\[
\Gamma(e;W)=
\bigl(\{2e+1\}\text{ if }e>0\bigr)
\uplus\{2a:a\in W\}.
\]

No restriction is placed on source size, word length, initial exponent, or
future target during this selection. `minimum_capturing_source` retains the
actual complete certificate that attains the minimum.

### Why the full old interval hypothesis follows

Suppose a child certificate has strictly smaller grade and an active query

\[
0<y\le2S'+1.
\]

If y were bad, target minimality would force `t≤y`. Therefore

\[
0<t\le y\le2S'+1.
\]

The very same child source would capture t at a smaller grade, contradicting
the choice of source. Thus y is in the basin.

This proves `original_interval_hyp`. It is precisely the repository's old
`CollatzGapComparison.Hyp Interval`; it does not impose `y≤t` or replace
that hypothesis with a weaker fixed-target version. A lower-grade carry
query may have a target larger than t and still use this hypothesis.

## 2. Maximum source at a fixed complete grade

The additional source tie is compatible with the preceding selection.
For every supplied complete powered certificate,

\[
S\le2^{e+\sum W}\le2^{\sum\Gamma(e;W)}.
\]

`source_grade_bound` proves this directly from the exact certificate
identity and the definition of the grade. Equal grade multisets have equal
sums, so the source values at the chosen grade form a nonempty bounded set
of natural numbers. Choose their maximum. This retains exactly the already
minimal grade, up to list permutation.

If a larger same-grade child source had a bad active target y, least-target
minimality would again give `t≤y`, and its source would also capture t. That
would contradict the chosen maximum source. Hence the source-value tie
provides another full arbitrary-target hypothesis:

\[
\begin{gathered}
\Gamma(S')=\Gamma(S),\qquad S'>S,\qquad
0<y\le2S'+1\\
\Longrightarrow\quad B(y).
\end{gathered}
\]

This is `original_same_grade_hyp`. `minimum_maximum_source` proves that the
minimum-grade and maximum-source choices hold simultaneously.

### Latest-source credit and immediate uses

PR180 at `ab3973099f0d285bbe88972382ad599bb02cd460`, specifically
`research/lean-joint-20261122/MIXED_COVER.md` and
`lean/MixedCoverAttack.lean`, supplies the source-ceiling insight and its
finite-defect induction. The present module proves the needed ceiling in
the core-only PR177 interfaces and realizes the same tie by bounded maximum
selection. It does not duplicate or import PR180's full induction framework.

For example, PR180's proved prefix permutation

\[
[3,4,2]\rightsquigarrow[2,3,4]
\]

retains the common endpoint and complete tail, raises the odd source from
q to q+4, and preserves the full gap multiset. At any retained initial
exponent, the powered source increases by `2^e·4`. Our same-grade hypothesis
therefore licenses this exact rewrite in the joint counterquery.

The same permission applies to PR180's written unbounded permutation

\[
[3],2^{[k]}[4,1]
\rightsquigarrow
[2,4],2^{[k-1]}[1,3],\qquad k\ge1,
\]

whenever its displayed physical source construction is supplied. That
written family is not relabeled as a newly formalized theorem here. The
joint selection supplies its missing recursive permission without changing
the rank of the original query.

## 3. The source floor follows for this same witness

Put `L=floor((t−1)/2)`. Suppose an ordinary source state at positive clock k
were above L. It would capture t, since `t≤2T^k(S)+1`.

The endpoint is above the terminal 1,2 cycle. The existing
`SourceOrbitProgress.advance_certificate` therefore obtains its complete
certificate by successive ordinary steps of the **original supplied
witness**, with a strict grade drop. The original interval hypothesis would
then prove B(t), a contradiction.

Consequently

\[
\boxed{\forall k\ge0,\qquad T^{k+1}(S)\le L.}
\]

`bad_query_floor` proves this statement. It needs the bad query and its full
interval hypothesis; it does not invoke the earlier independent cofinal
floor selector again. This distinction prevents a witness reset from being
mistaken for a valid recursive move.

The source-floor return theorems from `RootedSourceFloor` now apply to this
same selected source. In particular, an actual target return to `z≤3v+2`
at any odd literal source endpoint v lies below the **original** t.
An interval return using padding paid by the just-consumed source gap is
also a strict original-target descent. Earlier carry endpoints may have
been larger than t; they are not used as the induction reference.

## 4. Canonical normalization uses only already proved rules

The original interval hypothesis eliminates every high gap at least five,
every initial exponent at least four, odd initial sources, and the near
boundary `t≤S+1`. Least-target minimality eliminates even t and `t=1 mod4`
by their ordinary one- or two-step descents.

The bounded-four normal form then decomposes the selected supplied word.
The fixed terminal motifs close by the existing kernel-proved terminal
base. Positive terminal gap-two padding would permit deletion at strictly
smaller grade, so it cannot occur in a bad query. An empty prefix to 11
likewise lies in the proved terminal base. The original word must therefore
be exactly `P++[1,2,3,4]` with nonempty P.

No finite verification threshold is enlarged here: the module reuses the
already proved terminal range to obtain `t>1105`.

There is also an all-prefix restriction. If any nonempty literal prefix B
had `2^(sum B)≤3^(length B)`, its positive affine correction would force the
actual source endpoint to exceed the starting odd source. Deleting that
prefix while retaining the initial even exponent gives a larger source at
a smaller grade, capturing the unchanged target. Thus every nonempty
prefix satisfies

\[
\boxed{3^{|B|}<2^{\sum B}.}
\]

This is `bad_query_prefix_contracts`, and the complete restriction is stored
in `JointBadQuery`. It does not assert that strict contraction forces a
target return.

## 5. Exact remaining obligation

`FloorIntervalStep` asks for convergence only on the canonical nonempty
prefix-to-11 domain, with all of these supplied resources:

1. Every positive target smaller than the original t converges.
2. Every active query at a strictly smaller complete source grade succeeds.
3. Every active query from a strictly larger source at the same grade succeeds.
4. Every future ordinary state of the selected source is below the original
   target floor.
5. Every nonempty literal source prefix has a strictly contracting coefficient.

The statement does not assume that t is bad. The theorem
`collatz_of_floor_interval` shows that proving this restricted step would
contradict every possible `JointBadQuery` and establish full Collatz.
`collatz_iff_floor_interval` proves the exact equivalence.

The remaining task is a complete target-dependent return or descent cover
on this domain. The module does not combine unrelated well-founded orders,
extract an uncontrolled witness for a returned target, or infer successful
return merely because a finite source word has been consumed.

## Verification

The module uses core-only Lean 4.34.1 and imports the existing
`RootedSourceFloor` and `SourceOrbitProgress` modules. Its sixteen public
theorems are checked with warnings treated as errors and audited separately.
All proofs use ordinary kernel elaboration; there is no `sorry`, new axiom,
`native_decide`, or assumed global coverage theorem.
