# The entire ternary density profile along an ordinary escape

Suppose \(y_j=U^j y_0\) is a positive odd escaping ray. Let \(S_j\) be its original total division clock, \(A_j=3^j2^{-S_j}\), and \(F(x)=\prod_{i\ge0}3U^ix/(3U^ix+1)\) on this component. Thus \(A_j=y_jF(y_0)/(y_0F(y_j))\to\infty\) in the reals and \(v_3(A_j)=j\). Interpret the same rational \(A_j\) in the ternary argument and as a positive real density normalizer. There is a single nonnegative measurable field \(D\) on \(\mathbb Q_3\), determined almost everywhere by the original ray, such that on every compact ball about zero,
\[
                    D_j(u):={\rho(y_j+A_j u)\over A_j}
                          \ \uparrow\ D(u)                              \tag{1}
\]
almost everywhere for all sufficiently large \(j\). On each such ball the convergence also holds in the Banach weak-square norm (thus in every \(L^p\) norm, \(1\le p<2\), for normalized Haar). This uses the actual physical division clock to rotate the local ternary coordinate. Arbitrarily rotating charts at successive times would lose the increasing coupling.

Give \(y_j\) grade \(j\) and write \(V_v\) for the complete set of positive odd members of this component of grade \(v\); the grade is uniquely defined by eventual fusion and simplicity. For each \(x\in V_{-k}\) and every sufficiently late \(j\), the unique path from \(x\) to \(y_j\) has length \(j+k\) and weight \(A_{x,j}=3^{j+k}2^{-S_{x,j}}\). The exact relative slope stabilizes as the positive rational
\[
       r_x=A_{x,j}/A_j=\frac{F(x)y_0}{xF(y_0)},\qquad
                              v_3(r_x)=k.                              \tag{2}
\]
The second expression uses the identity for the physical products and agrees with the first at every late \(j\), not just asymptotically. On \(3^k\mathbb Z_3\) the full field is
\[
                D(3^k\zeta)=\sum_{x\in V_{-k}}r_x\,
                    \rho\big(x+(3^k/r_x)\zeta\big),                   \tag{3}
\]
and its mean there is \(\sum_{x\in V_{-k}}r_x\). This also specifies how the expressions at different grades fit into one field.

Indeed for \(n=j+k\ge0\) the true inverse-word formula for \(D_j\) gives the right side of (3) restricted to the positive sources that have already joined \(y_j\). These subsets increase to the whole grade. The affine maps in each term preserve ternary Haar on the \(\zeta\) coordinate. The reciprocal sum \(\sum_{x\in V_v}F(x)/x\) is finite uniformly over \(v\). On units this follows from the conserved grade mass \(\sum F(x)h(x)/x=H_C\) and the unit floor \(h(x)\ge\alpha\); each nonunit maps to a unit one grade later, with the sum of incoming slope factors at most three. Thus \(\sum r_x\) is finite. Positivity gives the almost-everywhere increasing limit, and the Banach weak-square norm of any omitted sum is at most \(N(\rho)\) times its omitted total weight. Countably many \(k\) and \(j\) suffice to fix simultaneous versions. The local convergence and (3) follow. [Grade conservation and its elementary cofinal proof](ORDINARY_COLLISION_ENERGY.md) · [Fixed-root local word identity](ORDINARY_LEBESGUE_POINTS.md)

The field has the following critical tail in every chart. Write \(T_{x,k}(z)=(r_x/3^k)(z-x)\), a ternary affine isometry. For full Haar \(m\) on the unit chart and for the stationary tilted law \(\sigma\),
\[
 t^2 1_{\{D(3^k\zeta)>t\}}dm(\zeta)
     \ \Rightarrow\ \kappa\sum_{x\in V_{-k}}r_x^2(T_{x,k})_*\sigma.    \tag{4}
\]
The terms in this finite measure are pairwise mutually singular. For distinct \(x,x'\) in this grade, compare the two images by composing the inverse of one isometry with the other. Up to interchanging them this has the form \(z\mapsto2^m z+B\), \(m\ge0\), \(B\in\mathbb Z\), mapping odd integers to odd integers. This follows since the ratios of the \(r_x\)'s on a fixed grade are powers of two, and both physical endpoints are odd. The map cannot be the identity unless its slope is one and \(x=x'\). The tilted law at geometric parameter \(3/4\) is mutually singular with its pushforward by every such nonidentity physical affine map, by the counted-synchronization and decoding result. [Arithmetic affine singularity, including the parameter above the entropy threshold](../../machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md)

Each term in (3) has the [single-density angular tail](JOINT_ANGULAR_TAIL.md) with its displayed weight and location. Mutual singularity then makes pairwise simultaneous exceedances of any fixed positive fractions of \(t\) have mass \(o(t^{-2})\): any weak limit of their rescaled measures is bounded by both singular limits. Thus at a fixed finite set of terms a single large summand accounts for the tail. The omitted sum has weak-square norm at most \(N(\rho)\sum_{x\ {\rm omitted}}r_x\). Bracket the full tail on a cylinder by a finite partial tail at thresholds \((1-\epsilon)t,t\) plus the omitted event at \(\epsilon t\); its scaled mass is \(O(\epsilon^{-2}(\sum_{\rm omitted}r_x)^2)\). Exhaust the grade, then take \(\epsilon\downarrow0\), proving (4). This argument also gives (4) with every finite-depth included set for \(D_j\), and its coefficients converge in total variation to the limiting angular measure in (4).

With \(c_0=H_C y_0/F(y_0)>0\), the [ordinary weak-square differentiation result](ORDINARY_WEAK_SQUARE_DIFFERENTIATION.md) and the moving grade estimates give
\[
            N(D(3^k\,\cdot))\to0\quad(k\to-\infty),\qquad
            N(D(3^k\,\cdot)-c_0)\to0\quad(k\to+\infty).
\]
To justify these iterated limits via the moving statement, at each chosen \(k\) take \(j\) large enough to approximate that ball's field in norm by (1), with error tending to zero along the chosen sequence of \(k\)'s; \(h(y_j)/A_j\to c_0\). The exact coefficient at positive \(k\) consequently tends to zero; equivalently \(\sum_{x\in V_{-k}}r_x^2\to0\). At any fixed \(k\), (4) has positive mass because the grade has a unit ancestor, so the strong second moment on every chart is infinite.

The global Haar volume on \(\mathbb Q_3\) of \(\{D>t\}\) is infinite for **each fixed** \(t>0\), although its fraction in growing centered balls tends to zero. On the chart \(3^{-j}\mathbb Z_3\) of Haar volume \(3^j\), (3) contains the ray vertex \(y_j\) with coefficient \(1/A_j\). Therefore
\[
  m_{\mathbb Q_3}\{u\in3^{-j}\mathbb Z_3:D(u)>t\}
           \ge 3^j m\{\rho>t A_j\}
           \sim\frac{\kappa3^j}{t^2A_j^2}
           \ge (1-o(1))\frac{\kappa}{t^2}(4/3)^j .
\]
Here \(A_j\le(3/2)^j\). The fraction tends to zero by the negative-\(k\) norm limit. This profile is constructed conditionally from an actual positive escape. Its necessary local and global properties alone do not establish existence or impossibility of such a ray.

The crossover has a direct global check. Extend each \(D_j\) by zero outside its full domain \(3^{-j}\mathbb Z_3\). The true main branch makes these zero-extended fields increasing almost everywhere on \(\mathbb Q_3\). Exactly,
\[
   m_{\mathbb Q_3}\{D_j>t\}=3^j m\{\rho>A_jt\}
                       \sim \kappa 3^j/(A_j^2t^2)\quad(t>0\text{ fixed}).
\]
The complete growing-domain exceedance volume is therefore already compatible with the global weak-square tail. A ball of fixed chart radius \(3^R\) corresponds at time \(j\) to an ordinary congruence class of spacing \(3^{j-R}\); for height on the order of \(y_j=O_{y_0}((3/2)^j)\), a fixed \(R\) provides no physical interval equidistribution. Positive-source counting would require control on expanding charts with \(R\) at least on the order of \(j-\log_3 y_j\). Fixed-chart convergence gives no uniform approximation on that scale.
