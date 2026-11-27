# Rare nonbinary valuations preserve the binary excursion alternative

Let $\delta=1/100000$. In the notation of the sparse real-depth theorem, every sufficiently large primitive positive rational Collatz cycle with arbitrary positive valuations satisfies, on the separately imported bound $\mu(\log_2 3)\le3$,
$$
 d>P^\delta
 \quad\hbox{or}\quad
 \#\{i:L_i>99/50\}+\#\{i:e_i\ge3\}>\delta P.
$$
The two counts may both include a departure. The bound requires neither a real-width cap nor a bound on the size of a nonbinary valuation. In particular the second conclusion applies to all sufficiently long ordinary primitive cycles. A sequence having $o(P)$ nonbinary steps must therefore have at least $(\delta-o(1))P$ odd departures of the stated real depth.

Suppose the two counts have sum at most $\delta P$ and $d\le P^\delta$ along growing periods. The unmarked physical-source estimate, convergence $\theta\to\lambda$, and upper exponent $3+\delta$ for $Y$ in the sparse real-depth theorem apply. Call marks of the first kind deep vertices and marks of the second kind exceptional edges. In a length-$b$ cyclic window count the deep vertices at offsets $1,\ldots,b$ and the exceptional edges at offsets $0,\ldots,b-1$. Incidence gives at most $\delta bP$ events summed over all starts, including winding windows. As before, at least $(1-2\delta-\delta/\tau)P$ windows have clean endpoints and at most $\tau b$ events of both types combined, where $\tau=1/80000$. There are at most $2^{2bH_2(\tau/2)}$ choices of their labeled mask. Fix the phase and encode the actual grades at deep sites by the arbitrary positive valuation construction, costing at most four bits for each deep vertex.

First make the projection described in the sparse theorem, clipping at one and setting the sites with $f_i>49/50$ to zero. The resulting bits $w_i$ satisfy positivity on every edge and the real cap. Each edge with original $e_i\le2$ still obeys the binary rule, since the first clipping is monotone and 1-Lipschitz on the adjacent original grades, and the forced-zero sites have a mechanical one coming in and a mechanical two going out. A remaining illegal binary transition must thus be a drop $w_i=1,w_{i+1}=0$ on a mechanical two at an exceptional edge. No two consecutive mechanical ones are needed for this argument. What is needed now is absence of three consecutive twos, which follows from $\theta<5/3$ for sufficiently large cycles. For three consecutive mechanical gaps, the sum is at most $\lceil3\theta\rceil\le5$.

Consider the maximal consecutive runs of mechanical twos within the window. They are separated by at least one mechanical one and have at most two edges, hence at most three vertices. For every such run containing an exceptional edge, record all its current bits, at a cost of at most three per exceptional edge. On these runs replace each bit by the minimum of the suffix starting at that bit. This makes the run nondecreasing, lowers or preserves its initial bit, and preserves its last bit. The incoming mechanical one, if present, permits a decrease into the initial bit, and the next mechanical one has an unchanged initial bit. The same reasoning works for simultaneous changes on the runs on opposite sides of a single mechanical one. Sites required to be zero stay zero. The repaired bits therefore obey all the binary rules at the original slope and intercept. The procedure also covers truncated runs at the two window ends. Runs containing no exceptional edge already have no drop.

Every changed site lies in the fixed deep record or a recorded exceptional run. Both its raw and repaired grades are fixed there. Recording the cut grades in each segment determines its repaired entrance as well. The map from raw paths to repaired paths is injective conditional on the records. As in the sparse theorem, if $\Delta_i$ is the raw grade minus the repaired grade, then raw and repaired dates within the segment satisfy $r_i-r_i'=\Delta_j-\Delta_{j+i}$. Consequently
$$
 B_{\rm raw}=2^{\Delta_j}B_{\rm repaired}+\text{a fixed integer},
$$
so the ordinary fourth energy is at most the clean binary fourth energy. Conditioning on all captured exceptional-run bits is a list of fixed individual-site restrictions on the raw grades (or their clipped values). These restrictions preserve the Cartesian factorization of the raw interiors after conditioning on the cut grades. The energy estimate allows arbitrarily large exceptional jumps.

If $q_1,q_2$ are the numbers of deep vertices and exceptional edges, the raw grade records and repair bits cost at most $4q_1+3q_2\le4\tau b$ bits. All placement and separation margins of the binary sparse theorem remain valid, because each raw grade is still at most $q_1+1\le\tau b+1$. In particular the same estimates use the original dates and denominator. In the final count one replaces $H_2(\tau)+2\tau$ by
$$
 2H_2(\tau/2)+4\tau
 \le \tau\bigl(\log_2(2/\tau)+\log_2 e+4\bigr)<24\tau
$$
using $2/\tau=160000<2^{18}$ and $\log_2 e<2$. At $\eta=1/10000$, $\lambda>19/12$ and $\gamma=999/1000$ the contradiction margin is
$$
 1-(3+\delta)\frac{5\eta/(19/12)+\gamma(1-\eta)+(4+\eta)24\tau/(19/12)}{3+\eta}
 = \frac{16016124887}{285009500000000}>0 .
$$
The companion checker tests the exact identity and complete positive-gap paths at a finite horizon, including successive mechanical twos, deep grades, nonbinary gaps and repairs meeting cut vertices. This is a written extension of the sparse theorem. Its analytic scope and external dependencies are the same as in that theorem.

Prepared by the GPT-6.2 Astra binary-energy reviewer, 27 November 2026 UTC.
