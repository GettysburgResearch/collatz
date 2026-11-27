# A quantitative test on the stopped trace after removing 1

Write \(\Lambda_k(x)=\rho_k(x)/[x(3x+1)]\) and \(\Lambda_\infty(x)=h(x)/[x(3x+1)]\) at positive odd \(x\). Weaver's Theorem 2 proves total variation convergence, with the total limiting mass explicitly retaining the cemetery contribution from escape. A rate on the *actual finite-law differences* can rule out positive escape without evaluating that mass. The needed estimate below remains open.

Let \(a_n=U^na\) be an ordinary escaping ray, and let \(H_C>0\) be its component charge in the normalization \(h(a_n)/a_n\to H_C\). There are finite constants \(L,k_0\), depending on the ray, such that for \(k\ge k_0\),
\[
 \sum_{x>1\ {\rm odd}}|\Lambda_k(x)-\Lambda_\infty(x)|
             \ \ge\ \frac{H_C}{16}\sum_{n\ge k+L}\frac1{a_n}.           \tag{1}
\]
Indeed the [ordinary scalar moving-front law](REAL_FIBRE_AND_FRONT.md) gives \(\rho_k(a_n)/h(a_n)\le1/2\) uniformly for \(n\ge k+L\) once \(k,L\) are large. In its formulas (5)–(6), the discrepancy tends to zero uniformly in \(k\) as \(n\to\infty\), and the masses of the unconditioned rows tend to zero as \(n-k\to+\infty\). Also \(h(a_n)\ge H_C a_n/2\) eventually. Thus the deficit of each displayed summand is at least \(H_C/[4(3a_n+1)]\ge H_C/(16a_n)\). The ray sites are distinct and none equals 1. One can equivalently test the signed measure on just this set of deficits. Taking an absolute value after summation over *all* positive odds would allow cancellation elsewhere. [Weaver 176, §4](https://rstation.ai/problems/collatz/papers/176/v1)

For instance, if the left side of (1) is \(O(k^{-A})\), then \(a_n\gg_a n^A\) on every escaping ray. The assertion also holds with a general decreasing positive rate \(r_k\) in the form \(a_{k+L}\gg_a 1/r_k\). At an exponential rate the endpoint \(r_k=(2/3)^k\) already excludes every escaping ray. In fact it suffices to have
\[
 \sum_{x>1\ {\rm odd}}\frac{|\rho_{k+1}(x)-\rho_k(x)|}{x(3x+1)}
                              =o\!\left(k^\gamma(2/3)^k\right),
 \qquad \gamma=\frac{\log2}{\log(\log_2 3)}.                            \tag{2}
\]
This test involves only the original finite geometric law on two consecutive levels. It makes no assumption about cycle count. By telescoping and pointwise convergence, (2) gives the same little-oh bound with \(\Lambda_\infty-\Lambda_k\) in (1), since the geometric tail with its polynomial factor has the order of the first term.

Here is the polynomial factor in (2). Write \(e_i=v_2(3a_i+1)\) and \(S_n=\sum_{i<n}e_i\). For any starting positive odd integer \(a\), the elementary inequality \(a_i+1\le (3/2)^i(a+1)\) holds. At a stretch of \(s\) consecutive exponents one starting at \(i\), the exact formula \(a_{i+s}+1=(3/2)^s(a_i+1)\) implies \(s\le\log_2(a_i+1)-1\) because \(a_{i+s}\) is odd. An infinite stretch is impossible. Consequently the successive times immediately after a gap exceeding one obey \(t_{j+1}\le(\log_2 3)t_j+O_a(1)\), starting at \(t_0=0\). For \(j\) such gaps before \(n\), one has \(n\le t_{j+1}\ll_a(\log_2 3)^j\). Therefore \(2^{S_n-n}\ge2^j\gg_a n^\gamma\). On an escaping ray the reciprocal packing bound gives \(F(a)>0\) and homogeneous transport gives
\[
  a_n=(3/2)^n 2^{-(S_n-n)}P(a)F(a_n)
               \ll_a (3/2)^n n^{-\gamma}.
\]
The single term \(n=k+L\) in (1) contradicts (2).

One can allow every fixed polynomial prefactor, and more, using Weaver’s stronger published rise-group theorem. If at least half the \(n\) exponents exceed one, then \(S_n-n\ge n/2\). Otherwise there are \(P>n/2\) rises. In his Theorem 4 mark all rise groups, so the residual rise count \(U\) is zero and the initial log height \(H\) is fixed. The number of groups is then \(\gg_a (\log n)(\log\log n)\); all but possibly the last are followed by distinct falls. It follows that \(S_n-n\ge c_a(\log n)(\log\log n)\) at all sufficiently large \(n\). On an escaping ray the left side of (1), divided by \((2/3)^k\), is consequently at least \(\exp(c'_a\log k\log\log k)\). In particular a bound \(O_A(k^A(2/3)^k)\) in (2) for any one fixed finite \(A\) suffices to exclude escape. The polynomial-free exponential improvement of the base remains unproved. [Weaver 174, Theorem 4, including finite prefixes of a fixed source](https://rstation.ai/problems/collatz/papers/174/v1)

Removing terminal vertex 1 removes every occurrence of its self-loop from the retained rows, since any path that has entered 1 remains there. The nonreal Mellin poles in [the first-return law](FIRST_RETURN_POISSON.md) concern the stationary spatial variable \(1-R_\infty\) at vertex 1. They do not furnish poles of the time-generating function of the remaining rows. Conversely (1) uses an escaping ray and does not exclude another cycle: a slow cycle multiplier alone does not prove that its initial signed discrepancy has a nonzero projection on its cyclic mode. Weaver's convergence proof at fixed bottom height uses the qualitative tail of finite stopping times before exhausting that height; its stated theorem has no rate of the size in (2).

There is also a one-sided subsequence test directly on consecutive rows. In the notation of the PR195 depth-difference theorem, any escaping component has some fixed integer grade \(v\) with \(\Delta_{C,v}>0\). Indeed \(Z_{C,0}>0\), \(Z_{C,v}\to0\) at \(+\infty\), and \(\Delta_{C,v}=Z_{C,v-1}-Z_{C,v}\). Its actual placement satisfies
\[
 \frac{\rho_{k+1}(a_{k+v})-\rho_k(a_{k+v})}{a_{k+v}}
                               \longrightarrow\Delta_{C,v}>0 .
\]
For the finite-law positive variation
\[
 B_k=\sum_{x>1\ {\rm odd}}
       \frac{(\rho_{k+1}(x)-\rho_k(x))_+}{x(3x+1)}
\]
the one site \(a_{k+v}\) now gives, on every such component and at all sufficiently large \(k\),
\[
             B_k\ge c_C(2/3)^k\exp(c'_a\log k\log\log k).
\]
Consequently even a subsequence on which \(B_k=O(k^A(2/3)^k)\), for any fixed \(A\), would exclude escape. This uses the positive part at each site before summation. The componentwise signed grade placement is a retained prior input. [PR195, depth differences at the pinned science head](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md)
