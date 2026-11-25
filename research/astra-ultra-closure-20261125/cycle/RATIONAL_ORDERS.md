# Both rotation orders allow a linear number of sorted octave changes

**PROPOSED written theorem.** There exist nonordinary positive rational shortcut cycles of arbitrarily large odd period $p$ with the following simultaneous properties.

- Every odd valuation is 1 or 2. The odd phases lie in $[s,8s/3)$, where $s$ is the minimum.
- Dyadic mantissas of odd phases advance by $h$ ranks modulo $p$, and ternary mantissas of all physical phases advance by $-p$ ranks modulo the shortcut period $h$.
- More than $p/20$ adjacent sorted dyadic octave labels change, and more than $p/10$ odd phases exceed $2s$.
- A fixed positive fraction of physical phases are both above $2s$ and strict all-pasts records for the PR193 threshold $3/5$.

One can take $h/p$ along upper continued-fraction convergents of $\alpha=\log_2 3$. The construction establishes neither the stronger exponent $1000/479$ of PR200 nor the ordinary least-basin condition. It shows that the two order properties together with synchronized records permit linearly many octave changes on genuine rational trajectories. Integrality remains essential.

## Construct a literal rational cycle

For a sufficiently large reduced upper convergent, put $\delta=h-p$, $m=\lfloor p/3\rfloor$ and $R(r)=(r+\delta)\bmod p$ for $0\le r<p$. Both $\delta$ and $p-\delta$ exceed $m$ because $\delta/p\to\alpha-1$. Set $j_r=0$ outside $1\le r\le m$, and choose a bit $j_r\in\{0,1\}$ inside. Put $k_r=\lfloor(r+h)/p\rfloor$ and $a_r=k_r+j_r-j_{R(r)}$. If $R(r)=r+\delta$, the target is above $m$, so $a_r=1+j_r$. When the addition wraps, the source is above $m$, so $a_r=2-j_{R(r)}$. Thus every $a_r$ is 1 or 2. Their sum is $h$.

There is a unique positive rational solution to the cyclic equations
$$
       2^{k_r}t_{R(r)}=3t_r+2^{-j_r}.
$$
Indeed $R$ has period $p$, the return slope is $3^p/2^h<1$, and the affine intercept is positive and rational. Put $x_r=2^{j_r}t_r$. Then $2^{a_r}x_{R(r)}=3x_r+1$. The rotated fixed-point formula gives odd numerators and denominators prime to six after reduction. Before reduction, the common denominator is $2^h-3^p$, and the carry numerator of each rotated word is odd and nonzero modulo three by its first and last summands. Consequently all valuations are exact. The physical parity word has $p$ odd positions in $h$ steps. Any proper repetition would make its repeat count divide $p$ and $h$, contrary to coprimality.

It remains to show that the prescribed rank labels are realized by the actual *sizes* of the rationals. This will be done for a positive proportion of the $2^m$ choices.

## Uniform height estimate

Write
$$
 v_r=2^{-r/p}t_r,\quad \lambda=3\,2^{-h/p},\quad
 b_r=2^{-(r+h)/p}2^{-j_r}.
$$

Then $v_{R(r)}=\lambda v_r+b_r$. Put $\bar b=p^{-1}\sum_r b_r$ and $V=\bar b/(1-\lambda)$. All $b_r$ are uniformly bounded above and below by positive absolute constants. The upper-convergent error is at most $p^{-2}$. Hence $0<1-\lambda=O(p^{-2})$ and $V\gg p^2$.

Choose the $m$ free bits independently with equal probabilities. With probability tending to one, all cyclic partial sums of $b_r-\bar b$ in rotation order, over lengths at most $p$, are $o(p)$. Here are details for the quantifiers.

1. The expected $b_r$ is $2^{-h/p}f(r/p)$ where $f(u)=2^{-u}(1-\mathbf1_{(0,1/3]}(u)/4)$ on $[0,1)$. For any $\epsilon>0$, this bounded piecewise smooth function has upper and lower trigonometric polynomial approximants with integrals within $\epsilon$ of its integral. One obtains them by replacing the finitely many jumps by continuous upper and lower ramps, then using uniform trigonometric approximation with a constant margin. For each nonconstant Fourier term with fixed frequency $n$, its sum over any segment of the rotation is bounded by $2/|1-\exp(2\pi i n\delta/p)|$. This is uniformly bounded for large $p$ because $\delta/p$ tends to an irrational number. The two approximants thus bound the departure from length times the integral by $\epsilon p+O_\epsilon(1)$ uniformly over all starts and lengths at most $p$. The arithmetic grid mean tends to the same integral. This proves uniform $o(p)$ discrepancy of the deterministic mean field after subtracting its own grid mean.
2. In one lap in rotation order, the variables $b_r-\mathbb E b_r$ are independent, centered and bounded by one. Their prefix sums $S_k$ satisfy $\Pr(\max_{k\le p}|S_k|\ge p^{3/4})\le p^{-1/2}$. Indeed, partition the crossing event by the first crossing index $k$. On each such event the conditional expectation of $S_p^2$ given the first $k$ variables is at least $S_k^2$, while $\mathbb E S_p^2\le p$. Every cyclic segment of length at most $p$ is a difference of prefixes, with at most one extra total sum at a wrap. Subtracting the realized mean changes each such sum by at most $|S_p|$. This proves the asserted uniform discrepancy.

The number of occupied bits has mean $m/2$ and variance at most $m/4$. Among $\lfloor m/2\rfloor$ disjoint adjacent pairs the number with unequal bits is a sum of independent fair Bernoulli variables. Chebyshev's inequality therefore gives more than $p/10$ occupied bits and more than $p/20$ differing pairs with probability tending to one. In particular at least $2^{m-1}$ patterns satisfy both count bounds and a common uniform $o(p)$ discrepancy estimate, for all sufficiently large convergents.

For any of those choices, every partial sum of $b_r-\bar b$ read backward in rotation order is uniformly $o(p)$ even beyond one lap, by its zero total. Summing the recurrence backward gives the absolutely convergent weighted sum for $v_r-V$. Abel summation bounds its absolute value by the supremum of those partial sums since $\sum_{i\ge0}(1-\lambda)\lambda^i=1$. Consequently
$$
                         v_r=V+o(p)
$$
uniformly in rank and in the selected patterns.

## The actual two orders

The virtual endpoints $t_r=2^{r/p}(V+o(p))$, including $t_p=2t_0$, are strictly increasing for large $p$. The nominal spacing is at least $(2^{1/p}-1)V\gg p$, and the uniform additive error in a difference is $o(p)$. Thus $s=t_0$ really is the minimum, the assigned $j_r$ are the ordinary logarithmic octaves of the odd phases, and the dyadic rank advance is $R$. The elevated phases have ranks at most $m$ and therefore $x_r/s\le 2^{4/3}+o(1)<8/3$. The other odd phases are below $2s$. Each occupied bit is at a strictly positive rank, so its odd phase exceeds $2s$.

Give each odd phase the integer label $L=r+p j_r$. Each intervening even physical phase equals twice its odd successor and receives its successor's label plus $p$. Hence every physical value is $2^{L/p}(V+o(p))$. Under one shortcut step the label changes by $h-p$ at an odd departure and by $-p$ at an even departure, by the definition of $a_r$. Its residues modulo $h$ are therefore all distinct and cover $0,\ldots,h-1$. Every $L$ is nonnegative and at most $(7/3)p<2h$ for large $p$.

Write $L=\sigma+\ell h$ with $\ell\in\{0,1\}$. The physical value divided by $3^\ell$ equals
$$
  2^{\sigma/p}(V+o(p))(2^{h/p}/3)^\ell
   =2^{\sigma/p}(V+o(p)).
$$
Indeed $(2^{h/p}/3-1)V=\bar b/\lambda=O(1)$. At $\sigma=0$ the value is $s$, since its physical phase is the starting minimum. At the virtual upper endpoint $\sigma=h$ use $3s$, also within $o(p)$ of $2^{h/p}V$. Nominal spacings are again $\gg p$, so the normalized physical values increase strictly in $\sigma$ and lie in $[s,3s)$. This proves the claimed ternary rotation for actual rational sizes.

The first two inverse odd gaps at rank zero are both 2. Their source ranks $p-\delta$ and $2(p-\delta)$ both exceed $m$, and both transitions wrap. The first forward odd gap from rank zero is 1. Consequently $s\equiv1\bmod 9$ and $s\equiv3\bmod4$ in the indicated local residue rings. Thus $(2s+1)/3\equiv1\bmod12$ also holds.

## Synchronized records and nonintegrality

Write $e_i=1$ at an odd physical departure and 0 at an even one. For $\rho=3/5$ let the score increment be $(e_i-\rho)\log3$. Its lap drift is positive, since $p/h\to1/\alpha>\rho$. Strict all-pasts records therefore recur periodically. If $a$ is a strict record and $a<t$ precedes the next one, the score has not risen above its value at $a$. The exact physical log-height increment equals the score increment minus $\log2-\rho\log3>0$, plus $e_i\log(1+1/(3x_i))$. As $s\to\infty$, the last term is uniformly at most half the positive drift correction. It follows that
$$
 \log x_t\le\log x_a-c(t-a),\qquad c=(\log2-\rho\log3)/2>0.
$$
All physical values are between $s$ and $6s$. Each high phase is therefore preceded by a high strict record at distance at most $(\log6)/c$, allowing distance zero. This gives a fixed positive fraction of high strict records from the $>p/10$ high odd phases and $h<2p$. This use of the score does not assume denominator one. [PR193 record criterion](https://github.com/GettysburgResearch/collatz/blob/24cdd0e5471d4421716cfce6bd88916f858f994c/research/astra-universal-proof-20261124/critical/COMPANION_SYNCHRONIZATION.md)

Finally distinct selected patterns give distinct cycle minima. A given rational minimum determines its forward orbit, and sorting the dyadic mantissas recovers every bit. Wu and Wang's integer linear-form bound and the exact lap identity bound *all* these minima by $O(p^6)$, as shown in the companion proof with any fixed $\epsilon<0.88$. There are at most $O(p^6)$ possible ordinary positive minima but at least $2^{m-1}$ distinct minima, so nonordinary examples exist for each sufficiently large upper convergent. The same counting bound gives examples whose reduced denominator grows exponentially: the number of positive rationals of size at most $O(p^6)$ and denominator at most $Y$ is $O(p^6Y^2+Y)$, which is smaller than $2^{m-1}$ for $Y=2^{p/10}$ and large $p$. No period bound stronger than the ordinary upper-convergent accuracy is imposed in this existence argument. [Complete-denominator bound and source](README.md)

As a finite exact check, choose $(p,h)=(306,485)$ and set the odd-indexed ranks of $1,\ldots,102$ to one. The prescribed word has 103 sorted changes and 51 high odd states. Both rank permutations hold on all phases, 75 strict record phases are high, and the reduced denominator has 476 binary digits. The checker reconstructs the rational minimum and every physical phase using integer and fraction arithmetic. This example tests the construction at one convergent. The asymptotic existence assertion uses the proof above. [Exact control](check.py)
