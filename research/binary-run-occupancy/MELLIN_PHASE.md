# One limiting rotation phase for a divergent positive orbit

**PROPOSED consequence, conditional on the displayed counting bound.** Consider one nonperiodic positive orbit and enumerate its odd states $n_j$ by the odd map U. In the notation of [the finite rotation estimate](MANTISSAS.md), the phase errors have one finite total. In particular the rotation can also be sampled at sparse polynomial clocks, where ordinary equidistribution of all odd steps alone would not suffice.

Write $h=H_2(\log_3 2)<1$. Use the proposed uniform count $N_S(X)\ll X^h/(\log X)^{3/2}$ for distinct shortcut states, pinned at `4182367ada14d566b5cc1c86daabe6838f88da2e`, `research/critical-orbit-mellin/CRITICAL_MOMENT.md`. This strengthening gives the rate below. The older reciprocal-summability estimate T-A3-403 at PR #92 `7bb6d36d3bc37dd09b52aa9a23c8e33973032359` suffices for existence of the phase. A finite segment of distinct odd states from first to last expands to a segment of distinct shortcut states: an even repetition would lead to the same next odd state, and successive halvings between two odd states are strictly decreasing.

For any segment with distinct odd states all at least $M\ge16$, dyadic shells give
$$
 \sum_i\log_2(1+1/(3n_i))\ll \frac{M^{h-1}}{(\log M)^{3/2}} .       \tag{1}
$$
Indeed the contribution from $2^k M\le n_i<2^{k+1}M$ is $O((2^k M)^{h-1}/(\log M)^{3/2})$. The geometric sum converges. The whole budget for an arbitrary distinct segment is $O(1)$ by adding the finitely many small integers. In particular equation (1) of MANTISSAS, combined with its stated two-logarithm lower bound with exponent $\tau$, sharpens its all-segment discrepancy to $O(N^{-1/(1+\tau)})$: take $Q=N^{1/(1+\tau)}$ in its convergent-denominator proof.

In the nonperiodic case write $M_j=\min_{i\ge j}n_i\to\infty$. Define the single real phase
$$
 \beta=\log_2 n_0+\sum_{i\ge0}\log_2(1+1/(3n_i)).
$$
Exact summation of the step formula gives
$$
 \log_2 n_j\equiv\beta+j\log_2 3-e_j\pmod1,\qquad
 0<e_j\ll M_j^{h-1}(\log M_j)^{-3/2}
$$
for $M_j\ge16$. The error is positive and decreases. The argument uses the future minimum, not the present height, which can precede a large drop.

For every nonconstant rational polynomial $p(t)$ taking eventually nonnegative integer values at integers and tending to infinity, the fractional logarithms of $n_{p(t)}$ are uniformly distributed modulo one. Indeed their distance from $\beta+p(t)\log_2 3$ tends to zero. The latter sequence is equidistributed by Weyl's polynomial theorem. Consequently a prescribed divergent trajectory whose odd states at all square clocks, for example, omit a fixed binary significand interval cannot be an ordinary realization. This says nothing about an unscheduled sparse subsequence chosen in response to the values themselves.

The power in the all-segment estimate can be made numerical: $D_N\ll N^{-1000/5117}$. Fan, Queffélec and Queffélec, Theorem 2.1, give $\|n\log_3 2\|\gg n^{-4.117}$ for every positive integer $n$, citing Wu and Wang. The reciprocal $\alpha=\log_2 3$ satisfies the same exponent: for $m$ nearest to $q\alpha$, $|q\alpha-m|=\alpha|m/\alpha-q|\gg m^{-4.117}\gg q^{-4.117}$. Use $\tau=4.117$ in the displayed discrepancy argument. The uniform bounded phase budget needed here already follows from the finite simple-path bound T-A3-651. Consequently every individual binary leading word of length at most $(1000/5117-\epsilon)\log_2N$ has its logarithmic frequency up to a uniformly vanishing relative error, for any fixed $\epsilon>0$. [Fan–Queffélec–Queffélec, *The Furstenberg set and its random version*, Theorem 2.1](https://doi.org/10.4171/LEM/1040) · [Finite simple-path reciprocal budget](../astra-three-routes/pass3/FINITE_RECORDS.md)
