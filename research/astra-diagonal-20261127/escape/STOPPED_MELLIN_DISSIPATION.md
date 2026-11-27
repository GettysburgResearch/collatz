# All-time variation of the stopped trace in the real defect

**Source-qualified written theorem.** The absolute unmarked stopped increment has a finite sum over all odd clocks and ordinary sites. The same is true of the absolute increment of the original real-prefix distribution integrated against every Mellin weight below its first reciprocal power. At the first power the spatial norm stays bounded, and a single additional cycle gives a persistent signal in a shrinking endpoint band. These statements allow both escaping and periodic counterexamples.

## The unmarked estimate

Write \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers, \(w_x=3x/(3x+1)\), and \(T\delta_x=w_x\delta_{Ux}\). The one-step input is the geometric law \(2^{-e}\), and \(\rho_k(y)\) is the original normalized density modulo \(3^k\), of mean one. Define
\[
 d_k(y)=\frac{\rho_{k+1}(y)-\rho_k(y)}y,\quad
 b_k=\sum_y(1-w_y)|d_k(y)|,\quad q_k=3^{k+1}.
\]
All site sums use positive odd integers. Then
\[
                         \sum_{k\ge0} b_k<\infty.                     \tag{1}
\]
The input from PR195 is the physical truncation \(p_k={\bf1}_{y<2q_k}d_k\) and the bound \(\|p_{k+1}-Tp_k\|_1\le t_k\), where \(t_k=q_k^{-1}\sum_{r\bmod q_k}|\rho_{k+1}(r)-\rho_k(r)|\). Tao's consecutive ternary mixing gives \(t_k\ll_A(1+k)^{-A}\) for each fixed \(A>0\). The truncation estimate uses the dyadic sparsity of discarded parents returning to the next physical period. [PR195, (1)–(3), frozen head](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md) · [Tao, Proposition 1.14](https://arxiv.org/abs/1909.03562) · [Weaver 176, (7)](https://rstation.ai/problems/collatz/papers/176/v1)

Since \(\|Tp_k\|_1\le\sum_x w_x|p_k(x)|\), one has
\[
 \sum_y(1-w_y)|p_k(y)|\le\|p_k\|_1-\|p_{k+1}\|_1+t_k .
\]
For an omitted site \(y=r+2q_kh\) with \(1\le r<2q_k\) odd and \(h\ge1\), its stopped denominator satisfies \(y(3y+1)\ge12q_k^2 h^2\). The entire omitted cost is at most \(\zeta(2)t_k/(12q_k)\). Telescoping proves (1), including the target 1. This does not assume uniform cancellation across different sites.

## A marked inequality that still uses the original path weights

For each inverse word of length \(j\) from the ordinary source \(x\) to \(y\), let \(A=3^j2^{-S_j(x)}\) and \(z=Ax/y=\prod_{i<j}w_{U^ix}\). Give it the exact mass \(A\rho_1(x)\). Write \(L_{j,y}(t)\) for the resulting mass of words with \(z\le t\). At depth zero put all the mass at \(z=1\). Equivalently \(\mu_{j,y}\), the measure on the coordinate \(s=-\log z\) with masses divided by \(y\), is the pushforward of \(\mu_{0,x}=\rho_1(x)\delta_0/x\) by the following transfer. The edge from \(x\) to \(Ux\) multiplies mass by \(w_x\) and translates the mark by \(\ell_x=-\log w_x\). The total mass at \(y\) is \(\rho_{j+1}(y)/y\). Each individual row is finite at every finite depth.

For \(0\le\theta\le1\), set
\[
 I_{j,\theta}(y)=\frac1y\int_0^1
       |L_{j+1,y}(t)-L_{j,y}(t)|\,\frac{dt}{t^{1+\theta}}.
\]
Every fixed-depth integral is finite since \(z\ge(3/4)^{j+1}\) on the two rows. There is a finite constant \(B\), independent of \(\theta\), such that
\[
 \sup_j\sum_y I_{j,\theta}(y)\le B,\qquad
 \sum_{j,y}(1-w_y^{1-\theta})I_{j,\theta}(y)\le B.                  \tag{2}
\]
In particular for \(0\le\theta<1\),
\[
 \sum_{j,y}\frac1{y(3y+1)}\int_0^1
      |L_{j+1,y}(t)-L_{j,y}(t)|\,\frac{dt}{t^{1+\theta}}
                      \le \frac{B}{1-\theta}.                       \tag{3}
\]

To prove this, remove the scalar increment by putting
\[
 \eta_{j,y}=\mu_{j+1,y}-\mu_{j,y}-d_{j+1}(y)\delta_0 .
\]
It has total mass zero. For each such finite signed measure define \(N_\theta(\eta)=\int_0^\infty e^{\theta u}|\eta([u,\infty))|\,du\). Then \(I_{j,\theta}(y)=N_\theta(\eta_{j,y})\). Translation by \(\ell\ge0\) multiplies this norm by exactly \(e^{\theta\ell}\), because the tail of the translated measure is zero below \(\ell\). Also \(N_\theta(\delta_\ell-\delta_0)=\int_0^\ell e^{\theta u}du\). In particular, uniformly in our parameter,
\[
 w_x N_\theta(\delta_{\ell_x}-\delta_0)\le
 w_x(e^{\ell_x}-1)=1-w_x .
\]
The signed row difference obeys the true marked transfer, whereas its total difference obeys \(T\). Subtracting gives
\[
 I_{j+1,\theta}(y)\le
  \sum_{Ux=y} w_x^{1-\theta} I_{j,\theta}(x)
     +\sum_{Ux=y}(1-w_x)|d_{j+1}(x)| .                               \tag{4}
\]
At depth zero the entire zero-mass remainder at \(y\) is
\(\sum_{Ux=y}w_x\rho_1(x)(\delta_{\ell_x}-\delta_0)/x\).
Hence \(\sum_y I_{0,\theta}(y)\le\sum_x(1-w_x)\rho_1(x)/x<\infty\), uniformly, by \(0\le\rho_1\le2\). For countably many parents the triangle inequality follows by integrating the absolute tail and using Tonelli on its positive majorant. Sum (4) over \(y\), then telescope using (1). One may take \(B=\sum_x(1-w_x)\rho_1(x)/x+\sum_{k\ge1}b_k\). Finally \(1-w^{1-\theta}\ge(1-\theta)(1-w)\) by concavity. This proves (2) and (3). All positive parts and absolute values can be taken after formation of the true signed fibre row.

## The critical exponent keeps a single cycle

For any fixed additional positive odd cycle \(C\) of length \(h\), put \(\lambda=\prod_{x\in C}w_x\), \(\gamma=\lambda^{1/h}\), and fix any \(y\in C\). The cropped *positive* Mellin increment satisfies, for all sufficiently large \(j\),
\[
 \frac1{y(3y+1)}\int_0^{1/(j+1)}
     (L_{j+1,y}(t)-L_{j,y}(t))_+\,\frac{dt}{t^{1+\theta}}
             \ge c_{y,\theta}\gamma^{(1-\theta)j}.                    \tag{5}
\]
At \(\theta=1\) this lower bound is independent of the clock. It comes from the entire witnessing interval. In each congruence class modulo \(h\), the prior endpoint theorem gives a depth \(j_0\) and a closed interval \([u,v]\), \(0<u<v<c_0/2\), strictly between the successive smallest defects at \(j_0+1\) and \(j_0\). On the interval the signed row difference is at least one fixed word mass \(a>0\). Here \(c_0\) bounds the defect below on all simple paths. Under \(b\) additional reverse laps, both rows at thresholds \(\lambda^bt\) equal \(\lambda^b\) times their original values. The scaled interval lies in the stipulated crop eventually. Its integrated contribution is \(a\lambda^{(1-\theta)b}\int_u^v t^{-1-\theta}dt\), before the site weight. Minimize over the finitely many depth classes. [Original endpoint identity and smallest-defect argument](../../astra-six-hour-20261127/escape/ENDPOINT_RATE_TEST.md) · [Weaver 176, simple-path packing](https://rstation.ai/problems/collatz/papers/176/v1)

On every nonperiodic site all prefixes consist of distinct departed states, so the cropped integral vanishes identically for all sufficiently large \(j\), uniformly in the site. Consequently the sum of the critical cropped positive increments over \(y>1\) tends to zero if and only if the ordinary positive cycle through 1 is the only cycle. Its eventual lower bound detects every extra cycle and its uniform upper bound follows from (2). Including 1 in this detector would retain the known trivial cycle. For \(\theta<1\), the finite all-time bound permits the geometric tail (5).

## The original supremum crop

The marked part of the earlier supremum test itself satisfies
\[
 \sum_{y>1}\frac{\sup_{0\le t\le1/(j+1)}
             (L_{j+1,y}(t)-L_{j,y}(t))_+}{y(3y+1)}
                                =o((j+1)^{-1}).                       \tag{6}
\]
For this assertion we use the prior ordinary-depth weak convergence of the marked prefix laws at each fixed site to a finite nonatomic measure, the uniform bound \(\rho_k(y)\le C h(y)\) for \(k\ge1\), and \(\sum_y h(y)/[y(3y+1)]<\infty\). These are specific original-law trace inputs. [Integer fibres and ordinary-depth selection](../../astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md) · [Positive trace budget](../../astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md)

Only periodic sites contribute for large \(j\). A simple lap has \(\lambda\ge c_0\), uniformly in cycles. For \(0<t<c_0\), choose the largest integer \(b\ge0\) with \(t<c_0\lambda^b\); then \(\lambda^b\le t/(c_0\lambda)\le t/c_0^2\). Every path ending at the periodic site whose defect is at most \(t\) must begin with those \(b\) complete reverse laps. If the clock is shorter than \(bh\), the row there is zero: an earlier departure has defect at least \(c_0\lambda^b\), and a path remaining on the cycle has defect at least \(\lambda^b\). Otherwise strip the laps. Each of the two row masses at the threshold is therefore \(O(t h(y))\), uniformly in sites and clocks. The positive difference has the same majorant.

For each fixed cycle site, divide the crop into \(0<t<\epsilon/(j+1)\) and \(\epsilon/(j+1)\le t\le1/(j+1)\). After multiplication by \(j+1\) the first part is \(O(\epsilon h(y))\). On the second, \(b=O_{y,\epsilon}(\log(j+1))\), so both residual clocks tend to infinity uniformly. Their distribution functions converge uniformly to the same CDF, by fixed-site weak convergence and its continuity. Their difference after stripping is \(o_{y,\epsilon}(1)\) uniformly over the remaining thresholds. Multiplication by \((j+1)\lambda^b=O(1)\), followed by \(\epsilon\downarrow0\), proves the fixed-site limit. The common majorant and the summable trace allow dominated convergence over all sites, proving (6).

For the original \(Q_j^*\), (1) and (6) imply that \((j+1)Q_j^*\to0\) in natural density. Indeed for any \(\delta>0\), the count in \([K,N]\) of \(j\) with \((j+1)b_{j+1}>\delta\) is at most \((N+1)\delta^{-1}\sum_{j\ge K} b_{j+1}\). Take \(N\to\infty\), then \(K\to\infty\). This gives unbounded clocks with \(Q_j^*=o(1/j)\). The required \(O(j^A(2/3)^j)\) source-specific rate remains open. In particular (1)–(3) give no exponential moment of the residence time of an individual ordinary source.
