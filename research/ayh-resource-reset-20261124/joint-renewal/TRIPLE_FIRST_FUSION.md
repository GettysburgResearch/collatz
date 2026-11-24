# Finite mean time to the first merger of three affine rays

Let the three initial ordinary integers be given by fixed affine forms
$3^{a_i}n+c_i$, with $a_i\ge0$, $c_i\in\mathbb Z$. Restrict to positive starts. On an original binary cylinder of depth $t$, each arm at shortcut clock $t$ is an affine function of the unexposed quotient, with slope $3^{L_i(t)}$, where $L_i(t)=a_i+p_i(t)$ and $p_i(t)$ is its odd-input count. Call two arms fused when their whole affine functions agree. This certifies a physical common future for every positive ordinary lift, and the agreement persists. Write $\sigma$ for the first fusion of *any* pair under the uniform binary-prefix law.

**Theorem.** For every fixed triple, $\mathbb E\sigma=\sum_{t\ge0}P(t)<\infty$. In particular $tP(t)\to0$. A proof using only the pair occupation bound, before invoking the additional mixed-clock estimate below, gives a finite constant $C$ such that
$$
 P(t):=\Pr(\sigma>t)\le C/(1+t).
$$
For every interval of $N\ge2$ positive parameter values on which the three forms are positive, at most $CN/(1+\log N)$ starts lack a certified fusion of any pair by $\lfloor\log_2N\rfloor$ shortcut steps. The bound also applies to three prescribed members of a larger fixed family. A union over its triples proves summability of the probabilities that the surviving partition of that fixed family has at least three classes. The same summability holds for the native head-row fractions, uniformly in the locations of the source intervals of the stated lengths. It gives no upper estimate of this strength for exactly two classes.

There is also a summability assertion. A strictly ordered, unfused triple has a *middle* arm in the order of the three grades $L_i$. Sum over all clocks the probabilities that the middle arm alone has parity different from both others. The sum is finite. In particular the corresponding fractions of native head sources are summable over $j$ at the clocks $h_j=\lfloor\log_2(81^{j-1})\rfloor$. To determine the next parities after these $h_j$ bits, the exceptional pattern “middle alone” is already known from the pairwise parity differences, before the next bit is read.

## Pair input and original sampling

On each parameter cylinder of depth $t$, write $n=r+2^tq$. The three current values are $3^{L_i(t)}q+C_i$. Each next parity is the parity of $q$ or its complement, with the choice fixed by $C_i$. This proves that the three parity increments and their simultaneous complements occur with equal conditional probability. In particular every difference $L_i-L_j$ is a martingale with increments of absolute value at most one. The statement uses no independent walks for the three arms.

For each pair use its canonical level $S=|L_i-L_j|$ and normalized offset $Z=D/3^S$ after orienting it as $z,3^S z+D$. Put $V=\sqrt{|Z|}$. Its fair-base-bit transition law is the same even conditional on the joint prefix, since the base coefficient of $q$ is odd. Its *future marginal* is therefore the canonical pair chain from its actual current state. The fixed-state survival tail is $O((1+t)^{-1/2})$. The frozen [PR 146 proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md) and its companion [killed occupation estimate](KILLED_GRADE_OCCUPATION.md) give, from *any* live state, the expected total physical time at levels $S\le K$ before pair fusion bounded by
$$
 C[(1+K)^2+(1+K)(1+V)].                                      \tag{1}
$$
All constants below can depend on the fixed initial triple. Duplicate initial forms give $P(t)=0$.

Let $A_t=\{\sigma>t\}$. The one-step inequality $\mathbb E(V'\mid\mathcal F_t)\le\rho V+1$ holds while the pair is live, with $\rho=(1/\sqrt2+\sqrt{3/2})/2<1$. Killing at the first fusion of any pair only decreases the nonnegative contribution. Thus for each of the three pairs
$$
 B_{t+1}:=\mathbb E[V_{t+1}{\bf1}_{A_{t+1}}]\le\rho B_t+P(t).
$$
Iterating from $\lfloor t/2\rfloor$, using $\sup B_t<\infty$ and monotonicity, gives $B_t\ll P(\lfloor t/2\rfloor)+e^{-ct}$. Apply (1) at $H$ on $A_H$, separately for each pair. The future triple-live event is contained in the corresponding future pair-live event. For $H\ge2$,
$$
 \sum_{t\ge H}\Pr(A_t,\ \min_{i<j}|L_i(t)-L_j(t)|\le K)
 \ll (1+K)^2[P(\lfloor H/2\rfloor)+e^{-cH}].                    \tag{2}
$$

## Ordered gaps

Sort the grades $A\le B\le C$ at each clock and define $F=(B-A)(C-B)$ and $U=C-A$. At strict order write $u=B-A$ and $v=C-B$. The next gaps in the old order are nonnegative (an integer gap decreases by at most one) and are $u+\alpha,v+\beta$ or $u-\alpha,v-\beta$. For parity bits $e_1,e_2,e_3$ in the sorted order, $\alpha=e_2-e_1$ and $\beta=e_3-e_2$. Then $\alpha\beta=-1$ exactly when $e_1=e_3\ne e_2$, and zero otherwise. The conditional expected new product equals $F+\alpha\beta$. Sorting tied new values does not change that product. Killing can only decrease it.

At a tie the old product is zero. The old tied pair still differs by at most one after the update, so one of the new sorted gaps is at most one. The total new spread is at most $U+1$. The new product is therefore at most $U+1$, including in the triple-tie case. With $I_t$ the event of a live strict order with the isolated middle parity, telescoping ordinary expectations over finitely many deterministic clocks gives
$$
 \mathbb E[F_T{\bf1}_{A_T}]+\sum_{t<T}\Pr(I_t)
 \le F_0+\sum_{t<T}\mathbb E[(1+U_t){\bf1}_{A_t,\,\mathrm{tie}}]. \tag{3}
$$

On a dyadic shell $H\le t<2H$, the spread is $O(\sqrt{H\log(2H)})$ at each fixed clock except on a set of probability $O(H^{-5})$, by Azuma applied to the three fixed pairwise martingales and an adequately large constant. Deterministically the spread is $O(1+H)$ there. By (2) with $K=0$, the contribution of the shell to the right of (3) is
$$
 O(\sqrt{H\log(2H)}[P(\lfloor H/2\rfloor)+e^{-cH}]+H^{-3}).     \tag{4}
$$
No independence of reaching a tie and having small spread is used.

## Bootstrap and return to the integers

Initially $P(t)\ll (1+t)^{-1/2}$ by any one fixed pair tail. Summing (4) over earlier dyadic shells gives $\mathbb E[F_t{\bf1}_{A_t}]\ll (\log(2+t))^{3/2}$. For $H\le t<2H$, either the minimum gap is at most $K$, or $F_t>K^2$. Use (2) on the former, Markov's inequality on the latter, then use monotonicity of the first-merger tail:
$$
 P(2H)\ll (1+K)^2 H^{-3/2} +(\log(2H))^{3/2}/K^2 .
$$
Taking $K=H^{3/8}$ gives $P(t)\ll t^{-3/4}(\log(2+t))^{3/2}$ for all $t\ge2$ by monotonicity. The right of (4) is now summable over dyadic $H$, so (3) gives both $\sup_t\mathbb E[F_t{\bf1}_{A_t}]<\infty$ and $\sum_t\Pr(I_t)<\infty$.

With that uniform product bound, use (2) again, retaining the present survival probability:
$$
 P(2H)\le C_1/K^2+
     C_2(1+K)^2 H^{-1}[P(\lfloor H/2\rfloor)+e^{-cH}].          \tag{5}
$$
Set $K=\lfloor\sqrt{\epsilon H}\rfloor$; for sufficiently large $H$ the floor changes $1/K^2$ by at most an absolute factor. Fix $\epsilon>0$ small enough that $4C_2\epsilon\le1/8$. For large dyadic $H$, (5) yields $P(2H)\le C_3/H+P(H/2)/8$. The numbers $(2H)P(2H)$ along dyadic $H$ are bounded by induction, since the previous term $(H/2)P(H/2)$ has coefficient $1/2$. Monotonicity between dyadic clocks proves the stated reciprocal-clock bound.

Each complete consecutive parameter block of length $2^h$ runs through all original bits of depth $h$ exactly once. Conditional grades and affine intercepts on those cylinders are the actual ones. Cover the given integer interval by at most two such blocks for $h=\lfloor\log_2 N\rfloor$. If a completion contains a nonpositive extrapolated start, use its algebraic binary-cylinder count only; all starts in the given interval are positive. The same cover transfers the summable $I_{h_j}$ estimate to head rows, since their clocks are distinct and the event is already determined by $h_j$ bits. Distinct fixed suffixes can be summed.


## Converting middle isolation to finite mean first-fusion time

The additional input is the unconditioned interior-block inequality, [rStation paper 13, proof of Theorem 6, equations (20)–(21)](https://rstation.ai/problems/collatz/papers/13). Start a canonical pair at level $2\le k\le J$ with arbitrary integer offset. Stop at its $\ell$-th mixed step (opposite parities), or upon hitting level one. Write $D_\ell$ for the elapsed shortcut time and $E_\ell$ for completion of the requested steps. With $R_*=\lceil\log_2(J+\ell+1)\rceil+6$, $0<\eta\le1$ and $\ell\ge4R_*^2$, that inequality bounds
$$
 \Pr(E_\ell,\ |D_\ell/\ell-2|>\eta)
 \le C\log^2(\ell+2)(R_*/\sqrt\ell)^{\eta^2/(18\log2)}.          \tag{6}
$$
This is the unconditioned intermediate estimate in that proof. Its terminal conditioning on a specified whole excursion duration is unnecessary here.

On the dyadic shell $H\le t<2H$, put $b=\lfloor H^{1/4}\rfloor$. The total probability of live clocks with minimum grade gap $\le 2b$ is $O(b^2/H)$ by (2) and the reciprocal-clock bound. This is summable over dyadic $H$.

At any remaining live prefix all three pair gaps exceed $2b$. Their order stays strict and no two rays can fuse during the next $b$ physical clocks. Each individual pair also stays above one until at least $b$ mixed steps have occurred, since its level changes by at most one per mixed step. Thus $E_\ell$ is certain for $\ell_- =\lfloor.45b\rfloor$ and $\ell_+=\lceil.55b\rceil$. The initial maximum gap is bounded by $2H+O(1)$ deterministically, so take this as $J$. At fixed $\eta=1/10$, the right side of (6) tends to zero uniformly in the prefix and in the integer offsets because $R_*=O(\log H)$ and $\ell_\pm\asymp H^{1/4}$. The conditional pair law at this given joint prefix is the actual canonical chain, with its future bits exposed by the original parameter. A union bound over the six tests succeeds with conditional probability at least $1/2$ for all sufficiently large $H$. On success $D_{\ell_-}<b<D_{\ell_+}$ for all three pairs. Their numbers $M_{12},M_{23},M_{13}$ of mixed steps in these $b$ physical clocks are then between $.44b$ and $.56b$ for sufficiently large $H$.

In the fixed sorted order, at every one of the $b$ clocks twice the isolated-middle indicator equals the sum of the two adjacent mixed indicators minus the outer mixed indicator. This is a direct identity on three binary parities. Thus on the six-test event at least $(.44+.44-.56)b/2=.16b$ clocks have isolated middle parity. It follows for every such high-gap starting prefix that the conditional expected number of isolated-middle clocks in the block is at least $.08b$. Consequently
$$
 \sum_{H\le t<2H}\Pr(A_t,\ \min_{i<j}|L_i(t)-L_j(t)|>2b)
 \le 13\sum_{H\le s<2H+b}\Pr(I_s).                              \tag{7}
$$
Indeed each integer $s$ belongs to at most $b$ of the sliding windows starting at $t$ in this shell. The enlarged dyadic shells have bounded overlap. Combining (7) with the summable low-gap estimate and (3) now gives $\sum_t P(t)<\infty$. Monotonicity gives $tP(t)\le 2\sum_{\lfloor t/2\rfloor\le s\le t}P(s)\to0$. The previously justified two-block cover at the distinct native clocks gives summability of actual three-class source fractions.

**Prior work and scope.** David Leen's [*Late synchronization and the geometry of Collatz families*](https://doi.org/10.5281/zenodo.23268753) treats capacities and surviving partitions of fixed families. The [published discussion of the fixed-triple result](https://rstation.ai/r/collatz/posts/20) attributes an $o(t^{-1/2})$ first-merger tail and the half-sum formula to Leen. [Paper 13](https://rstation.ai/problems/collatz/papers/13) describes his Theorems 5.1 and 6.1. The proof here obtains a concrete $O(1/t)$ bound and summable middle-isolation from the pair occupation estimate, and then uses the uniform mixed-clock estimate to prove finite mean first-fusion time. The primary DOI was inaccessible in the browsing environment; we do not assert that this is the best exponent in the literature. The two-class configurations left by the theorem can carry different eventual colors. The occupation upgrade is essential: the harmonic series prevents obtaining the three-class summability result from the reciprocal-clock bound alone.

The exact one-step ordered-gap identity, tie-creation inequality and mixed-parity identity are kernel-checked in [TripleGradeProduct.lean](TripleGradeProduct.lean). The occupation, concentration and bootstrap arguments are written proofs.
