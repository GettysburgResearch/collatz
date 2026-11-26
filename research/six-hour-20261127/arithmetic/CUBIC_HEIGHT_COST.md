# Degree required to cancel cubic heights on an ordinary Collatz interval

**PROPOSED written theorem.** All estimates concern one actual finite interval. The application to an escaping source is conditional. Collatz remains open.

Use the positive odd map \(2^{a_i}x_{i+1}=3x_i+1\) on \(m\ge1\) consecutive odd departures, with \(H=\sum_{i<m}a_i\). Assume \(3\nmid x_0\), so all \(m+1\) vertices are coprime to six. Define
\[
 E_i=(\sqrt{3x_i+1}+\sqrt{3x_i})^2,\quad
 F_i=\mathbb Q(\sqrt{3x_i(3x_i+1)}),\quad
 t_i=E_i^{1/3}+E_i^{-1/3},\quad
 U_i=\frac{(t_i+1)(t_i+2)}{(t_i-1)(t_i-2)},\quad V=\prod_{i<m}U_i .
\]
Radicals refer to the positive real choices. Assume the \(m\) fields \(F_i\) are pairwise distinct. A sufficient condition is \(\min_i x_i>4\cdot36^H\).

**Theorem A.** Write \(T=\sum_{0\le i<j\le m}\log\gcd(x_i,x_j)\). For every nonzero algebraic scalar \(\lambda\) of degree \(D=[\mathbb Q(\lambda):\mathbb Q]\), there is \(J\subseteq\{0,\ldots,m\}\) with \(|J|\le1+\lfloor\log_3 D\rfloor\) such that its absolute logarithmic Weil height satisfies
\[
 h(\lambda V)\ge\tfrac14\sum_{i\notin J}\log x_i-T,\qquad
 T\le {m+1\choose2} H\log3 . \tag{1}
\]
The choice of scalar may depend on the entire interval and may lie outside the orbit field. The original product has the sharper asymptotic
\[
 h(V)=\tfrac13\sum_{i=0}^m\log x_i+O(T+H+m), \tag{2}
\]
with absolute implicit constant. In particular let \(m\to\infty\), \(X=\min_i x_i\to\infty\), \(mH=o(\log X)\). Then \(h(\lambda V)=o(m\log X)\) requires \(D\ge3^{(1-o(1))m}\).

**Exact comparison.** The degree of \(V\) equals \(3^m\). The actual recurrence gives
\[
 V=rW^3,\qquad r=\frac{2^H x_m}{3^m x_0},\qquad W=\prod_{i<m}\frac{t_i+1}{t_i-1}. \tag{3}
\]
Thus the exact cancellation has \([\mathbb Q(W^{-3}):\mathbb Q]=3^m\), while \(h(W^{-3}V)=h(r)\le H\log2+m\log3+\log x_0+\log x_m\).

## 1. The required field and embedding statements

One has \(E_i+E_i^{-1}=12x_i+2\) and
\[
 P_i(t_i)=0,\quad P_i(t)=t^3-3t-(12x_i+2),\quad
 (t_i-2)(t_i+1)^2=12x_i,\quad
 (t_i+2)(t_i-1)^2=4(3x_i+1).
\]
The translate \(P_i(z+2)\) is Eisenstein at three. The negative discriminant gives one real and two complex roots. The factorizations rewrite \(U_i\) as
\[
 \left(\frac{t_i+1}{t_i-1}\right)^3\frac{3x_i+1}{3x_i}.
\]
Taking the norm gives one, using \(\operatorname{Norm}(t_i+1)=12x_i\) and \(\operatorname{Norm}(t_i-1)=4(3x_i+1)\). The physical value exceeds one, while both other conjugates have modulus \(U_i^{-1/2}<1\). Multiplication proves (3).

Let \(K\) be the compositum of all \(F_i\) and \(\mathbb Q(\mu_3)\). The norm-one unit \(E_i\) is a noncube in \(F_i\). A purported cube root would be an integral unit with norm one, and its sum with its inverse would be an integral rational root of \(P_i\). A norm down the power-of-two extension \(K/F_i\) preserves the noncube conclusion. Each line \([E_i]\in K^\times/K^{\times3}\) transforms by the quadratic character of \(F_i\), since conjugation inverts \(E_i\). The characters are distinct. Averaging over the multiquadratic Galois group with one character projects onto its eigenspace since the group order is invertible modulo three. The classes are independent. Kummer theory gives
\[
 M=K(E_0^{1/3},\ldots,E_{m-1}^{1/3}),\qquad
 \operatorname{Gal}(M/K)\simeq(\mathbb Z/3)^m .
\]
Each coordinate rotation permutes the three roots \(\zeta^c E_i^{1/3}+\zeta^{-c}E_i^{-1/3}\). Above any one embedding of \(K\) the \(m\) root choices are independent and uniform. The quadratic characters need only be distinct.

Every nonidentity element of this cubic rotation group lowers the physical modulus of \(V\), since it changes at least one factor from the unique maximizing conjugate. Its orbit has size \(3^m\). Over \(\mathbb Q\) the product lies in a compositum of \(m\) cubic fields of degree at most \(3^m\), proving the claimed degree. Multiplication by \(r\ne0\) and inversion preserve it.

For the effective distinctness test, if \(i<j\) have the same \(F\), then \(L=E_j/E_i\) is a norm-one unit and \(L+L^{-1}\in\mathbb Z\). Write the intervening native affine equation \(d x_j=g x_i+C\), \(d=2^s,\ g=3^\ell,\ 0<C\le3^s-2^s\), \(s\le H\). The last bound follows by comparing the carry updates with the all-odd native word. The odd numerator of \(g/d+d/g\) over the even grid \(dg\) gives distance at least \(1/(dg)\ge6^{-H}\) from every integer. Since \(E_i=12x_i+e_i\), \(1<e_i<2\), we have \(|d E_j-g E_i|\le16\cdot3^s\). Using \(x_j\ge x_i/d\) gives \(|L-g/d|+|L^{-1}-d/g|\le4\cdot6^H/x_i\), hence \(x_i\le4\cdot36^H\).

These field statements reconstruct C1, C2, C5 and P2 from PR192, head ed7a6fe30b8602407f77855ceb74ce0489ce9c10. The sources are [CUBIC_FIELDS.md](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/adelic/CUBIC_FIELDS.md) and [PELL.md](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/adelic/PELL.md). For the external Kummer correspondence see [J. S. Milne, Fields and Galois Theory, chapter 5](https://www.jmilne.org/math/CourseNotes/ft.html).

## 2. Outside-prime valuation distribution

At \(p\ge5\) set \(b_i=v_p(x_i)\). Adjacent \(b_i,b_{i+1}\) cannot both be positive. If \(b_i>0\), on edge \(i\) the residue root \(2\) is simple, and the two other roots reduce to \(-1\). The two factorizations above give valuations \(-b_i,b_i/2,b_i/2\) of \(U_i\). If \(b_{i+1}>0\), the simple residue root is \(-2\), the others reduce to \(1\), and the valuations are \(b_{i+1},-b_{i+1}/2,-b_{i+1}/2\). These formulas include primes ramified in the quadratic local factor. If both exponents vanish, every conjugate is a unit.

Consequently there are variables \(Z_{j,p}\) on the three root choices for edge \(j\), taking \(1,-1/2,-1/2\), such that
\[
 v_p(\sigma V)=\sum_{i=0}^m b_i(Z_{i-1,p}-Z_{i,p}),\qquad Z_{-1,p}=Z_{m,p}=0. \tag{4}
\]
Use the simple root as the distinguished choice for each edge with nonzero coefficient. Any choice works on the other edges. In a fiber of embeddings over \(K\) these variables are independent and have mean zero.

Put \(L=\mathbb Q(\lambda)\), \(E=ML\). Restriction identifies \(\operatorname{Gal}(E/KL)\) with a subgroup \(G\) of \((\mathbb Z/3)^m\) of codimension at most \(\lfloor\log_3D\rfloor\), because \(E/KL\) is Galois and \([E:KL]\ge[M:K]/[KL:K]\ge3^m/D\). At most that many coordinate projections vanish on \(G\). Let \(J\) comprise vertices for which every incident edge has such a vanishing projection. Apart from vertex zero, each is assigned to its own preceding fixed edge, giving the asserted size.

At a contributing prime choose \(i\) where \(b_i\) is largest, breaking ties arbitrarily, and put \(B_p=\sum_{j\ne i}b_j\). If \(i\notin J\), select \(\tau\in G\) rotating at least one adjacent edge. Use the uniform measure on embeddings \(\sigma:E\hookrightarrow\overline{\mathbb Q}_p\). In each fiber over \(K\) the restriction to \(M\) is still uniform, since all embeddings extend the same number of times. The contribution of \(b_i\) to \(v_p(\sigma V)-v_p(\sigma\tau V)\) has mean absolute value at least \(b_i\). A nontrivial rotation changes \(Z\) by \(0,3/2,-3/2\) with probabilities \(1/3\) each. If both edges rotate, the initial choices on them are independent. Adding the other centered difference cannot decrease the first absolute moment by convexity. At an endpoint there is one incident edge.

Each other vertex contributes at most \(3 b_j\) to the absolute difference. Right composition by \(\tau\) permutes embeddings, and \(\tau\) fixes \(\lambda\). Thus
\[
  2\,\mathbb E_\sigma |v_p(\sigma(\lambda V))|
  \ge \mathbb E_\sigma |v_p(\sigma V)-v_p(\sigma\tau V)|
  \ge b_i-3B_p. \tag{5}
\]
The chosen rotation may depend on \(p\). The same scalar is used at every place.

The product formula gives \(2h(z)\) as the sum over all places of the mean absolute logarithms of conjugates, with normalized local weights. Moreover \(\sum_p B_p\log p\le T\), since the pairwise gcds with the maximal index account for all other exponents. The dominant mass at indices outside \(J\) therefore totals at least \(\sum_{i\notin J}\log x_i-T\). Summing (5) proves (1). Finally \(\gcd(x_i,x_j)\) divides the intervening positive carry \(C\le3^H\), proving the claimed bound on \(T\).

For (2), the mean absolute value of \(Z_{i-1,p}-Z_{i,p}\) equals \(2/3\). At an interior vertex exactly one of the two choices is distinguished with probability \(4/9\), causing a jump of \(3/2\). At an endpoint \(\mathbb E|Z|=2/3\). The remaining terms in (4) have total absolute value at most \(3B_p/2\). This gives the main term at primes at least five with error \(O(T)\). At two the individual conjugate valuations are \(a_i,-a_i/2,-a_i/2\), so the total cost is \(O(H)\). Indeed the unique even root gives \(a_i\) by the second expression for \(U_i\), and the odd roots give the other values by the two factorizations. At three the translated cubic is Eisenstein, \(v_3(t_i-2)=1/3\), \(v_3(t_i+1)=1/3\), and each conjugate of \(U_i\) is a unit. At infinity \(\log U_i\) is uniformly bounded. The rational function defining \(U_i\) decreases for \(t_i>2\), and its positive argument increases with \(x_i\). The other conjugates have logarithmic modulus \(-(\log U_i)/2\). This proves (2).

## 3. One-source and known convergent controls

On a hypothetical injective odd orbit \(x_i\to\infty\). For fixed \(m\), there are arbitrarily late \(m\)-edge windows of native length at most \(2m\). Otherwise all sufficiently late disjoint \(m\)-blocks would have clock at least \(2m+1\), contradicting \(\sum_{i<n}a_i\le2n+\log_2x_0\) from \(2^{a_i}x_{i+1}\le4x_i\). Thus windows can be chosen along the same source with \(m\to\infty\), \(H\le2m\), and \(\log X\ge m^3\).

Known convergent starts also realize this obstruction on arbitrarily long high windows. Given \(m\), put \(\ell=m+1\), \(e=1+(2k+1)3^\ell\), \(u=(2^e+2)/3^{\ell+1}\) for an integer \(k\ge0\). This is a positive even integer since \(2^{3^\ell}\equiv-1\bmod3^{\ell+1}\) by induction. The source \(2^\ell u-1\) has \(\ell\) consecutive odd exponents one, ending at \(3^\ell u-1=(2^e-1)/3\), whose next odd state is 1. Omit the first edge to ensure all states are coprime to six. The resulting \(m\)-window has \(H=m\). By increasing \(k\) one can make its minimum exceed any prescribed threshold. This family uses changing initial sources.

**First unsupported step toward closure.** An upper bound of endpoint size for \(h(\lambda V)\), on a suitable sequence of high windows of *every hypothetical escaping source*, together with a degree saving of the form \(D\le3^{(1-\delta)m}\) for fixed \(\delta>0\), would contradict (1). The ordinary telescope (3) gives exactly \(3^m\). The known convergent controls likewise require exponential degree. A proof using this criterion would need all-time information about the fixed source beyond a single finite high interval.

