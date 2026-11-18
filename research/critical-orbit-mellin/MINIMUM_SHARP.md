# The sharp quadratic tail of the least-predecessor law

Paper 146 already proves the full tail equivalent for the stationary Syracuse density, stronger than the stationary-density corollary below. Its real-offset and delayed-overlap estimates are material methodological precedents. [Prior-work comparison](PRIOR_WORK.md)

**PROPOSED.** In the notation of [the fixed-depth bound](MINIMUM_TAIL.md) and [the all-depth density transfer](../fixed-floor-shells/PREDECESSOR_MINIMA.md), there is an absolute constant $c>0$ such that
$$
 c\theta^2\le d(\theta)\le\theta^2\qquad(0<\theta\le1).
$$
The lower bound uses many depths in the central window of the critical tilted law. A restriction on the final letters makes overlaps between different depths summable.

Put $z=\log(1/\theta)$ and $q_*=z/\log(3/2^{4/3})$. For sufficiently large $z$ use the integers $q_*-\sqrt{q_*}\le q\le q_*$; smaller $z$ are covered by monotonicity and adjustment of the constant. At each such $q$ take $A=\lfloor(q\log3-z)/\log2\rfloor$, so $D=2^A/3^q\in(\theta/2,\theta]$ and $|A-4q/3|\ll\sqrt q$. Under iid letters of law $3\cdot4^{-a}$, the local probability of $S_q=A$ is $\asymp1/\sqrt q$ uniformly here. This follows from the negative-binomial formula in the fixed-depth proof by Stirling, with bounded standardized deviation. Condition on this total.

With constants $B,K$ independent of $q,A$, a positive fraction of words satisfy both
$$
 C\le B3^q,\qquad
 a_q+\cdots+a_{q-k+1}\le 8k/5\quad(K\le k\le q).
$$
Indeed the fractional moment argument of the fixed-depth proof only uses the local lower bound at $A$, so $B$ can make the first failure probability at most $1/4$. Unconditionally the suffix of length $k$ exceeds $8k/5$ with probability $\le e^{-ck}$ by a Chernoff bound, since the tilted mean is $4/3$. Conditionally this bound increases by at most $O(\sqrt{q/(q-k)})$ for $k<q$, by the local upper bound on the complementary prefix, or by $O(\sqrt q)$ for any $k$. Sum the first estimate through $k\le q/2$ and the second beyond $q/2$; choosing $K$ large makes this additional failure probability at most $1/4$ uniformly. Write $E_q$ for the union of the resulting ternary cylinders. Distinct words with this fixed total have distinct numerators $C$, and the first restriction bounds the number per residue by $B+1$. As in the fixed-depth proof,
$$
 \mu_3(E_q)\asymp 3^{-q}\binom{A-1}{q-1}\asymp \theta^2/\sqrt{q_*}.
$$

For two selected depths $r<q$ write $l=q-r$. On a given ternary cylinder $t\equiv t_0\pmod{3^r}$, the numerators of all possible longer marked words satisfy
$$
 0<C\le B3^q,\qquad C\equiv 2^At_0\pmod{3^r}.
$$
Thus they lie in a single progression of at most $B3^l+1$ terms. Set $k=\lfloor l/2\rfloor$, $J=1+\lfloor8k/5\rfloor$. For $k\ge K$ each possible longer numerator must decode at least $k$ letters with total valuation at most $J-1$. This property is determined modulo $2^J$. To decode from odd $C_j$ at depth $j$, take $a_j=v_2(C_j-3^{j-1})$ and $C_{j-1}=(C_j-3^{j-1})/2^{a_j}$. At these $k<q$ layers the previous numerator of any actual word is odd. If one starts with an odd uniform dyadic integer in place of $C_q$, each valuation has the law $\Pr(a=n)=2^{-n}$ for $n\ge1$, and conditional on that valuation the new odd quotient is uniform. This follows by subtracting the fixed odd constant from a uniform odd residue and stripping its exact power of 2. The valuations are therefore independent. For a fixed finite residue of precision $J$ the event of total at most $J-1$ depends only on those $J$ bits, since they certify the exact valuations and the parity of the final quotient. Even residues cannot be numerators. A Chernoff bound under this geometric law of mean 2 shows that at most $O(2^J e^{-c'k})$ residues modulo $2^J$ pass the test.

The progression has odd step and $2^J\ll3^l$, so each accepted residue occurs at most $O_B(3^l/2^J)$ times. The number of eligible longer numerators in the progression is consequently $O(3^l e^{-c''l})$. Each determines at most one longer ternary cylinder because $A$ is fixed at depth $q$. Dividing by $3^l$ proves
$$
 \mu_3(E_q\mid t\equiv t_0\bmod 3^r)\ll e^{-c''(q-r)}
$$
for every shorter residue, with a larger absolute constant for $k<K$. In particular $\mu_3(E_r\cap E_q)\ll\mu_3(E_r)e^{-c''(q-r)}$.

For $N=\sum_q {\bf1}_{E_q}$, summing the pair bound yields $\mathbb E N^2\ll\mathbb E N$, while the central window gives $\mathbb E N\asymp\theta^2$. Cauchy–Schwarz now implies $\mu_3(N>0)\gg\theta^2$. Every marked word witnesses the required strict ordinary inequality, proving the theorem.

The same bound holds as an ordinary lower frequency in each fixed odd dyadic class modulo $2^j$ in $[X,2X]$, uniformly for $C_jX^{-\gamma}\le\theta\le1$, with $\gamma=\log(3/2^{4/3})/\log3$. Indeed the entire finite union has period $3^{\lfloor q_*\rfloor}$ or a divisor, and this times $2^j$ is at most $X/2$ once $C_j$ is sufficiently large. CRT transfers at least a constant fraction of the uniform measure. Consequently the shell mean of $(t/m(t))^2$ is $\gg_j\log X$, and that of $(t/m(t))^s$ is $\gg_{j,s} X^{\gamma(s-2)}$ for $s>2$. Only the finite lower screen is asserted uniformly at this scale.

## Supercritical pressure tails

Let $\mathcal H_s$ be the sum of $J^s$ over all legal inverse words at a Haar ternary target, with $J=3^q/2^A$ and the empty word included. The [ordinary pressure law](../fixed-floor-shells/PRESSURE_LAW.md), FS-014 at `a3b1b79`, identifies this random variable as the limit in distribution of the ordinary first-hit pressure $H_s(t)$ on odd targets. For each $s>2$ its upper tail satisfies
$$
 \Pr(\mathcal H_s>u)\asymp_s u^{-2/s}\quad(u\ge2).
$$
For $s=2$ this argument gives a lower bound $c/u$ and an upper bound $C(1+\log u)/u$. The comparison with ordinary populations may equivalently use liminf and limsup frequencies with the same bounds, by applying weak convergence at strictly smaller and larger thresholds.

For the upper bound, under the tilted iid letter law $3\cdot4^{-a}$, an individual word has probability $3^q/4^A$ whereas its ternary legality probability is $3^{-q}=J^{-2}(3^q/4^A)$. The tilted walk $\log J$ has positive drift $\log(3/2^{4/3})$. Its expected number of visits to an arbitrary interval of length $\log2$ is uniformly bounded: stop on first entry; from any entry point a visit $n$ steps later requires the future increment over $n$ steps to be at most $\log 2$. Those probabilities decay exponentially in $n$ by the exponential moment and positive drift. Hence the expected number of legal words with $R\le J<2R$ is $O(R^{-2})$, uniformly in $R>0$. Also the maximum $J$ has upper tail $O(R^{-2})$ for $R\ge1$, either by summing this bound or by FS-010.

Take $M=u^{1/s}$. The pressure from words with $J\le M$ has expectation $O_s(M^{s-2})$ for $s>2$, by summing the dyadic estimates down to zero. At $s=2$, the contribution from $1\le J\le M$ is $O(1+\log M)$; the contribution below 1 is bounded in expectation by the finite mean of $\mathcal H_{3/2}$ from FS-014. Markov's inequality combined with the tail of the maximum proves both upper bounds. The quadratic lower bound for the maximum above immediately gives the pressure lower bounds. For $s>2$, $\mathcal H_s$ has finite positive moments exactly in orders below $2/s$; at $s=2$ the threshold is 1 and its mean is infinite. These tail comparisons involve the limiting law. The exact ordinary pointwise escape criterion and its nonperiodic component obstruction were previously identified in [PR 140, Q2–Q5](https://github.com/GettysburgResearch/collatz/blob/6bee3183ff7f29f2e20ca88ab94bc7745c1af602/research/novel-swarm-20261030/pass3/ORDINARY_BOUNDARY.md).

### Critical pressure has a weak first moment

In fact $\Pr(\mathcal H_2>u)\asymp1/u$ for $u\ge2$. Put $f(t)=\mathbb E\min(\mathcal H_2,e^t)$. The bounded-interval occupation estimate just proved gives $f(t)\ll1+t^+$: count words with $J\le e^{t/2}$ by their truncated expected pressure, and bound the remaining clipped pressure by $e^t$ times the probability of a larger $J$. For $t<0$ the trivial bound suffices.

At a ternary target the exact recursion splits by the first letter $a$. It contributes $W_a\mathcal H_2((2^a\alpha-1)/3)$ where $W_a=(3/2^a)^2$, whenever that inverse is integral, in addition to the empty word of weight 1. Every letter is legal on one class of Haar measure $1/3$, and conditional on this class its new target is Haar. Subadditivity of clipping, followed by expectation, gives
$$
 f(t)\le1+\sum_{a\ge1}(W_a/3) f(t-\log W_a).
$$
The weights $W_a/3=3\cdot4^{-a}$ sum to one. Let $S_n$ be the sum of $n$ iid increments $\log W_a$ under this law, $S_0=0$, and $\tau$ the first $n$ with $S_n\ge\log2$. The positive mean and exponential moment give $\Pr(\tau>n)\le\Pr(S_n<\log2)\ll e^{-cn}$. Iterating the inequality to the bounded stopping time $\tau\wedge n$ yields $f(t)\le\mathbb E(\tau\wedge n)+\mathbb E f(t-S_{\tau\wedge n})$. On $\tau\le n$ the terminal term is at most $f(t-\log2)$. On $\tau>n$ its contribution tends to zero for each fixed $t$ by the linear growth bound and Cauchy–Schwarz, since $\mathbb E S_n^2=O(n^2)$ and the event has exponentially small probability. Consequently $f(t)-f(t-\log2)\le\mathbb E\tau$ uniformly in $t$. The left side dominates $(e^t/2)\Pr(\mathcal H_2\ge e^t)$ by the definition of clipping. This proves the stated sharp upper bound without requiring independence of different inverse branches.

## Consequence for the Sinai density

Let $g$ be the Haar density of the stationary geometric Syracuse offset, with the ordinary first-letter transfer $g(\alpha)=\sum_a (3/2^a){\bf1}_{a\ {\rm legal}}g((2^a\alpha-1)/3)$ holding Haar-almost everywhere as in [the critical norm proof](../unsafe-return-weights/SINAI_CRITICAL_NORM.md). Then $\Pr(g>u)\gg u^{-2}$ uniformly for $u\ge2$. Choose $a_0>0$ such that $\Pr(g>a_0)>0$. At the previous selected depths take $\theta=a_0/(2u)$ for large $u$ and keep one marked word per distinct cylinder. Conditional on a marked cylinder, the full inverse source after its word is Haar. Impose the additional requirement that $g$ there exceeds $a_0$. This retains a fixed fraction of each depth's marked mass, and iterating the positive transfer gives $g(\alpha)\ge J a_0>u$ there, outside null sets. Intersections remain bounded by the original summable cross-depth estimates. The same second-moment argument yields the asserted bound. This removes the logarithmic loss from a single central-depth lower bound. It does not identify a limit for $u^2\Pr(g>u)$.
