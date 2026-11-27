# Translation of whole ordinary predecessor measures

**Status.** Written consequences of [the marked trace](MARKED_TRACE.md), the source-qualified finite-clock coalescence bound, and the marked source formulation of the uniform first-entry profile in PR193. The conclusions retain arbitrary tests on ordinary sources.

Fix a positive odd unit \(z\). On the set \(\mathbb Z_{\rm odd}\) of signed odd integers define
\[
 m_{p,z}(v)=3^p2^{-D_p(v)}\,\mathbf1_{\{v>0,\ S^p v=z\}},
\]
taking it to be zero whenever the indicator vanishes. Fix \(r\ge0\), \(b\in\mathbb Z\) and \(A(v)=3^r v+2b\). Then
\[
 \lim_{p\to\infty}
   \sum_{v\in\mathbb Z_{\rm odd}}
       \left|m_{p,z}(v)-3^r m_{p-r,z}(A(v))\right|=0.             \tag{1}
\]
The second mass samples one of the \(3^r\) progressions of odd integers. In particular every fixed even translation acts asymptotically as the identity in the ordinary \(\ell^1\) norm. The full finite mass tends to \(h(z)>0\), so this also applies to the normalized probability. Individual components need not coincide.

To see (1), take \(L=\lfloor\log(2+p-r)\rfloor\) and fix the dyadic residue test \(B_L\) that the affine germs starting at \(v,A(v)\) fail to coalesce through \(L\) shortcut clocks. On a successful test from a positive pair, write \(i,j\) for their odd counts to the common clock. Equality of slopes on the cylinder gives \(3^i=3^r3^j\), so \(i=j+r\). After that clock the two ordinary paths are identical. For \(p-r\ge L\), if either of the two masses is positive, its terminal odd state occurs at a clock at least \(L\). The other path reaches \(z\) at exactly that clock with the required other odd count. Since both start odd and end odd, the traveled clocks are their full Syracuse totals. The two summands in (1) therefore coincide *exactly* on successful positive pairs.

Under odd Haar probability, \(B_L\) has probability \(O_{r,b}(L^{-1/2})\) by [PR146's all-initial-state bound](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md). The law of the first \(L\) gaps detects the first \(L\) dyadic bits. Thus [the marked trace](MARKED_TRACE.md) bounds the \(m_{p,z}\) mass of bad \(v\) by \(o_{z,r,b}(1)\). For the other term put \(w=A(v)\). On the odd dyadics \(w\mapsto(w-2b)/3^r\) is an affine measure-preserving bijection, so \(A(B_L)\) is also a length-\(L\) residue test of the same Haar probability. Enlarge the ordinary sum over \(w\equiv2b\bmod3^r\) to every odd \(w\). The marked trace for \(m_{p-r,z}\) again bounds the remaining bad mass by \(o_{z,r,b}(1)\), including the fixed factor \(3^r\). Only a finite set of signed sources has opposite positivity on the two sides. At each fixed positive \(v\), \(m_{p,z}(v)\to0\): a nonperiodic \(z\) occurs at most once, and repeated visits to periodic \(z\) include arbitrarily many laps with multiplier strictly below one. This removes the endpoints and proves (1).

For \(r=1\), the choices \(b=-1,0,1\) partition the odd integers into three images. If \(\mathcal A\) sends mass at \(v\) equally to \(3v-2,3v,3v+2\), equation (1) gives
\[
               \|m_{p-1,z}-\mathcal A m_{p,z}\|_1\to0.            \tag{2}
\]
Thus the approximation holds for all bounded ordinary source tests, including basin labels and arbitrarily irregular source-height restrictions. It need not accumulate with bounded error over a growing number of changes of grade.

## A particular escaping component, including moving targets

Suppose a fixed ordinary odd unit \(a_0\) escapes, and write \(a_n=S^n a_0\). Give its component its ordinary integer grade \(g(x)=i-t\) whenever \(S^t x=a_i\). Let \(P\) be the positive corrected height satisfying \(P(Sx)=3\,2^{-e(x)}P(x)\). Define the whole physical grade measure
\[
 \eta_j(v)=\mathbf1_{\{v>0,\ g(v)=j\}}/P(v)
\]
on signed odd integers, extended by zero outside this component. Its total \(Z_j\) tends to a positive \(H\) as \(j\to-\infty\), and to zero as \(j\to+\infty\). For all \(k,n\ge0\), the nonnegative discrepancy satisfies
\[
 0\le \eta_{n-k}-\frac{m_{k,a_n}}{P(a_n)},\qquad
 \left\|\eta_{n-k}-\frac{m_{k,a_n}}{P(a_n)}\right\|_1\le \epsilon_n\to0,
                                                                    \tag{3}
\]
uniformly in \(k\). The measure inequality follows term by term from the corrected-height cocycle. Its mass bound is exactly PR193's uniform first-entry estimate (3); taking the absolute value sum costs nothing because the omitted sources have one sign. [PR193, trace profile](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/TRACE_PROFILE.md)

For every fixed \(C\), the pushforward of \(\eta_j\) by the earliest \(L\le C\log(2+|j|)\) forward gaps converges in total variation to \(H P_L\) as \(j\to-\infty\), uniformly over these lengths. Fix \(n\), use (3) with \(k=n-j\), apply the fixed-target marked result at \(a_n\), and use \(|h(a_n)/P(a_n)-H|\le\epsilon_n\). The limsup is at most \(2\epsilon_n\); now send \(n\to\infty\). Consequently the physical posterior at the *moving target* \(a_n\), with normalization \(m_{k,a_n}/\|m_{k,a_n}\|_1\), has these Haar-distributed initial marks whenever \(n\to\infty\) and \(k-n\to+\infty\), with \(L\le C\log(2+k-n)\). At the actual depth \(k=n\) the posterior instead converges in ordinary total variation to the atomic law \(\eta_0/Z_0\) and retains positive mass at \(a_0\). The two different limit regimes use the same actual component. [PR193, own-word posterior](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/POSTERIOR.md)

With Paper 48's stronger input, the same proof gives the linear mark range \(L\le\lambda_*|j|\) for negative whole grades and \(L\le\lambda_*(k-n)\) for the posterior past onset, where \(\lambda_*\) is fixed in [the linear-horizon proof](MARKED_TRACE.md). For fixed \(n\) the available depth \(n-j\) exceeds \(|j|\), so the approximation does not change the chosen absolute fraction. These estimates transfer the untilted source law, whose shortcut parity after the fixed initial odd bit is fair.

The full translation and dilation conclusions also survive the first-entry comparison:
\[
 \lim_{j\to-\infty}
 \sum_{v\in\mathbb Z_{\rm odd}}
     |\eta_j(v)-3^r\eta_{j+r}(3^r v+2b)|=0,
 \qquad \|\eta_{j+1}-\mathcal A\eta_j\|_1\to0.                    \tag{4}
\]
Indeed apply (3) at the same \(n\) with the two depths \(k=n-j\) and \(k-r\). The approximation error on the progression is at most \((1+3^r)\epsilon_n\), independently of \(j\). Then use (1) and let \(n\) increase. This proves physical translation invariance arbitrarily far in the past grades of the hypothesized *specific* component. The grade-zero atom and its original positive source are both retained in (3).

There is a necessary cumulative loss in (4). Write \(E_j=\|\eta_{j+1}-\mathcal A\eta_j\|_1\). The pushforward \(\mathcal A\) is an \(\ell^1\) contraction. Its descendants of an odd positive \(v\ge3\) after \(r\) dilations have minimum \(3^r(v-1)+1\). The component excludes \(1\), so every \(\eta_j\) has this property. For any fixed \(J\),
\[
 \sum_{j=J-r}^{J-1} E_j\ \ge\
       \|\eta_J-\mathcal A^r\eta_{J-r}\|_1
                  \ \longrightarrow\ Z_J+H \quad (r\to\infty).   \tag{5}
\]
The limit follows by testing on an increasing finite interval carrying arbitrarily nearly all \(\eta_J\), disjoint for large \(r\) from the pushed support. In particular the \(E_j\)'s are nonsummable at negative infinity. Otherwise take \(J\to-\infty\) in the inequality \(\sum_{j<J}E_j\ge Z_J+H\) to obtain a contradiction. Escape therefore forces vanishing one-step errors with infinite cumulative mass on the original component. Positive near-agreement of individual layers gives no summable bound.

## Growing physical translations along the specified inverse layer

At equal formal count, use Leen's stronger large-displacement fair synchronization bound \(O(\sqrt{(1+\log(1+|b|))/(1+H)})\) at clock \(H\), recalled in [Weaver, Paper 13, equation (1)](https://rstation.ai/problems/collatz/papers/13). This pre-existing uniform estimate and the positive linear marked horizon in [Marked trace](MARKED_TRACE.md) extend the source-translation assertion. For each fixed odd unit \(z\), writing \(\tau_b v=v+2b\),
\[
 \sup_{\log(2+|b|)=o(p)}\|m_{p,z}-(\tau_b)_*m_{p,z}\|_1=o_z(1).      \tag{10}
\]
Here the supremum is over any prescribed deterministic range \(\log(2+|b|)\le B_p\) with \(B_p=o(p)\). For a fixed sufficiently small \(\theta>0\), the limsup at \(B_p=\theta p\) is \(O_z(\sqrt\theta)\), uniformly as \(\theta\downarrow0\). An analogous statement holds for the escaping-component grades \(\eta_j\) at \(p=|j|\): the error tends to zero throughout the \(o(|j|)\) range. In the fixed-\(\theta\) version its double limit, first \(j\to-\infty\) then \(\theta\downarrow0\), is zero.

Indeed at \(H=\lfloor\lambda_*p\rfloor\), the bad data for \(v,v+2b\) form a residue test of Haar probability \(O(\sqrt{(1+\log(1+|b|))/p})\). The translated bad set is another test at the same precision and Haar probability. The marked theorem at \(z\) controls uniformly the masses of both tests; on the complement equality of actual terminal counts and clocks gives exactly equal weights where both sources are positive. Unequal positivity requires the positive source to have size \(O(1+|b|)\). Its layer mass is \(o_z(1)\) for \(B_p=o(p)\) or for sufficiently small fixed \(\theta\), by the positive central-source-window comparison in the marked proof: outside the central \(\log v\) block about \(Dp\) the entire fixed-\(z\) mass tends to zero. For the component grade use the positive same-target comparison (3) above, translating signed-integer measures isometrically, first with the ray index fixed and then increasing it. No sum over the growing set of shifts is taken; (10) is uniform for each shift, and hence also permits an independent average of them.

For context the affine-rank fair estimate can also be seen directly from Leen's normalized-carry bound. With \(Y=3^rX+b\), burn in \(t\asymp1+\log(2+|b|/3^r)\) shortcut steps, using a large enough constant. The signed rank is \(d=r+K_Y-K_X\), where the two count marginals are \(\mathrm{Bin}(t,1/2)\), so \(\mathbb E|d|\le r+O(\sqrt t)\). Write \(C_X,C_Y\) for the affine offsets at this time. After canonical reorientation the absolute normalized carry is at most
\[
          (|b|/3^r)\,3^{K_X}2^{-t}+C_X+C_Y .
\]
For \(d\ge0\) divide the upper-minus-scaled-lower difference by \(3^d\). For \(d<0\) use the difference \(3^dX_t-Y_t\) and \(K_Y<K_X-r\). For each fixed \(0<s<1\), \(\rho=2^{-s}(1+3^s)/2<1\). Each individual \(s\)-moment of the affine offset is bounded by summing the geometric series in \(\rho\) over its past step increments; independence is only needed within that single marginal word. The \(s\)-moment of its bare multiplier is \(\rho^t\), so the chosen deterministic burn-in makes the expected normalized carry \(s\)-moment bounded. For \(H\ge2t\), condition on the full dyadic prefix: the remaining base coordinate is Haar by its odd affine slope in the fresh binary tail, including if orientation was reversed. The imported remaining-time bound then gives \(O((1+r+\sqrt{\log(2+|b|/3^r)})/\sqrt H)\); for shorter horizons this or the trivial bound suffices with an enlarged constant. This explains the logarithmic offset scale. The equal-rank rate itself is credited above. [Weaver, Paper 19, equation (7), quoting Leen's remaining-time theorem](https://rstation.ai/problems/collatz/papers/19)

At a fixed escaping root the typical source height on an inverse grade is exponential in its absolute grade with a *positive fixed* rate \(D\). Equation (10) controls shifts with smaller logarithmic order; it does not give vanishing discrepancy at a shift comparable with that entire physical source height.
