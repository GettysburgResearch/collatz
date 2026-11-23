# Harmonicity and dyadic-ray decay do not imply a sublinear ordinary envelope

**Status: written exact construction on the actual ordinary inverse graph.**
The explicit ray construction below is unconditional. The uniformly positive
perturbation uses the source-qualified harmonic envelope constructed in the
companion renewal work. The marked variant uses the precisely pinned
marked-ancestor theorem described in section 5. None of these constructions
is a divergent Collatz orbit, and this note does not refute sublinearity of
the particular envelope obtained from Abel averages.

For positive integers define

\[
(Pf)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
 \frac3{2^e}f\!\left(\frac{2^e q-1}{3}\right).
\tag{H1}
\]

Every argument on the right is positive and odd. On odd arguments, its
edges are exactly the inverse edges of the accelerated ordinary map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\).

## 1. An explicit increasing ordinary inverse ray

Set \(q_0=1\), \(q_1=5\). For \(j\ge1\), choose the exponent
\(e_j\) by this table and set \(q_{j+1}=(2^{e_j}q_j-1)/3\):

| \(q_j\bmod9\) | 1 | 2 | 4 | 5 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|
| \(e_j\) | 4 | 3 | 6 | 3 | 4 | 5 |

The table has \(2^{e_j}q_j\equiv4\) or \(7\pmod9\), so each new
value is a positive odd ternary unit. Moreover \(3\le e_j\le6\) and

\[
q_{j+1}\ge(8q_j-1)/3>2q_j.
\tag{H2}
\]

These are distinct, unbounded, actual ordinary predecessors, all of which
converge to one. The beginning is \(1,5,13,277,1477,7877,\ldots\).
The inverse edge from \(q_1=5\) to \(q_0=1\) has exponent four; write
\(e_0=4\). The additional odd predecessor of one on the trivial cycle is
one itself, with exponent two.

## 2. A finite harmonic function concentrated on this ray

Define a function on positive odd integers by

\[
h(1)=1,\qquad h(5)=\frac43,\qquad
h(q_{j+1})=\frac{2^{e_j}}3h(q_j)\quad(j\ge1),
\tag{H3}
\]

and set it to zero at all other odd arguments.
Every value is a finite nonnegative rational number.

At a ray node \(q_j\), \(j\ge1\), the only odd parent in the
support of \(h\) is \(q_{j+1}\). This follows from the deterministic
identity \(U(q_i)=q_{i-1}\) and distinctness of the ray. Thus
\((Ph)(q_j)=3\,2^{-e_j}h(q_{j+1})=h(q_j)\).
At one, both supported parents must be included:

\[
(Ph)(1)=\frac34h(1)+\frac3{16}h(5)
       =\frac34+\frac14=1=h(1).
\tag{H4}
\]

At every odd point outside the ray, there is no supported odd parent, so
both sides are zero. Consequently \(Ph=h\) on the full positive odd
domain, not merely on the selected edges.

Along the ray,

\[
\frac{h(q_{j+1})}{q_{j+1}}
 =\frac{h(q_j)}{q_j-2^{-e_j}}
 >\frac{h(q_j)}{q_j}.
\tag{H5}
\]

In particular

\[
\boxed{\frac{h(q_j)}{q_j}\ge\frac4{15}\quad(j\ge1).}
\tag{H6}
\]

The function even has a global linear upper bound. Put
\(x_j=2^{-e_j}/q_j\). By (H2),

\[
\sum_{j\ge1}x_j\le\frac18\sum_{j\ge1}\frac1{5\,2^{j-1}}
 =\frac1{20}.
\]

For every finite product, \(\prod(1-x_j)\ge1-\sum x_j\ge19/20\).
Equation (H5) therefore gives

\[
\frac4{15}\le\frac{h(q_j)}{q_j}\le\frac{16}{57}<1
 \quad(j\ge1).
\]

Together with \(h(1)=1\) and the zero values elsewhere, this proves
\(0\le h(q)\le q\) on odd arguments. Failure of sublinearity is not
caused by an infinite value or by superpolynomial growth.

## 3. Correct extension to every positive ordinary argument

It would be incorrect to set all even values to zero: odd edges pass
through even ordinary points. Instead, retain the odd values above and set

\[
\widetilde h(q)=(Ph)(q)\quad(q\text{ even}).
\]

For an odd \(r\) and \(E\ge0\), this is exactly

\[
\boxed{\widetilde h(2^E r)=
 2^E\sum_{\substack{a>E\\2^a r\equiv1\ (3)}}
       \frac3{2^a}h\!\left(\frac{2^a r-1}{3}\right).}
\tag{H7}
\]

For \(E=0\), (H7) agrees with \(h(r)\) by odd harmonicity.
For \(E>0\), substitute \(a=e+E\) in (H1). Since (H1) only
evaluates odd parents, the resulting all-positive function satisfies

\[
P\widetilde h=\widetilde h
\]

on every positive integer.

For a fixed odd core \(r\), at most one supported parent occurs in
(H7), except that \(r=1\) has the two parents in (H4). Each has one
fixed finite exponent. All even values are therefore finite, and on each
dyadic ray the function eventually vanishes identically. In this explicit
bounded-exponent example there is the stronger uniform statement

\[
\widetilde h(2^E r)=0\qquad(E\ge6,\ r\text{ positive odd}).
\tag{H8}
\]

Thus dyadic-ray decay, even with this uniform finite cutoff for the atomic
summand, does not control the values at the unbounded odd nodes \(q_j\).

## 4. Adding a uniform floor does not repair the implication

Let \(G_0\) be any finite nonnegative all-positive harmonic envelope
with a uniform positive floor on ternary units and with
\(G_0(2^E r)/(2^E r)\to0\) for every fixed odd \(r\).
The companion Abel/harmonicization construction supplies such an envelope,
subject to its stated analytic inputs.

For every \(\varepsilon>0\),

\[
G_\varepsilon=G_0+\varepsilon\widetilde h
\]

has all of those same properties. Linearity is legitimate because both
nonnegative inverse sums are finite. But

\[
\frac{G_\varepsilon(q_j)}{q_j}\ge\frac{4\varepsilon}{15}
\qquad(j\ge1),
\]

so \(G_\varepsilon(q)/q\to0\) fails along ordinary odd units.
Likewise, adding \(\varepsilon\widetilde h\) to an excessive envelope
before harmonicization leaves that summand in every iterate \(P^kF\).
Harmonicization by itself does not remove it.

This is a counterexample to the inference from these **properties** to
global sublinearity. It is not a counterexample to the desired existence
of a sublinear envelope. In particular \(G_\varepsilon\) is not claimed
to arise from the specified Abel averages with seed \(D_0=1\). An
argument using that specific provenance, or an additional minimality or
uniform-integrability condition, may distinguish the wanted envelope
from these atomic additions.

## 5. A version with unbounded marked nodes

The explicit bounded-exponent ray need not have unbounded marked nodes.
For the stronger band statement use the following separate, proved input:

> Every positive odd ternary unit has arbitrarily large positive odd
> ternary-unit marked ordinary predecessors.

One source-qualified Lean route is PR176 at
`3dbe5542fd6a5a1d63b354225d92391471c17002`, under
`research/lean-global-resolvent-20261121/section/lean/`:

- `BandSteering.lean`: `Band.goodScale_cofinal` and
  `Band.steered_root_with_clock`;
- `FanGeometry.lean`: `oddFan_spec`, `oddFan_lower`, and
  `oddFan_marked_of_phase`;
- `BandCriterion.lean`: `Band.marked_ancestors_with_clocks`.

The selected leaf is a unit by `oddFan_spec`; it is at least the steered
root, which is at least \(2^Q\), by `oddFan_lower`. Good scales are
cofinal. This inspection uses the stated source theorems; it is not an
independent fresh build of that PR. The earlier marked-population theorem
in this packet provides another source-qualified route.

Start again with the finite ray \(1,5\). Given its current outer odd
endpoint \(q\), choose a marked unit predecessor \(m\) greater than
every existing node and the current stage bound. Append the reversed
odd-step path from \(m\) to \(q\), stopping at its first hit of \(q\).
Every added odd state is a unit. There can be no repeated state on this
path, and it cannot meet the old ray except at \(q\): such a meeting
would give a positive return of the nonperiodic point \(q\), which
already has an actual path to one and is different from one.

Iteration constructs a simple infinite ordinary inverse ray containing
unbounded marked nodes. Intermediate values need not be monotone in
height. Define \(h\) by the same recursion (H3) along every successive
edge. The proofs of harmonicity, pointwise finiteness, and (H5)--(H7)
are unchanged. On each fixed dyadic ray there are still only finitely
many nonzero values, although there is no common cutoff six. At every
selected marked node,

\[
                    h(q)/q\ge4/15.
\]

Adding this version to \(G_0\) shows that harmonicity, a uniform floor,
and raywise decay alone do not even imply sublinearity restricted to
the actual marked section. All nodes of the construction still converge
to one. The additional input here is only marked-ancestor cofinality,
not a convergence conjecture or a hypothetical bad component.
