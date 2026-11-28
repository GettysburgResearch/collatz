# Strong Lebesgue differentiation at prescribed positive integers

Let \(\rho\) be the original fair ternary Syracuse density with respect to full ternary Haar \(m_3\). For a positive odd integer \(y\), let \(h(y)=\lim_n\rho_n(y)\) be its canonical ordinary-depth trace. The means on balls about \(y\) thus converge; this alone says nothing about absolute oscillation on those balls. Here the whole restricted density satisfies
\[
      \left\|\rho(y+3^n\,\cdot)-h(y)\right\|_{L^p(m_3)}
                        \longrightarrow0,\qquad 1\le p<2.            \tag{1}
\]
At every positive unit \(y\), the local second moment is infinite on every ball \(y+3^n\mathbb Z_3\), so strong second-moment differentiation fails. At nonunits the density and the trace on their first-trit cylinder are zero. A hypothetical ordinary escape has a moving transition for this stronger form of differentiation, including a nonvanishing oscillation at each fixed distance from its reference grade.

The subcritical differentiation itself also has a shorter route from an existing source. Valbuena's lower semicontinuous stationary representative agrees with \(h(y)\) at each positive odd integer. Thus on small enough balls the density is almost everywhere at least \(h(y)-\epsilon\). Its mean tends to \(h(y)\) by Weaver 176, so its absolute deviation tends to zero in \(L^1\). The uniform local weak-square bound from the word expansion below gives every \(p<2\) by interpolation. The joint source and clock proof additionally retains the affine isometry needed for the [critical weak-square endpoint](ORDINARY_WEAK_SQUARE_DIFFERENTIATION.md). [Valbuena, “The stationary density,” pinned stationary envelope](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex) · [PR213's pinned comparison and capped ordinary trace](https://github.com/GettysburgResearch/collatz/blob/b710ae3c0bf5c764b8ee575c7c2898156d5f7451/research/astra-global-rigidity-20261128/mass/POWER_CAPPED_ORDINARY_TRACE.md)

## Retaining the clock with the source residue

Use \(B=(1+2\mathbb Z_2)\times\mathbb Z_3\) and \(m=m_2\otimes m_3\), with odd binary Haar. We use the fixed ordinary target ancestor theorem on this base: at depth \(n\) and target \(y\), the measure assigning true source \(x\) weight \(A_w=3^n/2^{S_w}\) converges weakly to \(h(y)m\). Here \(S_w\) is its physical division total. The base forward map \(S\), taking its gap from the binary coordinate and acting with that gap in both coordinates, is exact under \(\pi=m_2\otimes(\rho m_3)\). The cited argument proves triviality of its tail and \(S_*m\ll\pi\). [Original binary–ternary ancestor theorem, PR193](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-diagonal-20261127/escape/FIRST_POWER_HAAR.md) · [Base exactness, adjoint formula and stationary iid representation, checkpoint one](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/machinery/PROFINITE_ANCESTORS.md) · [Ordinary-depth input, Weaver 176, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1)

For every fixed \(M\ge1\) the joint source and \(S_w\bmod M\) converge to \(h(y)m\otimes u_M\), with the uniform law \(u_M\) on \(\mathbb Z/M\mathbb Z\). To prove this, add a forward clock coordinate \(c\mapsto c+e\), where \(e=v_2(3x+1)\) is the binary-coordinate gap. Its transfer on tests uses the same inverse weights \(3/2^e\), legal ternary branches \(F_e^{-1}\), and \(c\mapsto c-e\). Call it \(L_M\) and the forward map \(S_M\). The change-of-variables identity is
\[
 \int a L_M f\,d(m\otimes u_M)=\int (a\circ S_M) f\,d(m\otimes u_M).
\]
The inverse clock at endpoint zero reads \(-S_w\), which has the same eventual uniform law. The test transfer maps continuous functions into continuous functions, because each fixed branch uses a clopen domain and the coefficient tails are summable.

The stationary probability \(\pi\otimes u_M\) is mixing for \(S_M\). Use a two-sided iid fair geometric gap sequence and an independent uniform clock at time zero. Moving forward shifts the gaps, adds their current value to the clock and applies \(S\) to the binary future and ternary past coordinates represented by those gaps. The finite clock walk has all transition probabilities positive because each residue is represented by a positive gap. Thus its \(n\)-step matrix tends to the uniform matrix. Two cylinder tests of the clock and gaps separated by a long uncovered interval decorrelate by summing over the boundary clock states of that interval. Cylinder approximation yields mixing of this process and hence of its factor \(S_M\).

For a tail-event indicator, take compatible representatives \(f_j=f_{j+1}\circ S_M\) almost everywhere for the invariant probability (equivalently take the binary pullbacks of one event at all future times). Averaging \(f_j\) over the finite clock gives \(b_j=b_{j+1}\circ S\). The level sets of \(b_0\) lie in the trivial base tail, so \(b_0\) is a constant multiple of \(1/M\). Thus all tail-event probabilities are multiples of \(1/M\); the tail probability algebra has at most \(M\) atoms. Pullback permutes these finitely many atoms modulo null sets by measure preservation. An atom of mass \(a\) recurring along multiples of a period satisfies \(a=a^2\) by mixing. The lifted tail is trivial.

From any subsequence of the fixed-root measures obtain by compactness joint weak limits at every translated depth \(n-j\), \(j\in\mathbb Z\), giving measures \(\nu_j=L_M^*\nu_{j+1}\). Their base projections are \(h(y)m\) by the unmarked ordinary theorem. The finite extra fibre gives densities \(r_j\le M h(y)\) with respect to \(m\otimes u_M\). The adjoint identity gives \(r_j=r_{j+1}\circ S_M\) almost everywhere for \(m\otimes u_M\), hence also for \(\pi\otimes u_M\). All level sets are tail events under the latter, so each \(r_j\) is constant there; the constants agree by invariance and coherence. The uniform unit floor makes this equality valid \(m\)-almost everywhere on the unit part. Since \(S_*m\ll\pi\), another application of the recursion extends it to all \(m\otimes u_M\). Each constant is \(h(y)\) by the total mass. Every subsequence yields this same limiting measure, proving the claimed fixed-root joint convergence. In particular the source ternary residue is uniform even conditional on each fixed clock class.

## The local field

For ternary Haar \(\zeta\), stationarity and the exact positive inverse words give, almost everywhere in \(\zeta\),
\[
        \rho(y+3^n\zeta)
             =\sum_{U^nx=y} A_w\,\rho(x+2^{S_w}\zeta).               \tag{2}
\]
Indeed shifting the root by \(3^n\zeta\) preserves the depth-\(n\) legal words, and the inverse slope is \(2^{S_w}/3^n\). Affine changes here are nonsingular; the countable positive sum presents no representative ambiguity for this integral identity. Its weights sum to \(\rho_n(y)\).

For a test \(\phi\) constant modulo \(3^k\), take \(M=\operatorname{ord}_{3^k}(2)\) (the constant test needs no clock). The preceding joint convergence makes the analogue of the right side of (2) with \(\phi\) tend to \(h(y)\int\phi\,dm_3\), uniformly in \(\zeta\), since there are only finitely many \(\zeta\bmod3^k\). Indeed for every specified clock the first coordinate \(x\) is uniform on this finite ring. For \(1\le p<2\), \(\rho\in L^p(m_3)\) by the cited density regularity. Replacing \(\rho\) by \(\phi\) inside (2) costs at most \(\rho_n(y)\|\rho-\phi\|_p\) by Minkowski and the fact that each \(x+2^{S_w}\zeta\) has Haar law. Approximation by finite-cylinder tests proves (1), since \(\rho_n(y)\to h(y)\). [Weaver 146, exact critical tail and subcritical moments](https://rstation.ai/problems/collatz/papers/146/v1)

At a unit \(y\) every depth-\(n\) ball meeting \(y\) has infinite local second moment. For a direct proof, choose a legal depth-\(n\) word to that ball, which exists by the unit atom floor. Its full image is that ball. The positive transfer lower bound \(\rho(F_w z)\ge A_w\rho(z)\) almost everywhere and \(\int\rho^2dm_3=\infty\) imply the assertion by integration. Subtracting the finite \(h(y)\) does not restore a second moment.

## The moving transition on a true escaping ray

Normalize an escaping component's odd grade so \(y_j=U^j y_0\) has grade \(j\), and write \(H_C=\lim h(y_j)F(y_j)/y_j>0\). Along a simple ray \(F(y_j)\to1\), so \(h(y_j)/y_j\to H_C\). Use \(n=j+k\ge0\) in the following limits, and \(j\to\infty\). For every \(1\le p<2\),
\[
\begin{array}{ll}
 k\to-\infty:&\displaystyle
 \|\rho(y_j+3^{j+k}\,\cdot)/h(y_j)\|_p\longrightarrow0,\\[3pt]
 k\to+\infty:&\displaystyle
 \|\rho(y_j+3^{j+k}\,\cdot)/h(y_j)-1\|_p\longrightarrow0,\\[3pt]
 k\in\mathbb Z\ \text{fixed}:&\displaystyle
 \liminf_j\|\rho(y_j+3^{j+k}\,\cdot)/h(y_j)-1\|_p>0 .
\end{array}                                                        \tag{3}
\]
Thus even at exact ordinary positive points, qualitative fixed-root differentiation cannot be substituted at every moving precision.

For the first regime, the conserved grade masses \(m_x=F(x)h(x)/x\) have total \(H_C\) and concentrate at the main \(y_v\) as the grade \(v\to+\infty\), by the elementary derivation in [the ordinary energy note](ORDINARY_COLLISION_ENERGY.md). Among units on grade \(v\), \(\sum F(x)/x\to0\): use \(h\ge\alpha\) on all ordinary units, the vanishing off-ray \(m\)-mass and \(h(y_v)\to\infty\). A nonunit \(x\) maps to a unit \(u\) one grade later, and \(F(x)/x=a_e F(u)/u\) on its actual gap \(e\); all such incoming \(a_e\) sum to at most three at each \(u\). This gives the same zero limit when including the nonunits. At depth \(n=j+k\) every source for \(y_j\) has grade \(v=-k\), and \(W_n(x)=F(x)/F(y_j)\). Hence \(\rho_n(y_j)/y_j\to0\). Minkowski in (2) bounds the unnormalized field norm by \(\rho_n(y_j)\|\rho\|_p\), proving the claim.

For the second regime fix a late unit \(y_l\) on the ray. Split (2) after \(j-l\) letters. Its true branch from \(y_l\) has coefficient \(a\), and by harmonicity the total of \(A_w h(x)\) on all other sources \(x\) at this depth equals \(h(y_j)-a h(y_l)\). Uniformly for ordinary \(x,r\ge1\), fixed-root contraction in (2) gives
\[
   \|\rho(x+3^r\,\cdot)\|_p\le\rho_r(x)\|\rho\|_p\le C h(x)\|\rho\|_p.
\]
The last inequality has a pointwise ordinary proof: at finite depth \(\rho_1\le(2/\alpha)\rho_m\) for all \(m\ge1\) by the uniform unit floor, then apply \(L^{r-1}\) and let \(m\to\infty\) at the specified ordinary target. This argument also treats the nonunit leaves. Thus the entire remaining \(L^p\) error on the sibling branches, including their subtracted stationary masses, is at most \(C_p[h(y_j)-a h(y_l)]\). The principal branch error relative to \(a h(y_l)\) tends to zero for fixed \(l\) as \(l+k\to\infty\) by (1); its unit dilation of \(\zeta\) leaves the norm invariant. Finally \(a h(y_l)/h(y_j)=m_{y_l}/m_{y_j}\to m_{y_l}/H_C\), which tends to one with \(l\). This proves the high-precision regime.

For fixed \(k\), take a fixed \(l\) with \(l+k\ge1\) and \(y_l\) a unit. The exact principal branch alone bounds the normalized density below by \((a/h(y_j))\rho(y_l+3^{l+k}2^{S_w}\zeta)\). Its coefficient tends to \(m_{y_l}/(H_C h(y_l))>0\). The displayed local \(\rho\) has the same law for every \(j\) and has unbounded essential supremum by its infinite second moment. It therefore exceeds an arbitrarily large fixed constant on a fixed positive measure. The other branches are nonnegative, proving the positive lower oscillation in (3).

The simultaneous ordinary spatial comparison from PR213 samples unit targets uniformly in a proportional positive interval. It gives convergence in probability and all log moments of the actual predecessor density scale divided by the finite original row at \(\lfloor\log_3 y\rfloor\). On a specified escaping ray, \(\lfloor\log_3 y_j\rfloor\le (\log_3(3/2))j+O_{y_0}(1)\), so this physical precision lies strictly behind the front in (3), where \(\rho_{\lfloor\log_3 y_j\rfloor}(y_j)/h(y_j)\to0\). This identifies the different quantifiers without imposing a rate on any prescribed target. [PR213, critical ordinary ternary share, pin 2c871ba1](https://github.com/GettysburgResearch/collatz/blob/2c871ba103c62603709a9af63099387738f31311/research/astra-global-rigidity-20261128/mass/ORDINARY_CRITICAL_TERNARY_SHARE.md)
