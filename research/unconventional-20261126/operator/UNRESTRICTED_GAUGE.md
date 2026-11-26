# The logarithmic gauge threshold for unbounded incoming slopes

**Status.** PROPOSED written theorem. The unrestricted set allows deep negative excursions between large incoming slopes. This changes its critical Hausdorff gauge from the one for the all-prefix positive critical trace in [Theorem S](../renewal/SHARP_GAUGE.md).

Use $B$ from [OP-T1](TERNARY_TRANSFER.md), $X=\{y\in\mathbb Z_3:B(y)=\infty\}$, $p=\log_3 2$, $\theta=H_2(p)$ and small-scale gauges $g_\gamma(r)=r^\theta(\log_3(1/r))^\gamma$. Then
$$
 \mathcal H^{g_\gamma}(X)=0\quad(\gamma<1/2),\qquad
 \mathcal H^{g_\gamma}(X)=\infty\quad(\gamma>1/2).
$$
In particular its dimension is $\theta$. The proof leaves equality open. The set $X$ is a dense $G_\delta$ in the ternary units, with Haar measure zero and no positive ordinary integer. Every finite script defines a clopen cylinder, so $\{B>t\}$ is open. The points $-2^{-j}$, $j\ge0$, are dense among the units and allow $j$ letters $E$ followed by arbitrarily many $O$, proving the category claim. On $3\mathbb Z_3$ only doublings occur and $B=1$. Haar nullity and the ordinary bound follow from [OP-B1](TERNARY_BARRIER.md) and OP-T1.

## OP-U1. Upper measure bound

Let binary scripts have independent letters with probabilities $p$ for $O$ and $1-p$ for $E$. Write $a=\log(3/2)>0$, $b=\log 2>0$ and $S_k=\log C_k=q\log3-kb$. The increments $a,-b$ are centered. With $h=-\log(1-p)/b>1$ the probability of an individual word is exactly
$$
                       \Pr(w)=3^{-\theta q}\exp(hS_k).
$$
This follows by comparing coefficients of $k,q$, using $p\log3=b$. Here $q$ is the number of odd letters and the ternary cylinder radius is $3^{-q}$.

Cover $X$ by scripts first crossing $L>0$. They form a prefix code, end with $S_k>L$ and have $q\ge L/a$. The centered bounded walk satisfies
$$
 \Pr(\tau_L>k)\le\min\{1,C(1+L)(1+k)^{-1/2}\},\qquad
 \tau_L=\min\{k:S_k>L\}.
$$
This is the one-sided estimate [O3](../renewal/OCCUPATION.md), rescaled to the present increments and sign. For $0<\gamma<1/2$ integration gives $\mathbb E\tau_L^\gamma\ll_\gamma(1+L)^{2\gamma}$. The total $g_\gamma$ cost is at most $e^{-hL}\mathbb E\tau_L^\gamma$ since $q\le k$. Taking $L\to\infty$ proves the upper bound. The estimate at $\gamma=0$ uses only prefix-freeness, and smaller gauges follow by comparison.

## OP-U2. A long excursion of bounded weighted occupation

For a fresh centered walk write $\tau=\min\{i\ge1:S_i>0\}$ and $V=\sum_{i<\tau}e^{S_i}$, including $i=0$. There exist absolute constants $K,c>0$ such that for all sufficiently large integers $N$,
$$
 \Pr\big(N\le\tau\le2N,\ a/4\le S_\tau\le3a/4,\ V\le K\big)
                          \ge c N^{-1/2}.                         \tag{U1}
$$

First omit $V$. For a central word of length $m$ choose its odd count $q$ so that $\delta=q\log3-mb\in[b-3a/4,b-a/4]$. This is possible for a positive-density set of $m$, because the sequence $mp\bmod1$ is equidistributed and the interval has positive length strictly below $\log3$. In particular there are $\gg N$ such $m\in[N,2N-2]$. Their $q=mp+O(1)$, so the total probability of central words at that count is $\gg m^{-1/2}$ by Stirling.

Rotate each central word after a maximum of its partial sums at indices $0,\ldots,m-1$. All partial sums of the rotated word are at most $\delta$: nonwrapped proper sums before the old endpoint are nonpositive, the old endpoint contributes at most $\delta$ since the maximum is nonnegative, and wraparound adds $\delta$ to a nonpositive difference. Each cyclic class has at most $m$ members. At least $1/m$ of the counted mass has this upper constraint. Prepend one $E$ and append one $O$. The nonterminal part lies strictly below zero after its first step; its last point before the appended $O$ is $-b+\delta\in[-3a/4,-a/4]$. The final positive point belongs to $[a/4,3a/4]$. Distinct $m$ give disjoint first-passage events. Summing $\gg m^{-3/2}$ over these lengths proves the requisite probability without $V$.

For any $i\ge0$,
$$
 \mathbb E[(1+|S_i|)e^{S_i};\tau>i]\ll(1+i)^{-3/2}.               \tag{U2}
$$
Indeed impose $-S_i\in[r,r+1)$, $r\ge0$. For the first third of the increments the running maximum stays at most zero. For the last third, read in reverse, the partial sums $S_i-S_{i-j}$ are at least $-r-1$. O3 bounds the probabilities of these independent necessary conditions by $C/\sqrt i$ and $C(r+2)/\sqrt i$. After conditioning on both blocks, the middle block must end in an interval of length one; its maximum binomial atom is $O(i^{-1/2})$ and its lattice spacing is $\log3>1$. Summing with weight $(r+2)e^{-r}$ gives (U2), enlarging constants at small $i$.

Now $\mathbb E[V;N\le\tau\le2N]\ll N^{-1/2}$. For $i\le N/2$, conditioning at $i$ on survival and $S_i$ gives a further necessary survival probability at most $C(1+|S_i|)/\sqrt N$ to time $N-1$, by O3. Sum using (U2). For $N/2<i\le2N$ discard future conditions and sum $O(i^{-3/2})$ by (U2). Taking $K$ sufficiently large and applying Markov's inequality to this restricted expectation proves (U1).

## OP-U3. Concatenation, projection and the lower measure bound

Choose $N_j=\lceil\exp(j!)\rceil$ for all sufficiently large $j$ and concatenate independent fresh excursions conditioned on (U1) with $N=N_j$. A finite word has at most one parsing into completed blocks and one partial block: each block ends at its first strictly positive local log slope. At successive block endpoints the total $S$ increases by at least $a/4$ and at most $3a/4$. Within a block the local $S$ is nonpositive until the endpoint. Thus the endpoint slopes are unbounded. Compatible word residues define a ternary point since their odd counts tend to infinity, and every resulting point is in $X$.

For a prescribed binary prefix of total length $k$ with current block index $j$ and local elapsed time $r$, each completed block costs at most $C\sqrt{N_i}$ over its unconditioned word probability. In an uncompleted block with $r<N_j/2$, remaining inside the nonpositive half-line up to time $N_j-1$ is necessary. O3 bounds its continuation probability by $C(1+|S^{\rm loc}_r|)/\sqrt{N_j}$. Division by (U1) costs at most $C(1+|S^{\rm loc}_r|)$. For $r\ge N_j/2$ division alone costs $C\sqrt{N_j}$. An empty partial block costs one. In the early case $k\ge N_{j-1}$ once a block has finished, and
$\sum_{i<j}\log N_i=(1+o(1))\log N_{j-1}$.
In the late case $k\ge N_j/2$ and the same estimate includes $j$. Constants from early fixed blocks cause no asymptotic loss. Consequently the constructed binary measure obeys uniformly
$$
 \mu([w])\le\Pr(w)\, k^{1/2+o(1)}(1+j+(-S_k)_+).                 \tag{U3}
$$
Here $|S^{\rm loc}_r|$ is bounded by the indicated factor because every completed increment is between $a/4$ and $3a/4$.

At ternary depth $q$ stop prefixes exactly at their $q$th $O$. The current index satisfies $j=o(\log q)$ uniformly: a completed block of length at least $N_{j-1}$ has odd count at least $pN_{j-1}$ because its total log slope is positive. Throughout any admissible prefix $S_k\le O(j)$, and the occupation restriction gives $\sum_{i<k} e^{S_i}\le K j\exp(O(j))$. The absolute constants can absorb the finitely many initial block indices. Write $D(q)=o(\log q)$ for a nonnegative uniform bound on the log of this last quantity and on $S_k$, enlarged by a constant.

At fixed $k,q$ the carry in OP-B1 satisfies
$$
 0\le A/3^q=A'/C_k\le \tfrac12 e^{-S_k}\sum_{i<k} e^{S_i}
                \le e^{D(q)-S_k}.
$$
Its injectivity at fixed counts and its congruence determine at most $1+e^{D(q)-S_k}\le2e^{D(q)-S_k}$ possible words for a fixed ternary ball. To transfer (U3), note that $k=(q\log3-S_k)/b\le Cq(1+(-S_k)_+)$. For any fixed small $\varepsilon>0$, the factors $k^{1/2+o(1)}(1+j+(-S_k)_+)$ are at most $q^{1/2+\varepsilon+o(1)}$ times a fixed polynomial in $1+(-S_k)_+$. Sum the word mass times its multiplicity over all clocks $k$ with $S_k\le D(q)$. The residual exponential is $\exp((h-1)S_k)$; its exponent coefficient is positive and the $S_k$ are spaced by $b$ at fixed $q$. The sum with that polynomial is $O(\exp((h-1)D(q)))$, uniformly in the fractional lattice offset. Thus the ternary pushforward law $\nu$ satisfies, for each $\varepsilon>0$ and all sufficiently large $q$,
$$
      \sup_{z\in\mathbb Z_3}\nu(z+3^q\mathbb Z_3)
               \ll_\varepsilon 3^{-\theta q}q^{1/2+\varepsilon}.   \tag{U4}
$$
One may decrease the intermediate $\varepsilon$ to absorb all $q^{o(1)}$ factors. The infinite-script measure is well-defined by independent finite block laws, and its pushforward is supported on $X$ by the endpoint construction. The ultrametric mass distribution bound yields positive $g_{1/2+\varepsilon}$-measure. Taking a smaller positive $\varepsilon$ than $\gamma-1/2$ and using the divergent gauge ratio yields infinity for each $\gamma>1/2$.

Consequently any positive cube-root correction in Theorem S's family gives infinite measure on $X$. That theorem's exact positive threshold applies to a different prefix constraint. The present onset is a factor of $(\log(1/r))^{1/2}$ in Hausdorff gauge, and all statements here concern ternary targets rather than ordinary escape.
