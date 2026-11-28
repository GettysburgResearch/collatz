# Positive ordinary basin cuts defeat full-support power-weight coercivity

Write \(C_Tf(n)=f(Tn)\), where \(T\) is the positive integer shortcut. Take any fixed \(p>1\) and put \(w(n)=n^{-p}\). In the Hilbert space \(\ell^2(w)\) there are pairwise orthogonal unit vectors \(u_r\), each a positive constant times the indicator of a true predecessor basin contained in the known component of one, with
\[
       \|(I-C_T)u_r\|_{\ell^2(w)}^2 \le (2/3)^{pr}.                  \tag{1}
\]
Each residual is supported at a single actual odd source. The same construction works on the known component alone. Every finite atom has positive weight, including each of these residual atoms. There is no coercive lower bound on the orthogonal complement of any fixed finite-dimensional subspace. In particular, subtracting each indicator's \(w\)-mean does not restore such a bound. This is an unconditional finite-arithmetic construction.

## A terminating witness inside each set

Use the explicit terminating ramplines of PR211's operator spectrum proof. For \(r\ge1\) set
\[
 k_r=(3^r+1)/2,\qquad a_r=(4^{k_r}-1)/3=(2^{3^r+1}-1)/3.
\]
The first step from \(a_r\) reaches \(2^{3^r}\), and all later steps remain powers of two. Every \(a_r\ge5\) is odd and the list is strictly increasing. Consequently their predecessor sets \(B_r=\{n:\exists j,\ T^j n=a_r\}\) are pairwise disjoint: an orbit visiting two would force one root's power-of-two future to contain the other. [PR211, terminating paths used for the operator spectrum, at 4b44cded44af5bb7c3ce67fb16a70c898ad505d5](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase2/OPERATOR_SPECTRUM.md)

The divisibility \(3^{r+1}\mid 2^{3^r}+1\) follows by induction. At level zero \(2+1=3\), and passing from \(v\) to \(v^3\) multiplies \(v+1\) by \(v^2-v+1\), divisible by three when \(v\equiv-1\bmod3\). Since \(a_r+1=2(2^{3^r}+1)/3\), one gets \(3^r\mid a_r+1\). The integer
\[
                   x_r=2^r(a_r+1)/3^r-1
\]
is odd and positive. Indeed \((a_r+1)/3^r\) is a positive integer. The successive states
\(2^{r-i}(a_r+1)/3^{r-i}-1\), \(0\le i\le r\), give ordinary integer odd departures at \(i<r\). As \(T(x)+1=3(x+1)/2\) at such a departure, the last state is \(a_r\). Thus \(x_r\in B_r\), and
\[
             x_r=(2/3)^r a_r+(2/3)^r-1\ \le\ (2/3)^r a_r.           \tag{2}
\]
The first examples are \(3\to5\to8\) and \(151\to227\to341\to512\).

## The forward defect and the orthogonal sequence

For \(n\ne a_r\), forward determinism gives \({\bf1}_{B_r}(n)={\bf1}_{B_r}(Tn)\). At \(n=a_r\) their values are respectively one and zero, since the powers of two never return. Hence
\[
                  (I-C_T){\bf1}_{B_r}={\bf1}_{\{a_r\}}.              \tag{3}
\]
Writing \(m_r=\sum_{n\in B_r}w(n)\), we have \(m_r\ge w(x_r)>0\) and \(m_r<\infty\) by \(p>1\). Therefore \(u_r={\bf1}_{B_r}/\sqrt{m_r}\) are orthonormal. Equations (2)–(3) give directly
\[
  \|(I-C_T)u_r\|^2=\frac{w(a_r)}{m_r}
             \le \frac{w(a_r)}{w(x_r)}
             =(x_r/a_r)^p\le(2/3)^{pr}.
\]
The composition operator is bounded: at most two \(n\)'s map to a given \(y\), and \(y\le2n\) gives \(w(n)\le 2^p w(y)\). Orthogonality implies \(u_r\rightharpoonup0\). For a fixed finite-dimensional orthogonal projection \(P\), \(Pu_r\to0\) in norm. Thus the normalized projections of \((I-P)u_r\) remain approximate eigenvectors, by boundedness of \(I-C_T\). This supplies a singular sequence for the **forward** operator at one. In particular \(I-C_T\) cannot be invertible modulo compact operators: a left inverse up to compact error applied to \(u_r\) would contradict its unit norm.

For the binary cut form \(\mathcal E(f)=\sum_n w(n)|f(n)-f(Tn)|^2\), the mass-to-boundary ratio \(m_r/\mathcal E({\bf1}_{B_r})\) is at least \((3/2)^{pr}\), on certified convergent sets only. If a weighted argument proves extinction, it must use more structure than a uniform spectral-gap or cut-coercivity inequality for this energy.

PR211 already constructs disjoint normalized forward columns on precisely these terminating predecessor trees for its squared-slope operator on unweighted counting space. Each column uses the product of squared slopes up to the first hit, has a one-coordinate residual, and becomes an approximate eigenvector. Its separate local-algebra note also gives an adjoint construction and the complete essential spectral disk. Our all-weight binary cut argument uses invariant indicators under plain composition and an arbitrary monotone summable vertex mass. For \(p=4\), unitary conjugation here gives weight \((Tn/n)^2\), which differs from those squared slopes by a sequence tending to zero. The essential-spectrum membership in that case is consistent with the earlier result. Our conclusion concerns explicit positive indicators, a one-point forward defect, the quotient by arbitrary finite-dimensional subspaces, and all summable power weights. The terminating paths themselves are prior. [PR211, local operator algebra and adjoint singular sequence](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/rigidity/phase2/LOCAL_OPERATOR_ALGEBRA.md)


## Every decreasing summable weight

More generally take *any* positive nonincreasing summable weight \(w:\mathbb N_{>0}\to(0,\infty)\). Every one of the \(r+1\) actual ramp vertices in (2) is at most \(a_r\), all are distinct, and all lie in \(B_r\). Indeed the displayed states plus one increase by a factor \(3/2\) at every step. Hence
\[
       m_r\ge(r+1)w(a_r),\qquad
       \frac{\mathcal E({\bf1}_{B_r})}{m_r}
          =\frac{w(a_r)}{m_r}\le\frac1{r+1}.                         \tag{4}
\]
Their normalized indicator sequence is again orthonormal. When \(C_T\) is bounded, (4) gives the same essential approximate eigenvalue. Boundedness is equivalent to \(\sup_y\sum_{Tn=y}w(n)/w(y)<\infty\), by directly summing the square norm on each disjoint fibre. This condition can fail for a rapidly decreasing weight. The cuts still belong to the natural domain \(\{f\in\ell^2(w):f\circ T\in\ell^2(w)\}\) by the exact identity (3). Given any finite-dimensional \(F\) in that domain, the compositions of its orthogonal projections of \(u_r\) tend to zero: the projections tend to zero in norm by weak convergence, and the restriction \(C_T|_F\) is bounded on a finite-dimensional space. This again rules out a uniform lower coercivity bound on \(F^\perp\) within the domain. The faster exponential-in-\(r\) estimate (1) exploits power weights; the all-weight conclusion needs only monotonicity and summability.
