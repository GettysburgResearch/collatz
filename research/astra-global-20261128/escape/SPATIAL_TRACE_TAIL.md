# Uniform spatial tails of the stationary trace and its real marks

**Status.** Source-qualified written deductions. The inputs are the weighted first-hit trace, the ordinary component flux and bilateral marked law, and the predecessor-minimum and forward-minimum estimates specified below. The spatial tail is over every positive odd integer. A moving target can change its component with its height.

Let \(U\) be the accelerated odd map, \(w_x=3x/(3x+1)\), \(b_j(x)=\prod_{i<j} w_{U^ix}\), and \(F(x)=\lim_j b_j(x)\). Write \(a_y=h(y)/y\), where \(h\) is the ordinary-depth trace. Let \(\nu_y\) be the stationary probability law of the relative complementary mark \(b=1-R/y\) at a positive odd unit of positive trace. Thus \(a_y\nu_y\) is the harmonic row. Write \(D_s\) for multiplication of this mark by \(s>0\). At nonunits assign the zero row. Define \(\tau_y=1\) at nonperiodic targets and \(\tau_y=1-\lambda_C\) on a cycle with primitive survival multiplier \(\lambda_C\).

For every integer \(M\ge1\) there is a finite exceptional set of targets, depending on \(M\), outside which the entire nonperiodic marked harmonic row is approximated from below by a finite sum of transported rows at ordinary roots \(m\le M\). The missing mass is \(O(M^{-\sigma})\) with the same absolute \(\sigma=1-H_2(\log_3 2)+\xi>0.05004447\) as the predecessor-minimum input. The same power controls the *sum over all escaping components* of the missing mass in the limiting marked profiles after retaining only their last visits to \([1,M]\). Neither the exceptional height nor the fate of any one of the retained ordinary roots is determined by this estimate.

## Precise source interfaces

1. Put \(\kappa=\log(4/3)/2\). For a nonperiodic root, \(a_y=\kappa\beta_y\), where \(\beta_y\) is the odd-relative weighted first-hit density with the actual survival product from source to target. For a periodic root \(\tau_y a_y=\kappa\beta_y\). In either case \(0\le\beta_y\le d_y\), the ordinary relative predecessor density. A legal first-hit path from a nonperiodic \(m\) to nonperiodic \(y=U^k m\) has conditional reverse probability \(a_m b_k(m)/a_y\); conditional on this path the remaining past is the canonical path sampled from \(m\). Its full mark at \(y\) is the product of \(b_k(m)\) and the relative mark from \(m\). Distinct positive odd path segments have survival product at least an absolute \(c_0>0\). [Valbuena, pinned manuscript, weighted-density, canonical-identification, and forward-components propositions](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex) · [PR193, stationary flux and normalization](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md)
2. For each escaping component \(C\), choose one actual ordinary ray \(r_C=(a_{C,n})_{n\ge0}\). The stationary flux \(H_C>0\) equals \(\kappa\langle F1_C\rangle\), with odd-relative logarithmic mean. These fluxes sum to \(\kappa\langle F1_{\rm escape}\rangle\). The bilateral canonical path \((Z_v)_{v\in\mathbb Z}\) has grade-\(v\) marginal \(\Pr_C(Z_v=y)=a_yF(y)/H_C\) for \(y\in C\) of grade exactly \(v\), and zero at every other site. The grade is fixed by assigning grade \(n\) to \(a_{C,n}\) and increasing by one on each forward odd edge. Conditional on that event its past is canonical at \(y\) and its future is the ordinary forward path. Its bilateral product \(J=\prod_{v\in\mathbb Z}w_{Z_v}\) has probability law \(\eta_C\); given \(Z_v=y\), its law is \((D_{F(y)})_*\nu_y\). The events \(Z_n=a_{C,n}\) increase to full probability. The stationary limits and all these distributions retain the true positive integer vertices. [PR193, common coupling and equation (2)](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md) · [Weaver, Paper 176, Theorems 1–2](https://rstation.ai/problems/collatz/papers/176/v1)
3. For an odd unit \(y\), let \(m_*(y)\) denote its least odd predecessor including itself. Uniformly in \(y\), \(d_y\ll m_*(y)^{-\sigma}\). The upper density of sources whose entire forward path stays above \(M\) is \(O(M^{-\sigma})\). This uses the relative-passage and finite-word inputs assembled in [PR213, predecessor-minimum power, conclusions 1 and 3](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/PREDECESSOR_MINIMUM_POWER.md). Weaver's earlier super-logarithmic predecessor-minimum bound also suffices for the qualitative spatial classification. [Paper 12, Theorem 11](https://rstation.ai/problems/collatz/papers/12)

## A finite section at each nonperiodic target

Write \(\mathcal O_M=\bigcup_{m\le M,\ m\,\mathrm{odd}}\{U^j m:j\ge0\}\). At a nonperiodic \(y>M\) let \(E_M(y)\) comprise the odd \(m\le M\) reaching \(y\) such that all strict intermediate states exceed \(M\). Each hitting time \(k_m\ge1\) is unique. The events that a reverse path from \(y\) first visits \([1,M]\) at the indicated \(m\) are disjoint. A last low ordinary vertex before reaching \(y\) has precisely this description, with the original source allowed as that vertex. Consequently
\[
 B_{M,y}=\sum_{m\in E_M(y)}
      a_m b_{k_m}(m)(D_{b_{k_m}(m)})_*\nu_m
       \ \le\ a_y\nu_y                                                    \tag{1}
\]
as measures. Zero-mass nonunit terms may be omitted.

For each \(M\) and all sufficiently large nonperiodic \(y\),
\[
             \|a_y\nu_y-B_{M,y}\|_{\rm TV}\ll M^{-\sigma}.              \tag{2}
\]
We take the variation norm, so the norm of a positive measure is its mass. If \(y\notin\mathcal O_M\), (1) is empty and (2) is the predecessor-minimum bound. Inside \(\mathcal O_M\), only finitely many distinct sites lie at or before a subsequent visit to \([1,M]\). Indeed each one of the finitely many starting paths either visits the low set finitely often, or returns to a low site and has a finite eventual cycle. Taking the finite initial segments through the last low visit in the former case and the whole finite orbit in the latter proves the assertion. Thus, at all sufficiently large \(y\in\mathcal O_M\), the future from \(y\) stays above \(M\).

At those targets the missing mass in (1) is \(\kappa\) times the weighted first-hit density of sources that reach \(y\) without previously visiting \([1,M]\). To check this identity without exchanging an infinite sum of natural densities, partition the first-hit sources by their last low point before \(y\). The partition uses only the finitely many \(m\in E_M(y)\). Every source reaching such an \(m\) first hits \(y\) after that \(m\), since an earlier visit to \(y\) would make \(y\) periodic. Its first-hit product to \(y\) is its first-hit product to \(m\) times \(b_{k_m}(m)\). Subtract the finite sum of these weighted densities from \(a_y/\kappa\). The remaining sources stay above \(M\) for their whole futures, including after \(y\). The global forward-minimum bound proves (2).

For example define \(\omega_m(s)=\sup_{|I|\le s}\nu_m(I)\) on normalized relative marks, with arbitrary interval centers. Since distinct path products in (1) are at least \(c_0\) and \(a_y\le\kappa\), (2) gives
\[
 \limsup_{y\to\infty,\ y\ {\rm nonperiodic}}
        a_y\sup_{|I|\le s}\nu_y(I)
    \le \kappa\max_{m\le M,\ h(m)>0}\omega_m(s/c_0)+C M^{-\sigma}.        \tag{3}
\]
Every fixed \(\nu_m\) is atomless and supported on a compact interval. Its modulus tends to zero. For arbitrary \(r(y)=o(y)\), first take the large-target limit, then \(M\to\infty\). The stationary intercept measure \(M_{\infty,y}\) therefore satisfies the uniform small-window law
\[
 \lim_{Y\to\infty}\ 
  \sup_{\substack{y\ge Y\ {\rm odd,nonperiodic}\\ I\subset\mathbb R\ {\rm interval},\ |I|\le r(y)}}
            y^{-1}M_{\infty,y}(I)=0.                                     \tag{4}
\]
No interval is singled out at the top or bottom of the real support. Neither (2) nor (3) supplies a computable common onset in \(y\).

## Simultaneous disintegration of the escaping mass

For each escaping component let
\[
 E_M(C)=\{m\le M:\ m\in C,\quad U^j m>M\text{ for every }j\ge1\}.
\]
All vertices in this set are nonperiodic. The set is finite, but its infinite future condition is undecided. Define a positive measure
\[
 G_{M,C}=\sum_{m\in E_M(C)}a_m F(m)(D_{F(m)})_*\nu_m .
\]
Then
\[
 0\le G_{M,C}\le H_C\eta_C,\qquad
 \boxed{\quad\sum_C\|H_C\eta_C-G_{M,C}\|_{\rm TV}\ll M^{-\sigma}.\quad}    \tag{5}
\]
On a bilateral sample, any visit to \([1,M]\) has a last such visit because all vertices are distinct. If it is at \(m\), the future restriction in \(E_M(C)\) is deterministic. Conversely the event of occupying this \(m\) at its unique grade ensures it is the last low visit. Its mass and corrected mark law are exactly those used in \(G_{M,C}\), by the grade-marginal and conditional-past identities. Distinct last low events are disjoint, giving positivity.

For the total remainder, an ordinary escaping source whose path visits \([1,M]\) likewise has a unique last low \(m\). Its survival product is the product to first hitting \(m\) times \(F(m)\). Summing the finitely many first-hit identities for \(m\le M\), with the whole escaping mass from source interface 2, gives
\[
 \sum_C\|H_C\eta_C-G_{M,C}\|_{\rm TV}
   =\kappa\langle F\,1_{\rm escape}\,1_{\{\min_{j\ge0}U^jx>M\}}\rangle.
\]
The mean on the right exists by this finite subtraction. The change between ordinary relative natural density and the odd-relative logarithmic bound is harmless by partial summation; upper natural density bounds upper logarithmic density. Applying source interface 3 proves (5). This pays for all components outside the finite collection meeting the low cutoff as well as the missing paths within that collection. Every contributing low vertex is actually in the boundary layer \((2M-1)/3<m\le M\), since its next odd landing is greater than \(M\) and \(U(m)\le(3m+1)/2\).

## Classification of the whole spatial trace at infinity

Use \(F(y)\) to rescale \(\nu_y\) on escaping components and use the identity on all other components; call the resulting probability \(\widehat\nu_y\). Each choice of one actual ray \(r_C\) per escaping component gives
\[
 \boxed{\quad
 \lim_{Y\to\infty}\sup_{y\ge Y\ {\rm odd}}
   \left\|\tau_y a_y\widehat\nu_y
       -\sum_C 1_{\{y\in r_C\}} H_C\eta_C\right\|_{\rm TV}=0 .
 \quad}                                                                  \tag{6}
\]
At most one term on the right is present at any site. For a given \(\varepsilon>0\) choose \(M\) so large that \(\tau_y a_y\le\kappa d_y<\varepsilon\) whenever \(y\notin\mathcal O_M\). If \(C\) has no odd member through \(M\), all its ray sites satisfy this bound, so \(H_C\le\varepsilon\) by the single-ray limit. If \(C\) contains a low site, its forward path eventually meets the selected ray and includes the remaining tail. Thus at all sufficiently large sites of the finitely many such rays the site belongs to \(\mathcal O_M\).

The finite union \(\mathcal O_M\) itself, apart from a finite set, is contained in the selected rays for its escaping components. Each individual low-start orbit either has finite range or eventually coincides with the selected ray for its component. Along such a ray set \(A_n=\{Z_n=a_{C,n}\}\). The submeasure \(a_{a_{C,n}}F(a_{C,n})\widehat\nu_{a_{C,n}}\) is precisely \(H_C\mathcal L_C(J;A_n)\), and \(\Pr_C(A_n)\to1\). Also \(F(a_{C,n})\to1\) from reciprocal packing. Thus the total-variation discrepancy tends to zero on each of these finitely many tails. The bound off those tails is at most \(2\varepsilon\), after raising the height past a finite exception. This proves (6).

Taking total masses shows that the positive spatial cluster values of \(\tau_y h(y)/y\), as \(y\to\infty\) through positive odds, are exactly the distinct \(H_C\)'s. Indeed \(\sum_C H_C\le\kappa\) leaves finitely many charges above each positive threshold. Each is attained as a limit on its ray. Zero is a cluster value already on nonunits. The scalar ingredients and the conditional limit along a single specified ray precede this note. The uniform statement (6) also covers changing components, off-ray branches, and the lap-corrected masses of periodic sites. The correction in the mark avoids asserting convergence in total variation after a varying near-identity dilation of a singular measure.

The first-arrival scalar \(\tau_y a_y\) in (6) multiplies the full conditional mark law. On periodic sites this is only a scalar normalization. The question whether every escaping mass \(H_C\) vanishes remains open. Formula (5) isolates it in weights at actual last departures from finite height floors; proving their decay would require a bound on their original forward futures.

## Uniform concentration without a target-height onset

The concentration estimate can be made simultaneous in **all** odd targets, including periodic ones. For \(M\ge1\), let
\[
 K_M=\max\bigl(\kappa,\ c_0^{-1}\max_{m\le M,\ m\ {\rm odd}} a_m\bigr),
 \qquad \Omega_M(u)=\max_{m\le M,\ h(m)>0,\ m\ {\rm odd}}\nu_m(I_u)^* ,
\]
where \(\nu_m(I_u)^*=\sup\{\nu_m(I): I\text{ is an interval of length at most }u\}\). In these definitions roots of total mass zero can be discarded. For every \(s>0\), \(0<\theta<1\), and integer \(M\ge1\),
\[
 \boxed{\quad
 \sup_{y\ {\rm positive\ odd}}\tau_y a_y\nu_y(I_s)^*
 \ \le\ K_M\Omega_M\!\left(\frac{s}{c_0\theta}\right)
          + C M^{-\sigma}+\kappa\theta.\quad}                           \tag{7}
\]
In particular the left side tends to zero as \(s\downarrow0\), by first fixing \(M,\theta\) and then making their two error terms small. This extends (4) to all targets with the periodic lap correction.

If \(y\) has a future visit to \([1,M]\), use its first such visit \(m\) (possibly \(m=y\)). The segment of length \(k\) to that visit has distinct departed sites, since any previously completed cycle would have precluded a first later visit. Its product \(b_k(y)\) is at least \(c_0\). Stationary transfer along this particular reverse path gives
\[
     a_y b_k(y)(D_{b_k(y)})_*\nu_y\le a_m\nu_m.
\]
Thus \(\tau_y a_y\nu_y(I_s)^*\le c_0^{-1}a_m\Omega_M(s)\), including when \(m\) is periodic.

If the future from \(y\) never visits \([1,M]\), let \(\phi_y=a_y\nu_y\) at a nonperiodic site. At a periodic site let
\[
 \phi_y=a_y\nu_y-\lambda_C a_y (D_{\lambda_C})_*\nu_y .
\]
This positive measure is exactly the contribution from reverse paths that do not begin with the whole primitive cycle through \(y\). Its total mass is \(\tau_y a_y\), the weighted first-hit mass. Repeat (1) for sources first arriving at \(y\), using only their first path to \(y\) from a last low \(m\). Such an \(m\) cannot be on \(y\)'s cycle, since the future from \(y\) avoids the low set. Its reverse cylinder does not begin with a complete lap and hence contributes to \(\phi_y\). Distinct last low choices have disjoint cylinders. The remaining mass is the first-hit density of sources avoiding low vertices before \(y\), with their weight and the factor \(\kappa\). Their whole futures avoid the low set, by the present case. In this case the argument yielding (2) has no exceptional targets. Since \(\phi_y\) has mass at most \(\kappa\), we get
\[
     \phi_y(I_u)^*\le \kappa\Omega_M(u/c_0)+CM^{-\sigma}.
\]
At a periodic site the full all-visit law is
\[
       a_y\nu_y=\sum_{j\ge0}\lambda_C^j(D_{\lambda_C^j})_*\phi_y
\]
by telescoping successive reverse laps. After multiplying by \(1-\lambda_C\), the total of the geometric coefficients is one. Those with \(\lambda_C^j<\theta\) have coefficient sum at most \(\theta\); their full contribution is at most \(\kappa\theta\). The other terms pull a window of length \(s\) back to length at most \(s/\theta\). The nonperiodic case uses just \(\phi_y\). This proves (7).

On the full-dimensionality input in PR193 there is also uniform control over many intervals at once. For every \(0<\alpha<1\) and \(\eta>0\) there is a finite \(K_{\alpha,\eta}\) such that every positive measure \(\tau_y a_y\nu_y\) has a submeasure \(\mu_y\) satisfying
\[
       \|\tau_y a_y\nu_y-\mu_y\|_{\rm TV}\le\eta,\qquad
       \mu_y(I)\le K_{\alpha,\eta}|I|^\alpha
            \quad\text{for every real interval }I.                     \tag{8}
\]
To check this, choose \(M,\theta\) so the two remainder terms in (7) cost at most \(\eta/2\). Each of the finitely many reference fibres has exact dimension one. Consequently, for any \(\delta>0\), it has a restriction of mass at least \(1-\delta\) satisfying a common \(\alpha\)-power interval bound. Indeed almost every point has \(\nu_m(B(x,r))\le r^\alpha\) for all sufficiently small \(r\); exhaust by fixed onset scales. For an interval meeting the restricted support, use a ball centered in that interval with radius twice its length. Increase the constant for the finitely bounded larger scales and for the finite list of roots.

In the first case of the proof of (7), pull the retained subset at \(m\) back through its positive dilation. The weight of the lost subset is at most \(K_M\delta\), and the retained dilate of the dominated measure has a common power bound. In the second case replace every low-root contribution to \(\phi_y\) by its retained part and discard the residual. The omitted low-root mass costs at most \(\kappa\delta\) since the weights sum to at most \(\kappa\). All retained dilations in the truncated lap mixture are at least \(c_0\theta\). Averaging their power bounds gives one finite constant. Choose \(\delta\) small enough in terms of \(M,\eta\). This proves (8), including every root whose first-arrival harmonic mass is bounded below. Constants arising from the individual low-root concentration functions are not claimed effective. The exponent one would in particular force absolute continuity after arbitrarily small trimming at each fixed positive root; the cited stationary fibres are singular, including at known terminating roots.
