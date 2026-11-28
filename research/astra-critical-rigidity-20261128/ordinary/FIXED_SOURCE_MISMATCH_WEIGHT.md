# A diverging height cost at actual mismatch dates of one ordinary orbit

**PROPOSED written theorem.** Let $x_0,x_1,\ldots$ be the odd states of any **fixed** noneventually periodic positive integer Collatz orbit, with native odd valuations $e_j=v_2(3x_j+1)$. Write $\gamma=\log_2 3$, $\beta=\gamma-1$, and fix
$$
                 0<a<\frac{1-\beta}{\beta}.
$$
In particular $a=1/2$ is allowed. For $1\le\ell\le ap$, let $D(p,\ell)=\{0\le t<p:e_t\ne e_{t+\ell}\}$. Then
$$
 \lim_{p\to\infty}\inf_{1\le\ell\le ap}
   \frac{1}{p}\sum_{t\in D(p,\ell)}
         \log_2\big[(x_{t+1}+1)(x_{t+1+\ell}+1)\big]=+\infty.            \tag{1}
$$
These weights involve only the actual two states **immediately after each unequal departure**. In particular, with
$W(n)=\max_{0\le t\le n}\log_2(x_t+1)$,
$$
 \inf_{1\le\ell\le ap}
       \frac{\#D(p,\ell)\,W(\lfloor(1+a)p\rfloor)}p\longrightarrow\infty .
                                                                            \tag{2}
$$
If the fixed orbit has a polynomial upper bound on its odd states, (2) implies $\inf_\ell\#D(p,\ell)\log(p+2)/p\to\infty$. No polynomial growth assumption enters (1) or (2). At lag one these are statements about changes in the actual sequence of valuations.

## Partitioning one observed comparison at its own mismatches

Compare trajectories from $x_0$ and $x_\ell$. They cannot meet at a common odd clock since the supplied orbit has no repeated state. In the notation of [the exact endpoint theorem](EXACT_ARC_ENDPOINTS.md), $H_0+h_p\le2\log_2(x_0+1)+\beta(1+a)p$, by the forward rise bound on each shifted state. Since $\beta(1+a)<1$, fix $\epsilon>0$ so that $\delta=1-\epsilon-\beta(1+a)>0$.

Mark the post-mismatch dates strictly inside $(0,p)$, in increasing order $u_1<\cdots<u_N$. A possible post-mismatch at date $p$ is charged as part of the last segment. Fix an arbitrary integer $m\ge1$. For each of the $m$ classes of mark indices modulo $m$, split the entire open interval from 0 to $p$ at the marks in that class. Each resulting path has at most $m$ mismatches. Between successive selected marks there are exactly $m$. The initial piece has at most $m$, and the final piece includes at most $m-1$ omitted interior marks plus the possible terminal mismatch. If the class contains no interior index, the whole interval likewise has at most $m$ mismatches.

Summing the uniform finite estimate (2) of the exact endpoint theorem over these $m$ complete partitions gives
$$
 m(1-\epsilon)p\le
 m(H_0+h_p)+\sum_{j=1}^N(H_{u_j}+h_{u_j})
                     +C(m,\epsilon)(N+m).                               \tag{3}
$$
The $m$ partitions have exactly $N+m$ segments in total. Each interior mark is used once as an ending boundary and once as a starting boundary, and the two supplied global boundaries occur once per partition. This is the open-interval counterpart of [the cycle lane's marked-window summation](../cycles/MISMATCH_EVENT_HEIGHT.md).

If (1) fails, take a sequence of lengths and lags on which the total weighted cost is at most a fixed multiple of $p$. Its interior dates are distinct, and the positive integers $x_{u_j}$ are distinct along the fixed orbit. Hence the sum of their logarithmic weights is at least $\log_2((N+1)!)$, which forces $N=o(p)$. For fixed $m$, divide (3) by $p$ and take the lower limit along the sequence. The normalized event weight is at least $m\delta$. Now let $m\to\infty$ to contradict the fixed upper bound. Each actual post-mismatch weight is at most $2W(\lfloor(1+a)p\rfloor)$, which proves (2). The argument applies to every supposed violating choice of lags and therefore gives the stated uniform infima.

## Local separation among many factors of the supplied trajectory

The same estimate holds uniformly for two length-$p$ factors starting at $0\le i<j$ with $i+j\le ap$. Use the paths from $x_i,x_j$. The two global endpoint logarithms are then at most $2\log_2(x_0+1)+\beta(i+j+p)$, leaving the same positive margin. The first state's interior marked values are still distinct regardless of the choice of $i,j$. Thus all pairs of distinct valuation factors starting at dates $0,\ldots,\lfloor ap/2\rfloor$ have Hamming distance whose product with $W(\lfloor(1+a)p\rfloor)/p$ tends to infinity uniformly. This provides a linear-sized separated family wholly inside an explicitly bounded initial segment.

If $\log(x_t+1)=o(t)$, one may use any fixed initial-window multiplier $A>0$ instead: when $0\le i<j\le Ap$, all four endpoint heights are $o(p)$ uniformly. For a polynomially bounded orbit, at every fixed $B>0$ the valuation language has a collection of mutually separated length-$p$ factors with pairwise Hamming distances greater than $Bp/\log(p+2)$ whose cardinality divided by $p$ tends to infinity. Indeed each fixed $A$ gives $\lfloor Ap\rfloor+1$ such factors in the initial $(A+1)p$ letters, and $W(\lfloor(A+1)p\rfloor)=O(\log(p+2))$ there. Taking the lower limit first and then arbitrary $A$ proves the cardinality assertion. These refinements retain the physical distinctness and actual height hypotheses of (1).

## Moving periodic words and finite circle partitions

Take $p=2L$, $\ell=L$, and the actual valuation prefix $e_0,\ldots,e_{3L-1}$. If a supplied comparison word $v_0,\ldots,v_{3L-1}$ has at most $B$ mismatches with its own lag $L$ on the first $2L$ dates and differs from the actual prefix at $E$ positions, then
$$
                         \#D(2L,L)\le B+2E .                               \tag{4}
$$
An actual discrepancy has a template discrepancy or an error at one of its two positions. Also $W(3L)=O_{x_0}(L)$ by the forward rise bound. Thus, uniformly over all such templates with **fixed** $B$,
$$
                    \frac{E\,W(3L)}L\longrightarrow\infty .               \tag{5}
$$
This applies even when the template changes completely with $L$. In particular it applies to three copies of an arbitrary length-$L$ word, whose internal factor complexity can be as large as its length permits. The asymptotic cost is measured at the ordinary states of the fixed source.

For an explicit nonperiodic class of templates, let $v_t$ be the label of $\rho+t\alpha\pmod1$ in any circle partition by intervals with at most $b$ boundary points. One may choose arbitrary labels and boundary conventions. If $a'/L$ is reduced and $|\alpha-a'/L|\le L^{-2}$, a discrepancy at lag $L$ requires $\rho+t\alpha$ to be within circular distance $1/L$ of at least one boundary. For $0\le t<2L$, the exact grid point $\rho+ta'/L$ is within $2/L$ of this angle. There are at most seven grid points within circular distance $3/L$ of any fixed boundary, counting coincident endpoints conservatively. The $L$-grid is traversed twice, so $B\le14b$ in (4). For small $L\le6$, the trivial $2L$ bound also gives this claim when $b\ge1$. For $b=0$ the template is constant. Every irrational rotation has infinitely many such reduced approximants by the usual continued-fraction bound. The intercept, endpoints, labels and rotation number may also vary with $L$, as long as the displayed hypotheses hold. Formula (5) applies uniformly. The same proof with a growing boundary count gives the tradeoff $(E+b)W(3L)/L\to\infty$ and retains (5) whenever $bW(3L)/L$ stays bounded. Under polynomial orbit height it gives $E\log(L+2)/L\to\infty$ on these scales.

This application uses ***odd valuations*** as letters. The raw shortcut parity encoding is a different word. Weaver's 19 November manuscript already proves that an aperiodic signed rational shortcut parity word has superlinear *global* factor complexity. Consequently an exact finite-interval rotation coding, or an exact fixed positive-integer-valued interval coding expanded by the bounded nonerasing substitution $e\mapsto10^{e-1}$, is already excluded. The conclusion here is the increasing finite-prefix Hamming error (5), uniform in the supplied moving template and measured against the actual source height. [Weaver, *Finite descent and superlinear factor complexity in rational Collatz dynamics*, Theorem and Corollary in §1](https://rstation.ai/problems/collatz/papers/173/v1)

[Exact finite replay](check_mismatch_partitions.py) · [Integer controls](MISMATCH_PARTITION_CONTROLS.json). The checker exhausts all post-mismatch subsets through length nine, verifies the boundary multiplicities on direct ordinary trajectories, and checks the nearby-grid and corruption inclusions using exact fractions. Its rotating slopes are rational finite controls. The unbounded limit statements are proved above.
