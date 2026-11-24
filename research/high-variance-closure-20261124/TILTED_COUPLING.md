# Testing the Haar tilt in the ordinary endpoint moment

**Status.** Exact coupling obstruction and exact ordinary residual. Neither proves nor disproves the exponential bound for the ordinary moment. This continues ORDINARY_MOMENT.md, using the same positive shortcut map and inverse transfer. PR146's fair-digit estimates are pinned there.

For $1<s<2$ put $\lambda=2^{-s}(1+3^{s-1})$, $\theta=3^{s-1}/(1+3^{s-1})>1/2$ and $h=\log(\theta/(1-\theta))$. The contributions of particular words to $\int L_s^k1$ are $(3^j/2^k)^s3^{-j}$, where $j$ is the odd count and $3^{-j}$ is the ternary endpoint Haar mass. On dividing by $\lambda^k$, the parity letters are independent Bernoulli $\theta$. Reversal does not change these word weights.

## Exact one-arm coupling and a positive nonfusion probability

Take a common binary upper parameter, with two actual profiles starting at $3^L n+r$ and $n$, and assign the first arm an initial odd-count surplus $L\ge0$. Choose the full length-$k$ binary grid with the probability of each start proportional to $\theta^{j}(1-\theta)^{k-j}$ for its *first-arm* parity word. Each word occurs exactly once because the initial slope is odd and each unexposed binary digit determines the next parity. The consistent grids also define an atomless dyadic probability. Write $D_t=L+j_1(t)-j_2(t)$.

Given the past, each arm is an integer affine function of the same fresh binary parameter with odd slope. Therefore the two next parities either agree for both possible bits, or disagree for both; this alternative is already known from the past. At a disagreement, $D$ increases by one with probability $\theta$ and decreases by one with probability $1-\theta$. At agreement it is unchanged.

Starting at $D_0=L>0$, stop when $D$ first hits zero. With $u=(1-\theta)/\theta$, the stopped process $u^{D_{t\wedge\tau}}$ is bounded by one and has constant expectation $u^L$, since $\theta u+(1-\theta)u^{-1}=1$. Hence $\Pr(\tau\le k)\le u^L$ for every $k$. Starting instead with the *adjacent* pair $n+1,n$, equal initial counts, the first step is necessarily a mismatch. With probability $\theta$ the first arm gains a unit surplus. Conditional on this event the preceding estimate applies at all later horizons. Thus at every positive horizon the probability of never having equal counts after time zero is at least $2\theta-1$. In the case $s=3/2$ this lower bound exceeds $0.2679$.

This rules out a uniform vanishing upper bound for *actual literal same-clock meetings on arbitrary full ordinary grids* under the same single-arm tilt. For a horizon $k$, take the whole grid above $2\cdot3^k$. At time $t\le k$, the two numerators are $3^{j_1}(n+1)+C_1$ and $3^{j_2}n+C_2$, with $0\le C_i\le3^t-2^t$ by induction. If the counts differ, equality forces $n\le2\cdot3^t$. At time zero the adjacent endpoints are distinct. The finite-grid failure lower bound therefore also applies to literal equality by the deadline. Moving these grids establishes no permanent nonmeeting for a fixed pair of positive ordinary integers.

A tilt deliberately attached to the lower-count arm can improve the orientation until the next tie. It does not preserve the original tilted word distribution. On a shared history at a mismatch the bits are complements, so both conditional marginals cannot be Bernoulli $\theta$.

## A symmetrized Feynman–Kac repair and its compensator

On the fair common grid define $W_i=(2\theta)^{j_i}(2(1-\theta))^{k-j_i}$, the exact density of the $i$th single-arm tilt. Then
$$W_1=\sqrt{W_1W_2}\exp\big(h(D_k-D_0)/2\big).$$
For $\sqrt{W_1W_2}$ the next bit at a match retains the common ordinary bias. At a mismatch the two possible weights coincide, so this gives a fair jump with killing factor $b=2\sqrt{\theta(1-\theta)}<1$. Restoring the required endpoint factor costs $\cosh(h/2)$ on this fair jump. The exact identity $b\cosh(h/2)=1$ spends the entire apparent mismatch contraction. This is the Doob transform from the killed symmetric jump back to the biased single-arm jump. It does not spend the separate Haar factor $\lambda^k$; it generates no further saving with which to estimate the terminal ordinary trace.

## The endpoint projection that a different repair must bound

For each parity word let $r$ be its least positive endpoint modulo $3^j$ (including $r=1$ for $j=0$), and define $Z_s(x)=\sum_{a\ge0}(a+x)^{-s}$. With the same normalized Haar tilt as above,
$$I_k(s)=\lambda^k\,\mathbb E_\theta H_s(w),\qquad H_s(w)=3^{j(1-s)} Z_s(r/3^j).$$
This is the complete positive atomic endpoint sum, obtained by inserting $n=r+3^ja$. In particular the tilted digits alone give no estimate of the required terminal weight. At $s=3/2$ and verified floor $B=20$, the desired bound would need exponential growth rate of $\mathbb E_\theta H_s$ strictly below $(61/60)^{-3/2}/\lambda$ (about $1.01$). The ordinary cycle at 1 already prevents a straightforward Cauchy–Schwarz replacement of this first moment by a second. At $k=2l$ its word starts and ends at $1$, so $j=l,r=1$, $H_s\ge3^l$, and its probability is $(\theta(1-\theta))^l$. Hence
$$\liminf_{l\to\infty}\|H_s\|_{L^2(\theta)}^{1/(2l)}\ge[9\theta(1-\theta)]^{1/4}>1.20\quad(s=3/2).$$
This lower bound is on a higher norm. The contribution of the same word to $I_k$ decays, so this is not a counterexample to the requested first-moment bound.

Equivalently the atomic masses transported forward form a different killed process. The unnormalized mass $m^{-s}L_s^k1(m)$ moves deterministically to $T(m)$, losing the factor $(1+1/(3m))^{-s}$ on odd inputs and retaining all its mass on even inputs. There is no fresh tilted digit conditional on that ordinary $m$. Uniform tightness of the normalized atomic masses would exclude loss of mass to infinity, but obtaining the specified numerical spectral rate also requires sufficiently large repeated killing below an effective cutoff. Neither the tilted nonfusion bound nor the symmetric compensation supplies that estimate.
