# Leading binary digits on distinct odd Collatz segments

**PROPOSED.** Every segment of N pairwise distinct positive odd Collatz states has a binary leading-digit law, uniformly in its start. At a range of digit lengths growing proportionally to $\log N$, the frequency of **each individual leading block** is asymptotic to the logarithmic length of its significand interval. In particular almost all these states have at least a constant times $\log N$ binary runs, with a power saving for the exceptional count. The quantitative exponent invokes the classical lower bound for a nonzero linear form in two logarithms. Section 2 also gives a finite inequality using only a rational approximation to $\log_2 3$. No exponent of escape or assumption of probabilistic parity is used.

## 1. Total angular error

Use the ordinary odd map $U(n)=(3n+1)/2^{v_2(3n+1)}$, extending $U(1)=1$ if needed. Let $n_j=U^j(n_0)$ for $0\le j<N$ and suppose these N states are distinct. Put $\theta_j=\{\log_2 n_j\}$ on the unit circle, and $\alpha=\log_2 3$. Then
$$
 \theta_{j+1}=\theta_j+\alpha+\epsilon_j\pmod1,
 \qquad \epsilon_j=\log_2(1+1/(3n_j)).
$$
The valuation subtracts an integer exactly. The total error over all transitions of this segment satisfies
$$
 E_N=\sum_{j=0}^{N-2}\epsilon_j
 \le \frac{1+\log N}{3\log 2}.
$$
Indeed $\log(1+x)\le x$, and distinct positive integers in sorted order are at least $1,2,\ldots$. All unmarked logarithms are natural. In particular the estimate applies uniformly to intervals anywhere along a nonperiodic positive orbit.

## 2. A finite discrepancy inequality

Define $D_N$ as the supremum over half-open circular arcs I of the absolute difference between their empirical frequency among the $\theta_j$ and their length. For any relatively prime integers p,q with $1\le q\le N$,
$$
 D_N \le \frac{2}{q}+2|q\alpha-p|+\frac{q(1+2E_N)}{N}.             \tag{1}
$$

Partition the segment into consecutive disjoint blocks of length q and a final remainder of length less than q. For a complete block beginning at a, compare the jth angle to $\theta_a+jp/q$, $0\le j<q$. Their circle distance is at most $|q\alpha-p|+E_a$, where $E_a$ is the sum of actual errors on transitions internal to that block. The comparison angles form a translated complete grid with spacing $1/q$. The grid frequency of any arc of length t differs from t by at most $2/q$, allowing for its endpoints. Enlarge or shrink I by the indicated distance on both sides. The proportion of actual points in I differs from its length by at most $2/q+2|q\alpha-p|+2E_a$; this remains valid if an enlargement fills the circle or a shrinking empties the arc. Sum after weighting each complete block by $q/N$, use $\sum_a E_a\le E_N$, and charge a possible discrepancy of one on the remainder. This proves (1).

Since $\alpha$ is irrational, arbitrarily large convergent denominators satisfy $|q\alpha-p|<1/q$. First fix one and then let N grow in (1). This proves $D_N\to0$ uniformly with no quantitative linear-forms input. It already gives the limiting frequency $\log_2(1+1/b)$ of each fixed k-bit leading block b on every nonperiodic positive odd orbit.

## 3. A power bound from a classical external theorem

For completeness state the precise number-theoretic dependency. There exist effective constants $K>0$ and $\tau\ge1$ such that
$$
 |q\log_2 3-p|\ge Kq^{-\tau}\qquad(q\ge1,\;p\in\mathbb Z).       \tag{2}
$$
For p nearest to $q\alpha$, apply the Baker–Wüstholz lower bound for a nonzero linear form in logarithms of fixed algebraic numbers to $q\log 3-p\log 2$. Nonvanishing follows from unique factorization, $p=O(q)$, and division by $\log 2$ is a fixed rescaling. Other p give no smaller distance. Small q may be absorbed in K. No numerical quality is assumed for the constants. An applicable source is A. Baker and G. Wüstholz, “Logarithmic forms and group varieties”, *J. reine angew. Math.* **442** (1993), 19–62. [DOI](https://doi.org/10.1515/crll.1993.442.19)

Let $q_i$ be consecutive simple continued-fraction denominators. The convergent inequality $|q_i\alpha-p_i|<1/q_{i+1}$ and (2) give $q_{i+1}<K^{-1}q_i^\tau$. Set $d=1/(\tau+1)$ and $Q=(N/(1+\log N))^d$. For large N take the first convergent denominator $q>Q$. Then $Q<q\le K^{-1}Q^\tau$, $q\le N$, and $|q\alpha-p|<1/q$. Equation (1) gives
$$
 D_N=O\!\left(\left(\frac{1+\log N}{N}\right)^d\right).         \tag{3}
$$
The implied constant depends only on the two fixed logarithms. At observation lengths $N=q_i^2$, (1) even gives $D_N=O((1+\log N)/\sqrt N)$ directly, along this sequence of lengths without (2).

## 4. Uniform leading words and run counts

For $k\ge1$ and $2^{k-1}\le b<2^k$, define the k-bit leading word by taking k leading binary digits and padding on the right with zeros if the integer is shorter. The word equals b exactly when
$$
 \theta_j\in\left[\log_2(b/2^{k-1}),\ \log_2((b+1)/2^{k-1})\right).
$$
The right endpoint 1 is identified with the end of the circle, with the half-open convention. The arc length $\ell_b=\log_2(1+1/b)$ is between positive absolute constants times $2^{-k}$. Consequently for every fixed $0<\kappa<d$, uniformly in all $k\le\kappa\log_2 N$, all b and all distinct segments,
$$
 \#\{j:\text{leading word equals }b\}
 =N\ell_b\left(1+O\!\left(N^{\kappa-d}(1+\log N)^d\right)\right).    \tag{4}
$$
For a given b and a physical bitlength below k, right padding determines at most one integer at that bitlength. Distinctness thus costs at most k−1 observations per bin when padding is forbidden. Relative to $N\ell_b\gg N^{1-\kappa}$ this also tends to zero. Each actual leading word in this growing range therefore occurs on every sufficiently long distinct segment.

Take $k=\lfloor\kappa\log_2 N\rfloor$ and any fixed $0<p<1/2$. The number of k-bit words with at most $p(k+1)/2$ runs of ones is at most
$$
 \sum_{i\le p(k+1)}\binom{k+1}{i}\le 2^{(k+1)H_2(p)}.
$$
Indeed each run contributes two distinct boundaries, and the last inequality follows from the binomial theorem with weights p and $1-p$. A prefix cannot have more runs than the entire source, even with trailing zero padding. By (4) each leading bin contributes $O(N2^{-k})$ observations, giving
$$
 \#\{j:r(n_j)\le p(k+1)/2\}
 = O_{\kappa,p}\left(N^{1-\kappa(1-H_2(p))}\right).              \tag{5}
$$
This uniform power saving applies to a logarithmically growing run threshold. The same leading-word law bounds any given family of k-bit prefixes by its cardinality times $O(N2^{-k})$.

**Scope.** Formula (1) gives a computable elementary bound for a proposed rational approximation and actual observation length. Formulae (3)–(5) use the cited two-logarithm theorem for all lengths. Leading-bit equidistribution is compatible with divergence. It does not determine low-order bits, the successive valuations, or joint independence between mantissa and valuation. A repeated positive cycle violates the distinctness hypothesis once its period is exceeded. The elementary signed-cut argument and capped-cycle census in the companion note do not use (2).
