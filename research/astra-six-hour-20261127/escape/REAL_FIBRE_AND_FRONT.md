# Real fibres at integer roots and their limit on a putative escaping ray

**Source-qualified written results.** The canonical conditional real law of the stationary joint Syracuse series at **each positive odd ternary unit** is singular continuous and exact-dimensional of real dimension one, using the counted-synchronization input for singularity. This includes the nonperiodic roots, where the support has a uniform relative gap below the root, and the periodic roots, where the upper endpoint has local dimension one. Along any actual positive escaping component, a single corrected rescaling makes the moving real fibres converge in total variation to a component probability of dimension one. Their realized inverse-word information has a transition at the real odd travel time from a fixed ordinary starting point.

We use the [fixed-root word and information theorem](CANONICAL_INVERSE_PATHS.md). Weaver's Paper 19, §9.2, identifies the fixed-root canonical real fibre \(\mu_a\) with the law of the inverse affine series below under \(P_{h,a}\). The limit defining that conditional **stationary** fibre in the cited theorem is taken in Cesàro depth. Whole-space dimension and almost-everywhere statements do not identify a fibre at a prescribed integer of zero ternary Haar mass. [Weaver, Paper 19, §9.2, (F3), (F9)–(F13)](https://rstation.ai/problems/collatz/papers/19)

## Full real dimension on each specified fibre

At a fixed ordinary root \(a\) use its inverse states \(X_j\), exponents \(E_j\), and totals \(S_j=\sum_{i\le j}E_i\). Put
\[
 A_j=3^j 2^{-S_j},\qquad R_n=\tfrac13\sum_{j=1}^n A_j,\qquad
 R=\lim_n R_n,\qquad R_n=a-A_nX_n .
\]
The last equality is exact inverse reconstruction. On a set of paths of probability one,
\[
 S_n=2n+O(\sqrt{n\log\log n}),\quad
 R-R_n\le \exp[-Dn+O(\sqrt{n\log\log n})],\quad
 P_{h,a}[E_1,\ldots,E_n]\le\exp[-Dn+O(\sqrt{n\log\log n})].
                                                               \tag{1}
\]
The middle bound follows by summing \(A_j/3\) for \(j>n\). For large \(n\), \(\sqrt{j\log\log j}\) increases beyond its value at \(n\) at a rate \(o(1)\) per additional index, so the resulting tail is bounded by a geometric series.

Fix a small \(\eta>0\). Restrict to paths for which the bounds
\[
 e^{-(D+\eta)n}\le A_n\le e^{-(D-\eta)n},\qquad
 0\le R-R_n\le e^{-(D-\eta)n},\qquad
 P_{h,a}[E_1,\ldots,E_n]\le e^{-(D-\eta)n}
\]
hold for every \(n\ge N\). These sets increase to full measure as \(N\to\infty\). If the projected endpoint lies in an interval of length \(e^{-Dn}\), its prefix \(R_n\) is in an interval of length at most \(2e^{-(D-\eta)n}\). At fixed \(S_n\), the possible prefixes have separation at least \(A_n\), because the distinct ordinary \(X_n\)'s are integers and each determines its whole word from that root. At most \(O(e^{2\eta n})\) such words occur per total and there are \(O_{D,\eta}(n)\) admissible totals. The restricted pushforward consequently has interval mass at most
\[
 O(n)\exp[-(D-3\eta)n].
\]
Interpolation between adjacent \(n\)'s gives a Frostman bound of every exponent less than \(1-3\eta/D\) for this restricted measure. Any Borel set of Hausdorff dimension below one thus has zero \(\mu_a\)-mass, by choosing \(\eta\) small and exhausting in \(N\). Equivalently the lower local dimension is at least one almost everywhere. Every finite measure on a bounded real interval has upper local dimension at most one almost everywhere; this follows by counting dyadic cells of mass less than \(2^{-n(1+\delta)}\) and applying Borel–Cantelli for each \(\delta>0\). Hence the local dimension of \(\mu_a\) is one almost everywhere. Weaver's Paper 175 already gives this fixed-total spacing argument for positive-density first-minimum cells. Its Theorem 3 supplies a common Borel carrier for the real values of **all** legal paths at a fixed root with single-gap frequencies \(2^{-g}\) and mean two. Under counted synchronization, this carrier has zero Hausdorff measure for every gauge \(r(\log(1/r))^s\), \(0\le s<1/2\). The fixed-root word theorem shows it carries \(\mu_a\). Thus \(\mu_a\) is singular continuous with full dimension, also at ordinary roots that are not specified as first-minimum cells. Qualitative synchronization suffices for Lebesgue singularity. [Weaver, Paper 175, Theorems 1 and 3 and §§7–9](https://rstation.ai/problems/collatz/papers/175)

## A common coupling over all odd travel times

Suppose \(a_0,a_1,\ldots\) is one actual positive escaping odd unit ray, \(a_n=U^n a_0\). Assign integer grade \(v=i-t\) to \(x\) whenever \(U^t x=a_i\). Define
\[
 w(x)=3x/(3x+1),\qquad F(x)=\prod_{j\ge0} w(U^jx),\qquad
 P(x)=x/F(x),\qquad M_x=h(x)/P(x)
\]
on its unit vertices. The source-qualified component identities give \(\sum_{Ux=y}M_x=M_y\), total \(H_C>0\) on every grade, \(M_{a_n}\to H_C\), and \(F(a_n)\to1\). Nonunit immediate parents have zero stationary trace and can be omitted. The one-edge canonical inverse kernel is \(M_x/M_y\); its telescoping equals the original \(3\,2^{-E}h(x)/h(y)\) because \(P(Ux)=3\,2^{-E}P(x)\). [Grade and flux proof](../../astra-unconventional-20261126/boundary/COLLISION_SOURCE.md) · [Source and moving-target profile](../../astra-unconventional-20261126/boundary/TRACE_PROFILE.md)

Sample a grade-zero integer \(Z_0\) with masses \(M_x/H_C\), sample its inverse path with \(P_{h,Z_0}\), label that past \(Z_{-1},Z_{-2},\ldots\), and attach its deterministic future \(Z_v=U^v Z_0\). Every grade marginal has masses \(M_x/H_C\). Set \(\mathcal E_n=\{Z_n=a_n\}\). These events increase, with probabilities \(M_{a_n}/H_C\to1\). Conditional on \(\mathcal E_n\), the past of \(Z_n\) is precisely \(P_{h,a_n}\) by the finite-cylinder telescope. Along almost every common sample, all sufficiently late future states are the original ray. The backward half satisfies (1) of the fixed-root theorem by conditioning on the countably many choices of \(Z_0\).

Write
\[
 J=\prod_{v\in\mathbb Z}w(Z_v).
\]
The entire product is positive. Every finite segment consists of distinct states on one positive ordinary path, so the imported uniform packing bound applies to every such segment; alternatively use (1) for the negative tail and forward packing for the positive tail. On \(\mathcal E_n\), the real fibre \(R^{(n)}\) sampled from \(a_n\) satisfies
\[
 F(a_n)(1-R^{(n)}/a_n)=J .
                                                               \tag{2}
\]
Indeed the complementary factor \(1-R^{(n)}/a_n\) is the limit of the products \(w(Z_v)\) over \(v<n\), by the ordinary affine product formula. Thus the law of the corrected rescaled real fibre is exactly \(\mathcal L(J\mid\mathcal E_n)\) and its total-variation distance from \(\mathcal L(J)\) is at most \(1-M_{a_n}/H_C\). This argument retains the correction in the dilation; weak convergence of the uncorrected relative fibre follows as \(F(a_n)\to1\).

Given \(Z_0=x\), the law of \(J\) is the affine image of \(\mu_x\) under \(r\mapsto F(x)(1-r/x)\). The mixture is countable. Every set of dimension below one is null for each summand, so the same holds for the mixture; its upper local dimension is again at most one almost everywhere. The resulting component distribution is singular continuous and exact-dimensional of dimension one. The countable union of the affine images of the preceding carriers is null for every stated logarithmic gauge, since each affine map has a fixed finite scale factor. It lives in a positive subinterval of \((0,1]\) by uniform reciprocal packing. A different reference ray in this component induces the same law, since it eventually shares the same ray and the corrected moving fibres determine the limit.

## Information before and after the fixed source

For a sample in \(\mathcal E_n\), the probability \(\pi_{n,k}\) under \(P_{h,a_n}\) of its own first \(k\) reversed letters is \(M_{Z_{n-k}}/M_{a_n}\). For negative grades write \(t=k-n>0\). The fixed-root conclusions give
\[
 -\log M_{Z_{-t}}=Dt+O_\omega(1+\sqrt{t\log\log(t+3)}),
\]
using the bounded correction \(F\) and the polynomial bound on \(h(Z_{-t})\). On all nonnegative grades the values \(M_{Z_v}\) are bounded below by a path-dependent positive constant, since the future eventually equals the original ray. Thus almost surely in this coupling, simultaneously for all sufficiently large \(n\) and all \(k\ge0\),
\[
 -\log\pi_{n,k}=
 D(k-n)_++O_\omega\!\left(1+\sqrt{(k-n)_+\log\log((k-n)_++3)}\right). \tag{3}
\]
When \(n-k\to+\infty\), the cylinder probability itself tends to **one**. If \(k/n\to\lambda>0\), the information divided by \(n\) tends to \(D(\lambda-1)_+\), also in probability for the actual laws \(P_{h,a_n}\). The conditioning event has probability tending to one, which justifies transfer of this convergence.

The positive branch charge forces a macroscopic initial stretch of almost deterministic reverse choices. Every fixed root nonetheless has the ordinary source information rate \(D\) and geometric word frequencies at large reverse times. A bound for the ternary almost-everywhere root, or a bound averaged over atoms of the ordinary entry law, cannot reverse these quantifiers. Excluding this delay uniformly from the specific integer trace remains a forward-escape obligation.

## Ordinary quotient depths and the entire measure profile

Write \(\nu=\mathcal L(R,Y)\) for the joint stationary real and ternary law and
\(\eta_k^a(B)=3^k\Pr(R\in B,Y\equiv a\bmod 3^k)\). In fact
\[
                 \eta_k^a\Longrightarrow h(a)\mu_a
                    \qquad(k\longrightarrow\infty)                  \tag{4}
\]
at each fixed positive odd unit, at **individual depths**. To see this put
\(g(x)=\rho_1(x)/h(x)\), bounded by \(2/\alpha_0\). The scalar ordinary-depth theorem gives \(\mathbb E_x g(X_t)=\rho_{t+1}(x)/h(x)\to1\) at every unit. Leave the last ternary digit of the stationary series in an independent suffix \((R',Y')\), as in (F4) of Paper 19. For a bounded Lipschitz test, replacing \(R_{k-1}+A_{k-1}R'\) by \(R_{k-1}\) costs \(o_a(1)\) after normalization by \(h(a)\). Indeed the suffix weight is at most \(3/\alpha_0\), \(R'\) is almost surely finite, and \(A_j\le a/X_j\to0\) almost surely by the fixed-root path theorem. Dominated convergence gives the claim. The normalized integral is therefore
\[
            \mathbb E_a[g(X_{k-1})f(R_{k-1})]+o_a(1).
\]
For each fixed \(t\), the Markov property and the scalar convergence imply
\(\mathbb E_a[g(X_{k-1})f(R_t)]\to\mathbb E_a f(R_t)\). The difference between using \(R_t\) and \(R_{k-1}\) is bounded by a constant times the expected modulus of continuity over \([R_t,R]\subset[0,a]\), for \(k-1\ge t\). This vanishes as \(t\to\infty\) and proves (4). [Weaver, Paper 176, Theorem 2](https://rstation.ai/problems/collatz/papers/176) · [Weaver, Paper 19, equations (F4)–(F8)](https://rstation.ai/problems/collatz/papers/19)

On a hypothetical escaping component write \(T_x(r)=F(x)(1-r/x)\).
Define the finite kernel and grade measures
\[
 K(x,B)=\frac3{h(x)}\Pr(Y'\equiv x\bmod3,\ T_x(R')\in B),\qquad
 \Xi_v(B)=\mathbb E[K(Z_{v+1},B)].
\]
Every row has total mass \(g(x)\le 2/\alpha_0\). There is an exact identity for every \(k\ge1\):
\[
 \frac{(T_{a_n})_*\eta_k^{a_n}}{h(a_n)}
     =\mathbb E[K(Z_{n-k+1},\cdot)\mid\mathcal E_n].                \tag{5}
\]
For an inverse prefix of length \(j=k-1\) terminating at \(x\), the independent suffix contributes \(Y'\equiv x\bmod3\) and real value \(R_j+A_jR'\). Since \(a_n-R_j=A_jx\) and \(P(a_n)=A_jP(x)\), its corrected mark is exactly \(T_x(R')\). The prefix coefficient \(3^k2^{-S_j}/h(a_n)\) equals its canonical inverse probability times \(3/h(x)\). Summing proves (5), including the last generation and all its residual dependence. The common coupling now gives
\[
 \sup_{k\ge1}\left\|
        (T_{a_n})_*\eta_k^{a_n}/h(a_n)-\Xi_{n-k}
       \right\|_{\mathrm{TV}}
       \le (2/\alpha_0)(1-M_{a_n}/H_C),                             \tag{6}
\]
where the norm of a difference of finite measures is the supremum of absolute discrepancies over measurable sets. Indeed each column test takes values between zero and \(2/\alpha_0\), and the conditioning discrepancy has this bound.

As \(v\to+\infty\) the masses \(\Xi_v(\mathbb R)\to0\). Along almost every sample \(Z_{v+1}=a_{v+1}\) eventually and \(h(a_{v+1})=M_{a_{v+1}}P(a_{v+1})\to\infty\). At every fixed finite grade, \(\Xi_v(({-}\infty,0))>0\): the stationary joint law has full support on the positive real coordinate times the ternary units, so \(\Pr(R'>x,Y'\equiv x\bmod 3)>0\) for each unit in the grade.

At the other end,
\[
                \Xi_v\Longrightarrow\mathcal L(J)
                           \qquad(v\to-\infty).                      \tag{7}
\]
Along the common sample, \(Z_{v+1}\to\infty\) and \(F(Z_{v+1})\to J\) since these products exhaust the bilateral path. For bounded Lipschitz \(f\), the row \(K(Z_{v+1},f)\) differs from \(g(Z_{v+1})f(J)\) by an error tending to zero in expected absolute value. Couple the same independent stationary pair for all rows, use the bound \(3/\alpha_0\) and dominated convergence. To decouple the remaining weight, first replace \(f(J)\) by \(f(F(Z_{-t}))\) at a fixed finite grade \(-t\), with error uniformly small as \(t\to\infty\). Given \(Z_{-t}=x\), the further backward chain is \(P_{h,x}\) and its expectation of \(g\) tends to one by the scalar theorem. Bounded convergence, then \(t\to\infty\), prove (7). Thus every sequence \(k-n\to+\infty\) yields the same ordinary-depth, corrected real law as the separately limiting integer fibres. Finite travel-time offsets retain both the single ternary digit and a negative real tail, which disappears in the deep limiting law.
