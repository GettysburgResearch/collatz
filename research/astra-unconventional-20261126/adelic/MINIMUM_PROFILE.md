# Exact highest shortcut grades throughout an escaping component

Use the positive ordinary component, integer grades \(l,h\), height \(L\) and rational coordinate \(\eta\) from [the pointed spectrum theorem](POINTED_SPECTRUM.md). All assertions in the first two sections use actual positive vertices of this same component.

## The complete high-level floor and a bounded increment sequence

Let \(m_j=\min\{z:l(z)\ge j\}\) over all positive odd sites in the component. This finite minimum exists since \(q_j\) belongs to the set for \(j\ge0\). The sequence is nondecreasing and tends to infinity, since each of the finitely many ordinary integers at most \(B\) has at most one odd-time level. Every future site of any \(z\) with \(l(z)\ge j\) is again in this truncated component. The reciprocal bound therefore gives, uniformly across all these sites,
\[
       0\le\log D(z)\le C m_j^{-\delta},\qquad
       |\log_2 z-l(z)\log_23-\log_2 L+h(z)|\le C' m_j^{-\delta}.  \tag{1}
\]
This keeps the ordinary value, both grades and the decay of the error simultaneous on all the indicated rays.

For each integer \(j\ge0\), define \(b_j=\max\{h(z):l(z)=j,\ 3\nmid z\}\). The set contains \(q_j\), and \(\eta(z)<L\) bounds \(h(z)\) above since \(z\ge1\). The maximum is attained. At every \(j\),
\[
                            1\le b_{j+1}-b_j\le4.                  \tag{2}
\]
For the lower bound follow a maximizing unit at level \(j\) forward for one genuine edge. For the upper bound take a maximizing unit at level \(j+1\) and any unit inverse at cost at most four, which exists by the six-element power cycle modulo nine. More generally,
\[
 b_j=\max_{\substack{l(y)=j+k\\3\nmid y}}\{h(y)-C_k(y)\},\qquad
                     b_{j+k}-b_j\le W_k,                            \tag{3}
\]
where \(C_k(y)\) is its least unit-ended inverse cost and \(W_k=\max_y C_k(y)\). Every unit source at level \(j\) goes forward \(k\) edges to an eligible \(y\), and a least-cost path at this \(y\) really realizes the displayed grade. Conversely every such least-cost path remains in the same component. The inequality follows by taking a maximizing \(y\) at level \(j+k\). In particular the limsup over lengths of the maximal block means of the bounded integer increments in (2) is at most \(\tau=\lim W_k/k\). [Minimum-cost definition and subadditive limit](MOMENT_LATTICE.md)

For all sufficiently high levels the smallest unit at a given exact level has grade \(b_j\). Indeed the common scale at grade \(h\) is \(L3^j2^{-h}\), and (1) puts the positive ordinary sources in a multiplicative interval of width ratio less than two. The bin at the next lower shortcut grade begins above the whole present bin. If the supplied ray is critical, \(A_j/j\to\alpha=\log_23\), then
\[
          b_j/j\to\alpha,\qquad \alpha j-b_j\longrightarrow+\infty .
\]
We have \(A_j\le b_j\le\alpha j+\log_2 L-\log_2 m_j\), proving both statements. The increments in (2) describe distinct maximizers at successive levels; a single path simultaneously realizing them all is an additional requirement.

## A whole future and an expanding number of backward tests at nearly minimal height

Under criticality, \(m_j\le q_j=\exp(o(j))\). For every fixed \(R\ge1\) and \(\epsilon>0\), there are arbitrarily high indices \(j\) with \(m_{j+R}\le(1+\epsilon)m_j\). Otherwise repeated shifts by \(R\) would force exponential growth. Choose a site \(z\) attaining \(m_{j+R}\), so \(l(z)\ge j+R\). Every site \(w\) in its entire coalescing component with \(l(w)\ge l(z)-R\) satisfies
\[
                          w\ge z/(1+\epsilon).                      \tag{4}
\]
In particular this holds for the endpoint of **any** genuine forward word of length \(n\ge0\) from \(z\) followed by **any** admissible true inverse word of length \(k\le n+R\), without bounds on the individual exponents. Taking \(R\to\infty,\epsilon\downarrow0\) along a diagonal sequence yields roots tending to infinity. Their entire ordinary forward suffixes are still part of the original fixed component.

Let \(A,H\) be the respective physical costs of those forward and inverse words. From (1), the relative multiplicative factor \(3^{n-k}2^{H-A}\) differs from \(w/z\) by a multiplicative \(\exp(O(m_j^{-\delta}))\), uniformly in both word lengths. This follows directly by dividing the two identities (1); the paths share the same component clock origin. Thus (4) constrains the whole profinite test family at once. Merely extracting a local limit of gap words may lose the critical Cesàro mean of the moving starting points.

## A profinite control retaining every inverse comparison

**Priority and scope.** At PR 201 head `3eb251fae9082fef33c047079a511d1c3f4c5969`, `research/unconventional-20261126/operator/HYBRID_DESCENT.md`, OP-D2 and OP-D3 give the same mixed unit root in the stronger full shortcut graph, together with quantitative positive ordinary finite-radius copies. The following independent accelerated proof gives the odd-step version of that control. The preceding moving-floor statements concern actual component levels and the additional critical-mean hypothesis.

There is an explicit mixed profinite source with both coordinates units passing the limiting coefficient test for **all** finite forward–inverse comparisons, with positive forward logarithmic drift. Take dyadic starting coordinate \(-1\) (its forward gaps are all one), ternary starting coordinate \(1\), and forward ternary states \(y_n=2(3/2)^n-1\), interpreted as rationals integral at three. The other primes can use the same rational coordinates with powers of two inverted. For every positive-gap word of length \(k\) whose reverse edges from \(y_n\) are ternary-integral, at total \(H\) its relative coefficient is
\[
                           r=3^{n-k}2^{H-n}\ge1.                    \tag{5}
\]
For \(k\le n\), this follows from \(H\ge k\). Suppose \(k>n\). Through the first \(n\) inverse steps the current real value is at least the all-ones inverse value \(2(3/2)^{n-i}-1\ge1\) after \(i\le n\), by monotonicity of \((2^e y-1)/3\) on positive inputs. Any exponent exceeding one makes the final comparison strict. At the \(n\)-th reverse step the current value \(W\ge1\) is an ordinary odd integer. Indeed the successive ternary-integral quotients are dyadic rationals. When \(n\ge1\) the initial dyadic denominator divides \(2^{n-1}\), and the total of the first \(n\) positive gaps is at least \(n\). Thus the last doubled power product before subtracting one is an even integer: if the denominator was cleared earlier the current value is already integral; if it first clears in that last product, the total exponent exceeds the initial denominator exponent. Division of the resulting odd numerator by three preserves oddness. At \(n=0\) one simply has \(W=1\).

The remaining reverse divisions from \(W\) produce positive ordinary odd states, ending at a positive integer \(t\). The complete positive carry gives
\[
                             t < (2^H/3^k)y_n < 2r .
\]
If \(r<1\) we would have \(t=1\). The remaining \(k-n\) edges reversed are a native positive path from \(1\) to the odd \(W\), so \(W=1\) and all its exponents are two. The comparison through the first \(n\) edges then forces all those exponents to be one. Consequently \(H=n+2(k-n)\) and \(r=(4/3)^{k-n}>1\), contradicting the assumption. This proves (5) without any bound on either reverse depth or individual gaps.

For any finite list of these tests (including a finite list of excluded reverse words), CRT chooses arbitrarily large positive odd unit starting integers realizing the same dyadic forward prefix and ternary decisions. The inequality concerns the slope in (5), which is independent of the lift. The model has forward average gap one; it isolates the failure of a universal local coefficient obstruction after dropping the critical-mean condition. It makes no assertion of an actual infinite positive orbit.
