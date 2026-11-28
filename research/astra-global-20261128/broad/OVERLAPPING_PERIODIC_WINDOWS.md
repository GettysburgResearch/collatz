# The union of all long, short-period parity windows

**PROPOSED, written proof.** Let $x_t$ be a positive non-eventually-periodic integer shortcut orbit, $B_t=\log_2(x_t+1)$. Fix $\delta>0$ and any function $f:\mathbb N\to[0,\infty)$ with $f(L)/L\to0$. Mark every time belonging to at least one parity subword $[a,a+L)$ of length $L\ge\delta B_a$ that has a period $1\le p\le f(L)$. Subwords may overlap, and the periodic word and its period may change with every window. If $M(t)$ counts marked time in $[0,t)$ and $U(t)$ counts odd inputs outside this union, then
$$
 M(t)\le cU(t)+o(t),\qquad
 \limsup M(t)/t\le c/(1+c),\qquad
 \liminf U(t)/t\ge1/(\log_2 3)^2,\quad c=\log_2(3/2).
$$
The cutoff applies to the union of complete infinite-orbit windows, so a marked window crossing $t$ is counted up to $t$. This result includes every fixed periodic dictionary, and permits unbounded periods sublinear in their matched lengths.

## 1. Exact extensions and controlled overlap

For each eligible window choose a witnessing period $p$ and extend its periodic pattern to the right until first mismatch. Equivalently one can keep every witnessing period. The resulting interval $I=[a,b)$ has length $\ell\ge L$ and exactly matches a periodic rational shortcut start $\rho$ in $\mathbb Z_2$. For a period word of length $p$ with $s$ odd bits and affine numerator $3^sx+A$, its periodic point is $\rho=A/(2^p-3^s)$; the denominator is odd and nonzero, and the affine parity coding gives precisely the repeated word. The positive bounds $0\le A\le2^{p-s}3^s\le3^p$ and $|2^p-3^s|\le3^p$ show that every cyclic phase has height at most $3^p$. The match is finite since $x_a=\rho$ would make its orbit periodic. The nonzero numerator of $x_a-\rho$ gives
$$
 \ell=v_2(x_a-\rho)\le B_a+\gamma p,\qquad \gamma=\log_2 3.
$$
For each fixed $a$ the candidate $L$ are consequently bounded, using $L\le B_a+\gamma f(L)$ and $f(L)=o(L)$. There are finitely many extended intervals starting there. Uniformly as $a\to\infty$, $B_a\to\infty$, $p=o(L)$ and $p=o(\ell)$, hence $\ell\le (1+o(1))B_a$. In particular all intervals with start at most $t$ end before $C(1+t)$, for a constant depending on the source and $f$, since $B_a\le B_0+ca$.

If two extended intervals $I,I'$ with strictly increasing starts and ends overlap, the overlap has length less than $p+p'$ where $p,p'$ are their witnessing periods. Otherwise the two infinite periodic continuations agree forever after the later start. One short proof compares the generating series of the two periodic tails at the start of the overlap. They have forms $P(z)/(1-z^p)$ and $Q(z)/(1-z^{p'})$ with $\deg P<p$, $\deg Q<p'$. Their difference numerator has degree less than $p+p'$. Agreement of the first $p+p'$ coefficients makes it zero. Agreement beyond the earlier right endpoint contradicts the maximal extension defining that endpoint. The sharper Fine–Wilf threshold is unnecessary.

## 2. One disjoint family controls the whole union

Apply the following greedy selection on the integer times. At the first point of the extended union not yet covered, choose an interval covering that point with the farthest right endpoint. Break ties by earliest start, then arbitrarily. There are finitely many candidates at each pivot. Stop if everything is covered. The selected intervals $I_i=[a_i,b_i)$ have strictly increasing starts and ends and cover the extended union. Indeed each selection covers every union point from its pivot through $b_i-1$, and right endpoints increase by at least one. An interval chosen two selections later starts strictly after the intervening pivot (otherwise it offered a farther right endpoint at that pivot). Thus $a_{i+2}\ge b_i$, and no point lies in more than two selected intervals.

Put $d_1=0$ and $d_i=\max(0,b_{i-1}-a_i)$ for $i>1$. The overlap bound gives $d_i\le p_{i-1}+p_i$. The sum of lengths over selected intervals starting before $t$ is $O(1+t)$ by multiplicity two and the endpoint bound above. It follows that
$$
 \sum_{a_i<t}p_i=o(t),\qquad \sum_{a_i<t}d_i=o(t).
$$
This estimate charges the *entire* overlap even for a window extending far beyond $t$.

Trim $d_i$ positions from the left of $I_i$; the fragments $[a_i+d_i,b_i)$ are disjoint and cover the same extended union. Discard a fragment when $d_i>\ell_i/2$, $\ell_i=b_i-a_i$. Its length is then at most $d_i$, so the total discarded coverage before $t$ is $o(t)$. For any remaining fragment of length $\ell'_i\ge\ell_i/2$, its exact match continues from a shifted phase to the same mismatch. Its period obeys $p_i=o(\ell'_i)$, and
$$
 B_{a_i+d_i}\le B_{a_i}+c d_i\le(\delta^{-1}+c)\ell_i
 \le 2(\delta^{-1}+c)\ell'_i .
$$
Both end phases have log-height at most $\gamma p_i+O(1)=o(\ell'_i)$. Consequently the retained disjoint fragments satisfy all bounded-terminal hypotheses of [the rational-match theorem](RATIONAL_MATCH_MASS.md). The extended union differs from these fragments by $o(t)$ positions up to every cutoff. The original union is a subset of the extended union, so its marked count can only decrease and its outside odd count can only increase. This proves the theorem. If the greedy selection is finite all masses of matched times are bounded and the result follows directly from the total odd lower bound.

The same argument transfers the stronger adjacent-odd gap budget: adding back $o(t)$ discarded positions can destroy at most $o(t)$ previously uncovered adjacent pairs. Irregular low-density changes of parity need not form periodic windows satisfying the threshold; nothing here gives a positive lower frequency of even inputs.
