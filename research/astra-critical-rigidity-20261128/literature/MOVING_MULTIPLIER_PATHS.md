# Independent ordinary height fluctuations for moving multipliers

Fix finitely many arms and let \(t=\lfloor\log_2 N\rfloor\). At each \(N\) choose distinct positive integers \(c_{1,t},\ldots,c_{B,t}\) prime to six. Their residues and prime factors may change arbitrarily. Assume
\[
                         H=1+\max_b\log c_{b,t}=o(\sqrt t).
\]
Choose \(x\) uniformly from any interval of \(N\) consecutive positive integers. Give each arm a group \(b(i)\) and form the positive ordinary source
\[
             y_i=c_{b(i),t}3^{s_i}x+D_i,\qquad
             s_i/\sqrt t\longrightarrow a_i\ge0,\qquad
             \log(2+|D_i|/3^{s_i})=o(t)
\]
with nonnegative integer \(s_i\) and integer \(D_i\). Require that every arm is positive on the sampling interval. Write \(g_i(k)\) for its actual odd count in \(k\) shortcut steps, \(\gamma=\log_2 3\) and \(b=1-\gamma/2\).

**Proposed theorem.** The linearly interpolated paths \((s_i+g_i(k)-k/2)/\sqrt t\) and \((\log_2 T^k y_i-\log_2 x+bk)/(\gamma\sqrt t)\) converge jointly in \(C([0,1])\) per arm. Each group gives coalescing Brownian motions of variance rate \(1/4\) started at its \(a_i\). Different groups are independent, including when their initial or later positions coincide. At fixed positive observation times the numerical equality partitions within each group have the Brownian limit. The probability of a numerical meeting between different groups at any date through \(t\) tends to zero. These statements hold along every such family of multiplier arrays and interval placements. The [fixed-multiplier theorem](INDEPENDENT_MULTIPLIER_PATHS.md) supplies the compact pair kernel, stationary classification, martingale characterization and ordinary sampling argument.

In particular, any fixed number of distinct moving primes above three of size \(\exp(o(\sqrt{\log N}))\) yield independent Wiener paths from the **same** ordinary sample \(x\). The population result permits any number \(m_t\to\infty\) of distinct integers prime to six with the same uniform height bound. With \(y_i=c_{i,t}x\), the empirical measure of their centered actual log-height paths converges in probability, weakly on \(C([0,1])\), to Wiener measure of variance rate \(1/4\). This also holds for deterministic weights totaling one whose largest weight tends to zero.

## A uniform arithmetic estimate at the possible stationary atom

Compare two different groups under a Haar dyadic lower input. Put \(\alpha_t=c_{b(j),t}/c_{b(i),t}\), and start the raw kernel at level \(h_0=s_j-s_i=O(\sqrt t)\) with its actual dyadic offset. In particular, \(\alpha_t3^h\ne1\) at every integer \(h\). On a subsequence the odd units \(\alpha_t\) tend in \(\mathbb Z_2^\times\) to an odd unit \(\alpha\). Each transition in the [raw formula](INDEPENDENT_MULTIPLIER_PATHS.md) is jointly continuous in the slope and state. Thus \(P_{\alpha_t}f\to P_\alpha f\) uniformly for every continuous \(f\) on the compact raw state space. Bounded martingale telescoping implies that every subsequential random limit of the native empirical occupation measures is \(P_\alpha\)-stationary almost surely.

The only candidate besides product Haar is the absorbing point \((s_*,0)\) when \(\alpha3^{s_*}=1\). The closed subgroup of powers of three consists precisely of the units \(1,3\bmod8\). Indeed the continuous even powers \(9^j\) cover \(1+8\mathbb Z_2\), by \(v_2(9^k-1)=3+v_2(k)\) for nonzero integer \(k\) and finite residue counting. The continuous parametrization \(s\mapsto3^s\) has a continuous inverse on its image. In the possible-atom case, all sufficiently late \(\alpha_t\) belong to this subgroup, and their levels \(s_{*,t}\) with \(\alpha_t3^{s_{*,t}}=1\) converge to \(s_*\).

For \(h\in\mathbb Z\) write \(e_t(h)=v_2(\alpha_t3^h-1)\). Yu's two-factor inequality with last exponent one gives the moving-height estimate
\[
          e_t(h)\le C H\log(2+|h|/H).                                   \tag{1}
\]
For \(h>0\) clear the odd denominator and apply equation (8) of the [two-factor specialization](../ordinary/FIXED_NUMERATOR_LANDING_COMPLEXITY.md) to the coefficients \(c_{b(i),t},c_{b(j),t}\) with the appropriate signs. For \(h<0\) exchange them. At \(h=0\) use the nonzero numerator directly. The constant is absolute. [Yu, *p-adic logarithmic forms and group varieties II*, Theorem 2](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

Let \(L=\lceil\sqrt t\rceil\), assume \(|h_0|\le C_0L\), and partition the levels on either side of \(h_0\) into blocks of \(L\) consecutive integers. On a block at distance \(jL+O(L)\), (1) gives
\[
           \max e_t(h)\ll H\log(2+(C_0+j+2)L/H)=:E_j.
\]
Precisely one residue class at each increasing binary precision can have the higher valuations around \(s_{*,t}\). Indeed \(e_t(h)=2+v_2(h-s_{*,t})\) for \(h\equiv s_{*,t}\bmod2\), by the even-power identity. Thus the sum of \(e_t(h)+2\) over the precision-\(r\) absorbing-level class in that block, for \(r\ge1\), is
\[
                  O((r+1)L\,2^{-r}+r+E_j).                               \tag{2}
\]
This counts at most \(L2^{-l}+1\) representatives at each precision \(l\) up to \(E_j+O(1)\).

Every direction visit to \(h\) costs at most \(e_t(h)+2\) native steps in conditional expectation, for every incoming offset. The embedded direction walk is simple symmetric. Its first \(t\) directions have expected local time at a point of this block at most \(CL\exp(-cj^2)\), adjusting absolute constants at the first blocks. Conditional charging of the whole visit, using the incoming state, bounds the expected proportion of native dates with level \(s_{*,t}\bmod2^r\) by
\[
 C(r+1)2^{-r}+\frac{C}{L}\sum_{j\ge0}e^{-cj^2}(r+E_j).
\]
The final term tends to zero for each \(r\). In fact for \(\eta=H/L\to0\) the log contribution is at most \(C_{C_0}\eta[\log(2+1/\eta)+1]\), using \(\log(2+(C_0+j+2)/\eta)\le\log(2+1/\eta)+\log(C_0+j+2)\). At fixed \(r\) the tested level cylinder eventually agrees with the cylinder at \(s_*\). Taking the occupation limit, then \(r\to\infty\), gives zero mass at the atom almost surely. In both cosets the occupation limit is product Haar.

## From raw occupations to actual paths and populations

On each positive fixed fraction \(u\) of the horizon one still has \(H=o(\sqrt{ut})\), \(h_0=O(\sqrt{ut})\). Test the clopen odd-offset event under the occupation measure. It has product-Haar mass one half. A finite mesh gives vanishing normalized cross brackets uniformly in the horizon fraction. Within a group the relative multiplier is exactly \(3^{s_j-s_i}\) and its initial dyadic affine offset involves only \(D_i,D_j\) and this power. Under Haar the first arm is a uniform unit-affine transform of the original input. The within-group critical first-meeting and coalescence proof therefore applies independently of \(c_{b,t}\). The joint martingale characterization yields independent groups. The shortened cylinder transfer still has an \(O(\log t)\) terminal remainder, since every initial multiplier is an odd integer.

For ordinary real heights the added term \(\log_2 c_{b,t}/(\gamma\sqrt t)\) vanishes uniformly. The exact carry bound and typical lower bound on \(x\) in the [finite-family height theorem](COALESCING_ORDINARY_HEIGHTS.md) still apply, since the multiplier is at least one. To verify numerical separation across groups in the finite-deadline accident estimate, compare \(U=c_{b(i),t}3^A,\ V=c_{b(j),t}3^B\) for the two adjusted terminal grades. If the two numbers are within a factor of two then \(|A-B|=O(H)\), and clearing their common power of three yields distinct integers with maximum at most \(\exp(O(H))\). Hence \(|U-V|/\max(U,V)\ge\exp(-O(H))\). Outside that factor use \(1/2\). In the affine meeting equation this multiplies the earlier per-grade-pair candidate interval length by at most \(\exp(O(H))\). The \(O(2^{3t/4})\) carry bound (enlarging by subexponential factors if necessary), polynomial number of terminal grade pairs and exponentially rare low grades still give \(o(N)\) candidates uniformly over interval placements. Any earlier actual meeting persists to the deadline.

For the population take one and two independent indices from the given weights, independently of the common ordinary sample. A double draw repeats an index with probability at most the largest weight. The one-arm and distinct two-arm laws above hold uniformly over the available choices by the subsequence formulation of the theorem. For any bounded continuous path test, its weighted empirical integral consequently has limiting mean the Wiener integral and limiting variance zero. The one-arm laws supply tightness in expectation. A countable convergence-determining class gives weak convergence in probability of the empirical measures. These growing windows of actual ordinary sources leave a distinguished source's future open.
