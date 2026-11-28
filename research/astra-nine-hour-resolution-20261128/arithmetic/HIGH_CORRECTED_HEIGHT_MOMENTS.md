# Physical-source moments near unit corrected-height ratio

**PROPOSED written results conditional on the existence of one escaping component \(C\).** Set \(F(n)=n/H(n)\) on \(C\) and zero elsewhere. Here \(H\) is the corrected height from the [ordinary pressure note](ORDINARY_CONFORMAL_PRESSURE.md). For \(p>0,\ \kappa>1\) define
\[
 M_{p,\kappa}(E)=\sum_{n\in E}F(n)^p n^{-\kappa},\quad
 Z_\kappa(p)=M_{p,\kappa}(\mathbb N),\quad
 D_X(p)=X^{-1}\sum_{n\le X}F(n)^p .
\]
Use \(\underline D,\overline D\) for the lower and upper limits as \(X\to\infty\). The estimates also apply to a union of escaping components, with the lower bounds requiring a nonempty union. No existence is asserted.

## Subinvariance and ternary concentration

Write \(u=2^{-\kappa}\), \(v=(3/2)^\kappa\). Even-source masses satisfy \(m(2n)=u m(n)\). For a positive odd source \(x\) and \(y=(3x+1)/2\),
\[
 m(x)=v(1+1/(3x))^{\kappa-p}m(y).
\]
Consequently \(p\ge\kappa\) gives \(m(x)\le v m(y)\). The mass fraction in \(2\bmod3\) is at least \((1-u)/v=(2^\kappa-1)/3^\kappa\), strictly greater than \(1/3\) for \(1<\kappa<2\). The equivalent inequality \(2^{-\kappa}+\frac13(3/2)^\kappa<1\) follows from strict convexity and the endpoint values one.

More precisely put
\[
 K=\frac{3^\kappa}{2^\kappa-1},\qquad d=\log_3 K,\qquad
 s=\log_3(2^\kappa-1)=\kappa-d .
\]
For \(1<\kappa<2\), \(0<d<1\). The probability \(\nu=M_{p,\kappa}/Z_\kappa(p)\), projected onto the ternary integers, satisfies
\[
 \nu\le A\nu,\qquad
 A\delta_y=u\delta_{2y}+v\,\mathbf1_{y=2\bmod3}\delta_{(2y-1)/3}.
 \tag{1}
\]
Every weak limit as \(p\to\infty\) satisfies (1), since these branch domains are clopen. If \(g_l(z)=3^l\nu(z\bmod3^l)\), then
\[
 g_l(z)\le u g_l(z/2)+(v/3)g_{l+1}((3z+1)/2).
\]
In Haar \(L^q\), \(1\le q\le\infty\), the last composition has norm at most \(3^{1/q}\|g_{l+1}\|_q\). Iteration from \(g_0=1\) gives
\[
 \|g_l\|_q\ \ge\ 3^{(1-d-1/q)l},\qquad
 \max_{c\bmod3^l}\nu(c\bmod3^l)\ \ge\ 3^{-dl}.                 \tag{2}
\]
In particular no limit has a Haar density in \(L^q\) for \(q>1/(1-d)\). An absolutely continuous obstruction shows why one cannot infer singularity. For \(1-\log_3 v\le b<1\), the integrable Haar density \(g(z)=|z+1|_3^{-b}\) satisfies \(g\le A g\) almost everywhere, where \(A\) acts on densities as \(u g(z/2)+(v/3)g((3z+1)/2)\). The second term alone equals \(v3^{b-1}g(z)\). This gives a nonordinary subinvariant test law supported throughout the ternary integers.

There is a complementary absolute upper estimate at native precision:
\[
 M_{p,\kappa}(c\bmod3^l)\ \ll_\kappa\
 p^{-s}3^{-dl},\qquad 0\le l\le\lfloor\log_3 p\rfloor,\quad p\ge\max(\kappa,3). \tag{3}
\]
For the proof first count only odd starts. Their accelerated \(r\)-step word \(w\) has positive gaps \(e_1,\ldots,e_r\) with total \(S\) and slope \(a=3^r2^{-S}\). Exact correction transport gives \(m(x)\le a^\kappa m(y)\) for the odd endpoint \(y\). For a fixed word, initial class \(c\bmod3^l\) requires one target class modulo \(3^{r+l}\). This follows from \(2^S y=3^r x+B_w\) with integral intercept. The word acts injectively on its legal sources. Every \(n\in C\) reaches an odd state \(z\le n\) by halving, so \(F(n)\le\exp(-1/(4n))\) by \(\log(1+1/(3z))\ge1/(4z)\). The unimodal envelope \(t^{-\kappa}\exp(-p/(4t))\) has integral \(O_\kappa(p^{1-\kappa})\) and maximum \(O_\kappa(p^{-\kappa})\). Summing over either monotone side on a progression of modulus \(Q\) gives the bound \(O_\kappa(p^{1-\kappa}/Q+p^{-\kappa})\), uniformly in its residue. The word weights sum to \(K^r\); choose \(r=\lfloor\log_3 p\rfloor-l\). This proves (3) for odd starts. For all starts, sum the images under the powers of two, which permute ternary classes and contribute the geometric weights \(u^j\).

If \(w\) is a forward odd word of \(r\le\log_3p\) gaps, the same argument, now applying (3) to its target class, gives the wordwise bound
\[
 \sum_{x\ {\rm odd\ with\ prefix}\ w}m(x)
 \ll_\kappa p^{-s}\prod_{j=1}^r(2^\kappa-1)2^{-\kappa e_j}.      \tag{4}
\]
The product on the right is an independent geometric probability. Normalization by the true \(Z_\kappa(p)\) can increase the right side considerably.

## Comparison with the stronger absolute barrier bound

Write \(m_*(n)=\min_{j\ge0}T^j(n)\). This is odd and \(F(n)^p\le\exp[-p/(4m_*(n))]\) on \(C\). Wren's written fixed-barrier Corollary 2 states that for some \(\xi>1-H_2(\log_3 2)\), the count of \(n\le X\) with \(m_*(n)\ge Y\) is \(O(XY^{-\xi})\), uniformly for all \(X,Y\ge1\). Its external mixing and certified-stage inputs are used here as published, without a local formal rebuild. [Wren 67, Corollary 2](https://rstation.ai/problems/collatz/papers/67/v1).

Partition \(m_*(n)\) at the dyadic scales above and below \(p\). On the intervals above \(p\) the convergent geometric count alone suffices. Below \(p\) the weight at scale \(2^{-j}p\) contributes \(O(e^{-2^j/8})\) alongside the count. Thus
\[
 \sup_{X\ge1}D_X(p)\ll p^{-\xi},\qquad
 Z_\kappa(p)\ll_\kappa p^{\,1-\kappa-\xi}\quad(p\ge 3).          \tag{5}
\]
For the second estimate, on each dyadic ordinary height interval \(N\le n<2N\) factor off \(F^{p/2}\le\exp(-p/(16N))\) and apply the first estimate at \(p/2\) to the other half. The sum over \(N\) is \(O_\kappa(p^{1-\kappa-\xi})\).

In particular (3) at \(l=0\) is superseded by (5) for every \(1<\kappa<2\). Indeed \(\max_\kappa(s+1-\kappa)=1-H_2(\log_3 2)\), attained where \(1-2^{-\kappa}=\log_3 2\). A weak-limit argument assuming \(Z_\kappa(p)\asymp p^{-s}\) would therefore start from an excluded case.

## Lower natural moments from the physical inverse intercept

For \(0<t\le1/2\) and \(p\ge1\) the same physical sources give
\[
 \underline D((1-t)p)\ \ge\ c\,t^2 p\, Z_2(p),                   \tag{6}
\]
with an absolute \(c>0\). This direction compares a natural lower mean with the sum of the weighted atoms at ordinary heights. It does not assume a relative trit equidistribution theorem.

We first justify a uniform predecessor observation. At any nonperiodic positive odd unit \(y\), for \(0<\epsilon\le1/2\), there is a set \(G_y\) of odd positive predecessors of lower natural density at least \(c_0\epsilon/y\). Their inverse word has affine intercept \(\beta\) at the root at most \(c_1\epsilon\), with \(c_1\) as small as desired by an absolute change in \(c_0\). Here the inverse endpoint is \(x=(2^S/3^r)(y-\beta)\). Choose an integer \(v\) in a string of six consecutive integers within \(O(1)\) of \(\log_2(1/\epsilon)+C\), so \(2^vy\equiv4\bmod9\), and first step outward to the unit \(z=(2^vy-1)/3\asymp y/\epsilon\). Enlarge \(C\) so \(z>2B\), where \(B\) is the absolute real-intercept cap in the external central-clock word count. For large \(X/z\) write \(L=\log_2(X/(2z))\). For all positive \(r\) in a sufficiently narrow \(c\sqrt L\) window about \(L/(2-\log_23)\), put \(S=\lfloor L+r\log_23\rfloor\). Then \(|S-2r|\le\sqrt r\). At least \(c2^S/(3^r\sqrt r)\gg X/(z\sqrt r)\) integral inverse words at \(z\) have \(\beta'\le B\). Their distinct sources lie below \(X\). Rows at different \(r\) are disjoint for nonperiodic \(z\), as holds when \(y\in C\). Summing in \(r\) gives at least \(cX/z\) sources. Composition with the first letter gives \(\beta=2^{-v}(1+3\beta')\le c_1\epsilon\). Only nonperiodic roots are needed in this observation. The external input is the written fixed-total real-intercept floor, without a local formal rebuild. [Weaver and Wren, bounded-intercept input (3.4) as quoted in Paper 200](https://rstation.ai/problems/collatz/papers/200/v1).

Write \(L(n)=-\log F(n)\) for \(n\in C\). By the exact homogeneous transport of \(H\), for \(x\in G_y\)
\[
 F(x)=F(y)(1-\beta/y),\qquad
 L(x)\le L(y)+2c_1\epsilon/y\le (1+8c_1\epsilon)L(y).
\]
The last step uses \(L(y)\ge1/(4y)\). Take \(\epsilon=t\) and \(c_1\le1/16\). Then \(F(y)^p\le F(x)^{(1-t)p}F(y)^{tp/2}\) on \(G_y\). On any single escaping orbit, for every \(a>0\),
\[
 \sum_{y\ {\rm odd\ on\ orbit}} F(y)^a/y\le4/a
\]
because \(F(Ty)^a-F(y)^a\ge aF(y)^a/(4y)\) on odd departures and \(F\) is constant on even departures. Hence for every physical \(x\),
\[
 \sum_{\substack{y\ {\rm odd\ unit\ in}\ C\\x\in G_y}} F(y)^p/y
       \le \frac8{tp}F(x)^{(1-t)p}.
\]
Apply this to finite subsets of targets, take lower natural means, use the lower density of \(G_y\), and then exhaust the targets. This proves (6) with the sum restricted to odd units. To pass to all positive \(n\), dyadic lifts have a summable factor \(4^{-j}\). Every odd divisible by three maps under the accelerated odd map to a positive odd unit \(y\). Its weight \(F(x)^p/x^2\) is at most \(C4^{-e} F(y)^p/y^2\) when its gap is \(e\), using \(x=(2^e y-1)/3\). There is at most one such \(x\) per \(y,e\). This proves (6).

The argument also gives a finite ordinary-height bound with a moving prescribed ternary class. There are absolute \(c,C>0\) such that for \(0<t\le1/2\), \(p\ge1\), \(h\ge0\), and every \(b\bmod3^h\),
\[
 \frac{3^h}{X}\sum_{\substack{n\le X\\n=b\bmod3^h}}F(n)^{(1-t)p}
 \ \ge\ c t^2p\sum_{n\le c t X e^{-Ch}}F(n)^p/n^2 .              \tag{8}
\]
Indeed, in each row at \(z\), prescribing the final inverse source \(x=b\bmod3^h\) prescribes \(\beta'=z-3^r2^{-S}b\bmod3^{r+h}\), a unit class. The same input (3.4) permits every \(h\le\delta r\), with loss exactly \(3^{-h}\) in its count lower bound. The narrow clock window works uniformly for \(X/z\) above an absolute threshold, and \(h\le\delta r\) throughout it whenever \(z\le c X e^{-Ch}\). Consequently \(\#\{x\le X:x\in G_y,\ x=b\bmod3^h\}\gg tX/(3^hy)\) uniformly for \(y\le c t X e^{-Ch}\). Apply the same orbit telescope before taking any limit in \(X\). For the upgrade from odd units to all positive sources, the odd part of \(n\) is at most \(n\) and its next odd state is at most \(2n\), so reducing the cutoff constant suffices. The right side is zero when its cutoff is below one.

Let \(\eta<1\) be the exponent from the uniform distinct-orbit packing bound and \(\Delta=1-\eta\). At a future minimum \(y\), dyadic summation gives \(L(y)\ll y^{-\Delta}\). Each large \(Y\) has such an odd unit \(y\in[Y,2Y]\) on any fixed escaping orbit: pass the last state below \(Y\), then minimize the remaining tail, whose initial state is at most \((3Y+1)/2\). Taking \(Y=p^{1/\Delta}\), \(F(y)^p\gg1\). The preceding bounded-intercept source set for fixed \(\epsilon\) gives
\[
 \underline D(p)\gg p^{-1/\Delta},\qquad
 Z_\kappa(p)\gg_\kappa p^{-\kappa/\Delta}.                        \tag{7}
\]
These are deliberately coarse. The implied onset in (7) may depend on the chosen component. Equations (5) and (7) permit multiplicative subsequences on which each moment's ratio between \(p/2\) and \(p\) stays bounded. For instance a lower-mean doubling subsequence in (6) gives \(pZ_2(p)\ll\underline D(p)\) there. Simultaneous regularity at all scales or for every choice of moments has not been established here.

## Remaining issue

The true normalizer can be much smaller than the native envelope (3). Equation (6) obtains many actual positive sources with the required weight. Controlling their *relative* distribution inside the high-moment ensemble, particularly through transport between ordinary heights near \(p\) and heights much larger than \(p\), remains open. Neither escape nor an additional finite cycle is excluded.
