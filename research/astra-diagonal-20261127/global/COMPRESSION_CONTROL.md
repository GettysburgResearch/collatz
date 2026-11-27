# Cardinality compression at the borderline for dyadic compactness

**PROPOSED control.** There exists \(P:\mathbb N_{>0}\to\langle2,3\rangle\subset\mathbb Q_{>0}\) such that \(F(n)=n/P(n)\) stays in a compact subinterval of \((0,1)\), \(P(2n)=2P(n)\), \(P(3n)=3P(n)\), and
\[
 \#\{P(n):n\in I\}\ll(1+\log(2+|I|))^8,\qquad
 \frac1N\sum_{N\le n<2N}|F(n+1)-F(n)|^2\ll(1+\log N)^{-2} .           \tag{1}
\]
Nevertheless \(F(\lfloor2^k t\rfloor)\) on \(1\le t<2\) is not precompact in \(L^2\). The control tests the *numerical bound on the number of labels* in Weaver's interval compression theorem. It does not place two prescribed sources in the same actual Collatz fibre. The average result holds also with \(F^2\) in place of \(F\).

Write \(\alpha=\log_2 3\), \(K_j=2^j\). Choose by Dirichlet \(1\le q_j\le K_j^2\) with \(\|q_j\alpha\|\le 1/K_j^2\). Then \(q_j\to\infty\). On \(s\in[K_j,2K_j]\) let
\[
 h(s)=\tfrac12+\tfrac18\min(2(s/K_j-1),2(2-s/K_j))\cos(2\pi q_j s).
\]
Use \(1/2\) on \([0,1]\). The amplitude is zero at the joins. For \(l=a+d\alpha\) with nonnegative integers \(a,d\) and \(0\le l\le s/4\),
\[
       |h(s)-h(s-l)|\ll (1+l)/(1+s).                                  \tag{2}
\]
In a single stage the amplitude changes by \(O(l/s)\), and the phase changes modulo one by \(O(d/s^2)\). Across a join the two amplitudes are \(O(l/s)\). Each stage has derivative \(O((1+s)^2)\) away from the finitely many corners.

Write \(n=2^a3^d u\) with \((u,6)=1\), \(j_0=\lfloor\log_2u\rfloor\). Round \(u\) down within its dyadic octave to the grid with \(2^{L}\) equal cells, where \(L=\min(j_0,\lceil4\log_2(2+j_0)\rceil)\). Write \(w\) for the positive left endpoint. For each possible \(w,j_0\), choose \(G(w)\in\langle2,3\rangle\) within relative error \((10+j_0)^{-2}\) of \(w/h(\log_2w)\); this group is dense in \(\mathbb R_{>0}\). Put \(P(n)=2^a3^dG(w)\). The two dilations are exact. The grid is integral, so if \(L=j_0\) then \(w=u\); otherwise \(|u/w-1|\ll(2+j_0)^{-4}\). The derivative bound gives \(F(n)=h(\log_2u)+O((2+j_0)^{-2})\), and the chosen values keep \(F\) uniformly inside \((0,1)\).

For a translated interval \([N,N+M)\) with \(N\ge M\), at most two inputs have \(2^a>M\) or \(3^d>M\) (each exceptional divisibility class has at most one point). There are \(O((1+\log M)^2)\) other valuation pairs. For a fixed pair the core ranges through an interval of relative width \(M/N\) meeting at most two octaves; its coarse grids give \(O(1+(M/N)(1+\log N)^4)\) possible labels. Since \(N\ge M\), this is \(O((1+\log(2+M))^4)\) uniformly. For \(N<M\) enumerate all \(O((1+\log M)^2)\) pairs and the \(O((1+\log M)^5)\) grid points through \(2M\). This proves the first estimate.

On \([N,2N]\), the mean of \((1+a+d)^2\) is bounded uniformly by divisibility counting, including the \(O((\log N)^3/N)\) finite-end error. With \(s=\log_2 n\), (2) and the grid error show that the mean square of \(F(n)-h(\log_2 n)\) is \(O((1+\log N)^{-2})\). For \(a+d\alpha>s/4\) use the trivial bounded error and the same second-moment estimate. The difference of the two adjacent smooth profile values is \(O((1+\log N)^2/N)\), proving (1).

At the peak integer octaves \(k_j=3K_j/2\) for \(j\ge1\), the sampled profiles are \(L^2[1,2]\)-close to \(1/2+\cos(2\pi q_j\log_2t)/8\). The amplitude changes by \(O(1/k_j)\) within the octave, the floors change the phases by \(O(q_j 2^{-k_j})\), and (1)'s preceding mean-square comparison supplies the rest. The displayed cosines tend weakly to zero while their squared norms tend to \(1/2\), by the change of variable \(s=\log_2t\) and the Riemann–Lebesgue lemma. They have no strongly convergent subsequence.

In contrast, for bounded \(F\) with \(F(2n)=F(n)\), the squared \(L^2\) distance between two consecutive dyadic profiles is exactly \(2^{-k-1}\sum_{2^k\le n<2^{k+1}} |F(2n+1)-F(2n)|^2\). Summability over \(k\) of its square root gives a strong limit by completeness. The borderline decay in (1) permits the changes of frequency above. To improve it for a physical component one must use more than the number of images in each translated interval. [Weaver, Paper 28/v3, Theorem A](https://rstation.ai/problems/collatz/papers/28/v3).
