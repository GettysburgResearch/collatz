# Positive integer cycles under congruence-preserving changes of the carry

**Written countermodel to a transfer of divisibility arguments.** For every modulus $M$ there is a single bounded positive odd carry function $c(n)\equiv1\bmod M$ on the positive odd integers for which the modified Syracuse map has infinitely many primitive positive integer cycles. Their gaps are the coprime mechanical gaps of lengths $A,p$ with $A\log2-p\log3\to0^+$. For the same words the literal $+1$ orbit has full reduced denominator $2^A-3^p\to\infty$. One can also impose agreement with the original map outside a set of natural density zero. This tests deductions based on congruences or frequency of agreement along the ambient integers. The construction changes literal carries on each exceptional orbit.

Fix $Q=\operatorname{lcm}(6,M)$. Take $L$ a common multiple of the multiplicative orders of 2 and 3 modulo the prime-to-six part $q$ of $Q$, using $L=1$ if $q=1$. Initially let $p=Ln$, $A=L\lfloor n\log_2 3\rfloor+1$. By density of irrational rotations there are infinitely many $n$ with $\{n\log_2 3\}$ approaching $1/L$ from below. Thus $\Lambda=A\log2-p\log3\to0^+$ and $2^A-3^p\equiv1\bmod q$. Divide $A,p$ by their gcd. The new gap $D=2^A-3^p$ divides the original gap by difference of powers, so $\gcd(D,Q)=1$. The new positive $\Lambda$ still tends to zero. The reduced clocks must tend to infinity, since finitely many bounded $p$ yield finitely many $A$ in this near-critical range. Eventually $1<A/p<2$.

Set $s_i=\lfloor iA/p\rfloor$, $g_i=s_{i+1}-s_i\in\{1,2\}$ for $0\le i<p$, with cyclic indices for vertices. For the literal odd-only $+1$ map, its periodic rational orbit solves $2^{g_i}x_{i+1}=3x_i+1$. Its initial value is $C/D$, where $C=\sum_{i=0}^{p-1}3^{p-1-i}2^{s_i}$. Here is an elementary check of the known balanced-word coprimality. For $D>1$, choose integers $u,v$ with $up+vA=1$ and put $z=2^u3^v$ in $(\mathbb Z/D)^\times$. Then $z^p=2$ and $z^A=3$. The residues $Ai-p s_i$ run through $0,\dots,p-1$ exactly once. Thus
$$
 (z^{-1}-1)\, C\,3^{1-p}=z^{-p}-1=-1/2\pmod D .
$$
Consequently $C$ is a unit modulo $D$. The same reduced denominator holds at every phase, since the multipliers $2,3$ are units modulo $D$. The standard cyclic carry formulas show the $x_i$ are odd at every odd-only phase. In particular they have residues modulo $Q$ because $\gcd(D,Q)=1$. Lagarias's two-log bound gives $D\gg2^A A^{-13.3}\to\infty$. [Balanced denominators, Theorem 3](https://rstation.ai/problems/collatz/papers/4) and [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

Put $K=8Q$, $H=K/(2^{A/p}-3)$ and $z_i=H2^{\{iA/p\}}$. Choose a nearest integer $n_i\equiv x_i\bmod Q$ to $z_i$. These integers are odd and lie in $[H-Q/2,2H+Q/2]$. The identity
$$
 2^{g_i}z_{i+1}-3z_i=(2^{A/p}-3)z_i\in[K,2K)
$$
shows that $c_i=2^{g_i}n_{i+1}-3n_i$ satisfies
$$
 0<K-\tfrac72 Q\le c_i<2K+\tfrac72Q<20Q,\qquad c_i\equiv1\bmod Q.
$$
Since $\gcd(A,p)=1$, consecutive *sorted* ideal levels are separated by at least $H(2^{1/p}-1)\ge H\log(2)/p$. Now $H/p=K/[3p(e^{\Lambda/p}-1)]\sim K/(3\Lambda)\to\infty$. Therefore the $n_i$ are positive and pairwise distinct for sufficiently large clocks. With $c(n_i)=c_i$, the odd part of $3n_i+c(n_i)$ equals $n_{i+1}$ with valuation exactly $g_i$. The finite orbit has least odd period $p$ and its shortcut word has least period $A$.

Select a subsequence with disjoint height intervals and $H$ growing at least geometrically. Define the single autonomous function by these values on the selected cycles and $c(n)=1$ elsewhere. To see that the exceptional inputs can be made sparse, arrange $\sum_{k<j}p_k/H_j\to0$ when selecting the intervals. One also has $p_j/H_j\to0$. In interval $j$, and in the gap after it, the number of assigned inputs up to that point is at most $\sum_{k\le j}p_k$, divided by a threshold of at least $H_j-Q/2$. Their union has natural density zero.

There is a second simultaneous variant. Given any unbounded nondecreasing $E(n)>0$, run the construction at stage $j$ with $Q_j=\operatorname{lcm}(6,j!)$. Choose its clocks so large that the intervals are disjoint, $\Lambda_j\to0$, both sparsity estimates above hold, $Q_j/H_j\to0$, and $E(\lfloor H_j-Q_j/2\rfloor)\ge20Q_j$. The resulting single function agrees with $1$ modulo each fixed integer eventually, equals $1$ off a set of density zero, and satisfies $c(n)\le E(n)$ eventually. It still has all the prescribed genuine finite integer cycles, whereas the literal $+1$ cycles on their words have unbounded full denominator. The uniformly bounded alphabet was asserted for a fixed modulus. A bounded integer function congruent to $1$ modulo every fixed modulus eventually must itself equal $1$ eventually.
