# A critical real-marked susceptibility computed from fixed ordinary terminals

**Status.** Written, source-qualified theorem. It gives an absolutely convergent signed formula using only fixed ordinary inverse fibres for a positive measure supported by the bilateral correction of the escaping components. The sign of the scalar test below is unresolved.

Let \(w_y=3y/(3y+1)\) for positive odd \(y\), \(f_k(v)=\prod_{i<k}w_{S^iv}\), and \(F(v)=\lim f_k(v)\). Let \(h(y)\) be the ordinary stationary ternary trace; it is zero at odd multiples of three. At a unit let the canonical inverse chain from \(y\) have limiting real affine offset \(R_y\). Write \(A_y=1-R_y/y\). At each fixed unit \(0<A_y<1\) almost surely: the first inverse step gives positive offset; for nonperiodic roots the uniform simple-path product is positive, and the canonical chain from a periodic root departs its lap after finitely many turns almost surely, as its lap multiplier is strictly below one. The remaining simple inverse tail has positive product. The inverse chain and its affine real law at ordinary roots are the inputs in [Weaver, Paper 19, §9.2](https://rstation.ai/problems/collatz/papers/19) and [PR193, canonical integer real fibres and the bilateral component coupling](https://github.com/GettysburgResearch/collatz/blob/795cfa38fbd6a2436285edfe82580680df4f9b0d/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md).

For each Lipschitz \(\phi:[0,1]\to\mathbb R\) with \(\phi(0)=\phi(1)=0\), define
\[
 L_\phi=\sum_{y\ {\rm unit}}\frac{h(y)}y
   \mathbb E_y\frac{\phi(w_y A_y)-\phi(A_y)}{A_y}.                   \tag{1}
\]
This sum is absolutely convergent, since each absolute summand is at most \(\operatorname{Lip}(\phi) h(y)/[y(3y+1)]\), whose sum is finite by [Weaver, Paper 176, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1). If \(C\) is an escaping component, put \(P(v)=v/F(v)\), \(M_v=h(v)/P(v)\), and let \(H_C\) be its conserved mass on every grade. Write \(J_C\) for the product of \(w\) along the actual bilateral ordinary path distributed by the probability grade flux \(M_v/H_C\). Then
\[
                   L_\phi=\sum_{C\ {\rm escaping}}
                     H_C\,\mathbb E[\phi(J_C)/J_C].                  \tag{2}
\]
Each \(J_C\in(0,1)\). Thus the signed functional on the left is positive on nonnegative tests. In particular the strict positivity of (1) for the single polynomial \(\phi(t)=t(1-t)\) is equivalent to the existence of an escaping positive integer, allowing any number of positive cycles.

## Ordinary component proof and cancellation at cycles

First take a nonnegative test supported in a compact subinterval of \((0,1)\). Put
\[
 I_y=\frac{h(y)}y\,\mathbb E_y[\phi(A_y)/A_y],\qquad
 O_y=\frac{h(y)}y\,\mathbb E_y[\phi(w_y A_y)/A_y].
\]
Give nonunits zero flux. The canonical first inverse step \(x\) from \(y\) has probability \(3\,2^{-e(x)}h(x)/h(y)\), and on this branch \(A_y=w_x A_x\) in law. The affine identity \(3\,2^{-e(x)}/y=w_x/x\) yields exactly \(I_y=\sum_{Sx=y} O_x\). The summand in (1) is \(O_y-I_y\).

If either term is nonzero at a nonperiodic unit \(y\), some finite or infinite simple backward path through \(y\) has accumulated at least a fixed positive logarithmic correction, with \(y\) itself included if needed. More explicitly, if \(\operatorname{supp}\phi\subset[0,1-\delta]\), the sum of \(-\log w\) along this path including \(y\) is at least \(-\log(1-\delta)\). Select \(B\) with \(T(B)/3<-\log(1-\delta)\) in the [uniform simple-path reciprocal bound](FIXED_FLOOR.md). This forces an ordinary point at most \(B\) on the path. In particular \(y\) is forward of one of finitely many such points. Both fluxes on any cyclic component therefore have finite support: include the finite cycle itself and the finite forward orbits of its points through \(B\). Their component sum is zero, without an assertion of absolute summability of the undifferenced fluxes across components.

On an escaping component, the two flux supports are included in the finite branches and common future tail of the finitely many points through \(B\); if there are none both fluxes vanish. Take \(a_n=S^n a_0\) on this tail. Summing the divergence over the finite truncated union through \(a_n\) gives \(O_{a_n}\). On the bilateral path of PR193 conditional on visiting \(a_n\), we have \(F(a_n)A_{a_n}=J_C\). Also \(M_{a_n}\to H_C\), \(F(a_n),w_{a_n}\to1\), and the probabilities of these conditioning events tend to one. Hence
\[
 O_{a_n}=M_{a_n}\mathbb E[\phi(w_{a_n}J_C/F(a_n))/J_C\mid a_n\ {\rm visited}]
              \ \longrightarrow\ H_C\,\mathbb E[\phi(J_C)/J_C].
\]
The simple-path bound keeps \(J_C\) uniformly above zero, and the Lipschitz bound would also give domination here. Absolute convergence in (1) permits component grouping. In a component containing no point through \(B\), the entire bilateral path has \(J_C>1-\delta\), so its contribution in (2) vanishes. For general nonnegative Lipschitz \(\phi\) with zero endpoints use compact cutoffs \(\min(\phi,(\operatorname{Lip}\phi)\,d(\cdot,[0,\epsilon]\cup[1-\epsilon,1]))\). Their Lipschitz constants are uniformly bounded and their values increase to \(\phi\). Dominated convergence applies on the left and monotone convergence on the right. Subtract the positive and negative parts for a signed test.

## The first real moment and the exact surviving term

Set \(N_y=h(y)\mathbb E_y R_y\), \(U_y=N_y/y^2\), and \(c_y=3h(y)/(3y+1)^2\). Let \(b_x=3\,2^{-e(x)}\) denote the one-odd-step multiplier from \(x\) to \(Sx\). The first reversed affine offset is \(b_x/3\), and the remaining real series is multiplied by \(b_x\). Thus
\[
 N_y=\sum_{Sx=y}\left(b_x^2N_x+\tfrac13 b_x^2h(x)\right),\qquad
 U_y=\sum_{Sx=y}\left(w_x^2 U_x+c_x\right).                       \tag{3}
\]
All terms are nonnegative. The affine series for \(R_y\) is the increasing sum of its individual step offsets. Consequently (3) gives the *minimal* nonnegative Green solution: each \(c_x\) is injected at \(Sx\) and subsequently retains the factor \(w_z^2\) at each departure from \(z\). This assertion follows by expanding finite nonnegative partial offset sums then taking the limit, with no inversion or uniqueness premise.

For \(\phi(t)=t(1-t)\), equation (1) becomes
\[
 \begin{split}
 L_\phi
 &=\sum_y \frac{h(y)}{y(3y+1)}
       \left[w_y-(1+w_y)\frac{\mathbb E_y R_y}{y}\right]\\
 &=\sum_y c_y-\sum_y(1-w_y^2)U_y
   =\sum_y c_y F(Sy)^2
   =\frac13\sum_{y\ {\rm escaping}}\frac{h(y)}{P(y)^2}.             \tag{4}
 \end{split}
\]
Both source and loss sums are finite by the same discounted trace bound. For the third equality, along the deterministic path starting at \(Sy\) the sum of its successive lost fractions is \(1-F(Sy)^2\), by the finite product telescope and a limit. Tonelli sums these losses over the injected \(c_y\)'s. Reindexing the undamped sum of the \(U_y\)'s would be invalid: on an escape ray its terms tend to \(H_C\mathbb E[1-J_C]>0\). On the bilateral path the independent check is
\[
 F(Sv)-F(v)=\frac1{3P(v)},\qquad
 \sum_{j\in\mathbb Z}\frac1{3P(Z_j)}=1-J_C .
\]
Averaging the last identity with the grade flux gives agreement of (2) and (4). The rightmost series in (4) has a strictly positive summand at each escaping unit under the ordinary trace positivity input. Equation (4) recovers it through a difference of two absolutely convergent fixed-target inverse statistics. A proof that all input is eventually lost would still be needed for universal nonescape.

## Physical finite-depth susceptibility

For each fixed \(k\) write
\[
                  B_k(\phi)=\sum_{v>0\ {\rm odd}}\phi(f_k(v))/v .
\]
This is absolutely convergent. Indeed \(|\phi(f_k)|\le\operatorname{Lip}(\phi)(1-f_k)\), and the positive product telescope gives
\(\sum_v(1-f_k(v))/v=\sum_{i<k}\sum_y W_i(y)/[y(3y+1)]<\infty\), where the discounted finite-depth masses are those of Paper 176, and \(W_0(y)=1\). For a word from \(v\) to \(y=S^kv\), its multiplier \(M\) satisfies \(M/y=f_k(v)/v\) and \(f_k(v)=1-R_{v,k}/y\). Grouping the exact first difference by \(y\) therefore gives
\[
 B_{k+1}(\phi)-B_k(\phi)=
 \sum_y \frac1y\sum_{S^kv=y} M\,
            \frac{\phi(w_y f_k(v))-\phi(f_k(v))}{f_k(v)}.            \tag{5}
\]
The finite-depth total at each \(y\) converges to the expectation in (1). For completeness, take a fixed number \(t\) of first reversed letters at a fixed unit \(y\). For each legal prefix ending at \(x\), its unnormalized continuation mass is its multiplier times \(W_{k-t}(x)\to h(x)\). The limiting prefix masses sum to \(h(y)\) by harmonicity, and the total masses \(W_k(y)\to h(y)\); hence discrete total-variation convergence of this prefix. Alternatively for the whole real offset at individual depths one can use the canonical chain: for \(k\ge1\) sum its first \(k-1\) reversed steps with the extra bounded weight \(W_1(X_{k-1})/h(X_{k-1})\) for the last finite step. The final individual offset is at most \(3^{k-1}2^{-D_{k-1}}/2\le y/(2X_{k-1})\to0\) almost surely; the canonical root path goes to infinite height backwards almost surely. The bounded weight is at most \(2/\inf_{\rm units}h\). For each fixed prefix the conditional weight tends to one by the scalar ordinary-depth theorem, as in PR193's ordinary-depth fibre proof. First truncate the real series at fixed depth, apply this conditional convergence, and then let the truncation grow, by dominated convergence. This proves weak convergence of the finite physical real-offset laws to \(h(y)\operatorname{Law}(R_y)\). The test in (5) is continuous for positive \(f\), bounded by \(\operatorname{Lip}(\phi)(1-w_y)\), and its only possible endpoint discontinuity is at zero, which has no limiting mass. The conclusion follows also for nonunits, at which positive-depth mass is zero. The bound in \(y\) for (5) is \(\operatorname{Lip}(\phi) W_k(y)/[y(3y+1)]\). The discounted stopping measures converge in ordinary \(\ell^1\) by Paper 176, so their tails are uniformly tight, and
\[
                    B_{k+1}(\phi)-B_k(\phi)\longrightarrow L_\phi .
\]
This is an individual-depth limit; summing gives the same limit for \(B_k(\phi)/k\). The formula uses finite physical real series, while Paper 19's stationary quotient formulation retains a final independent suffix. The difference of these constructions at fixed roots is handled above. [Weaver, Paper 176, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1) · [PR193, individual-depth canonical-fibre proof](https://github.com/GettysburgResearch/collatz/blob/795cfa38fbd6a2436285edfe82580680df4f9b0d/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md)

## A real threshold function with a positive singular derivative

For \(0<t<1\), set, up to changes on a Lebesgue-null set,
\[
 K(t)=\sum_{y\ {\rm unit}}\int_{(1-t)y-t/3}^{(1-t)y}
                     \frac{h(y)\,\mu_y(dr)}{y-r},                   \tag{6}
\]
where \(\mu_y\) is the law of \(R_y\) and either endpoint convention is harmless in the integral in \(t\). All strips have absolute real width \(t/3\). Indeed the strip condition is \(w_y A_y<t\le A_y\). Tonelli gives
\[
 \int_0^1 K(t)\,dt=\sum_y\frac{h(y)}{y(3y+1)}<\infty.
\]
For a compactly supported smooth test, (1) equals \(-\int K(t)\phi'(t)\,dt\). Thus \(K\) has a nondecreasing representative and its distributional derivative on the open interval is exactly
\[
                 dK=\sum_C H_C\,\operatorname{Law}(J_C)(dt)/t .   \tag{7}
\]
The stationary component coupling in the cited PR193 gives each \(\operatorname{Law}(J_C)\) singular continuous of dimension one, under counted coalescence and the stated canonical path inputs. Hence (7) is a positive singular continuous measure. In particular, proving that this *specific fixed-root strip sum* is locally absolutely continuous on \((0,1)\) would exclude every escape. The absolute convergence established for (1) tests Lipschitz differences. It does not establish local absolute continuity of (6).

There is an exactly constant contribution in (6) from each cyclic component. This follows from its zero derivative by the preceding component proof. For an escaping component separately, its contribution is precisely
\[
                   K_C(t)=H_C\,\mathbb E[{\bf1}_{\{J_C<t\}}/J_C]
\]
for almost every \(t\). Along one bilateral path write \(Z_j\) for its successive states. At grade \(j\) the interval of thresholds is
\((w_{Z_j}J_C/F(Z_j),J_C/F(Z_j)]\). The endpoints telescope as the grade increases, because \(F(Z_j)=w_{Z_j}F(Z_{j+1})\). At the past end \(F(Z_j)\to J_C\); at the future end \(F(Z_j)\to1\). These intervals partition \((J_C,1)\) up to endpoints. The factor on that path is \(H_C/J_C\), by the definition of \(M_x\). This proves the formula by Tonelli and retains the actual ordinary point in its branch.

### An exact dyadic and ternary balance for a.e. real slope

Let \(\lambda_a=h(a)\mu_a\) at an odd unit \(a\), and zero at odd nonunits. For \(y=2^j a\) with \(a\) odd, define a positive real-coordinate measure \(\lambda_y=2^j(D_{2^j})_*\lambda_a^{\{e_1>j\}}\), where the superscript restricts the actual first canonical reversed exponent before projecting to the real coordinate; \(D_b(r)=br\). This defines the even-root quantities directly. The first branch formula, or removing the layer \(e_1=j+1\), gives
\[
 2(D_2)_*\lambda_y=\lambda_{2y}
     +3\,{\bf1}_{\{3\mid2y-1\}}(r\mapsto3r+1)_*\lambda_{(2y-1)/3}. \tag{8}
\]
For the removed layer the unique predecessor is \(x=(2y-1)/3\), the identity \(2^{j+1}R_a=1+3R_x\) holds, and its scaled mass is \(3h(x)\). The formula also covers a nonunit predecessor with zero trace.

For \(t\in(0,1)\) put \(s_t(y,r)=(y-r)/t-y\). Let \(\mathcal M_{t,\rm all}\) sum the pushforwards of \(\lambda_y(dr)/(y-r)\) under \(s_t\) over all positive \(y\); use odd and even subscripts for the two parts. These can be used on bounded subsets of \([0,\infty)\) for Lebesgue-almost every \(t\): the integral over all slopes of the mass in \([0,X]\) is at most \(\sum_y X\lambda_y(\mathbb R)/[y(y+X)]<\infty\). Here \(\sum_y\lambda_y(\mathbb R)/y^2\le2\sum_{a\ {\rm odd}}h(a)/a^2<\infty\) by the even-lift definition and the discounted trace theorem. Scaling the residual \(y-r\) and the variable \(s_t\) in (8) yields the measure balance
\[
 (s\mapsto2s)_*\mathcal M_{t,\rm all}
    =\mathcal M_{t,\rm even}+(s\mapsto3s-1)_*\mathcal M_{t,\rm odd}.
\]
Consequently for every fixed \(X\ge1\) and almost every \(t\),
\[
 K(t)=\mathcal M_{t,\rm all}((X/2,X])
       -\mathcal M_{t,\rm odd}(((X+1)/3,X]).                         \tag{9}
\]
In this normalization \(K(t)=\mathcal M_{t,\rm odd}([0,1/3))\). Apply the balance to \([0,X]\). Countably many choices of \(X\) may be imposed simultaneously. Dropping both large-scale shell terms by formally using the entire positive half-line would be erroneous, since each undamped half-line mass can be infinite. Formula (9) gives a concrete large-scale arithmetic target for the local absolute-continuity question about (6).

[Susceptibility.lean](Susceptibility.lean) kernel-checks the two rational coefficient identities in (3)–(4) and the finite source-minus-loss product telescope. [Strict compiler and axiom output](../../../reports/astra-sixhour-20261127/transport/susceptibility-lean.txt). The canonical-measure, infinite-series, and differentiation arguments are written proofs.
