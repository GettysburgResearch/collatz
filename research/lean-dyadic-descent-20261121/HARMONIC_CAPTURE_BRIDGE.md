# The complete Green potential of the unchanged canonical source seed

**Status: written deductions from pinned ordinary harmonic-flow inputs,
independently reviewed. The ten finite/series statements in the companion
Lean module passed the fresh combined 22-statement replay and axiom audit.
The analytic inputs and bridges retain written-proof status. Full Collatz
remains open.**

This note computes the all-time Green sum of the actual canonical source
seed, with time zero, killing, and source collisions retained. It gives a
normalized bounded potential, a uniform estimate on predecessor domains
with a high minimum, and a finite global weighted space-time collision
budget. These concern the specified seed at actual ordinary targets.
They are stronger than an estimate for newly sampled endpoint weights.

The deductions do not give an effective contact time at a moving root.
Section 6 identifies exactly why combining them with the current obstacle
entrance theorem does not yet yield that estimate.

## 1. Exact domain and frozen input

Use the accelerated odd map

\[
U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

Let \(\mathcal N\) be the positive odd ternary units which are not
themselves periodic. A state in this set can eventually enter a cycle.
Forward transport is killed at its first periodic state. An inverse
predecessor of a nonperiodic unit is again nonperiodic. Every finite path
ending in \(\mathcal N\) is injective.

Throughout,
\(\operatorname{Pred}(q)=\{n\in\mathcal N:U^j(n)=q\text{ for some }j\ge0\}\).
It includes the target at time zero and includes only the states in this
unit domain; for example, the nonunit source \(3\to5\) is not in this set.

The primary repository input is PR185 at
`276be8154f4e867acc0230466b34d9cb224aacf5`,
`research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`,
Git blob `9b8ed17476a6c133f3bb3710c4fe1d5de8d5a1f1`.
Its equations (7)--(19) provide the following source-qualified written
facts, retaining their exact PR175/176/180 dependencies.

Define ordinary inverse counting and the two seeds by

\[
(Lf)(q)=\sum_{\substack{n\in\mathcal N\\U(n)=q}}f(n),\qquad
h(q)=G(q)/q,\qquad
\lambda(q)=\frac{3q}{3q+1},\qquad
d(q)=(1-\lambda(q))h(q)=\frac{h(q)}{3q+1}.
\]

The critical harmonic equation, written in ordinary counting variables,
is

\[
L(\lambda h)=h,\qquad Lh=h+Ld. \tag{1}
\]

The increasing harmonicization has finite limit

\[
L^k h\uparrow\nu,\qquad L\nu=\nu,\qquad
0<h\le\nu\le\delta^{-1}h,\qquad
\delta=e^{-200/3}.
\tag{2}
\]

The reference is positive and has infinite total mass. With the upstream
population constant \(c>0\), put

\[
A=\frac{203}{3c},\qquad\theta=\frac{39}{40}.
\]

The upstream moment estimates give

\[
\nu(q)\le A,\qquad
\sum_{q\in\mathcal N}\frac{\nu(q)}{q^s}
\le\frac{5sA}{s-\theta}\quad(s>\theta).
\tag{3}
\]

If the **whole unit-predecessor set** of a target lies above \(m\ge1\),
the stronger comparison is

\[
h(q)\ge\delta_m\nu(q),\qquad
\delta_m=\exp\left(-\frac{200}{3}m^{-1/40}\right).
\tag{4}
\]

This floor is not a minimum of just the target's later forward suffix.
All source ancestors are retained.

The canonical original-source mass is the same one used in PR185:

\[
a_0(n)=\frac{h(n)}n=\frac{G(n)}{n^2},\qquad
b_k(q)=L^ka_0(q).
\tag{5}
\]

It is positive at every state, has finite total mass, and has finite
initial collision energy. No weight in (5) is replaced after transport.

## 2. Exact immigration Green sum, including time zero

The first equality in (1) gives

\[
L^{k+1}h-L^kh=L^{k+1}d.
\]

Consequently, for every \(N\ge0\),

\[
\boxed{
\sum_{k=0}^{N}L^kd(q)
=d(q)+L^Nh(q)-h(q)
=L^Nh(q)-\lambda(q)h(q).
}
\tag{6}
\]

Every summand is nonnegative. Increasing the finite limit and using (2)
proves the complete identity

\[
\boxed{
W(q):=\sum_{k\ge0}L^kd(q)=\nu(q)-\lambda(q)h(q).
}
\tag{7}
\]

This is the time-domain form of PR185's predecessor-source sum. In
particular it is not new construction of the harmonic reference. The new
use below is its comparison with the fixed canonical source seed and the
complete history of its retained-source collisions.

For an ordinary source height \(n\ge1\), an exact identity gives

\[
\boxed{
a_0(n)=\left(3+\frac1n\right)d(n),\qquad
3d(n)\le a_0(n)\le4d(n).
}
\tag{8}
\]

The positive operator \(L^k\) preserves both inequalities. Therefore

\[
\boxed{
3W(q)\le R(q):=\sum_{k\ge0}b_k(q)\le4W(q)<\infty.
}
\tag{9}
\]

Equation (9) controls the **entire all-time mass from the unchanged
canonical seed at one actual target**, not just the single-time energy.

There is also an exact source expansion. A source can hit a nonperiodic
target at only one odd depth, so nonnegative summation gives

\[
\boxed{
R(q)=\sum_{n\in\operatorname{Pred}(q)}\frac{h(n)}n
=3W(q)+\sum_{n\in\operatorname{Pred}(q)}\frac{d(n)}n.
}
\tag{10}
\]

Different sources reaching the same target are all included. The
uniqueness concerns the depth of one fixed source-target pair; it does
not erase different-source collisions.

### All-time tail at a fixed target

For \(N\ge1\), subtracting the first \(N\) terms in (7) gives

\[
\sum_{k\ge N}L^kd(q)=\nu(q)-L^{N-1}h(q).
\]

Thus

\[
\boxed{
3\bigl(\nu(q)-L^{N-1}h(q)\bigr)
\le\sum_{k\ge N}b_k(q)
\le4\bigl(\nu(q)-L^{N-1}h(q)\bigr).
}
\tag{11}
\]

This tail tends to zero for every fixed ordinary target. Its uniformity
when the target changes is not asserted.

## 3. A normalized coboundary and inverse occupation budget

Use the ordinary harmonic inverse Markov kernel

\[
K(q,n)=\mathbf1_{U(n)=q}\frac{\nu(n)}{\nu(q)}.
\]

Its rows sum to one by \(L\nu=\nu\). Define

\[
z(q)=\frac{\lambda(q)h(q)}{\nu(q)},\qquad
g(q)=\frac{a_0(q)}{\nu(q)}.
\]

All these values are ordinary point values. From (1),

\[
Kz(q)=\frac{h(q)}{\nu(q)},\qquad
\boxed{Kz-z=d/\nu.}
\tag{12}
\]

The potential is bounded by

\[
\frac34\delta\le z(q)<1,
\qquad
3(Kz-z)\le g\le4(Kz-z).
\tag{13}
\]

For \(k\ge1\), telescoping along the actual inverse paths gives
\(K^kz(q)=L^{k-1}h(q)/\nu(q)\to1\). If \(X_k\) follows
this kernel from \(q\), nonnegative summation and (9) consequently give

\[
\boxed{
3(1-z(q))
\le\mathbb E_q\sum_{k\ge0}g(X_k)
=\frac{R(q)}{\nu(q)}
\le4(1-z(q)).
}
\tag{14}
\]

The process \(z(X_k)\) is a bounded submartingale with expectations
tending to one, and it tends to one almost surely. One elementary
justification uses \(Y_k=1-z(X_k)\ge0\), a supermartingale. For
\(M\ge n\), stopping at its first crossing of \(\varepsilon\)
between \(n\) and \(M\), the finite supermartingale inequality gives

\[
\Pr\{\max_{n\le k\le M}Y_k\ge\varepsilon\}
\le\mathbb E Y_n/\varepsilon.
\]

Increasing \(M\) and then \(n\), whose expected values tend to zero,
proves the assertion. This is a normalization along the inverse law;
it is not forward absorption.

### Uniform gain on an actual high-floor predecessor domain

Under the whole-domain hypothesis of (4), \(q\ge m\), so

\[
z(q)\ge\frac{3m}{3m+1}\delta_m.
\]

The canonical occupation bound becomes

\[
\boxed{
\frac{R(q)}{\nu(q)}
\le4\left(1-\frac{3m}{3m+1}
 e^{-(200/3)m^{-1/40}}\right)
\le\frac4{3m+1}+\frac{800}{3}m^{-1/40}.
}
\tag{15}
\]

The last inequality is \(1-e^{-t}\le t\). Thus the normalized
all-time canonical-source mass tends uniformly to zero on actual
predecessor domains whose minimum tends to infinity.

The same argument after time \(N\) gives the quantitative targetwise
tail budget in terms of \(1-K^Nz(q)\), by (11). No source-independent
rate for that quantity is supplied.

## 4. Global weighted space-time collision summability

Define the retained-source energy with a spatial weight by

\[
\mathcal E_s(k)=
\sum_{q\in\mathcal N}\frac{b_k(q)^2}{\nu(q)q^s}.
\]

For each target, nonnegativity and (9) imply

\[
\sum_{k\ge0}\frac{b_k(q)^2}{\nu(q)}
\le\frac{R(q)^2}{\nu(q)}
\le16\frac{W(q)^2}{\nu(q)}
\le16\nu(q).
\tag{16}
\]

All source-pair collisions at each clock remain inside \(b_k(q)^2\).
The first inequality even retains the nonnegative cross-clock terms on
its right; it makes no source independence assumption.

Combining (16) with the actual reference moment (3), Tonelli gives

\[
\boxed{
\sum_{k\ge0}\mathcal E_s(k)
\le16\sum_q\frac{W(q)^2}{\nu(q)q^s}
\le\frac{80sA}{s-39/40}
\quad(s>39/40).
}
\tag{17}
\]

In particular \(\mathcal E_s(k)\to0\), and the tails of its
time series tend to zero. These are actual all-source, all-time weighted
collision estimates for the fixed canonical seed, with a displayed
constant. The weight is \(q^{-s}\), and is part of the theorem.

For any finite target region \(q\le X\), (16) and PR185's prefix
moment bound also give

\[
\sum_{k\ge0}\sum_{q\le X}\frac{b_k(q)^2}{\nu(q)}
\le80A X^{39/40}.
\tag{18}
\]

Thus the retained-source energy present in every finite target region
tends to zero, with a finite complete occupation budget there. Entry into a
periodic orbit is killed; escape to unbounded ordinary targets remains
compatible with these estimates.

## 5. Lean interface

`HarmonicCapture.lean` supplies the finite and real-series core:

* exact identity (8) and both seed comparisons;
* telescoping (6), with the time-zero term retained;
* finite canonical Green bounds and passage to a `HasSum` under the
  explicitly supplied harmonicization limit;
* complete canonical Green summability and both bounds;
* the normalized algebra used in (15);
* targetwise finite and complete collision-series bounds (16).

The abstract sequence substitution is
\(h_k=L^kh(q)\), \(d_k=L^kd(q)\), \(a_k=L^ka_0(q)\).
Existence and finiteness of the actual ordinary harmonic reference,
countable-kernel transport, path-law assertions, the global moment
estimate, and the final Tonelli application remain written mathematics
with the retained input pins. They are not installed as Lean axioms.

## 6. Contact minimality: the precise remaining cost problem

The source for this comparison is PR176 at
`8aeb843bba254f065743b6fa277a70906b51d520`,
`research/lean-global-resolvent-20261121/overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md`,
Git blob `38d4044de54a424935eb85d52f4f28251afec6ce`, and its companion
`CONTACT_CAPTURE_SYNTHESIS.md`, blob
`e8def811f6946f9ed2034b745fbe79229b21bdb6`.

That argument proves almost-sure first contact with
\(C=\{V\le1+\varepsilon\}\) under both the stopped \(V\)-Doob law
and the harmonic \(G\)-Doob law, and gives a finite-front bound.
PR185 compares the harmonic \(G\)-Doob law with \(K\); it does not
directly compare the stopped \(V\)-law with \(K\).

The additional stopped-word bridge is elementary. The pinned
every-ordinary-point comparison is \(G\le V\le2\kappa G\), for a
fixed finite \(\kappa>0\). For an actual first-contact word from
\(q\) to \(x\), the \(V\)- and \(G\)-Doob probabilities satisfy

\[
\frac{\Pr_q^V(w)}{\Pr_q^G(w)}
=\frac{V(x)/G(x)}{V(q)/G(q)}
\in[(2\kappa)^{-1},2\kappa].
\tag{19a}
\]

This follows by telescoping the same critical coefficients before contact.
Summing the disjoint first-contact words gives the bounded comparison of
the two stopped laws. PR185's full \(G\)-to-\(\nu\) path density lies
between \(\delta\) and \(\delta^{-1}\), so its pushforward to paths
stopped at the same contact set has the same bounds. Combining the two
comparisons is therefore legitimate on the same physical predecessor
tree, without identifying the two Doob kernels.

The new budget controls the cost \(g(X_k)\), which satisfies

\[
\frac{\delta}{X_k}\le g(X_k)\le\frac1{X_k}.
\tag{19}
\]

These estimates supply no positive constant lower bound for this cost on
the continuation set \(V>1+\varepsilon\). They do not exclude high
ordinary ancestors remaining there while paying very little cost per
inverse step. Therefore
(14) does not bound the expected contact time, or give contact probability
at PR176's native logarithmic depth. A proof of such a rate needs another
arithmetic relation between height, continuation, and the actual source.

Likewise, (15) cannot be applied with the growing minimum of a later
forward suffix. Every later endpoint retains the original source among
its predecessors. Along one hypothetical escaping component that source
does not disappear from the sum (10).

The spatial factor in (17) is equally essential. An escaping source of
mass \(w>0\), at endpoints \(q_k\to\infty\), can retain unweighted
energy approaching \(w^2/C>0\), as PR185 proves, while its weighted
contribution \(w^2/(\nu(q_k)q_k^s)\) tends to zero. The new budget
therefore establishes weighted decay and finite local occupation, not
the tightness needed to remove that weight. Nontrivial cycles also remain
outside this killed-state domain.

The remaining positive target is a bound that prevents the canonical
source energy from moving to ever larger ordinary endpoints, or a
lower bound on cost accumulation before inverse contact. None is assumed
in this note.
