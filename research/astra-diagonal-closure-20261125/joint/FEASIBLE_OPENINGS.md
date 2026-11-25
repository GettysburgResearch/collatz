# Jointly attainable opening seeds without the required row height

**PROPOSED written extension of the trit-grid obstruction, for positive witnesses of unrestricted height.** The two arms are the actual orbits from the *same* positive parent $n$ and $81n+u$. The parameter $d$ still specifies the target row, clocks and grid. The positive parent constructed below need not satisfy $7\cdot81^j\le81n+u<8\cdot81^j$ at $d=\log_2(81^j)$. Consequently this result does not give a lower bound for the physical-parent statistic of that row.

Use the notation of [the grid theorem](README.md), including $a_0=\lfloor d/2\rfloor$, $h=\lfloor d/3\rfloor$, $\Delta_\tau=\lceil KW\rceil$, $m=\lfloor 3^{k_0}2^{-t_0}n\rfloor$, and the opening cell $(v,\ell)=(n\bmod2^{a_0},m\bmod2^{\Delta_\tau})$. The bounds on the two initial exponents may be chosen with sufficiently large fixed constants in their $O(W)$ grade envelopes, and the opening corrections with a sufficiently large fixed polynomial bound. All estimates are uniform in the suffix $0\le u<81$.

**Claim.** On a fraction $\gg d^{-1}$ of all opening cells there is a single positive ordinary $n$ of unrestricted height realizing the displayed native residue and coarse prefix whose two *physical* opening seeds have grade gap at least $8\sqrt d$ and satisfy the interior and correction requirements of the diffusive-separation theorem for, say, $A=1$. The same pair of seed parameters can be realized on *every* grid residue completing that opening, by an appropriate positive ordinary parent for that completion. A bounded menu admitting these physically witnessed seeds and using the formal four-trit query paths therefore still has $P_d(h)\gg d^{-1}$ for the sufficiently small mark fraction in that theorem, even with the genuine native-survival test. The proof concerns arithmetic upper events with the row's public coarse-coordinate checks on its chosen grid representatives. It does not give true invariant-color replies.

### Steering until a prescribed grade

Given a native prefix of length $j$, each current arm is an integer-affine function of the next quotient, with odd coefficient. Orient them by the exponents of three in those coefficients. At positive level $s$, the larger-slope arm $Y$ and smaller-slope arm $X$ satisfy $Y=3^sX+D$ over the whole remaining cube, with a known integer $D$. Either parity of $X$ can be specified by choosing the next native bit.

Write $L=\nu_2(3^s-1)$. If $D$ is odd, choose $X$ even. Then $Y$ is odd and the next grade difference is $s+1$. If $D$ is even and nonzero with $\nu_2(D)\le L$, choose both arms even until $D$ becomes odd. Each step halves $D$ and leaves $s$ fixed. In the other even case, including $D=0$, choose both arms odd once. The new offset is $(3D+1-3^s)/2$ with valuation exactly $L-1$, since $2^{L+1}\mid D$. Another $L-1$ joint-even steps then make the offset odd. Thus each increase from $s$ to $s+1$ requires at most $L+1$ chosen bits.

For odd $s$ one has $L=1$. For even $s$, $L=2+\nu_2(s)$: an odd exponent factor leaves the valuation of $3^{2^k}-1$ unchanged, squaring $3$ first gives valuation three, and each subsequent squaring adds one since $3^{2^k}+1\equiv2\bmod 8$ for $k\ge1$. In particular $\sum_{s=1}^{S-1}(L+1)\le3S+\sum_{s\le S}\nu_2(s)\le4S$. The last bound follows by summing $\lfloor S/2^j\rfloor$ over $j\ge1$. From any initial positive level below $S$, at most $4S$ prescribed native bits suffice to attain level $S$.

### Scalar and joint control on actual prefixes

On the full native grid modulo $2^{a_0}$, the signed-grade second-moment estimate in [the grid theorem](README.md) gives fraction at least $16/(16+a_0)$ of residues with nonzero grade difference. For either physical arm let $B_j$ be the additive real correction to its own initial ordinate,
\[
 T^j x=3^{p_j(x)}2^{-j}x+B_j,\qquad B_0=0 .
\]
It obeys $B_{j+1}=(3^\epsilon B_j+\epsilon)/2$. Both arms separately have fair scalar parity words on this grid. The square-root contraction from the grid theorem bounds $\mathbb E\sqrt{B_{a_0}}$ by a constant on each arm. Discard from all native residues the set with either $B_{a_0}>d^8$, of fraction $O(d^{-4})$, and those with either $|p_{a_0}-a_0/2|>4W$, of fraction $o(d^{-2})$ by the binomial exponential moment. There remain $\gg d^{-1}$ of all native residues, with a positive level after orienting, polynomial corrections, and both grades in the prescribed range.

Fix such a residue. Set $S=\lceil16\sqrt d\rceil$. Use the steering proof if its current level is below $S$; otherwise use no prescribed bits. At most $4S$ bits have been added, and they are fixed before the remaining bits are drawn. The number $j_*$ of native bits fixed at this point satisfies $j_*\le a_0+4S<t_0$ for large $d$. Each arm's absolute grade, including the child's initial grade four, is within $4W+2S+4$ of $j_*/2$. Its correction satisfies
\[
              B_{j_*}+1\le(3/2)^{4S}(d^8+1).
\]
This follows directly from $B_{j+1}+1\le(3/2)(B_j+1)$ for either parity.

Draw the remaining native bits through $\tau$ uniformly. Denote their number by $T=\tau-j_*$, which lies between $2d$ and $3.1d$ for all sufficiently large rows. Retain a fixed orientation from the end of steering and let $Z_T$ be the signed difference of the resulting two absolute grades. Its conditional variance is at most $T$, because every successive increment has conditional mean zero and conditional second moment at most one. Its conditional mean is the initial gap $s_*\ge16\sqrt d$. Hence $\Pr(Z_T<8\sqrt d)\le T/(s_*-8\sqrt d)^2\le3.1/64<1/20$.

For each arm the remaining scalar odd count is binomial $(T,1/2)$, and it stays within $4W$ of $T/2$ with probability $1-o(1)$ at the opening. Its total native exponent (including the upper arm's initial grade four on $81n+u$) is within $9W+5$ of $\tau/2$ for all large $d$ on these events. Choose public bounds with at least $W$ extra margin; this accommodates the diffusive theorem's subsequent $A\sqrt h/8$ tolerance. A sufficiently large fixed $K$ gives the required rebase positivity and slope bounds.

For either arm the fresh fair scalar law also gives
\[
  \mathbb E[\sqrt{B_\tau}\mid\text{steered prefix}]
  \le \rho^T(3/2)^{2S}\sqrt{d^8+1}+(1-\rho)^{-1}=O(1).
\]
Indeed $\rho<1$, $T\ge2d$ and $S=O(\sqrt d)$. Thus $B_\tau\le d^8$ with probability $1-O(d^{-4})$ after conditioning. The actual coarse seed correction $b_\pm$ is nonnegative and at most $d^8+3$ on the good event. To check it, expand the exact formula above at $\tau$ in the original parent coordinate. For the child arm the suffix contributes $u3^{p_\tau}2^{-\tau}=o(1)$ under the grade bound. Replacing $3^{k_0}2^{-t_0}n$ by its floor contributes less than one since $3^{g_\pm}2^{-\Delta_\tau}\le1$. Taking the coarse floor contributes less than one more. The nonnegative sum of these corrections is an integer in the opening formula. All claimed seed properties together therefore hold for at least $4/5$ of native continuations from the steered prefix for large $d$.

### Recovering the opening and the common future string

Given $n_0=n\bmod2^{t_0}$, write $n=n_0+2^{t_0}Q$. Then
\[
 m=\left\lfloor3^{k_0}2^{-t_0}n_0\right\rfloor+3^{k_0}Q .
\]
Because $j_*<t_0$, the $\Delta_\tau$ bits of $Q$ are still uniform conditional on the first $t_0$ bits, so $\ell=m\bmod2^{\Delta_\tau}$ is uniform. The successful native continuations from each retained $v$ must therefore meet at least $4/5$ of the distinct opening prefixes $\ell$. This gives the claimed $\gg d^{-1}$ measure of opening cells. One successful continuation selects one physical pair of seeds per such cell.

Finally, changing $n$ by $2^\tau k$ preserves all physical parity decisions through $\tau$ and changes $m$ by $3^{k_0}2^{\Delta_\tau}k$. The physical endpoint shifts by exactly the change in its coarse seed formula on both arms, so both opening corrections as well as the exponents are unchanged. Since $3^{k_0}$ is odd, all grid residues modulo $2^H$ completing $\ell$ are realized this way. One may choose a positive witness $n\le2^{\tau+H-\Delta_\tau}$ by using the least positive representative of the corresponding native residue. This bound is far above the original row scale $2^d$. Constraining the lift to the original short interval, or requiring true answers for the formal query paths, remains a separate obstruction.
