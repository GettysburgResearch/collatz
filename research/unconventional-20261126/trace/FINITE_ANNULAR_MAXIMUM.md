# A sublinear depth detects the largest escape charge in every height annulus

**Status.** Proposed, source-qualified. This uses the averaged odd first-hit ramp and the small-ancestor and orbit-packing estimates. It does not evaluate the resulting limit.

Use the odd Syracuse map, the first-hit coefficients \(L_k(a)\), and \(v_N(a)=(aN)^{-1}\sum_{k=1}^N L_k(a)\) from [the first-hit spectrum](FIRST_HIT_SPECTRUM.md). Let \(b_*\) be the largest escaping-component charge, or zero if there is no escaping component. A positive maximum is attained when escape exists since \(\sum_C b_C\le c_*\). Define the finite, cycle-corrected observable
\[
 F(X,N)=\max_{\substack{X<a\le(3X+1)/2\\a\ {\rm odd}}}v_N(a)
\]
for sufficiently large integer \(X\). If \(K(X)/X^{39/40}\to\infty\), then
\[
 \lim_{X\to\infty}\ \sup_{N\ge K(X)}|F(X,N)-b_*|=0.           \tag{1}
\]
For example, the single depth \(N=\lceil X^{99/100}\rceil\) suffices, and all depths beyond it obey the same limit. Alternatively use \(K(X)/X^{19/20}\to\infty\) with the additional forward-invariant packing refinement T-A3-402, whose constant is unspecified.

For the upper bound, \(v_N(a)\le C d_a\) at every target, including cycles after the first-visit correction. Outside the union of the forward orbits of odd sources at most \(M\) this is \(O(\delta(M))\), uniformly in depth. Inside there are finitely many finite sets and one tail per represented escaping component after finite deletions. On each tail \(a_i\), the uniform averaged ramp gives
\[
 v_N(a_i)=\frac{h(a_i)}{a_i}\big((1-i/N)_++o_{i\to\infty}(1)\big),
 \qquad h(a_i)/a_i\to b_C,
\]
with the error uniform in every \(N\ge1\). As \(X\) grows, the least index from each represented tail that is present in the annulus goes to infinity whenever such vertices are present. Thus \(\limsup_X\sup_{N\ge1}F(X,N)\le b_*\) after letting \(M\to\infty\).

For the lower bound with positive \(b_*\), fix one ordinary ray of the maximizing component. Take its first state \(a_i>X\); this exists by escape, has predecessor at most \(X\) for large \(X\), and satisfies \(a_i\le(3X+1)/2\). Every earlier odd state is distinct and at most \(X\), hence
\[
 i\le 4X^{39/40}
\]
by [T-A3-401](../../astra-three-routes/pass2/ORBIT_MELLIN.md). In particular \(i\to\infty\) and \(i/N\to0\) uniformly for \(N\ge K(X)\). The same ramp gives \(v_N(a_i)\to b_*\) uniformly in those depths. If \(b_*=0\), nonnegativity completes the argument without choosing any ray.

At each displayed finite depth the original ternary cylinders are rational and can be evaluated recursively, grouping exponents by their periods modulo powers of three. The first-hit correction only needs returns of period at most the queried depth, which are decidable by that many forward steps at the target. No whole-orbit oracle is used by (1)'s finite measurement. In contrast, the empirical source labels in [the signed current](ANNULAR_ESCAPE_CURRENT.md) use complete visits. The strongest missing step here is a subsequence \(X_j\to\infty\) along which these actual finite maxima at the stated depth tend to zero. An early-depth bound below the record-crossing time cannot supply that conclusion.
