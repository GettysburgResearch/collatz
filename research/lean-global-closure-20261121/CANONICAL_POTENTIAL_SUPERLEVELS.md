# Global superlevel bounds for the canonical inverse potential

**Status: new written deduction from the pinned analytic inputs below;
not a Lean formalization and not a proof of Collatz.** The conclusion is
an upper bound over all nonperiodic ordinary targets. It goes beyond
decay inside one fixed predecessor basin, while allowing sparse escaping
forward trajectories.

## 1. Inputs, notation, and exact statement

Use the accelerated odd map

\[
U(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}
\]

and the ordinary shortcut map \(T\). All roots considered in the main
theorem are positive odd ternary units. A root is *nonperiodic* if it is
not itself on a cycle; it may enter a cycle later. No cycle classification
is assumed.

At PR180 head `d0349de2108abb7c8fb8393c086610e3372df116`, use:

* `research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md`, (PDU):
  absolute \(c,C>0\) give at least \(cX/a\) positive odd unit ordinary
  predecessors of each unit target \(a\), for every \(X\ge Ca\).
* `research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`,
  (M1)--(M4): the finite least excessive majorant
  \[
  V_0=g,\quad V_{j+1}=\max(g,PV_j),\quad V=\lim_jV_j,
  \quad g(q)=\mathbf1_{3\nmid q},
  \]
  where
  \[
  (Pf)(q)=\sum_{\substack{e\ge1\\2^eq\equiv1\ (3)}}
           \frac3{2^e}f\left(\frac{2^eq-1}{3}\right).
  \]
  The same note supplies \(0<G\le V\) on units, with \(PG=G\), and
  uniform decay of \(V(n)/n\) through the predecessors of each fixed
  ordinary target.

For the orbit count use
`research/astra-three-routes/pass2/ORBIT_MELLIN.md`, Section 1,
at PR175 head `2055b8a311ab87d07bffc730154a7f8546fe382c`, Git blob
`16c943601ce791afb1bbd5f02f3a9ea88ef38520`. That source gives the explicit
exponent \(\beta=39/40\) by an elementary cylinder calculation. Section 4
below explains exactly the small extension needed for a convergent
preperiod, so no injectivity claim about an entire inverse basin is used.

Put \(H(n)=V(n)/n\) and

\[
\ell(X)=\left\lfloor\frac35\log_2X\right\rfloor,
\qquad B(X)=4X^{39/40}+\ell(X),\qquad X\ge1.
\]

Then for every \(\varepsilon>0\),

\[
\boxed{
\#\{n\le X:n\text{ positive odd unit and nonperiodic},\quad
                 H(n)\ge\varepsilon\}
\le\frac{B(X)}{c\varepsilon}.}
\tag{S}
\]

Moreover \(H(n)\le1/c\) on this domain. The stronger weighted
antichain argument below proves

\[
\boxed{\sum_{\substack{n\le X\\n\text{ nonperiodic odd unit}}}H(n)
       \le\frac{B(X)}c.}
\tag{M}
\]

In particular, for every \(s>39/40\),

\[
\boxed{
\sum_{n\text{ nonperiodic odd unit}}\frac{H(n)}{n^s}
\le \frac{5s}{c(s-39/40)}<\infty.}
\tag{L1}
\]

For every \(p\ge1\), the power-moment estimate is

\[
\boxed{
\sum_{n\text{ nonperiodic odd unit}}\frac{H(n)^p}{n^s}
\le\frac{5s}{c^p(s-39/40)}<\infty.}
\tag{Lp}
\]

At the harmonic weight this gives

\[
\sum_{n\text{ nonperiodic odd unit}}\frac{V(n)}{n^2}
 \le\frac{200}{c},\qquad
\sum_{n\text{ nonperiodic odd unit}}\frac{V(n)^2}{n^3}
 \le\frac{200}{c^2}.
\tag{H}
\]

Every displayed upper bound remains valid with \(G\) in place of \(V\).
The constants retain the source-qualified analytic constant \(c\); no
numerical value for that constant is asserted.

## 2. The stopping-cutset representation retains actual ordinary sources

At a fixed nonperiodic odd unit root \(q\), unfold its actual inverse
\(U\)-tree. A vertex is a legal finite inverse word \(w\); write
\(n_w\) for its positive odd source and
\(\omega_w=\prod_{e\in w}3/2^e\) for its weight. The empty word has
source \(q\) and weight one.

A finite stopping cutset here means any finite prefix-free collection of
such words. It need not meet every infinite ray. Its value is

\[
                     \sum_{w\in\mathcal L}\omega_w g(n_w).
\]

For each \(j\), the supremum of these values over cutsets of depth at
most \(j\) is exactly \(V_j(q)\). At depth zero the only nonzero choice
is the root. Inductively one either stops at the root, or chooses stopping
cutsets below some of its children. Nonnegativity permits approximation
of the countable parent sum by a finite collection of children, and then
approximation of each child's supremum by one finite cutset. This proves
both inequalities in the recursion \(\max(g,PV_j)\). Taking the supremum
over \(j\) gives

\[
V(q)=\sup_{\mathcal L\text{ finite prefix-free}}
                    \sum_{w\in\mathcal L}\omega_wg(n_w).
\tag{C}
\]

Only leaves with \(g(n_w)=1\) need be retained. These are ordinary unit
sources, rather than formal residues. The exact positive affine identity
on the branch gives

\[
                       \omega_w n_w\le q.
\tag{A}
\]

The ordinary predecessor sets of two retained leaves are disjoint. To
check this at the level of actual integers, suppose some ordinary source
hits both leaves. Its deterministic trajectory orders the two hits, so
one leaf subsequently hits the other. Because \(q\) is nonperiodic,
each ordinary source can hit \(q\) only once; in particular each odd
source has only one inverse-word depth and one actual word to \(q\).
Thus the two leaf words would be comparable by prefix, contradicting the
cutset condition. This is disjointness of entire ordinary basins, not
just of valuation cylinders at a prescribed depth.

Define the lower natural density of odd unit predecessors by

\[
\underline d(q)=\liminf_{X\to\infty}\frac1X
 \#\{n\le X:n>0,\ n\text{ odd},\ 3\nmid n,\ n\to q\}.
\]

For any one finite cutset, (PDU) applies to all its leaves once
\(X\ge C\max_w n_w\). Since their predecessor basins are disjoint
and lie inside the predecessor basin of \(q\),

\[
\underline d(q)\ge c\sum_{w\in\mathcal L}\frac1{n_w}
              \ge\frac c q\sum_{w\in\mathcal L}\omega_w.
\]

Taking the supremum in (C) proves the useful capacity estimate

\[
\boxed{\underline d(q)\ge cH(q).}
\tag{D}
\]

In particular \(H(q)\le1/c\). No existence of a natural density is
required, and no countable additivity of lower density has been used.

## 3. Large-potential targets have finite width

Order nonperiodic odd targets by ordinary forward reachability. For odd
targets this is the same as reachability under \(U\). If a finite set
of roots is an antichain for this order, its entire predecessor basins
are pairwise disjoint by the same deterministic-trajectory argument.

For any such finite antichain \(\mathcal A\), (D) and finite-family
counting give the stronger weighted budget

\[
\boxed{\sum_{q\in\mathcal A}H(q)\le1/c.}
\tag{WA}
\]

Indeed the predecessor sets are disjoint, so the sum of their lower
densities is at most one. If \(H(q)\ge\varepsilon\) at every root in
an antichain of size \(m\), this implies

\[
                         mc\varepsilon\le1.
\tag{W}
\]

Consider now the finite superlevel set in (S), and choose its minimal
elements under reachability. They form an antichain, so there are at
most \(1/(c\varepsilon)\) of them. Every member of the finite set
lies on the forward orbit of one of these minimal elements: descend
inside the finite partial order until a minimal ancestor is reached.
Thus the whole finite superlevel set is covered by that many actual
forward-orbit chains. A general infinite-poset chain-partition theorem
is not needed.

There is also a global finite-orbit cover. For any fixed heavy target,
the fixed-basin sublinearity proved in the pinned PR180 note makes its
heavy ancestors a finite set. Consequently it has a predecessor-minimal
heavy ancestor. All such globally minimal heavy roots form an antichain,
so there are at most \(1/(c\varepsilon)\) of them. Hence the entire
nonperiodic superlevel set \(\{H\ge\varepsilon\}\) is contained in
the union of finitely many actual forward orbits. This last strengthening
uses the fixed-basin theorem; the counting bound (S) itself does not.

## 4. Counting a finite forward chain, including convergent preperiods

Fix \(X\ge1\) and \(\ell=\ell(X)\). The pinned Section 1 cylinder
proof uses only injectivity of \(U^\ell\) on the source set for this
one selected \(\ell\); its stated all-depth injectivity assumption is
stronger than needed at this fixed scale. It therefore gives
\(4X^{39/40}\) for any subset of \([1,X]\) whose selected-depth
endpoints are distinct. When \(\ell=0\), the same bound is immediate.

Let \(S\) be any finite set of nonperiodic odd states on one ordinary
forward trajectory. If the trajectory never repeats, \(U^\ell\) is
injective on \(S\). If it eventually enters any positive cycle, remove
from \(S\) the states whose first entrance to that cycle occurs within
\(\ell\) odd steps. There are at most \(\ell\) such states: each
positive entrance time occurs at most once on the nonperiodic part of
one deterministic trajectory.

All remaining \(U^\ell\)-images are outside the cycle. They are
distinct, because the nonperiodic part of a deterministic trajectory
has no repeated states. The cylinder estimate applies to these remaining
sources. Restoring the removed states gives

\[
                        \#(S\cap[1,X])\le B(X).
\tag{O}
\]

This removal count depends only on \(\ell=O(\log X)\), not on the
heights of the intermediate states, the eventual cycle length, or the
first source's total stopping time. In particular it does not assume
that the relevant cycle is the known cycle through 1.

Apply (O) to the finite cover from Section 3 to obtain (S).

## 5. Weighted antichain layering removes the layer-cake loss

The weighted budget (WA) yields (M) directly. In the finite set of
nonperiodic odd unit targets at most \(X\), assign to each target the
maximum length of a reachability chain ending there. These are positive
integer ranks. If one target strictly precedes another, its rank is
strictly smaller: append the latter to a longest chain ending at the
former. Thus each equal-rank set is an antichain, with total \(H\)-weight
at most \(1/c\) by (WA).

The largest rank is the length of one actual forward-orbit chain, hence
is at most \(B(X)\) by Section 4. Sum the antichain budget over these
at most \(B(X)\) rank layers to obtain (M). This argument involves only
a finite partial order; it needs neither an infinite chain partition
nor a measure on a boundary. For \(p\ge1\), the pointwise bound
\(H\le1/c\) also gives
\(\sum_{q\le X}H(q)^p\le B(X)/c^p\) on the same domain.

The elementary inequality \(\ell(X)\le X^{39/40}\) gives
\(B(X)\le5X^{39/40}\). For \(s>39/40\), apply
\(n^{-s}=s\int_n^\infty t^{-s-1}\,dt\), and interchange only
nonnegative terms. The integral
\(\int_1^\infty t^{39/40-s-1}\,dt=(s-39/40)^{-1}\) then gives
(L1) and (Lp), including the constants in (H).

## 6. Completion test: what this does and does not control

This is an actual global upper estimate for the canonical potential.
For each fixed threshold its exceptional targets lie on finitely many
ordinary forward trajectories, and the potential has the stated finite
weighted moments over every nonperiodic ordinary target.

It does not prove that those finitely many trajectories terminate.
An escaping trajectory may have very few points below each height, with
\(H\) bounded away from zero on that sparse trajectory and small on
its many incoming predecessors. This behavior is compatible with (S),
(L1), and (Lp).

The resident PR155/163 rigidity theorem applies to a **Collatz-invariant
label** \(f\) with finite specified five energy

\[
\sum_{\substack{n>0\\n\text{ odd},\ 3\nmid n}}
 \frac{d(f(5n),f(n))}{n}<\infty.
\]

The normalized inverse potential \(H\) is not such a label. Its
weighted moments do not establish a bound on that label boundary. A
closing use of this new estimate would require a proved transfer or
charging inequality from the actual label defects to these potential
moments, with original source weights and bounded incoming multiplicity.
No such inequality is assumed or claimed here. Periodic targets were
excluded explicitly from the main theorem, so these estimates also do
not exclude an additional positive cycle.
