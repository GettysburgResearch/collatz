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
