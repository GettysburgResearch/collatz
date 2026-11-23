# An unchanged ordinary spine forces summable sibling Green ratios

23 November 2026.

**Status: written theorem conditional on an escaping ordinary component;
no escape exclusion or full Collatz proof.** The new result is an exact
summability constraint on the Green function along one fixed ordinary
orbit. It follows from disjoint *ordinary predecessor basins*, not a
change to Haar, a stationary time limit, or a fresh source distribution.
It gives a concrete near-logarithmic sibling comparison that would
exclude escape. That comparison is not proved here.

## 1. Retained objects and dependencies

Let

\[
 O=\{n\in\mathbb Z_{>0}: n\text{ odd},\ 3\nmid n\},\quad
 U(n)=\frac{3n+1}{2^{a(n)}},\quad a(n)=v_2(3n+1).
\]

Fix one escaping eventual-meeting component \(E\subset O\), an arbitrary
\(s>1\), and the pressure probability from the parent packet:

\[
 r(n)=\frac1n\prod_{k\ge0}\frac{3U^kn}{3U^kn+1}>0,\quad
 M_s=\sum_{n\in E}r(n)^s,\quad
 \mu(n)=r(n)^s/M_s.
\tag{1}
\]

The inherited ordinary product bound and \(r(n)\le1/n\) give
\(0<M_s<\infty\). All forward orbits in \(E\) are injective and
escape to infinity. Exact edges give

\[
 r(n)=(3/2^{a(n)})r(Un),\qquad
 \mu(n)=(3/2^{a(n)})^s\mu(Un).
\tag{2}
\]

For \(q\in\mathbb Z_3^\times\), retain the operator

\[
 P_sf(q)=\sum_{\substack{e\ge1\\(2^eq-1)/3\in\mathbb Z_3^\times}}
 (3/2^e)^s f((2^eq-1)/3),\qquad
 Z_s(q)=\sum_{k\ge0}P_s^k1(q).
\tag{3}
\]

At positive ordinary unit roots every legal parent is a positive odd unit
with the exact stated valuation. The pressure identity is \(\mu P_s=\mu\).
No row normalization is implicit in (3).

The precise inherited sources are PR177, commit
`f47a5ec51aa5853f104013a6d5046d6220ff7423`:

- `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`,
  HE2 and HE18--HE24a: ordinary product positivity and pressure measure.
- `research/lean-exact-witness-global-20261121/literature-closure/atomic/ORDINARY_RENEWAL_AND_RETAINED_ENDPOINT.md`,
  (5), (7), (23), and (29)--(31): same-successor scaling, actual Green
  mass, and the retained endpoint.

The latest PR180 note `research/profound-step-20261123/STATIONARY_REAL.md`
was read at `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`. Its conditional
stationary drift classification and minimum-source qualification remain
separate. No assertion about a stationary law is imported below.

## 2. Exact finite-mass geometry of ordinary predecessor basins

Define the ordinary predecessor set and its pressure mass by

\[
 \operatorname{Pred}(q)=\{n\in E:U^kn=q\text{ for some }k\ge0\},
 \qquad A(q)=\mu(\operatorname{Pred}(q)).
\tag{4}
\]

Each source in this set has a unique hitting depth. If two different
depths hit \(q\), then \(q\) is periodic, contrary to escape. At depth
\(k\), multiplying (2) along the actual path gives

\[
 \sum_{U^kn=q}\mu(n)=\mu(q)P_s^k1(q).
\]

Consequently

\[
 \boxed{A(q)=\mu(q)Z_s(q),\qquad 0<A(q)\le1.}
\tag{5}
\]

In particular the Green function is finite at every root used here.
This identity is a positive ordinary sum, so Tonelli is enough; no
spectral or regularity theorem is required.

The predecessor subtrees of different immediate parents are disjoint,
and none contains \(q\). Thus the exact tree conservation law is

\[
 \boxed{A(q)=\mu(q)+\sum_{Un=q}A(n).}
\tag{6}
\]

Now fix one original source \(q_0\in E\) and put \(q_j=U^j q_0\).
The sets \(\operatorname{Pred}(q_j)\) increase to \(E\): every member
of the component eventually meets this ray. Hence

\[
 \boxed{A(q_j)\uparrow1.}
\tag{7}
\]

Every object in (4)--(7) retains the same ordinary component and source.

## 3. All upper sibling subtrees are simultaneously disjoint

Use the unit-preserving symmetry

\[
 S(n)=64n+21,\quad S^h(n)=64^hn+(64^h-1)/3,\quad t=64^{-s}.
\tag{8}
\]

It satisfies

\[
 U(S^h n)=Un,\quad a(S^h n)=a(n)+6h,\quad
 \mu(S^h n)=t^h\mu(n).
\tag{9}
\]

For \(j\ge0,h\ge1\), call \(v_{j,h}=S^h q_j\) an upper sibling.
Every one belongs to \(E\), but none lies on the original ray. Indeed,
if \(S^h q_j=q_i\), applying \(U\) gives \(q_{j+1}=q_{i+1}\),
so injectivity gives \(i=j\), contradicting \(S^h q_j>q_j\).

**Disjointness lemma.** The sets

\[
 \operatorname{Pred}(q_0),\qquad
 \operatorname{Pred}(v_{j,h})\quad(j\ge0,h\ge1)
\tag{10}
\]

are pairwise disjoint.

To see this, two roots reached from a common source lie on the same
forward ray. An upper sibling joins the original ray after exactly one
step, so it cannot later reach another upper sibling. Equality of two
upper siblings would force equality of their next states, then \(j=i\),
then \(h=k\) by strict monotonicity of \(S^h q_j\). An upper sibling
cannot have a common predecessor with \(q_0\) either: the two possible
orders of the roots would force an upper sibling onto the original ray
or a repetition within that ray.

Therefore countable additivity yields the exact source budget

\[
 \boxed{\sum_{j\ge0}\sum_{h\ge1}A(S^h q_j)
          \le1-A(q_0).}
\tag{11}
\]

There can be other sibling branches, so equality is not asserted.
The same estimate is available at every finite rectangle of indices
before any infinite sum is taken.

## 4. Summability of the actual Green ratios

Using (5) and (9), for every \(j,h\),

\[
 \frac{A(S^h q_j)}{A(q_j)}
       =t^h\frac{Z_s(S^h q_j)}{Z_s(q_j)}.
\tag{12}
\]

Since \(A(q_j)\ge A(q_0)>0\), (11) gives

\[
 \boxed{\sum_{j\ge0}\sum_{h\ge1}
       t^h\frac{Z_s(S^h q_j)}{Z_s(q_j)}
       \le\frac{1-A(q_0)}{A(q_0)}.}
\tag{13}
\]

In particular, for each fixed \(h\ge1\),

\[
 \boxed{\sum_{j\ge0}\frac{Z_s(S^h q_j)}{Z_s(q_j)}
       \le64^{hs}\frac{1-A(q_0)}{A(q_0)}<\infty.}
\tag{14}
\]

The ratios in (14) thus tend to zero on this **unchanged ordinary
forward orbit**. This is stronger than finding a sparse subsequence or
an averaged loss of regularity under a newly chosen measure.

Equation (6) gives a sharper local form. The upper siblings in (8) are
among the immediate parents of \(q_{j+1}\), distinct from \(q_j\).
Thus

\[
 \boxed{\sum_{h\ge1}t^h
       \frac{Z_s(S^h q_j)}{Z_s(q_j)}
 \le\frac{A(q_{j+1})-A(q_j)-\mu(q_{j+1})}{A(q_j)}.}
\tag{15}
\]

All terms on the right are actual ordinary masses. Summing after the
coarse bound \(A(q_j)\ge A(q_0)\) proves the finite estimate

\[
 \sum_{j<N}\sum_{h\ge1}t^h
       \frac{Z_s(S^h q_j)}{Z_s(q_j)}
 \le\frac{A(q_N)-A(q_0)-\sum_{j=1}^N\mu(q_j)}{A(q_0)}.
\tag{16}
\]

For example, if a proposed comparison gives
\(Z_s(Sq_j)\ge\epsilon Z_s(q_j)\) at \(L\) distinct actual clocks,
then necessarily

\[
 L\epsilon\le64^s\frac{1-A(q_0)}{A(q_0)}.
\tag{17}
\]

This is a finite quantitative falsification test for a claimed
source-preserving Harnack estimate.

## 5. A near-logarithmic comparison would exclude escape

The physical forward bound needs no growth hypothesis:

\[
 q_{j+1}+1\le\tfrac32(q_j+1),\qquad
 q_j+1\le(3/2)^j(q_0+1).
\tag{18}
\]

It follows that

\[
 \sum_{j\ge0}
 \frac1{(1+\log(q_j+1))\log(2+\log(q_j+1))}=\infty.
\tag{19}
\]

Indeed the denominator is at most \(C(j+1)\log(j+2)\) for a
constant depending only on \(q_0\). The latter reciprocal series
diverges. Combining (14) and (19) proves the following unconditional
consequence *of a hypothetical escaping source*:

\[
 \boxed{\liminf_{j\to\infty}
 (1+\log(q_j+1))\log(2+\log(q_j+1))
 \frac{Z_s(Sq_j)}{Z_s(q_j)}=0.}
\tag{20}
\]

Thus a sufficient arithmetic closing theorem is this narrowly specified
ordinary comparison: for some fixed \(s>1,c>0,Q\),

\[
 Z_s(64q+21)\ge
 \frac{c\,Z_s(q)}
 {(1+\log(q+1))\log(2+\log(q+1))}
\tag{HC}
\]

for every positive odd unit \(q\ge Q\) at which \(Z_s(q)<\infty\).
It is enough to prove it on every escaping ray; a global estimate is
stated to make the proposed arithmetic input independently testable.
A comparison only on a subsequence must retain a divergent reciprocal
sum there; arbitrary infinitely many good clocks do not suffice.

**If (HC) is proved, escape is excluded.** Equations (14) and (19)
would contradict one another. This conclusion concerns escape only;
nontrivial positive cycles are still a separate obligation.

The same argument permits further iterated logarithms as long as the
corresponding reciprocal clock series diverges. No such lower bound
is asserted in this packet.

## 6. The direct transport attempt and its exact cost

A literal inverse-word transport exists when the shifted roots agree at
the full required ternary precision. For the unit operator, \(P_s^k1\)
is a function of the residue modulo \(3^{k+1}\). The symmetry has

\[
 v_3(S^h q-q)=1+v_3(h),
\tag{21}
\]

since \(3q+1\) is a ternary unit. Hence, for \(h=3^d\),

\[
 P_s^k1(S^h q)=P_s^k1(q)\quad(0\le k\le d).
\tag{22}
\]

This is an exact equality of finite-depth complete predecessor-weight sums;
it does not presume ordinary integrality of an infinite completion.
At ordinary roots both sides enumerate actual positive parents.
Consequently

\[
 Z_s(S^{3^d}q)\ge\sum_{k=0}^dP_s^k1(q).
\tag{23}
\]

But its contribution to the common-source mass budget (13) carries
\(t^{3^d}=64^{-s3^d}\), and it compares a different sibling
\(S^{3^d}q\), not the fixed sibling \(Sq\) in (HC).
Thus the exact full-precision transport supplies no near-logarithmic
fixed-sibling comparison. Replacing that cost by a small constant or
silently identifying these siblings would lose the actual source.

The separate [balanced inverse-tree compiler](BALANCED_INVERSE_TRANSPORT.md)
now compares the fixed pair q and Sq at every depth. It bijects all
ordinary parents using their class modulo three and the quotient of
their exponent modulo six. Its signed per-edge cost lies between -4
and 4, with an exact physical-height cocycle and no collision loss.
This still permits exponential cost in the word length. No amortized
bound reducing its full-pressure cost to the scale in (HC) has been
constructed. That is the first unsupported step of this attack.

## 7. Relation to the inspected operator literature

Idris Assani, *Collatz map as a non-singular transformation*, arXiv
2208.11675v3, Theorem 1.2 and Definition 2.5, gives a finite-measure
power-boundedness characterization for the shortcut map. Primary PDF:
<https://arxiv.org/pdf/2208.11675v3>.

That theorem does not supply power boundedness for the pressure measure
(1). In particular, finite conformal mass is not forward invariance or
power boundedness. The present argument uses the finer ordinary
predecessor-basin partition to obtain (13)--(20) directly; it imports no
operator recurrence assertion from that paper.

PR180's stationary real-series results likewise do not supply (HC):
the ordinary label and Green profile in (HC) are retained at each
actual clock. Critical divergence of a stationary real series does not
compare these two sibling predecessor basins.

## 8. Scope of this checkpoint

The proved new conclusion is the same-source double summability (13),
its local and finite forms (15)--(17), and the near-logarithmic collapse
(20). Their proofs are written mathematics; there is no new Lean
verification of their infinite measure-theoretic content.

The all-ordinary Harnack estimate (HC) remains OPEN. No escape measure
has been shown to vanish, no actual time-law collision upper bound is
claimed, and no full Collatz result follows from this note alone.
