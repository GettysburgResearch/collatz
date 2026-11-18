# Ternary pole constraints on a fixed ordinary escaping orbit

**PROPOSED, source-qualified.** Let $K$ be the existing [coefficient-record limit set](../profinite-orbit-averages/RECORD_LIMITS.md). At depth $q$ its legal reverse valuation words satisfy $P_i=3^i/2^{a_1+\cdots+a_i}\ge1$ for every $i\le q$, where letters are read from target to source. Denote the union of their depth-$q$ cylinders by $K_q$. The compact set $K=\bigcap_qK_q$ already has known ternary dimension $H_2(\log_32)$ and excludes positive odd integers. Below $g_q=L^q1$ and $h$ is the [canonical pointwise trace](../native-pressure-20261118/EVERY-DEPTH.md), normalized so $g_q\to3h/2$ everywhere in the extended sense.

## A uniform lower bound on every finite record cylinder

For every legal reverse prefix from a ternary target $t$, with partial multipliers $P_i$ defined above, one has
$$
 g_q(t)\ge c\sum_{i=1}^q P_i,\qquad h(t)\ge c\sum_{i=1}^q P_i .
$$
At letter $a_i$ replace it by either $a_i+2$ or $a_i+4$ so the new parent is a ternary unit. Indeed the three consecutive choices of the right parity have parents in the three different classes modulo three, since four generates the principal units modulo nine. The replacement multiplier is at least $1/16$ of the original. All such first-departure words for different $i$ are disjoint. After that letter, the remaining unrestricted inverse words have total weight $g_{q-i}$ at a unit, bounded below absolutely by [uniform minorization](../native-pressure-20261118/MINORIZATION.md), including depth zero. Summing yields the first inequality. For the second, extend the disjoint prefixes to any common larger depth, use the same lower bound and take its pointwise limit. Thus $g_q,h\gg q$ throughout $K_q$, and $K$ lies entirely in the stationary trace pole set. Its rational members are constrained by the [rational pole classification](RATIONAL_PHASE_TRACE.md).

## Quantitative approximation and positive-integer repulsion

Every depth-$q$ ball in $K_q$ meets $K$: extend its admissible reverse word by the constant infinite valuation-one tail, whose phase is $-1$. The resulting point is $F_w(-1)$ for the forward affine word $F_w$ with that prefix. It belongs to $K$, and its stationary ternary local dimension is the minimum $\log_3 2$. In particular $K_q$ is exactly the union of depth-$q$ balls meeting $K$.

If $n>0$ is odd, a length-$q$ critical path interpreted at $n$ consists of actual positive ordinary odd numerators. Writing $x_0=n$ and $x_i$ for its backward states gives
$$
 P_i x_i=n-\tfrac13\sum_{j=1}^iP_j.
$$
All states are at most $n$. They are distinct: a repetition forces $n$ onto the forward cycle, and then the final full lap into $n$ gives $P_d=J_C<1$ at its period $d$, contrary to criticality. Therefore $q\ll n^\eta$ by [translated orbit packing](PRIOR_WORK.md), where $\eta=h_0-\gamma<1$ denotes any admissible power-saving exponent with $h_0=H_2(\log_3 2)$. Consequently
$$
 \operatorname{dist}_3(n,K)\ge3^{-C n^\eta}.
$$
The direct positive-numerator identity also gives $q<3n$ without the packing input. The maximum depth can be computed by a finite tree with the critical-prefix cutoff.

Now let $t=y_j$ be a coefficient record at odd depth $j$ from a fixed nonperiodic positive odd $n$. Its own reverse word has all $P_i\ge1$. The explicit rational minimum-dimension pole $F_w(-1)\in K$ satisfies
$$
 |t-F_w(-1)|_3=3^{-j-v_3(n+1)}.
$$
Indeed $t-F_w(-1)=3^j2^{-A}(n+1)$. Since $y_j\le(n+1)(3/2)^j$, this gives $\operatorname{dist}_3(t,K)\ll_n t^{-\log(3)/\log(3/2)}$. Both bounds concern a growing ordinary integer; neither excludes its approach to $K$.

The same compact pole set attracts ordinary *height* records, even at logarithmically increasing depth. If $t=y_j$ exceeds all earlier values, any last $i\le j$ steps have $t=P_i y_{j-i}+F_i$, $0\le F_i\le(3/2)^i-1$. Hence $P_i\ge1-F_i/t$. If $P_i<1$, the rational denominator gap gives $1-P_i\ge1/(3^i+1)$. Thus $P_i\ge1$ whenever $t>((3/2)^i-1)(3^i+1)$, so $t\in K_q$ up to $q\le j$ in this range. Using the [fixed two-logarithm lower bound](../binary-run-occupancy/MANTISSAS.md) improves this: for $P_i<1$ one has $1-P_i\gg(1+i)^{-B}$ with an absolute $B$, by the bound on $|i\log3-A\log2|$ when the form is near zero. Therefore every sufficiently large height record from fixed $n$ lies in $K_q$ with
$$
 q=\left\lfloor\frac{\log t-(B+2)\log\log t}{\log(3/2)}\right\rfloor.
$$
The starting-height bound above ensures $q\le j$ eventually. This yields the same power of ternary approximation up to polylogarithmic factors for height records.

## A real-offset Lyapunov potential for the full empirical phase law

Let $F_w$ be the nonnegative real affine offset of the forward word $w$, with legality tested only in $\mathbb Z_3$ at its indicated endpoint. Define
$$
 G(t)=1+3\sup_{w\ {\rm legal\ at}\ t} F_w
 =1+\sup_w \sum_{i=1}^{|w|}P_i,\qquad \mathcal U=\{G=\infty\}.
$$
The empty word is allowed. The equality follows by affine composition in inverse-prefix order. The function is Borel and lower semicontinuous as a supremum over locally constant truncated-word observables. For every legal forward edge $s\mapsto t=(3s+1)/2^a$ of multiplier $J=3/2^a$ it obeys
$$
 G(t)\ge1+J G(s).
$$
This inequality includes the positive additive term at *every* edge of an actual ordinary trajectory. At every positive ordinary integer $t$, even or odd, $G(t)\le1+3t$ because every legal word there has positive ordinary starting numerator. By the sibling inequality above, $G(t)\ll1+h(t)$ at every ternary phase.

The set $\mathcal U$ has exactly the same ternary Hausdorff dimension $h_0$ as $K$. For the lower bound $K\subset\mathcal U$. For the upper bound, unbounded prefix sums force arbitrarily large $i$ at which some legal prefix has $P_i\ge i^{-2}$; otherwise the sum of the small terms and the finitely many exceptional depths is uniformly bounded, since $P_i\le(3/2)^i$. Such a prefix has positive valuation total at most $i\log_2 3+2\log_2 i$. There are at most $\binom{\lfloor i\log_2 3+2\log_2 i\rfloor}{i}=3^{(h_0+o(1))i}$ such words, each on one depth-$i$ ball. The limsup-cover bound gives dimension at most $h_0$. Its rational elements are exactly the poles classified in [the rational trace theorem](RATIONAL_PHASE_TRACE.md): it is contained in the pole set, every negative cycle belongs to $\mathcal U$ by its growing lap multiplier, and $\mathcal U$ is forward invariant.

Every subsequential empirical ternary phase law $\nu$ of a fixed escaping ordinary positive orbit assigns **positive mass** to $\mathcal U$. If the associated stationary phase/transition process is ergodic, $\nu(\mathcal U)=1$. For a quantitative version, let $(s,a,t)$ denote a transition in any limiting empirical joint law, $J=3/2^a$. Its two phase marginals equal $\nu$ and $E\log J\ge0$: the actual exponent sum is $N\log_2 3+\log_2(y_0/y_N)+O(1)$ by the simple reciprocal-product bound, so the exponents are tight with limiting mean at most $\log_2 3$. We have
$$
 \log(3/2)\,\nu(\mathcal U)
 \ \ge\ E\log J+\int_{\mathcal U^c}-\log(1-1/G(t))\,d\nu(t).
$$
There is no boundary flow between $\mathcal U$ and its complement by forward invariance and stationarity. On the finite part,
$$
 \log J-\log(1-1/G(t))\le\log G(t)-\log G(s).
$$
A unit target has $G(t)>1$. To integrate without assuming integrability of $\log G$, take a stationary Markov chain with this transition law on the finite part, truncate the nonnegative loss at a fixed constant, and telescope to time $N$. The right hand side divided by $N$ tends to zero in probability by stationarity and finiteness of $\log G$. The left average converges to its invariant conditional expectation by the ergodic theorem, since the exponent has finite first moment. Thus its mean is at most zero. Monotone convergence removes the loss truncation. On the infinite part bound $\log J$ above by $\log(3/2)$, proving the stated inequality; the loss is strictly positive on the finite part. This proves the positive-mass and ergodic assertions. It forces a singular component on a fixed set of dimension strictly below one in *every* empirical limit, without requiring positive exponential real growth or selecting only record times. A fixed-start proof that these laws avoid $\mathcal U$ would exclude escape. Pointwise finiteness at every ordinary state does not imply such avoidance under weak convergence.
