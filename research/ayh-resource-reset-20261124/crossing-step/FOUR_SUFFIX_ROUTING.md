# Four fixed suffixes route actual tripling failures into every head arc

**Status.** Proposed written arithmetic and counting arguments for the positive shortcut map. The reduction from the directed tripling implication to universal convergence imports the finite certificate in PR193 at `67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e`, `research/astra-global-resolution-20261124/rewriting/SEVEN_RETURN.md`. No density theorem, pair-chain estimate or stochastic restart enters the routing. Universal convergence is open.

Let \(f\) be any invariant component label. Put \(D_a(u)=\mathbf1_{f(3^a u)\ne f(u)}\). Fix a nonempty open interval \(J\subset(7,8)\), and let \(H_J\) consist of the positive children \(x\) with \(x/81^j\in J\) for some integer \(j\ge0\). Use four suffixes only:

| Initial odd steps \(p\) | Multiplier exponent \(a=4-p\) | Suffix \(r=81-2^p3^a\) |
|---:|---:|---:|
| 0 | 4 | 0 |
| 1 | 3 | 27 |
| 2 | 2 | 45 |
| 3 | 1 | 57 |

**Routing theorem.** For \(p=1,2,3\) take any ordinary positive \(u\) prime to three. For \(p=0\) take **any** positive \(u\). There are arbitrarily large actual head edges \((x,m)\), with \(m=\lfloor x/81\rfloor\), \(x\in H_J\), and the indicated suffix, whose ordered colors are exactly \((f(3^a u),f(u))\). The two arms individually reach \(3^a u,u\) at the same finite clock. One such \(x\) satisfies \(u\le x\le C_Ju\), uniformly in \(u\). More generally the corresponding head **level indices** have bounded gaps for a fixed \(u,p,J\).

Indeed powers of 2 generate the units modulo 27 (the finite order is 18). Choose \(0\le k_0<18\) with \(2^{k_0}u\equiv-1\pmod {27}\). For \(p=0\) use \(k_0=0\) without a unit assumption. For every \(k=k_0+18t\), \(t\ge0\), set
\[
 v=(2^ku+1)/3^p,\qquad m=2^p v-1,\qquad x=81m+r=2^{p+k}3^a u.
\]
The integer \(m>0\) has the first \(p\) steps odd: after \(i\le p\) steps it is \(2^{p-i}3^i v-1\). Hence \(T^p m=3^p v-1=2^k u\), and \(T^{p+k}m=u\). Meanwhile \(T^{p+k}x=3^a u\). The checked arithmetic of the construction appears in `HeadRayRouting.lean`. As \(t\) increases, \(\log_{81}x\) advances by the irrational \(18\log_{81}2\). A finite initial segment of this rotation is an arbitrarily fine net of the circle. Thus among **any** \(C'_J\) consecutive \(t\)'s a point lands inside \(\log_{81}J\bmod1\), uniformly in the initial phase. This proves the size bound (including a bounded initial advance if needed to obtain \(j\ge0\)) and the bounded gaps of levels. The density here concerns the logarithmic indices of witnesses from a fixed seed, not ordinary density of those children on the rows.

**Original-weight comparison.** Write
\[
 A_j=81^{-j}\#\{x: x/81^j\in J,\ x\bmod81\in\{0,27,45,57\},\ f(x)\ne f(\lfloor x/81\rfloor)\},
\quad B(X)=X^{-1}\sum_{X\le n<2X}D_1(n).
\]
Set \(A_j=0\) for \(j<0\). There are constants \(C,K\) depending only on \(J\) such that for every integer \(j\ge0\)
\[
 B(81^j)\le C\sum_{q=0}^j 81^{-q}
          \sum_{|\ell-(j-q)|\le K} A_\ell + C81^{-j}. \tag{1}
\]
The proof applies also to a fixed multiple of the initial octave. For each fixed \(p\), among \(u\) in any fixed-ratio interval \([cY,C_0Y]\), choose the first successful phase in the fixed finite menu above. Since \(x=2^{p+k}3^au\), **each \(x\) has at most as many antecedents as there are menu entries**. All output rows have \(|\ell-\log_{81}Y|\le K\); normalization by \(Y\) is comparable with normalization by their row sizes. This bounds the normalized count of \(D_a(u)\) in that interval by a constant times the displayed local head sum, for units if \(a=1,2,3\), and all inputs if \(a=4\).

For a tripling comparison at \(n\) divisible by 81 write \(n=81m\). The triangle inequality through \(3m,m\) gives
\[
 D_1(81m)\le D_4(3m)+D_1(m)+D_4(m).
\]
The two fourth-power terms are covered by the preceding menu at scale \(X/81\); passing from \(3m\) to an entire interval only enlarges their count. The middle term contributes exactly \(B(X/81)/81\). For \(81\nmid n\), write \(n=3^i u\) with \(0\le i<4\) and \(3\nmid u\). Then \(D_1(n)\le D_i(u)+D_{i+1}(u)\), including \(D_0=0\). All these terms are similarly covered at scales comparable to \(X\). Iterate the resulting inequality with coefficient **exactly** \(1/81\) only on the recursive term; the bounded bottom scale contributes \(O(81^{-j})\). This proves (1). In particular summability of the four original head weights implies summability of the actual tripling discrepancy on these octaves. This alone is not pointwise tripling invariance.

**Pointwise closing consequence.** If all sufficiently high heads in \(J\) in these four suffixes are concordant, then \(f(81n)=f(n)\) on every positive integer and \(f(3^a u)=f(u)\) on every ternary unit for \(a=1,2,3\). Write \(n=3^k u\), \(3\nmid u\), and successively remove factors \(3^4\); it follows that \(f(3n)=f(n)\) for every positive \(n\). For the basin-of-one label the PR193 directed criterion now yields universal convergence. Specifically that source proves it suffices that convergence of \(9v+8\) implies convergence of \(8v+7\) for every \(v\ge0\); physically \(T^3(3(8v+7))=9v+8\). Thus if any counterexample exists, in every prescribed \(J\) at least one of the four suffixes supplies genuine discordant edges on a syndetic set of sufficiently high levels. Accordingly it even suffices to find arbitrarily long consecutive runs of levels with no such discordant edge. The count lower bound from one seed is one or more edges on those levels. Their ordinary row fractions can still be exponentially small.

**The exact directed native cylinder.** PR193 also supplies the equivalent implication \(36k+8\in C\Rightarrow72k+17\in C\) for all \(k\ge0\). The two antecedent/consequent orbits respectively reach \(z=9k+2\) and \(9z+2=81k+20\) after two and three clocks. The head pair with \(m=8k+1,r=79\) reaches the same ordered parent/child endpoints at clock three; \(m=16k+3,r=77\) does so at clock four. Thus the directed parent-to-child condition on either one of these affine cylinders, **without a mantissa restriction**, is itself equivalent to universal convergence. The quartet from PR197 at `6eb986b0ce0b1836a356474d25d709ed4e948b67`, `joint-renewal/QUARTET_COLLAPSE.md`, has the additional restriction \(z=27q+20\). It does not cover the two other ternary lifts by the preceding identity.

**Scope of combining this test with native fiber projection.** A witness from one fixed failing seed has child a multiple of \(2^{p+k}\). For every clock \(h\le p+k\) its child word is all even. In a labeled block of \(2^h\) consecutive parent integers and at its fixed suffix, there is only one such parent: the congruence \(81m+r=0\bmod 2^h\) has one class since 81 is odd. Thus the exact ordered record at that witness has a singleton fiber on the block, already from its child's zero odd count. Although varying the seed transfers original counts with bounded multiplicity in (1), a single pointwise failure need not lie in any of the polynomially dense good fibers at large clocks. Symmetric triples only guaranteed in those retained fibers do not bridge this exception.
