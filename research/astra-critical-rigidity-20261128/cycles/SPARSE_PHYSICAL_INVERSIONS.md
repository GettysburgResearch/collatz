# Few physical order reversals force the full spectral denominator rate

**Proposed written theorem.** For a primitive positive rational odd cycle let \(m,X,p,A,q,g,P,B,r\) denote, respectively, the native minimum, maximum, odd period, cumulative valuation, complete reduced denominator, \(\gcd(A,p)\), reduced period \(p/g\), reduced grade \(A/g\), and the chronological annihilator degree. Put
\[
          I=\#\{(x,y)\text{ actual odd phases}:0<y-2x<1/3\}.
\]
There is a fixed \(\delta>0\), depending only on the classical finite irrationality measure of \(\log_2 3\), with the following property. Suppose \(m\to\infty,\ g=O(1),\ X/m\le2^{1+\eta}\) and
\[
            \bigl(\eta+m^{-\delta}+I/p\bigr)\log(2+\eta m+I)\to0.
                                                                         \tag{1}
\]
Then
\[
                                 \log_3 q/r\ \longrightarrow\ 1 .       \tag{2}
\]
In particular, if \(I\) is bounded and \(\eta\log(2+\eta m)\to0\), (2) holds **without a separate restriction on \(g\)**. For coprime clocks, \(r=p\). At \(m\ge p^\epsilon\) with any fixed \(\epsilon>0\) and \(\eta=o(1/\log p)\), a family with bounded \(g\) and \(q\le3^{(1-\epsilon')r}\) for fixed \(\epsilon'>0\) therefore satisfies \(\liminf I\log p/p>0\). Each pair has a positive odd numerator difference strictly below \(q/3\); the count is on the complete rational cycle and the unscaled difference in (1) has fixed length \(1/3\).

The [zero-reversal resultant](SPATIAL_DEFECT_RESULTANT.md) used a single global rotation. Here the actual chronological ranks can change position at every inversion. Some roots of the clock characteristic polynomial can disappear when \(g>1\); (2) normalizes by the dimension that survives. The unconditional [minimal denominator divisor](MINIMAL_RECURRENCE_DENOMINATOR.md) supplies the upper bound. [Chronological dimension](NEAR_OCTAVE_CYCLE_DENOMINATORS.md)

## Controlling all true rank errors by the total inversion count

Write \(z_j\) for the increasing enumeration of all dyadic lifts, with \(z_0=m,\ z_{j+p}=2z_j\). The true lift map \(N(2^kx)=2^k(3x+1)\) is some bijection \(z_j\mapsto z_{f(j)}\), where \(f(j+p)=f(j)+p\). Condition (1) implies \(\eta\to0\) and \(I=o(p)\). At all sufficiently large periods \(X<4m\), so the inversions of \(f\), counted modulo simultaneous index translation by \(p\), are exactly the \(I\) pairs above: the lower input must be \(2x\) when the upper is normalized to \(y\), since only a larger correction can reverse the order. Ties are impossible. The actual ray action is one \(p\)-cycle, and \(f^p(j)=j+pA\). Thus \(\sum_{j=0}^{p-1}(f(j)-j)=pA\).

Sort by exchanging inverted adjacent input positions and all their \(p\)-translates. Whenever any inversion exists an adjacent one does. One swap removes one inversion class; comparisons with other input positions are permuted in pairs, and comparisons between two translated swapped blocks are permuted without changing the order between the two blocks. Equivalently this is the adjacent sorting proof for the complete dyadic order, now with one unrestricted real fiber. The displacement sum is preserved. After \(I\) swaps the increasing bijection is the shift \(j\mapsto j+A\). Each swap changes \(\sum_{j<p}|f(j)-(j+A)|\) by at most two: the two target positions against which the images are compared differ by one, including a seam swap after translating one representative. Consequently, with \(u_i=f^i(0)\),
\[
              \sum_{j<p,\ j\ge0}|f(j)-(j+A)|\le2I,\qquad
                         |u_i-iA|\le2I\quad(0\le i\le p).              \tag{3}
\]
The second bound sums along distinct true ray ranks. Also \(g\le I+1\): the sorted ray permutation has \(g\) cycles and each swap changes their number by one. [Prior adjacent-sort argument on native lifts](RESIDUE_FIBER_INVERSIONS.md)

Put \(\beta_j=1\) if the physical phase on the ray of \(z_j,\ 0\le j<p\), is \(2z_j\), and zero if it is \(z_j\); these are the only possibilities. All ones lie in the prefix \(0\le j<K\) of lifts \(z_j\le 2^\eta m\), and \(\beta_0=0\). The true occupation argument of the [zero-reversal theorem](SPATIAL_DEFECT_RESULTANT.md), which only uses the angle update on true windows, gives \(K/p\ll \eta+m^{-\delta}\), also if the averaging block contains multiple periods. If \(J\) is the number of runs of ones, their starting gaps satisfy
\[
                             J\le 6(2^\eta-1)m+I .                     \tag{4}
\]
Indeed at a transition \(0\to1\) the correction on consecutive sorted lifts drops from \(1\) to \(1/2\). Unless that pair is one of the \(I\) inversions, the gap is \(>1/6\); the distinct birth gaps have total length at most \((2^\eta-1)m\).

For \(j_i=[iB]_P\), let \(d_i=E_i-\lfloor iB/P\rfloor\). The true identity \(2^{E_i}x_i=z_{u_i}\) gives
\[
   d_i=\lfloor u_i/p\rfloor-\lfloor iA/p\rfloor-\beta_{[u_i]_p},
                            \qquad -2\le d_i\le1 .                       \tag{5}
\]
Here \(iA\bmod p=gj_i\). Let \(h_0=\lceil2I/g\rceil+2,\ k_0=\lceil K/g\rceil\). All \(d_i\ne0\) have \(j_i\) in the first \(k_0+h_0\) or last \(h_0\) positions of the reduced rank circle, by (3). Call a reduced rank exceptional if its full rank \(gj\) is within circular distance \(2I+2\) of a mark boundary or of the octave seam. There are \(O((I+1)(J+1))\) exceptional reduced ranks, since there are at most \(2J+1\) such boundary positions. At every other rank the \(g\) dates with \(j_i=j\) have the **same** \(d_i=-\beta_{gj}\), because no shift by at most \(2I\) crosses either a mark boundary or the seam. These assertions use only (3), so the ordering and allocation of the actual inversions within the lap is arbitrary.

## One resultant for each fixed cyclotomic clock component

Pass to a subsequence of fixed \(g\), which suffices since it is bounded. Factor \(\Delta=2^A-3^p=\prod_{d\mid g}\Delta_d\), where \(\Delta_d=3^{P\varphi(d)}\Phi_d(2^B/3^P)\) is the positive homogeneous cyclotomic factor. Write
\(M=\sum_{i<p}3^{p-1-i}2^{E_i}\) (all such sums run from \(i=0\)) and \(G_d=\gcd(M,\Delta_d)\). For \(G_d>1\) there is a homomorphism \(\mathbb Z[\zeta]\to\mathbb Z/G_d\mathbb Z\) taking a primitive \(d\)-th root \(\zeta\) to \(\lambda=2^B3^{-P}\): the primitive cyclotomic polynomial vanishes there and \(G_d\) is prime to six. All of this arithmetic uses the full \(G_d\), including its prime powers.

Fix \(Pu+Bv=1\), put \(t=(2^u3^v)^{-1}\bmod G_d\). Then \(t^{-P}=2\lambda^{-v}\), \(t^{-B}=3\lambda^u\). Form the clock polynomial over \(\mathbb Q(\zeta)\)
\[
    L_d(T)=\sum_{j=0}^{P-1} c_j T^j,\qquad
          c_j=\sum_{i:\,j_i=j}2^{d_i}\zeta^{\,v\lfloor iB/P\rfloor+ui}.
\]
At the modular evaluation, \(L_d(t)=3^{1-p}M=0\), since each term is \(2^{E_i}3^{-i}\). With \(d_i=0\) the nominal coefficient is \(c^0_j=g\) for \(d=1\), and \(c^0_j=0\) for \(d>1\), as the \(g\) dates for a fixed \(j\) differ successively by \(P\) and their root-of-unity exponent increases by \(vB+uP=1\).

Define a short Laurent sum \(D_d(T)\) from \(\sum_j(c_j-c^0_j)T^j\) by replacing every high-end monomial \(T^j\), \(j\ge P-h_0\), by \((\zeta^v/2)T^{j-P}\). The two end intervals are disjoint eventually by (1). Set
\[
  F_d(T)=16T^{h_0}\left(-1_{d=1}\,g/2+(T-1)D_d(T)\right)
                                          \in\mathbb Z[\zeta][T].       \tag{6}
\]
The four possible \(d_i\), and the single factor \(1/2\) at the high end, justify the clearing factor \(16\). Wherever \(T^P=\zeta^v/2\), the expression in parentheses equals \((T-1)L_d(T)\). In particular \(F_d(t)=0\bmod G_d\). One has \(F_1(1)=-8g\ne0\). Write \(\mathcal A\) for the divisors with \(F_d\) nonzero; this set can depend on the cycle.

The degree is at most \(W=k_0+2h_0+2\), and every coefficient in every conjugate polynomial has absolute value \(O_g(1)\) by (5). Their coefficient sums in absolute value are \(O_g((I+2)(J+2))\). Indeed away from the exceptional ranks \(c_j=2^{-\beta_{gj}}c^0_j\). For \(d>1\) these nominal corrected coefficients vanish; for \(d=1\) the correction \(c_j-c^0_j\) there agrees with \(-g\beta_{gj}/2\), whose consecutive differences are nonzero at at most \(2J\) ranks. Changing or folding the exceptional positions, and folding at the end cut, adds only \(O((I+1)(J+1))\) boundary coefficients of bounded size. In particular with \(H_1=\log(2+I+\eta m)\) one has
\[
                                W H_1=o(P).                             \tag{7}
\]
Here \(W\ll_g K+I+1\), (1) bounds the main terms, and \(\log m=O(\log P)\) by the physical clock and the fixed finite irrationality measure. Thus the extra constant in \(W\) poses no problem.

For \(d\in\mathcal A\), we prove \(\log G_d=o(P)\) uniformly over the finitely many \(d\). Take an integer \(H\asymp\sqrt{PH_1/W}\) with \(1\le H<P\); it tends to infinity by (7). Dirichlet approximation gives a primitive pair \(a,b\ge1,\ b\le H,\ a=O(H)\) with \(0<\ell=|bB-aP|\le P/H\), reducing a pair by its common divisor if necessary. Since \(B/P\to\log_2 3\) is irrational, these primitive denominators \(b\) tend to infinity: otherwise a limiting fixed rational would have \(|bB/P-a|\to0\). The modular \(t\) also obeys a binomial relation
\[
    3^b t^\ell=2^a\lambda^s\quad\hbox{or}\quad
                        2^a t^\ell=3^b\lambda^s
\]
for some \(s\in\mathbb Z\), from the two identities for \(t^{-P},t^{-B}\). Denote by \(C_d(T)\) the corresponding binomial over \(\mathbb Z[\zeta]\).

No nonzero \(F_d\) shares a complex root with \(C_d\) at large periods. Indeed the product of all Galois conjugates of \(F_d\) is a nonzero rational integer polynomial with leading coefficient bounded in absolute value by \(O_g(1)\). For a hypothetical common algebraic number \(\alpha\) of degree \(n_\alpha\) over \(\mathbb Q\) one has \(\alpha^{d\ell}=(2^a/3^b)^{\pm d}\). Therefore its rational field norm has absolute value \((2^a/3^b)^{\pm n_\alpha/\ell}\). Its valuations at two and three are integers, so \(\ell\mid an_\alpha,\ \ell\mid bn_\alpha\); primitivity gives \(\ell\mid n_\alpha\). The denominator of this field norm is at least \(\min(2^a,3^b)\to\infty\). It divides the leading coefficient of the primitive integral minimal polynomial of \(\alpha\), which in turn divides the bounded leading coefficient above by Gauss's lemma. This contradiction handles negative seam exponents and roots of unity equally.

Thus the resultant of \(F_d,C_d\) is a nonzero cyclotomic integer. Its rational norm is a nonzero integer divisible by \(G_d\): one conjugate of the resultant maps to zero in the displayed homomorphism, by the integral Sylvester adjugate identity, and the other factors also belong to \(\mathbb Z[\zeta]\). Hadamard's inequality at each embedding gives
\[
           \log G_d\ll_g \ell H_1+WH
                     \ll_g\sqrt{PWH_1}=o(P).                           \tag{8}
\]
This argument concerns the components with a nonzero short polynomial.

## Zero components and the actual chronological dimension

The polynomials \(T^p-2^A\) and \(T-3\) are coprime. Thus \(V\) and \(U_i=2^{E_i}=(S-3)V_i\) have identical active roots in their simple Fourier expansion on the unfolded clock. For a complex \(\beta\) with \(\beta^p=2^A\), its coefficient for \(U\) is \(p^{-1}\sum_{i=0}^{p-1}2^{E_i}\beta^{-i}\), by Fourier inversion after removing the common real slope. Let \(\zeta\) range over the primitive \(d\)-th roots. For each of the \(P\) solutions \(w^P=2\zeta^{-v}\), put \(\beta=w^B\zeta^{-u}\). They are exactly the \(P\) roots with \(\beta^P=2^B\zeta^{-1}\), since \((B,P)=1\). The sum just displayed equals \(L_d(w^{-1})\), before the factor \(1/p\). Here \((w^{-1})^P=\zeta^v/2\), and \(w^{-1}\ne1\). If \(F_d\) vanishes identically, all these coefficients are zero by (6), also for all conjugate \(\zeta\). Therefore
\[
                           r\le P\sum_{d\in\mathcal A}\varphi(d).
\]
This direction requires no assumption that every nonzero short polynomial activates every root.

Finally \(q=\Delta/\gcd(M,\Delta)\) is a multiple of \(\prod_{d\in\mathcal A}(\Delta_d/G_d)\), by comparing prime valuations: \(\max(0,\sum v(\Delta_d)-v(M))\) dominates the sum of the positive component deficits. No pairwise coprimality is required. For \(d>1\) the polynomial \(\Phi_d(x)\) is bounded below by a positive constant on \(x\ge1\); for \(d=1\), \(2^{B-P\log_2 3}-1\gg P^{-C}\) by the classical two-logarithm input. Thus \(\log\Delta_d\ge P\varphi(d)\log3-O_g(\log P)\). Summing (8) gives \(\log q\ge r\log3-o(P)\). The universal [upper bound](MINIMAL_RECURRENCE_DENOMINATOR.md) and \(r\ge P\to\infty\) now prove (2). When \(m\ge p^\epsilon\) and \(\eta=o(1/\log p)\), the classical bound also gives \(\log m=O(\log p)\); a subsequence with \(I\log p/p\to0\) would satisfy (1), proving the stated lower count of physical pairs.
