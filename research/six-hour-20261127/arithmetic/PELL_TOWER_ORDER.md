# A uniform order gap across the whole Pell division tower

**PROPOSED written theorem.** This tests fixed rational functions of the Pell radicals introduced in PR192. It uses the divisor of a function over a generic rational parameter. A numerical unit at one specialization need not arise from such a function.

For \(x>0\) put \(E=(\sqrt{3x+1}+\sqrt{3x})^2\), and \(t_d=E^{1/d}+E^{-1/d}\) for \(d\ge1\). Let \(P_d\) be the monic Dickson polynomial, determined by \(P_0=2,\ P_1=T,\ P_{d+1}=TP_d-P_{d-1}\). Its identities are
\[
 P_d(z+z^{-1})=z^d+z^{-d},\qquad P_d(t_d)=12x+2,\qquad
 P_{D/d}(t_D)=t_d\quad(d\mid D).
\]
Every rational expression in finitely many division levels is therefore a rational function on a single sufficiently high level. The set
\[
 B_d=\{u_j=2\cos(j\pi/d):0\le j\le d\}
\]
is exactly the finite support of \(P_d(T)^2-4\). These points lie above \(x=0\) or \(3x+1=0\). Passing to a common multiple of levels preserves this support condition.

**Theorem B.** Let \(R\in\overline{\mathbb Q}(T)^\times\) satisfy \(R(\infty)=1\) with all its finite zeros and poles in \(B_d\). Either
\[
 R(t_d)=\left(\frac{3x+1}{3x}\right)^n,\quad n\in\mathbb Z,
 \tag{1}
\]
as a rational function, or
\[
 \log R(t_d)=c\,x^{-2/q}+o(x^{-2/q}),\quad c\in\mathbb R\setminus\{0\},
 \qquad q\mid 2d,\quad q\ge3. \tag{2}
\]
In particular a fixed function anywhere in the directed union of these covers which satisfies \(R(t_d)=1+o(x^{-2/3})\) must be the ordinary rational correction (1). The threshold is sharp, even among cubic field elements of norm one.

### Proof

Write \(e_j=\operatorname{ord}_{u_j}R\). These are rational integers for any algebraic coefficient field. The normalization gives \(\sum e_j=0\) and \(R(T)=\prod_{j=0}^d(T-u_j)^{e_j}\). Every \(t_d>2\), so \(R(t_d)>0\) and its real logarithm is defined. Set \(\zeta=\exp(\pi i/d)\), \(v=E^{-1/d}\). Factoring \(t_d-u_j=v^{-1}(1-\zeta^j v)(1-\zeta^{-j} v)\) gives the exact absolutely convergent expansion
\[
 \log R(t_d)=-\sum_{k\ge1} S_k v^k/k,\qquad
 S_k=\sum_{j=0}^d e_j(\zeta^{jk}+\zeta^{-jk}). \tag{3}
\]
There can be a nontrivial expression with this sum identically zero only if all \(e_j=0\). More precisely, for \(k=0,\ldots,d\) the rows \(P_k(u_j)\) form an invertible matrix. The \(u_j\) are distinct, \(P_0\) is a nonzero constant, and \(P_1,\ldots,P_d\) are monic of distinct degrees. Thus the first nonzero \(S_k\) occurs at some \(1\le k\le d\) unless \(R=1\).

Put \(N=2d\). If \(a\) is a unit modulo \(N\), the cyclotomic automorphism \(\zeta\mapsto\zeta^a\) takes the *number* \(S_k\) to \(S_{ak}\), because it fixes every integer \(e_j\). The function itself and its divisor need not be invariant. The units modulo \(N\) act transitively on indices of fixed gcd with \(N\). Indeed after dividing out the gcd this is transitivity on units modulo a divisor of \(N\), whose units lift to units modulo \(N\) by the Chinese remainder theorem. The smallest positive index in that orbit is \(g=\gcd(k,N)\). For the first nonzero \(S_k\), this forces \(k=g\). Thus \(k\mid2d\).

If \(k<d\), write \(q=2d/k>2\). As \(E=12x+O(1)\), (3) gives (2). If \(k=d\), the equations \(S_0=\cdots=S_{d-1}=0\) leave a one-dimensional vector space for \((e_j)\), by the same polynomial evaluation rank. The rational function
\[
 Q(T)=(P_d(T)+2)/(P_d(T)-2)
\]
has exactly this order at infinity since \(P_d\) is monic of degree \(d\). Its divisor spans that space. The order of \(Q\) at \(u_0=2\) is \(-1\), because \(P'_d(2)=d^2\). This last identity follows from the Dickson recurrence and \(P_j(2)=2\), or by differentiation of the parameter \(2\cos\theta\) at \(\theta=0\). Since \(e_0\in\mathbb Z\), the multiple is an integer. Normalization at infinity gives \(R=Q^n\), and substituting \(P_d(t_d)=12x+2\) proves (1).

On the cubic level \(R(T)=(T^2-4)/(T^2-1)\) is supported on \(\{-2,-1,1,2\}\), and \(R(t_3)=1-3/(t_3^2-1)\) has exact order \(x^{-2/3}\). Evaluating the cubic \(P_3(T)-(12x+2)\) at \(\pm2,\pm1\) gives \(\operatorname{Norm}(t_3^2-4)=\operatorname{Norm}(t_3^2-1)=48x(3x+1)\). Thus its norm is one whenever \(x\) is an ordinary post-initial odd state, by irreducibility at three. At \(d=5\) the possible first indices are \(1,2,5\), although the six support values allow arbitrary independent integer multiplicities subject to their sum vanishing. A possible cancellation at indices one and two already forces the remaining pre-fifth moments to vanish. Choosing unequal multiplicities at conjugate support points does not evade this.

### All-time significance and limitation

The only faster normalized rule with this divisor support on any fixed level is the rational correction whose product on an ordinary interval is \(2^H x_m/(3^m x_0)\). Thus climbing division levels or using coefficients in a larger cyclotomic field cannot supply an independent, faster-decaying correction while retaining this support. The result allows arbitrary finite levels in the rule. It supplies no uniform numerical lower bound for functions or levels newly chosen at each state, and imposes no condition on the rate at which a hypothetical escaping orbit visits high integers. The inequality in (2) alone does not decide convergence or divergence of a series along such a source. Rational rules with other zeros or poles and state-dependent algebraic elements remain possible.

The source of the edge units and \(d=3\) trace is PR192, head ed7a6fe30b8602407f77855ceb74ce0489ce9c10, [PELL.md, P1](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/adelic/PELL.md) and [CUBIC_FIELDS.md, C1 and C5](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/adelic/CUBIC_FIELDS.md).

