# Arithmetic concentration of exceptional prime factors in the mandatory clock

**Status.** Proposed fixed-source theorem. Through $N$ native clocks an escaping ordinary ray can put only $O(\sqrt N)$ coefficient-record log-height on prime-cofactor exceptions away from the specified negative signed record cycles. This includes adaptive bounded-size pools and does not assume exponential growth or a limit of odd frequency. When the cumulative log peak grows faster than $\sqrt N$, it identifies the only part of the compulsory height law where such exceptions can persist.

Use one fixed nonrepeating positive native trajectory and its odd coefficient-record states $p_i=x_{t_i}$ at native clocks $t_i$. Mark the record at $t_i$ with its **incoming** roof $a_{i-1}=\log_2(3^{m_{i-1}}/2^{s_{i-1}})$ for $i\ge1$. Thus $0<a_{i-1}\le\log_2(3/2)$. Let $A_N$ be the sum of these roofs at $t_i<N$, so $A_N\to\infty$. It equals the running coefficient log peak in the odd convention, and differs by a bounded amount (depending on the source) from $\log_2$ of the largest native height through that horizon. At a prefix ending partway through an odd-to-odd step, intermediate native heights exceed one of the previous odd heights by at most a factor two, which suffices for this comparison.

Fix a finite nonempty set $Z\subset\mathbb Q\cap\mathbb Z_2$, a common positive odd denominator $D$, $0<\epsilon<1$ and $r\in\mathbb N$. At each horizon take any one set $S_N$ of at most $r$ primes, selected using the entire prefix if desired. For $Y=D(p_i-z)\ne0$, call the pair $(i,z)$ exceptional if
$$
              |Y|\prod_{\ell\in S_N}\ell^{-v_\ell(Y)}
                             < |Y|^{1-\epsilon}.
$$
The finitely many zero cases can be discarded. The group argument below uses the elementary prime-power return identity from [the native-clock cofactor theorem](../renewal/SHIFTED_COFACTORS.md).

## OP-G9. Square-root record-height budget

Fix a finite precision $b$. For a negative signed odd rational record-cycle phase $z$, a protected neighborhood at a terminal mark means that its actual incoming and next complete ladder labels agree with the signed cycle there, and its actual preceding, current, and next coefficient-record states agree with their respective signed phases modulo $2^b$ and $3^b$. There is no protection for any other rational $z$.

Uniformly over all permitted $S_N$, the following sum has order $O_{x_0,Z,\epsilon,r,b}(\sqrt N)$:
$$
 \sum_{\substack{i\ge1,\ t_i<N\\
       (i,z)\ {\rm exceptional\ for\ some}\ z\in Z\
       {\rm without\ its\ protected\ neighborhood}}}a_{i-1}.
$$
For a terminal mark close to one negative phase that also violates the test for a different unprotected shift, the latter still enters this bound. If $Z$ has no negative signed record-cycle phases then the bound applies to **every** exceptional record. A next label beyond the native horizon causes no difficulty because the original escaping ray is infinite; possible interval endpoints of the proof are in any case discarded.

Indeed the coefficients at strict records and the corresponding odd heights are both increasing. All marks with $\log_2(p_i+1)\le\sqrt N$ have combined roof at most $\sqrt N+O_{x_0}(1)$ by the exact discrepancy bound in [OP-G5](GATE_SUSPENSION.md). For each of the remaining exceptional pairs at least one prime $\ell\in S_N$ satisfies
$$
             v_\ell(D(p_i-z))\,\log_2\ell\ \ge c\sqrt N
$$
for a fixed $c=c(\epsilon,r)>0$ and sufficiently large $N$, because $\log_2|D(p_i-z)|=\log_2(p_i+1)+O_Z(1)$ uniformly at these high marks. An empty pool has no exceptions. Fix $\ell,z$ and order the qualifying **record marks** by native time. Separate them into groups wherever the gap is at least $c'\sqrt N$, with $0<c'<c/\log_2 3$. There are $O(1+\sqrt N)$ groups. At two consecutive marks in the same group the intervening word $w$ of native length $l$ and grade $j$ satisfies
$$
 \ell^{\lceil c\sqrt N/\log_2\ell\rceil}
 \ \mid\ D(3^j z+C_w-2^l z),\qquad
                 |D(3^j z+C_w-2^l z)|\le C_Z3^l .
$$
The integer must vanish. Reading the indicated affine branches backwards from the dyadic integer $z$ proves that this word is a genuine periodic return from $z$ to itself. Since the earlier and later physical vertices are odd coefficient records, the multiplier on the intervening word is strictly larger than one. Its nonnegative carry is strictly positive. Thus $z$ is a negative odd rational phase on the indicated native cycle. Furthermore a complete lap ends at a strict odd coefficient record, so its endpoint is one of the signed cycle's actual record phases. To see this last point, every earlier odd coefficient within the last lap is strictly below the terminal one, and every still earlier lap is reduced by the reciprocal of the superunit lap slope.

Within a nonsingleton group all intervening native letters concatenate to the same signed periodic itinerary between its first and last qualifying marks. The first is already an actual coefficient record, so from it every subsequent complete ladder before the end of the group is exactly the finite signed-cycle ladder. The previous and next signed record phases are at native distance at most the lap length. Remove marks within a fixed native distance $B_b$ of each end of each group, also removing every singleton. Choose $B_b$ so that, about any of the three retained record centers, the common future has at least $b$ native letters and the common past contains at least $b$ odd departures. This is possible uniformly over the finitely many relevant periods in $Z$. The matching future enforces $2^b$ agreement by the exact parity congruence. The matching past enforces $3^b$ agreement by forward affine contraction, since all signed phases of such a negative period are 3-integral and all actual states are integers. Thus every remaining mark has its desired protected neighborhood. The number removed per group is $O_b(1)$, each costs at most $\log_2(3/2)$, and there are at most $r|Z|$ pair families. Together with the low-height marks this proves the budget.

## OP-G10. Consequence for mandatory occupation

Along any subsequence with $A_N/\sqrt N\to\infty$, form the compulsory roof-weighted edge laws of [OP-G6](GATE_SUSPENSION.md) up to the last completed coefficient record before $N$. Any weak limit of the subprobabilities marked exceptional for at least one shift is dominated by the corresponding full edge law and supported on the finite collection of exact negative signed cycle edges **terminating** at phases in $Z$. The circle coordinate is unrestricted in this support assertion. Indeed for each fixed $b$ the complement of the union of those cylinder neighborhoods has total normalized exceptional weight $O_b(\sqrt N/A_N)\to0$. The neighborhoods at increasing precisions decrease onto those signed cycle edges. Using the previous and current vertex and incoming label is already enough for the edge space; the next-label assertion in OP-G9 is extra. OP-G8 classifies the full law on these marked cycles. In particular any diffuse regular sector and any infinite-label sector carry zero limiting exceptional submass in this super-square-root regime. If the limiting law gives zero weight to the listed signed edges, then asymptotically all its compulsory height has the simultaneous prime-to-pool lower bound.

Independently, through horizons with $A_N/N\to v>0$, the native occupancy theorem C1 bounds the total normalized exceptional record weight by
$$
         \limsup\ \frac{\sum_{\rm exceptional}a_{i-1}}{A_N}
               \le \min\{1,(1-\log_3 2)\log_2(3/2)/v\}.
$$
This second estimate also limits the possible exceptional fraction *inside* a signed-cycle atom when $v>(1-\log_3 2)\log_2(3/2)$. A coarse statistical atom at a rational phase does not force any positive fraction of the integer's logarithmic height into any fixed set of prime factors. The slow regime $A_N=O(\sqrt N)$ and the ordinary diagonal integrality problem remain unresolved.
