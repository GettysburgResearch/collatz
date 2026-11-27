# Polynomial tests for complete denominators on binary odd cycles

**Proposed.** On the accelerated map an edge is \(2^a y=3x+1\) between odd phases, with \(a\) the exact positive exponent. If all the exponents on a cycle are one or two, its actual ternary past restricts every polynomial in an auxiliary integer index. The coefficients may depend on the full cycle. A height estimate then gives a test for its common reduced denominator. The general cycle and escape problems remain open.

## Pulling a two-child set back through a polynomial

Call \(S\subseteq\mathbb Z_3\) a two-child set if at each occupied residue modulo \(3^j\), the points of \(S\) occupy at most two of its three lifts modulo \(3^{j+1}\), starting with \(j=0\). The missing lift may depend on the entire residue.

**Theorem 1.** For a nonconstant \(F\in\mathbb Q[X]\) of degree \(d\), the set \(\{x\in\mathbb Z_3:F(x)\in S\}\) can be covered by at most \(d\) two-child sets. At depth \(k\) its number \(N_k\) of occupied residues satisfies the stronger estimate
\[
                       N_k+(d-1)\le d\,2^k .
\]
Both bounds are uniform in the coefficients, translations and scales of \(F\). For any interval of \(n\ge1\) consecutive integer indices take \(k=\lceil\log_3 n\rceil\). The same bound counts actual indices in the interval, because their residues at that depth are distinct. For the degree-one case, exponent \(\log_3 2\) is attained on an abstract ternary Cantor tree.

**Proof.** Consider an input ball specified by \(x=a+3^j u\). Normalize \(F'(a+3^j U)\) by a nonzero rational scalar to obtain a polynomial \(Q(U)\) over the rationals with denominator prime to three and at least one coefficient a unit modulo three. Its reduction \(\bar Q\) is nonzero.

For a trit \(e\) which is not a root of \(\bar Q\), the entire **child** \(u=e+3v\) is a scaled isometry for \(F\). Write \(G(V)=F(a+3^j(e+3V))=\sum b_i V^i\). Its derivative is proportional to \(Q(e+3V)\). In the latter polynomial the constant coefficient is a unit, and its coefficient of degree \(i-1\) is divisible by \(3^{i-1}\). Hence \(b_1\ne0\), and for \(i\ge2\)
\[
          v_3(b_i/b_1)\ge i-1-v_3(i)\ge1
\]
when \(b_i\ne0\). The final inequality follows from \(3^{i-1}>i\). In the divided difference \((G(v)-G(w))/(v-w)\), the linear part is \(b_1\) and the remaining part belongs to \(3b_1\mathbb Z_3\). Thus on distinct integral inputs
\[
                    v_3(G(v)-G(w))=v_3(b_1)+v_3(v-w).
\]
Every subball inherits this property. In any such ball, three surviving points in three different immediate children would have one common pairwise output valuation. If it is negative, two integral outputs are already impossible. If it is nonnegative, the three outputs occupy all three children of their common output prefix. This contradicts the definition of \(S\). The argument uses only the three actual images.

For a root trit \(e\), let \(m_e\) be its multiplicity in \(\bar Q\). Expand \(Q(e+Y)=\sum q_iY^i\). The coefficient \(q_{m_e}\) is a unit. The minimum coefficient valuation of \(Q(e+3V)\) is at most \(m_e\), while every coefficient of degree greater than \(m_e\) has strictly larger valuation. After primitive normalization, the reduction on this child has degree at most \(m_e\). The sum of the root multiplicities of \(\bar Q\) at the three trits is at most \(\deg\bar Q\). Give root children credit \(m_e\), give isometric children zero credit, and start with credit \(d-1\). For \(d=1\) the initial ball is itself isometric. For \(d>1\) a positive-credit ball is allowed to be exceptional even if its local reduction has degree zero. Total exceptional credit never increases. Thus at each depth at most \(d-1\) balls are exceptional, and all the others have at most two occupied children. Iterating \(N_{k+1}\le2N_k+(d-1)\) from \(N_0\le1\) proves the numerical estimate.

For the cover, give the initial ball \(d\) colors. An exceptional ball of credit \(m\ge1\) has \(m+1\) available colors. Each occupied child of credit \(m_i\) requests \(m_i+1\) colors. Each request is at most \(m+1\), and their sum is at most \(m+3\le2(m+1)\). Allocate the requests successively around a cyclic list of the colors. No child repeats a color, and each color occurs at most twice in total. An isometric ball passes its single color to each occupied child. Continue at all depths. A point's finite nonempty nested color sets have common intersection. Each color separately admits at most two children per occupied prefix. This constructs the cover.

For a finite subset \(A\) of the preimage consisting of ordinary integers, its ordered additive energy \(E(A)=\#\{u+v=w+z:u,v,w,z\in A\}\) consequently satisfies
\[
                        E(A)\le d^{4-\kappa}|A|^\kappa,\qquad \kappa=\log_2 6.
\]
Partition \(A\) using the cover and apply the hereditary two-child energy inequality \(E(A_i)\le |A_i|^\kappa\) from PR201. The triangle inequality for the fourth norm of the Fourier sums on the unit circle gives \(E(A)^{1/4}\le\sum_i E(A_i)^{1/4}\). Concavity proves the estimate. Only this corollary imports the two-child energy inequality.

## Actual cycle phases and normalization

For a positive rational odd cycle with common reduced denominator \(q\) prime to six, every phase lies in \(\mathbb Z_3\). If the exponents are all one or two, an endpoint \(y\) chooses the inverse exponent \(a\in\{1,2\}\) uniquely from \(2^ay\equiv1\bmod3\), and the predecessor is \((2^ay-1)/3\). In a fixed occupied class modulo \(3^j\) its first \(j\) inverse exponents are consequently common to the points of that class. After those inverse steps, the three lifts modulo \(3^{j+1}\) map to the three distinct residues modulo three. A further predecessor requires a unit residue, so at most two lifts occur. This holds at every depth of the actual closed history, and on the union of all such cycles. A finite list of compatible histories through a fixed depth only guarantees branching through that depth.

Let the rank labels on one fundamental interval be \(Z_r=c_rx_r\), with distinct true odd phases \(x_r\) and tags \(c_r\in\{1,2,4\}\). These are the labels on the bounded least-disagreement branch. General cycles need not admit this chart. Because 2 and 3 are units modulo \(q\), \(q\) is the actual reduced denominator at every odd phase and after dyadic tagging. A positive shortcut word of length \(h\), weight \(p>0\), and carry \(C\) has \(q=(2^h-3^p)/\gcd(2^h-3^p,C)\). For a nonconstant polynomial \(F\), equality \(Z_r=F(r)\) puts \(r\) in one of the three pullbacks for \(F/c\). On any interval of \(n\) fundamental ranks the number of equalities is at most
\[
                   3\bigl(d\,2^{\lceil\log_3 n\rceil}-(d-1)\bigr).
\]
For a constant there are at most three equalities by distinctness of the underlying odd phases. The energy corollary holds with \(3d\) in place of \(d\).

## A whole-denominator cost for intervals of one sign

Write \(\Delta Z_r=Z_{r+1}-Z_r\). For \(m\ge2\), choose the least positive \(k\) with \(3^k>3(m-1)2^k\), and put \(L_m=3^k\). Every block of \(L_m\) consecutive \(m\)-th differences whose inputs all lie on the fundamental interval contains a nonzero difference. Otherwise the corresponding \(L_m+m\) values agree with a polynomial of degree at most \(m-1\). Indeed the starting differences give the Newton polynomial in \(\binom{r-r_0}{i}\) for \(i<m\), and vanishing of the \(m\)-th difference determines each next value. The occupancy bound contradicts agreement on the first \(L_m\) ranks, including the constant case. Thus \(L_m=O(m^{\log3/\log(3/2)})\) is sufficient.

Let \(0<Z_r\le X\) on the fundamental interval. Suppose the \(m\)-th differences at \(r,\ldots,r+m(t-1)\) all have the same weak sign, where inputs through \(r+mt\) lie on that interval. For integer \(t\ge2L_m\), the common reduced denominator satisfies
\[
                     \boxed{\quad q\ge\frac{(t/2)^m}{2L_m X}.\quad}
\]
In fact \(\Delta_t=E^t-I=(I+E+\cdots+E^{t-1})\Delta\), with \(E\) the unit shift. Expanding its \(m\)-th power gives
\[
 \Delta_t^m Z_r=\sum_{0\le i_1,\ldots,i_m<t}\Delta^m Z_{r+i_1+\cdots+i_m}.
\]
For each fixed \(i_2,\ldots,i_m\), at least \(\lfloor t/L_m\rfloor\) of the \(t\) summands are nonzero, by disjoint length-\(L_m\) subblocks. Every nonzero summand has absolute value at least \(1/q\). The common sign prevents cancellation. Thus \(|\Delta_t^m Z_r|\ge t^m/(2L_mq)\), while the binomial expansion gives \(|\Delta_t^m Z_r|\le2^m X\).

If \(q=1\) and \(X\le p^A\) for a fixed \(A\), each fixed \(m>A\), \(m\ge2\), has both positive and negative \(m\)-th differences in every fundamental interior interval of length \(O_{A,m}(p^{A/m})\), with a sufficiently large constant. More generally take \(m=\lceil\log p\rceil\). Then both signs occur on every interior interval of length \(O_A((1+\log p)^{1+\log3/\log(3/2)})\) for sufficiently large \(p\). Indeed \(t=2L_m\) gives \((t/2)^m/(2L_m)>p^A\) eventually. The \(m\) terminal input ranks needed by the differences are included in the interval lengths. These assertions concern each ordinary candidate satisfying the stated height hypothesis and require no particular irrationality-exponent claim.

## Boundaries and sources

The exceptional children are necessary. For \(F(r)=r^2\), the indices \(0,1,2\) give the two-child set \(\{0,1,4\}\), even though the three indices occupy every first trit. For \(F(X)=X^3-X\), the derivative reduces to the nonzero constant \(-1\), yet all three residues have image zero modulo three. Our argument declares its three *child balls* isometric. It assigns the root credit two and leaves its actual branching unrestricted. An abstract two-child tree at denominator one can also consist of all integers with a prescribed finite number of digits from \(\{0,1\}\). These controls do not assert an ordinary positive cycle. Rational periodic phases pass the same ternary condition. Their full reduced denominator enters through the spacing \(1/q\) of nonzero signed differences.

The cut-dependent inverse branches and linear-progression result are from [PR201, ternary-past theorem](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/TERNARY_PAST_ENTROPY.md). The [strict curvature theorem at that head](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/arithmetic/FULL_RANK_CURVATURE.md) proves a positive second difference on the full binary bounded branch. [PR192, all-shift denominator theorem](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-sixhour-20261127/arithmetic/SHIFT_DENOMINATORS.md) uses alignment of shortcut words. [PR193, rank division](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/arithmetic/RANK_DIVISION.md) uses integer combinations of shifted labels. Here the test concerns an arbitrary polynomial in the individual index and every actual ternary prefix, regardless of Hamming distance or tag sequence.

The first unsupported step toward exclusion on the bounded branch is to show that every nontrivial candidate has a sufficiently long interval with one weak sign at some higher difference, or to obtain an equivalent bound on cancellations. Strict positivity of the second differences supplies no such higher-order assertion. Beyond this branch a cycle can have exponents greater than two, and its reverse choices can exceed the two-child limit. The denominator-one case and escaping positive trajectories remain open.

## A quantitative version for every positive cycle

Choose any two positive exponents \(a,b\) of opposite parity. Let \(E\) count the edges of one positive rational primitive odd cycle whose actual exponent is outside \(\{a,b\}\). With the complete denominator \(q\), let \(H=\max_i(qx_i)-\min_i(qx_i)\) be the ordinary numerator span and \(J=\lceil\log_3(H+1)\rceil\). At most \(JE\) phases have an exceptional edge among their last \(J\) departures, counting incidences around the cycle. For \(J=0\) the span is zero and the cycle has one distinct odd phase.

The other phases form a two-child set **at all depths**. Through depth \(J\), an endpoint chooses the common predecessor exponent from the pair by the residue modulo three, since the two exponent parities differ. At depth \(J\) the actual surviving numerators are already pairwise distinct modulo \(3^J\), because \(H<3^J\). Each occupied prefix from this depth onward has only one of the finitely many rational phases in it. Multiplication by \(q\), a ternary unit, permutes all the children. This argument neither treats arbitrary long exponents as binary nor assumes extension of a finite path beyond its known history.

For any indexing of the distinct phases, and any \(g\) fixed nonzero rational tagging factors, Theorem 1 now gives
\[
 \#\{r\in I: Z_r=F(r)\}
 \le g\bigl(d2^{\lceil\log_3 |I|\rceil}-(d-1)\bigr)+B_I .
\]
Here \(F\in\mathbb Q[X]\) has degree \(d\ge1\), \(I\) is an integer interval of indices, and \(B_I\le\min(|I|,JE)\) counts its actual phases whose past contains an exception. Use \(F/c\) for each tag. Constants meet at most \(g\) ranks. With tag one this statement applies to every positive ordinary or rational cycle, independently of any rank chart or width bound.

There is a corresponding whole-denominator inequality for unrestricted cycles with dyadic integer tags (so all labels remain on the \(1/q\) lattice). For \(m\ge2\) take \(\mathcal L_m=3^k\) with \(3^k>2g(m-1)2^k\). In every block of \(\mathcal L_m\) consecutive zero \(m\)-th differences, more than half of its *first* \(\mathcal L_m\) participating ranks must be exceptional, by polynomial agreement. On a common-sign interval as above let \(B\) count actual exceptional ranks in the entire input interval. For each fixed \(i_2,\ldots,i_m\), at most \(2B/\mathcal L_m\) disjoint blocks of the \(t\) inspected first-coordinate positions can be completely zero. If \(t\ge 4\mathcal L_m+8B\), there are therefore at least \(t/(2\mathcal L_m)\) nonzero summands on that slice: subtract \(1+2B/\mathcal L_m\) from \(t/\mathcal L_m\). It follows that
\[
       q\ge\frac{(t/2)^m}{2\mathcal L_m X}
       \quad\text{whenever}\quad t\ge4\mathcal L_m+8B .
\]
Thus a supplied long interval of one sign requires either sufficient exceptional pasts or a large common reduced denominator. The frequency and arrangement of the other exponents in a general positive cycle remain unrestricted. The [five-column constructions](HIGHER_DIFFERENCES.md) exhibit the independent obstacle to proving the necessary sign behavior from local physical constraints.

## Replays and formal scope

[The exact Python controls](check_polynomial_rank.py) optimize over target trees on 2,392 polynomial and interval inputs, test 324 derivative trees, compare 431 convolution windows and audit three genuine rational periods; the largest has 306 odd phases and a 476-bit reduced denominator. [Recorded output](polynomial_rank_controls.json). [The Lean file](PolynomialRank.lean) checks the root-multiplicity budget over the three trits, finite occupied-child recurrence, tag union, difference transport/convolution, and stride magnitude bound, with standard axioms. The polynomial similarity, coloring of all depths and physical specialization are written proofs.
