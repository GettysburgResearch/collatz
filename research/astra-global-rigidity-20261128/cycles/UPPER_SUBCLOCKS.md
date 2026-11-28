# Adjacent rational returns at every upper subclock, including coprime clocks

Let \(s>1\) be the odd minimum of a hypothetical primitive positive integer cycle \(x_i\). Write \(p\) for its number of odd states and \(A\) for its total halving count. Choose **any** \(1\le t<p\) and integer \(n\) with \(n/t>A/p\). Then \(D=2^n-3^t>0\). There are consecutive dates \(i,i+1\) at which both actual arcs of \(t\) odd transitions take at most \(n\) halves. Append even shortcut letters to each to reach length \(n\). The two resulting positive rational cycles have exact reduced denominators \(q,q'\) satisfying, uniformly as \(n\to\infty\),
\[
 \operatorname{lcm}(q,q')=2^{n-o(n)},\qquad
        \min(q,q')\ge 2^{t-O(\log(2+n))}/(2s).                         \tag{1}
\]
The result includes \(\gcd(A,p)=1\) and permits zero padding on the second arc. It holds without reference to the physical width or the complexity of the native word.

For \(n=\lceil tA/p\rceil\), (1) applies at each nonintegral \(tA/p\); [the reduced-sublap result](SUBLAP_RESIDUES.md) proves the sharper height-independent individual bound at every interior integral \(tA/p\). Thus every \(t=1,\dots,p-1\) has such a pair on the **least upper integer truncation**. If \(t/\log(2+p)\to\infty\) along distinct ordinary cycles, the two words there have least period \(n\) for all sufficiently large inputs. A separate estimate below gives primitivity on the exact upper Farey parent even when comparing \(t\) to \(\log p\) would be inadequate.

## Crossing or two returns at the minimum

Use \(S_{i+1}-S_i=a_i=v_2(3x_i+1)\), \(e_i=S_{i+t}-S_i-n\) and \(R_i=2^{e_i}x_{i+t}/x_i\). All \(R_i\ne1\), since \(t<p\) and distinct positive odd integers have distinct dyadic rays. One has \(\prod_{i=0}^{p-1}R_i=2^{tA-pn}<1\). If some \(R_i>1\), there is a cyclic \(>1\) to \(<1\) transition, and the proof of [the adjacent crossing](SUBLAP_RESIDUES.md) applies verbatim: it only uses this transition, not equality of the mean clock. The deficits \(d,d'\) are positive, and each defect has absolute value less than \(2^d\le2^{n-t}\).

It remains to consider \(R_i<1\) at every date. Start at \(x_i=s\). Since \(x_{i+t}>s\), necessarily \(e_i=-d<0\). At a nontrivial ordinary minimum the native valuation is one: if \(4\mid3s+1\), the odd successor is at most \((3s+1)/4<s\). Consequently \(x_{i+1}=(3s+1)/2<2s\). Since every state is at least \(s\), \(2^{e_{i+1}}x_{i+t+1}<x_{i+1}\) implies \(e_{i+1}=-d'\le0\). Define signed defects \(h=x_{i+t}-2^d x_i\), \(h'=x_{i+t+1}-2^{d'}x_{i+1}\). Both are strictly negative, and every actual arc costs at least \(t\), giving
\[
          0<|h|,|h'|<2^{n-t}\,2s.                                        \tag{2}
\]
In both cases let \(a=a_i\), \(b=a_{i+t}\). The two clocks give \(d'=d+a-b\), and the two genuine native transitions give
\[
 2^b h'=3h+1-2^d,\qquad
 q=D/\gcd(D,h),\quad q'=D/\gcd(D,h').                                  \tag{3}
\]
In particular \(D/\operatorname{lcm}(q,q')\mid\gcd(D,2^d-1)\), with \(1\le d\le n-t\). Corvaja–Zannier, Corollary 1, bounds the logarithm of the last gcd by \(o(n)\) since \(2^n3^{-t}\) and \(2^d\) are independent rational \(S\)-units of height \(O(n)\). The standard two-log lower bound gives \(D=2^{n-O(\log(2+n))}\). These prove (1) and (2) gives the individual bound even in the absence of a sign change. The two rooted words can represent the same rational orbit. [Full gcd and two-log inputs](SUBLAP_RESIDUES.md)

The joint divisor in (3) also follows directly from the two finite words. If their unpadded carries are \(C,C'\) and the first has length \(m=n-d\), composing the same \(t+1\) odd transitions from either end gives
\[
                     2^a C'=3C+2^m-3^t.
\]
Subtract \(D\) modulo any common divisor of \(D,C,C'\) and cancel the unit \(2^m\). Hence the joint divisor statement for a *given* pair of padded words is purely formal. The ordinary orbit forces two simultaneously eligible dates, controls the individual defects, and realizes them at every requested upper clock. This distinction also explains the source qualification in the lower-parent proof.

For \(n=\lceil tA/p\rceil\), the cycle log identity \(0<A/p-\log_2 3\le1/(3s\log 2)\) gives \(t/n\to\log_3 2>1/2\) whenever \(t,s\to\infty\). The two-log bound and that identity give \(s\ll p^{B+1}\), for instance with \(B=4.116201\) and a fixed enlargement of constants for bounded inputs. Hence \(\log s=O(\log(2+p))\). When \(t/\log(2+p)\to\infty\), the individual denominators exceed \(2^{n/2}\). A proper repetition would have denominator dividing a positive determinant \(<2^{n/2}\). Distinct ordinary cycles have minima tending to infinity, since each integer minimum determines its forward orbit. [Two-log estimate at the reduced ratio](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE.md)

## Both Farey parents of a coprime clock

Let \(U=p/g\), \(N=A/g\), \(g=\gcd(A,p)\), with \(U\ge2\). For any primitive upper Farey parent \((n,t)\) of \((N,U)\) one has \(Un-tN=1\), \(1\le t<U\). Its lower parent satisfies \(Un-tN=-1\), \(1\le t<U\). Uniformly at **either** parent,
\[
                 s\ll (1+t)^{B(B+1)}+(1+t)^{B+1}.                        \tag{4}
\]
To verify this, write \(\gamma=\log_2 3\), \(\delta=N/U-\gamma>0\). The classical absolute two-log bound gives \(|n-t\gamma|\gg (1+t)^{-B}\) since \(n=O(1+t)\). But \(|n-t\gamma|\le1/U+t\delta\) and \(\delta\le1/(3s\log 2)\). Either \(s\ll (1+t)^{B+1}\), or \(U\ll(1+t)^B\). In the latter case \(N-U\gamma=U\delta\gg(1+U)^{-B}\) implies \(s\ll(1+U)^{B+1}\). This gives (4). In particular the least possible upper parent length tends to infinity along distinct cycles, and (1) gives there \(q,q'\ge 2^{t-O(\log(2+t))}\). Its two positive rational words are eventually primitive, with no condition on \(g\).

For the **lower Farey parent when \(g=1\)**, the determinant \(D=2^n-3^t\) can be negative. Along distinct ordinary cycles, two consecutive arcs again have genuine nonnegative padding, with positive denominators \(q,q'\) of their signed rational roots satisfying
\[
 \operatorname{lcm}(q,q')=2^{n-o(n)},\qquad
          \min(q,q')\ge2^{t-O(\log(2+t))}.                               \tag{5}
\]
Their signs are the sign of \(D\), and the words are eventually primitive. If a positive-to-negative crossing occurs, the same two-defect proof applies using absolute determinants. In fact that crossing necessitates \(D>0\): the first correction \(\log_2(1+1/(3x_i))\) exceeds the positive log gap \(\log_2 R_i\), and the sum of all corrections on the arc is still larger. Otherwise all \(R_i>1\), since the product equals two. Then \(z_i=\log_2 R_i>0\) has \(\sum_i z_i=1\) and
\[
 |z_{i+1}-z_i|\le \log_2(1+1/(3s))\ll 1/s .
\]
For any \(1\le H\le p\), averaging \(z_i\le z_{i+j}+O(H/s)\) over \(0\le j<H\) gives \(\max_i z_i\le1/H+O(H/s)\). Taking \(H=\min(p,\lfloor\sqrt s\rfloor)\) gives \(\max_i z_i\to0\) since both \(s,p\to\infty\). At the minimum and its immediate successor the departures have size at most \((3s+1)/2\). Thus \(2^{e_j}x_{j+t}=R_j x_j<2s\) for each of these two dates once \(s,p\) are large, and both \(e_j\le0\). Their defects \(h,h'>0\) satisfy \(|h|,|h'|\le 2^{n-t}\,2s\) eventually because \(R_j-1=o(1)\). If the first deficit \(d=-e_i\) is positive, (3) and the same gcd bound prove (5). If \(d=0\), then already \(0<h=(R_i-1)s<s\), so \(q\ge |D|/s=2^{n-O(\log(2+t))}\) by (4). Again the absolute two-log bound yields \(|D|=2^{n-O(\log(2+n))}\) here, since \(|n-t\gamma|=O(1/U+t/s)\), \(t\le U\), and \(t/n\to1/\gamma\); more directly, the lower bound on the distance from zero gives \(|2^n-3^t|\gg 2^n/(1+t)^B\), while on the negative side \(t\gamma-n<1/U\) so \(|D|<2^n\). For a repeated word, its shorter signed determinant has magnitude at most \(\max(2^{n/2},3^{t/2})=2^{n/2+o(n)}\), precluding repetition. This proves (5).

The coprime best-upper-clock angular tiling and its monotone rank structure were already established in PR213, including nonmechanical rational controls. The result here forces adjacent genuinely padded rational returns at both parents, along with bounds at the complete signed determinants; the earlier tiling has a separate order-geometric conclusion. None of the rational returns requires its original integral source to be periodic when considered in isolation. [PR213, Farey tile](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/FAREY_TILE.md)
