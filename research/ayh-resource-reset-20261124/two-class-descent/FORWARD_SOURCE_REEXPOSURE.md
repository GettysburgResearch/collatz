# Forward re-exposure of an actual pair after an intermediate clock

This counting consequence of [adaptive paired projection](ADAPTIVE_PAIRED_PROJECTION.md) transfers estimates available separately on ordinary intervals for every incoming canonical offset. The offsets may be selected by the actual past. No independent replacement of either arm is involved.

Let the common parameter $n$ range uniformly over $[N_0,N_0+N)\cap\mathbb Z$, with integer endpoints. The two initial arms are $3^{a_i}n+b_i$, $a_i\ge0$, with integer offsets and positive values on the interval. Pick a deterministic first clock $t\ge1$, put $H=2^t\le N$, and take $L\ge1$, $0<\alpha<1$. For a **fixed** count vector $(p_1,p_2)$ after the first clock, put $g_i=a_i+p_i$, order by grade, breaking ties by label, and write
$$
   \lambda=3^{g_{\rm hi}},\quad \nu=3^{g_{\rm lo}},\quad
   \rho=\lambda/\nu=3^s,\quad F=H/\lambda,\quad V=N\nu/H,
   \quad c_i=3^{p_i}b_i/H.
$$
At its true clock-$t$ outputs the original pair has the exact orientation
$$
 z=Y_{\rm lo},\qquad Y_{\rm hi}=\rho z+D,
$$
with integer $D$. Allow any collection $\mathcal G$ of acceptable count vectors satisfying $F\ge1$ and $V\ge L+1$. Discard all sources whose counts fall outside it. For a vector in $\mathcal G$ define the fixed real interval
$$
 I_p=[\nu N_0/H+c_{\rm lo},\ \nu (N_0+N)/H+c_{\rm lo}+L].
$$
Its length is $V+L$. For every integer $D$ in
$$
 [c_{\rm hi}-\rho c_{\rm lo}-\rho L,\ c_{\rm hi}-\rho c_{\rm lo}+L]       \tag{1}
$$
prescribe an arbitrary event $B_{p,D}(z)$ on the future started from $(z,\rho z+D)$, in the inherited labeling. The event may depend on the full integer $z$; points for which either coordinate is nonpositive can simply be omitted. Assume for each vector and offset the **ordinary integer** bound
$$
       \#\{z\in I_p\cap\mathbb Z:B_{p,D}(z)\}\le\delta V.        \tag{2}
$$
Then the probability that the actual source's own future satisfies its specified event is at most
$$
 \Pr(p\notin\mathcal G)
 +C_\alpha L^{-\alpha}+2H/N
 +C(t+1)^2 L^2\delta.                                               \tag{3}
$$
Only (2) is an external future-event hypothesis. It can depend on $t,N$ and the original family. No uniformity in a larger offset range than (1) is needed. In particular a statement about independent pairs, or one averaging offsets with unspecified unequal weights, does not yield (2).

Indeed tile the original interval by complete $H$ blocks plus at most two partial ends. Outside relative mass $C_\alpha L^{-\alpha}+2H/N$, both scalar affine intercepts $e_i$ from the previous theorem belong to $[0,L]$. On these original sources $z\in I_p$ and (1) follows exactly from $D=c_{\rm hi}-\rho c_{\rm lo}+e_{\rm hi}-\rho e_{\rm lo}$. Hence there are at most $1+(1+\rho)L\le3\rho L$ possible offsets at the fixed counts. For each specified $(z,D)$ the high endpoint is fixed. Its scalar equation confines all original $n$ to one interval of diameter $LF$, regardless of the number of original binary blocks. Thus the multiplicity **over the entire original interval** is at most $1+LF\le2LF$. Inserting (2), multiplying the three bounds, and using $\rho F V=N$ yields $6L^2\delta N$ per count vector. There are at most $(t+1)^2$ vectors. This proves (3).

### A new binary window beyond the initial bit budget

If $B_{p,D}$ is determined by the first $k$ parities/parameter bits from the new lower source, the exact canonical profile with fixed $D$ realizes the complete residues modulo $2^k$. Suppose its uniform-word event has probability at most $\delta_0$ for each permitted vector and offset. Counting complete $2^k$ periods and at most two endpoints in $I_p$ proves (2) with
$$
 \delta\le 3\delta_0+2\max_{p\in\mathcal G}2^k/V,
$$
also for a separately chosen $k=k(p)$ obeying this bound. More generally any event dominated by such a word test obeys the same bound. A target in a word test must be fixed under the fresh uniform grid, or may be predictably chosen within it if its cited bound allows this. The incoming pair itself retains its original offset, both actual coordinates and both orbit colors.

For example take $d=\log_2N$, fixed initial slopes, $t=\lfloor c d\rfloor$ with $0<c<1$, and both counts in $t/2\pm\eta t$. Their complementary probability is $O_\eta(e^{-c_\eta t}+H/N)$ by the scalar grid. Write $a=1-\frac12\log_2 3$. For small fixed $\eta>0$, $F\ge 2^{(a-\eta\log_2 3)t-O(1)}$ and $V\ge 2^{d-(a+\eta\log_2 3)t}$. Thus $V\ge L+1$ for $L$ any fixed power of $d$. One may take
$$
       k=\lfloor d-(a+\eta\log_2 3)t-\eta d\rfloor .
$$
For $\eta$ sufficiently small in terms of $c$, the aggregate physical deadline $t+k$ strictly exceeds $d$ by a fixed multiple of $d$. The second window does not ask the original integer for more independent low bits than it has: (3) proved a one-sided counting bound instead, retaining its two actual trajectories. Uniform errors $\delta_0=O(d^{-A'})$ of arbitrarily high inverse-polynomial order remain arbitrarily high inverse-polynomial errors in original mass, by first choosing $L$ large enough for the target order and then $A'$ large enough to absorb $(t+1)^2L^2$. An unconditioned root that is polynomially rare can also absorb the resulting discard by division by its actual mass.

The extension controls events with a sufficiently strong *one-profile* bound. An ordinary square-root two-arm survival estimate has neither the necessary arbitrary-power decay nor a uniform small prefactor for large inherited $s$. In particular (3) gives an actual additional window for sparse tests and does not supply a summable failure estimate for the two terminal basin colors.
