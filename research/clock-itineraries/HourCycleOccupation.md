# Height counts on finite simple Collatz paths

Put $\alpha=\log_2 3$, let $h(s)=s\log s-(s-1)\log(s-1)$, and set $\gamma=h(\alpha)/\log3\simeq0.949956$. For every $\theta>\gamma$ there is $C_\theta$ such that **every finite sequence of distinct consecutive positive odd Collatz sites** satisfies
$$
  \#\{x\text{ in this sequence}:x\le X\}\le C_\theta X^\theta\qquad(X\ge1).
$$
The constant is uniform in the length, starting point, and maximum height. The argument sharpens the exponent $39/40$ in the repository's finite simple-path estimate by reapplying the counting function to a smaller height. It is a written proof. [Prior finite-path argument, §1](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass3/FINITE_RECORDS.md)

## Reduction to a smaller height

The same entropy exponent appears in earlier counts of all-time coefficient-supercritical sources and global forward minima. Here the distinctness of later endpoints on one path allows the reduction at high total clock. A count on each individual path places no bound on the union of the inverse basins of many paths. [Earlier population estimates](https://github.com/GettysburgResearch/collatz/blob/38766dec583b5ad5fc09dd010b41a53f0ec417db/research/external/mazur-2026/fixed-height-power-saving-attack.md)

It suffices to consider $\gamma<\theta<1$. Choose $\alpha<s<2$ close enough to $\alpha$ that $\gamma_s=h(s)/(s\log 2)<\theta$. For an integer cutoff $X$ put $b=\lfloor(\log_2 X)/s\rfloor$ and initially take $X$ large enough that $b\ge1$. Write $P(X)$ for the number of sites at most $X$ on the given path. At most $b$ final sites lack $b$ subsequent steps. Classify all other small sources by the sum $A$ of the next $b$ positive odd-to-odd valuations.

**Low total clock.** For a fixed word of sum $A$, its starting odd value lies in one residue class modulo $2^{A+1}$. Indeed the integer affine identity at the far endpoint $y$ is $2^A y=3^b x+c$ with a carry determined by the word. Since $y$ is odd and $3^b$ is invertible modulo $2^{A+1}$, this determines the class of $x$. When $A\le sb$, we have $2^A\le X$, so there are at most $2X\,2^{-A}$ possible starts at or below $X$ for this word.

There are $\binom{A-1}{b-1}$ ordered words. Put $z=2(s-1)/s\in(0,1)$. The geometric series for each of the $b$ positive valuations yields
$$
 \sum_{A=b}^{\lfloor sb\rfloor}\binom{A-1}{b-1}2^{-A}
 \le z^{-sb}\left(\frac{z}{2-z}\right)^b
 =\exp\big(b[h(s)-s\log 2]\big).
$$
The exponent in brackets is negative for $1<s<2$, by strict concavity. Accounting for the floor in $b$ costs a constant depending on $s$. The total number of these sources is $O_s(X^{\gamma_s})$.

**High total clock.** For $A>sb$, iteration of $y'=(3y+1)/2^e$ gives
$$
  y\le3^b2^{-A}x+(3/2)^b-1 .
$$
Each additive summand is at most one half times a power of $3/2$ since $e\ge1$. Hence $y\le C_s X^{\alpha/s}$, as the two terms have respective exponents $\alpha/s$ and $(\alpha-1)/s$. These endpoints are distinct sites of the same finite sequence. Counting them with $P$ gives
$$
 P(X)\le b+C_s X^{\gamma_s}+P\big(\lfloor C_s X^{\alpha/s}\rfloor\big).
$$
Both exponents $\gamma_s<\theta$ and $\alpha/s<1$ are strict. For $X$ beyond a fixed cutoff the recursive argument is smaller than $X$ and its $\theta$th power is at most $X^\theta/2$. Strong induction on the integer cutoff now bounds $P(X)$ by $C_\theta X^\theta$. Enlarge $C_\theta$ to absorb the first two terms in $C_\theta X^\theta/2$ and cover all smaller base cases using $P(X)\le X$.

## Cycles, escape, and the clock

For every fixed $0<\beta<1/\gamma\simeq1.052681$, a primitive cycle with $p$ odd sites has all but $O_\theta(p^{\beta\theta})=o(p)$ sites above $p^\beta$, by choosing $\gamma<\theta<\min(1,1/\beta)$. The same estimate holds on each simple path of $p$ odd sites. The threshold is absolute and places no restriction on the ratio of maximum to minimum.

For $\gamma<\theta<1$, dyadic summation from a floor $m\ge1$ gives $\sum_i x_i^{-1}=O_\theta(m^{\theta-1})$ uniformly on finite simple paths above $m$. Thus on an escaping positive odd orbit the correction factor in
$$
  \frac{2^{e_0+\cdots+e_{j-1}}}{3^j}
  = \frac{x_0}{x_j}\prod_{i<j}\left(1+\frac1{3x_i}\right)
$$
is bounded independently of $j$. For each $0<\beta<1/\gamma$, all but $o(p)$ of the indices $j<p$ have clock ratio at most $C_{x_0,\theta}p^{-\beta}$. These are negative clock excursions. They remain compatible with an escaping trajectory. The proof uses only integer residue classes, elementary estimates, and counting on the individual ordinary path.
