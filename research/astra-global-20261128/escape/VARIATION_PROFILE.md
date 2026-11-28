# Disjoint interval variation and the complete marked derivative on escaping rays

**Status.** The period and transport estimates below are written deductions for the original positive integer law. The signed period estimate uses Tao's fine-trit theorem through [the full-threshold estimate](SUMMABLE_ORIGINAL_TRACE.md). The identification of the countably many escaping profiles uses the ordinary stationary trace and bilateral path inputs in [the all-depth profile](ALL_DEPTH_SPATIAL_PROFILE.md). The positive individual-atom estimates in the last section require only the actual affine words and elementary arithmetic up through (8).

For \(1<p<\infty\) and a finite signed measure \(b\) on the real line, put
\[
 V_p(b)=\sup_{I_1,\ldots,I_m}
       \left(\sum_{i=1}^m |b(I_i)|^p\right)^{1/p},
\]
with the supremum over every finite family of pairwise disjoint intervals. Allow all endpoint conventions and singletons. Write \(K(b)\) for the supremum of the absolute cumulative mass on a lower ray. The cumulative mass on an open lower ray is a limit of values on closed lower rays. Thus
\[
      V_p(b)\le [2K(b)]^{1-1/p}\|b\|_{\rm TV}^{1/p}.                 \tag{1}
\]
The analogous assertion holds with upper rays, including the full line as a limit. Indeed each interval discrepancy is at most twice the ray norm and the sum of their absolute discrepancies is at most the variation norm. Minkowski gives the triangle inequality; all positive dilations and all affine bijections with positive slope are isometries for \(V_p\). Each assertion holds for countably supported measures, with no continuity hypothesis on mark distributions.

Use the original intercept rows \(M_{d,y}\) of total mass \(\rho_{d+1}(y)\), including target one and every visit to a cycle. Let \(n_{p,d}(y)=V_p(M_{d+1,y}-M_{d,y})\). Each row in intercept coordinates is periodic as a function of the ordinary odd representative modulo \(q_d=3^{d+2}\), so the same holds for \(n_{p,d}\). Write \(h_{p,d}\) for its mean on that period. The *mean* of \(\|M_{d+1,y}-M_{d,y}\|_{\rm TV}\) is at most two. Indeed the means of the two positive row masses are each one: over compatible residues each terminal trit is equally frequent and \(\rho_1\) has mean one. The probabilities of all length-\(d\) geometric words sum to one. Combining (1) with finite-period Hölder and the preceding superpolynomial estimate on the mean upper-ray norm gives
\[
 h_{p,d}\le (2H_d)^{1-1/p}2^{1/p}\ll_{p,B}(1+d)^{-B}
       \qquad(B>0).                                                  \tag{2}
\]
Both words in a consecutive difference propagate by the same increasing affine map at every first edge. The triangle inequality thus gives the physical subtransport for \(n_{p,d}\). Applying the moving cutoff and the one-edge harmonic identity as in the full-threshold result proves
\[
   \boxed{\quad\sum_{d\ge0}\sum_{y\ {\rm positive\ odd}}
          \frac{V_p(M_{d+1,y}-M_{d,y})}{y(3y+1)}<\infty
             \qquad(1<p<\infty).\quad}                               \tag{3}
\]
The far height tail can alternatively be paid by the uniform row bound \(2^{d+2}\) past \(3^{d+2}\). The left side allows the entire disjoint family to be chosen anew at each height and depth. At \(p=1\) the interval norm agrees with total variation on atomic measures: use their finitely many largest one-point atoms and then exhaust. At a fixed target every finite-depth row and its successor have disjoint positive atom sets, by the valuation calculation below. Their total-variation discrepancy is their sum of masses. Consequently (3) at \(p=1\) fails already at the known positive-trace target one, using \(\rho_d(1)\to h(1)>0\).

## The harmonic sum over every target and phase

Use the normalized finite measures \(P_{d,y}=y^{-1}(R\mapsto1-R/y)_*M_{d,y}\). Reflection as well as positive dilation preserves the disjoint-interval norm. Set
\[
 p_d(y)=1_{\{y\le q_d\}}(P_{d+1,y}-P_{d,y}),\qquad
 (Tb)(z)=\sum_{U x=z}w_x(D_{w_x})_*b(x).
\]
The \(V_p\) norms of these normalized rows are \(1_{y\le q_d}n_{p,d}(y)/y\). On the countable sum norm \(\|b\|_{1,p}=\sum_y V_p(b(y))\), \(T\) is a contraction. On an exactly propagated summand the transport multiplies the mass and its complementary mark by the same ordinary survival \(w_x=3x/(3x+1)\). All retained sites land below the next cutoff. Thus
\[
    p_{d+1}=Tp_d+e_d,\qquad \|e_d\|_{1,p}\le 2h_{p,d}.                \tag{4}
\]
For the exterior estimate, sort \(x=r+2q_d j\) with its least positive odd representative \(r\le2q_d\). For \(j=0\), omitted representatives \(r>q_d\) cost at most \(n_{p,d}(r)/q_d\). For \(2^h\le j<2^{h+1}\), landing below \(3q_d\) forces \(2^{v_2(3x+1)}>(3x+1)/(3q_d)>2j\). Thus \(2^{h+2}\mid 3r+1+6q_d j\); this selects at most one \(j\) in that shell, since \(3q_d\) is odd. It costs at most \(n_{p,d}(r)/(2q_d 2^h)\). Summing shells and all representatives proves (4). The identical bound applies to the sum with any positive row seminorm satisfying the same transport. [Original unmarked finite-period propagation, PR195](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md).

For an escaping target use \(s_y=F(y)\); elsewhere put \(s_y=1\). Define the correction \((Sb)(y)=s_y(D_{s_y})_*b(y)\). For each escaping component use the selected ordinary ray \(r_{C,n}\) and the measures \(\Gamma_{C,v}\) defined by (4) of [the all-depth profile](ALL_DEPTH_SPATIAL_PROFILE.md). With \(\Delta\Gamma_{C,v}=\Gamma_{C,v-1}-\Gamma_{C,v}\), one has
\[
 \boxed{\quad
  \sum_{C,v} V_p(\Delta\Gamma_{C,v})<\infty,\qquad
  \left\|Sp_d-
     \sum_{C,v:\,d+v\ge0}\delta_{r_{C,d+v}}\Delta\Gamma_{C,v}
  \right\|_{1,p}\longrightarrow0 .\quad}                             \tag{5}
\]
Here \(\delta_r\) specifies the ordinary target and the second factor is its signed real mark measure. The estimate sums over all heights as well as all possible phase offsets.

Indeed fix a finite input at depth \(j\), supported on finitely many physical sites, whose marked rows are finite signed measures. Every bounded positive orbit enters a finite cycle with primitive product strictly below one, and its propagated norm tends to zero. Every escaping input at \(x\) eventually lands at \(r_{C,d+v}\) with \(v=\mathrm{grade}_C(x)-j\). At all later times its corrected row is exactly \(F(x)(D_{F(x)})_*b(x)\), since \(b_{d-j}(x)F(U^{d-j}x)=F(x)\). Sum these finitely many corrected rows into a finite phase array \(A_j(b)\). It has norm at most \(\|b\|_{1,p}\), and \(A_{j+1}(Tb)=A_j(b)\).

Apply this observation to \(b=p_j\). Iterating (4) gives \(\|p_d-T^{d-j}p_j\|_{1,p}\le t_j=2\sum_{i\ge j}h_{p,i}\), with \(t_j\to0\). The operator \(S\) is contractive. The finite propagation comparison shows that the limsup error in approximating \(Sp_d\) by the moving placement of \(A_j(p_j)\) is at most \(t_j\). At each fixed phase \((C,v)\), the exact all-depth identity (6) and total-variation control there imply that \(Sp_d(r_{C,d+v})\to\Delta\Gamma_{C,v}\) in variation norm. The site is inside \(q_d\) eventually by \(r_n+1\le(3/2)^n(r_0+1)\). Fatou on the countable phase indices now gives \(\|A_j(p_j)-\Delta\Gamma\|_{1,p}\le t_j\). The moving placement is a contraction, as the occupied sites are all distinct. Together these inequalities prove (5) and avoid any completeness assumption on the space of measure-valued rows.

In particular \(\sum_v V_p(\Gamma_{C,v-1}-\Gamma_{C,v})\) is finite even at the backward end approaching the nonzero atomless law \(H_C\eta_C\). In variation norm of measures, the corresponding series diverges at this end of every escaping component: consecutive phase profiles are mutually singular and their masses tend to \(H_C\). The limiting harmonic \(V_p\) norm of \(Sp_d\) is exactly \(\sum_{C,v} V_p(\Delta\Gamma_{C,v})\). It vanishes exactly if there are no escaping components; a positive component has different forward and backward limits. The same scalar norm limit holds before applying \(S\): on each of the finitely many significant placed tails \(s_y\to1\), and \(s_y\ge c_0>0\) uniformly on escaping sites. Scaling alone changes a row norm by the mass factor \(s_y\); no continuity assertion about the moving positions of atoms is required.

## Individual ordinary sources and a quantitative endpoint bound

For an individual inverse word use the notation \(A_w=3^d2^{-S_w}\), \(x_w\) its actual positive odd source. Write
\[
 B_{p,d}(y)=\left(\sum_{w:\ |w|=d,\ w\to y}
              [A_w\rho_1(x_w)]^p\right)^{1/p}.
\]
Every positive word here has a unique atom, even when both adjacent rows are compared: equality of physical complementary marks at a common target gives \(3^d2^{-S}x=3^{d'}2^{-S'}x'\). The positive sources are odd and coprime to three. Two-adic valuations first give \(S=S'\); three-adic valuations give \(d=d'\). Then \(x=x'\), which fixes its whole forward segment. In particular testing (3) on individual disjoint singletons already gives a positive, unsigned, joint all-source bound. There is a sharper direct proof with an explicit dependence on \(p\).

For each real \(p>1\), set \(c_p=(1+2^p)/3\) and \(\lambda_p=3^{p-1}/(2^p-1)\). On either sufficient full ternary period, the exact identity
\[
  \operatorname{mean}_y B_{p,d}(y)^p=c_p\lambda_p^d                 \tag{6}
\]
holds at every depth. For a fixed word its compatible residue class has relative size \(3^{-d}\), and on that class the terminal trit is uniform, giving the factor \(c_p\). The sum of all \(2^{-pS_w}\) over length-\(d\) positive words is \((2^p-1)^{-d}\). Tonelli handles the countable word family. At \(p=2\) the mean second power is exactly \(5/3\) at every depth. For \(1<p<2\), strict concavity of \(\log(2^p-1)-(p-1)\log3\), which vanishes at both endpoints, gives \(\lambda_p<1\). Jensen bounds the mean of \(B_{p,d}\) by \(c_p^{1/p}\lambda_p^{d/p}\).

The positive word norms satisfy the same physical subtransport: the child lists concatenate disjointly at every target, their weights on a branch are multiplied by \(3\,2^{-e}\), and the norm of a concatenation is at most the sum of the norms of its lists. Write \(J_d=\sum_{y\le q_d,\ y\ {\rm odd}}B_{p,d}(y)/y\). The retained one-edge depletion and the exterior estimate in (4) give
\[
 J_{d+1}+\sum_{y\le q_d,\ y\ {\rm odd}}\frac{B_{p,d}(y)}{y(3y+1)}
       \le J_d+2\operatorname{mean}_y B_{p,d}(y).
\]
The full omitted tail costs at most \(q_d^{-1}\operatorname{mean}B_{p,d}\): write \(y=r+2q_d j\) with odd representatives \(1\le r\le2q_d\). The omitted first representatives cost at most \((3q_d^2)^{-1}\) times their period sum; the positive shells \(j\ge1\) cost at most \((12q_d^2j^2)^{-1}\) times that sum. Consequently
\[
 \begin{split}
  \sup_d J_d&\le J_0+2c_p^{1/p}/(1-\lambda_p^{1/p}),\\
  \sum_{d\ge0}\sum_{y\ {\rm positive\ odd}}
              \frac{B_{p,d}(y)}{y(3y+1)}
      &\le J_0+3c_p^{1/p}/(1-\lambda_p^{1/p})
                 \qquad(1<p<2).                                    \tag{7}
 \end{split}
\]
For \(p\ge2\) use monotonicity of the individual list norm and the bound at \(p=3/2\). Since \((\log\lambda_p)'|_{p=1}=-\log(4/3)\), the two bounds in (7) are \(O((p-1)^{-1})\) as \(p\downarrow1\). In ordinary forward terms the integrand on the second line is exactly
\[
 \frac{1}{3y+1}
  \left(\sum_{\substack{x\ {\rm positive\ odd}\\ U^d x=y}}
            [\rho_1(x)b_d(x)/x]^p\right)^{1/p}.                      \tag{8}
\]
Equations (6)–(8) use the original arithmetic, including all cycles; no mixing theorem or assertion of positive basin density is needed.

The order \((p-1)^{-1}\) in the second line is sharp using the fixed-root input \(\rho_{d+1}(1)\to h(1)>0\). At this one terminating target discard physical clocks \(S_w>8d\). Their total row mass is \(O(\xi^d)\), \(\xi=6(3/4)^8<1\), by dropping compatibility and using the geometric exponential moment. The retained total is at least \(h(1)/2\) for all sufficiently large \(d\). It is split among at most \(\binom{8d}{d}\le2^{8d}\) words. Hölder gives \(B_{p,d}(1)\ge [h(1)/2]2^{-8d(1-1/p)}\). Summing in \(d\) proves the lower order. In particular control near the endpoint incurred by known terminating fibres is already of this order.

For the escaping-source consequence, the positive phase profile at \((C,v)\) has individual atom weights \(\rho_1(x)F(x)/x\) at distinct marks \(F(x)\). Consecutive phases have disjoint such sets. The global estimate (5) therefore gives
\[
 \boxed{\quad
  \sum_{C,v}\left(\sum_{\substack{x\in C,\ x\ \mathrm{unit}\\
         \mathrm{grade}_C(x)=v}}x^{-p}\right)^{1/p}<\infty
         \qquad(1<p<\infty).\quad}                                  \tag{9}
\]
Here \(\rho_1(x)\ge1\) and \(F(x)\ge c_0\) on the indicated sources. In particular the reciprocals of the least unit representative of every nonempty phase are summable over *all* escaping components and their integer phases. A quantitative proof uses only (7) and the all-depth formula: the corrected finite-row atom norm on \(r_{C,d+v}\) tends at each fixed phase to the atom norm of \(\Gamma_{C,v}\), by its total-variation approximation and the triangle inequality for atomic norms. Fatou over those distinct sites yields an upper bound \(c_0^{-1}\sup_d J_d\) for (9). The right side is \(O((p-1)^{-1})\) near one.

At \(p=1\), (9) fails whenever an escaping component exists. On each such component \(\Gamma_{C,v}([0,1])\to H_C>0\) as \(v\to-\infty\), and \(\rho_1(x)F(x)\le2\). Thus the sum of reciprocals over its unit representatives in all these phases diverges. This proves the endpoint failure even without an additional density comparison. Establishing a bound uniform as \(p\downarrow1\) for (9) would exclude all positive escape; estimate (7) does not supply it.

[The exact checker](check_variation_profile.py) independently propagates full rational period power sums at \(p=1,2,3\) through grade four, including all physical clocks by an exact geometric tail per compatible residue. It also checks 4,433 finite-source atoms and 1,528 occupied adjacent-grade pairs by forward iteration. The normal and optimized interpreter modes reproduce the [same receipt](../../../reports/astra-global-20261128/escape/VARIATION_PROFILE_CHECKS.json).
