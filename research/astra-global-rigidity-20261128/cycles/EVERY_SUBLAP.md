# Physical consequences of the prior same-phase crossing theorem

**Prior crossing theorem, with new consequences below.** Weaver114 §2 already proves a strict reversal at every nonzero same-phase separation and the exact near-dyadic relation, crediting Wren for the separation-class observation. The proof here reconstructs that fact in the unscaled odd clock. The additions are the physical width-below-sixteen criterion, the actual clock padding and full rational denominators, and the near-nine matching and entropy bounds. [Weaver114/v1, §2, equations (9)–(10) and the separation-class paragraph](https://rstation.ai/problems/collatz/papers/114/v1).

Let a primitive ordinary positive cycle have \(p\) odd states \(x_i\), total halving count \(A\), minimum odd state \(s\), and maximum odd state \(X\). Use cyclic indices, write \(2^{a_i}x_{i+1}=3x_i+1\), and extend \(S_{i+1}-S_i=a_i\) so \(S_{i+p}=S_i+A\). Put
\[
                   g=\gcd(p,A),\qquad U=p/g,\qquad N=A/g .
\]
For **each** \(1\le k<g\) there are an index \(i\) and positive integers \(d,r\) such that
\[
 x_{i+kU}=2^d x_i+r,\qquad 0<3r<2^d-1,\qquad
                 S_{i+kU}-S_i=kN-d.                                   \tag{1}
\]
In particular \(d\ge3\) and \(r\) is odd. If \(X<16s\), each \(d=3,r=1\). Thus for every nonzero sheet difference \(k\) the physical orbit has an exact pair \(x_{i+kU}=8x_i+1\) with the displayed clock count.

PR213 derived an aggregate inversion count of at least \(g-1\), its parity, the reversal symmetry of lag counts, and a required half-lag for even clocks in the full sixfold chart. It also obtained a matching graph in the width-below-twelve range and the finite width-nine coprimality criterion. The prior separation-class theorem supplies every nonzero reduced-sublap witness. Here its literal dyadic pairs are obtained from the physical odd-width bound of sixteen, and the subsequent consequences retain the complete native clock. [PR213, full-circuit inversion formula](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/FULL_CIRCUIT_INVERSIONS.md)

## The sublap product

Fix \(t=kU\), and let
\[
          e_i=S_{i+t}-S_i-kN,\qquad R_i=2^{e_i}x_{i+t}/x_i .
\]
All \(R_i\ne1\), since distinct positive odd integers have distinct dyadic rays. Their product is 1: the vertex ratios telescope on the cycle and \(\sum_i(S_{i+t}-S_i)=tA=pkN\). In fact the product is 1 separately in each residue class modulo \(\gcd(t,p)\). For \(h=\gcd(k,g)\), the arc lengths \(kU\) are multiples of \(hU\), so the arcs beginning in any such class cover the entire circle \(k/h\) times, and their endpoint indices permute that class.

There must be a cyclic date with \(R_i>1>R_{i+1}\). Exact odd iteration gives
\[
 R_{i+1}=2^{e_i}\frac{3x_{i+t}+1}{3x_i+1}.
\]
If \(e_i\ge0\), the inequality \(2^{e_i}x_{i+t}>x_i\) implies \(2^{e_i}(3x_{i+t}+1)>3x_i+1\), a contradiction. Write \(e_i=-d<0\). The two strict inequalities now give \(2^d x_i<x_{i+t}\) and \(3x_{i+t}+1<2^d(3x_i+1)\), proving (1). For \(d\le2\) there is no positive integral \(r\); for \(X<16s\), \(d\ge4\) is impossible, and at \(d=3\) the only positive odd \(r\) satisfying the inequality is 1.

## Full rational denominators on all shorter clocks

Start at the low endpoint of (1), take its \(kU\) odd transitions, write the resulting shortcut word of length \(kN-d\) with affine numerator \(C\), and append \(d\) formal even shortcut letters. The padded word has length \(kN\), weight \(kU\), and the same carry \(C\). Its positive rational periodic root is
\[
 \frac{C}{D_k}
   =x_i+\frac{2^{kN-d}r}{D_k},\qquad D_k=2^{kN}-3^{kU}>0.              \tag{2}
\]
Indeed \(2^{kN-d}(2^d x_i+r)=3^{kU}x_i+C\). Each positive formal word with positive determinant realizes its genuine parity cycle at this rational root: the denominator \(D_k\) is odd, and the final divisibility in the shortcut affine equation forces each successive prescribed bit modulo two. Thus its complete reduced denominator is exactly \(D_k/\gcd(D_k,r)\). These are rational cycles in addition to the hypothesized original integer one.

Under \(X<16s\), (2) attains the entire determinant for every \(1\le k<g\). Each padded word has least period \(kN\): any proper repetition has a shorter positive determinant whose absolute value is strictly smaller than \(D_k\), while its reduced denominator would divide that smaller determinant. The same strict inequality follows by factoring the difference of equal powers of two and three. For unrestricted but fixed \(X/s\le R\) the loss in the denominator is bounded by \(r<R/3\), uniformly over the sublaps.

## What the simultaneous witnesses force near width nine

In the width-below-sixteen case the low source \(x\) of any pair produces the three further odd states \(8x+1,6x+1,9x+2\), since the last two are the first two odd successors of \(8x+1\). Thus \(s\le x\le(X-2)/9\). A given low source has only one physical partner, so the \(g-1\) witnesses of different directed lags have distinct low sources. Their upper endpoints are distinct too, and a high endpoint cannot be a low source under this width bound. On each fixed time class modulo \(U\), these pairs are a directed matching of its \(g\) sheets. Their signed sheet differences, taken across all \(U\) classes, cover every nonzero residue modulo \(g\).

In particular \(g\ge3\) requires source phases in at least two different classes modulo \(U\): a matching in a single class has at most \(\lfloor g/2\rfloor<g-1\) edges. The following metric estimate makes this restriction quantitative. Put \(\Lambda=A-p\log_2 3>0\). For any chronological odd arc of \(j\) steps starting at \(i\),
\[
 \left\|\log_2(x_{i+j}/x_i)-jA/p\right\|_{\mathbb R/\mathbb Z}
 \le\Lambda,
\]
since the cumulative positive log correction lies between 0 and \(\Lambda\), as does \(j\Lambda/p\) for \(0\le j\le p\). For two low sources in different classes, \(jA/p=jN/U\) has distance at least \(1/U\) to an integer. The ordinary ratio of their magnitudes lies between \(9s/(X-2)\) and its reciprocal. Therefore
\[
                  \log_2\!\frac{X-2}{9s}+\Lambda\ \ge\ 1/U
                  \qquad(g\ge3,\ X<16s).                               \tag{3}
\]
More generally if the sources lie in \(J\) reduced classes, the circular grid spacing gives \(J\le1+U(\log_2((X-2)/(9s))+2\Lambda)\) whenever the expanded interval has length less than one: compare them to one fixed low source using its actual signed log offsets. Neither (3) nor the exact difference cover excludes a cycle by itself.

There is also an arithmetic bound on the number of possible low sources, stronger than their raw interval count. Set \(J=1+(X-2)/9-s\), \(\alpha=\log_3 2\), and \(h_\alpha=-\alpha\log_2\alpha-(1-\alpha)\log_2(1-\alpha)\). For \(g>1\) and \(X<16s\),
\[
            g-1\ll \frac{J^{h_\alpha}}{(1+\log J)^{3/2}}.              \tag{4}
\]
Indeed take \(l=\lceil\log_2 J\rceil\). The low sources are distinct modulo \(2^l\), since they lie in an interval of length \(J-1\). Each such residue has a distinct \(l\)-bit shortcut parity word. If its first \(j\le l\) clocks have \(v_j\) odd departures, then
\[
   \log_3(T^j(x)/x)=v_j-\alpha j+c_j,\qquad
     0\le c_j\le j/(3s\ln3).
\]
All states exceed or equal the cycle minimum. Since \(x/s<16/9\), \(J\le1+s\) and \(l=O(1+\log s)\), this implies \(v_j-\alpha j\ge-2\) for every prefix, enlarging constants for bounded inputs if needed. Prepend six odd bits: \(6(1-\alpha)>2\), so every prefix of this longer word lies strictly above the line of slope \(\alpha\). The number of such words of length \(l+6\) is \(O(2^{h_\alpha l}(1+l)^{-3/2})\), by the biased ballot estimate already proved for sparse direction modifications. This proves (4), using the estimate only as a counting lemma for actual integer parity residues. In particular \(X-9s\gg g^{1/h_\alpha}(\log g)^{3/(2h_\alpha)}\) as \(g\to\infty\) in this width range. The onset is immaterial for this asymptotic assertion. [Strict-prefix word count](SHARP_PERIODIC_REMOVALS.md)

There are genuine rational controls with the literal endpoints and exact integer difference. At \(U=6,N=10\), a positive rational cycle of odd length \(12\) has a source \(797/295\) and opposite state \(8(797/295)+1\). Its width is \(7763/737<16\). The odd states have common denominator \(295=2^{10}-3^6\), while the full formal determinant is \(2^{20}-3^{12}\). Exact arithmetic at the proper determinant or the mere existence of a paired positive rational return does not force ordinary integrality. At the displayed source its six-step odd arc padded by three even letters has affine carry \(925\), so its reduced denominator is \(59\), illustrating exactly where (2) uses an integer \(x_i\). The companion control reconstructs the complete valuation word.
