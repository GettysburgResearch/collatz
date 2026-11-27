# Sliding dyadic stacks and ordinary ternary cofactors

**Written consequence of the corrected moving-shadow theorem M1 and the local Yu discrepancy estimate.** Fix one ordinary odd start $n>0$, with $x_j=U^j(n)$. A clock shared by consecutive closed intervals is counted once in each interval. All logarithms are natural except where a base is displayed.

Let $B\ge1,b\ge0$ be fixed. For integers $J,r\ge1$ put $s_i=2^iJ$, $0\le i<r$. At shell $i$ choose any positive integer cap $H_i\le B(2s_i)^b$, with no nesting condition. Let $S_i$ count the clocks in $[s_i,2s_i]$ satisfying the simultaneous inequality
$$
  \max_{0<p,q\le H_i} v_3(x_j+p/q)
   \le L_i=C\log(2H_i)\log(3+s_i+\log(x_{s_i}+1)).
$$
Fractions are reduced, and $C$ is one absolute effective constant from the adjacent-edge estimate. In particular the threshold uses the actual shell start. There is an absolute effective $c>0$, and for the supplied $n,B,b$ an effective $r_0$, such that
$$
                  \sum_{i<r} S_i\ \ge\ c r\log(r+1)
                  \qquad(r\ge r_0,\ J\ge1).                 \tag{S1}
$$
The same lower bound with half the constant counts distinct dates satisfying their own shell test in the stack. Every date satisfies at most two copies of the shell test. The result includes periodic positive orbits.

Choose maximizing positive anchors separately in each shell. Their denominators can be taken prime to three. On each mismatch a shallow endpoint exists by the local Yu estimate, since the shell's division exponents have the upper bound $2+\log_2(x_{s_i}+1)+s_i\log_2(3/2)$. With $D_i\le2S_i$ mismatching edges, take the mismatches as singletons and the intervening exact runs as shadow pieces. There are at most $2D_i+1\le4S_i+1$ pieces. End phases may change at a shell boundary, as allowed by M1. The entire length $(2^r-1)J$ thus has at most $k=4\sum_iS_i+r$ pieces of height at most $H=\max H_i$.

The physical inequality $x_J+1\le(n+1)(3/2)^J$ and the polynomial envelope on the caps give
$$
 \log(x_J+2H+2)\le C_{n,B,b}J(r+2).
$$
M1 at the single actual start $x_J$ now gives
$$
 r\log2-\log(2C_{n,B,b}(r+2))
 \le K\,(k+1)/\log(k+2).
$$
The function on the right increases with $k\ge0$. For $r\ge r_0(n,B,b)$ the left side is at least $r\log2/2$. Since $k\ge r$, it follows that $k+1\ge c' r\log(r+2)$ with absolute effective $c'$; enlarging $r_0$ absorbs the extra $r+1$ into half the right side. This proves (S1).

In particular some shell in every stack of $r\ge r_0$ has $S_i\ge c\log(r+1)$, irrespective of the rate of growth of the orbit. A consecutive string of dyadic shells with at most $D$ shallow dates per shell has length at most $\max(r_0,\exp(D/c))$. For each fixed $\delta>0$, apply the theorem with $r=\lfloor\delta\log_2 J\rfloor$. For every sufficiently large $J$, the span $[J,J^{1+\delta}]$ contains a whole dyadic shell with $\gg\log\log J$ simultaneous shallow clocks, and its covered stack contains $\gg_\delta \log J\log\log J$ distinct shallow dates. Each cap and threshold remain local. For a quantitative count of such shells, fix $0<\theta<1$ and split an $r$-shell stack into disjoint groups of $\lfloor r^\theta\rfloor$ consecutive shells. Uniformity in the starting date gives $\gg r^{1-\theta}$ different shells with at least $c_1\theta\log r$ shallow dates apiece, for large enough $r$ depending on the fixed parameters and $\theta$. Thus every late polynomial span above has $\gg_{\delta,\theta}(\log J)^{1-\theta}$ such shells. The theorem does not locate them at prespecified places.

**Fixed positive anchors and cofactors.** Specialize to a fixed cap $H_i=H_0$. Every selected date certifies the same inequality for every fixed anchor of that ball. If an anchor must also *attain* the maximum, a fixed tie-breaking order shows that in any such stack one of the finitely many anchors attains it at $\gg_{H_0}r\log r$ distinct qualified dates. The identity of this winner may vary between stacks. Infinitely many stacks along a subsequence have a common winner.

On a non-eventually-periodic orbit all $x_j$ are distinct. Fix any positive reduced $p/q$ of height $\le H_0$ and $3\nmid q$. At each qualified date there is a positive ordinary cofactor
$$
     u_j=(q x_j+p)/3^{v_3(qx_j+p)} .
$$
For fixed $u$ and fixed exponent $v$, the integer state $x_j=(3^vu-p)/q$ is unique. Across the stack the exponent is at most $C_{n,H_0}(1+r+\log(2J))$, by physical growth and the local thresholds. It follows that the number of distinct $u_j$ among its qualified dates is at least
$$
        c_{n,H_0}\,r\log(r+1)/(1+r+\log(2J))\qquad(r\ge r_0). \tag{S2}
$$
For $r=\lfloor\delta\log_2J\rfloor$ this is $\gg_{n,H_0,\delta}\log\log J$ distinct cofactors in every sufficiently late span $[J,J^{1+\delta}]$, simultaneously for each fixed anchor of the ball whose denominator is prime to three. For odd $p,q$, $u_j/2$ is the corresponding positive integer cofactor after extracting the inevitable two. In particular this applies simultaneously to the seven reflected integer anchors at fixed cap 91. It proves growth of the cofactor set, not a repeated prescribed cofactor or an upper bound on its least member.

The argument treats positive anchors to avoid exact coincidences. Its count transfers to a signed ball on a stack whose states everywhere exceed the corresponding local cap; alternatively one counts exact coincidences together with shallow dates. Neither (S1) nor (S2) forces one of the cofactor values to produce a smaller ordinary ancestor. Their bounds can hold on an escaping charged ray.
