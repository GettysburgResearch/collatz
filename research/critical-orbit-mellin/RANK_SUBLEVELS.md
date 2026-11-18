# Lower-rank merges in native rank sublevels

**PROPOSED.** On the section \(\mathcal H=\{n\ge1:n\equiv1\bmod3\}\), use the repository's rank
\[
 2n+1=3^v u,\qquad 3\nmid u,\qquad P(n)=3^v u^2 .
\]
The rank is injective there: the valuation of \(P(n)\) gives \(v\), then its residual square gives the positive \(u\). We consider physical shortcut certificates \(T^r(n)=T^r(m)\), with \(m\in\mathcal H\) and strict \(P(m)<P(n)\). The [existing rank program](../astra-critical-mass/MINIMUM_RANK.md) also permits unequal clocks.

Write \(h=H_2(\log_3 2)\). There is a common finite clock \(r_Y=O(\log Y\log\log Y)\) such that among \(\mathcal H_Y=\{n\in\mathcal H:P(n)\le Y\}\), all but
\[
 O\!\left(Y^{h/2}(\log Y)^{-3/2}\right)                     \tag{1}
\]
have such a certificate with \(m\in\mathcal H_Y\) and \(r=r_Y\). This is relative to the intrinsic rank population, which is \(\asymp\sqrt Y\). Numerically \(h/2=0.47497776\ldots\). Bounds on \(\mathcal H_Y\) solely by its ordinary diameter would lose this relative saving.

## A finite-coalescence bound in progressions

Let \(p=\log_3 2\) and \(\kappa=\log(p/(1-p))/\log 3\). For an odd positive step \(d\), take any progression of \(A\ge16\) consecutive indices and retain just its positive values. There is a clock \(O(\log(2dA)\log\log(4dA))\), uniform in translation, for which the number of distinct endpoints is at most
\[
 C (1+\log d)d^\sigma\,\frac{A^h}{(\log A)^{3/2}},
 \qquad \sigma=\max(h/3,2\kappa/3)<h/2 .                    \tag{2}
\]
For the stated strict inequality one can use \(0.6309<p<0.6310\), \(0.949<h<0.951\), \(0.487<\kappa<0.490\); these loose inequalities follow directly from the displayed elementary logarithms.

Indeed, put \(L=\lfloor\log_2 A\rfloor\), \(u(t)=\min(t,L-t)\), \(c_u=K(1+u)^2\) with any fixed \(K\ge2\), and capture if \(2\cdot3^{q_t-pt}\le d^{-2/3}/c_{u(t)}\). In the progression each length-\(L\) parity word occurs at most twice, since the odd stride permutes dyadic residues. Uncaptured paths obey the [curved ballot bound](CRITICAL_MOMENT.md) with endpoint allowance \(a=\log_3(2K)+(2/3)\log_3 d\). The tilted count is \(O(F(A)(1+a)e^{\lambda a})\), where \(\lambda=\log(p/(1-p))\) and \(F(A)=A^h/(\log A)^{3/2}\). This gives the \(d^{2\kappa/3}\) term.

For each captured pair \((t,q)\), the physical input interval has length at most \(dA\), and the endpoint interval has width \(W=2\cdot3^{q-pt}dA\le d^{1/3}A/c_{u(t)}\). After spending the first \(t\le L\) steps, reserve the [critical finite coalescence clock](FINITE_COALESCENCE.md) for widths up to \(dA\). For \(W\ge\sqrt A\) its bound is \(O(W^h/(\log A)^{3/2})\). Sum over the geometric widths in \(q\) and the two copies of each \(u(t)\), using \(\sum c_u^{-h}<\infty\). This costs \(O(d^{h/3}F(A))\). For \(W<\sqrt A\) all pairs together cost \(O(L^2(1+\sqrt A))=O(F(A))\). This proves (2). No uniform mixing of values modulo the odd stride is assumed.

## Summing the ternary-depth slices

At \(v\ge1\), \(d=3^v\), the possible positive \(u\) are odd, at most \(\sqrt{Y/d}\), and prime to 3. Ignoring the last restriction covers all \(n=(du-1)/2\) by one progression with step \(d\) and \(A\le 1+\sqrt{Y/d}\) consecutive indices. The contribution to \(\#\mathcal H_Y\) summed over \(v\) is \(O(\sqrt Y)\). The \(v=1\) slice gives a matching lower bound.

When \(d\le\sqrt Y\), use the whole covering progression with \(A=\lceil\sqrt{Y/d}\rceil\). Then \(\log A\gg\log Y\), and by (2) the number of distinct images is at most
\[
 C\frac{Y^{h/2}}{(\log Y)^{3/2}}(1+\log d)d^{\sigma-h/2}.
\]
The sum over \(d=3^v\) converges uniformly. When \(d>\sqrt Y\) the total number of inputs is \(O(Y^{1/4}+\log Y)\) by a geometric tail. No count for \(d>Y\) is needed. Choose a common clock larger than every slice clock; in the enlarged progressions used above \(dA\le2Y\). Later iteration cannot increase the image cardinality. Thus the whole sublevel has at most the number in (1) of distinct images. Retain the unique least-\(P\) member of each image fiber. Every remaining input merges with it at the common clock, proving (1).

It follows by dyadic summation that the \(P^{-h/2}\) weights of section states with no cheaper equal-time partner in the entire section have finite total mass. The same conclusion holds for the subset with no cheaper asynchronous partner. This argument gives no pointwise certificate for those possible permanent minima, including a hypothetical least-rank exceptional source.
