# A divergent weighted set of shallow dates on a fixed tropical geodesic

Fix one positive odd source $a_0$ and put $a_t=U^ta_0$. Use the polynomially bounded local height caps and the actual Yu thresholds of the dyadic-stack result S1, consistently on the shells $[2^i,2^{i+1}]$. Let $\mathcal S$ be the union of dates shallow for at least one of their incident shells. Write, for $t\ge3$,
$$
 w_t=\frac1{(1+\log t)(1+\log\log t)^2}.
$$
Then on **every** such ordinary source
$$
                  \sum_{t\in\mathcal S,\ t\ge3} w_t=\infty .       \tag{W1}
$$
Indeed group the dyadic shells with indices $2^k\le i<2^{k+1}$. Their number is $r=2^k$ and their starting date is $J=2^{2^k}$. S1 gives at least $c2^kk$ distinct qualified dates in the group. Since $w_t\gg2^{-k}k^{-2}$ throughout, the group contributes at least $c'/k$. A shared endpoint belongs to at most two groups; alternatively remove the last endpoint of each group. This proves W1. The argument gives $\sum_{t\in\mathcal S,\,3\le t\le N}w_t\gg\log\log\log N$ for all sufficiently large $N$, by summing complete groups. Constants and onset follow S1.

Assume this source escapes and use the *same* forward states $a_t$ to evaluate the ordinary reverse cost $m_t$ of PR 201. For a ternary target $y$, $m_t(y)$ is the least total exponent of a legal $t$-letter inverse word. Its value is infinite for a nonunit at positive depth. Put $B^j y=4^jy+(4^j-1)/3$ and
$$
 R_t=\min_{j\ge1}\{2j+m_t(B^j a_t)-m_t(a_t)\}.
$$
At least one of three successive larger siblings is a unit, since $By\equiv y+1\bmod 3$. A finite minimum exists since $m_t(\cdot)\ge t$ on units. The exact positive-ordinary sibling summability (1) in PR 201 gives
$$
 \sum_{t\ge1}2^{-R_t}\le
 \sum_{t\ge1}\sum_{j\ge1}4^{-j}2^{m_t(a_t)-m_t(B^j a_t)}<\infty .
$$
This is the imported same-source arithmetic input; its exponent-one proof uses the positive antichain estimate identified in that manuscript. [PR 201, SHA 4c36876ebbe8d3cca69b2c4867aeee34f5700470, tropical sibling formula (1)](https://github.com/GettysburgResearch/collatz/blob/4c36876ebbe8d3cca69b2c4867aeee34f5700470/research/six-hour-20261127/escape/TROPICAL_SIBLINGS.md)

For every fixed real $K$ one must consequently have
$$
 \sum_{\substack{t\in\mathcal S,\ t\ge3\\
                  R_t\le\log_2(1/w_t)+K}} w_t<\infty .            \tag{W2}
$$
In fact each such $w_t$ is at most $2^K2^{-R_t}$. Combining W1 and W2 gives a divergent-weight set of actual shallow dates outside every fixed additive allowance. Equivalently the isolation $R_t-\log_2(1/w_t)$ tends to $+\infty$ in density with respect to the growing weighted census on $\mathcal S$. The explicit target is
$$
 \log_2(1/w_t)=\log_2(1+\log t)+2\log_2(1+\log\log t).
$$

There is also a local count on every sufficiently late fixed-power span. For $r=\lfloor\delta\log_2 J\rfloor$, $\delta>0$ fixed, take the stack starting at any integer date $J$ and give it any allowed local caps. Its distinct qualified-date count is $\gg_\delta \log J\log\log J$. At most
$$
        2^K(\log J)(\log\log J)\sum_{t\ge J}2^{-R_t}
          =o_K(\log J\log\log J)
$$
dates anywhere after $J$ can have $R_t\le\log_2((\log J)(\log\log J))+K$. Thus every such span contains $\gg_\delta\log J\log\log J$ dates satisfying both the simultaneous shallowness and the complementary sibling isolation bound, for each fixed $K$. Neither the location nor the available sibling index is chosen by comparing different starting integers.

This identifies a sufficient closing input. An independent upper bound $R_t\le\log_2(1/w_t)+O(1)$ on a subset of the qualified dates with divergent $w_t$-sum would contradict W2. The weaker upper bound $\log_2 t+O(1)$ on these dates alone would require a divergent ordinary harmonic sum there, which S1 does not imply. No cheap off-ray inverse word is constructed by the valuation count.
