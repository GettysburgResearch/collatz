# A binary character sum for the escaping flux on the actual target representatives

Put $\alpha=\log_2 3$, $g=7/4-\alpha>0$ and $H=\sum_C H_C$, with the ordinary escaping components and fluxes of [the stationary trace](SPATIAL_TRACE_TAIL.md). For odd $x$ put $e(x)=v_2(3x+1)$ and $\psi(x)=\min(e(x),3)-7/4$. Its four values in increasing order of odd classes modulo eight are $(1,-3,5,-3)/4$. Let $\rho_N$ be the original all-visit positive row of period $3^N$, of period mean one. The following unnormalized Dirichlet sums converge for each positive integer $N$, and satisfy
\[
 \boxed{\qquad
 -\tfrac34 H\ \le\ \liminf_{N\to\infty}\frac1N
    \sum_{x>0\ {\rm odd}}\frac{\rho_N(x)\psi(x)}x
 \ \le\ \limsup_{N\to\infty}\frac1N
    \sum_{x>0\ {\rm odd}}\frac{\rho_N(x)\psi(x)}x
 \ \le\ -gH .\qquad}                                                \tag{1}
\]
The middle quantities use the actual small positive representatives. In particular a nonnegative subsequential upper limit for this one explicit contrast would exclude every ordinary escaping component. The present estimate proves the upper sign and a gap proportional to any escaping mass. It does not prove that the lower size is $o(N)$. The source inputs for (1) are the original scalar front of PR195 and Tao's fine-trit estimate. The result concerns escape and leaves other possible cycles open. [PR195, full-period scalar harmonic front and its endpoints](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md) · [Tao input and exact row identification](SUMMABLE_ORIGINAL_TRACE.md).

## Averaging the signed front in physical space

On the discrete set of positive odds put $q_k=3^k$ and
\[
 p_k=\sum_{x<2q_{k+1}\ {\rm odd}}\frac{\rho_{k+1}(x)-\rho_k(x)}x\delta_x.
\]
Write $r_{C,n}$, $n\ge0$, for the chosen actual forward ray in each escaping component. The scalar PR195 front approximates $p_k$ in the sum of absolute masses by a moving placement of signed phase masses $\delta_{C,v}$ at $r_{C,k+v}$, omitting negative indices. Its error tends to zero, $\sum_{C,v}|\delta_{C,v}|<\infty$, and $\sum_v\delta_{C,v}=H_C$. An index shift in defining the base depth only translates $v$ and leaves these statements unchanged. The same scalar statement follows from [the marked derivative](VARIATION_PROFILE.md) by taking full mass. Changing its half-period cutoff to the full odd representative system costs at most the mean absolute scalar row difference times an absolute constant, tending to zero. Removing its $F$ correction costs $o(1)$ in the scalar sum norm, since $F$ is uniformly bounded below on simple positive paths and tends to one along each fixed escaping ray. Truncate to finitely many significant phases to make this last statement simultaneous.

A shift of a single ray average by a fixed $v$ costs at most $2|v|/N$ in the variation norm on the **discrete physical sites**, including a truncated negative beginning. Cesàro averaging the front errors, first retaining finitely many phases and then exhausting their absolute summable tails, proves
\[
 \left\|\frac1N\sum_{k=1}^N p_k-
     \sum_C\frac{H_C}{N}\sum_{n=1}^N\delta_{r_{C,n}}\right\|_{\rm TV}
 \longrightarrow0.                                                   \tag{2}
\]
Thus the negative variation tends to zero after this averaging. Spatial test functions in (2) can change with $N$ if uniformly bounded.

On each true escaping ray, $S_n=\sum_{j<n}e(r_{C,j})$ satisfies the exact positive-source identity
\[
 S_n=n\alpha+\log_2(r_{C,0}/r_{C,n})-\log_2 b_n(r_{C,0})
       \le n\alpha+\log_2(r_{C,0}/F(r_{C,0})).                        \tag{3}
\]
Here $F(r_{C,0})>0$ follows from reciprocal packing **on a sequence of distinct positive ordinary vertices**. This inequality need not hold for periodic positive or formal $2$-adic orbits. Since $\psi$ is bounded, (3) gives a limsup average at most $-g$ separately on each escaping ray, and finite-component truncation gives the same bound times $H$ globally. Its pointwise lower bound gives $-3H/4$. Apply (2).

For the last conversion let $B_k=\sum_{0<x<2q_k,\ x\ {\rm odd}}\rho_k(x)\psi(x)/x$. Write $R_k$ for the sum with the same summand on the outside shell $2q_k<x<6q_k$. Then $p_k(\psi)=B_{k+1}-B_k-R_k$. One has $\sum_k|R_k|<\infty$. In fact replace $\rho_k$ there by $\rho_j$ for $j=\lfloor k/2\rfloor$. The error is $O_A((1+k)^{-A})$ for every fixed $A$ by the sum of the adjacent full-period mean differences. The shell comprises exactly two complete odd representative systems mod $q_k$, each denominator exceeding $2q_k$. The remaining signed periodic function $1_{x\ {\rm odd}}\rho_j(x)\psi(x)$ has zero mean over a period $8q_j$, by coprimality and the centered four binary classes. Every partial sum over one period has absolute value $O(q_j)$ because the positive $\rho_j$ has mean one. Summation by parts costs $O(q_j/q_k)$. This proves summability. The identical partial-sum argument at $j=k$ bounds the infinite tail beyond $2q_k$ by an absolute constant and gives convergence by Dirichlet's test. Telescoping now gives (1), with a shift of one in the averaging endpoint. In conventional characters one can take $4\psi=3\chi_{-4}-\chi_8-\chi_{-8}$ on odd integers, where the subscripts denote fundamental discriminants.

## Invariant measures on binary output phases

Regard (2) as measures on the compact odd $2$-adic integers. Every subsequential weak limit $\mu$ is positive, has total mass $H$ and satisfies $\int e\,d\mu\le\alpha H$. For the last assertion first test with each bounded locally constant truncation $\min(e,L)$, setting $e(-1/3)=\infty$. Apply (3) on finitely many components, bound the discarded components by $L$ times their total mass and then let $L$ increase. Thus $\mu$ gives no mass to $-1/3$. The odd acceleration $U$ is continuous away from that one point; define it arbitrarily there. For continuous bounded $f$, the averages of $f\circ U-f$ converge to zero by telescoping on each positive ray. Weak convergence tests this function as its discontinuity set has $\mu$-measure zero. Hence $U_*\mu=\mu$.

For $\alpha<c<2$, at least $(c-\alpha)H/(c-1)$ of $\mu$ lies on a set of $2$-adic Hausdorff dimension at most $H_2(1/c)<1$, where $H_2$ is binary entropy. Indeed the almost-sure limit $E$ of the Birkhoff averages of the integrable $e$ has mean at most $\alpha H$ and $E\ge1$. The claimed mass lies on $E\le c$. Almost every one of these points avoids the singularity and all its preimages by stationarity. Between consecutive odd sites its shortcut clock runs for exactly $e$ steps. The limiting density of odd departures in shortcut time is then $1/E\ge1/c$. The length-$t$ shortcut parity word is bijective with residues modulo $2^t$: for a fixed prefix, the $t$-step multiplier after removing $2^t$ has odd numerator, so lifting the residue by $2^t$ toggles the next parity. Prefixes with at least $(1/c-\varepsilon)t$ odd bits have cardinality at most $2^{tH_2(1/c-\varepsilon)+o(t)}$ for small $\varepsilon>0$. Cover the eventual frequency set and let $\varepsilon$ decrease to zero. Taking $c\uparrow2$ shows that the part singular to odd binary Haar measure has mass at least $(2-\alpha)H$. This assertion concerns output phases. Uniform residues of the *remote inverse source* at a fixed target are compatible with it. [PR215, profinite inverse ancestors](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/machinery/PROFINITE_ANCESTORS.md).

## All last-low flux lies on a defect in binary dimension

For each high floor $M$ use the ordinary last-low sections $E_M(C)$ and the positive rows $a_mF(m)(D_{F(m)})_*\nu_m$ from [the simultaneous stationary disintegration, equation (5)](SPATIAL_TRACE_TAIL.md). Attach to each row its binary coordinate $m$. Each joint weak accumulation point on odd $\mathbb Z_2\times[0,1]$ has real marginal $\sum_C H_C\eta_C$ and binary marginal supported on the single closed set
\[
 \mathcal D=\{z: S_j(z)\le\lfloor\alpha j\rfloor\text{ for every }j\ge1\},
 \qquad \dim_H\mathcal D\le H_2(1/\alpha)<1.                            \tag{4}
\]
Here $S_j$ is the shortcut time to the $j$th next odd site. A missing next landing takes infinite time. Each finite clock condition is clopen, determined by a finite parity prefix.

Indeed $m>(2M-1)/3$, all future odd sites exceed $M$, and these sites on its escaping component are distinct. The uniform bound for the sum of reciprocal heights on a simple positive orbit above $A$ is $R(A)\to0$. Applying (3)'s exact identity at $m$ yields $S_j(m)\le j\alpha+O(R((2M-1)/3))$ simultaneously for every $j$. For each fixed number of conditions the integral clocks therefore satisfy the floor bounds once $M$ is sufficiently large; $\alpha$ is irrational. Intersect these clopen constraints after passing to the limit. The real marginal converges in variation by the stationary disintegration. For $z\in\mathcal D$ the number of odd departures in its first $t$ shortcut steps is at least $t/\alpha-O(1)$, since the times of successive odd departures are $S_0=0,S_1,S_2,\ldots$. The parity-word count just given proves (4). It also proves a finite bound: the total number of possible $m$ in the union of the true $E_M(C)$ is at most $M^{H_2(1/\alpha)+o(1)}$, by testing $t=\lfloor\log_2 M\rfloor$ shortcut bits and allowing the uniform $O(1)$ additive clock slack. A binary residue has at most three positive representatives through $M$ at that scale.

The binary constraints in (4) are compatible with the quadratic-clock exclusions even on a positive-entropy family. Concatenate independently chosen words `110` and `1110`, starting at a block boundary. Among the first $j$ odd gaps at most $\lfloor j/2\rfloor$ are two and all others are one. Thus $S_j\le3j/2<\alpha j$ at every grade. All complete odd runs have length two or three. A strictly increasing arithmetic progression of complete odd-run lengths has at most two terms, at every offset. Even allowing its initial partial run, every prefix pattern in the quadratic-clock theorem has bounded absolute length in this family. The independent binary choices give positive entropy, and the parity bijection realizes these sequences as odd $2$-adic points. This construction makes no claim about positive integer realizations. The clock bias alone therefore cannot force the growing patterns excluded by the positive-integer theorem. [Quadratic-clock bounds on positive ordinary prefixes](../broad/QUADRATIC_CLOCK_PADE.md).
