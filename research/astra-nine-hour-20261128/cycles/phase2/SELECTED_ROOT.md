# Two limits on cancellation at the selected congruence root

**Proposed written results.** The moving-polynomial estimate below is elementary. The separate nonzero-norm statement imports Ljunggren’s irreducibility theorem. For coprime $n,u$ put $D=|2^n-3^u|$. Let $z_0\in\mathbb Z/D$ be the [selected root](SEMIGROUP_BOUNDARY.md) with $z_0^u=2$ and $z_0^n=3$. The following tests use that *same* root at each prime power.

## A nonzero trinomial norm for every admissible boundary

Write $f=z^n-z^u-1$. Let $f_*$ denote the irreducible factor containing its positive real root $\rho>1$. By Ljunggren's Theorem 3 on trinomials, $f$ has only one noncyclotomic irreducible factor, with multiplicity one. His convention $n\ge2m$ is satisfied directly when $n\ge2u$, and otherwise by taking the reciprocal up to sign, $z^n+z^{n-u}-1$. In the reducible case his theorem on pp. 69–70 expressly leaves an irreducible second factor. Since $z^n-z^u$ increases from zero to infinity on $[1,\infty)$, that factor is $f_*$. A root of unity $\zeta$ on $f$ must have $\zeta^u$ primitive of order 3 and $\zeta^n=1+\zeta^u$ primitive of order 6, by the equilateral triangle identity on the complex unit circle. Since $\gcd(n,u)=1$, the order of $\zeta$ is 6. A unit-circle zero is simple by $|n\zeta^{n-1}|=n>u=|u\zeta^{u-1}|$. Thus $f=f_*$ or $f=\Phi_6 f_*$. [Ljunggren, Theorem 3, Math. Scand. 8 (1960), pp. 69–70, publisher PDF](https://journals.msp.org/mscand/article/download/2753/2752/2784) · [Boyd–Martin–Thom, Lemma 4.1(a)(iii), explicit coprime residue classes](https://doi.org/10.1112/S1461157014000436)

For every semimodule boundary $J=1-(1-z)G$ we have $J(\rho)=1+(\rho-1)G(\rho)>0$. Consequently
$$                       R_* = |\operatorname{Res}(f_*,J)|>0.$$
Let $m=\gcd(D,C)$, the full cancellation for this word. If there is a cyclotomic factor, any divisor $a$ of $m$ annihilating $\Phi_6(z_0)$ also annihilates $z_0^6-1$. Therefore $a$ divides $\gcd(2^6-1,3^6-1)=7$. Since $f(z_0)=0\bmod m$, the elementary integer identity $m\mid AB\Rightarrow m/\gcd(m,A)\mid B$ gives $f_*(z_0)=0\bmod m/\gcd(m,7)$. In the irreducible case $f_*(z_0)=0\bmod m$ directly. Since $J(z_0)=0\bmod m$ in both cases, the integer Bezout identity for the resultant gives
$$\frac{m}{\gcd(m,7)}\mid R_*;\qquad m\mid R_*\quad\text{if }f=f_*.$$
This permits the loss of at most one power of seven, even when $49\mid m$. For the zero-norm control $n=13,u=8$, word $1111111010000$, the full resultant is zero whereas $R_*=72{,}283$. A nonzero integer can still be much larger than $D$.

## Every moving polynomial has a short-binomial test

Let $P\in\mathbb Z[z]$ be nonzero of degree $d>0$, with multiplicative Mahler measure $M(P)=|a_d|\prod_{P(\alpha)=0}\max(1,|\alpha|)$, roots counted with multiplicity. For any integer $1\le K<n$ there are integers $1\le k\le K$, $-k\le l\le0$, $\gcd(k,l)=1$, with
$$0<|s|=|ku+ln|\le n/(K+1).$$
Indeed among the $K+1$ residues $ju\bmod n$, $0\le j\le K$, the least circular gap is at most $n/(K+1)$. Take the difference of the corresponding indices, change its sign if necessary so $k>0$, and divide both coefficients by their gcd. Coprimality of $n,u$ and $k<n$ exclude zero. The bounds on $l$ follow from $0<ku<kn$ and $|s|<n$.

Write the positive rational $(2^k3^l)^{\operatorname{sgn}(s)}=A/B$ in lowest terms and put $Q(z)=Bz^{|s|}-A$. Its coefficients satisfy $1\le A,B\le3^K$, and $Q(z_0)=0$ throughout the *full* physical modulus. This primitive binomial is irreducible over $\mathbb Q$. All its complex roots have absolute value $(A/B)^{1/|s|}$. The absolute constant term of a monic rational factor of degree $e$ equals $(A/B)^{e/|s|}$. Rationality forces $|s|\mid ek$ and $|s|\mid el$ by the valuations at two and three. Since $\gcd(k,l)=1$, it forces $|s|\mid e$.

Thus precisely the following useful dichotomy holds for the selected $Q$:

* If $Q\mid P$, the entire modulus annihilates $P(z_0)$. This is an exact clock relation already valid before a Collatz word has been chosen.
* Otherwise $\operatorname{Res}(P,Q)$ is a nonzero integer divisible by $m=\gcd(D,P(z_0))$. Its complex product formula gives
$$\log m\le |s|\log M(P)+d\log(A+B)
\le \frac{n\log M(P)}{K+1}+d(K\log3+\log2).                     \tag{1}$$
Indeed $|B\alpha^{|s|}-A|\le(A+B)\max(1,|\alpha|)^{|s|}$ at each root, and the leading-coefficient power is included in $M(P)$. Divisibility uses the resultant Bezout identity evaluated at the *same* root modulo $m$, so it applies to all prime-power multiplicities.

Set $H=1+\log M(P)$. Whenever $dH=o(n)$ along a sequence of such inputs, choose $K=\lfloor\sqrt{nH/d}\rfloor$. Eventually $1\le K<n$. Outside the displayed exact binomial case, (1) gives
$$                 \log\gcd(D,P(z_0))=O(\sqrt{ndH}+d)=o(n).          \tag{2}$$
Neither the degree nor the coefficients are required to be fixed. A constant polynomial is handled directly by its absolute value.

**A universal per-word estimate.** Every actual normalized boundary $J$ avoids the exceptional case for *every* $K$. It has no positive real root: for $0<x<1$, $J(x)=(1-x)\sum_{s\in S}x^s>0$; at 1 it equals 1; above 1 it equals $1+(x-1)G(x)>0$. In contrast $Q$ has a positive real root. Consequently the *full* reduced cycle denominator satisfies
$$\log d_{\rm red}\ge \log D-\frac{n\log M(J)}{K+1}
              -(\deg J)(K\log3+\log2)\qquad (1\le K<n).            \tag{3}$$
This holds at every coprime type of either sign; if $J=1$, the denominator equals $D$. For $N_{\rm c}$ nonzero boundary terms, Jensen's inequality and Parseval on the circle give $M(J)\le\sqrt{N_{\rm c}}$. In particular, at critical positive clocks the exact denominator is $2^{n-o(n)}$ when $(\deg J)(1+\log N_{\rm c})=o(n)$. Here $\log D=n\log2-O(\log n)$ by the explicit two-logarithm lower bound already sourced in the [contracting-calendar note](../CONTRACTING_CALENDARS.md). The conductor $\deg J$ can be quadratic in $n$ and (3) need not be nontrivial for that word.

**Fixed polynomials, without a Subspace Theorem.** For *every* fixed nonzero $P$, if $n\to\infty$ and $u/n$ tends to an irrational number in $(0,1)$, then
$$                       \log\gcd(D,P(z_0))=O_P(\sqrt n).            \tag{4}$$
In fact if $Q\mid P$ then $|ku+ln|\le d$, and $2^k,3^{-l}\le M(Q)\le M(P)$: the primitive $Q$ divides $P$ over the integers and every nonzero integer quotient has Mahler measure at least one. Only finitely many $(k,l)$ are therefore possible. For each one $|ku+ln|\to\infty$ by the irrational limit, contradicting bounded degree. Now employ $K=\lfloor\sqrt n\rfloor$ in (1). This also covers polynomials with zeros at zero or roots of unity. Previously known sparse-block gcd theorems use different hypotheses and can require a multivariable Subspace Theorem. [Paper 22 v2](https://rstation.ai/problems/collatz/papers/22/v2)

With variable degrees and coefficients one can also exclude the exact binomial case without a sign hypothesis at sufficiently small effective heights. At critical clocks $0<\delta=n\log_3 2-u\le1$, that exceptional case forces $k\le H/\log2$ and $|s|\le d$, hence
$$|k\log_3 2+l|=|s+k\delta|/n\le(d+k\delta)/n.$$
Lagarias's lower bound gives $n\ll H^{13.3}(d+H\delta)$. For bounded degree, $H=o(n^{1/14.3})$ therefore rules out that alternative uniformly. This particular last refinement uses the external irrationality estimate; (1)–(4) do not use it to bound the gcd.

**The binomial exception really can absorb the whole determinant.** Even at critical positive clocks with $\delta\to0$, an unrestricted moving-polynomial claim with bounded degree and $H=o(n)$ is false. Take lower convergents $j/k<p=\log_3 2$ and $\epsilon=kp-j\in(0,1/k)$. Choose $n$ in the residue class $jn\equiv-1\bmod k$ just above $1/\epsilon+k^{3/2}$, with extra overshoot at most $k$. Put $u=(jn+1)/k$. Then $ku-jn=1$, so $n,u$ are coprime and $k=o(n)$. We have $0<np-u=(n\epsilon-1)/k=O(k^{-1/2})$. The genuine linear polynomial $3^jz-2^k$ has $H=O(k)=o(n)$ yet vanishes modulo all of $D$, since $z_0=2^k3^{-j}$. It has a positive real root, as required by the exceptional alternative. These clocks need not be lower records.

## Direct optimization of chronological lifts fails

At the lower record $(n,u)=(5,3)$, the word $00111$ has $S=\mathbb N\setminus\{1\}$, $J=1-z+z^2$, and $D=5$. For the positive sums in the [clock-window proof](BOUNDARY_FAMILIES.md), choosing clock lifts in each of the five cyclic intervals gives the cleared numerators $13,11,11,7,7$, respectively. All are already coprime to six. Translating all clocks by another entire lap multiplies all three rational summands by the same unit and does not change these primitive numerators. Thus even the best of the chronological-window lifts can exceed $D$. This does not preclude a different multiplier, a non-window choice of individual lifts, or an independent bound on the gcd.
