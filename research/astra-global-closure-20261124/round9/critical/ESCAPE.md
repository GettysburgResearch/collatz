# Growth required of one escaping ordinary trajectory

**Written elementary bound.** Let $x_j=T^j(x_0)$ be an aperiodic positive integer shortcut orbit. Let $P_j$ count the odd inputs before time $j$, $X_H=\max_{0\le j\le H}x_j$, $\alpha=\log_3 2$ and $\rho=H_2(\alpha)=0.949955527\ldots$, where $H_2$ is binary entropy. Then

$$
 \liminf_{H\to\infty}\frac{\log X_H}{\log H}\ \ge\ \rho^{-1}=1.05268\ldots.
$$

The count below uses distinct vertices of the supplied ordinary orbit. No typicality of its initial value or its individual windows is assumed. Garcia and Tal proved a uniform zero-Banach-density theorem for each orbit, with a power saving in their finite packing estimate. PR201 supplies an explicit simple-path exponent $39/40$. We give a separate peak estimate at the entropy exponent. It controls the maximum up to time $H$, whereas a spatial occupation theorem can also count visits separated by large excursions. [Garcia and Tal, *A note on the generalized 3n+1 problem*, Acta Arithmetica 90 (1999), Corollary 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf) · [PR201 simple-path estimate](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md)

All $x_j$ are distinct. Multiplying the physical step ratios gives

$$
 \log(x_H/x_0)=P_H\log3-H\log2+\sum_{j<H,\,x_j\text{ odd}}\log(1+1/(3x_j)).
$$

The sum is at most $(1+\log H)/3$, since $H$ distinct positive integers have reciprocal sum at most the first $H$ harmonic numbers. The left side is at least $-\log x_0$. It follows that $P_H\ge\alpha H-O_{x_0}(\log(H+1))$.

It suffices to consider subsequences with $\log X_H=O(\log H)$. Set $d=\lceil\log_2(X_H+1)\rceil=O(\log H)$. The $H-d+1$ complete length-$d$ windows of the first $H$ parity bits have total weight at least $dP_H-d(d-1)$. A lost copy can occur only at the two ends. Their mean fraction of odd inputs is consequently at least $\alpha-o(1)$. For any $1/2<a<\alpha$, at least $c_a H$ windows have weight at least $ad$ for all large $H$. For example use any $0<c_a<(\alpha-a)/(1-a)$ and the upper weight $d$ of each window.

Their starting integers $x_j$ are distinct and lie in $[1,X_H]\subset[0,2^d)$. At this binary precision the shortcut parity map is a bijection, so there are at most $\sum_{k\ge ad}\binom{d}{k}\le2^{dH_2(a)}$ such starts. The last inequality follows by weighting the binomial expansion by $a^k(1-a)^{d-k}$. Thus $H\ll_a X_H^{H_2(a)}$ along the chosen subsequence. Letting $a$ increase to $\alpha$ proves the result.

For the coefficient excess $D_j=P_j\log3-j\log2$, the simple-path reciprocal estimate of PR201 bounds the correction sum uniformly in $j$, for instance by $200/3$ for a path above 1. Consequently $D_j\to+\infty$ because an infinite nonrepeating integer orbit leaves every finite set, and

$$
 \liminf_{H\to\infty}\frac{\max_{j\le H}D_j}{\log H}\ \ge\ \rho^{-1}.
$$

This excludes an escaping trajectory whose coefficient tracks the critical slope within a fixed additive band, and even one whose upper excess stays below $c\log H$ cofinally for some $c<1/\rho$ in the running-maximum sense. A path can obey these restrictions while having asymptotic odd fraction $\alpha$. For example the abstract counts $\lfloor\alpha h+C\log(h+1)\rfloor$ have eventual increments in $\{0,1\}$ and can satisfy the lower peak restriction for $C\log3>1/\rho$. Realization of this symbolic example by an ordinary positive source is not established. Growth beyond $6q$ or beyond the bound above does not contradict being a positive Collatz trajectory.
