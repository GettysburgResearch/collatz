# Uniform transport of the complete ordinary Sinai clock profile

**PROPOSED, source-qualified.** Let $y_j=U^j(n)$ be a nonperiodic positive odd Syracuse orbit, $J_j=3/2^{v_2(3y_j+1)}$, and $D_j=J_0\cdots J_{j-1}$ with $D_0=1$. Write $g_q(y)$ for the ordinary value of the depth-$q$ ternary Sinai density, as in [the low-ancestor and width bounds](../unsafe-return-weights/SINAI_LOW_ANCESTORS.md), commits `f0ad2cb` and `31d9fe3`. For all integers $k$ set
$$
 P_j(k)=\begin{cases}g_{j+k}(y_j)/D_j,&j+k\ge0,\\0,&j+k<0.\end{cases}
$$
Then $P_j$ increases coordinatewise to a bounded function $P$ on $\mathbb Z$ and
$$
 \sum_{j\ge0}\|P_{j+1}-P_j\|_\infty<\infty .
$$
In particular the convergence is uniform simultaneously over all incoming clocks. The limit tends to zero at negative infinity and is bounded away from zero on the nonnegative integers, using the [unit minorization](../native-pressure-20261118/MINORIZATION.md), commit `a367328`, for the latter conclusion. The vanishing at negative infinity sharpens to the quantitative tail bound by the variation series below. This describes a necessary profile if an ordinary orbit escapes.

Put $Z_j=\{z:U(z)=y_{j+1},\ z\ne y_j\}$, always taking odd positive sources. Every $z\in Z_j$ first enters the spine at $y_{j+1}$. The orbit is injective, so $Z=\bigcup_j Z_j$ is a reachability antichain of nonperiodic states. The width estimate (4) at the cited pin gives
$$
 \sum_{z\in Z}\sup_{q\ge1} g_q(z)/z\le C .
$$
The exact positive first-step recursion gives
$$
 R_{j,q}=g_{q+1}(y_{j+1})-J_j g_q(y_j)
  =\sum_{z\in Z_j}\frac3{2^{v_2(3z+1)}}g_q(z)\ge0 .
$$
Every coefficient divided by $y_{j+1}$ is at most $1/z$. Thus the preceding antichain bound yields $\sum_j\sup_{q\ge1} R_{j,q}/y_{j+1}\le C$. Also $R_{j,0}\le\sum_{a\ge1}3/2^a=3$, and $\sum_j1/y_j<\infty$ by the [simple-path reciprocal bound](CRITICAL_MOMENT.md). Hence $\sum_j\sup_{q\ge0}R_{j,q}/y_{j+1}<\infty$.

The ordinary affine product gives $y_j/D_j=n\prod_{i<j}(1+1/(3y_i))$, bounded above and below by positive constants depending on $n$. The new boundary coordinate $k=-j-1$ contributes $1/D_{j+1}$; all older coordinates increase by $R_{j,j+k}/D_{j+1}$. Consequently
$$
 \|P_{j+1}-P_j\|_\infty\le C_n\frac{1+\sup_{q\ge0}R_{j,q}}{y_{j+1}},
$$
which is summable. The initial $P_0$ is bounded by the same width estimate for the singleton $n$, together with its depth-zero entry. For $k<-j$, $P_j(k)=0$, so $\sup_{k<-j}P(k)\le\sum_{i\ge j}\|P_{i+1}-P_i\|_\infty\to0$. For every fixed negative $k$, its first depth-zero entry gives $P(k)\ge1/D_{-k}>0$. For $k\ge0$, $y_1$ is a ternary unit and the minorization gives $P(k)\ge P_1(k)=g_{k+1}(y_1)/D_1\ge c/D_1$.

Equivalently, define the integer phase of a source $x$ in the merger component by $b-j$ if $U^b(x)=y_j$; injectivity of the spine makes this independent of the meeting chosen. Put $r(x)=\prod_{i\ge0}(1+1/(3U^i(x)))^{-1}>0$. For each $k$ the limiting profile equals
$$
 P(k)=\sum_{x:\,\mathrm{phase}(x)=k}\frac{n\,r(x)}{x\,r(n)} .
$$
Indeed $P_j(k)$ includes exactly the sources in that phase already joined by clock $j$; each has the displayed weight by telescoping. Coordinatewise monotone convergence gives the formula. The bounded variation above therefore proves uniform convergence of these positive harmonic sums across all phase classes, including the clocks arbitrarily far ahead of the spine.

## Conservative mass and reversed transition probabilities

A positive harmonic mass on all nonperiodic integer branches follows without specifying a pointwise limit of $g_q$. Choose a common increasing sequence $N_i$ along which the bounded Cesàro means $N_i^{-1}\sum_{q<N_i} g_q(y)$ converge at every nonperiodic positive odd $y$, by a countable diagonal extraction. Call the limits $b(y)$. The width bound for singletons gives boundedness for fixed $y$, and unit minorization gives $b(y)\ge c$ whenever $3\nmid y$. At three-multiples $b=0$. Averaging the positive recursion and passing to the limit gives
$$
 b(y)=\sum_{Uz=y}J(z,1)b(z).
$$
Indeed the children form an antichain, and for $q\ge1$ the sum of the termwise suprema is at most $y\sum_{Uz=y}\sup_{q\ge1}g_q(z)/z<\infty$. The depth-zero terms are summable separately. This justifies the limit over the entire infinite child set.

Write $m(y)=r(y)b(y)/y$. Telescoping gives $m(y)=\sum_{Uz=y}m(z)$ exactly. For any reachability antichain of nonperiodic positive odd states, $\sum_y m(y)$ is bounded by the absolute width constant. On a nonperiodic component $C$, the numbers $m(y_j)$ therefore increase to a finite positive limit $m_C$ independent of anchor: any two anchors have a common tail, and $m(y_1)>0$. The sum of $m_C$ over all such components is bounded by the same constant, by choosing one late representative per component. These masses may depend on the common Cesàro subsequence.

On each positive-mass parent use the reversed transition probabilities $m(z)/m(y)$ for $Uz=y$. The mass defect relative to the true spine is summable even before normalizing,
$$
 \sum_{j\ge k}\sum_{z\in Z_j}m(z)=m_C-m(y_k).
$$
The probability of following the ordinary spine backwards from $y_j$ to $y_k$ is exactly $m(y_k)/m(y_j)$. Its limit as $j\to\infty$ is $m(y_k)/m_C$, tending to one as $k\to\infty$. This shows why a backward transition law with an atom on the whole old spine is compatible with the existing lower bounds on individual sibling masses. This conclusion is conditional on the existence of a nonperiodic component; it does not construct one.

Under Valbuena's prior canonical-trace theorem, the common subsequence in this construction is unnecessary. His depth density $\rho_q(v)=3^q\pi(v+3^q\mathbb Z_3)$ has the same normalization as $g_q(v)$. He proves convergence of its integer Cesàro averages, and his forward-component proposition already identifies the limit $L_C$ of the canonical trace divided by height along each divergent spine with the weighted component mean times $\log(4/3)/2$. The harmonic construction above and the existence of a component mass should therefore carry no independent priority claim. The uniform all-clock transport gives the additional identification
$$
 \lim_{K\to\infty}\frac1K\sum_{k=0}^{K-1}P(k)
   =\lim_{j\to\infty}\frac{b(y_j)}{D_j}
   =\frac{n}{r(n)}L_C .
$$
Indeed each fixed $P_j$ has positive-age Cesàro mean $b(y_j)/D_j$, and uniform convergence permits passage to $P$. The last equality uses $y_j/D_j\to n/r(n)$. This imports only the indicated source theorem for the identification; the uniform-profile proof above does not require it. [Valbuena, *Collatz basin densities and canonical traces from first-passage stabilization*, archived source `paper/tao-basin-densities.tex`, SHA-256 `d5c61f228ece84aae6d565c777de84089c016073df19d7b0e6974e1cfa2bb258`](https://doi.org/10.5281/zenodo.23025885)

## The empirical law at the age of a moving root

Use the [fixed-root canonical inverse empirical theorem](../native-pressure-20261118/CANONICAL-RETURN.md) at `b7b9d59`. Write $h=(2/3)b$ for its normalization of the ordinary canonical Cesàro trace, $\rho_q=(2/3)g_q$, and $\nu$ for the invariant product law on the compact dyadic and ternary state space. Suppose $j,Q\to\infty$ on a nonperiodic spine and $Q/j\to\lambda\in(0,\infty]$. Then
$$
 \frac{1}{Qh(y_j)}\sum_{q<Q}\rho_q(y_j)\ \longrightarrow\ (1-1/\lambda)_+ .
$$
Indeed this ratio is the mean of $P_j(k)$ over $-j\le k<Q-j$, divided by $b(y_j)/D_j$. Uniform profile convergence allows $P$ in the numerator. Its negative side tends to zero, its positive side has Cesàro limit $A=(n/r(n))L_C>0$, and the denominator tends to $A$. For bounded positive $\lambda$ each side contributes its proportion of the window times its corresponding limit; the same reasoning works at $\lambda=\infty$. In particular positive lower bounds on $h(y_j)/y_j$ do not imply uniformity of (1) of the fixed-root theorem at the age $Q=j$.

The moving-root empirical law itself has an explicit decomposition. Let $l=\min(j,Q)$ and start the canonical reverse chain at $y_j$. For each bounded continuous test $f$, the difference
$$
 \frac1Q\sum_{q<Q} f(X_q)
 -\frac1Q\sum_{i=j-l+1}^{j} f(y_i)
 -\left(1-\frac lQ\right)\nu(f)
$$
tends to zero in probability along any $Q,j\to\infty$. To see this, fix a large $K$ and couple the first $j-K$ steps to the true reversed spine by the event of following its transitions, of exact probability $m(y_K)/m(y_j)$. Its complement has probability at most $1-m(y_K)/m_C$, which tends to zero as $K\to\infty$. On this event the initial spine terms agree up to at most $K$ boundary terms. Any remaining $Q-j+K$ steps start at the fixed root $y_K$ with its canonical law by the Markov property. If that remaining length tends to infinity, apply the fixed-root empirical theorem; if it stays bounded its contribution divided by $Q$ vanishes. These alternatives suffice on every subsequence. Sending $K\to\infty$ gives the claim. Thus universal convergence is recovered at $Q/j\to\infty$. At $Q=j$ the empirical law follows the deterministic forward prefix.

This distinction is visible with one bounded clopen test. Take $f(v)=\min(v_2(3v+1),3)$ with value 3 at the exceptional dyadic point. Its $\nu$ mean is $7/4$. Along a nonperiodic spine, the ordinary product formula gives $\sum_{i<j}v_2(3y_i+1)\le j\log_2 3+O_n(1)$, since $y_j\ge1$ and the correction product is bounded. Hence at $Q=j$ the reverse empirical mean is at most $\log_2 3+o(1)$ in probability, strictly below $7/4$. At ratios $Q/j\to\lambda\in[1,\infty)$ the limiting upper bound is $7/4-(7/4-\log_2 3)/\lambda$. This failure of a uniform fixed-root conclusion is a necessary consequence of an escaping orbit and is consistent with the fixed-root empirical theorem.
