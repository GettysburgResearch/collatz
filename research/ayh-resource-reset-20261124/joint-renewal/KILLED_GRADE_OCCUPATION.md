# Summable low-level survivors among the actual head children

Take the ordinary positive shortcut map. For an arm starting at $n$, write $p_n(h)$ for the number of odd inputs at clocks $0,\ldots,h-1$. For each $R=81^j$ and each $x=81m+r\in[7R,8R)$, put
$$
  h_j=\lfloor\log_2(R/81)\rfloor,
  \qquad S_h(x)=|4+p_x(h)-p_m(h)|.
$$
This level is the absolute exponent of 3 in the ratio of the two affine slopes at a common clock. It uses the original pair throughout. Results below concern $j\ge2$, with finite initial levels immaterial.

**Theorem.** Let $k_h$ be a nondecreasing positive tolerance. Write $N_j$ for the number of actual children whose two arms have failed to merge symbolically through $h_j$ and satisfy $S_{h_j}(x)\le k_{h_j}$. For every $H\ge 2$,
$$
 \sum_{j:H\le h_j<2H}\frac{N_j}{81^j}
   \ll (1+k_{2H})^2 H^{-1/2}.                                      \tag{1}
$$
The implied constant is independent of the tolerances, landing threshold, row and orientations. In particular, the sum over all rows is finite for $k_h=h^\beta$, $0\le\beta<1/4$, or $k_h=h^{1/4}/(\log(2+h))^{1/2+\epsilon}$, $\epsilon>0$. More generally, the series for this finite certificate converges exactly when $\sum_{h\ge2}(1+k_h)^2 h^{-3/2}<\infty$ for nondecreasing $k_h$, as proved below. Failure to have any common future and having different basin-of-one colors are each subsets of failure of symbolic merger by this deadline.

For the timed first-passage weights $W_j(v,w)$, refine the actual counts into $W_j^{\le k}(v,w)$ by requiring $S_{h_j}(x)\le k_{h_j}$. For the stated choices of $k$,
$$
 \sum_{j\ge2}\frac1{81^j}\sum_{v,w}W_j^{\le k}(v,w)
   {\bf1}_{f(v)\ne f(w)}<\infty.                                  \tag{2}
$$
More strongly, an explicit finite test of symbolic merger by $h_j$ gives the bound in (1), whether or not either first-passage clock precedes $h_j$. Timely entrance is only a further restriction in (2).

## Occupation of a finite range of slope levels

Use the written fair binary model of [PR 146, THREE_RAY_UPPER, frozen source](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md). Its canonical state is $(s,D)$ representing the two arms in either order as $z,3^s z+D$. Kill it at the first visit $\tau$ to $(0,0)$; visits after killing count zero. Let $Z=D/3^s$, $V=\sqrt{|Z|}$. The two ordinary branch updates at positive level multiply $Z$ by $1/2$ and $3/2$, with additive errors of absolute size at most one. At zero with odd offset both absolute multipliers are $1/2$; at zero with even offset the multipliers are again $1/2$ and $3/2$. With
$\rho=(1/\sqrt2+\sqrt{3/2})/2<1$, we consequently have
$$
 \mathbb E[V_{t+1}{\bf1}_{\tau>t+1}\mid\mathcal F_t]
 \le(\rho V_t+1){\bf1}_{\tau>t}.                                  \tag{3}
$$
For the fixed initial states $(4,r)$, $0\le r<81$, PR 146 gives $\mathbb P(\tau>t)\ll (1+t)^{-1/2}$. Iterating (3) proves
$$
 \mathbb E[(1+V_t){\bf1}_{\tau>t}]\ll(1+t)^{-1/2}.                \tag{4}
$$
Indeed the early half of the convolution is $O((1+t)\rho^{t/2-1})$, and the late half is bounded by a geometric sum times $O((1+t)^{-1/2})$.

For an arbitrary entering state, the expected physical occupation before killing satisfies
$$
 \mathbb E_{s,D}\sum_{t<\tau}{\bf1}_{S_t\le K}
   \ll (1+K)^2+(1+K)(1+V),\qquad K\ge0 .                          \tag{5}
$$
Here is the excursion accounting underlying (5). At positive level $l$, the chain of level changes is simple symmetric walk up to its return to zero. Each visit to $l$ has expected physical duration at most $e_l+2$, $e_l=v_2(3^l-1)$. The gambler's ruin Green function before zero is $2\min(s,l)$ visits, whence the initial positive excursion contributes at most $2\sum_{1\le l\le K} l(e_l+2)\ll(1+K)^2$, uniformly in its start. The last inequality follows from $e_l=1$ for odd $l$, $e_l=2+v_2(l)$ for even $l$, and $\sum_{l\le K}v_2(l)\le K$. Rounding $K$ down only decreases the sum.

For completeness, the boundary estimates used here are precisely those in the cited PR 146 proof, paragraphs “Why the offsets at level zero stay controlled” and “Adding the elapsed times”. At the first return from a positive initial level the raw offset satisfies $\mathbb E\sqrt{|D_{\rm ret}|}\le (99/100)^sV+C$. Each further excursion launched from an odd level-zero offset is followed by a boundary coast with expected length controlled by $1+\sqrt{|D|}$. The drift at successive odd boundary offsets contracts their square-root magnitude outside a finite set, and trials in that set absorb with a fixed positive probability. Thus the expected number of further excursions and of boundary-phase steps is $O(1+V)$, also when the initial state is already at the boundary. Further excursions start at level one or at a uniformly bounded level following a finite failed trial; clocks during the trial words themselves are already included among boundary-phase steps. From any bounded level $s_0$ a further excursion contributes at most $2s_0\sum_{l\le K}(e_l+2)\ll1+K$ low-level physical steps. Summing conditional expectations proves (5). Taking $K=0$ counts boundary steps alone.

Apply (5) on the event $\tau>H$ at clock $H$. Using the Markov property and (4) yields the genuinely summable dyadic occupation estimate
$$
 \sum_{h=H}^{2H-1}\mathbb P_{4,r}(\tau>h,S_h\le K)
 \le\mathbb E_{4,r}\bigg[\sum_{h\ge H,\ h<\tau}{\bf1}_{S_h\le K}\bigg]
 \ll (1+K)^2 H^{-1/2},                                           \tag{6}
$$
uniformly in the 81 initial offsets. This bounds a sum over clocks, not the probability of an unweighted union of late return events multiplied by $H$.

## Return to the integer intervals

For $j\ge1$ and fixed residue $r$, the parents form exactly the consecutive interval $7R/81\le m<8R/81$, of integer length $L_j=R/81$. There is no parity-conditioning loss: in a complete block of $2^{h_j}$ parent values the canonical base history is bijective with all binary words of that length. This follows by exposing one base bit at a time: the residual high-quotient coefficient is odd even under an orientation swap. An arbitrary length-$L_j$ interval is covered by at most two consecutive blocks of length $2^{h_j}$ starting at its left endpoint. Consequently the number of parents surviving with the stated level condition divided by $L_j$ is at most twice the corresponding fair-model probability from $(4,r)$. For each $r$, the sampled clocks $h_j=\lfloor(j-1)\log_2 81\rfloor$ are distinct. Sum over $j$ in the dyadic shell, majorize $k_{h_j}$ by $k_{2H}$, and use (6). Averaging the 81 residue bounds proves (1). Summing over $H=2^m$ proves (2), using invariance of the basin color along each physical orbit. In the logarithmically reduced endpoint case the dyadic majorant is $O((1+m)^{-1-2\epsilon})$.

The finite embedded-walk identity is checked in [KilledGradeGreen.lean](KilledGradeGreen.lean). Its theorem visits_add_remainder counts occupation and terminal potential over all binary histories of any given jump length. The theorem weighted_band_visits_le allows arbitrary nonnegative integer rewards by level, as required to insert the physical holding-time bounds. The physical-time comparison, inherited survival and boundary estimates in PR 146, and the dyadic transfer are written proofs.

## Sharp threshold for this finite certificate

For the actual integer counts $N_j$, the converse to the general summability condition holds. Finite symbolic failures include pairs that can merge later or at different physical clocks, so this converse gives no lower bound for different basin colors.

Start the embedded level walk at 4 and stop at its first zero. Before that time it is an ordinary simple symmetric walk $J_l$ and all its physical waiting times are finite almost surely. For all large $l$ and $16\le K\le\sqrt l$, reflection at zero and Stirling's estimate give
$$
  \Pr(\min_{i\le l}J_i>0,\ J_l\le K)\gg K^2/l^{3/2}.                \tag{7}
$$
In detail, let $P_l(k)$ be the unrestricted mass at $k$ from zero. The killed mass at $k>0$ from 4 equals $P_l(k-4)-P_l(k+4)$. For $4\le k\le\sqrt l$ of the correct parity this is a sum of four nonnegative differences, including
$P_l(k)-P_l(k+2)=P_l(k)\,2(k+1)/(l+k+2)\gg k/l^{3/2}$.
Here $P_l(k)\gg l^{-1/2}$ uniformly in this range by Stirling. Sum over matching $k$ in the upper half of the band.

Write $\sigma_l$ for the physical clock of jump $l$ before the first zero, so $\sigma_l\ge l$. The last $h_j\le\sigma_l$ differs from $\sigma_l$ by at most 7. At that row the process is still unkilled and $S_{h_j}\le J_l+7$, since levels move by at most one per clock. If the nondecreasing tolerance is unbounded, set $K_l=\lfloor\min(k_{l-7}/2,\sqrt l)\rfloor$. For large $l$, $J_l\le K_l$ guarantees $S_{h_j}\le k_{h_j}$. At most seven distinct jump clocks can be charged to any one sampled clock, since successive $h_j$ differ by at most seven. Compare the pathwise counts and take expectations to see that the fair-model sum over $j$ dominates a constant times $\sum_l K_l^2 l^{-3/2}$ by (7).

Each actual length-$L_j$ parent interval contains a full block of $2^{h_j}\ge L_j/2$ parents; hence its normalized finite-certificate count **also dominates** one half of the model probability. Retaining any one initial residue $r$ suffices. If $k_{l-7}\le\sqrt l$ eventually, the lower series has the convergence behavior of $\sum_h k_h^2h^{-3/2}$. If $k_{l-7}>\sqrt l$ at arbitrarily large $l$, monotonicity gives a contribution $\gg\sqrt l$ to the lower series from $[l,2l]$, so it diverges. Bounded tolerances already give convergence. In the upper direction the dyadic majorant in (1) is bounded by a constant times the sum of $(1+k_h)^2 h^{-3/2}$ over $2H\le h<4H$, by monotonicity.

Thus $h^{1/4}$ and even $h^{1/4}/\sqrt{\log h}$ give divergent finite-certificate series on the actual head intervals. A stronger claim about the full weighted discordance needs information about the later physical dynamics or about the basin colors.
