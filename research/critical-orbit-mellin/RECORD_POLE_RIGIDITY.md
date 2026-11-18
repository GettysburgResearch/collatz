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
