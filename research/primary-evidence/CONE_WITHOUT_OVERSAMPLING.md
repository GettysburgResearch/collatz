# Fixed-target sublinearity and a two-source proof of the finite cone test

**PROPOSED, source-qualified.** Fix the finite rational scalar $C_Q$ of the [two-scale test](../critical-orbit-mellin/TWO_SCALE_TEST.md) at repository revision `0bc6a7e`. The following argument proves that universal positive-integer convergence implies $C_Q\to0$, whereas failure of universal convergence implies $\liminf C_Q>0$. It does not identify the numerical limit in the latter case. Its external analytic inputs are Tao's published fine-scale mixing for the ordinary Syracuse offset (Proposition 1.14) and the retained-word construction in Mazur's positive predecessor theorem. It requires no ordinary pointwise trace, first-landing lower bound uniform in the target, affine-map mixing at excess precision, or sublinear bound uniform in the target. The two-scale paper's evaluation of the nonzero limit is a separate assertion.

Write $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. For a physical forward word of length $q$, write $t=J_wx+F_w$, $S_w=\sum a_i$, $J_w=3^q2^{-S_w}$. Put $g_q(t)=\sum_{U^qx=t}J_w$, with $g_0=1$. Each word admits precisely one odd endpoint $t_w$ in $[1,2\cdot3^q]$. A compatible positive odd endpoint has a positive odd inverse at every step. Its weighted term satisfies $J_w/t\le1/x$.

## Elementary bounds

For all $q\le Q$ the total of $J_w$ over words with $S_w>12Q$ is at most
$$
 3^q 2^{-6Q}(1+\sqrt2)^q\le [3(1+\sqrt2)/64]^Q .
$$
This follows by exponential Markov with independent geometric letters $\Pr(a=i)=2^{-i}$ and moment $\mathbb E2^{a/2}=1+\sqrt2$. Consequently
$$
 \sum_w J_w/t_w=O(Q)\qquad (|w|=Q).
$$
Indeed the remaining physical sources satisfy $x\le 2^{12Q+1}$ and are distinct, since each odd source has exactly one forward word of length $Q$. Their reciprocal sum is $O(Q)$.

For each fixed positive odd $t$, including periodic targets,
$$
 \sum_{q=0}^Q g_q(t)=O_t(Q+1). \tag{1}
$$
For the retained terms $x\le t2^{12Q}$. For a given $x$, the first visit to $t$ has weight at most $t/x$. If $t$ is periodic, repeated hits contribute successive powers of its lap multiplier $J_C<1$, since $t=J_Ct+F_C$ with $F_C>0$. Thus the total for this $x$ is bounded by a fixed multiple of $t/x$. The discarded mass is exponentially small after summing over depths.

## Pointwise sublinearity from published offset mixing

For each fixed odd $t$,
$$
 g_q(t)=o_t(q). \tag{2}
$$
On the compact ring $\mathbb Z_3$ with Haar probability $\lambda$, $g_j$ is the lifted density of the random Syracuse offset at precision **exactly** $j$. The initial residue is immaterial modulo $3^j$, and its law assigns mass $3^{-j}g_j(r)$ to $r$. The projection of this law to depth $m\le j$ is the depth-$m$ law. Tao's Proposition 1.14 says precisely $\|g_j-g_m\|_1\ll_A m^{-A}$ for $j\ge m$, so these nonnegative densities converge in $L^1$ to some $g$ of mean one. [Tao, Forum of Mathematics, Pi](https://doi.org/10.1017/fmp.2022.8)

The map $P(x)=4x+1$ is a single cycle modulo every $3^m$. Indeed $P^i(x)-x=(4^i-1)(3x+1)/3$ has valuation $v_3(i)$ for $i>0$. It is therefore Haar ergodic: the conditional expectations of any invariant function on every finite residue partition are constant. Fix $c>0$ with $\lambda\{g>2c\}>0$. For each $\eta>0$ there exists a fixed $I$ such that all but $\eta/2$ of Haar measure meets $\{g>2c\}$ under some $P^i$, $0\le i\le I$. For all sufficiently large $j$, the complementary depth-$j$ residue set
$$
 E_j=\{x:g_j(P^i x)\le c\text{ for every }0\le i\le I\}
$$
has measure at most $\eta$, by the union bound and $L^1$ convergence.

Suppose $g_q(t)\ge\epsilon q$ along a sequence $q\to\infty$. For every fixed $j$, the fraction of that mass with $x\in E_j$ is controlled in absolute terms by
$$
 t\sum_{x\le t2^{12q},\ x\bmod3^j\in E_j}1/x+o(1)
 \le 12t(\log2)\lambda(E_j)q+O_{j,t}(1).
$$
This uses ordinary harmonic summation on fixed arithmetic progressions. Choose $\eta$ small enough that at least $\epsilon q/2$ remains for each fixed sufficiently large $j$, once $q$ is large. If $U^qx=t$ and $q\ge1$, then $U^q(P^i x)=t$, as the first forward valuation increases by $2i$ while the first successor is unchanged. The slope of that suffix becomes $4^{-i}J_w$. For one fixed $i$ the map is injective. Choosing one good $i$ for each retained source can thus give at most $I+1$ copies of any translated source. The exact decomposition into a $j$-step prefix and $q$-step suffix yields
$$
 g_{q+j}(t)\ge {c4^{-I}\epsilon\over2(I+1)}q .
$$
The positive coefficient is independent of $j$. Sum over an arbitrarily large **fixed** number of consecutive good depths $j$, then take $q\to\infty$ along the same sequence. This contradicts (1). This proof yields sublinearity only at a fixed ordinary target. Neither a pointwise density limit nor an oversampled Fourier estimate was assumed.

## Positive cumulative trace at one seed from the predecessor construction

If an ordinary divergent orbit exists, there is a divergent odd unit $a$ (advance one odd step if needed). Mazur's September 2026 paper, Lemma 2.3 and Proposition 3.1, constructs a fixed sufficiently large odd seed $R$ in the selected unit class which reaches $a$ and has no positive return. For every sufficiently large $X$, its proof of (4.5) gives a set of selected legal words ending at this same $R$ whose sources lie in $[X,32X)$ and whose total of slopes is at least a fixed $\eta_R>0$. This last statement is stronger than the paper's concluding lower density of predecessors and uses the **retained** weights in its proof. [Mazur, Positive Lower Density of Collatz Predecessors](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

Their lengths are $O_R(\log x)$ for physical source $x$. Here is how the needed qualification follows from the written construction. In Appendix A.2–A.3 the central restrictions and the terminal block restriction of the preceding paper are retained. The last-valuation reduction leaves all block lengths unchanged and the terminal excess is zero or one. Write $b_j$ for the successive barrier scales. Each block has at most $b_j+\lfloor3b_j/5\rfloor$ letters. In the derivation of (7.2) of the preceding paper the seed enters as $\log M$ and through $M\ge16^{b_0}$. One may choose $R$ above that fixed threshold before choosing $X$. The growth estimate $\log x\ge (2569/9000)\sum_j b_j$ uses the per-block inverse affine bounds and the one terminal shift. Its derivation precedes any use of the step from the special seed to $1$. If one keeps the initial-scale terms as fixed constants the same inequality with an additive $O_R(1)$ suffices. Hence the total depth is at most $6\log x+O_R(1)$. [Mazur, Explicit Positive-Density Collatz Convergence in Logarithmic Time, Section 7](https://www.proofatlas.ai/formalizations/explicit-positive-density-collatz-convergence/)

Take disjoint shells $[32^i,32^{i+1})$ up to $\exp(Q/7)$. Every selected word in them ends at $R$ within $Q$ steps. Words across these shells have distinct sources. Summing the retained mass gives
$$
 \liminf_{Q\to\infty}Q^{-1}\sum_{q<Q}g_q(R)>0.\tag{3}
$$
The operation uses no uniformity in $R$ and needs just this one seed in a hypothetical divergent component.

## The finite scalar

If every orbit reaches $1$, every word ending at $t_w>1$ follows a simple path. When its odd inputs all exceed $H$, the product identity $F_w/t_w=1-\prod_{i<Q}(1+1/(3U^ix))^{-1}$ makes the ratio at most a quantity $e(H)\to0$, by the uniform simple-orbit reciprocal tail. For odd inputs this bound also follows by extending to the shortcut orbit: a repeated shortcut state before the endpoint would force a repeated cycle, which here would have reached $1$. Such words contribute at most $O(e(H))$ to the normalized scalar by the raw harmonic bound. The other endpoints lie in the finite union of the forward orbits of $s\le H$. Their normalized contribution tends to zero by (2). The cycle indicator vanishes, so letting $H$ tend to infinity proves $C_Q\to0$. If only $\liminf C_Q=0$ is wanted, (1) alone suffices on these finite endpoint sets by averaging $Q$ over $[M,2M]$. [Simple-orbit reciprocal bound](../critical-orbit-mellin/CRITICAL_MOMENT.md)

If an orbit escapes, take the seed $R$ in (3). For $y_j=U^jR$, $1\le j\le Q$, all endpoints are distinct and exceed one. For large $Q$ they lie within $2\cdot3^Q$ by the upper bound $(R+1)(3/2)^j$. Every length-$Q$ word obtained by prefixing this suffix with a length-$(Q-j)$ history ending at $R$ has $F_w/y_j\ge1/(3R+1)$. The suffix satisfies $J(R,j)/y_j\ge c_R/R>0$ uniformly by the simple-orbit reciprocal bound. Their contribution to the uncut first moment is thus bounded below by a fixed positive multiple of $Q^{-1}\sum_{q<Q}g_q(R)$. The discarded words with a letter exceeding $2Q$ cost at most $Q(3/4)^Q$ before normalization by the geometric union bound. This proves the positive lower limit. Finally, a nontrivial periodic orbit gives an eventually positive indicator in the same finite array, using the geometric decay of its repeated lap multiplier. The finite threshold and its exclusion of simple paths are as in the original two-scale test.
