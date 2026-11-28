# Reciprocal mass on the complete signed clock rows

Fix a reference in every escaping ordinary shortcut component, and write
\(D_C(n)=(s,p)\in\mathbb Z^2\) for its physical and odd-count differences to a common meeting. With the signs of the [clock quotient](../phase5/SMOOTH_SOURCE_CLOCK_GROUPS.md), each reverse edge adds \((1,0)\) or \((1,1)\). Let
\[
 A_C(s,p)=\sum_{n\in C:\ D_C(n)=(s,p)}\frac1n,
 \qquad b_j(k)=2^{-j}\binom jk
\]
with binomial weights zero outside \(0\le k\le j\). Then there are real coefficients \(R_C(s,p)\), absolutely summable jointly in the component and both integer coordinates, with exact formulas
\[
 \begin{split}
 R_C(s,p)&=\sum_{\substack{y\in C\\D_C(y)=(s-1,p-1)}}
     \left(\frac{3\mathbf1_{y=2\bmod3}}{2y-1}-\frac1{2y}\right),\\
 A_C(s,p)&=\sum_{j\ge0}\sum_k b_j(k)R_C(s-j,p-k),\qquad
 \sum_{s,p}R_C(s,p)=\kappa d_C,\qquad \kappa=\tfrac12\log(4/3).
 \end{split}                                                        \tag{1}
\]
Here \(d_C\) is ordinary source density. The first sum defining each coefficient has finitely many terms: all its sources have the same corrected height \(P(y)=P(a_C)2^{s-1}3^{1-p}\ge y\). Absolute summability in (1) is *after* collecting the displayed fibres. It implies the joint unrestricted reciprocal limit
\[
 \lim_{s\to+\infty}\sum_{C,p}|A_C(s,p)-\kappa d_C b_s(p)|=0,
 \qquad \lim_{s\to-\infty}\sum_{C,p} A_C(s,p)=0.                    \tag{2}
\]
These are signed comparison levels. All positive starts in the indicated component and level are included, without a height cutoff or a choice of predecessor subtree. The only specific analytic input is the signed original-trit theorem for the marked true endpoint.

## The complete boundary source

Let \(V(x,C,s,p)=e^{-x}\#\{n\le e^x:n\in C,D_C(n)=(s,p)\}\). Write \(a=\log2,L=\log3,b=L-a\). Both vectors below run over all escaping components and both signed integers. The exact physical split gives
\[
 V(x,C,s,p)=
 \tfrac12 V(x-a,C,s-1,p)+\tfrac12 V(x+b,C,s-1,p-1)+r(x,C,s,p).
                                                                    \tag{3}
\]
The even summand is exact. The odd image uses the indicator of residue two modulo three, the cutoff \((3e^x+1)/2\), and an ideal comparison with one third of the whole cutoff at \(3e^x/2\). The sum norm of their difference after dividing by \(e^x\) satisfies
\[
  \|r(x)\|_1\ll_B(1+x)^{-B}\quad(x\ge0),\qquad r(x)=0\quad(x<-b).
\]
Indeed for any future time \(t\) the entire class of an escaping \(n\) is reconstructed from \((F_t(n),T^tn)\) by adding \((t,F_t(n))\) to the terminal signed class. Drop other endpoints. Apply the [signed input (3)](../phase2/NATIVE_BINOMIAL_TRANSFER.md), let \(t\) increase without bound, and add the single physical cutoff error. In particular \(\int\|r(x)\|_1dx<\infty\). Set \(R_C(s,p)=\int r(x,C,s,p)dx\). Integrating each physical indicator from its true initial cutoff gives the first formula of (1). For the sum within a component, (3) with the unmarked component indicator is the scalar boundary equation (8) of [the native Mellin theorem](../phase5/NATIVE_MELLIN_RIGIDITY.md), with \(\tau=0\). Its integrated forcing is \(\kappa d_C\).

Iterate (3) for a finite number of steps. The final term tends to zero at fixed \(x\): its absolute value is bounded by the probability that the fair size walk has not ended below zero at the final date, which tends to zero by its strictly negative drift. The absolute sum of the residual terms is finite pointwise by the uniform unit-strip occupation bound and the displayed decay. For fixed \(s\), summing the integrated absolute residual terms over \(C,p,j,k\) costs at most \(\int\|r(x)\|_1dx\), since the shifts in \(x\) preserve integrals, the weights sum to one in \(k\), and the residual time levels \(s-j\) are all distinct. Tonelli on \(V\) gives \(\int V(x,C,s,p)dx=A_C(s,p)\), proving (1). The norm of a binomial row shifted by any fixed integer in space and any fixed integer in time differs from the unshifted row by \(o(1)\) in sum norm. This follows from the adjacent-space identity \(\|b_j(\cdot-1)-b_j\|_1=2\max_k b_j(k)\) and the one-step time recursion. Apply this to a finite subset of the absolutely summable coefficients, then take the complementary mass to zero. In the other direction only residual levels at most \(s\) can contribute. These observations prove (2).

## The cross section at the same row

The same proof retains the real coordinate without a restriction on the modulus. Set
\[
 W_{C,s,p}(u)=V(u+sa-pL,C,s,p),\quad
 e_{C,s,p}(u)=r(u+sa-pL,C,s,p),\quad
 g_C(u)=\sum_{s,p} e_{C,s,p}(u).
\]
All series defining \(g_C\) converge in \(L^1(du)\) jointly across components. In (3) the indicated shifts align the same \(u\) **exactly**: the two inputs become \(W_{C,s-1,p}(u)\) and \(W_{C,s-1,p-1}(u)\). Therefore
\[
 \sum_{C,p}\|W_{C,s,p}- b_s(p)g_C\|_{L^1(du)}\longrightarrow0.       \tag{4}
\]
The proof just given applies verbatim with integrable functions as coefficients. The profiles are nonnegative almost everywhere by (4), and \(\int g_C=\kappa d_C\). Thus this heat limit incorporates arbitrary real aggregate shapes and allows a nonzero escape amplitude.

For greater precision, distributional differentiation gives
\[
 (1+\partial_u)W_{C,s,p}
  =\sum_{D_C(n)=(s,p)}n^{-1}\delta_{\log n-sa+pL}.
\]
Every atom lies in a fixed compact interval depending on the component reference: the coordinate equals \(\log P(a_C)-\log(P(n)/n)\), and the correction factor has an absolute upper bound on every simple trajectory. Summing the last formula in \(p\), (4) shows that \((1+\partial_u)g_C\) is a positive finite measure on that compact interval, of total mass \(\kappa d_C\). For example, a compactly supported smooth test identically one on this interval computes the mass in the limit from (2). These statements do not assert convergence in total variation for the differentiated, atomic finite rows.

Earlier work identifies the corrected-height fibres and the asymptotic backward law with a stationary odd-path weight at a fixed root. Equation (4) uses reciprocal weight on every original shortcut source in a full signed physical-clock level. The recent Green and moving-root energy results study distinct weighted operators and conditional real fibres. [PR195, corrected classes and backward law](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md) · [PR213, moving-root macroscopic energy](https://github.com/GettysburgResearch/collatz/blob/ca48af42546268771e34297872783631f61e8f02/research/astra-global-rigidity-20261128/mass/MACROSCOPIC_REAL_ENERGY.md)
