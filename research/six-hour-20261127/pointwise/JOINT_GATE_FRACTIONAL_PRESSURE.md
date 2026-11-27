# Fractional pressure of the full original principal trace with its drift gate

Fix $1<a<2$ and the original independent law $\Pr(e)=2^{-e}$. At length $n$ set $A_i=\sum_{j<i}e_j$, $A=A_n$, $W=\{A_i\le ai,\ 1\le i\le n\}$. Write $m$ for the least positive odd source of the actual word, $G=\sum_{i<n}2^{A_i}/3^{i+1}$ and $Z(z)=2^A/(m+zG)$, for fixed $z\ge0$. With $d=H_2(1/a)$ put
$$
 \gamma=2^{-a(1-d)},\qquad p_c=1+\log_2\gamma=1-a(1-d).
$$
Here $p_c$ denotes a certified endpoint, with no optimality assertion beyond the displayed range.

**Theorem.** For every real $p\le p_c$,
$$
 \lim_{n\to\infty}\frac1n\log\mathbb E[\mathbf1_W Z(z)^p]=\log\gamma. \tag{1}
$$
For $p_c\le p\le1$ the upper exponential rate is at most $(p-1)\log2$. In particular the normalized conditional critical moment $\mathbb E[Z(z)^{p_c}\mid W]$ grows at most polynomially. These are estimates on **all accepted words under their original probabilities**, including every actual principal source and unscreened physical height. For the drift $a=7/4$ the endpoint is $1+\log_2((7/8)(7/6)^{3/4})$.

The rotation count at total $\lfloor an\rfloor$ and the geometric tilt of mean $a$ give
$$
 c_a n^{-3/2}\gamma^n\le\Pr(W)\le\gamma^n.
$$
These two elementary bounds are proved in the accompanying rare-gate profile. Every word has $m<2^{A+1}$, and its principal terminal $y=3^n2^{-A}(m+G)$ is below $2\cdot3^n$, so $Z(z)\ge1/(2\max(1,z))$.

## Counting physical seeds at one total and one seed shell

Fix the integer total $n\le A\le\lfloor an\rfloor$, put $b=A-n$, and take $k=\lfloor\log_2m\rfloor\in[0,A]$. Among the first $k$ physical shortcut positions the number of even departures is at most
$$
 \min((1-1/a)k,\ b).                                                   \tag{2}
$$
For the first bound when $k\ge1$, stop the first accepted odd-clock prefix whose total reaches $k$. With $i$ its odd date there are exactly $i$ odd departures in these first $k$ shortcut positions, and $i\ge k/a$ by the prefix gate. For the second bound there are exactly $A-n$ even positions in the entire $A$-position shortcut word. At $k=0$ both statements hold. Each length-$k$ binary word determines one residue modulo $2^k$ and hence at most one integer in $[2^k,2^{k+1})$. Such an integer determines just one length-$n$ actual word by forward determinism. Consequently, even with the specified total fixed, (2) bounds the number of relevant words by the binary upper entropy bound for strings with that many even positions.

Set $k_0=ab/(a-1)$. For $0\le k\le k_0$, the reciprocal $p$-power mass in the shell, with $p\ge0$, is at most $2^{(d-p)k}$. For $k>k_0$ it is at most
$$
 2^{kH_2(b/k)-pk}.                                                       \tag{3}
$$
Here $b/k<1-1/a<1/2$, as required by the binomial bound. For $b>0$ the derivative in $k$ of the exponent in (3) is $-\log_2(1-b/k)-p$, at most $\log_2 a-p$. If $b=0$ that exponent is $-pk$. Thus, whenever $\log_2a\le p\le d$, every shell costs at most $2^{(d-p)k_0}$, including the adjoining real boundary $k_0$ and the zero-even case. There are at most $A+1$ shells.

For $p\ge0$ the true joint moment is bounded by its value at $z=0$, where the mass of each word is exactly $2^{-(1-p)A}m^{-p}$. The exponent resulting from the shell bound is
$$
 (p-1)A+(d-p)\frac{a(A-n)}{a-1}.
$$
It is linear on $n\le A\le an$, taking endpoint values $(p-1)n$ and $a(d-1)n=n\log_2\gamma$. Summing totals and shells therefore costs at most
$$
 C_a(n+1)^2 2^{n\max(p-1,\log_2\gamma)}.                               \tag{4}
$$
This bound holds for $\log_2a\le p\le d$. For $d\le p\le1$, each shell instead costs at most $2^{(d-p)k}\le1$ using just the prefix half of (2), so the rate is at most $(p-1)\log2$ on this range as well.

Now $p_c<d$ follows from $d-p_c=(a-1)(1-d)>0$, and
$$
 p_c-\log_2 a=(a-1)\left(\log_2\frac{a}{a-1}-1\right)>0.
$$
At $p=p_c$ the two exponents in (4) coincide. Dividing by the lower gate probability proves $\mathbb E[Z(z)^{p_c}\mid W]\le C_a(n+1)^{7/2}$. For $0\le p\le p_c$, conditional power mean gives a polynomial upper bound and the uniform positive payoff floor gives a constant lower bound. For $p<0$ the floor gives a constant upper bound, and conditional Jensen for the convex negative power $p/p_c$ applied to $Z(z)^{p_c}$ gives a polynomial lower bound. Multiplying again by $\Pr(W)$ proves (1). The upper rate for $p_c\le p\le1$ follows from (4) and the last shell bound.

The additional constraint $b=A-n$ in (2) uses the very same complete accepted word as the physical dyadic shell count. Using only the total composition count and the all-depth sparse-seed count separately gives a weaker finite range of exact rates. At $p=1$ the upper rate supplied here is zero. It gives no decay of the full first-power trace and no exclusion of a fixed ordinary survivor. The proof of (1) uses no orbit-distribution assumption, irrationality input or independent resampling.

The principal seed identity and fixed-drift binary cutoff argument are originally used in PR201's global prefix trace. [Global prefix trace](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)
