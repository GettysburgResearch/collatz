# A summable component boundary would give the full collision endpoint

**PRIOR THEOREM, independently reconstructed in a harmonic-boundary formulation; the closing estimate remains OPEN.** The map is the genuine shortcut
\(T(2n)=n,\ T(2n+1)=3n+2\) on positive ordinary integers. A basin label means a function
\(f:\mathbb N_{>0}\to\{0,1\}\) satisfying \(f(Tn)=f(n)\) at **every** positive integer.
Thus it labels entire asynchronous components, rather than the synchronous phases within a component.

**Priority correction from the current literature check.** Lean Assurance Lab's [Paper 212, version 1, November 23, 2026](https://rstation.ai/problems/collatz/papers/212/v1), section *Density from dyadic siblings*, already proves the summable-sibling zero-one theorem, using the same binary interpolation limit and invariance under dilations by two and three. It also gives the positive-predecessor upgrade and permits finitely many exceptional edges. The argument below was reconstructed independently before that source was located; it is not claimed as a new zero-one theorem. Full adjacent harmonic energy and summable dyadic sibling variation are equivalent under exact halving, by the finite boundary-creation identity and its geometric shell sum. The distinct work in this lane is the [sharp halving-only counterlabel](SHARP_HALVING_BOUNDARY.md), the explicit [one-edge collision calibration](ONE_EDGE_COLLISION_SPLIT.md), and their separately scoped finite kernels.

Write
\[
 D_f=\{n\ge1:f(n+1)\ne f(n)\},\qquad
 \mathcal E(f)=\sum_{n\in D_f}\frac1n.
\]

The following implication needs no minimum-clock, Gaussian, or phase-distribution theorem:

> If \(\mathcal E(f)<\infty\), the natural density of \(f=1\) exists and is either zero or one.

With the independently imported positive-predecessor theorem, this strengthens to: **every such finite-energy basin label is constant at every positive integer.** In particular, for the indicator \(f_1\) of the basin of the known cycle \(1\leftrightarrow2\),
\[
 \boxed{\quad \text{Collatz}\quad\Longleftrightarrow\quad
       \sum_{\substack{n\ge1\\f_1(n+1)\ne f_1(n)}}\frac1n<\infty.\quad}       \tag{1}
\]

Finiteness, rather than a zero boundary, is the sufficient analytic estimate. It is **not established here**. The known adjacent synchronous coalescence estimate only supplies a nonsummable majorant. This is a full-proof target at the ordinary asynchronous boundary; it is not an evaluation of the median collision probability.

## 1. Exact dyadic interpolation

More generally, first suppose only that \(f(2n)=f(n)\). For \(x>0\) and sufficiently large \(j\), put
\[
                 F_j(x)=f(\lfloor2^j x\rfloor).
\]
On the first half of a mesh cell \([m2^{-j},(m+1)2^{-j})\), \(F_{j+1}=f(2m)=f(m)=F_j\). On its second half,
\[
                 |F_{j+1}-F_j|=|f(2m+1)-f(2m)|.
\]
Consequently, on \([1,2)\), the identity is exact:
\[
 \|F_{j+1}-F_j\|_{L^1([1,2))}
 =2^{-j-1}\sum_{m=2^j}^{2^{j+1}-1}|f(2m+1)-f(2m)|.                    \tag{2}
\]
The same estimate on any compact \([a,b]\subset(0,\infty)\) has at most two partially covered cells. Summing it over \(j\), each even boundary index participates in a bounded number, depending on \(a,b\), of comparable dyadic scales. Thus \(\mathcal E(f)<\infty\) implies
\[
          \sum_j\|F_{j+1}-F_j\|_{L^1([a,b])}<\infty.                   \tag{3}
\]
By Tonelli, \(F_j(x)\) changes only finitely many times for almost every \(x\) in each such compact interval. A countable exhaustion gives an almost-everywhere limit \(F\) on \((0,\infty)\), still taking only the values zero and one. Dominated convergence also gives local \(L^1\) convergence.

There is a simpler version when a natural density \(d\) is already known. For every interval \([a,b]\subset(0,\infty)\), the cumulative density asymptotic implies
\[
            \int_a^b F_j(x)\,dx\longrightarrow d(b-a).
\]
Together with the binary local \(L^1\) limit, this forces \(F=d\) almost everywhere and hence \(d\in\{0,1\}\). This version uses exact halving and the density assumption, without the odd equation.

## 2. The exact odd equation removes the density assumption

For the actual basin label,
\[
              f(2m+1)=f(3m+2)                                      \tag{4}
\]
holds at every \(m\ge0\) for which the positive inputs occur. Directly from the interpolation definition,
\(F_j(2x)=F_{j+1}(x)\), so \(F(2x)=F(x)\) almost everywhere.

Fix a compact positive interval. If \(m=\lfloor2^j x\rfloor\), the indices \(\lfloor3\cdot2^j x\rfloor\) and \(3m+2\) differ by at most two. The indices \(\lfloor2\cdot2^j x\rfloor\) and \(2m+1\) differ by at most one. Using (4), integrating the corresponding adjacent differences, and enlarging the compact interval a fixed amount bounds
\[
   \|F_j(3\,\cdot)-F_j(2\,\cdot)\|_{L^1([a,b])}
        \le C_{a,b}\,2^{-j}
               \#\bigl(D_f\cap[c_{a,b}2^j,C_{a,b}2^j]\bigr).          \tag{5}
\]
The right side tends to zero: it is bounded by a constant times the tail of the convergent series defining \(\mathcal E(f)\). Passing to the local \(L^1\) limit gives \(F(3x)=F(2x)=F(x)\) almost everywhere.

Set \(G(u)=F(e^u)\). It is a bounded measurable function invariant under translations by both \(\log2\) and \(\log3\). Their ratio is irrational, since an equality \(2^r=3^s\) with positive integers is impossible. Regard \(G\) as an \(L^1\) function on the circle of circumference \(\log2\). Its Fourier coefficient at a nonzero integer \(k\) is multiplied, under translation by \(\log3\), by
\(e^{2\pi i k\log3/\log2}\ne1\); invariance therefore makes that coefficient zero. The Fejér means converge in \(L^1\), so \(G\), and hence \(F\), is constant almost everywhere. Its constant value \(d\) is zero or one.

The local \(L^1\) convergence gives uniform convergence of the partial integrals
\[
 \sup_{1\le u\le2}\left|\int_1^u F_j(x)\,dx-d(u-1)\right|\to0.
\]
These are the normalized counts on all partial dyadic shells, with an endpoint error \(O(2^{-j})\). Summing earlier complete shells geometrically proves
\(X^{-1}\sum_{n\le X}f(n)\to d\) at every cutoff \(X\), as claimed.

## 3. From density zero-or-one to every ordinary source

Use Mazur's positive-predecessor result in precisely the following form: for each fixed positive shortcut target prime to three, its full set of ordinary predecessors has positive lower natural density. This is an external theorem, not a consequence of the interpolation argument. The original full-map theorem and its shortcut conversion are [Theorem 1.1 and equation (1.3)](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf); its independently reported verification scope is recorded [here](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html).

Explicitly, for a shortcut target \(v\) prime to three, apply the full-map positive-density theorem to the ordinary target \(2v\). Every full-map predecessor of \(2v\) is a shortcut predecessor of \(v\) after the odd-step/halving conversion in that equation. This is the normalization used below.

If either color occurs at any positive source, follow its orbit until an odd departure. Such a departure exists because repeated halving reaches an odd positive integer. The resulting shortcut target is prime to three and has the same color. Every predecessor of that target has that color. Each nonempty color therefore has positive lower density. The zero-or-one conclusion permits only one nonempty color. Applying this to \(f_1\) proves (1), since the color of 1 is one. Under Collatz the reverse implication is immediate: \(f_1\) is identically one and its boundary is empty.

This also makes clear that no rate or effective uniformity in the predecessor theorem is required here. One target is fixed after choosing a nonempty color.

## 4. What estimate would close the route?

Let \(D_j=\#(D_{f_1}\cap[2^j,2^{j+1}))\). Then
\[
        \mathcal E(f_1)<\infty
        \quad\Longleftrightarrow\quad
        \sum_{j\ge0}2^{-j}D_j<\infty.                                \tag{6}
\]
For example, the uniform bound
\[
          D_j\le C\,2^j j^{-1-\epsilon}\qquad(j\ge1)                  \tag{7}
\]
for any fixed \(\epsilon>0\) suffices. A summable sequence of non-power errors would suffice as well.

The previously used exact-cylinder adjacent synchronization theorem gives only
\(D_j=O(2^j/\sqrt j)\), because different basin labels cannot synchronize. Its proof counts words of a native length comparable to \(j\); the Haar survival tail is of order \(j^{-1/2}\). That is not summable. See the source pins and complete density-transfer argument in [the prior synchronous phase proof](../../astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md), and [Duran's Corollary C](https://doi.org/10.5281/zenodo.23003524) / [Leen's exact rates](https://doi.org/10.5281/zenodo.23268751).

The boundary in (6) is **asynchronous and component-valued**. A nonzero synchronous phase boundary can occur even when both numbers eventually enter the known cycle. Bounding that larger synchronous boundary by a summable series is not the intended target.

One tempting improvement is to allow a bounded number of different terminal clocks in the pair coupling. This does not improve the generic Haar absorption tail by itself. On each pair of specified parity words, an equality
\(T^r(n)=T^s(n+1)\) is an affine equation in \(n\). If it holds for two distinct sources, the slopes agree, so
\(3^a/2^r=3^b/2^s\); unique factorization gives \(r=s\) and \(a=b\). Therefore every unequal-time word pair contributes at most one source. There are only countably many finite word pairs, so all unequal-time mergers together have Haar measure zero. Any gain beyond the synchronous Haar estimate must use ordinary-integer endpoint information rather than a new label for the same finite-word coupling.

**First unsupported step:** no summable upper bound in (6), and no substitute that controls its accumulated dyadic variation, has been proved. The exact odd equation is used in the theorem, but has not yet supplied the needed estimate. Establishing merely that every \(D_j/2^j\to0\) does not close it.

## 5. Relationship to the requested one-eighth endpoint

At the pinned PR #214 head `504d29d399efa941a62006d1ea4635385ce6bb5f`, the source-qualified median collision law is
\[
    L=\frac14\sum_{C\text{ cyclic}}\frac{d_C^2}{P_C}\le\frac18.
\]
Together with the same positive-predecessor input, \(L=1/8\) is equivalent to Collatz. The finite-energy implication above would prove this endpoint by a different analytic estimate, and would not need the Gaussian law in its proof of convergence. It currently supplies an exact new target, not the missing lower bound.

The contemporaneous [PR #216](https://github.com/GettysburgResearch/collatz/pull/216), frozen at `1917b07ae5cc8f5d27c79f34cc43a4bcf25efff8`, already proves source-qualified positive lower bounds and near-quadratic counts of separated median mergers. Its normalization retains the unknown basin density and it explicitly leaves the one-eighth endpoint open. Those bounds are not claimed as new here.

## 6. Formal and finite verification scope

[BoundaryEnergy.lean](BoundaryEnergy.lean) contains eight checked finite roots: exact doubling and odd identities for a basin label of the actual shortcut map; binary boundary creation and its paired inequality; the complete finite-shell sum bound; the even-boundary affine identity; and both directions of the unequal-slope affine uniqueness test. The accompanying [runner](check_boundary_energy.py) freshly compiles this module and separately imports and audits every listed root using the pinned Lean 4.34.1 / Mathlib environment. Its [receipt](../../../reports/astra-collision-factor-bridge-20261128/collision/boundary-energy-lean.json) records the exact source hash and axioms.

The infinite interpolation, irrational-dilation argument, positive-density import and conclusion (1) remain written proofs. The [sharp halving-only construction](SHARP_HALVING_BOUNDARY.md) and its [finite replay](check_binary_boundary.py) delimit the unsupported estimate; a finite successful replay does not prove the asymptotic statement.
