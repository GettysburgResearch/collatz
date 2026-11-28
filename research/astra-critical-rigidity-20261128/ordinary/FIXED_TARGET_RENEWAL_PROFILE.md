# Reciprocal preimages of every large ordinary integer

Fix a bounded source interval \(I=(a,b)\), \(0\le a<b\). For each positive integer \(N\) take every positive reduced source \(m/3^n\in I\), \(n\ge1\), whose first integer is exactly \(N\). Its weight is \(2^{-T}\), where \(T\) is its true shortcut landing time. Write \(G_I(N)\) for the total weight. Eligible marks have \(N\not\equiv2\pmod3\). All logarithms here are natural unless a base is written.

At **every** eligible integer tending to infinity,
\[
                 N G_I(N)\longrightarrow |I|/d,\qquad
 d=\log3-\tfrac43\log2,\quad \sigma=\tfrac23\log2 .                 \tag{1}
\]
At ineligible marks the mass vanishes exactly. Normalize the eligible column to probability and put \(x=\log N,\ s_x=\sigma d^{-3/2}\sqrt x,\ \gamma=\log_23\). With \(S_n=n\log3-T\log2\), the joint limit is
\[
 \left(\frac m{3^n},       \frac{n-x/d}{s_x},       \frac{T-4x/(3d)}{\gamma s_x},       x-S_n\right)
 \Longrightarrow
            (U,H,H,\log(U+Z)).                                         \tag{2}
\]
Here \(U\) is uniform on \(I\), \(H\) is standard normal and \(Z\) has the distribution of
\[
 \frac12\sum_{j\ge1}e^{-S_j^*},\qquad
 S_j^*=\sum_{i=1}^j\log(3/2^{e_i}),\quad
 \Pr_*(e_i=k)=3\cdot4^{-k},\quad k\ge1
\]
for independent \(e_i\). The three variables \(U,H,Z\) are independent. These conclusions concern all physical, reduced first preimages of a prescribed ordinary integer, including its actual landing date.

## A marked renewal calculation

Use the reversed gap order of the [exact inverse identity](RECIPROCAL_FIXED_TARGETS.md). Under the original geometric law \(\Pr(e=k)=2^{-k}\), put \(S_0=0\), \(S_n=\sum_{i=1}^n\log(3/2^{e_i})\), \(Y_n=\frac12\sum_{j=0}^{n-1}e^{S_j}\) and \(Z_n=Y_ne^{-S_n}\). The only source for the word is \(y=e^{x-S_n}-Z_n\). At each eligible mark this is a genuine reduced first preimage whenever \(y>0\). Its original probability is its physical weight. The likelihood ratio of the tilted law to the original through grade \(n\) is exactly \(e^{S_n}\). Thus the scaled column evaluates tests against the measure
\[
 \sum_{n\ge1}\mathbb E_*[
              e^{x-S_n}\,{\bf1}_{\{e^{x-S_n}-Z_n\in I\}}              \delta_{(x-S_n,Z_n,(n-x/d)/s_x)}].                        \tag{3}
\]

First disregard \(Z_n\) and the weights in (3). For continuous compactly supported \(f\),
\[
 \sum_{n\ge1}\mathbb E_* f(x-S_n,(n-x/d)/s_x)
 \longrightarrow
 \frac1d\int f(u,v)\,du\,\varphi(v)\,dv,                            \tag{4}
\]
where \(\varphi\) is the standard normal density. Indeed \(D_n=(n\log3-S_n)/\log2\) is a sum of \(n\) tilted independent geometrics of mean \(4/3\) and variance \(4/9\). On \(|n-x/d|\le B\sqrt x,\ |x-S_n|\le B\), its point mass from the negative binomial formula \(\binom{D_n-1}{n-1}(3/4)^n(1/4)^{D_n-n}\) is uniformly
\[
 (1+o_B(1))\frac{\log2}{\sigma\sqrt n}
              \varphi((x-nd)/(\sigma\sqrt n)).
\]
This is Stirling's formula within bounded standard deviations. Break the \(n\) window into adjacent intervals of \(\lfloor x^{1/4}\rfloor\) terms plus boundary remainders. Both the standard coordinate and the normalized Gaussian factor vary by \(o(1)\) inside a block. The attainable \(u=x-S_n\) at fixed \(n\) lie on one translate of \((\log2)\mathbb Z\). The phases shift by \(-\log3\) at each grade; their block averages converge to uniform modulo \(\log2\), uniformly in the initial phase. Indeed each nonconstant Fourier monomial has bounded partial sums by the geometric-series formula. Apply uniform trigonometric approximation to the continuous periodization of \(f(\cdot,v)\), using uniform continuity on its compact set of \(v\)'s. The phase mean is \((\log2)^{-1}\int f(u,v)du\). The remaining normal Riemann sum has factor \(s_x/(\sigma\sqrt{x/d})=1/d\), proving (4).

For each fixed interval length \(B\) there is a uniform renewal bound
\[
 \sup_{|J|=B}\sum_{m\ge0}\Pr_*(S_m\in J)\le C_B .
\]
At first entrance into \(J\), any subsequent return requires a fresh sum in \([-B,B]\); the expected total such visits is finite, since for \(0<p<1\), \(r_p=\mathbb E_*e^{-pS_1}<1\) by strict concavity and \(\mathbb E_*e^{-S_1}=1\). In particular \(\Pr_*(S_i\le B)\le e^{pB}r_p^i\). Subadditivity of the \(p\)-th power gives also
\[
 \sup_{|J|=B}\sum_{m\ge0}\mathbb E_*[Z_m^p;\ S_m\in J]
 \le 2^{-p}C_B\sum_{i\ge1}r_p^i.                                      \tag{5}
\]
Expand the \(m\)-th summand by the individual final \(i\)-increment exponentials in \(Z_m\). After fixing these increments, the preceding walk must land in a translate of \(J\). This gives (5) after summation.

Replace \(Z_n\) by its contribution \(Z_k^{\rm last}\) from the last \(k\) increments for \(n\ge k\). The omitted term is \(e^{-(S_n-S_{n-k})}Z_{n-k}\). For any compactly supported Lipschitz test on \((u,z,v)\), the summed error in (4) is \(O(r_p^k)\) by (5), conditioning on the final \(k\) increments; a bounded Lipschitz test is \(p\)-Hölder. For fixed \(k\), the early grades make no contribution as \(x\to\infty\), since \(S_n\le n\log(3/2)\). Condition on the final increments and apply (4) at \(x-(S_n-S_{n-k})\) to the preceding walk. The fixed shift in the time and grade centers is negligible on the \(s_x\) scale; the uniform interval renewal bound permits bounded convergence over the suffix. Finally \(Z_k^{\rm last}\), by reversing iid increments, has the distribution of the first \(k\) terms of the displayed positive series for \(Z\). That series converges almost surely by positive drift. We have proved vague convergence of the unweighted marked sum to
\[
                    d^{-1}du\,\mathcal L(Z)(dz)\,\varphi(v)dv .          \tag{6}
\]

## Recovering the entire column

With \(y=e^u-z>0\), the measure \(e^u du\) becomes ordinary \(dy\) for fixed \(z\). The boundary \(y=a,b\) has zero measure in (6). Compact restrictions in (3), followed by exhaustion, give \(\liminf NG_I(N)\ge |I|/d\). A blocking identity supplies the matching upper bound even if \(u,z,v\) are all unbounded.

Let \(W\) be an independent copy of the original, untilted \(Y_k\) for a fixed \(k\). Then \(0<W\le(3/2)^k-1\), \(\mathbb E W=k/2\), and \(Y_n+e^{S_n}W\) has the distribution of \(Y_{n+k}\). All finite \(Y_i\), \(i\ge1\), are nonintegral. For \(N>(3/2)^k\) the inverse formula and telescoping give
\[
 \mathbb E_W G_{(0,W)}(N)
   =\sum_{n\ge0}[\Pr(Y_{n+k}>N)-\Pr(Y_n>N)]
   =k\Pr(Y>N),
 \qquad Y=\lim_jY_j .                                                    \tag{7}
\]
Here the \(n=0\) term is zero. The known index-one perpetuity estimate gives \(N\Pr(Y>N)\to1/(2d)\). Its normalization and original sources are checked in the [half-window calculation](RECIPROCAL_FIXED_TARGETS.md). Choose \(k\) with \(\Pr(W>b)>0\), possible by a run of gaps one. If a subsequence of eligible marks has \(NG_I(N)\ge|I|/d+\epsilon\), partition each \((0,W)\) with \(W>b\) into \(I\) and its two open complements, omitting any empty piece. Their separate lower bounds give a lower limit at least \(W/d+\epsilon\). For other \(W\) it is at least \(W/d\). Fatou's lemma contradicts (7), since \(\mathbb E W/d=k/(2d)\). This proves (1).

The compact mass of (6) after weighting and restriction already exhausts the limit in (1). Thus the normalized full measures converge weakly, with \(y,v,z\) independent and distributed as \(U,H,Z\); \(x-S_n=\log(y+z)\). The exact identity
\[
       T-4x/(3d)=\gamma(n-x/d)+(x-S_n)/\log2
\]
now proves (2).

## Physical initial histories and ordinary harmonic weights

Every prescribed finite shortcut word \(w\) of duration \(l\) and grade \(g\) takes its real source affinely to \(F_w(y)=(3^g y+C_w)/2^l\). At a reduced source of positive ternary height \(h\) for the suffix, inversion through the designated bits gives numerator \(2^lm'-3^hC_w\) over \(3^{h+g}\), a ternary unit. Every inverted parity is the designated one. If this source belongs to \(I\), positivity holds throughout. Histories which finish inside the prefix have \(n\le g\) and bounded landing mark as \(I,w\) are fixed. Thus for all sufficiently large marks the restricted mass is exactly \(2^{-l}G_{F_w(I)}(N)\). By (1), its fraction of the whole column tends to \(3^g/4^l\). This applies to the initial word of each particular ordinary integer. The same substitution in (2) gives independent tilted initial bits, uniform real source and Gaussian grade fluctuation, jointly for any fixed number of bits. The carry variable can depend on these initial bits.

More globally, let \(Q_H(N)=\sum_{n=1}^H G_{n,I}(N)\). Then
\[
 \sum_{N\ge1}\left| Q_H(N)-
 \frac{|I|}{dN}{\bf1}_{\{N\le e^{dH},\ N\not\equiv2\ (3)\}} \right|=o_I(H).   \tag{8}
\]
Indeed \(G_I(N)\) is finite for every mark, by domination by \((0,W_0)\) for an atom \(W_0>b\) in the blocked law and the finite right side of (7) (the general telescoping only subtracts nonnegative early terms). At eligible marks (1) makes the sum of \(|G_I(N)-|I|/(dN)|\) through \(e^{dH}\) be \(o(H)\). Fix \(0<\epsilon<d\). Below \(e^{(d-\epsilon)H}\) the total contribution of grades above \(H\) is \(O_{I,\epsilon}(e^{-cH})\) by the grade-wise [exponential concentration of the log landing mark](RECIPROCAL_LANDING_WORDS.md). Between the two cutoffs this contribution is at most the entire harmonic mass of the strip, \(O_I(\epsilon H)+o_I(H)\). Above \(e^{dH}\) one may compare the equal leading total masses: the row asymptotic gives \(\sum_N Q_H(N)=2|I|H/3+O_I(1)\), while the restricted harmonic proxy also has total \(2|I|H/3+O_I(1)\). Let \(\epsilon\downarrow0\). This proves (8), including uniformity over all subsets of ordinary marks and all bounded tests.

Consequently logarithmic-density information about a subsequent ordinary basin can be transferred in either direction on the admissible mark classes. Each positive integer has an admissible multiple, either itself or its double, with exactly the same tail orbit. Equation (8) transfers an averaged arithmetic measure; equation (1) treats each large ordinary landing mark separately. Neither determines the subsequent orbit of a prescribed mark.
