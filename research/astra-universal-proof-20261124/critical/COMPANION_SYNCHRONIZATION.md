# High physical states and short companion pasts on the same cycle

**PROPOSED written theorem.** Fix $\rho=3/5$, $\alpha=\log_3 2$ and $\beta=\log_2(3/2)$, so $\beta<\rho<\alpha$. On each sufficiently long primitive positive ordinary cycle, a fixed positive fraction of the **same physical phases** simultaneously have height greater than twice the odd minimum and satisfy the all-pasts record condition of PR205. Their positive companion phases are bounded by a common absolute constant; their length-$k$ physical pasts are distinct for $k$ the least integer with $3^k>Bq$, where $q$ is the exact reduced companion denominator. The phases counted need not themselves be odd.

Use the shortcut map, with physical period $L$, physical phases $x_i$, parity $e_i$, and $p=\sum_{i=0}^{L-1}e_i$ odd phases. The physical minimum $m$ is odd, since an even positive state has a smaller successor. Telescoping gives $L\le2p$ and $L/p=\log_2 3+O(1/m)$. Along any sequence of distinct cycles with $p\to\infty$, the minima tend to infinity: only finitely many cycles can meet any fixed finite set by determinism. Thus $p/L>\rho$ for sufficiently large $p$.

Extend $S_{i+1}-S_i=(e_i-\rho)\log3$ to all integer times. Its drift per lap is positive. The strict record indices $a$ with $S_a>\max_{j<a}S_j$ form a nonempty periodic set modulo $L$. Each satisfies the PR205 inequality on every past. If $a<b$ are consecutive strict records, then $S_t\le S_a$ for $a<t<b$, and $S_b-S_a\le V=(1-\rho)\log3$. In physical logarithmic heights $z_t=\log x_t$ the exact step is
$$
 z_{t+1}-z_t=S_{t+1}-S_t-d+\gamma_t,\qquad
 d=\log2-\rho\log3,\qquad
 \gamma_t=e_t\log(1+1/(3x_t)).
$$
Choose $c=d/2>0$. At large periods, $\gamma_t\le1/(3m)\le c$. Hence the entire interval satisfies $z_{a+j}\le z_a-cj$ for $0\le j<b-a$, and $z_b\le z_a+V-c(b-a)$.

For **any** threshold $H$ put $P_t=\max(z_t-H,0)$ and $I_t=\mathbf{1}_{z_t>H}$. Write $h$ for the number of high times in $[a,b)$. Then
$$
 ch\le P_a-P_b+cI_a+VI_b.
$$
If $I_b=1$, use $P_b\le P_a+V-c(b-a)$ and $h\le b-a$. If $I_b=0$ and $h>0$, the last high time has index at least $a+h-1$, so $P_a>c(h-1)$ and $I_a=1$. If both $I_b$ and $h$ vanish, the bound follows from positivity. Summing record intervals over a whole lap cancels the potentials and proves the stronger arbitrary-threshold statement
$$
 \#\{a\bmod L:a\text{ a strict record},\ x_a>e^H\}
 \ \ge\ \frac{c}{c+V}\#\{t\bmod L:x_t>e^H\}.
$$
At $H=\log(2m)$ the right side exceeds $cL/(42(c+V))$ by the preceding cycle occupation theorem. This synchronization uses the same deterministic orbit on both sides; it does not infer overlap from adding marginal densities. [Cycle occupation theorem](CYCLE_OCCUPATION.md)

For the closed companion on this primitive physical word, the real slopes are $3/2^{1+e_t}$ and the additive term is $e_t/4$. All backward products of $j$ slopes at a strict record are at most $(2^{\beta-\rho})^j$, giving $0<w_a\le B=1/(4(1-2^{\beta-\rho}))$. PR205's fixed-word ternary injection therefore holds on this specific high subset. For clarity, for a $k$-step past of odd count $u$ the ordinary integer numerator satisfies $2^{k+u}qw_a=3^kqw_{a-k}+qC^*$. A fixed past determines $qw_a$ modulo $3^k$; the marked numerators are positive and at most $Bq<3^k$. A primitive physical cycle has a primitive parity necklace: if the word were a proper power, its seed would be fixed by an iterate of an increasing affine return map, hence by that return map itself. Distinct companion phases then follow from primitive-word dyadic legality, so no two marked phases have the same past. [PR205 companion packing, equation (1), frozen 32d722c5d5597846da5dad842c8ea15742abc176](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/arithmetic/README.md)

The denominator in this last injection belongs to the companion. On the physical side, rotating one complete word changes its carry numerator $C_i$ by $2C_{i+1}=3^{e_i}C_i+e_iD$, where $D=2^L-3^p$ and $C_i=Dx_i$. Since $D$ is prime to six, $D\mid C_i$ implies $D\mid C_{i+1}$ and conversely. Selecting a positive proportion of high strict records therefore supplies a simultaneous short-past constraint but only one divisibility test modulo $D$ among all these rotated physical equations. No bound on the reduced companion denominator from the physical denominator one has been established here. No fixed-arity nondegenerate unit equation with all selected phases in a fixed multiplicative group follows from their magnitudes or from the companion packing.
