# The complete Collatz denominator from a numerical semimodule

Let a nonconstant binary shortcut word have length \(n\), weight \(u\), positive determinant \(D=2^n-3^u\) and affine carry \(C\). We give a semimodule that determines \(\gcd(D,C)\) at the entire integer \(D\), including clocks with \(\gcd(n,u)>1\). The usual bijection between rational Dyck paths at coprime slope and normalized numerical semimodules is classical. The specialization below concerns the Collatz numerator and denominator. [Gorsky, Mazin and Vazirani, §5, Definition5.1](https://dmtcs.episciences.org/articles/2450/download)

## Primitive lattice slopes

First suppose \(\gcd(n,u)=1\), and let \(p_i\) count ones strictly before site \(i\). The heights \(u i-np_i\), \(0\le i<n\), give every residue modulo \(n\) once. Subtract their minimum and write the results \(e_i\). The set
\[
 S=\bigcup_{i=0}^{n-1}(e_i+n\mathbb N_0)
\]
contains zero, has finite complement in \(\mathbb N_0\), and is closed under adding \(u\) and \(n-u\). At a zero letter the next height is \(e_i+u\); at a one letter it is \(e_i-(n-u)\). Moving forward or backward along this step shows the two closure properties. Conversely, in any such set the least element in each class modulo \(n\) is defined. In the class reached by adding \(u\), its least element lies between \(e_i-(n-u)\) and \(e_i+u\) by the two closures. Those two endpoints are the only possibilities. This recovers the cyclic word, with its canonical root at height zero.

Choose integers \(h,k\) with \(uh+nk=1\) and put \(z=2^h3^k\bmod D\). Then \(z^u=2\) and \(z^n=3\) modulo \(D\). The polynomial
\[
 A_S(X)=(1-X)\sum_{s\in S}X^s
        =1-(1-X)\sum_{j\notin S,\ j\ge0}X^j
\]
has alternating nonzero coefficients of magnitude one. It has \(A_S(1)=1\) and degree at most \(u(n-u)\) by the two-generator Frobenius bound. At the indicated specialization,
\[
                           \gcd(D,C)=\gcd(D,A_S(z)).                     \tag{1}
\]
For example, let \(P=\sum_i X^{e_i}\), \(Q=\sum_{i:\,w_i=1}X^{e_i}\). Summing the differences of successive monomials gives \((X^u-1)P=X^{u-n}(X^n-1)Q\), while \(P=(1+\cdots+X^{n-1})A_S\). At the indicated residue the elements \(z,z-1,z^u-1,z^n-1\) are units, using \(z^u=2\) for \(z-1\). Also \(C\) is a unit multiple of \(Q(z)\), by the definition of the carry. This proves (1); a modulus of one is vacuous.

**An order obstruction.** Uniformly for \(1\le m\le K n^2\),
\[
                  \log\gcd(D,z^m-1)=o_K(n),\qquad
                  \operatorname{ord}_D(z)/n^2\longrightarrow\infty .    \tag{2}
\]
Take \(0\le r<n\) with \(ur\equiv m\bmod n\), and \(s=(m-ur)/n\). Then \(z^m=2^r3^s\bmod D\), \(|s|=O_K(n)\), and the exponent vectors of \(2^n3^{-u}\) and \(2^r3^s\) have determinant \(m\ne0\). The independent \(S\)-unit gcd bound applies to the entire modulus, with denominators cleared by units outside two and three. A linear form in logarithms gives \(D\ge2^n/n^{O(1)}\). This proves (2). In particular when \(A_S\) divides a product of a bounded number of polynomials \(X^{m_j}-1\) with \(m_j=O(n^2)\), every such cycle has reduced denominator \(2^{n-o(n)}\). In general \(A_S\) can be noncyclotomic. For example the gap set \(\{1,2\}\) gives \(1-X+X^3\) whenever both generators are at least three. The order bound does not exclude vanishing of an arbitrary boundary polynomial at this residue. [Independent-clock gcd proof](COMPLETE_MODULUS_TRACE.md)

## All clocks, with torsion retained

Put \(g=\gcd(n,u), N=n/g,U=u/g,V=N-U\), choose \(Uh+Nk=1\), and set
\[
 \mathcal G=\mathbb Z^2/\mathbb Z(n,-u)\cong\mathbb Z\times(\mathbb Z/g),
 \qquad (r,s)\mapsto(Ur+Ns,kr-hs).
\]
The integer change-of-basis determinant is minus one. Define \(a=(U,k)\), \(\sigma=(N,-h)\), \(b=\sigma-a\). The cyclic path has vertices \(v_i=ia-p_i\sigma\); its successive steps are \(a\) and \(-b\). Translate by a vertex of least first coordinate, making the minimum zero, and form
\[
                 \mathcal S=\bigcup_i (v_i+\mathbb N_0\sigma)
\]
with the translated vertices. Their classes modulo \(\sigma\) are all distinct: in the original lattice coordinates the class of \((1,0)\) modulo \((0,1)\) has order \(n\). Thus \(\mathcal S\) contains all sufficiently high full torsion fibers. It is closed under \(a,b\) by the same forward and backward inequalities. Conversely such a cofinite closed set with minimum height zero recovers the two choices by taking its least vertex in each \(\sigma\)-class, just as above, in the order of adding \(a\). The reconstructed word has weight \(u\), since \(na-u'\sigma=0\) in \(\mathcal G\) forces \(u'=u\). Different torsion normalizations describe the same cyclic word. The word is primitive exactly when \(\mathcal S\) has no nonzero torsion translation stabilizer. A proper word period translates the least vertices by a nonzero torsion point because the period vector has the full slope. Conversely such a stabilizer permutes their classes by a nonzero cyclic shift and preserves their outgoing choices.

For each height \(s\ge0\) let \(F_s\subset\mathbb Z/g\) be the torsion fiber. For \(j=0,1\) define the finite polynomials in the group ring \(Y^g=1\)
\[
 A_j(X,Y)=(1-X)\sum_{s\ge0}\sum_{f\in F_s} X^sY^{f-js} .
\]
They are finite since all sufficiently late fibers are full, supplying the same coefficient \(1+Y+\cdots+Y^{g-1}\) at every such height. Define residues
\[
 \lambda=2^N3^{-U},\qquad z=2^h3^k\pmod D.
\]
The first has exact order \(g\): for \(0<t<g\) one has \(0<2^{Nt}-3^{Ut}<D\). Also \(z^U\lambda^k=2\), \(z^N\lambda^{-h}=3\). This gives the full formula
\[
       \boxed{\gcd(D,C)=\gcd\big(D,A_0(z,\lambda),A_1(z\lambda,\lambda)\big).} \tag{3}
\]
Indeed the semimodule Hilbert series \(H=\sum_{(s,f)\in\mathcal S} X^sY^f\) has the finite least-vertex numerator divided by \(1-X^NY^{-h}\). At \((z,\lambda)\) this denominator is \(-2\), a unit. The monomial at the translated site \(i\) specializes to \(2^i3^{-p_i}\) times one common unit. Summing differences around the path, whose two multipliers are 2 and \(2/3\), gives \(\sum_{i:\,w_i=0}2^i3^{-p_i}=\tfrac13\sum_{i:\,w_i=1}2^i3^{-p_i}\) modulo \(D\). Therefore \(H(z,\lambda)\) is a unit multiple of the carry. The two polynomial evaluations in (3) equal \((1-z)H(z,\lambda)\) and \((1-z\lambda)H(z,\lambda)\). No prime dividing \(D\) divides both multipliers: that would force \(z=\lambda=1\) at that prime and hence \(2=z^U\lambda^k=1\). Taking the gcd with both evaluations proves (3), including all prime powers. A single evaluation can give an incorrect extra factor: at \((n,u)=(20,8)\) take seven initial ones, a zero, a one and eleven zeros, and \((h,k)=(3,-1)\). Then \(5\mid D\) and \(z-1\), but the carry is \(6433\), prime to five.

Every superlevel set \(\{s:|F_s|\ge j\}\), \(1\le j\le g\), is a shifted numerical semimodule over \(\langle U,V\rangle\), since adding either generator translates a fiber injectively into the later fiber. At the trivial torsion character their Hilbert series sum to the projected Hilbert series of \(\mathcal S\). This identity supplies an aggregate of smaller primitive clocks; it does not extract an integer cycle on one of them. The other torsion characters are required by (3). In particular physical word primitivity alone does not imply a primitive lattice slope. [Exact control on 3,109 rooted words](check_semimodule_denominator.py)
