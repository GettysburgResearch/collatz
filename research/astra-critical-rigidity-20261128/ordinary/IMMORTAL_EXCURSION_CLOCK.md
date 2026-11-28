# A linear physical clock with exponential error on the immortal positive-level law

Start the [positive-level transform](SURVIVOR_LOWER_GAUGE.md) at any fixed level $s\ge1$, with an arbitrary incoming integer offset. Let $J_r$ denote the level just after $r$ mixed letters, $J_0=s$, and $\tau_r$ their native clock. The direction transition at $j$ has probabilities $(j\pm1)/(2j)$. For absolute constants $C,c>0$, all sufficiently large $r$ depending only on $s$, and uniformly in the incoming offset,
$$
      \Pr(\tau_r>Cr)\le C_s e^{-c r^{1/3}},\qquad
      \frac1r\sum_{i<r}v_2(J_i)\longrightarrow1\quad\text{almost surely}.         \tag{1}
$$
The coefficient of the physical clock in (1) is an upper bound. No exact limiting clock speed is required.

## Occupation of the dyadic valuations

Put $f(k)=v_2(k)-1$ for $k\ge1$. The elementary factorial valuation formula gives $\sum_{k\le N}f(k)=-s_2(N)$, with $s_2$ the binary digit sum. Thus these partial sums are $O(\log(2+N))$. Define $W(0)=W(1)=0$ and
$$
       W(k+1)-2W(k)+W(k-1)=2k f(k),\qquad U(k)=W(k)/k\quad(k\ge1).
$$
Summation by parts gives $|W(k+1)-W(k)|=O(k\log(2+k))$, by bounding $\sum_{m\le k}m f(m)$. Therefore $|W(k)|=O(k^2\log(2+k))$, $|U(k)|=O(k\log(2+k))$ and $|U(k+1)-U(k)|=O(\log(2+k))$. For the direction kernel $Q$, the exact Poisson equation is
$$
                     Q U(j)-U(j)=f(j).
$$
At $j=1$ the zero-probability lower term is interpreted through $W(0)=0$. The martingale difference $U(J_{i+1})-QU(J_i)$ is bounded by $C\log(2+s+r)$ for $i<r$. Its partial sum $M_r$ obeys, for fixed $\delta>0$,
$$
             \Pr(|M_r|>\delta r)\le2\exp[-c_\delta r/\log^2(2+s+r)]
$$
by the bounded-increment martingale inequality.

The hyperbolic-sine transform from [the lower gauge proof](SURVIVOR_LOWER_GAUGE.md) also applies at direction times, starting at $s$: the initial factor is $\sinh(\theta s)/s$. With $H=\lceil r^{2/3}\rceil$ and $\theta=H/r$, it gives $\Pr(\max_{i\le r}J_i>H)\le C_s e^{-c r^{1/3}}$ for all large $r$. On its complement $|U(J_r)-U(s)|=O_s(r^{2/3}\log r)=o(r)$. Now $\sum_{i<r} f(J_i)=U(J_r)-U(s)-M_r$. For each fixed $\delta$ the probabilities of a deviation larger than $2\delta r$ are summable, proving the second assertion of (1). Taking $\delta=1/2$, for example, bounds $\sum_{i<r}v_2(J_i)$ by $3r$ outside an event of probability $C_s e^{-c r^{1/3}}$.

## From directions to native dates

At positive level $j$ let $b_j=v_2(3^j-1)\le 2+v_2(j)$. The number of native steps until and including the next mixed letter is conditionally dominated by $b_j+1+Z$, where $Z$ is geometric with success probability $1/2$ on $\{1,2,\ldots\}$. To verify this, when $v_2(a)<b_j$ both common letters reduce that valuation by one; at valuation at least $b_j$, at least one of the two fair common letters reduces it to $b_j-1$. Offset zero can be regarded as having infinite valuation. The transform preserves fairness of common letters, and the final choice of mixed direction changes no holding length. This is the physical holding argument of Leen. [Leen, *Quantitative synchronization of Collatz trajectories*, “Holding times and the level walk”](https://doi.org/10.5281/zenodo.23268755)

For $0<\theta<\log2$, the conditional exponential moment of the excess over $b_j+1$ is at most $\mathbb E e^{\theta Z}$ at each actual mixed epoch. Iterated conditioning and the exponential Markov inequality show that the accumulated excess is at most $C_1r$ outside an event of probability $e^{-c_1r}$. Combining with the occupation bound proves (1).

## A quantitative high-level trial within every late macroscopic time interval

There are absolute $c_0,\alpha>0$ such that, for all large integers $N$, an immortal positive excursion starting at a fixed level $s$ at any global date $m\le N^{1/4}$ has
$$
 \Pr\!\left\{\text{no global date }t\in[\sqrt N,N]\text{ has }
                j_t\ge c_0\sqrt{t\log\log t}\right\}
       \le C_s\exp[-c_s(\log N)^\alpha].                                \tag{2}
$$
This is uniform in its incoming integer offset. Use dyadic mixed epochs $r_i=2^i$ between $2\sqrt N$ and $N/(2C)$, with $C$ from (1). A union bound makes all corresponding physical end dates at most $m+Cr_i\le2Cr_i$ and at least $r_i\ge\sqrt N$, except with probability $C_s(\log N)\exp(-c N^{1/6})$.

Use an independent sequence of uniform random variables for the successive mixed directions, since the conditional probability of up is always $(J+1)/(2J)$ given prior history and holdings. Each direction increment dominates the fair sign obtained by thresholding the same uniform at $1/2$. The fair sums on disjoint mixed blocks $(2^{i-1},2^i]$ are independent. For small absolute $b>0$ and $m_i=2^{i-1}$ their probabilities of exceeding $b\sqrt{2^i\log i}$ are at least $c i^{-1/2}$ for all large $i$. For example, sum the binomial atom bound $c m_i^{-1/2}\exp(-C k^2/m_i)$ over the correct-parity integers $k$ from that threshold to that threshold plus $\sqrt{m_i}$. The bound follows from Stirling's inequalities for $k=O(\sqrt{m_i\log i})$. Choose $b$ small enough to absorb the absolute exponent constant. The positive starting level of each block means that any such large fair sum gives at least as large a final level. At a clock-good epoch this exceeds $c_0\sqrt{t\log\log t}$ for a small absolute $c_0$. The possible $i$ range has length $\asymp\log N$ with both endpoints of order $\log N$. The product of the independent failure probabilities is at most $\exp[-c(\log N)^{1/2}]$. No independence from the clock-good event is needed for the union bound. This proves (2).

The proof works with Leen's positive-level chain; it is separate from the full capacity law allowing returns to level zero. The quantitative uniformity in the entry offset and the starting-date bound in (2) are useful when summing over actual departure histories.
