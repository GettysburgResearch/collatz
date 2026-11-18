# Automatic errors are impossible for an unbounded rational-base integer trajectory

**Proposed corollary of the new finite-place argument.** Let $P>Q\ge2$ be coprime integers, and let $(x_n)$ be integers such that $d_n=Qx_{n+1}-Px_n$ takes only finitely many values. If $(d_n)$ is automatic in any integer base $k\ge2$, then $(x_n)$ is bounded. This proof depends on the [finite-place independence argument](PROOF.md). It does not require the multivariate lifting proposition in rStation paper 16.

Write $\alpha=Q/P$ and choose any prime $p\mid Q$. Let $f(z)=\sum_{n\ge0}d_nz^n$. Telescoping gives $f(\alpha)=-P x_0$ in $\mathbb Q_p$. To show equality in the real embedding too, put the generating functions of all members of the finite $k$-kernel of the error word into a column $G$, with an additional coordinate equal to 1. Splitting each series by residue classes modulo $k$ gives $G(z)=M(z)G(z^k)$ with rational polynomial entries, allowing repeated kernel members. The constant coordinate uses $1=1$.

Select from $G$ a basis $F$ for its component span over $\mathbb Q(z)$ and write $G=RF$. Its components are still independent over $\overline{\mathbb Q}(z)$: clear denominators of a putative dependence and expand all algebraic coefficients in a number-field basis over $\mathbb Q$. Selecting the corresponding rows in the kernel identity gives $F=A(z)F(z^k)$ over $\mathbb Q(z)$; a left kernel of $A$ would contradict independence of $F$. At $\beta=\alpha^{k^m}$ for some sufficiently large fixed $m$, all iterates avoid the poles of $A,A^{-1},R$, since their union is finite. All the functions converge for $|z|<1$ in both completions.

Let $v$ be the rational row encoding $P x_0+f(\alpha)=0$. Its transported row
$$
 w=v M(\alpha)M(\alpha^k)\cdots M(\alpha^{k^{m-1}})R(\beta)
$$
has rational entries and annihilates $F(\beta)$ at $p$. The proposed finite-place independence theorem implies $w=0$. The same identities therefore give $P x_0+f(\alpha)=0$ over the reals as well. The real tail formula
$$
x_n=-\frac1P\sum_{j\ge0}d_{n+j}\alpha^j
$$
bounds $|x_n|\le \max_j|d_j|/(P-Q)$ uniformly.

In particular the positive ceiling orbit $x_{n+1}=\lceil Px_n/Q\rceil$, $x_0\ge1$, is strictly increasing and its error word in $\{0,\ldots,Q-1\}$ cannot be automatic. For $P/Q=3/2$, $d_n=x_n\bmod2$. Starting at $1$ produces the rational-base minimal word $g_{3/2}$, with the one-place indexing convention explained by Stephan. His Theorem B states that automaticity would imply transcendence of the real growth constant; the proposed argument here directly excludes automaticity by using both completions. It gives no value or arithmetic classification of the growth constant. Stephan’s Appendix A also identifies the noninvariance of separate matrix-variable degrees under a constant linear substitution and the need for a fixed coefficient field. Our local proof uses total degree and fixes the field before the auxiliary polynomial construction. [Stephan, *Transcendence criteria for the minimal word of the rational base 3/2*, Remark 1.1, Theorem B and Appendix A](https://arxiv.org/abs/2609.19007)

For the physical six-branch chart $P=3^{12}>Q=2^{19}$ the same conclusion applies to a positive integer survivor with strictly increasing heights and its six fixed errors. The physical parity coding gives a separate source-qualified route through the automatic parity theorem in paper 16. [Physical coding and prior source](../rotation-coded-orbits/PRIOR_WORK.md)
