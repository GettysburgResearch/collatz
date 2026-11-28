# What the missing one-eighth lower bound must establish

**SOURCE-QUALIFIED reduction; eight infinite-series theorem roots checked in Lean.**
The statistic is synchronous equality of two independently sampled ordinary
sources at the median shortcut clock, with the normalization and analytic
inputs fixed in [PR 214's phase-dispersion proof](../astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md).
It is not an asynchronous meeting probability or a success rate among a
selected collection of merger certificates.

The existing source-qualified law is

\[
 L=\lim_{X\to\infty}\Pr\{T^{H_X}n_1=T^{H_X}n_2\}
   =\frac14\sum_{C\text{ cyclic}}\frac{d_C^2}{P_C}\le\frac18.
\]

Here the sources are uniform in the specified initial interval, \(P_C\) is
the actual shortcut period, and \(d_C\) is the component's ordinary density.
Every positive cycle has period at least two. The known component has period
two and density \(b>0\), where positivity uses the named predecessor theorem.
The formula, density existence, Gaussian clock law, and predecessor theorem
remain external analytic inputs. The present Lean module does not postulate
any of them as an axiom.

## The complete countable series

Write the other cycle masses as \(w_i\ge0\), their periods as \(P_i\ge2\),
and allow arbitrary unused mass:

\[
 b+\sum_i w_i\le1,
 \qquad
 L=\frac{b^2}{8}+\sum_i\frac{w_i^2}{4P_i}.
\]

Unused mass can include nonperiodic components. No finiteness of the cycle
list, and no assumption that all mass is periodic, is used. Term by term,

\[
 0\le\frac{w_i^2}{4P_i}
 \le\frac{(1-b)w_i}{8}.
\]

The dominating series is summable. Summing and using the mass budget gives

\[
 L\le\frac{b^2+(1-b)^2}{8},
 \qquad
 \boxed{\frac18-L\ge\frac{b(1-b)}4.}                         \tag{1}
\]

Since \(b>0\), a lower bound \(L\ge1/8\) forces \(b=1\). Conversely,
\(b=1\) forces every other nonnegative mass to vanish, and gives \(L=1/8\).
Thus the endpoint lower bound is precisely the full-known-basin-mass claim
within this analytic representation. If one ordinary counterexample existed,
the positive-predecessor theorem would give a positive-density bad set,
contradicting \(b=1\). This last use of the predecessor theorem is what turns
the density endpoint into universal convergence.

For a quantitative version, any independently proved floor \(0<c\le b\)
and estimate \(L\ge1/8-\epsilon\) give

\[
                     c(1-b)\le4\epsilon.                    \tag{2}
\]

A single fixed positive \(\epsilon\) does not imply full convergence.
Bounds approaching the endpoint with no fixed deficit would do so. The
already known bound \(L\ge b^2/8>0\), and near-quadratic counts whose
normalized proportion can tend to zero, do not establish that endpoint.
The latter progress is already in [PR 216](https://github.com/GettysburgResearch/collatz/pull/216),
at `1917b07ae5cc8f5d27c79f34cc43a4bcf25efff8`, and is not claimed as new here.

## A different full-proof estimate found in this pass

For the exact component indicator \(f_1\), define the adjacent boundary
\(D=\{n\ge1:f_1(n+1)\ne f_1(n)\}\). The new
[dyadic boundary theorem](collision/DYADIC_BOUNDARY_ZERO_ONE.md) proves,
using the same positive-predecessor input,

\[
              \text{Collatz}\quad\Longleftrightarrow\quad
                          \sum_{n\in D}\frac1n<\infty.       \tag{3}
\]

The forward implication is immediate. For the reverse implication, exact
halving gives a locally summable sequence of dyadic interpolation changes;
the exact odd relation makes its binary limit invariant under both real
dilations two and three. Irrational rotation makes that limit constant, and
positive predecessors exclude a nonempty color of zero density. This proof
does not need the Gaussian minimum law.

Equation (3) is an exact target, not a proved summability bound. The generic
synchronous pair estimate is only \(O(X/\sqrt{\log X})\) for the boundary
count and is not summable after dyadic normalization. The
[explicit halving-only construction](collision/SHARP_HALVING_BOUNDARY.md)
shows that even \(O(X/\log X)\), exact halving, and an existing density of
one-half do not suffice. The genuine odd equation must supply the missing
regularity, or a different ordinary arithmetic argument must replace it.

## Formal scope and reproducibility

[CollisionThreshold.lean](CollisionThreshold.lean) proves eight public roots:

1. Nonnegativity and the termwise remaining-mass bound.
2. Summability of all other-cycle contributions.
3. The complete two-mass upper bound.
4. The deficit inequality (1).
5. The maximal-lower-bound implication \(b=1\).
6. The quantitative implication (2).
7. The full-mass evaluation \(L=1/8\).
8. The equivalence of the maximal lower bound and full known mass.

The [runner](check_collision_threshold.py) freshly compiles the module and
then separately imports, checks the types of, and audits all eight roots.
The [receipt](../../reports/astra-collision-factor-bridge-20261128/collision-threshold-lean.json)
records Lean 4.34.1, Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`, exact source and runner digests,
and only `Classical.choice`, `Quot.sound`, and `propext` in the axiom closures.
Pinned compiled dependencies were reused. This is a fresh proof replay of
the displayed series argument, not a cold dependency build, independent
LeanChecker run, or formal proof of the external median law.

**First unsupported step:** no lower bound of \(1/8\), no summability in
(3), and no substitute full-mass theorem has been established in this pass.
The formal result prevents a partial lower bound from being mistaken for
the full endpoint.
