# Whole denominators under one or two cyclic adjacent swaps

Let \(w\) be a primitive nonconstant cyclic binary word of length \(n\), weight \(u\) and \(D=2^n-3^u>0\). Its shortcut branches are \(T_0(x)=x/2\) and \(T_1(x)=(3x+1)/2\). At phase zero write \(U_i=\sum_{j<i}w_j\) and
\[
 C(w)=\sum_{w_i=1}2^i3^{u-1-U_i},\qquad
 G=\gcd(D,C(w)),\qquad d=D/G .
\]
The returning rational starting value is \(C(w)/D\). The word is primitive in the usual least-period sense. Since \(D\) is prime to 6, both branch maps preserve the reduced odd denominator \(d\) on this orbit. Indeed division by 2 cancels in the numerator of the genuine parity branch and 3 is invertible modulo \(d\). Equivalently the two affine numerators at adjoining cuts obey \(2C(\operatorname{rot}_1 w)=3^{w_0}C(w)+w_0D\), which proves invariance of \(G\) without presupposing the parity claim. The numerator identity also gives the actual parity at every cut.

Suppose some proper rotation \(w'_i=w_{i+h}\), \(0<h<n\), can be produced by one or two swaps of adjacent unequal bits. Edges are cyclic, including \((n-1,0)\). Any presented sequence of such swaps suffices. Zero swaps cannot produce a proper rotation by primitivity. Swapping the same unordered pair twice restores the original word. For \(n=2\) the two oriented cyclic edges name the same unordered pair and only the one-swap case survives. For \(n\ge3\), choose a common cut through an unused cyclic edge so every presented swap is internal in both linear representatives. This simultaneously rotates the source and target and preserves \(h,D,G\).

| Presented swaps | Whole-denominator conclusion |
| --- | --- |
| One | \(G=1,\ d=D\). |
| Two intersecting edges, moving one odd bit past two zeros | \(G=1\). |
| Two intersecting edges, moving one zero past two odd bits | \(G\mid5\). |
| Two disjoint edges in the same direction | \(G\mid\gcd(2^{2|\Delta|}-1,3^{2|\Delta|}-1)\) for a nonzero \(|\Delta|\le3n\). In particular \(\log G=o(n)\) by BCZ. |
| Two disjoint edges in opposite directions | For the explicit proper divisor \(r\) of \(M\) below, \((t^M-b^M)/(t^r-b^r)\mid d\). Consequently \(d>2^{n/2}\) at every period. The exponent \(1/2\) is sharp even at critical odd counts. |

The opposite-direction divisor is an elementary finite statement. The same-direction asymptotic uses the Bugeaud–Corvaja–Zannier theorem. Under the additional sourced two-logarithm bound \(u2^n/(3D)<600n^{14.3}\), the first four rows have \(\log_2d/n\to1\) as \(n\to\infty\). Indeed that input gives \(\log_2D=n-O(\log n)\). See [Wren 218/v2, §1, citing 216 (8), (16)](https://rstation.ai/problems/collatz/papers/218/v2).

The one-swap argument is prior. Knight proved the balanced high-cycle exclusion, Weaver 84 §5 gives the precise local monomial difference, and the January 2026 X0rr0/MathKook discussion explicitly uses rotations differing by one swap and gives the local factor 5 for the overlapping example. The disjoint two-edge classification below uses the cyclic window constraint in addition to the local affine difference. Paper 4 Theorem 5 uses a different presentation, a single perturbation of a chosen Sturmian valuation word, with Farey-parent congruences. [Knight, Discrete Math. (2026)](https://doi.org/10.1016/j.disc.2025.114812), [Weaver 84, Lemma 4](https://rstation.ai/problems/collatz/papers/84), [X0rr0 and MathKook, January 27, 2026](https://forum.collatzworld.com/t/rotation-swaps-numerator-gaps-and-central-structure-in-collatz-parity-vectors/173), [Paper 4, §7](https://rstation.ai/problems/collatz/papers/4)

## Affine swap and window identities

The change in \(C\) under \(10\to01\) at positions \(p,p+1\) is \(+2^p3^{u-1-U_p}\). The reverse move changes its sign at the same cut, with \(U_p\) denoting the number before the pair. Contributions from all other positions agree. This proves the first row. On three consecutive sites, the only two-step moves which do not undo are \(100\leftrightarrow001\) and \(110\leftrightarrow011\). Their unsigned changes are respectively \(3\) and \(5\) times a product of powers of 2 and 3: the local affine numerators are \(1,4\) and \(5,10\). This proves both overlapping rows.

For disjoint swaps put their left positions at \(p<q\), let \(a=q-p\) and \(v'=U_q-U_p\), and let \(\sigma_p,\sigma_q\in\{\pm1\}\) be their affine signs. Each earlier swap preserves the total number of ones before the later pair. Thus \(C(w')-C(w)\) is a product of powers of 2 and 3 times
\[
 \sigma_p3^{v'}+\sigma_q2^a .
 \tag{1}
\]
Both affine numerators are divisible by \(G\), so \(G\) divides (1).

Extend \(U_{i+n}=U_i+u\) to integer indices. For any cut \(i\) put
\[
 A_i=U_{i+h}-U_i,\qquad F_i=U_i-iu/n .
\]
Then \(A_{i+1}-A_i=w'_i-w_i\), \(\sum_{i\bmod n} A_i=hu\), and \(F_{i+h}-F_i=A_i-hu/n\). Each swap produces opposite jumps at two consecutive sites. Therefore \(A_i=K+e_i\) for an integer \(K\), where \(e\) is supported at \(p+1,q+1\) and its two nonzero values are \(-\sigma_p,-\sigma_q\). Put \(g=\gcd(n,h)\), \(M=n/g\), and \(s_0=\sum e_i=hu-nK\).

For a segment \(J\) of fewer than \(M\) steps along one \(h\)-orbit, the difference of its endpoint \(F\)-values is \(\sum_i(1_J(i)-|J|/n)e_i\). Its absolute value is at most 2. If \(g\le2\), every pair of physical dates is connected by such a segment and at most one natural unit step. As \(|F_{i+1}-F_i|\le1\), the global oscillation of \(F\) is at most 3. For \(g=1\) it is at most 2.

## Same direction and the determinant resonance

Here \(s_0=\pm2\), so \(g\mid2\) and \(\gcd(n,u)\mid2\). Let \(\Delta=nv'-ua=n(F_q-F_p)\). The window bound gives \(|\Delta|\le3n\). Suppose \(\Delta=0\). Since \(0<a<n\), the preceding divisibility gives \(\gcd(n,u)=2\) and \(a=n/2\). Equal-sign swaps are antipodal. Their difference sequence \(w'_i-w_i\) is invariant under shift by \(n/2\). It follows that \(Y_i=w_i-w_{i+n/2}\) is constant on every \(h\)-coset, and \(Y_{i+n/2}=-Y_i\). If \(g=1\) or \(g=2\) and \(n/2\) is even, this forces \(Y=0\), contradicting primitivity. In the remaining case the two parity classes have opposite constant values. A zero value again gives a half-period. A nonzero value forces the whole word to alternate, contradicting primitivity for \(n\ge4\). Two disjoint edges require \(n\ge4\). Hence \(\Delta\ne0\).

Modulo \(G\), the units \(2,3\) satisfy \(2^n=3^u\) and \(2^a=-3^{v'}\). On squaring and then eliminating each generator in turn, \(2^{2\Delta}=3^{2\Delta}=1\) in the unit group. This proves the finite divisibility in the table. BCZ gives \(\log\gcd(2^k-1,3^k-1)=o(k)\). For \(k=2|\Delta|\le6n\), unbounded \(k\) give \(o(n)\), and bounded \(k\) give \(O(1)\). This also proves uniformity over choices of words and presentations at each \(n\). See [Bugeaud, Corvaja and Zannier, Math. Z. 243 (2003), 79–84, Theorem 1](https://doi.org/10.1007/S00209-002-0449-Z) and [Levin and Wang, Theorem 1.12, for the exact statement](https://doi.org/10.1515/crelle-2019-0033).

## Opposite directions and the geometric divisor

Now \(s_0=0\) and \(hu=nK\). Writing \(h=g h_0\) with \(\gcd(h_0,M)=1\) gives \(M\mid u\), so put \(v=u/M\). Since \(0<u<n\), \(g\ge2\). The sum of \(F_{i+h}-F_i=e_i\) around every \(h\)-coset vanishes. The cancelling nonzero entries of \(e\) must lie in the same coset. Thus \(a=g\ell\) for \(0<\ell<M\).

Cut into \(M\) consecutive blocks of length \(g\) starting at \(p\). Only columns 0 and 1 can change when the row index is advanced by \(h_0\). At both swaps the change in column 0 cancels that in column 1 in the same row. The sum of these columns is invariant under the row advance. Every other column is invariant separately. As \(h_0\) generates all rows, every block has the same number \(v\) of ones. In particular \(v'=\ell v\).

Put \(t=2^g\), \(b=3^v\) and \(r=\gcd(M,\ell)<M\). We have \(t>b\ge1\), \(D=t^M-b^M\), and (1) gives \(G\mid t^\ell-b^\ell\). The element \(t/b\) in \((\mathbb Z/G\mathbb Z)^\times\) has both \(M\)th and \(\ell\)th powers equal to 1. Its \(r\)th power is 1 by Bézout, so \(G\mid t^r-b^r\). For \(G=1\) the same divisibility holds directly. As \(r\mid M\), \(t^r-b^r\mid D\). Hence
\[
 Q=\frac{t^M-b^M}{t^r-b^r}\ \mid\ d .
\]
The geometric sum for \(Q\) has first term \(t^{M-r}\) and at least one further positive term. Since \(r\le M/2\), \(d\ge Q>2^{g(M-r)}\ge2^{n/2}\). This excludes every positive ordinary integer cycle with an opposite-direction presentation using two disjoint swaps.

## Sharpness at the critical odd count

Set \(p_*=\log_3 2\). For reduced lower continued-fraction convergents \(v/g\to p_*\), put \(\delta=gp_*-v>0\) and \(k=\lfloor\delta^{-1/2}\rfloor\). Then \(k\to\infty\) and \(2k\delta\to0\). Define \(A=1^v0^{g-v}\), let \(B\) move its final odd bit right by one, and form \(w=A^k B^k\). For sufficiently large convergents all blocks are defined. A shift by \(g\) changes only the two boundary rows. These are opposite swaps separated by \(n/2=kg\). The two positive sites of \(w_{i+g}-w_i\) are separated by \(n/2+1\) in one cyclic direction, so they are not antipodal when \(n>4\). A nontrivial stabilizer of a two-element set must interchange antipodal sites. Therefore the word is primitive. Positivity follows from \(3^{u}<2^n\), with \(u=2kv=\lfloor np_*\rfloor\) eventually.

Write \(t=2^g,\ b=3^v\). A single row \(A\) has affine map \((bx+c_A)/t\), likewise for \(B\). Its \(k\)th iterate has intercept numerator \(c_A S_k\) or \(c_B S_k\), where \(S_k=(t^k-b^k)/(t-b)\). Composition shows \(S_k\mid C(w)\), and \(S_k\mid D=t^{2k}-b^{2k}\), giving \(S_k\mid G\). The preceding opposite-direction result with \(M=2k,\ \ell=r=k\) also gives \(G\mid t^k-b^k\). Therefore
\[
 t^k+b^k\ \mid d \mid (t-b)(t^k+b^k).
\]
Taking base-2 logs gives \(\log_2d/n\to1/2\) since \(\log_2(t-b)<g\) and \(n=2kg\). The fixed-row family \(g=2,v=1\), with words \((10)^k(01)^k\), already attains the exact formula \(d=4^k+3^k\) for every \(k\ge1\).

The classification uses a particular type of near-rotation. A general primitive parity word need not admit any two-swap presentation. The asymptotic results give no explicit BCZ onset.
