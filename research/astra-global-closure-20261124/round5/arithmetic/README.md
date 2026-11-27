# The complete denominator when discrepancy exponents form a generalized arithmetic progression

**PROPOSED written theorem.** Let a physical gap word have $p$ odd steps and total division exponent $A$, with $\gcd(A,p)=1$ and $p<A\le Bp$ for fixed $B$. If its normalized discrepancy exponents form any proper generalized arithmetic progression, its **entire reduced denominator** satisfies
\[
             \log d=\log|2^A-3^p|-o_B(p),\qquad p\longrightarrow\infty.       \tag{1}
\]
The rank, digit sizes, steps and ordering of the progression can all vary. This covers quadratic discrepancy spans and families for which no common annihilating order is polynomial in $p$. The proof charges every digit to a bound derived from the physical division exponents. A [second theorem](UNIT_RELATIONS.md) treats moving algebraic units and arbitrary common divisors of the two clocks. Neither argument forces the stated factorization on a general cycle.

## The physical set of exponents

Use $2^{e_i}x_{i+1}=3x_i+1$ with $e_i\ge1$, $E_i=\sum_{j<i}e_j$, $E_p=A$. The word has carry $C=\sum_{i<p}3^{p-1-i}2^{E_i}$, clock difference $D=2^A-3^p$, periodic fixed point $C/D$, and reduced positive denominator $d=|D|/\gcd(|D|,C)$. A positive ordinary cycle requires $D>0,d=1$. Such a cycle has $A\le2p$ since $3x_i+1\le4x_i$.

Set $a=A-p>0$, $s_i=pE_i-Ai$, $t_i=s_i-\min_j s_j$, $S=\{t_i:0\le i<p\}$ and $M(X)=\sum_{t\in S}X^t$. These exponents are distinct modulo $p$, and $0\in S$. The periodic extension of $t_i$ satisfies
\[
                       t_{i+1}+a=t_i+p(e_i-1).                                \tag{2}
\]
Thus $\Delta=S+p\mathbb N_0$ is closed under addition by $p$ and $a$. Each member of $S$ is the least element of $\Delta$ in its residue class. In the language of two-generated numerical semigroups, $\Delta$ is a normalized semimodule over $\langle p,a\rangle$, and $S$ is its Apéry set relative to $p$. Conversely any such $\Delta$ with $0\in\Delta\subset\mathbb N_0$ gives a legal gap word. Choose its least representatives $t_i\equiv-ai\bmod p$, with $t_0=t_p=0$. Closure gives $t_{i+1}+a\ge t_i$, so $e_i=1+(t_{i+1}+a-t_i)/p\ge1$ and $\sum e_i=A$. This chooses the rotation at exponent zero. The semimodule terminology is classical. [Moyano-Fernández and Uliczka, §§2–3](https://arxiv.org/abs/1209.4797)

For every $0\le j<p$, the $j+1$ numbers $0,a,\ldots,ja$ belong to $\Delta$ and occupy different classes modulo $p$. Their least representatives are distinct and at most $aj$. If $s_{(j)}$ is the zero-based $j$th smallest exponent, this proves
\[
                             s_{(j)}\le a j .                                  \tag{3}
\]
In particular $\deg M\le a(p-1)$. Tiling $S+p\mathbb Z=\mathbb Z$ alone gives no bound on these representatives. Equation (2) supplies the second closure.

For $|D|>1$, choose integers $u,v$ with $up+vA=1$. In the unit group of $\mathbb Z/|D|\mathbb Z$, let $z=2^u3^v$. Then $z^p=2,z^A=3$. If $K=-\min s_i$,
\[
                        3^{p-1}M(z)=z^K C\pmod {|D|}.                          \tag{4}
\]
Thus $d=|D|/\gcd(|D|,M(z))$ for every integer lift of $z$. The geometric factor $1+\cdots+X^{p-1}$ divides $M$, since its residues are complete. Its value is a unit because $(z-1)(1+\cdots+z^{p-1})=z^p-1=1$. This is PR193's full-modulus identity. The cases $|D|=1$ are immediate. [PR193, 5f160a843750f209ea1251dfb01ea0b23e532fd6, §1](https://github.com/GettysburgResearch/collatz/blob/5f160a843750f209ea1251dfb01ea0b23e532fd6/research/astra-ordinary-boundary-20261124/arithmetic/README.md)

## Joint cancellation at moving orders

For any $m\ge1$ and $P\mid X^m-1$ in $\mathbb Z[X]$, put $G=\gcd(|D|,P(z))$. Then $z^m=1\bmod G$ and both 2 and 3 are powers of $z\bmod G$. For $G>1$ these facts in the complete composite ring give
\[
           |\langle2,3\rangle\bmod G|\le\operatorname{ord}_G(z)\le m.         \tag{5}
\]
Varjú's Corollary 3 gives $|\langle2,3\rangle\bmod G|/(\log G)^2\to\infty$ as $G\to\infty$ through every integer coprime to six. Consequently there is a nonnegative $f(m)=o(\sqrt m)$, independent of the word and clocks, such that $\log G\le f(m)$. Indeed for any $\epsilon>0$, sufficiently large $G$ have $\log G\le\epsilon\sqrt m$, and the remaining finite set adds a fixed bound. Also $G\mid 2^m-1$ directly. Varjú credits earlier work of Hernández–Luca and Corvaja–Zannier for the order result. [Varjú, Corollary 3, arXiv:2104.04367v2](https://arxiv.org/pdf/2104.04367v2) · [Corvaja–Zannier, Proposition 2, arXiv:math/0311030v2](https://arxiv.org/pdf/math/0311030v2)

In particular every cyclotomic factor $\Phi_m\mid M$, anywhere in any such physical word, contributes only $\exp(o_B(p))$ to the gcd when counted once. Indeed $m\le2\deg M$, since otherwise all terms of $M(e^{2\pi i/m})$ lie in an open semicircle and cannot sum to zero. This includes factors of quadratic order. One occurrence leaves open contributions from large multiplicities or many different orders.

More generally, take any collection of integer polynomials $P_j\mid X^{m_j}-1$, allowing repetitions, such that $\sum_j\sqrt{m_j}\le K_0p$ for fixed $K_0$. Then
\[
             \log\gcd\left(|D|,\prod_jP_j(z)\right)=o_{B,K_0}(p).             \tag{6}
\]
For $m_j>M_0$ sum (5), using $\gcd(n,bc)\le\gcd(n,b)\gcd(n,c)$. For $m_j\le M_0$ all bad rational primes divide the fixed integer $\prod_{m\le M_0}(2^m-1)$. Their entire contribution, all multiplicities combined, is bounded by the part of $D$ supported on this set. For every fixed finite set of primes prime to six that part has logarithm $o_B(p)$. Apply the one-variable $S$-unit estimate from Ridout stated in the proof of Corvaja–Zannier's Proposition 2 to $2^A/3^p$, with these primes, $2,3,\infty$ in $S$. Their valuations in $2^A/3^p-1$ equal those in $D$, and $h(2^A/3^p)=O_B(p)$. Unique factorization accounts for the finitely many exceptional inputs. Let $p\to\infty$ at fixed $M_0$, then $M_0\to\infty$. The same estimate at infinity, or Lagarias's explicit two-log lower bound, gives $\log|D|=\max(A\log 2,p\log3)-o_B(p)$. [Corvaja–Zannier, p. 7](https://arxiv.org/pdf/math/0311030v2) · [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

This also controls the entire cyclotomic part of any subproduct of $M$ of degree $O(p)$. Indeed $\sqrt m/\varphi(m)\to0$. For every $\eta>0$ the standard bound $m/\varphi(m)\ll_\eta m^\eta$ follows by bounding $q/(q-1)\le q^\eta$ off a fixed finite set of primes. Thus the sum of $\sqrt m$ with multiplicity over these factors is $O(p)$, and (6) applies. In particular bounded span of $E_i-Ai/p$ implies subexponential cancellation from the whole cyclotomic part, whatever the multiplicities. Noncyclotomic factors may remain.

## The whole progression

A proper generalized arithmetic progression here means any representation
\[
 S=\left\{\sum_{i=1}^h j_iw_i:0\le j_i<b_i\right\},
 \qquad b_i\ge2,\quad w_i\in\mathbb Z_{>0},
\]
with all digit sums distinct. Sorting the steps imposes no restriction. Reversing negative steps and translating the minimum to zero yields this form. Put $B_0=1$, $B_i=\prod_{k\le i}b_k$, so $B_h=p$. At most $B_{i-1}$ exponents can be **strictly** below $w_i$, since every digit from level $i$ onward must vanish there. As $B_{i-1}<p$, (3) gives
\[
                    w_i\le aB_{i-1},\qquad m_i=b_iw_i\le aB_i.               \tag{7}
\]
Every factor $P_i=1+X^{w_i}+\cdots+X^{(b_i-1)w_i}$ divides $X^{m_i}-1$, and properness gives $M=\prod_iP_i$ literally. Since $B_i\le p/2^{h-i}$,
\[
                     \sum_i\sqrt{m_i}\le\frac{\sqrt{ap}}{1-2^{-1/2}}=O_B(p).
\]
Now (6) and (4) prove (1). For this application the small-order step even avoids Ridout: there are at most $\log_2 p$ digits. For $m_i\le M_0$ the full gcd of each digit divides $2^{m_i}-1$, giving total loss $O_{M_0}(\log p)$. For $m_i>M_0$ the total is at most $O_B(p)\sup_{m>M_0} f(m)/\sqrt m$. This also verifies the quantifiers when the number of repeated small orders grows. On the contracting side the conclusion rules out integer cycles of this type for all sufficiently large $p$, with an ineffective threshold.

## Range and obstruction

*Quadratic span.* For every coprime pair take $S=\{0,a,\ldots,(p-1)a\}$, the Apéry set of $\langle p,a\rangle$. For near-critical $A/p\to\log_2 3$ this has span $\asymp p^2$. Its order $ap$ is quadratic, where the earlier estimate for $X^{Lp}-1$ with $L=o(p)$ does not give a subexponential loss.

*Unboundedly many orders with no common order of polynomial size.* Let $p=2^j$ and let $c_i$ be the successive odd primes for $0\le i<\lfloor j/3\rfloor$, with $c_i=1$ for remaining $i<j$. Set $w_i=2^ic_i$ and take binary digits. The lowest differing dyadic valuation makes the subset sums a transversal modulo $p$. Their maximum is $p-1+O(j^2 2^{j/3})=p+o(p)$, since the prime number theorem gives $c_i=O(j^2)$. Choose $A$ the least odd integer above $p\log_2 3$. Eventually the maximum is below $A$, so the difference between any two representatives is greater than $-A$ and the corresponding $e_i=(A+t_{i+1}-t_i)/p$ are positive integers. For each changed digit $X^{w_i}+1$ has a root of exact order $2^{i+1}c_i$. A common order contains $\prod_{i<\lfloor j/3\rfloor}c_i\ge\lfloor j/3\rfloor!$, larger than every fixed power of $p$. Equation (7) does not require the dyadic alignment of this example.

*Tiling and cyclotomicity do not imply a progression.* For each prime $p\ge5$, the mask $M=(1+\cdots+X^{p-1})(1-X+X^2)$ has support $\{0,2,3,\ldots,p-1,p+1\}$. It is a transversal with $\Delta=\mathbb N_0\setminus\{1\}$, closed under every $a\ge2$. Taking $A=p+a$ with $p\nmid a$ gives a legal word by (2). At $p=5,A=8$ the representatives are $(0,2,4,6,3)$ and the gaps are $(2,2,2,1,1)$, with $C=653,D=13,d=13$. Prime cardinality forces any proper generalized arithmetic progression on this set to have a single nontrivial digit. These exponents do not form an arithmetic progression. All roots nevertheless are roots of unity. The example rules out this use of a digit factorization. Its own two factors are controlled by (6), and it gives no counterexample to a general cyclotomic cancellation bound. The Fourier criterion for tiling concerns prescribed roots of unity, whereas (4) specializes at a unit with $z^p=2$. [Łaba and Londner, Lemma 2.2 and the integer tiling criteria](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/combinatorial-and-harmonicanalytic-methods-for-integer-tilings/21F92E36210451C3039EA5CC6D1883E8)

When $M$ consists entirely of cyclotomic factors its constant coefficient is one and $M(1)=p>0$, so every factor is reciprocal, and $S=H-S$ with $H=\max S$. In the index order $t_i\equiv-ai+K\bmod p$, the reflecting partner has index $k-i$ for a constant $k\bmod p$. Thus $t_{k-i}=H-t_i$ and the physical gaps satisfy $e_{k-i-1}=e_i$. This gives a reflection of the actual gap necklace. Reflection alone supplies no bound on a joint order cover in (6). More generally $(1-X)\sum_{n\in\Delta}X^n=M/(1+\cdots+X^{p-1})$. Actual numerical semigroups have a literature on when this polynomial is cyclotomic and on complete-intersection criteria. A general $\Delta$ here is a semimodule, with no axiom making it closed under addition of two members. Those criteria cannot simply be applied. [Ciolan, García-Sánchez and Moree, §1](https://arxiv.org/abs/1409.5614)

For an unrestricted word the uncharged factors may still cancel the whole numerical divisor, including through many unrelated torsion orders, or through irreducibles not covered by the fixed-field estimate. A word-specific upper bound on the cost in (6), or a numerical estimate bypassing factorization, remains open. Periodizing a prefix of one escaping ordinary source yields a different rational orbit and gives no contradiction to that source.

### The ungrouped order bound actually fails on physical words

Even restricting to squarefree, entirely cyclotomic masks does **not** yield $\sum_{m:\Phi_m\mid M}\sqrt m=O(p)$ uniformly. For the genuine Apéry set $\{0,a,\ldots,(p-1)a\}$ above, the quotient $M=(X^{pa}-1)/(X^a-1)$ is squarefree. Since $\gcd(a,p)=1$, every $\Phi_{pd}$ with $d\mid a$ occurs. Therefore
\[
 \frac1{\sqrt{pa}}\sum_{m:\Phi_m\mid M}\sqrt m
      \ \ge\ \sum_{d\mid a}\frac1{\sqrt d}.
\]
Take $a$ divisible by the primorial $V_j=\prod_{q\le j}q$ (prime $q$). The right side is at least $\prod_{q\le j}(1+q^{-1/2})\to\infty$, for instance by divergence of the prime reciprocal sum. For each $j$ take $a=V_j$ and let $p$ be the largest prime below $a/(\log_2 3-1)$. The prime number theorem gives $p\sim a/(\log_2 3-1)$ and $p>j$, so $\gcd(p,a)=1$. The physical slope $A/p=1+a/p$ approaches $\log_2 3$ from above, and $\sqrt{pa}\asymp p$. Thus the raw sum is genuinely superlinear on these contracting clocks. All these factors together divide the **one** polynomial $X^{pa}-1$, so grouping them proves subexponential cancellation. An upper bound for an optimized grouping for every cyclotomic physical mask remains open.

The [moving-unit construction](UNIT_RELATIONS.md) also gives whole denominators for arbitrarily chosen **fixed** outer digit transversals, including a legal family whose non-torsion subproduct has quadratic degree and cannot have any geometric digit factorization.
