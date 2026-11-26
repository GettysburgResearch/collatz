# Exact onset of the finite ternary trace on an ordinary escape

Let \(a_n=U^n(a_0)\) be any injective sequence of positive odd ternary units under the actual odd Collatz map. Let \(p_k\) denote the ternary residue law for \(k\) independent positive geometric gaps of mass \(2^{-e}\), \(\rho_k(y)=3^k p_k(y\bmod3^k)\), and \(\rho_0=1\). Write \(A_K(y)=K^{-1}\sum_{k=1}^K\rho_k(y)\), and let \(h(y)=\lim_{K\to\infty}A_K(y)\) be the established fixed-integer Cesàro trace. Then, for every fixed \(\lambda>0\),
\[
       \lim_{n\to\infty}\frac{A_{\lfloor\lambda n\rfloor}(a_n)}{h(a_n)}
        =\begin{cases}0,&0<\lambda\le1,\\ 1-1/\lambda,&\lambda>1.\end{cases}       \tag{1}
\]
The time \(n\) is the number of actual odd steps from the specified fixed ordinary source. In particular the onset is resolved on the whole linear time scale, including the value zero at \(K=n\). This conditional theorem describes an arbitrary ordinary escape, if one exists. The named density and trace inputs are stated below. This extends [PR 200's quantitative earlier-onset obstruction](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md).

## The uniform moving-target statement

In the odd component of \(a_0\) give every odd \(x\) its signed grade \(g(x)=i-t\), where \(U^t x=a_i\). Injectivity on the reference ray implies consistency and \(g(Ux)=g(x)+1\). Its positive corrected height \(P(x)=x\prod_{j\ge0}(1+1/(3U^j x))\) is finite by the uniform simple-path reciprocal bound. We have
\[
 P(Ux)=3\,2^{-e(x)}P(x),\qquad P(x)\ge x,\qquad P(a_n)/a_n\to1 .
\]
Define the reciprocal mass of an entire grade, including odd multiples of three, by \(Z_v=\sum_{g(x)=v}1/P(x)\) for \(v\in\mathbb Z\). The [own-word posterior theorem](../global/POSTERIOR.md) proves the uniform estimate \(Z_v=O(1)\) and the exact identity
\[
        \frac{\rho_k(a_n)}{P(a_n)}
           =\sum_{\substack{g(x)=n-k\\U^k x=a_n}}\frac1{P(x)} .                   \tag{2}
\]
Indeed the actual inverse-word probability is \(2^{-S_k(x)}\), and the corrected multiplier telescopes. All sums in (2) use ordinary positive sources.

Let \(d_y\) be the relative odd natural predecessor density, \(d_n=d_{a_n}\) and \(d_\infty=\lim_n d_n\). The limit exists by nesting. The named predecessor lower bound is \(d_y\ge c/y\) at every odd ternary unit. We claim the following profile uniform in **every** integer depth \(k\ge0\):
\[
 \sup_{k\ge0}\left|\,\frac{\rho_k(a_n)}{P(a_n)}-Z_{n-k}\right|
       \le\frac4c(d_\infty-d_n)+\frac3{P(a_{n+1})}\longrightarrow0 .               \tag{3}
\]

To prove (3), consider a unit of grade \(n-k\) omitted from (2). Its first ray entrance is at some index \(i>n\). In fact, if the first entry were \(a_i\) at \(t\) and \(i\le n\), then \(t=i-n+k\) and exactly \(k\) steps take \(x\) to \(a_n\). Distinct units of one grade form an antichain, hence their predecessor sets are disjoint. For any finite group of these missing units take the largest of their first-entry indices \(i_*\). Their basins lie in the basin of \(a_{i_*}\) and are disjoint from the basin of \(a_n\): a path hitting both would place the missing unit before \(a_n\), or on the ray at/after \(a_n\), and the grade and missing condition exclude all such possibilities. Finite additivity therefore gives \(\sum d_x\le d_{i_*}-d_n\le d_\infty-d_n\). Supremizing over finite subsets bounds the sum of \(1/P(x)\le d_x/c\) over the omitted units. This is the same ordinary antichain and first-entry mechanism underlying the [whole-ray branch theorem](../../astra-multiple-attacks-20261125/synthesis/README.md); its stronger fractional moment estimate is unnecessary here.

Every omitted odd multiple of three maps to a unit \(y=U(x)\). At a given \(y\), their total reciprocal cost is at most \(3/P(y)\) by the exact multiplier and \(\sum_{e\ge1}2^{-e}=1\). For \(k\ge1\), this \(y\) is missing at \((n,k-1)\), so the same unit bound applies. For \(k=0\) it has grade \(n+1\), and can also equal \(a_{n+1}\); the other units first enter later. This proves (3) with its stated uniform bound.

By taking \(k=0\) in (3), \(Z_v\to0\) as \(v\to+\infty\). In the other direction (2) at \(a_0\) gives \(Z_{-j}\ge\rho_j(a_0)/P(a_0)\ge\alpha/P(a_0)\) for \(j\ge1\) by the uniform ternary atom floor. Thus the uniform moving profile goes from vanishing reciprocal grade mass on the future side to positive mass on the past side. For any integers \(v(n)\to\infty\) with \(v(n)\le n\), the normalized density at the shortened depth \(n-v(n)\) tends to zero. At depth \(n\) it tends to \(Z_0>0\).

## Taking the two limits in order

Write \(\varepsilon_n\) for the upper bound in (3). For each fixed \(n\), the depth averages of \(\rho_k(a_n)/P(a_n)\) converge to \(h(a_n)/P(a_n)\). By (3), that number lies within \(\varepsilon_n\) of both the limsup and liminf of \(K^{-1}\sum_{k=1}^K Z_{n-k}\). Since \(Z\) is bounded, shifting by fixed \(n\) changes neither of those limits. Their difference is at most \(2\varepsilon_n\) for every \(n\). Hence
\[
           H=\lim_{J\to\infty}\frac1J\sum_{v=1}^J Z_{-v}
            =\lim_{n\to\infty}h(a_n)/P(a_n)>0 .                                 \tag{4}
\]
The positive atom floor gives the strict inequality. Formula (3) can now be averaged up to any growing depth. For \(K=\lfloor\lambda n\rfloor\le n\), the average of \(Z_{n-k}\) tends to zero because \(Z_v\to0\) at positive infinity. If \(K>n\) with fixed \(\lambda>1\), the positive-index part still averages to zero, and the negative-index part has length \(K-n\) and Cesàro mean tending to \(H\). Divide by (4) to obtain (1).

More generally \(K/n\to0\), \(K/n\to1\), and \(K/n\to\infty\) yield normalized ratios \(0,0,1\), respectively, with \(K\ge1\). At \(K/n\to1\) any negative-index overshoot is \(o(K)\) and \(Z\) is bounded. At \(K/n\to\infty\) the nonnegative indices occupy \(o(K)\). A fixed fraction \(0<\eta<1\) of the trace first appears on the scale \(n/(1-\eta)\): the uniform approximation (3) and these sequential limits rule out earlier isolated crossings, even though \(A_K\) itself need not be monotone.

Valbuena's stronger fixed-target result also gives \(\liminf_{k\to\infty}\rho_k(a)=h(a)\) and convergence in Cesàro mean absolute error. By (3), the number \(\liminf_{v\to-\infty} Z_v\) differs from \(h(a_n)/P(a_n)\) by at most \(\varepsilon_n\). Consequently \(\liminf_{v\to-\infty} Z_v=H\). Combined with (4), this gives \(J^{-1}\sum_{j=1}^J |Z_{-j}-H|\to0\). In particular at macroscopic depth \(K\sim\lambda n\), the normalized individual values \(\rho_k(a_n)/h(a_n)\), for \(k\) uniform on \(1,\ldots,K\), converge in law to a Bernoulli variable of mean \((1-1/\lambda)_+\). Uniform boundedness of \(Z\) gives convergence of all fixed positive moments and bounded continuous tests. [Valbuena, integer trace corollary and its proof](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/positive-stationary-envelope.tex)

## Detecting an escape from first-hit trace peaks

Let \(L_k(y)\) count the inverse weight of sources whose **first** odd hit of \(y\) is at step \(k\), counting the zero-length word. Uniformly in \(k\) and odd targets \(y\) outside the forward orbits of **all ordinary positive starts through \(M\)**,
\[
                         L_k(y)/y \ll M^{-\delta}                   \tag{5}
\]
for some absolute \(\delta>0\). We use the uniform first-hit layer bound \(L_k(y)\le Cy d_y\) from input I of [PR 200](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md) at unit targets. For \(3\mid y\) positive depth is impossible and the zero-depth term is \(1/y\le1/M\).

Every full shortcut orbit \(O\), including an eventual cycle and its transient part, satisfies \(|O\cap[1,M]|\ll (1+\log M)^2M^{\theta-\gamma}\) for the interval-compression exponent of Paper 28/v3. At clock \(H=\lceil\log_2 M\rceil^2\) the full map on the set of distinct orbit states has multiplicity at most \(H+1\): every element merges after at most \(H\) further steps with the unique suffix representative or has its uniquely determined earlier nonperiodic representative. More explicitly, at a nonperiodic endpoint there is at most one source on this orbit at that clock. At a periodic endpoint there is one periodic source, and at most \(H\) transient sources lying within the last \(H\) transient steps. Apply the compression bound to the whole interval and multiply by \(H+1\).

Suppose a start in a high sampling window ever visits \(y\). No state before or at that visit can be \(\le M\), by the exclusion in (5). Its first odd landing at or below \(M\) must fail or belong to the forward orbit of \(y\) in \([1,M]\). Apply Paper 102/v1 to this deterministic landing set and failure. Sending the window height to infinity bounds the ordinary predecessor density by \(\exp(C\sqrt{\log M})[O((1+\log M)^2 M^{-(1-\theta+\gamma)})+O(M^{-g})]\), with \(g>0\). This proves (5). The original inputs and their normalization appear in [the whole-ray theorem](../../astra-multiple-attacks-20261125/synthesis/README.md).

It follows that the existence of an ordinary escape is equivalent to
\[
          \limsup_{\substack{y\to\infty\\y\ {\rm odd}}}\ \sup_{k\ge0} L_k(y)/y>0 .
\]
An escaping fixed source \(a_0\) provides the lower bound through its one actual word at \((a_n,n)\), which is a first hit and contributes \(P(a_n)/(a_n P(a_0))\ge1/P(a_0)\). Conversely, any positive limsup and (5) force arbitrarily large \(y\)'s onto the union of the forward trajectories of one fixed finite set of ordinary starts. One of those trajectories is infinite. This converse allows arbitrarily many positive cycles of arbitrary lengths. Removing repeat visits in \(L_k\) prevents the periodic amplification factor in the unrestricted trace. Estimate (5) controls targets outside the specified finite union and supplies no bound on an unknown infinite orbit contained in it.

The critical-law sampling of [ORDINARY_RENEWAL.md](ORDINARY_RENEWAL.md) controls a growing prefix of broadly sampled ordinary ancestors. It does not yield a trace bound for this specific moving target at depths comparable with its actual odd travel time. A uniform continuity estimate in depth that forbids (3), or any independent macroscopic onset law incompatible with (1), would exclude all such escapes. Such an estimate has not been established here.

## Primary inputs and scope

- The positive odd predecessor density, its reciprocal floor, the normalized fixed-integer Cesàro trace, and the whole-Haar ternary atom floor are the source-qualified inputs recorded in the [own-word posterior proof](../global/POSTERIOR.md) and [PR 200, inputs I and II](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md). The second-moment estimate from input II is unnecessary for (1). [Weaver, Paper 12](https://rstation.ai/problems/collatz/papers/12), [Wren, Paper 10/v3](https://rstation.ai/problems/collatz/papers/10/v3)
- The count of actual odd sources in (2), the individual posterior dichotomy and its finite Lean verification are in [the global branch](../global/POSTERIOR.md). The uniform estimate (3) and the macroscopic Cesàro profile are written deductions.

## The individual depth transition with the stronger fixed-target theorem

Weaver's Paper 176, Theorem 2, equations (4)–(5), proves the stronger ordinary limit \(\rho_k(z)\to h(z)\) for **every fixed positive odd** \(z\) in the same whole-Haar normalization. Apply (3) first with \(n\) fixed and \(k\to\infty\). Both the limsup and the liminf of \(Z_v\) as \(v\to-\infty\) differ from \(h(a_n)/P(a_n)\) by at most \(\varepsilon_n\). Letting \(n\to\infty\) gives the pointwise limit \(Z_v\to H\) as \(v\to-\infty\). Hence for every sequence of ordinary depths with \(n\to\infty\) and \(k-n\to+\infty\),
\[
                         \rho_k(a_n)/h(a_n)\longrightarrow1 .
\]
On the other side \(n-k\to+\infty\) gives limit zero. For each fixed integer offset \(v=n-k\), the limit is \(Z_v/H\). Thus the two separate pointwise limits of the translated profile determine the behavior at all diverging offsets. The earlier Cesàro proof uses weaker fixed-target hypotheses. [Weaver, *Ternary harmonic moments and Collatz orbit occupation*, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1)
