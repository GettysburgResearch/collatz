# Strict rank convexity for the full binary physical band

Let an ordinary positive cycle have least odd period $P$, odd minimum $s$, odd maximum $X\le(16s+7)/3$, and all native valuations in $\{1,2\}$. Put $A=\sum e_i$, $h=A-P$, $\theta=A/P$, and $\gamma=\log_2 3$. Use the canonical maximizing root and its grades $z_i=\lfloor i\theta\rfloor-E_i\ge0$, where $E_i$ is the initial valuation sum. Write $r=ih\bmod P$, $c_r=2^{2-z_i}$ and $L_r=c_rx_i$, extending $c_{r+P}=2c_r$ and $L_{r+P}=2L_r$. For all sufficiently large $P$:
$$
 L_{r+2}-2L_{r+1}+L_r\ge1\qquad(0\le r<P).
$$
In particular *every* nonzero rank offset has $P$ distinct positive gap values. For any chronological lag with smaller rank offset $t$ satisfying $\log t/\log P\to0$, its valuation mismatch fraction has lower limit strictly above $1/18$ when the quoted bound $\mu(\gamma)\le3$ is used.

PR200 established strict convexity for canonical height one with arbitrary positive valuations and quantified microscopic mismatches there. Its independent full-width binary all-lag theorem gives a positive qualitative mismatch bound using the 2018 Diophantine input and the integral Subspace Theorem. Here the curvature theorem includes the third grade allowed at the full physical ceiling. Its new seam exclusion uses the progression-free *ordinary* binary past. Our argument uses the integral Subspace Theorem through the established height lower bound $s\gg P^{2+\delta}$ for some $\delta>0$, and uses no finite irrationality exponent for the curvature itself. [PR200, strict convexity](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/cycles/STRICT_CONVEX_RANKS.md) · [PR200, microscopic gaps](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/cycles/MICROSCOPIC_CONVEX_LAG_BOUND.md) · [PR200, full-band all-lag result](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/cycles/CLASSICAL_FULL_BAND_ALL_LAG.md) · [Earlier physical height bound](FOUR_COPY_TAILS.md) · [Ordinary progression theorem](TERNARY_PAST_ENTROPY.md)

## The physical rank and its closed third-grade boundary

The exact positive product gives $0<\theta-\gamma\ll1/s$. At a maximizing discrepancy cut, $f_i+z_i=i\theta-E_i\ge0$. Iteration gives
$$
 \log_2(x_i/x_0)=f_i+z_i+O(P/s),\qquad
 f_i+z_i\le\log_2((16s+7)/(3s))+O(P/s).
$$
Consequently $0\le z_i\le2$, and $z_i=2$ implies $f_i\le2-\theta+O(P/s)$. The phase and $2-\theta$ are both multiples of $1/P$, while $P/s=o(1/P)$. Thus grade two is allowed only at $r\le P-h$, with equality retained.

The rank is simple. If several sites have the same phase, their scaled labels are distinct by their odd parts. The update on each such fiber maps $L$ to $(3L+\operatorname{lowbit}(L))/2^m$ with a common $m$. It is weakly increasing on the eligible integers of lowbit $1,2,4$, since $3$ times any positive integer increment is at least the largest possible lowbit drop. Its restriction to the cycle fiber is injective because the next odd parts are distinct. One mechanical period therefore acts as an increasing permutation of each fiber and fixes it. Primitivity gives $\gcd(h,P)=1$. This is the same-phase ordering of Weaver's Paper 114. Now $f_i=r/P$, $L_r=4x_0 2^{r/P}+O(P)$, and $s\asymp x_0$. The main term grows by $\gg s/P\gg P$ per rank, including across the doubled seam. In particular $G_r=L_{r+1}-L_r>0$. [Weaver, Paper 114](https://rstation.ai/problems/collatz/papers/114/v1)

Set $H_r=L_r-2L_{r+1}+L_{r+2}$. At base rank $r$ record the **unwrapped** lowbit triple $c=(c_r,c_{r+1},c_{r+2})$. Each coefficient in slot $i$ is $2^{\lfloor(r+i)/P\rfloor}(4\mathbin{/}2^z)$ for an admissible grade at $(r+i)\bmod P$. For $r'=(r+h)\bmod P$, let $d$ be its unwrapped triple, and $m=1+\mathbf1_{r+h\ge P}$. Subtracting the three ordinary equations before reducing their common base gives
$$
 2^mH_{r'}=3H_r+c_0-2c_1+c_2,\qquad
 2^md_i\in\{2c_i,4c_i\}.
$$
Each $L_{r+i}$ has exact lowbit $c_i$, hence
$$
 H_r\equiv c_0-2c_1+c_2\pmod{\gcd(2c_0,4c_1,2c_2)}.
$$
Whenever $H_r=0$ and all three $c_i$ agree, division by their common value produces a nonconstant arithmetic progression of actual odd phases. This is impossible by the ternary past theorem. It applies equally at doubled slots because $L$ and its exact lowbit double together.

## The exceptional reverse orbit

A negative curvature leaving the negative integers, or a positive one reaching zero, has $1\le|H_r|\le4$ since all coefficients belong to $\{1,2,4,8\}$ and $|c_0-2c_1+c_2|\le14$. The finite control checks all allowed triples, integer divisors and curvature residues. The only negative exits are
$$
 r=P-h-2\ \text{or}\ P-h-1,\qquad
 (c,H_r)=((4,1,4),-2),\qquad(d,H_{r'})=((4,2,8),0).
$$
In the second case $r'=P-1$ and the doubled middle coefficient is $2c_0=8$ by $z_0=0$. This conflicts with the required middle coefficient two. In the first case retain the displayed initial state at $r=P-h-2$ and evolve backwards by 35 chronological letters. At every step test the ordinary multiplier, the ternary divisibility of the signed numerator and the exact lowbit congruence. Drop equal-lowbit progressions. The last three predecessor-set sizes are $10,2,0$. Thus no negative curvature can leave the negative integers. Since the chronological shift is transitive and $\sum_{r<P}H_r=G_P-G_0=G_0>0$, every curvature is nonnegative.

From a positive curvature reaching zero, the same local enumeration tests the next step, retaining all nonnegative states and rejecting only equal-lowbit progressions at the zero vertices. There are no surviving two-step transitions. Transitivity and the positive sum now exclude zero altogether.

For reproducibility, local tests through two forward edges have cuts $r=-jh-i\bmod P$, $0\le j\le3$ and $0\le i\le2$. These include wraps, native divisors and both sides of the *inclusive* grade cutoff for every needed vertex. Test singleton cuts and an integer in each nonempty intervening interval. At the backward seam all tested ranks are explicitly $-(j+1)h-2\bmod P$, $1\le j\le35$. The sample $P=1000003,h=584964$ represents every calendar in these tests for sufficiently large $P$. Indeed for $\beta\in[584962,584963]/10^6$ and $1\le j\le40$, the checker bounds $j\beta$ strictly between $\lfloor j\beta\rfloor+1/1000$ and $\lfloor j\beta\rfloor+1-1/1000$. Distinct multiples maintain their circular cut order under all offsets of at most four mesh units. Within any coincident-multiple cluster, the offsets have their fixed integer order and spacing. The actual $h/P\to\gamma-1$ is in the bracket eventually. In the 35 backward steps there are no wrapped triples or inclusive-boundary exceptions. Every earlier triple therefore uses the same choice set in all three slots, $\{1,2,4\}$ for $m=1$ and $\{2,4\}$ for $m=2$. The Lean theorem independently evaluates all 35 predecessor sets using those letters and the equivalent modulus $2\min(c_0,2c_1,c_2)$. [Exact local and reverse checker](check_full_rank_curvature.py) · [Integer control](FULL_RANK_CURVATURE_CONTROLS.json) · [Kernel-checked reverse elimination](FullRankCurvature.lean)

## Microscopic lag information

Strict curvature makes each $G_r^{(t)}=L_{r+t}-L_r$, $1\le t<P$, strictly increasing in the fundamental rank, since consecutive such gaps differ by at least $t$. The doubled extension has $G_{r+P}=2G_r$, so $0<G_r<2G_0$ on the fundamental octave and $G_0\le L_0/P\ll X/P$. Consequently $G_r^{(t)}\ll tX/P$ for all fundamental ranks. For uniform rank its entropy is exactly $\log_2 P$.

Let $\epsilon$ be the mismatch fraction at the chronological lag corresponding to the smaller rank offset $t$. In the signed gap recurrence the drift is $\delta_r=2^{c}\ell(z_{r+t\bmod P})-\ell(z_r)$ with $c=\mathbf1_{r+t\ge P}$ and $\ell(z)=2^{2-z}$. Record the mechanical schedule, wraps and grade-cap faces on a window of $b=\lceil\log_3(1+C tX/P)\rceil$ edges for a sufficiently large absolute $C$. They cost $O(\log(b+1))$ bits from their $O(b)$ phase cuts, including both orientations of each threshold. The drift word determines the terminal gap modulo $3^b$ and hence exactly. The corrected profile $w=z_{r+t\bmod P}-z_r-c$ changes by $0$ or $\pm1$ and changes precisely at a valuation mismatch, by differencing the two mechanical date formulae. Its word entropy is at most $O(1)+b[H_2(\epsilon)+\epsilon]$, recording the change mask and signs. At unwrapped sites with both grades at most one the drift is determined by $w$, including $w=0$. At unwrapped sites with a third available grade the drift given $w$ has at most two choices, as $w=0$ still fixes zero. These sites have fraction at most $2-\theta+O(t/P+1/P)$. Wrapped sites contribute only $O(t/P)$ further bits per edge since the alphabet is bounded. Cyclic stationarity consequently gives
$$
 \log_2 P\le O(\log(b+1))
   + b\big[H_2(\epsilon)+\epsilon+2-\theta+O(t/P+1/P)\big].
$$
Here $H_2$ is the binary entropy in bits. If $\mu(\gamma)\le3$, the native product gives $X\le P^{3+o(1)}$ on growing periods. For $\log t/\log P\to0$, $b\le(2+o(1))\log_3 P$. Every subsequential mismatch limit then satisfies $H_2(\epsilon)+\epsilon\ge3\gamma/2-2>3/8$. The strict integer comparison $18^{72}<2^{23}17^{68}$ gives $H_2(1/18)+1/18<3/8$. Monotonicity near zero and compactness yield the stated strict lower limit. [Corrected signed profiles in PR200](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/cycles/CLASSICAL_FULL_BAND_ALL_LAG.md) · [Chudnovsky, Theorem 11.1](https://arxiv.org/html/2610.28079v1#S11)
