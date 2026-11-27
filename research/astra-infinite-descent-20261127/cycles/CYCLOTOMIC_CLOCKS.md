# Unramified clock factors sharpen the denominator exponent

Use the separated signed sum or the arbitrary small-height arc covers of [MOVING_ARCS.md](MOVING_ARCS.md). Let \(s\) bound the number of surviving terms and let \(g_n=\gcd(h_n,p_n)\). If eventually every prime dividing \(g_n\) is at least \(P>\max(s,3)\), then
\[
 \liminf_n\frac{\log_2 q_n}{h_n}\ \ge\ 1-\frac{s-1}{P}.                 \tag{1}
\]
When the clock gcd is a fixed prime \(\ell\ge5\) with \(\ell>s\), the stronger lower bound \(1-1/\ell\) holds. The only possible accumulation values in that case are \(1-1/\ell\) and one. An empty set of prime divisors, when \(g_n=1\), gives the full exponent one.

Here are the additional algebraic steps in the moving theorem. On a subsequence the fixed character degree is \(d\), \(X_n=c_nT_n^d\), and the limit exponent is \(J/d\), the proportion of roots of \(c_nT^d-1\) missed by the common factor. Keep \(\delta=\gcd(d,h_n,p_n)\) constant on a further subsequence. This is possible since \(\delta\mid d\). The identity for \(X_n\) gives
\[
 \delta=\gcd(d,v_2(c_n),v_3(c_n)),\qquad
 d_0=d/\delta,\quad c_n=c_{0,n}^{\delta},\quad
 \gcd(d_0,v_2(c_{0,n}),v_3(c_{0,n}))=1
\]
with \(c_{0,n}\) a positive rational \(\{2,3\}\)-unit. The positivity removes any sign ambiguity from the rational root.

If \(\gcd(\delta,6)=1\), every \(\mathbb Q(\zeta)\) for \(\zeta^\delta=1\) is unramified at two and three. One can see this from separability of \(T^\delta-1\) in both residue characteristics and the discriminant criterion. Over \(K=\mathbb Q(\zeta)\), the binomial
\[
 T^{d_0}-\zeta/c_{0,n}
\]
is irreducible. Indeed any monic factor of degree \(a>0\) has nonzero constant term. At each place of \(K\) over \(l=2,3\) the valuation normalized by \(v(l)=1\) is integer-valued on \(K^\times\). Every root has valuation \(-v_l(c_{0,n})/d_0\). Thus \(d_0\mid a v_l(c_{0,n})\) at both primes. The displayed gcd condition forces \(d_0\mid a\). Together with transitivity of the Galois action on primitive roots of any order \(e\mid\delta\), this shows every rational factor of \(c_nT^d-1\) chooses entire disjoint sets of \(d_0\varphi(e)\) roots, one set for each \(e\mid\delta\). [Conrad, *Discriminants and ramified primes*](https://kconrad.math.uconn.edu/math5230f12/handouts/disc.pdf) · [Conrad, *Cyclotomic extensions*](https://kconrad.math.uconn.edu/math5211s13/handouts/cyclotomic.pdf)

In particular
\[
 J/d=\delta^{-1}\sum_{e\in E}\varphi(e)
 \quad\text{for some nonempty } E\subseteq\{e:e\mid\delta\}.
\]
For fixed prime clock gcd \(\ell\), \(\delta\in\{1,\ell\}\), giving possible values \(1/\ell,(\ell-1)/\ell,1\). Since \(J/d\ge1/s\), the first is impossible when \(\ell>s\).

For (1) use a rational linear-independence fact. If every prime dividing \(m\) is at least \(P\), any list of fewer than \(P\) **distinct** \(m\)-th roots of unity is linearly independent over \(\mathbb Q\). Induct on \(m\). Remove a prime \(l\), writing \(m=l m'\). If \(l\mid m'\), \([\mathbb Q(\zeta_m):\mathbb Q(\zeta_{m'})]=l\), and the powers of \(\zeta_m\) with exponents \(0,\ldots,l-1\) are linearly independent over the smaller field. Group a proposed relation by these \(l\) exponents and apply induction to each group. If \(l\nmid m'\), use the unique product representation of roots by an \(l\)-th root and an \(m'\)-th root. Over \(\mathbb Q(\zeta_{m'})\) the minimal polynomial of a primitive \(l\)-th root is \(1+T+\cdots+T^{l-1}\) by multiplicativity of the cyclotomic degree. Every relation forces the coefficients in all \(l\) groups to be equal. At least one group is empty since fewer than \(P\le l\) roots occur, so every group vanishes and induction again applies.

Now fix one occupied \(Z\)-character in \(G_n\), and one occupied residue \(a\bmod d_0\) among its powers \(m_j\). On \(T^{d_0}=\zeta/c_{0,n}\), the coefficient of \(T^a\), using the power basis of the degree-\(d_0\) extension of \(K\), is
\[
 \sum_j b_{j,n}\zeta^{k_j},\qquad
      m_j=a+d_0 k_j,\quad b_{j,n}\in\mathbb Q^\times .
\]
Negative original powers are allowed, since the displayed binomial has nonzero constant term. The \(k_j\) are distinct modulo \(\delta\) by the distinct-residue argument of the moving theorem. There are at most \(s<P\) of them. Choose any one frequency \(k_0\) among them. If its root \(\zeta^{k_0}\) differs from all the other listed roots, collect any other equal roots. The independence fact prevents the sum from vanishing. For each \(k_j\ne k_0\pmod\delta\), at most \(\gcd(\delta,k_j-k_0)\le\delta/P\) of the \(\delta\) choices of \(\zeta\) produce a collision. Therefore at least \(\delta(1-(s-1)/P)\) choices have a nonzero coefficient of \(T^a\). Irreducibility makes the entire \(Z\)-coefficient nonzero at all \(d_0\) roots above each such \(\zeta\). These roots are absent from the common factor, which proves (1). The case \(\delta=1\) follows directly from irreducibility and the uniqueness of occupied residues.

The prime-clock rate \(1-1/\ell\) can occur already for the two-atom determinant difference \(C=2^m-3\), \(D=2^{\ell m}-3^\ell\) at \(h=\ell m,\ p=\ell\): the reduced denominator of \(C/D\) is \(D/C\). This example concerns the signed-sum theorem. In a rational-cycle application \(q\) always means the value for the actual word or designated fixed-point difference. Ramification at two or three prevents this argument from giving the same classification when \(\delta\) shares those prime factors. The fixed-dimensional Diophantine height input still comes from the moving theorem.
