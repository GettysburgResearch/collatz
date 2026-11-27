# A full-denominator estimate uniform in the raised rank

**PROPOSED written theorem.** Fix $C_0$. For all sufficiently large coprime positive $h,p$ with $0<h-p\log_2 3\le C_0/p$, set $D=2^h-3^p$ and take $u\bmod D$ with $u^p=2,\ u^h=3$. Uniformly for every $1\le s\le p-2$, put
$$
  Q_s(X)=2\sum_{i=0}^{p-1}X^i-X^s,\qquad
  g_s=\gcd(D,Q_s(u)).
$$
Then $\log g_s=O_{C_0}(p^{5/6})$. Thus the complete reduced denominator is $D/\exp(O_{C_0}(p^{5/6}))$ in the actual legal single-raised-rank words derived in the [cycle note](CYCLE_CLOSURE.md). No position of the moved letter is frozen as $p$ grows. Each of these polynomials is irreducible, undilated and of degree $p-1$. The proof specifically uses its one-term deviation from a constant rank polynomial.

## Two independent short relations

All implied constants below are independent of $s$. Consider the integer lattice
$$
  \mathcal L=\{(j,e)\in\mathbb Z^2:jh+e=0\bmod p\}.
$$
Let $\mu$ be the smallest sup norm of a nonzero lattice vector $(j,e)$. The box proof of Dirichlet approximation, or a pigeonhole argument on a square of side $\lceil\sqrt p\rceil$, gives $1\le\mu\ll\sqrt p$. Put $i=-(jh+e)/p$. Then $|i|\ll\mu$ since $h/p$ is bounded. For all sufficiently large $p$, neither $j$ nor $e$ is zero: either vanishing implies the other is a multiple of $p$ by coprimality.

We need another relation
$$
                  ap+bh+ks+t=0,\qquad k\ne0                        \tag{1}
$$
with all four coefficients $O(R)$ for
$$
             R=\left\lceil 20\max(p^{1/3},\sqrt{p/\mu})\right\rceil .
$$
To verify it, map the triples $(b,k,t)\in[0,R]^3\cap\mathbb Z^3$ to $bh+ks+t\bmod p$. If two triples with different $k$ map together, their difference gives (1), including $|a|=O(R)$ because $1\le s\le p$ and $h=O(p)$. Otherwise all triples in each fiber have the same $k$. Their differences in $(b,t)$ lie in $\mathcal L$ and have norm at most $R$. For every such difference $(b',t')$, its determinant with $(j,e)$ is divisible by $p$, since both first coordinates times $h$ plus their second coordinates vanish modulo $p$. Its absolute value is at most $2\mu R<p$ for large $p$, by $\mu\ll\sqrt p$. Hence every difference is collinear with $(j,e)$. Along that line, any two distinct lattice points have sup-norm distance at least $\mu$ by minimality. Project on the coordinate of larger absolute direction to see that a fiber has at most $1+R/\mu$ elements. But
$$
             (R+1)^3>p(1+R/\mu)
$$
by the chosen constant and the two defining lower bounds for $R$. This is a contradiction. Finally
$$
        \mu R \ll \mu p^{1/3}+\sqrt{p\mu}+\mu=O(p^{5/6}).          \tag{2}
$$

## A fixed exceptional set over the complex numbers

If $g_s=1$ there is nothing to prove. Modulo $g_s$, multiplying the rank relation by $u-1$ yields
$$
                         (u-1)u^s=2.
$$
Both $u$ and $u-1$ are therefore units at this modulus. The two short relations give
$$
       2^i3^j u^e=1,\qquad
       2^{a+k}3^b u^t(u-1)^{-k}=1 \pmod {g_s}.                    \tag{3}
$$
Clear positive and negative exponents in each by putting the positive and negative parts on opposite sides. The resulting two polynomials $P(X),V(X)\in\mathbb Z[X]$ have degrees $O(\mu),O(R)$ and coefficient absolute sums $\exp(O(\mu)),\exp(O(R))$, respectively. For $V$, expanding a power of $X-1$ costs at most $2^{|k|}$ in coefficient sum. The first polynomial is a nonconstant binomial with nonzero constant; it has neither 0 nor 1 as a root. For 1, use $j\ne0$ and multiplicative independence of 2 and 3. The second polynomial is not identically zero, since the two rational functions in (3) differ in their order at $X=1$ when $k\ne0$. Thus clearing did not introduce any candidate common roots at 0 or 1.

Define $\Gamma$ to be the subgroup of $\overline{\mathbb Q}^{\,*}$ consisting of all $\alpha$ such that $\alpha^m\in\langle2,3\rangle$ for some $m\ge1$. Its rank is two in the precise sense of Evertse, Schlickewei and Schmidt: modulo the rank-two subgroup $\langle2,3\rangle$ it is torsion. This includes all roots of unity, and does not assume that $\Gamma$ itself is finitely generated. Their Theorem 1.1, over the algebraically closed field $\overline{\mathbb Q}$, gives only finitely many solutions to $X+Y=1$ in $\Gamma^2$, a group of rank four. In dimension two every such solution is nondegenerate, since each coordinate is nonzero. Thus the following set is finite, independently of all clocks and ranks:
$$
             \mathcal E=\{\alpha\in\Gamma:1-\alpha\in\Gamma\}.
$$
[Evertse, Schlickewei and Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics 155 (2002), pp. 807–808, rank definition and Theorem 1.1](https://arxiv.org/pdf/math/0409604)

If a complex number $\alpha$ were a common root, $e\ne0$ and the first equation give $\alpha\in\Gamma$. In the second, $k\ne0$ then implies $\alpha-1\in\Gamma$, hence $1-\alpha\in\Gamma$ as $-1$ is torsion. Consequently $\alpha\in\mathcal E$. On the other hand every root of the first binomial satisfies
$$
      \log|\alpha|
       =-\frac{i\log2+j\log3}{e}
       =\frac{\log2}{p}
          +\frac{j}{e}\left(\frac hp\log2-\log3\right).
$$
The second term is $O_{C_0}(p^{-3/2})$ uniformly, since $|j|\ll\sqrt p,\ |e|\ge1$. Thus all root moduli tend to one and are **strictly larger than one** for large $p$. Even without this last asymptotic sign, equality of the modulus to one would imply $2^i3^j=1$ with $j\ne0$. Among the finitely many members of $\mathcal E$ with modulus not equal to one, the distance of their moduli to one has a positive minimum if any exist. The members on the unit circle cannot be roots of the binomial either. This proves that there is no common complex root for all sufficiently large $p$ uniformly in $s$. The use of a finite exceptional set establishes existence of an onset and does not compute it.

Consequently $g_s$ divides the nonzero integer $\operatorname{Res}(P,V)$; this follows by evaluating the integral resultant identity at the common modular root, even at prime powers. The bound
$$
 |\operatorname{Res}(P,V)|\le M(P)^{\deg V}\|V\|_1^{\deg P}
        \le \exp(O(\mu R))
$$
and (2) finish the proof. [PR195, earlier short-relation bound for irreducible factors](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/cycle/README.md)

With many independently placed raised ranks, $(u-1)Q(u)$ no longer gives $u^s=2/(u-1)$. Hence the second short relation cannot be turned into this one-variable polynomial, and the same two-coordinate unit equation no longer follows. A proof for unrestricted high-degree rank masks is still missing.
