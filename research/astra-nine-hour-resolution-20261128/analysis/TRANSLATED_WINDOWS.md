# Actual translated windows and component frequencies

Let \(T(2n)=n,T(2n+1)=3n+2\) on the positive integers. For \(|f|\le1\) put
\[
 D(X,H)=H^{-1}\sum_{X\le n<X+H}f(n)
\]
with real endpoints and positive integer sources.

**W1.** Suppose \(f(Tn)=f(n)\) outside a fixed finite set, and \(f\)
has natural mean \(d\). There is an absolute \(\kappa>0\) such that
\[
 \sup_{H\le X\le H(\log H)^\kappa}|D(X,H)-d|\longrightarrow0.
 \tag{1}
\]
Every sufficiently high interval of this width contains predecessors
of each prescribed positive target of positive natural predecessor density.
The assertion also holds in total variation for a countable
complete-component coloring whose initial-segment laws converge in
total variation. The fusion estimates are uniform in the label once
the smallest possible prefix state exceeds the exceptional edges.
The final convergence uses the individual or joint natural mean,
without a uniform rate for convergence to that mean.
[Weaver, counted fusion, Lemma 2 and (18)](https://rstation.ai/problems/collatz/papers/124/v1)
· [earlier fixed-target and Fourier estimates, §§2–3](https://rstation.ai/problems/collatz/papers/221)
· [fixed-target lower bound](https://rstation.ai/problems/collatz/papers/12)

For \(r\in\{1,2\}\), throughout an interval \(I=[Z,Z+V)\)
with \(Z\ge V/4\), the proportion of \(n\) with
\(f(n+r)\ne f(n)\) is \(O((\log V)^{-1/2})\) for sufficiently
large \(V\). Indeed counted equal-state, equal-odd-count fusion by
\(j=\lfloor\frac12\log_2 V\rfloor\) fails with Haar proportion
\(O((j+1)^{-1/2})\). The test is periodic modulo \(2^j\).
A period remainder costs \(O(2^j/V)\) independently of the translate,
and every prefix through this date stays above \(Z2^{-j}\).
On a fixed-stride subpopulation enlarge to the enclosing interval,
costing at most a constant depending on the stride in normalization.

For each \(s=2,3\),
\[
 |D(sZ,sV)-D(Z,V)|\ll (\log V)^{-1/2}.                              \tag{2}
\]
Group the first dilate in blocks \(2n,2n+1\), replace the second
member by the first using fusion, and use the exact halving.
For the second dilate group in blocks \(3n,3n+1,3n+2\)
and replace all three labels by \(f(3n+2)=f(2n+1)\). Replace that
last label by \(f(2n)=f(n)\). Endpoint costs are \(O(1/V)\).
This proves (2) in the sum norm for the coordinate unit vectors of
a countable coloring.

Put \(\theta=\log_2 3\) and \(t_j=2^{\{j\theta\}}\in[1,2)\).
Move from \(t_j\) to \(t_{j+1}\) by multiplying by three and
dividing by two once or twice. All intermediate factors lie in
\([1,6]\). For \(J=\lfloor(\log H)^{1/4}\rfloor\), telescoping (2)
and averaging \(0\le j<J\) costs \(O(J/\sqrt{\log H})\).
The variation of \(u\mapsto D(2^u X,2^u H)\) on \(0\le u\le1\) is
\(O(1+X/H)\). Each relevant integer enters or leaves at most twice,
with jump size at most \(H^{-1}\). The smooth normalization term
costs \(O(1)\). Replacing the rotation average by the integral costs
\(O((1+X/H)\mathcal D_J)\), where \(\mathcal D_J\) is star
discrepancy. Integration against the bounded primitive of the
difference of the averaging measures proves this estimate, with
either one-sided convention at jumps. The variation estimate also
holds in the sum norm for a countable coloring.

Here \(\mathcal D_J\ll J^{-\eta}\) for some absolute \(\eta>0\).
The two-logarithm theorem for the fixed rationals 2 and 3 gives
\(\|q\theta\|\ge c q^{-B}\) for fixed \(B\ge1,c>0\).
Indeed the nonzero form \(q\log3-p\log2\) has coefficients
\(O(q)\) for the nearest integer \(p\). For \(Q=\lfloor\sqrt J\rfloor\),
Dirichlet approximation supplies coprime \(p,q\) with
\(q\le Q,\ |q\theta-p|\le Q^{-1}\), so \(q\gg Q^{1/B}\).
In each complete block of length \(q\), the rotated grid of denominator
\(q\) approximates its orbit points within \(1/Q\). The remaining
partial block costs \(q/J\). Thus
\(\mathcal D_J\ll J^{-1/(2B)}+J^{-1/2}\).
The elementary bound \(\|q\theta\|\gg 3^{-q}\), from separation
of the distinct integers \(3^q,2^p\), gives \(\mathcal D_J\ll1/\log J\).
[Matveev, two fixed logarithms, *Izvestiya* 64 (2000)](https://www.mathnet.ru/eng/im314)

The integral is
\[
 \int_0^1D(2^uX,2^uH)\,du
 =\sum_n f(n)w(n),\qquad
 w(v)=\frac1{H\log2}\int_{[1,2]\cap(v/(X+H),v/X]}
                   \frac{dt}{t^2}.
\]
For \(X\ge H\), this weight is supported on \([X,2(X+H)]\),
is unimodal, and is \(O(1/X)\). It increases up to \(X+H\),
equals \(1/(v\log2)\) from \(X+H\) to \(2X\), then decreases.
Also \(\int w(v)\,dv=1\). Partial summation bounds the error from
\(d\) by
\[
 O\left(X^{-1}+\sup_{y\ge X/2}
 \left|y^{-1}\sum_{n<y} f(n)-d\right|\right)
\]
independently of \(X/H\). The same argument applies to the countable
law in the sum norm. Take \(0<\kappa<1/(8B)\) to obtain (1).
The elementary alternative gives \(X/H=o(\log\log H)\) without
linear forms in logarithms.

## A signed endpoint estimate before taking an invariant label

**W2.** Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odds,
\(E_t(x)\) sum the first \(t\) halving exponents, and
\(|\psi|\le1\) have zero mean on \(\mathbb Z/3\). Uniformly for
\(X\ge1\), \(H\ge2\), and \(1\le t\le(\log_2 H)/32\),
\[
 \sum_{s,y}\left|\sum_{\substack{X\le x<X+H,\ x\ {\rm odd}\\
                          E_t(x)=s,\ U^t(x)=y}}\psi(x)\right|
          \ll_A H(1+t)^{-A}                                              \tag{3}
\]
for every fixed \(A\). The normalization uses the width even for
arbitrarily high translates. This is the unweighted translated version
of the signed physical source argument in PR195.
[PR195, physical source cutoff and extra trit](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/PHYSICAL_SOURCE.md)
· [Weaver–Wren, Theorem 6, (66)](https://rstation.ai/problems/collatz/papers/48/v1)

Write \(q=3^t,Q=3q,A_s=q2^{-s}\). A word sends its source to
\(y=A_s x+F\), with \(0<F<q\) dyadic. Its probability under the
independent geometric law is \(2^{-s}\). Let \(P_s(r)\) be the joint
mass of its total \(s\) and \(F\bmod Q=r\). Let \(M\) take the
average over lifts of each residue modulo \(q\). The external input is
\(\sum_s\|P_s-MP_s\|_1\ll_A(1+t)^{-A}\).
For \(s\le4t\) replace \(x\in I\) by \(y\in A_s I\).
A changed word-source pair has \(x\) within \(2^{4t}+1\) of one
of the two endpoints, because \(F/A_s<2^s\). For a legal word
at a positive odd \(y\), the inverse odd source and its whole path
are positive. Each integer inverse step is \((2^e y-1)/3>0\).
Each such \(x\) has just one word of depth \(t\). Their combined
counting cost is \(O(2^{4t})\). Discarding \(s>4t\) from the original
interval costs \(O(H e^{-ct}+2^{4t+1})\) by counting full binary
periods and one incomplete period of the tail event. The iid geometric
moment at \(3/2\) gives the exponentially small tail on a full period.

At any fixed odd \(y\), admissibility means \(y=F\bmod q\),
and the source digit is \(2^s(y-F)/q\bmod3\). Consequently the
signed coefficient after replacement is
\[
 2^s{\bf1}_{y\in A_s I}\sum_{j=0}^2
      \psi(2^sj)P_s(y-jq\bmod Q).
\]
Replacing \(P_s\) by \(P_s-MP_s\) leaves it unchanged.
Each residue occurs \(O(1+A_sH/Q)\) times on the output interval.
Thus summing over \(y\) costs \(O((2^s+H)\|P_s-MP_s\|_1)\).
The original range has \(2^{4t}\le H^{1/8}\), giving (3).

## Comparison with the scale needed for convergence

For a complete component label, almost every interval \([n,n+D)\)
in an octave has a common label whenever
\((1+\log D)^4=o(\sqrt{\log n})\), by the whole-block counted fusion
bound. If every sufficiently high interval of one such width contained
a predecessor of 1, almost every start would reach 1. Positive
predecessor density in each potential bad component would then exclude
every bad start. The width in (1) approaches the full source height on
a logarithmic scale. Rotation averaging pays \(X/H\) for resolving the
translated interval and does not reach the required small widths.
The disjoint positive-density cones of 5 and 85 both obey (1).
Their indicators have a single possible exceptional edge, so a proof
identifying all complete components must use structure beyond
finite-defect high-source cancellation.
