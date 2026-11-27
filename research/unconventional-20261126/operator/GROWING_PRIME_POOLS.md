# Growing adaptive prime pools on actual native segments and numerical records

**Status.** Proposed quantitative ordinary theorem. The elementary prime-power return identity C2 and the weak-$L^1$ summation of [the polynomial cofactor theorem](../renewal/POLYNOMIAL_COFACTORS.md) give absolute finite-segment bounds. The prime pool may be selected after the whole segment is known. Its cardinality can grow.

Fix a nonempty finite $Z\subset\mathbb Q\cap\mathbb Z_2$ with common positive odd denominator $D$, and $0<\epsilon<1$. A mark $x$ is exceptional for $z$ and a pool $S$ if $Y=D(x-z)\ne0$ and $|Y|\prod_{\ell\in S}\ell^{-v_\ell(Y)}<|Y|^{1-\epsilon}$. At most $|Z|$ zero cases occur on any simple segment and can be omitted. Constants may depend on $\epsilon,Z,D$ and on any required fixed bilateral precision. They are independent of the source and sizes of the selected primes in the native finite-segment bound.

## OP-G11. A quantitative fixed-source roughness theorem

On any $N$ consecutive **distinct** ordinary native states, for a single pool of $r\ge1$ primes the number of marks exceptional for some nonperiodic shift in $Z$ is
$$
 O\!\left(\sqrt N+r+\frac{r\log(2r)\,N}{\log(2N)}\right).
$$
The same bound holds for arbitrary shifts when counting any exceptional pair lacking the following protection: $z$ is genuinely periodic and the actual native word agrees with its literal periodic itinerary on any prescribed **fixed** number of clocks in both directions around that hit. For a period with an odd letter the required native width can ensure any fixed dyadic and ternary precision. The all-even phase $0$ gives just the native/dyadic conclusion. An empty pool has no exceptions.

For one shift $z$ and prime $\ell$, on its unprotected nonzero times let $V_\ell(t)=v_\ell(D(x_t-z))\log_2\ell$. At each threshold $u>0$ the count with $V_\ell\ge u$ is at most $C_b(1+N/u)$, where $b$ denotes the required bilateral width. For $u$ below a fixed constant the estimate is trivial. Otherwise group hits with successive gaps less than $c u$, where $c\log_2 3<1/2$. For consecutive hits the [exact integer return identity C2](../renewal/SHIFTED_COFACTORS.md) has an integer divisible by $\ell^{\lceil u/\log_2\ell\rceil}$ and bounded by $C_Z3^{\rm gap}$, so it vanishes. The intervening native word is a genuine return to $z$. There are $O(1+N/u)$ groups. They are singletons for nonperiodic $z$. For periodic $z$, all but $O_b(1)$ times per group have the protected bilateral itinerary; a group formed from unprotected hits alone therefore has only $O_b(1)$ of them. Constants are uniform over the primes.

Remove the $M=\lceil C_b\rceil$ largest values per prime on the unprotected set for this $z$, costing $Mr$ clocks. On the rest $\#\{V_\ell\ge u\}\le C_bN/u$ for all $u>0$. For any $Q>0$ the number of remaining times with $\sum_{\ell\in S}V_\ell\ge Q$ is $O_b(r\log(2r)N/Q)$. First remove the times with some $V_\ell>Q$ by the single-prime tails. Values below $Q/(2r)$ then contribute at most $Q/2$ in total at a time. For each prime, the sum of the remaining medium values in $[Q/(2r),Q]$ is at most $C_bN(1+\log(2r))$, by integrating its tail and including the lower threshold times their count. Summing and dividing by $Q/2$ proves the claim. Finally at most $\lceil\sqrt N\rceil$ distinct positive integers in the segment have $x_t+1<\sqrt N$. On all remaining clocks $\epsilon\log_2|D(x_t-z)|\ge c_\epsilon\log_2 N$ for large $N$. Use this $Q$ and sum the fixed set of shifts. This proves the displayed bound, uniformly over adaptive pools without the Subspace Theorem.

In particular, on a **hypothetical** fixed escaping ordinary path choose as $Z$ any finite set of states of that very path. They are nonperiodic under this hypothesis. For any sequence of pools with $r_N\log(2r_N)=o(\log N)$, the exact prefix conclusion is
$$
 \frac1N\#\left\{t<N:\ R_{S_N}\big(D(x_t-z)\big)\ge
 |D(x_t-z)|^{1-\epsilon}\ \text{for every }z\in Z\right\}\longrightarrow1 .
$$
At horizon $N$ this uses the same chosen $S_N$ for all $N$ comparisons.
For one fixed shift and one prime the exceptional count is $O(N/\log(2N))$. There is no growth-rate assumption. The finite-segment bound also applies to simple paths in the known basin.

At positive lower exponential growth $\liminf_t\log(x_t+1)/t>0$, the nonperiodic conclusion permits $r_N\log(2r_N)=o(N)$. Discard $t<\delta N$ and take $Q=c_\delta N$ on the rest. The bound above gives $O_\delta(r_N\log(2r_N))$ exceptional clocks in addition to that discarded portion. Divide by $N$ and let $\delta\downarrow0$. If $p_t/t\to d$ for the cumulative odd count $p_t$, the same density-one conclusion holds for any fixed shifts whose periodic frequencies differ from $d$, provided $r_N\log(2r_N)D_N=o(N)$ where $D_N=1+\max_{t\le N}|p_t-dt|$. Indeed comparison at the ends of a periodic group bounds its span by $O_Z(D_N)$; this multiplies the per-prime tail constant and the removed-maximum count by $O_Z(D_N)$. These conclusions do not assert the native $\log_3 2$ bound for all resonant periodic shifts and growing pools.

## OP-G12. Square-root budget with growing pools in the compulsory height law

For the notation and protected signed edges of [OP-G9–G10](ROUGH_LOG_GATES.md), the unprotected exceptional coefficient-record roof through $N$ clocks is
$$
                O\!\left(1+\sqrt{N r_N\log(2r_N)}\right)
                   \qquad (r_N\ge1).
$$
Here the fixed trajectory's initial-height constant is allowed. Indeed the single-prime tail $C_b(1+N/u)$ remains valid when the index set consists of coefficient-record marks unprotected for a given $z$. Use the same short-gap groups at valuation threshold $u$. As proved in OP-G9, two consecutive marks in a group force $z$ to be a negative signed cycle record phase, and all but boundedly many end marks have the required incoming and outgoing labels and three pairs of matched local coordinates. For all other $z$ the groups are singletons. Thus the identical weak-tail argument applies. Split at log height $H=\sqrt{N r_N\log(2r_N)}$. The lower marks together cost at most $H+O_{x_0}(1)$ in record roof. On the remaining marks take $Q=c_\epsilon H$: the unprotected count is $O(r_N+r_N\log(2r_N)N/H)$ and each roof is bounded. For $r_N\le N$ the linear term is absorbed in $O(H)$; for $r_N>N$ the whole roof is already $O(N)$. This proves the uniform estimate.

Consequently for horizons with $A_N/\sqrt N\to\infty$ the support statement in OP-G10 remains valid whenever $r_N\log(2r_N)=o(A_N^2/N)$. Positive log-peak speed allows nearly linearly many primes in this precise sense. For a single escaping ray, [the total-variation record discrepancy](GATE_SUSPENSION.md) changes coefficient-to-numerical log-threshold weights by bounded total mass. Charging every numerical-only mark as unprotected therefore preserves this estimate for that ray's numerical pre-gates. This gives no uniform rate for the global sum over distinct components.
