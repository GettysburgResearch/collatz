# Survival above a floor on the positive rational source mesh

Let $a\ge2$, $N=2^k$, $f_{N,a}(x)=N^{-1}\mathbf1_{[a,N]}(x)$, and set

$$
 K_a f(y)=\mathbf1_{y\ge a} K(\mathbf1_{[a,\infty)} f)(y),
 \qquad K f(y)=\frac{\mathbf1_{y>1/2}}3
     \sum_{e\ge0} f\big(2^e(2y-1)/3\big).
$$

Sample $u$ uniformly from $1,\ldots,N3^r$. Start at $u/3^r$, and record the state after each successive odd departure, including its preceding halvings. Then $w_r^a(y)=K_a^r f_{N,a}(y)$ at positive integer $y$ is the joint probability of endpoint $y$ and of every recorded state, including the origin, being at least $a$. The probabilities have their original normalization. This follows by the disjoint positive-numerator preimage partition at each remaining denominator. The barrier tests the recorded states, and suffices for any whole ordinary component lying above the floor. [Pointwise mesh arithmetic](../parity/LITERAL_ENTRANCE_KERNEL.md)

**Fixed-floor estimate.** Write $D=2-\log_2 3$, $r_*=k/D$, $r=r_*+h$ integer. For $k\to\infty$, $0<h=o(k)$, there is $u_0\asymp h/k$ such that for every integer $a\ge32$ and integer $y\ge a$, with absolute constants,

$$
 w_r^a(y)\le C\exp(-c h^2/k)y^{-1-u_0},
 \qquad
 \sum_{y\ge a}w_r^a(y)
 \le C u_0^{-1} a^{-u_0}\exp(-c h^2/k).                            \tag{1}
$$

At the single fixed floor $32$, total survival therefore tends to zero if $h/\sqrt{k\log k}\to\infty$. At growing floors and any fixed $0<\varepsilon<1$, $k=\lfloor a^\varepsilon\rfloor$, $r=\lceil r_*+M\sqrt{k\log a}\rceil$, sufficiently large fixed $M$ gives survival $o(1/a)$. Both conclusions use an elementary positive-operator estimate.

**Proof.** For $s>0$ write $L_s(y)=y^{-s}$ and $\rho_s=3^{s-1}/(2^s-1)$. Summing the geometric series gives $KL_s(y)=\rho_s(y-1/2)^{-s}$ for $y>1/2$. Take $q=3/2$. When $y\ge32$,

$$
 \rho_q(1-1/(2y))^{-q}
 < \frac{442}{465}\left(\frac{64}{63}\right)^2
 = \frac{1810432}{1845585}< \frac{99}{100}.
$$

Indeed $\sqrt3<26/15$ and $\sqrt2>24/17$. Since $\rho_1=1$, choose $\bar u\in(0,1/2)$ such that $\rho_p\ge199/200$ for $1\le p\le1+\bar u$. For $y\ge32$ the exact leading-power image is at most $\rho_p y^{-p}+C_1y^{-p-1}$, uniformly in this range. The auxiliary power has a fixed margin of at least $1/200$. Since $p+1>q$, there is one absolute $C_2$ for which the positive function

$$
 V_p(y)=y^{-p}+C_2 y^{-q}
 \quad\text{satisfies}\quad
 K_a(\mathbf1_{[a,\infty)} V_p)\le
     \rho_p\mathbf1_{[a,\infty)} V_p \quad(a\ge32).                 \tag{2}
$$

Set $p=1+u_0$. On $[a,N]$, $N^{u_0}V_p(x)\ge 1/N$; the initial subprobability is bounded by $N^{u_0}\mathbf1_{[a,\infty)}V_p$. Positive iteration costs at most $\rho_p^r$. The derivative of $\log\rho_p$ at $1$ is $-\log(4/3)$, so

$$
 u_0\log N + r\log\rho_{1+u_0}
 \le -h u_0\log(4/3)+C_3 r u_0^2 .
$$

Take $u_0$ a sufficiently small positive constant times $h/r$. Since $V_p(y)\le(1+C_2)y^{-p}$ on $y\ge1$, the integral test gives (1). The auxiliary power absorbs the full $+1$ affine correction even at a fixed floor. A single telescoping test $H_p(x)=(1+x)^{-p}-(1+2x)^{-p}$ would instead give $K_aH_p/H_p\le\rho_p(1+C/a)$ on $y\ge a$, introducing $O(k/a)$ in the exponent. [Earlier telescoping estimate](RATIONAL_ENTRANCE_KERNEL.md)

**Sharp total survival down to floor one.** For $\sqrt k\ll h=o(k)$ the normalized mass on the entire rational source mesh surviving the floor $1$ satisfies

$$
 \sum_{y\ge1} K_1^r f_{N,1}(y)\le C\exp(-c h^2/k).                 \tag{3}
$$

The matrix bound (1) also gives individual high-floor endpoint decay. The new total bound follows already from the initial binary precision of the rational *numerators*. For $\lambda=\log_2 3$ one has $\log_2(N3^r)=2r_*+\lambda h$. Take $t=\lfloor2r_*+5h/4\rfloor$, $d_0=\lfloor r_*+h/4\rfloor$ and $d=\lfloor r_*+h/2\rfloor$. The first $t$ shortcut parity bits of the genuine rational seed $u/3^r$ have total variation distance at most $2^t/(N3^r)$ from independent fair bits. Indeed, for any fixed odd denominator, each parity word identifies one initial numerator class modulo $2^t$ by the successive invertible odd multipliers. Its count through $N3^r$ differs from the equal count by at most one. Tracking a fixed denominator through the shortcut steps or cancelling factors of three gives the same parities.

Couple these bits with an infinite fair sequence, whose waiting times between odd departures are independent $E_i$ with $\Pr(E_i=e)=2^{-e}$ for $e\ge1$. Put $S_j=\sum_{i\le j} E_i$. The event $S_d>t$ costs $O(\exp(-c h^2/k))$ by the geometric Chernoff bound since $t-2d=h/4+O(1)$. Throughout the first $d$ completed departures on the matching event, the genuine path from $u/3^r\le N$ is bounded above by the path from $X_0=N$ on the same fair digits:

$$
                       X_i=3\,2^{-E_i}X_{i-1}+1/2.
$$

This monotone domination does not require the genuine seed size to be independent of its digits. At date $d_0$, write $X_{d_0}=N3^{d_0}2^{-S_{d_0}}+B_{d_0}$, where $B_j$ follows the same recursion from zero. The event that the first term exceeds one costs $O(\exp(-c h^2/k))$, since $2d_0-(k+\lambda d_0)=(2-\lambda)h/4+O(1)$. Both Chernoff estimates follow from the finite moment generating function $\mathbb E e^{sE}=e^s/(2-e^s)$ around zero. The contribution from $B_{d_0}$ obeys $\sup_j \mathbb E\sqrt{B_j}<\infty$, since for $x\ge0$ a fair step satisfies

$$
 \mathbb E_x\sqrt{X_1}\le \gamma\sqrt x+1/\sqrt{2},\qquad
 \gamma=\frac{\sqrt3}{2^{3/2}-1}<1 .
$$

There are absolute $C_0>0$ and $\delta>0$ such that $\Phi(x)=C_0+\sqrt x$ obeys $\mathbb E_x[\Phi(X_1)\mathbf1_{X_1\ge1}]\le(1-\delta)\Phi(x)$ for all $x\ge1$. Choose $R$ with $(1-\gamma)\sqrt R>2/\sqrt2$. For $1\le x\le R$ a sufficiently large fixed digit forces $X_1<1$ with probability at least some $p_R>0$. Choose $C_0p_R>2/\sqrt2$. On the compact interval the drop in expected $\Phi$ is at least $C_0p_R-1/\sqrt2$. Above $R$ it is at least $(1-\gamma)\sqrt x-1/\sqrt2$. The ratio of each lower bound to $\Phi(x)$ has a positive infimum on its interval. Iterating over $d-d_0$ independent future steps, with $X_{d_0}\le1+B_{d_0}$ on the good event, bounds survival there by $O((1-\delta)^{d-d_0})$. Together with both clock errors and the binary coupling error, this proves (3).

On the opposite side of the same clock, take $r=r_*-h$ with $\sqrt k\ll h=o(k)$. Rational survival now has probability at least $1-C\exp(-c h^2/k)$ at every floor $a\le2^{Dh/2}$. Indeed the numerator precision is $k+\lambda r=2r+Dh$. Couple the first $t=\lfloor 2r+Dh/2\rfloor$ bits. With loss $O(2^{-Dh/4})$ the genuine starting value is at least $N2^{-Dh/4}$. The coupled fair clock satisfies $\max_{i\le r}(S_i-2i)\le Dh/4$ outside probability $O(\exp(-c h^2/k))$, by the exponential maximal inequality for the centered geometric sums with parameter proportional to $h/k$. Both events are enforced by a union bound. Then $S_r\le t$ for large $k$, and $k+\lambda i-S_i\ge3Dh/4$ through every $i\le r$. Omitting the positive affine increments furnishes the lower bound $X_i\ge2^{Dh/2}$ for the genuine states, starting from their genuine positive seed. Thus the rational source populations on the two sides have opposite survival limits at floor one.

For comparison, *every* ordinary positive origin survives the same floor at *every* stopping depth. Thus the entire ordinary invariant set, with zero departing edges, has native survival one and rational survival tending to zero. The actual component of $1$ alone has positive native lower density by the stated predecessor theorem and gives the same qualitative discrepancy. These examples use floor $1$. The [one-edge controls](ONE_EDGE_ENTRANCE_CONTROL.md) have unbounded floors and one genuine departure. A statement for whole components avoiding the verified core would have to use that arithmetic condition.

A rational recorded state below $1$ can also lead to any specified ordinary target $y\ge1$. Choose $j\ge1$ with $(3/2)^j<y+1<2(3/2)^j$, possible since these intervals overlap and contain every integer $y+1\ge2$. Put $u=2^j(y+1)-3^j$. Then $0<u<3^j$, and the formal seed $u/3^j$ has $j$ consecutive odd shortcut departures leading to $y$: the successive state plus one is $(2/3)^{j-i}(y+1)$. At $i<j$ its reduced numerator is odd and denominator odd, as required. This is an existence statement about an actual positive rational prehistory; it gives no uniform lower bound on its mesh probability.

**What the native population would require.** If $B$ is a union of complete ordinary components, so $\mathbf1_B(n)=\mathbf1_B(Tn)$ at every positive integer, and if all its elements are at least $a$, then at every $y\in B$ with $y\equiv2\pmod3$ the odd integer $(2y-1)/3$ and its whole doubling column are also in $B$. Their steps to $y$ preserve the mark. Consequently for $w_d^a=K_a^d f_{N,a}$,

$$
 \frac{\#(B\cap[1,N])}{N} -\sum_{y\in B} w_r^a(y)
 =\sum_{d=1}^r\sum_{y\in B}(3\mathbf1_{y\equiv2\ (3)}-1)w_d^a(y).        \tag{4}
$$

If a nonconvergent ordinary component exists, all its members exceed 31 since these finite starts converge. Taking the single fixed floor $a=32$, its positive native predecessor lower density at any one ternary unit target gives a positive lower limit on the left-hand side as $k\to\infty$. Every component contains such a unit, since iterating halvings to an odd value and then making an odd departure reaches a ternary unit. This applies to escape and cycles. At a large least bad source $a$, the uniform reciprocal predecessor lower bound would give $c/a-o(1/a)$ at the growing scales above. The rational term is small for the whole surviving population in both cases by (1). An upper estimate for the accumulated signed term in (4) strong enough to contradict this lower bound remains open. Every native orbit in a whole bad component survives this floor at every date. The unbounded-floor physical examples each have one genuine exit from their mark. [Physical one-edge control](ONE_EDGE_ENTRANCE_CONTROL.md) · [Ordinary reciprocal count and external provenance](https://rstation.ai/problems/collatz/papers/12)

**Where the trit discrepancy accumulates.** Take the recorded-state floor $a=1$ and the complete ordinary mark $B=\mathbb N_{>0}$. Use the original unconditioned mesh normalization in $w_d^1$, and write $H_d=\sum_y w_d^1(y)$. Let $d_\pm=\lfloor r_*\pm h\rfloor$, with $\sqrt k\ll h=o(k)$. The one-step form of (4) gives $H_{d-1}-H_d=\sum_y(3\mathbf1_{y\equiv2\ (3)}-1)w_d^1(y)$. Applying the two sides of the critical-clock estimate yields

$$
 \sum_{d_-<d\le d_+}\sum_y(3\mathbf1_{y\equiv2\ (3)}-1)w_d^1(y)
 =1+O\bigl(\exp(-c h^2/k)\bigr).                                    \tag{5}
$$

The critical window alone carries asymptotically one unit of signed trit mass on this actual invariant mark.

More generally, fix any floor $a$ and ordinary set $F$ whose natural density $d(F)$ exists. At $r=d_-$ the killed rational endpoint mass in $F$ tends to $d(F)$. To see this, take the typical subcritical words retained above. Their widths $Y=N3^r2^{-S_r}$ are at least $2^{Dh/2}$ after adjusting bounded endpoints. Their intercept $B_r$ is $o(Y)$ outside probability $o(1)$, by the uniform square-root moment and the genuine-to-fair prefix coupling. For a fixed completed word the native numerator in $[1,N3^r]$ runs over one class modulo $2^{S_r}$. Its terminal ordinary integers thus run through *every* integer in $(B_r,B_r+Y]$, once each and with equal conditional weight. The fraction in $F$ tends uniformly to $d(F)$ when $Y\to\infty$ and $B_r/Y\to0$, by the definition of natural density. Discarding the killed histories changes total mass by $o(1)$ by subcritical survival. At $d_+$ the total surviving mass tends to zero for fixed $a\ge1$. Consequently, for any fixed complete component mark $B$ of natural density lying above such a floor, its signed critical-window flux in (4) tends to $d(B)$. This last limit is for a fixed set and floor; no uniform rate in growing targets follows.

This is a written derivation. No local Lean check of these estimates is claimed.
