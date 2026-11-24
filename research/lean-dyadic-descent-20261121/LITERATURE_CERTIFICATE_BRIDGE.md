# A sharp limit on suffix-preserving certificate resets

## The result

The complete-certificate rank permits an arbitrarily long replacement word.
That freedom does not guarantee that the replacement source can remain large
enough for the wanted target. The new development proves a sharp, proportional
failure of this particular source-reset strategy.

For \(j\in\mathbb N\), put

\[
u=729j+7,\qquad q=3888j+37,\qquad S=4q=15552j+148.
\]

There is an exact odd edge \(3q+1=16u\). Supply any complete certificate
\(\tau\) for \(u\). Then \(4::\tau\) is a complete certificate for \(q\),
and the original powered source \(S\) has initial even run two.

**Sharp source bound.** For every natural child source \(S'\), every initial
even run \(e'\), and every finite inserted word \(W\), assume

\[
\operatorname{PoweredCertificate}(S',e',W\mathbin{+\!+}\tau)
\]

and

\[
\Gamma(e';W\mathbin{+\!+}\tau)<\Gamma(2;4::\tau).
\]

Then

\[
\boxed{S'\le M:=13824j+130,\qquad9S'+14\le8S.}
\]

The bound is attained: initial even run one and the inserted word
\([2,2,4]\) give exactly \(S'=M\). The original suffix is unchanged in
both the upper-bound theorem and the attaining construction.

There is **no length cutoff on \(W\)** and no bound on the length or entries
of the supplied suffix. In particular, an arbitrarily deep search for a
smaller-rank prefix cannot produce \(S'\ge S\) on these inputs.

`LiteratureCertificate.lean` contains the formal development. Its main
statements are `same_tail_source_bound`, `same_tail_bound_attained`,
`proportional_source_loss`, and `unbounded_certified_obstruction`.

The further theorem `no_uniform_forward_lookahead` rules out every fixed
number of direct forward target steps as a uniform repair of this
suffix-preserving strategy. Its sources and targets depend on the proposed
horizon. The explicit unbounded witnesses have a large gap in the preserved
suffix: this is not a theorem that every bounded-lookahead dispatcher fails
on an unbounded family already normalized to gaps at most four.

## Why the literature suggests this distinction

[Dershowitz and Manna, *Proving termination with multiset orderings*
(ICALP 1979)](https://www.cs.tau.ac.il/~nachumd/papers/LNCS/Multisets.pdf)
explain why replacing removed entries by any finite collection of smaller
entries still gives a well-founded order. Their framework proves termination
when actual computation steps decrease the rank. It does not create an
applicable computation step at every state. This is the distinction tested
here: the repository's rank is well founded, but its arithmetic source and
target conditions still need coverage.

[Applegate and Lagarias, *Density bounds for the 3x+1 problem I: Tree-search
method* (1995; linked author preprint dated December 1993)](https://websites.umich.edu/lagarias/doc/applegateI.pdf)
organize inverse trees using ordinary congruence classes and distinguish the
branches divisible by three. Their finite tree analysis motivates proving
an invariant for the entire restricted inverse language. We use that
approach after the certificate rank has imposed its exact restrictions on
the permitted gap words.

The displayed sharp bound is derived here for the repository's particular
rank and supplied-suffix interface. It is not stated as a theorem of either
external paper. No external analytic or computational result is imported as
a Lean axiom.

## Exact definitions and source pins

The shortcut map remains

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.
\end{cases}
\]

The module imports `CertificateBoundary.lean` from the previously verified
packet. That file's frozen SHA-256 is
`3cdedfd465939cf48528b8ee199d528a7d6d9f795b332470757ac0d96944d3c9`.
It supplies complete odd-gap certificates with terminal value exactly one,
their checked ordinary-orbit semantics, powered certificates, and the rank
definitions. Terminal-one cycle padding is permitted; first-hit minimality
is not assumed.

Those rank definitions reproduce PR177 at
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317`, in
`research/lean-exact-witness-global-20261121/lean/Collatz/GapMultiset.lean`:

\[
\Gamma(e;A)
 =(\,[2e+1]\text{ when }e>0\text{, otherwise }[]\,)
   \mathbin{+\!+}\operatorname{map}(2\cdot,A).
\]

At the highest grade whose multiplicities differ, the child must have fewer
occurrences. Direct cross-file equivalence with PR177's algebraic
certificate implementation remains the source-qualified correspondence
documented in `CERTIFICATE_BOUNDARY.md`. The new module works entirely with
the already checked inductive certificate interface.

## Step 1: keeping the literal suffix fixes the ordinary endpoint

A complete odd-gap word has only one ordinary source. This follows by
induction on the word: the empty word forces source one, and two certificates
with the same first gap and identical remaining word have equal first
endpoints and therefore equal sources.

Consequently, if a new certificate is \(W\mathbin{+\!+}\tau\), splitting
it at \(W\) produces a prefix ending at the original \(u\), not at a
freely chosen integer. The module proves this as
`certificate_unique` and `prefix_of_shared_suffix`.

This rules out an easy interface mistake: one cannot retain the written
suffix while silently replacing its actual ordinary source.

## Step 2: the whole lower-rank set has only two possible forms

The unchanged suffix cancels from the multiset comparison. What remains is

\[
\Gamma(e';W)<[5,8].
\]

The largest differing grade must be five or eight, because those are the
only grades present in the parent front. The resulting possibilities are:

| Decreased grade | Initial even run | Permitted inserted gaps |
|---|---|---|
| Eight | \(e'\le3\) | Every gap is at most three |
| Five, with eight retained | \(e'\le1\) | Exactly one gap four; all other gaps are at most two |

The formal `lower_rank_alphabet` uses the weaker budget "at most one four"
in its second conclusion, which suffices for the bound. Its proof also
derives that the multiplicity of four is exactly one in that case.

This exhausts every smaller rank, including words much longer than the
parent front and arbitrarily large proposed initial even runs. It is not
a chosen search grammar narrower than the rank condition.

## Step 3: ordinary integrality closes both restricted inverse trees

An inverse odd edge into \(v\) has the exact equation

\[
3z+1=2^a v,\qquad a>0.
\]

For \(u=729j+7\), gaps at most three permit only the inverse gap two:

\[
u\longleftarrow p=972j+9.
\]

The new node \(p\) is divisible by three, so it admits no further positive
odd inverse edge. Thus every prefix over gaps at most three has source
either \(u\) or \(p\), regardless of its proposed length.

For the second rank case, allow at most one gap four and all other gaps at
most two. The complete set of possible ordinary nodes is

| Node | Value | Permitted next inverse edge before the budget is exhausted |
|---|---:|---|
| Root | \(729j+7\) | Gap two to \(p\), or gap four to \(q\) |
| \(p\) | \(972j+9\) | None; divisible by three |
| \(q\) | \(3888j+37\) | Gap two |
| \(r_1\) | \(5184j+49\) | Gap two |
| \(r_2\) | \(6912j+65\) | Gap one |
| \(r_3\) | \(4608j+43\) | Gap two |
| \(r_4\) | \(6144j+57\) | None; divisible by three |

The gap-four branch uses the unique permitted four. Subsequent edges are
therefore restricted to gaps one and two. Their exact integrality conditions
force the displayed path. The alternative gap-two branch terminates before
the four can be used.

`lower_three_prefix` and `one_four_prefix` establish these as inductive
invariants for every finite word. The proof is therefore exhaustive at
arbitrary depth, rather than a statement that a finite search happened to
find no more nodes.

## Step 4: combine the rank and the ordinary source bounds

In the first rank case, the child odd source is at most \(p\) and its even
run is at most three. Hence

\[
S'\le8p=7776j+72.
\]

In the second rank case, the largest possible odd source is \(r_2\) and
the even run is at most one. Hence

\[
S'\le2r_2=13824j+130=M.
\]

The latter is the larger bound for every \(j\ge0\). Its achieving word,
read forward into the inherited suffix, is \([2,2,4]\):

\[
r_2\xrightarrow{2}r_1\xrightarrow{2}q\xrightarrow{4}u.
\]

The front grade replacement is

\[
[5,8]\quad\longrightarrow\quad[3,4,4,8].
\]

Grade eight is retained, grade five decreases once, and all newly added
grades are smaller than five. This verifies attainability in the same
complete-certificate order, with the same full suffix.

Finally,

\[
9M+14=8S.
\]

The positive correction 14 remains in the formal inequality. The gap is

\[
S-M=1728j+18.
\]

Thus these inputs cannot be repaired merely by accommodating a fixed
additive loss of source height. The loss grows proportionally with the
original source.

## Step 5: the obstruction has unbounded fully certified instances

Define

\[
h_m=729m+385,\qquad
j_m=\left\lfloor\frac{4^{h_m}}{2187}\right\rfloor.
\]

The exact closed congruences

\[
4^{729}\equiv1\pmod{2187},\qquad
4^{385}\equiv22\pmod{2187}
\]

give

\[
4^{h_m}=2187j_m+22,
\quad
3(729j_m+7)+1=4^{h_m}=2^{2h_m}.
\]

Accordingly, the root \(u_m=729j_m+7\) has the explicit complete tail
\([2h_m]\), and \(q_m=3888j_m+37\) has complete word \([4,2h_m]\).
The module checks the congruences by ordinary kernel reduction and proves
\(m<j_m\). No Collatz hypothesis is used to supply these certificates.

This proves that the source loss occurs for arbitrarily large fully certified
parents. The suffix in this particular unbounded witness family has a large
gap. It does **not** prove that infinitely many parents in the residual
alphabet \(1,2,3,4\) have the obstruction. Larger-gap rules can act on
that witness family's suffix if they are allowed to change it.

There is also a small fully low-alphabet instance: \(j=0\), \(u=7\), with
complete tail \([1,1,2,3,4]\). Then \(q=37\), \(S=148\), and the exact
maximum child source is 130. A wanted target 287 is within the original
interval ending at 297, but outside every such child interval, all of which
end at or below 261. This is a certificate-interface example, not a claim
that the target fails Collatz descent.

## Every fixed direct-forward horizon also fails uniformly

Fix an arbitrary proposed forward horizon \(K\), and put \(D=2^K\).
Choose the fully certified source with \(j=j_D>D\), using the explicit
family just proved. Set

\[
Q=\left\lfloor\frac{2S+2}{D}\right\rfloor,
\qquad n=DQ-1.
\]

The gap between the old upper boundary and the largest possible child
boundary is

\[
(2S+1)-(2M+1)=3456j+36>D.
\]

Ordinary quotient and remainder arithmetic therefore gives

\[
0<Q,\qquad 2M+1<n\le2S+1.
\]

The selected target is inside the original source's interval and outside
every smaller-rank child interval preserving the suffix. Moreover, it has
the exact shape \(2^KQ-1\). The previously checked `odd_run` theorem gives

\[
n\le T^t(n)\qquad(0\le t\le K).
\]

Combining this with the sharp child source bound proves

\[
\boxed{\forall t\le K,\quad T^t(n)>2S'+1}
\]

for **every** complete child certificate with the same suffix and smaller
full grade multiset, regardless of the inserted prefix length or proposed
initial even run. The Lean theorem includes the original powered source's
complete certificate and the positive target and interval bounds.

Thus no uniform finite horizon for direct target entry into a child interval
can complete this particular prefix-only strategy over its stated domain.
This does not rule out asymmetric common-future comparisons, in which a
smaller child target first rises before meeting the original target. It
also does not rule out a horizon depending without a uniform bound on the
source, nor a rule that edits deeper into the supplied suffix.

The quantifiers are essential: for each \(K\) the proof selects new ordinary
sources and targets. It does not construct one fixed target avoiding all
child intervals forever. The preserved tail here is again the large-gap
one-entry word from the explicit family. No infinite low-alphabet coverage
claim is inferred from these changing finite witnesses.

## Relation to the latest bounded-clock and physical-merger results

This is not presented as the repository's first bounded-clock obstruction.
The following later source heads were read before freezing this note.

**PR185: fixed affine marked covers.** At
`b8c8de2e6859df702eb93eb28197520258fa767f`,
[FIXED_AFFINE_MARKED_COVER_LIMIT.md](https://github.com/GettysburgResearch/collatz/blob/b8c8de2e6859df702eb93eb28197520258fa767f/research/literature-orbit-closure-20261121/FIXED_AFFINE_MARKED_COVER_LIMIT.md)
gives a written proof that a finite collection of fixed affine, fixed-clock,
strictly smaller marked-partner rules cannot cover every sufficiently large
marked source. It also treats unbounded marked families whose initial odd-run
length tends to infinity. Its hypotheses concern the affine form of the
partner, marking on both sides, and an actual common future. Our theorem
instead quantifies over every child in one complete-certificate rank ideal,
with no prefix-length bound and no marking assumption, but only tests direct
forward entry into the child's covered interval. Neither result is an
obstruction to all merger architectures.

**PR178: unequal-clock physical tail separation.** At
`be5696cc45a95ad1903802b08ba1dc3ebba66930`,
[PhysicalTailBarrier.lean](https://github.com/GettysburgResearch/collatz/blob/be5696cc45a95ad1903802b08ba1dc3ebba66930/research/literature-reframe-20261122/lean/PhysicalTailBarrier.lean)
proves that if \(A=3^rB\), \(r>0\), \(B\) is odd,
\(B>6^H\), and \(2^H\mid A+1\), then
\(T^a(A-1)\ne T^b(B-1)\) for all \(a,b\le H\).
Its ordinary rising-prefix form therefore excludes bounded continuation
clocks on both sides of the specified erasure pair. That is a genuine
unequal-clock nonmeeting statement. The present theorem covers all
lower-ranked children preserving a literal suffix, but does not exclude
such asymmetric common-future comparisons. The domains and conclusions
are different; neither is used as an unproved premise of the other.

**PR185: a positive variable-clock selector.** The same PR185 head's
[AL27_HALF_ROUTE.md](https://github.com/GettysburgResearch/collatz/blob/b8c8de2e6859df702eb93eb28197520258fa767f/research/literature-orbit-closure-20261121/AL27_HALF_ROUTE.md)
documents a parameterized ordinary family with
\(0<x<n\), \(16x+3=9n\), and
\(T^{k+5}(x)=T^{k+9}(n)\), while the original source has no strict descent
through clock \(k+9\). The clocks grow with the parameter, and the smaller
partner need not be marked. This is an example of an actual physical route
outside the restricted fixed-horizon strategy ruled out here. Our theorem
does not prohibit it, require its partner to have a lower certificate rank,
or extend its guarded family to universal coverage.

## What this settles, and what it leaves open

The result rules out a universal repair that simultaneously:

1. preserves this literal supplied suffix;
2. strictly lowers the existing full multiset rank;
3. enlarges or preserves the original source so that every target can remain
   unchanged in the interval query.

Neither an unrestricted prefix length nor ordinary integrality rescues that
specific strategy. Integrality is instead what makes the obstruction exact.
Adding a fixed direct-forward lookahead still does not give universal
coverage of the stated suffix-preserving domain.

The theorem does not refute the complete-certificate architecture. A complete
dispatcher may change more of the supplied suffix, transform the wanted
target through an unbounded number of actual ordinary steps, use a smaller common-future partner,
or establish a different common rank. Those operations must still preserve
their stated target relation and compare with the original source. The new
bound says precisely which tempting local source reset cannot supply the
missing universal branch by itself.
