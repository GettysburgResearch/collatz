# What the two-parameter overhead test sees of fixed positive stopping times

Use the notation of `ORDINARY_OVERHEAD_SPECTRUM.md`. Write $S(h)$ for the supremum of the successful $s\ge1$ at fixed overhead $h$ (zero for an empty set). Put $\alpha=3/2$ and $\gamma=4/3$. For a positive odd $w$ reaching 1, write $\tau(w)$ for its *first accelerated odd* arrival time, and $E(w)$ for the sum of division exponents through that time.

**Exact transfer from a supplied ordinary source.** Every $w>1$ known to reach 1 supplies a successful rank $s=\tau(w)$ as soon as
\[
                  2\cdot 2^{E(w)}/3^{\tau(w)}<\alpha^h.
\]
Indeed take $c=1$, $D=1$, $m=33$ in the exact test. The latter reaches reflected 17 after $(7,12)$ odd and physical clocks. The displayed inequality implies the required pool bound on $w$, because $2^{E(w)}/3^{\tau(w)}=w\prod_{i<\tau(w)}(1+1/(3U^i(w)))>w$. The existing CRT construction gives genuine cheaper visitors on each phase for sufficiently long laps. More generally, taking $s=\tau(w)+j$ for $j\ge0$ multiplies the left-hand side by $\gamma^j$ because $U(1)=1$ with exponent 2. In particular the single fixed source $w=1$ supplies a success at *every* positive $s$ whenever $2\gamma^s<\alpha^h$.

**Two-sided stopping-time bounds.** Let $F_1(B)$ be the maximum first positive-odd hitting time of 1 among the odd $w\le B$ that actually reach 1, with maximum zero for an empty set. With the absolute constant $C=\exp(200/3)$ one has unconditionally
\[
                   F_1\left(\frac{\alpha^h}{3C}\right)\le S(h).
\]
If all odd $w<17\alpha^h$ reach 1, one also has
\[
             S(h)\le F_1(17\alpha^h)+h\frac{\log\alpha}{\log\gamma}.
\]
For the lower bound the pre-first-1 trajectory is a finite simple shortcut path. The resident finite-path reciprocal packing estimate, Theorem T-A3-651, gives $\sum_i1/U^i(w)\le200$; its proof uses an explicit split of short valuation words and a disjoint-endpoint count. Thus $2^{E(w)}/3^{\tau(w)}\le Cw$. The exact transfer above applies. For the upper bound a successful rank at most $\tau(w)$ is already bounded by the pool's maximum. At a larger $s$, the projected endpoint is 1 and $2^E/3^s\ge\gamma^{s-\tau(w)}$. The strict slope inequality from the exact test implies $\gamma^{s-\tau(w)}<\alpha^h$. [Finite simple-path packing, T-A3-651](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/astra-three-routes/pass3/FINITE_RECORDS.md)

For example, a proof of $S(h)=O(h)$ would imply the ordinary bound $\tau(w)=O(\log(2+w))$ for every convergent positive odd $w$. Conversely, universal convergence together with this logarithmic stopping-time bound would imply $S(h)=O(h)$. Neither estimate is asserted here. Nor does the first implication decide convergence of a supplied input. The exact transfer uses the *same* physical orbit of $w$ whose stopping time is measured; the produced counterexamples to extra-budget protection are on varying, explicitly specified positive cofactors.
