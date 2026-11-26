# Original-source incidence of regenerated smaller head edges

Write $a_j=81^{-j}\#\{7\cdot81^j\le x<8\cdot81^j:f(x)\ne f(\lfloor x/81\rfloor)\}$ for any shortcut-invariant color $f$. Use the regenerated chains in [ROUNDED_HEAD_DESCENT.md](ROUNDED_HEAD_DESCENT.md) and the companion original-source low-grade theorem [ACTUAL_FRONTIER_OCCUPATION.md](ACTUAL_FRONTIER_OCCUPATION.md). Put $R=81^j$, $d=\log_2 R$ and $L=\sqrt{d\log d}$. For $A>1$, $L\le B\le d/4$, and sufficiently large $j$,

$$a_j\ll_A d^{-A}+\frac{\sqrt{\log d}}{B}
\sum_{\substack{z\in\bigcup_{l\ge0}[7\cdot81^l,8\cdot81^l)\\B-O(1)\le \log_2 z\le 2B+O_A(L)}}
\frac{{\bf1}_{f(z)\ne f(\lfloor z/81\rfloor)}}{z}.\tag{1}$$

One good original-source sample works for all $B$ in this range. The sum is bounded by a constant times the sum of the corresponding smaller $a_l$, including the two boundary rows. No factor exponential in the physical grade enters this estimate.

## A bounded intercept at many witnesses

For either original scalar arm $n$, write $I_t=T^t n-3^{p_t}2^{-t}n$. This nonnegative affine intercept obeys exactly $I_{t+1}=A_{e_t}(I_t)$, $I_0=0$, using $A_e(w)=(3^ew+e)/2$. Before the common $M=d^D$ entrance the sliding scalar growth tests and the geometric sum in [HIGH_GRADE_SHADOW.md](HIGH_GRADE_SHADOW.md) give $I_t\le d^{C_2}$. Enlarge the block length $b=\lceil C_A\log_2d\rceil$ of ROUNDED_HEAD_DESCENT as needed. Its scalar forgetting test makes the zero-start proxy and full-history $I_t$ differ by at most one throughout the last half of each inspected block outside an exponentially small scalar word event.

Let $\delta>0$ be the lower success frequency on the fixed candidate schedules in ROUNDED_HEAD_DESCENT. We may require that at most $\delta N/4$ of the $N$ upper candidates have $I_t>E$ for a fixed constant $E$, at an extra scalar word cost $O(e^{-cN})$. Indeed at these deterministic times the restarted scalar square-root proxy $V$ satisfies $\mathbb E[V'\mid V]\le\rho V+B_1$ for fixed $\rho<1,B_1$, by iteration across the gaps. Put $G(V)=1+c_0V$, choose $\eta>0$ with $e^\eta\rho<1$, and then $c_0>0$ with $\log(1+c_0B_1)<\eta\delta/8$. For large enough $K$ and $V>K$ this gives $e^\eta\mathbb E[G(V')\mid V]\le G(V)$; for $V\le K$ the expectation is at most $(1+c_0B_1)G(V)$. Iterating yields

$$\Pr\left(\#\{i:V_i>K\}\ge\delta N/4\right)\ll e^{-\eta\delta N/8},$$

because the initial expected $G$ after burn-in is bounded. Set $E=K^2+1$ and use uniform forgetting to return to $I_t$. The scalar-grid transfer costs the same $O(Rd^{-A})$ as before. At most $\delta N/2$ upper truncation certificates fail, and at least $\delta N$ lower marks succeed. Thus at least $\delta N/4$ of the candidates in each good high-grade block supply regenerated chains and have actual upper intercept $I_t\le E$. This is a fixed positive fraction of the block's physical clocks, uniform in $j,B$ and the color.

## Counting in the two directions

Let $t_2,t_1$ be the first clocks at which either arm lies below $2^{2B},2^B$, respectively. Both occur by the common polylog-floor stop. Since a positive shortcut divides by at most two, $t_1-t_2\ge B-O(1)$. Before $t_1$ both heights are at least $2^B$. The arm landing at $t_2$ has height below $2^{2B}$ there. It can rise by at most a factor $d^{C_3}$ until $t_1$: full scalar sliding blocks above $M$ contract, and the remaining $O(\log d)$ steps grow by at most two each. By the simultaneous partial-odd-count bound the grade $s_t$ is at most $C_AL$ through $t_1$. On high-grade windows the larger-grade endpoint is at most $2^{2B+C_AL}$: $Y=3^{s_t}(X-W)$, the smaller-grade arm is the smaller physical value here, and $|W|$ is polynomial in $d$.

Partition $[t_2,t_1)$ into successive length-$b$ blocks, dropping a possible terminal remainder. Any block beginning with $s<4b$ stays in $s\le5b$. On a discordant source the pair never symbolically absorbs. The pathwise low-grade occupation theorem bounds the total length of such blocks by $O_A((\log d)^5)$ outside $O(Rd^{-A})$ original children. Every other block offers the positive fraction of good witnesses established above. Hence each good discordant source offers at least $cB$ distinct physical clocks. At every one choose any discordant child $z$ in the regenerated chain. For the larger-grade endpoint $U_t$,

$$2^B/2\le z\le2^{2B+C_AL},\qquad z=\lfloor U_t/3^u\rfloor,\qquad 0\le u\le s_t\le C_AL.\tag{2}$$

The exponent includes the initial adjustment of at most three trits. Count one incidence per source and chosen physical time.

Conversely fix $(t,z)$ and which original arm $n$ is upper. Put $p=p_n(t)$. Since $0\le U_t-3^p2^{-t}n\le E$, (2) confines the actual original source to

$$n\in 2^t3^{-(p-u)}[z-E,z+1].\tag{3}$$

For fixed $(t,z)$ and arm at most one integer $p-u$ gives an interval meeting the original sample: the sample endpoint ratio is $8/7$, distinct intervals differ by multiplicative factors of at least three, and $(z+1)/(z-E)=1+o(1)$. The length is $O(R/z)$ independently of the trit depth. For each fixed initial suffix convert (3) back to the original parent parameter and enlarge the resulting interval to length comparable to $R/z$ if needed. Here $\log_2(R/z)\asymp d$ by (2) and $2B\le d/2$. Actual discordance implies failure of the original pair's symbolic fusion at depth $\lfloor\log_2(R/z)\rfloor+O(1)$. The uniform complete-grid pair bound on that interval costs $O(R/(z\sqrt d))$ sources for the given $(t,z)$. There are only two arm labels and 81 suffixes. No fair law at a selected landing is used.

Finally $\log_2 n=d+O(1)$, $p=t/2+O_A(L)$ and $u=O_A(L)$. Taking logarithms in (3) shows

$$\log_2(2/\sqrt3)t=d-\log_2z+O_A(L).$$

At most $O_A(L)$ clocks therefore charge the same smaller head $z$. Sum the source bound over these clocks and the discordant targets in (2), divide by the $cB$ incidences per good discordant source and then by $R$, and obtain (1).

The estimate does not contract the total weighted discrepancy. For example a profile $a_l\asymp l^{-1/2}$ is consistent with its scale dependence. A stronger multiplicity bound or a new restriction on the colors of these smaller heads is needed for universal convergence.

## Distinct smaller edges from one original source

The $cB$ incidences supplied by one good discordant source in this proof have **different smaller child heights**. Write $z,z'$ for any chosen children at distinct marked times $t,t'$. From (3),

$$\log n=t\log2-(p-u)\log3+\log z+O(1/z).$$

The corresponding original upper arms are either the same or their logarithms differ by $\pm4\log3+O(1/R)$, since $x=81m+r$. Subtracting therefore expresses $\log(z/z')$ as $(t'-t)\log2-k\log3$ with integer $k=O_A(d)$, up to $O(1/z+1/z'+1/R)$. The published two-logarithm separation used in [LANDING_WEIGHT_TRANSFER.md](../joint-renewal/LANDING_WEIGHT_TRANSFER.md) gives a lower bound $c_A d^{-\nu}$ for the absolute value of this nonzero linear form, with fixed $c_A,\nu>0$. Here $t'\ne t$, all exponents are $O_A(d)$ and multiplicative independence excludes zero. Since $z,z'\ge2^{B-1}$, the displayed errors are smaller than half the lower bound for large $d$. Consequently $|\log(z/z')|\gg_A d^{-\nu}$. The incidence recurrence (1) itself does not need this Diophantine input.

For any fixed nonempty open mantissa interval $J\subset(7,8)$ the same construction gives $c_{A,J} B$ distinct returned discordant heads in this band with $z/81^l\in J$. Choose the interior rotation arc in ROUNDED_HEAD_DESCENT within $J$ with a positive margin; the effect of any subsequent floor on the normalized mantissa is $O(2^{-B})$ since every selected head remains above $2^{B-1}$. The constants and source exception may depend on $J$. A finite family of such requirements can be imposed simultaneously by a union bound on the original exceptions.

## A global criterion on separated logarithmic bands

Fix a nonempty open $J\subset(7,8)$ and $0<\varepsilon<1$. Suppose some strictly increasing unbounded sequence $L_i$ satisfies $L_{i+1}\le L_i^{2-\varepsilon}$ eventually. For the basin-of-one color it suffices to prove

$$\sum_{\substack{z/81^l\in J\ \text{for some }l\ge0\\ L_i/2\le\log_2z\le3L_i}}
\frac{{\bf1}_{f(z)\ne f(\lfloor z/81\rfloor)}}{z}=O(1/L_i)\quad\text{for all large }i.\tag{4}$$

Indeed the whole incidence proof can use only regenerated heads in $J$, by the preceding interior-arc modification. Given $d$, take the largest $L_i\le d/4$. The next term exceeds $d/4$, so $L_i\ge(d/4)^{1/(2-\varepsilon)}\gg\sqrt{d\log d}$. The entire target range in (1) with $B=L_i$ then lies within (4). We get $a_j\ll_A d^{-A}+\sqrt{\log d}\,L_i^{-2}$, summable over all $j$. Under the source-qualified fixed-target positivity used in [MACROSCOPIC_PAIR_CLOSURE.md](../literature-step/MACROSCOPIC_PAIR_CLOSURE.md), the one-arc rigidity theorem for the basin-of-one color now forces universal convergence. Thus (4) is a sufficient actual-color estimate even for sequences such as $L_{i+1}\asymp L_i^{3/2}$. Neither the incidence theorem nor the fixed-target input proves (4).
