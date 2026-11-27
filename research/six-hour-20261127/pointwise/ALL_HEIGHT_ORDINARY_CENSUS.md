# All positive rational heights at one ordinary integer

For an odd positive integer $x$ define
$$
 Q(x)=\sup_{\substack{p,q\ge1,\ (p,q)=1\\3\nmid q}}
          \frac{v_3(qx+p)}{\log(2\max(p,q))},
 \qquad g(x)=\log(3+\log(x+1)).
$$
Logarithms are natural. This is one statistic for every height simultaneously: $Q(x)\le D$ implies $v_3(x+t)\le D\log(2H)$ for every positive rational of height at most $H$, at this same $x$. Reduced denominators divisible by three have negative scores and can be included in that conclusion. Positivity gives $3^{v_3(qx+p)}\le h(x+1)$, $h=\max(p,q)$, and in particular the supremum is finite.

**Theorem A.** For $c>0$ let $\mathcal A_c=\{x>0\text{ odd}:Q(x)>cg(x)\}$. Then
$$
             \sum_{x\in\mathcal A_c}\frac1x<\infty
             \quad\Longleftrightarrow\quad c>\frac1{\log2\,\log3}. \tag{A}
$$
This statement concerns a set of actual starting integers. It places no restriction on which of those integers belong to one supplied exceptional forward orbit.

Consider the uniform odd integers in $[2^k,2^{k+1})$, $k\ge1$. There $g(x)=\log k+O(1)$ with absolute upper and lower errors. A violating anchor has $3^v>(2h)^{c g(x)\log3}$ and $3^v\le h(x+1)$, so $h\le\exp(O_c(k/\log k))$ on all sufficiently large octaves. For fixed $h$ there are at most $2h$ ordered positive numerator-denominator pairs of exact height $h$. A unit denominator specifies one residue mod $3^d$, where $d=\lfloor c\log(2h)(\log k-C_0)\rfloor+1$ suffices for the upper count. The probability of that residue in the octave is at most $3^{-d}+2^{1-k}$. Summing the second term over every possible pair is exponentially small in $k$. For the first term put $s=c(\log3)(\log k-C_0)$. When $s$ is large, $\sum_{h\ge1}2h(2h)^{-s}\ll2^{-s}$. Thus the octave contribution to the reciprocal sum is $O_c(k^{-c\log2\log3}+e^{-c'k})$. This proves convergence on its claimed range.

For sharpness use only $p=q=1$. Fix an integer $d>\!c\log2(\log k+C_1)$ with $d=c\log2(\log k+C_1)+O(1)$, taking $C_1$ larger than the uniform upper error for $g(x)$. Every odd $x\equiv-1\bmod3^d$ in this octave violates the bound. Their probability is at least $3^{-d}-2^{1-k}\gg_c k^{-c\log2\log3}$. Since $x$ and $2^k$ differ by at most a factor two, the harmonic contributions diverge at and below the threshold.

**The pointwise time obstacle.** No interval $[0,C\log n]$ with $C<1/\log2$ works at *every* ordinary start with any fixed multiplier of $g$. Let $s=\lceil(\log(k+2))^2\rceil$, $n=2^{k+1}3^s-1$. The first $k$ actual exponents are one and $x_j+1=2^{k+1-j}3^{s+j}$ for $0\le j\le k$. Hence $Q(x_j)\ge(s+j)/\log2$ throughout, while $\max_{j\le k}g(x_j)=O(\log k)$ and $\log n/k\to\log2$. This family does not refute an all-height clock with a larger absolute time constant. The height-dependent one-clock theorem and (A) by themselves supply no such universal all-height result.
