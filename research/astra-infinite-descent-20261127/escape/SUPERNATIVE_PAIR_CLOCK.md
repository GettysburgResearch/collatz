# Two-clock meetings slightly beyond the source bit length

Put $I_J=[2^J,2^{J+1})\cap\mathbb N$ and give this set uniform mass $\mathbb P_J$. For $n\in I_J$ and nonnegative integer $K$, let $E_K$ mean that there is no equality $T^i n=T^l(3n+2)$ for any $0\le i,l\le K$. These clocks may differ. Write $q_i(x)$ for the number of odd inputs among the first $i$ shortcut steps. A counted meeting occurs when $T^i n=T^i(3n+2)$ and $q_i(n)=1+q_i(3n+2)$. The initial formal count of the higher trajectory is one.

Under the scalar synchronization results cited below, the actual two-clock search on these positive sources satisfies

$$
 \mathbb P_J(E_{J+h_J})\sim\frac{\kappa_{1,2}}{\sqrt J}
 \qquad(0\le h_J=o(\sqrt J)).                                      \tag{1}
$$

At $h_J=\lfloor c\sqrt J\rfloor$ for fixed $c\ge0$, the probability is $\Theta_c(J^{-1/2})$. More generally, at $h_J=\lfloor\eta\sqrt{J\log J}\rfloor$ for fixed $\eta>0$,

$$
 \liminf_{J\to\infty}\frac{\log\mathbb P_J(E_{J+h_J})}{\log J}
       \ \ge\ -\tfrac12-\eta^2 .                                   \tag{2}
$$

In particular the harmonic sum of these finite failures over all octaves diverges when $\eta<1/\sqrt2$. For $\eta=1/\sqrt2$ (2) does not decide convergence. Constants and probability claims in this note are written deductions from external scalar theorems. The exact finite integer crossing, slope separation and persistence implications are kernel checked in [AsynchronousGuard.lean](AsynchronousGuard.lean).

## Actual crossings at unequal clocks

Let $G_i(x)=3^{q_i(x)}/2^i$. The usual integer affine numerator identity gives

$$
 T^i(x)=G_i(x)(x+b_i(x)),\qquad
 b_i(x)=\sum_{s<i,\,T^s x\ {\rm odd}}2^s/3^{q_{s+1}(x)}.           \tag{3}
$$

Let $K=J+o(J)$ with $K\ge J$. Apart from a proportion $O(J e^{-2\sqrt J})$ of $I_J$, simultaneously for $x=n,3n+2$ and $0\le t\le J$ we have $|q_t(x)-t/2|\le J^{3/4}$. Indeed the first $J$ parity bits form a uniform word separately for each $x$. Both $n$ and $3n+2$ traverse complete residue systems modulo $2^J$. Hoeffding's inequality and a union bound suffice and require no independence between the words. Past $J$ each extra step changes a count by zero or one. Hence $q_t(x)=t/2+o(J)$ uniformly through $K$ on this event. All little-oh terms in this paragraph are uniform for the given sequence $K$.

Put $D=1-\tfrac12\log_2 3>0$. Equation (3) gives $\log_2 G_t(x)=-Dt+o(J)$ and $0\le b_t(x)\le K2^{DK+o(J)}$. For any meeting at $i,l\le K$,

$$
 \frac{G_i(n)}{3G_l(3n+2)}
     =\frac{n+(2+b_l(3n+2))/3}{n+b_i(n)}
     =1+O(2^{-(1-D)J+o(J)}).
$$

Taking logarithms first gives $|i-l|=o(J)$, and the count bounds then give $|q_i(n)-q_l(3n+2)-1|=o(J)$. The ratio on the left is exactly $2^{l-i}3^{q_i(n)-q_l(3n+2)-1}$. A ratio of these powers has reduced denominator $2^{o(J)}$. If unequal to one its distance to one is at least the reciprocal of that denominator, which contradicts the preceding display. Unique prime factorization now gives $i=l$ and $q_i(n)=q_l(3n+2)+1$. This holds simultaneously for all pairs of clocks on the single good event. No quantitative theorem on linear forms in logarithms is needed. The use of integer separation for two different trajectories has more distant precedents in affine first-passage comparisons. [Weaver, paper 194, equation (18)](https://rstation.ai/problems/collatz/papers/194)

## Transfer through the last native bit

Use Haar measure on $\mathbb Z_2$ for this paragraph. Write $\sigma$ for counted fusion, $k_t=|1+q_t(3x+2)-q_t(x)|$ and $U_t$ for the absolute canonical offset divided by $3^{k_t}$. The starting canonical state is $(1,2)$. Leen's theorem for a fixed integer canonical state gives

$$
 Q(t)=\mathbb P(\sigma>t)=\kappa_{1,2}t^{-1/2}+o(t^{-1/2}).
$$

The coefficient is positive. On $x\equiv0\bmod4$, two steps put the actual pair at $(u,9u+2)$ with formal counts $(0,2)$ and fresh Haar parameter $u=x/4$. The gap must reach one before fusion. Its mixed-step height above one starts at one and is a simple symmetric walk up to its first hit on zero. Ordinary time dominates mixed time, giving the usual positive inverse-square-root lower bound. We also use a scalar remaining-time bound $A\sqrt{(1+k^2+\log(2+U))/(s+1)}$ and the one-step fractional-moment contraction, which gives $\sup_t\mathbb E U_t^\alpha<\infty$ for any fixed $0<\alpha<1$. These are precise fixed-state inputs for the ordinary shortcut clock. [Leen, *Exact rates in Collatz synchronization*](https://doi.org/10.5281/zenodo.23268751) · [Weaver, scalar estimates (3)–(5)](https://rstation.ai/problems/collatz/papers/124/v1) · [Weaver, retained mixed-step clock](https://rstation.ai/problems/collatz/papers/13)

For $h=o(\sqrt J)$ choose $s=o(J)$ with $h^2+\log J=o(s)$. On $\{\sigma>J,\ k_J\le h,\ U_J\le J^P\}$, the probability of remaining unfused for $s$ more steps is $o(1)$ uniformly. The mass of this set is therefore at most $(Q(J)-Q(J+s))/(1-o(1))=o(J^{-1/2})$. Markov's inequality, with $P\alpha>1/2$, controls the discarded offset tail at the same order. It follows that

$$
 \mathbb P(\sigma>J,\ k_J>h)=Q(J)-o(J^{-1/2}).                      \tag{4}
$$

Both events $\{\sigma>J\}$ and $\{\sigma>J,\ k_J>h\}$ depend only on the residue of $x$ modulo $2^J$. The two words are fixed on such a residue. When the formal counts match, lifting $x$ by $2^Jz$ shifts the two endpoints by exactly the same amount, so equality or inequality within that cylinder is preserved. Thus (4) transfers **exactly** to $n\in I_J$. No event involving the unknown continued Haar bits after $J$ is being transferred.

For such surviving integers with $k_J>h$, the formal counts cannot match by $J+h$, since their signed difference changes by at most one a step. An earlier counted meeting would persist. Except for the exponentially small set in the preceding section, any actual two-clock meeting in this square would be counted. This gives the lower bound in (1). The upper bound follows because a counted meeting through $J$ is already a meeting in the square. See the finite lemma named *no_meeting_from_gap* in [AsynchronousGuard.lean](AsynchronousGuard.lean).

## Larger surviving gaps at the native clock

Return to the residue $n\equiv0\bmod4$ and the state $(2,2)$ after two steps. Put $r=J-2$, fix $0<\delta<1/2$, and let $u=\lfloor(1-\delta)r/2\rfloor$, $v=\lceil(1+\delta)r/2\rceil$. Before its first hit on zero, the height $H$ of the gap above one on mixed clocks is a simple symmetric walk from one. Let $S_m$ be the physical time of its $m$-th mixed step measured from entry into this state, and let $\zeta$ be its mixed hitting time.

On $\{\zeta>v\}$ the probability mass of either $S_u>r$ or $S_v\le r$ is $O_{\delta,\gamma}(\exp(-c_{\delta,\gamma}r^\gamma))$ for any fixed $0<\gamma<1$, by Weaver's surviving-prefix clock lemma (25). For the $S_u$ estimate enlarge the event to $\{\zeta>u\}$. Dependence between the physical waits and the walk is allowed. [Weaver, Lemma 7](https://rstation.ai/problems/collatz/papers/13)

For $h=\lfloor\eta\sqrt{J\log J}\rfloor$, require $H_u$ to lie in $[h+C\sqrt r,\ h+(C+1)\sqrt r]$ with the appropriate parity and require $H_m>h$ for every $u\le m\le v$. For a sufficiently large fixed $C$, a walk started in this window has probability bounded below by a positive constant to satisfy the latter condition, by the maximal inequality for its centered increments. Before $u$, with $p_u(z)$ the unrestricted simple-walk mass of displacement $z$, reflection gives

$$
 \mathbb P(\zeta>u,H_u=y)
   =p_u(y-1)-p_u(y+1)
   =\frac{2y}{u+y+1}\,2^{-u}\binom{u}{(u+y-1)/2}.
$$

For all the allowed $y$ in the window, Stirling's formula gives the binomial mass $r^{-1/2-\eta^2/(1-\delta)+o(1)}$. Here $y^2/(2u)=(\eta^2/(1-\delta)+o(1))\log r$ and $y=O(\sqrt{r\log r})$ keeps the quartic error $O(y^4/u^3)=o(1)$. Multiplying by $2y/(u+y+1)$ and summing a constant multiple of $\sqrt r$ parity-compatible values gives mass at least $r^{-1/2-\eta^2/(1-\delta)-o(1)}$. For $h=\lfloor c\sqrt J\rfloor$ the same computation gives a positive constant times $r^{-1/2}$, without a power loss.

After discarding the stretched-exponential clock errors, $S_u\le r<S_v$ and the height at physical time $r$ exceeds $h$. The implied physical event that the pair at clock $J$ has survived with gap exceeding $h$ uses only the first $J$ bits. It transfers exactly, even though its Haar lower bound used additional bits. Reinstate the residue factor $1/4$, the integer crossing guard and the deterministic $h$-step persistence. Taking the logarithmic liminf first, then $\delta\downarrow0$, proves (2). The upper bound for the square-root window still follows from $Q(J)$. Since $\sum_{n\in I_J}e_{J+h}(n)/n\ge \mathbb P_J(E_{J+h})/2$, the strict inequality $\eta<1/\sqrt2$ gives the asserted divergence.

## Remaining interval

Formula (1) estimates actual finite searches, even with unequal clocks. For the same source pairs, true nonmeeting is bounded above by $Q(J)=O(J^{-1/2})$. Available proofs allow this harmonic cost to be infinite. The new lower bounds concern the cost of the *finite deadline*. They do not give a lower bound on the eventual failure indicator. A summable estimate for the true meetings, even on one specified cone, would have the consequence in [the dyadic budget](README.md). Positive density of the two possible fates would give a weak limiting color density and almost-everywhere changes in that cone. Promoting this to a contradiction requires further ordinary-integer arithmetic.
