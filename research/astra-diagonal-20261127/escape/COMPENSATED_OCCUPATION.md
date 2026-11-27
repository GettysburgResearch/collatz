# Positive compensated occupation at one ordinary clock

**Source-qualified written theorem.** On the original positive odd Collatz graph put
\[
 w_x=\frac{3x}{3x+1},\quad \phi(x)=1-w_x,\quad
 D=\log(4/3),\quad \kappa=D/2,\quad
 \alpha(x)=\frac{\rho_1(x)}x .
\]
Here \(\rho_1\) takes the values \(0,1,2\) on residues \(0,1,2\bmod3\).
Write \(d_C\) for the ordinary relative odd natural density of the full basin of a positive cycle \(C\), and \(h_C\) for its odd period. Then
\[
 \lim_{j\to\infty}\frac1j\sum_{x>0\ {\rm odd}}
   \frac{\rho_1(x)}{x(3U^j x+1)}
  =\kappa\sum_{C\ {\rm cyclic}}\frac{d_C}{h_C}
              \sum_{y\in C}\frac1{3y+1}
  \le \frac{\log(4/3)}8 .                                             \tag{1}
\]
Under the all-unit predecessor positivity input, equality holds exactly when all positive integers reach 1. The observable uses every positive odd source and its actual endpoint. It contains no assertion about a selected gate or conditional distribution of its principal seeds.

## Proof by preserving the mass released at each edge

Let \(P\delta_x=\delta_{Ux}\) and \(T\delta_x=w_x\delta_{Ux}\). The original density on inverse words gives \((T^j\alpha)(y)=\rho_{j+1}(y)/y\). The reciprocal of the actual multiplicative defect compensates each word's discount, resulting in \((P^j\alpha)(y)=\sum_{U^jx=y}\rho_1(x)/x\). The series converges for each fixed \(j,y\): every path discount is at least \((3/4)^j\). Put \(\lambda_i(y)=\phi(y)(T^i\alpha)(y)\). The exact positive identity is
\[
 P^j\alpha=T^j\alpha+\sum_{i=0}^{j-1}P^{j-i}\lambda_i.               \tag{2}
\]
At each fixed source and path, with \(f_i=\prod_{r<i}w_{U^rx}\), this is \(1=f_j+\sum_{i<j}f_i(1-w_{U^ix})\). All mass released at \(U^ix\) is carried through the remaining true steps to \(U^jx\). Nonnegativity permits exhaustion in the sources. The [Lean module](CompensatedOccupation.lean) verifies the path identity, retained endpoint, and the finite set/test version over the rationals.

Weaver's ordinary-depth theorem says \(\lambda_i\to\lambda_\infty\) in total variation, where \(\lambda_\infty(y)=h(y)/[y(3y+1)]\) in the normalized original law. The earlier component budget gives \(\lambda_\infty(\text{basin}(C))=\kappa d_C\) for each cyclic component. These are imported results; the convergence rate is unnecessary. [Weaver 176, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1) · [Component budget and its prior global identity](../../astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md)

Since \(P\) contracts the absolute mass, the replacement of all \(\lambda_i\) in the normalized sum by \(\lambda_\infty\) costs at most \(j^{-1}\sum_{i<j}\|\lambda_i-\lambda_\infty\|_1=o(1)\). After multiplying the rows by \(\phi\), the first term of (2) costs \(\|\lambda_j\|_1/j=o(1)\). For one starting point the Cesàro mean of its unweighted point masses converges in \(\ell^1\) to the uniform cycle measure if its orbit enters a cycle. The finitely many terms before entry disappear. On an escaping orbit the \(\ell^1\) norm of the mean after multiplication by \(\phi\) tends to zero, since \(\phi(U^r x)\to0\). Every positive ordinary orbit is described by one of these alternatives, without deciding any particular start. The bound \(\|\phi\|_\infty=1/4\) and the summability of \(\lambda_\infty\) permit summing these limits over the fixed source measure. This proves the stronger spatial convergence
\[
 \left\|\frac{\phi\,P^j\alpha}{j}-
      \kappa\sum_{C\ {\rm cyclic}}\frac{d_C}{h_C}
                    \sum_{y\in C}\phi(y)\delta_y\right\|_1\longrightarrow0 .      \tag{3}
\]
Summing gives (1). The same argument permits any bounded endpoint test dominated in absolute value by a multiple of \(\phi\).

For each extra cycle, all vertices are at least three and hence \(\phi\le1/10\); escaping components contribute zero. If \(d_1\) is the density of convergence to 1, the deficit from \(\kappa/4\) is at least \((3\kappa/20)(1-d_1)\) and at most \((\kappa/4)(1-d_1)\), using the ordinary total basin mass or simply that all other cycle densities sum to at most \(1-d_1\). Every counterexample would yield an odd unit successor with a positive-density predecessor set under the stated input. Thus equality excludes every counterexample. Conversely universal convergence gives \(d_1=1\) and equality. No lower estimate attaining the displayed upper endpoint has been proved. [Mazur, positive predecessor density](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) · [Lau, quantitative positive-density formulation and source](https://github.com/AxiomMath/CollatzPositiveDensity)

## Original words, canonical seeds, and all aliases

Fix an odd-clock exponent word of total \(A\), let \(m\) be its least positive odd source, and \(v=U^jm\). Put \(V=2^{A+1}\), \(W=2\cdot3^j\), and \(\omega=W/V\). Its other positive odd sources and targets are exactly \((m+Vb,v+Wb)\), \(b\ge1\). Therefore the contribution of all nonprincipal sources to the **unnormalized** left-hand sum in (1) is at most
\[
 \sum_{\text{words}}\frac{2\zeta(2)}{3VW}
       =\frac{\zeta(2)}{6\cdot3^j},                                  \tag{4}
\]
because \(\sum_{\rm words}2^{-A}=1\). The source weight \(\rho_1\) was retained and only bounded above by two. The principal-only sum thus has the same linear coefficient as the full sum. Unlike the rare-prefix first-moment problem, no drift gate is imposed, and a single source \(x\) contributes at most \(1/(2xj)\) after normalization.

Writing \(u=m/V\), \(R=v-\omega m>0\), and \(t=(R+1/3)/W\), the principal sum alone is exactly
\[
 \frac{1}{12\cdot3^j}\,\mathbb E_{\rm original}
       \left[\frac{\rho_1(m)}{u(u+t)}\right].                         \tag{5}
\]
To check the constant, \(m=Vu\) and \(3v+1=3W(u+t)\). Thus each word contributes \((3VW)^{-1}\rho_1(m)/[u(u+t)]\); extracting its original probability \(2^{-A}=2/V\) gives (5). At fixed word the other aliases have the same formula with \(u\) replaced by \(u+b\) and the correct modified source residue. The tiny \(u\) regime cannot be replaced by a continuous uniform seed without a joint estimate with this actual offset and residue. Formula (4) shows that exact digamma evaluation of the other aliases cannot create a missing linear term.

## The actual sources on the logarithmic scale

For any bounded continuous \(g:[0,\infty)\to\mathbb R\), the source-marked version of (1) is
\[
 \lim_{j\to\infty}\frac1j\sum_x
     \frac{\rho_1(x)g(\log(x)/j)}{x(3U^j x+1)}
   =\frac12\int_0^D g(t)\,dt\;
          \sum_{C\ {\rm cyclic}}\frac{d_C}{h_C}\sum_{y\in C}\phi(y). \tag{6}
\]
In particular neither fixed sources nor all sources of subexponential height carry its main term. All compact positive source-log intervals inside \((0,D)\) retain the same unknown ordinary coefficient per unit length.

To keep the source through each release, write
\[
 \lambda_i(x,y)=\frac{\rho_1(x)}x f_i(x)\phi(y)\,\mathbf1_{U^i x=y}.
\]
For each fixed positive odd unit \(y\), the normalized measure from this row has \(\log x/i\to D\) in probability. Indeed the normalized actual word measure is the canonical inverse path law, multiplied by \(\rho_1(X_i)/h(X_i)\) and a fixed factor \(h(y)\phi(y)/y\) in the unnormalized row. This reweight is uniformly bounded. The canonical division total satisfies \(S_i/i\to2\), while \(\log x=S_i\log2-i\log3+\log(y-R_i)\). A canonical path almost surely leaves a periodic root's cycle after finitely many laps, since its probability of following \(b\) full laps is \(\lambda^b\). After departure it has a positive lower defect by distinct-state packing. The same bound holds from the outset for a nonperiodic root. Hence \(\log(y-R_i)/i\to0\) along these paths. At nonunit sites there are no positive-depth rows. Tightness of \(\lambda_i(y)\) from its total-variation convergence now shows
\[
 \sum_{x,y}\lambda_i(x,y)\mathbf1_{|\log x/i-D|>\epsilon}\to0 .
\]
[Canonical word law and clock](../../astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md) · [Actual terminal reweight](../../astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md)

In (2) with the source tag, the surviving part after the final \(\phi\) test costs \(O(\|g\|_\infty/j)\). For each \(1\le i<j\), replace \(g(\log x/j)\) on the released term by \(g(Di/j)\). Good tags differ in argument by at most \(\epsilon\); these arguments lie in the compact interval \([0,D+1]\) for \(\epsilon\le1\). The exceptional mass tends to zero with \(i\) for each fixed \(\epsilon\). Bounded tests, uniform continuity on that compact interval and Cesàro averaging prove a total \(o(1)\) error, with \(i=0\) negligible. Replace each marginal \(\lambda_i\) by \(\lambda_\infty\) as before. From each fixed atom of that measure, a cyclic path has eventually periodic \(\phi(U^{j-i}y)\), and each residue of \(j-i\bmod h_C\) gives the same Riemann integral of \(g(Di/j)\) after division by \(j/h_C\). A fixed escaping path has vanishing Cesàro absolute mean under this test. Dominated convergence and \(\kappa/D=1/2\) now give (6). Fixed source-log intervals follow by approximation since the limiting source measure is absolutely continuous.

For finite truncation without asymptotic clock inputs, the part of the unnormalized sum at \(x\ge e^{16(\log2)j}\) is exponentially small in \(j\). In an octave \([X,2X)\) in this range, a terminal below \(\sqrt X\) forces division total at least \((\log_2X)/2\). For \(L=\lfloor(\log_2X)/2\rfloor-1\), the event that this total exceeds \(L\) is read modulo \(2^{L+1}\) on odds. Its geometric probability is at most \(3^j(2/3)^L\), since \(\mathbb E(3/2)^e=3\). The physical octave adds \(O(2^{L+1}/X)\) to the proportion. As \(j\le (\log_2 X)/16\), both bounds are \(O(X^{-c})\) with absolute \(c>0\). Larger endpoints have \(\phi\le1/(3\sqrt X)\). Summing the reciprocal contributions of the octaves gives the asserted tail. This gives finite positive rational approximations at each clock; taking the lower bound in (1) all the way to \(D/8\) remains open.
