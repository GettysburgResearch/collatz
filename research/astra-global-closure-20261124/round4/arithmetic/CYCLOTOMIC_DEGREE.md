# Denominators from the degree of the reference carry sum

**PROPOSED written theorem.** The quadratic-residue template is one case of a degree bound at a primitive root of unity. This version permits arbitrary many equal-clock reference blocks, arbitrary prime slot count $N\ge5$, and the same interval replacements as in the [quadratic theorem](README.md). An undamaged reference invariant under reflection already forces an exponential denominator when the block length exceeds a large enough multiple of $\log N$, even if every pair of reflection-related slots uses a different word.

Let $U_i$ be any length-$L$, weight-$p$ binary block at each slot $i\bmod N$, with $Q=2^L>P=3^p$, $p\ge1$. Let $A_i$ be its integer carry, $V(X)=\sum_{i=0}^{N-1}A_i X^i$, and $\alpha=V(\zeta)$ for a primitive $N$th root $\zeta$. Suppose the $N-1$ carries indexed by nonzero slots are not all equal. Set $m=[\mathbb Q(\alpha):\mathbb Q]$. Then $m$ is the index in $(\mathbb Z/N)^\times$ of the group of multipliers that preserve the entire list of the nonzero-indexed carries. Indeed $V(\zeta^b)=V(\zeta)$ exactly if the polynomial of reduced exponents in their difference is a multiple of $\Phi_N=1+X+\cdots+X^{N-1}$. Its constant coefficient is zero and its degree at most $N-1$, so it vanishes identically. This proves the index formula by the Galois action and gives $m>1$.

Write $d$ for the full reduced denominator of the altered word, with $r\ge1$ displaced intervals of individual lengths at most $H$ and with each interval preserving its total weight. With the definitions $D=(Q-P)S$ and $g=\gcd(S,C)$ at the common cut from the [main proof](README.md), every $1\le K$ with $K^r<N$ gives

$$
 d\ \ge\ \frac{Q^{N-1-2mN/K}}{\big((N+r)3^{HL}\big)^{mK^r}}.             \tag{5}
$$

To prove (5), set $B=P^{H-1}$ and use $E_j=P^{H-h_j}J_j$ as before. The physical equation now gives $B V(t)+\sum E_jt^{a_j}=0\bmod g$, where $t=Q/P$. In particular $\Phi_N(t)=0$ without requiring $t-1$ to be invertible. Let $M_\alpha(Y)$ be the monic integer minimal polynomial of the algebraic integer $\alpha$. Since $\Phi_N$ is monic, $\Phi_N(X)\mid M_\alpha(V(X))$ in $\mathbb Z[X]$. Thus the same polynomial vanishes at $V(t)$ modulo the complete numerical $g$.

Use the simultaneous approximation and the unit $z$ from (3) of the main proof, retaining $u<N$, $z^u=t$, signed exponents $s_j$, $T=\max|s_j|<N/K$ and $E(X)=\sum E_j X^{s_j}$. The integer polynomial

$$
 G(X)=X^{mT}(-B)^m M_\alpha(-E(X)/B)
     =X^{mT}\prod_{\alpha'}(E(X)+B\alpha')
$$

has degree at most $2mT$ and vanishes at $z$ modulo $g$. Here $B$ is a power of $P$, a unit modulo $g$, and $\alpha'$ runs once over the conjugates. They all satisfy $|B\alpha'|\le N3^{HL}$, since $|A_i|<3^L$ and $B\le(3^L)^{H-1}$. As $\|E\|_1\le r3^{HL}$, multiplication of the factors bounds $\|G\|_1\le((N+r)3^{HL})^m$.

**Nonvanishing at every conjugate root.** Suppose a common characteristic-zero root $x$ of $PX^u-Q$ and $G$ existed. Under an embedding in an algebraic closure of $\mathbb Q_N$, the binomial has all its roots in a finite unramified extension $K_0$ of $\mathbb Q_N$. In fact its reduction splits into distinct nonzero roots in a finite residue extension, since $N\nmid uPQ$. Lift that finite residue extension to its unramified extension, then lift the roots by Hensel's lemma. In this field $N$ is still a uniformizer. The monic polynomial $\Phi_N(X+1)=((X+1)^N-1)/X$ is Eisenstein at $N$ over its valuation ring. Thus the only relation of degree at most $N-1$ on a primitive $N$th root over $K_0$ is a scalar multiple of $\Phi_N(X)$. For every $b\ne0\bmod N$, $V(\zeta^b)$ cannot belong to $K_0$, since reducing its exponents modulo $N$ and subtracting that putative constant would force all nonzero-index coefficients equal. But $G(x)=0$ places a conjugate of $\alpha$ at $-E(x)/B\in K_0$. This contradiction proves the resultant is nonzero. The standard local-field inputs here are unramified lifting, Hensel's lemma and Eisenstein's criterion. [Sutherland, *Number Theory I*, lectures 9–11](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/pages/lecture-notes/) · [Sutherland, binomial unramifiedness and the translated cyclotomic polynomial, pp. 2–3](https://math.mit.edu/classes/18.785/2015fa/LectureNotes19.pdf)

Applying the same Bézout and root-modulus bounds to $PX^u-Q$ and $G$ gives (5). For instance fixed $r,m$ and $H=o(N)$ give $\log_2 d/(NL)\to1$ uniformly. No individual restriction on the carries inside a replaced interval appears in this proof. Formula (5) also applies to an arbitrary choice of labels on cosets of a subgroup of bounded index so long as their carries are not constant away from zero. The slot at zero is arbitrary.

## Reflection with unboundedly many templates

Without damage the simpler norm bound applies. If $\Delta_A=\max A_i-\min A_i$, then

$$
 g\mid |M_\alpha(0)|,\qquad
 0<|M_\alpha(0)|\le\left(\frac{N\Delta_A}{2\sqrt{N-1}}\right)^m.       \tag{6}
$$

The divisibility follows from $V(t)=0\bmod g$ and $M_\alpha(V(t))=0$. Here $\alpha\ne0$ by the nonconstant hypothesis. For the upper bound, discrete Parseval gives

$$
 \sum_{b=1}^{N-1}|V(\zeta^b)|^2
 =N\sum_i(A_i-\bar A)^2\le N^2\Delta_A^2/4 .
$$

The variance inequality follows by bounding squared distances to the midpoint of the interval of carries, since the mean minimizes their sum. Each conjugate occurs $(N-1)/m$ times, so the arithmetic–geometric mean bound on the product of their squared moduli gives (6).

If $A_i=A_{-i}$ for all $i$, then $m\le(N-1)/2$ regardless of how many different blocks occur. The carry of any length-$L$, weight-$p$ physical block is at most $2^{L-p}(3^p-2^p)$, by moving its odd positions to the last $p$ sites in their positive sum. Since $3^p<Q$, this is less than $Q^{2-\log_3 2}$. Therefore for all undamaged nonconstant-off-zero reflection-symmetric schedules with $N\to\infty$ and $\log N=o(L)$,

$$
 \liminf\frac{\log_2d}{NL}\ \ge\ \tfrac12\log_3 2\ >\ 0.315 .
$$

More generally (6) gives a finite test using the actual carry spread and multiplier index, without requiring reflection. When the reference has full degree $m=N-1$, its conjugates can have too large a product to force a numerical denominator. The geometric-sum reduction still requires the prime repeated clocks and does not cover arbitrary ordinary cycles. The cyclotomic and asymptotic arguments in this file are written proofs. The modular-resultant lemma used by (5) is checked in [PaleyResultant.lean](PaleyResultant.lean).
