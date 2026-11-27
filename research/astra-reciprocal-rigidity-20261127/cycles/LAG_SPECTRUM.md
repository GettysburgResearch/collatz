# Rational approximations to every lag with few mismatches

**PROPOSED written theorem, no external Collatz premise.** Keep $n,d,m,\alpha$ and $s=s(h)$ from [the all-shift theorem](ALL_SHIFT.md). Define $L=1+\log_2(d(m+1))$.

**Theorem.** If $n\ge4sL$, then there exists an integer $q$ with
$$
1\le q\le 8s,\qquad \min_{p\in\mathbb Z}|qh-pn|\le2s^2. \tag{6}
$$
This concerns the actual time shift $h$, not the collection of positions on which the bits mismatch. A zero remainder is allowed and records a small-order shift.

At any integer cutoff $k\ge1$ for which $n\ge4kL$, the number of proper shifts with $s(h)\le k$ is at most
$$32k^3+32k^2+4k. \tag{7}$$
For ordinary cycles with polynomial minimum this applies uniformly at $k=o(n^{1/3})$ for large $n$, so only $o(n)$ shifts can have such a small mismatch count. If the reduced fraction $h/n$ has a convergent denominator in $[c_1n^{1/3},c_2n^{1/3}]$ for fixed positive $c_1,c_2$, then $s(h)\gg_{c_1,c_2} n^{1/3}$ when $L=O(\log n)$. This last criterion specifies an individual lag.

### Coverage by a convergent denominator

Suppose $P/Q$ is a reduced convergent to $h/n$, including the terminal convergent. For the first $Q$ multiples of $h/n$ on the unit circle, each grid point $jP/Q$ has the corresponding point $jh/n$ at circular distance at most $1/Q$. This uses $|h/n-P/Q|\le1/Q^2$ and $0\le j<Q$. An empty clockwise gap of length greater than $3/Q$ would, after removing an open interval of length $1/Q$ at each end, contain a grid point more than $1/Q$ away from every anchor, a contradiction. Hence from the phase at the minimum, the $Q$ forward shifts by multiples $0,h,\ldots,(Q-1)h$ have maximum clockwise gap at most $3n/Q$ in clock units. For $Q=1,2$ the same loose bound follows directly.

The maximum of the shifted numerator $N_i+d$ on this anchor set is at most $d(m+1)3^{s(Q-1)/2}$ by successive use of the centered pair bound (2) in the main note. From any anchor the shifted numerator grows per physical clock by at most $3/2$. Therefore its log-base-two maximum over the **whole cycle** satisfies
$$\log_2\max_i(N_i+d)\le L-1+(\alpha/2)s(Q-1)+3(\alpha-1)n/Q.$$

Around the circle there are $s$ discrepancies and hence $s$ intervening common runs, including runs of length zero. The longest such run has length at least $n/s-1$. At its entrance the nonzero paired numerator difference is divisible by $2^R$. We conclude
$$\frac ns<L+\frac{\alpha}{2}s(Q-1)+3(\alpha-1)n/Q. \tag{8}$$

### The short multiple and the number of admissible lags

If the denominator of $h/n$ in lowest terms is at most $8s$, take it for $q$ in (6). Otherwise take the **first** convergent denominator $Q\ge8s$ and let $q$ be its predecessor denominator, so $1\le q<8s$. In (8) the first term is at most $n/(4s)$, while the final term is at most $(9/40)n/s$ since $\alpha<8/5$. Consequently
$$\tfrac12 n/s < (\alpha/2)sQ,\qquad Q> n/(2s^2).$$
The elementary bound for two consecutive convergents gives $|q h/n-p|\le1/Q$ at the preceding numerator $p$. This proves (6). The individual cube-root conclusion follows directly from (8): if $s\le c\,n^{1/3}$ the left side is $\ge n^{2/3}/c$, the middle term is $O(c\,n^{2/3})$, and the last term is $O(n^{2/3}/c_1)$. Choosing $c$ sufficiently small gives a contradiction, uniformly for large $n$.

For each $1\le q\le8k$ write $v=\gcd(n,q)$. A right side $r$ in $[-2k^2,2k^2]$ admits solutions of $qh\equiv r\bmod n$ only when $v\mid r$, and in that case it admits exactly $v$ residue classes of $h$. Thus this $q$ contributes at most $v+4k^2$. Summing using $v\le q$ proves (7). No independence of the shifts is assumed.

The cyclic identity $\sum_h s(h)=2u(n-u)$ supplies only the mean. It does not yield (6) for an individually specified lag. The new restriction leaves the typical case of linearly many mismatches at every proper lag open. Armstrong's project has a related sparse rotation spectrum on the **odd valuation clock**, cited by Wren 218/v2 §7; we make no priority claim about a transfer beyond the stated shortcut formulation. [Versioned comparison](https://rstation.ai/problems/collatz/papers/218/v2)
