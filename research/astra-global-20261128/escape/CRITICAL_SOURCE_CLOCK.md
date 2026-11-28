# A critical source-clock limit for every ordinary loss and escape outcome

**Status.** Written deductions from the source-qualified ordinary trace at each positive odd unit, the inverse-path law of large numbers there, the stationary total budget, and the original marked convergence in this packet. The existence and size of escaping components remain undetermined. The natural-source Gaussian transition for the untagged deterministic correction and its finite half-mean test were obtained previously in [PR145](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/unsafe-return-weights/DISTORTION_CUTOFF.md). The present allocation resolves each killed ordinary site, each surviving native component, and its own real mark at the source-power clock.

Let \(D=\log(4/3)\), \(\kappa=D/2\). For \(u>0\) sample a positive odd integer \(x\) with probability proportional to \((\rho_1(x)/x)^{1+u}\), \(\rho_1(x)=x\bmod3\). Follow its actual accelerated Collatz orbit. At each ordinary site \(y\) kill with probability \(1-w_y^{1+u}\), independently given survival to that site, where \(w_y=3y/(3y+1)\). A kill at depth \(d\), before departure from \(y=U^dx\), records the site, scaled age \(u d\), and the true product \(b_d(x)=\prod_{j<d}w_{U^jx}\).

A survivor necessarily belongs to an escaping component \(C\). There record the component, the scaled negative grade \(-u\,\mathrm{grade}_C(x)\) and the product \(F(x)=\prod_{j\ge0}w_{U^jx}\). The chosen grade of an ordinary site increases by one on every forward odd edge and has zero at the selected ray origin. The survivor grade statistic can be negative at finite \(u\).

As \(u\downarrow0\), the scaled age converges to an exponential variable of rate \(D\). It is independent of the limiting joint law of the discrete outcome and its real product. The latter probability measure has rows
\[
  \boxed{\quad \kappa^{-1}(1-w_y)a_y\nu_y
    \text{ at each ordinary killed site }y,\qquad
    \kappa^{-1}H_C\eta_C
    \text{ at each escaping component }C .\quad}                       \tag{1}
\]
For the sampled source itself, \(u\log x-D\cdot(\text{scaled age})\to0\) in probability. All cycles contribute with every ordinary visit allowed. Both the distribution of the real product within an outcome and the relative sizes of outcomes in (1) are inherited from the positive map.

## The finite arrays

To describe convergence at all ages, initially use unnormalized source masses and multiply them by \(u\). Their total tends to \(1/2\):
\[
   u Z_u=u\sum_{x\ {\rm odd}}(\rho_1(x)/x)^{1+u}\longrightarrow1/2.
\]
The odd-relative average of \(\rho_1\) is one and \(\rho_1^{1+u}-\rho_1=O(u)\) uniformly. Abelian summation gives the formula.

For \(t\ge0\) put \(d=\lfloor t/u\rfloor\), \(p=1+u\). The unnormalized kill density, spreading each time atom across the interval \([ud,u(d+1))\), is the positive mark measure
\[
 K_u(t,y)=(1-w_y^p)\sum_{U^d x=y}
       (\rho_1(x)b_d(x)/x)^p\,\delta_{b_d(x)}.                          \tag{2}
\]
Its time integral is exactly \(u\) times the corresponding unnormalized kill mass. At \(t<0\) set \(K_u=0\). For every real \(t\), put \(v=-\lfloor t/u\rfloor\). The survivor density on the same width cells is
\[
 E_u(t,C)=\sum_{\substack{x\in C\ {\rm unit}\\\mathrm{grade}_C(x)=v}}
        (\rho_1(x)F(x)/x)^p\,\delta_{F(x)}.                              \tag{3}
\]
Write \(K(t,y)=1_{t>0}e^{-Dt}(1-w_y)a_y\nu_y\) and
\(E(t,C)=1_{t>0}e^{-Dt}H_C\eta_C\). For every fixed \(1<q<\infty\), with \(V_q\) the disjoint-interval norm in [the variation theorem](VARIATION_PROFILE.md), the joint convergence is
\[
 \int_{\mathbb R}\left(\sum_y V_q(K_u(t,y)-K(t,y))
             +\sum_C V_q(E_u(t,C)-E(t,C))\right)dt\longrightarrow0.     \tag{4}
\]
In particular every measurable choice of an age set, a collection of ordinary sites or components, and a mark interval depending on the age and outcome is controlled for the interpolated age. The underlying lattice age differs from the interpolated age by at most \(u\), so it has the same asserted joint weak limit and closeness to \(u\log x/D\). A total-variation statement in the continuous age coordinate for the original lattice law would fail.

## The local limits and tightness

Fix an ordinary positive odd unit \(y\) and a sequence \(u\downarrow0\) at a fixed \(t>0\). On its canonical inverse path let \(X_d\) be the actual source, \(S_d\) its division clock, and \(g=\rho_1/h\) the bounded terminal density. The canonical representation of [the finite original row](ALL_DEPTH_SPATIAL_PROFILE.md) shows that the positive sum in (2), before multiplication by \(1-w_y^p\), equals
\[
     a_y\,\mathbb E_y\left[
       g(X_d)\left(\frac{\rho_1(X_d)3^d 2^{-S_d}}{y}\right)^u
       \delta_{b_d(X_d)}\right].                                        \tag{5}
\]
The arbitrary-fixed-root inverse clock law gives \(S_d/d\to2\) and \(\log X_d/d\to D\) almost surely. Thus the factor in parentheses to the power \(u\) tends almost surely to \(e^{-Dt}\). It is at most \([2(3/2)^d]^u\), bounded uniformly when \(t\) lies in a compact interval. Under the canonical law all terminal sites are units, so \(\rho_1(X_d)\ge1\). By dominated convergence the difference from \(e^{-Dt}P_{d,y}\) tends to zero in variation norm; the common mark on each path can be arbitrary for this comparison. The finite original \(P_{d,y}\) tends to \(a_y\nu_y\) in cumulative norm with uniformly bounded mass. Interpolation by (1) of the variation theorem gives its convergence in every \(V_q\) above one. This proves \(K_u(t,y)\to K(t,y)\) in each such norm. Nonunits are zero rows. [Fixed-root canonical clock and growth theorem, PR193, (1)](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

The unmarked stopped sums \(\sum_y(1-w_y)P_{d,y}([0,1])\) converge with tight rows by [the summable original variation](SUMMABLE_ORIGINAL_TRACE.md); the limit rows are \((1-w_y)a_y\). Here the stopped weight for the normalized \(P_{d,y}\) is exactly \(1-w_y\). From \(1-w_y^{1+u}\le(1+u)(1-w_y)\) and the uniform upper bound for the tilt in (5), these rows dominate the masses of \(K_u(t,y)\) up to a bounded factor on each fixed compact time interval. Thus the summed convergence over all ordinary sites holds at every \(t>0\). The summed norms remain uniformly bounded on compact time intervals, giving convergence after integration there.

For a fixed escaping component \(C\) and \(t>0\), use the actual bilateral source \(Z_v\) in (3). Its nonnegative mark weight before the power tilt is \(H_Cg(Z_v)\); the remaining tilt is \([\rho_1(Z_v)F(Z_v)/Z_v]^u\). Conditional on \(Z_0\), the earlier path is canonical at that specified ordinary root. Therefore \(\log Z_v/(-v)\to D\) almost surely as \(v\to-\infty\). The product \(F\) has a uniform positive floor on escaping paths and \(1\le\rho_1\le2\) at units. The tilt tends to \(e^{-Dt}\) and is bounded by \(2^u\). Dominated convergence again removes the tilt with an error tending to zero in variation norm. The remaining phase law \(\Gamma_{C,v}\) tends to \(H_C\eta_C\) in cumulative norm, hence in \(V_q\) by interpolation. [Original phase formula and backward end](ALL_DEPTH_SPATIAL_PROFILE.md).

The total mass of each positive-time row (3) is at most \(2^u G H_C\). The charges sum to at most \(\kappa\). This proves convergence summed over components and integrated over compact positive times. Finally the total of (2) and (3) over all outcomes and the whole real time axis is precisely \(u Z_u\), since kill and survival exhaust each positive source. The candidate positive limiting densities have exactly the same total:
\[
   D^{-1}\left(\sum_y(1-w_y)a_y+\sum_C H_C\right)=\kappa/D=1/2.
\]
This uses the known stationary loss and cemetery identity, and bypasses any appeal to uniform diagonal first-passage times or a separate Mellin estimate for survivors. Exhaust \([0,\infty)\) by compact intervals. The norms at missing times are at most the totals of the positive measures there, and equality of the full limiting mass forces their combined error to zero. In particular the negative scaled ages of survivors carry vanishing mass. This proves (4). Normalization gives (1). [Stationary total and cemetery budget, PR193 (1), citing Weaver 176, Theorem 2](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md).

To verify the asserted source-height relation, fix \(\varepsilon>0\). Insert the indicator \(1_{\{|u\log X_d-Dt|>\varepsilon\}}\) in (5); the integrand tends to zero at each specified \(y,t>0\) by the same almost-sure root theorem. For (3) insert \(1_{\{|u\log Z_v-Dt|>\varepsilon\}}\) on the bilateral path, using the same conditional root law. The already proved compact tightness in outcome and global tightness in age show that their entire probabilities tend to zero. The interpolation moves \(t\) by at most \(u\).

## Scalar survival through a growing number of genuine odd steps

Let \(A_p(d)=\sum_{x\ {\rm odd}}(\rho_1(x)b_d(x)/x)^p\) and \(H=\sum_C H_C\). The exact depletion \(A_p(d)-A_p(d+1)=\sum_y K_u(ud,y)([0,1])\) and the preceding result give, at every \(t\ge0\),
\[
   \boxed{\quad
    \lim_{u\downarrow0}u A_{1+u}(\lfloor t/u\rfloor)
           =\tfrac12 e^{-Dt}+\frac{H}{D}(1-e^{-Dt}).\quad}              \tag{6}
\]
The convergence of these survival functions is uniform on the full half-line: the difference from the initial mass is their cumulative time integral, whose full \(L^1\) error tends to zero, and the exponentially weighted limiting density has uniformly small mass on one cell. At infinite depth the limit is \(H/D\). Equation (4) records every surviving component and its true real product as well as every finite killing site. With normalized probabilities the plateau is \(H/\kappa\). For any fixed \(t>0\), a separate proof of the upper bound \(\liminf_{u\downarrow0}u A_{1+u}(\lfloor t/u\rfloor)\le e^{-Dt}/2\) would exclude all escaping components. Formula (6) alone leaves the plateau undetermined.
