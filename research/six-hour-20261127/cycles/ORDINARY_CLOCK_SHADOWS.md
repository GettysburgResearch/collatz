# Where a long agreement of odd clocks can occur

**PROPOSED written results.** In a primitive positive ordinary cycle, every proper comparison of valuation windows has at least logarithmically many defects. Its defects cannot concentrate into finitely many sublinear arcs of odd time. A linear gap between defects forces the lag to be within a constant multiple of the defect count of a rational rotation of bounded order. An irrational limiting lag gives the full largest-gap denominator fraction for positive rational cycles with high phases even when the raw defect count is unbounded. The finite peak estimate below gives an elementary quantitative form. It uses no toric gcd estimate.

## A common word viewed from both ends

Use odd phases \(x_i>0\) of a primitive rational Syracuse cycle with least odd period \(p>1\), common reduced denominator \(d\), and gaps \(e_i\ge1\). Write
\[
 2^{e_i}x_{i+1}=3x_i+1,\quad E_i=\sum_{j<i}e_j,\quad A=E_p,\quad
 D=2^A-3^p,\quad \mu=\min_i x_i,\quad X=\max_i x_i .
\]
The positive determinant is prime to six. Each numerator \(N_i=d x_i\) is an odd positive integer and every two phases in one period are distinct. Put \(\lambda=\log_2 3,\ \kappa=\log_2(3/2)=\lambda-1\) and
\[
 \Delta=A-p\lambda=\sum_{i<p}\log_2(1+1/(3x_i)).
\]
The statements for ordinary cycles set \(d=1\). Their mean clock satisfies \(A/p\le2\). For rational asymptotic statements we assume \(\mu\to\infty\), which implies \(A/p\to\lambda\). On either family, two fixed logarithms give \(\Delta\gg p^{-C}\). The product identity gives \(\mu\le p/(3\Delta\ln2)\), hence \(\log_2(\mu+1)=O(\log p)\). Moreover, in a primitive ordinary cycle the p distinct positive odd states give \(\Delta=O(\log(2p))\) by summing the p largest allowed summands. Distinct primitive ordinary cycles of growing period have \(\mu\to\infty\) because each bounded positive integer determines at most one cycle. [Matveev](https://doi.org/10.1070/IM2000v064n06ABEH000314) · [Weaver, Mahler and Wren, Paper 22 v4, equation (56)](https://rstation.ai/problems/collatz/papers/22/v4)

Choose any \(1\le v<p\) and integer \(u\). Let \(B_i=E_{i+v}-E_i,\ J=\{i:B_i\ne u\},\ m=|J|\), and let \(h\) be the largest cyclic spacing between successive elements of J. For primitive words \(m>0\), as a constant \(B_i\) would imply \(e_{i+v}=e_i\) at every index. Statements assuming a good start have \(m<p\), so \(u\in[1,A]\). If \(m=p\) the logarithmic lower bound is immediate and \(h=1\).

If two phases follow the same k successive accelerated clocks with sum E, subtract the recurrences. For some nonzero integer z their initial and terminal numerator differences are respectively
\[
 2^{E+1}z,\qquad 2\,3^kz. \tag{P1}
\]
Indeed \(2^E(N'_k-N_k)=3^k(N'_0-N_0)\). The two powers are coprime, and the final difference is even. At intermediate time j the difference is \(2^{E-E_j+1}3^j z\). The two ends cannot both be small. This integer-gap calculation is already present for ordered gap paths in Paper 22, equations (50)–(53). The native agreement-height principle is also used in the project's earlier shift-distance work. Here the two phases need only be separated by the selected odd-time lag, and the estimates track the distribution of its window exceptions. [Paper 22 v4, Theorem 10](https://rstation.ai/problems/collatz/papers/22/v4) · [Prior native-shift distance theorem](https://github.com/GettysburgResearch/collatz/blob/711a9bb05c240ac3a8e89ce1b541fb59495ddb56/research/cyclic-shift-distance/HEIGHT_AND_ALMOST_PERIODS.md)

A run of H consecutive good starts gives \(H-1\) identical future clocks at the first start and its v-shift, since \(B_{i+1}-B_i=e_{i+v}-e_i\). Therefore \(dX\ge 2\,3^{\max(h-2,0)}\) whenever \(h\ge2\). The harmless degenerate case \(h=1\) has no bearing on any limiting statement.

## An effective bound for any cover by odd-time arcs

At each good start \(i\), exact multiplication along its v steps gives
\[
 |\log_2(x_{i+v}/x_i)|\le (A/p)m+\Delta.                 \tag{P2}
\]
In fact \(\sum B_i=Av\), so \(|Av/p-u|\le mA/p\). The remaining error in the logarithm is the difference between the partial distortion and \((v/p)\Delta\), both in \([0,\Delta]\). At physical distance t forward from the minimum, \(x_i+1\le(3/2)^t(\mu+1)\). If a run of H good starts begins there, (P1) at its initial end gives
\[
 H\le\kappa t+B,\qquad
 B=\log_2(d(\mu+1))+(A/p)m+\Delta .                    \tag{P3}
\]
This includes \(H=1\): any two distinct odd numerators differ by at least two.

Suppose J is covered by R circular intervals containing in total T odd-time positions, counted with multiplicity. Cut the circle at the minimum, merge overlaps, and read the complement. There are at most R+1 clean pieces. A covered piece of length l increases elapsed time by l. Each clean piece sends elapsed time t to at most \(\lambda t+B\) by (P3). Moving the covered pieces to the beginning in this scalar upper bound only increases it. Thus
\[
 p\le \lambda^{R+1}T+B\,\frac{\lambda^{R+1}-1}{\kappa}. \tag{P4}
\]
A fixed R and \(T=o(p)\) imply for any family of primitive high positive rational cycles
\[
 \liminf\frac{\log d}{\log D}\ge
 \frac{\kappa}{\lambda(\lambda^{R+1}-1)}>0 .             \tag{P5}
\]
Here \(m\le T,\ \Delta=o(p),\ \log_2D/p\to\lambda\). For ordinary cycles this forbids such a cover in odd time alone, irrespective of native cluster diameter. Taking \(R=T=m\) instead gives for **every** proper window of every primitive ordinary cycle
\[
 m\ge\frac{\log p-\log\log(2p)-O(1)}{\log\lambda}.       \tag{P6}
\]
Indeed \(B=O(m+\log p)\). Equation (P4) yields \(p\ll\lambda^m(m+\log p)\). When \(m\) exceeds a sufficiently large constant times \(\log p\) (P6) holds directly; otherwise take logarithms. The appearance of the base \(\lambda\) in chains of integer gaps is classical. Theorem 10 of Paper 22 proves a bound with this base for a different statistic on sorted ranks. Formula (P4) tracks exception arcs for an arbitrary comparison in physical odd time. The stronger Farey square-root theorem remains prior and applies under its own clock hypotheses. [Simons and de Weger, §§3.3–3.4](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf) · [Paper 22 v4](https://rstation.ai/problems/collatz/papers/22/v4)

## Peak estimate from the multiples of the lag

For \(c=v/p\), let \(G_K(c)\) be the largest circular spacing among the distinct points \(0,c,\ldots,Kc\bmod1\), with spacing one for a singleton. Set
\[
 \eta=\frac{(A/p+\kappa)m+\Delta}{p}.
\]
For every positive integer K and \(0<r\le1\),
\[
 \frac{\log_2((X+1)/(\mu+1))}{p}
 \ \le\ \kappa\bigl(G_K(c)+r\bigr)+\frac{K\eta}{r}.        \tag{P7}
\]
No density or independence assumption on the individual exceptional points enters this estimate.

Rotate the minimum to zero. Interpolate \(H(i/p)=p^{-1}\log_2(x_i+1)\) linearly and periodically on the circle. Since \(x_{i+1}+1\le(3/2)(x_i+1)\), its *forward* slope is at most \(\kappa\), including across the periodic seam. Its full oscillation is at most \(\kappa\). At good starts (P2) bounds the absolute shift difference of H by \(((A/p)m+\Delta)/p\): adding one contracts the absolute logarithmic ratio of two positive reals. The m exceptional vertices have shift difference at most \(\kappa\). Convex interpolation and periodic summation give
\[
 \int_0^1 |H(t+c)-H(t)|\,dt\le\eta.
\]
Translation invariance and the triangle inequality give the bound \(k\eta\) at every multiple \(kc\).

Let H attain its maximum at s. Choose a sampled point \(kc,\ 0\le k\le K\), immediately before or equal to \(s-r\bmod1\). Use real lifts so that \(\ell=s-kc\) lies in \([r,r+G_K(c)]\). For \(0\le t\le r\) the forward slope bound gives
\[
 H(kc+t)-H(t)\ge H(s)-\kappa(\ell-t)-H(0)-\kappa t
                 =H(s)-H(0)-\kappa\ell .
\]
Integrate on this interval, use \(r\le1\), and apply the \(k\eta\) bound. This proves (P7).

Suppose \(m=o(p),\ \mu\to\infty,\ v/p\to c_0\). If \(c_0\) is irrational, (P7) gives \(\log X=o(p)\). If \(c_0=a/q\) in lowest terms, including q=1 for the endpoints 0,1, it gives
\[
 \limsup_{p\to\infty}\frac{\log_2(X+1)}p\le\frac{\kappa}{q}.
\]
Indeed for fixed K the largest finite-set gap varies continuously with c, including collisions. At a rational rotation \(K\ge q-1\) suffices for the \(1/q\) grid. At an irrational rotation the mesh tends to zero as K increases. First take \(p\to\infty\) for fixed K and r, then \(r\downarrow0\), and finally K large. Combining with (P1) at the terminal end gives
\[
 \liminf\left(\frac{\log d}{\log D}-\frac hp\right)
 \ \ge -\frac{1-\log_3 2}{q},                              \tag{P8}
\]
where \(1/q=0\) in the irrational case. For ordinary cycles this forces \(\limsup h/p\le(1-\log_3 2)/q\). In particular every clean gap has sublinear length at an irrational limiting lag with \(m=o(p)\). There, a sublinear odd-time arc automatically has sublinear native duration: the exact segment identity gives \(E_{i+k}-E_i=k\lambda+\log_2(x_i/x_{i+k})+\Delta_{i,k}\), with \(\Delta_{i,k}\le\Delta=o(p)\). Thus an a priori native-rectangle assumption disappears in this actual trajectory regime.

**Quantitative near-resonance.** Fix \(\delta>0\) and \(0<\epsilon<\lambda\delta\). For all sufficiently long primitive ordinary cycles with \(h\ge\delta p\) there are coprime integers \(a,q\), \(q\ge1\), with
\[
 q\le\frac{\kappa}{\lambda\delta-\epsilon},
 \qquad |qv-ap|=O_{\delta,\epsilon}(m).                    \tag{P9}
\]
First, (P1) gives \(\log_2X/p\ge\lambda\delta-O(1/p)\), while direct forward growth from the minimum gives an upper bound \(\kappa+O(\log p/p)\). If \(\lambda\delta>\kappa\) there are no such large ordinary cycles. In the remaining range the denominator bound permits q=1. Equations (P6) and the ordinary distortion bound give \(\eta=O(m/p)\). If \(\eta\) exceeds a fixed positive threshold, take q=1 and the nearest integer to \(v/p\); then \(p=O(m)\). Otherwise choose a sufficiently small fixed \(r>0\), and \(K=\lfloor c_*/\eta\rfloor\) for a sufficiently small positive \(c_*=c_*(\delta,\epsilon)\). After decreasing the threshold, K is arbitrarily large, \(\kappa r+K\eta/r<\epsilon/3\), and \(2\kappa/K<\epsilon/3\). Dirichlet approximation gives a reduced \(a/q\) with \(1\le q\le K\) and \(|qc-a|\le1/K\). The first q sample points are each within \(1/K\) of the grid \(0,1/q,\ldots,(q-1)/q\), whence \(G_K(c)\le 1/q+2/K\). Apply (P7), absorbing the vanishing minimum and endpoint errors into \(\epsilon\). This gives the claimed q bound and \(|qv-ap|\le p/K=O(m)\). For a family satisfying \(m=o(p)\), the measure of detuning in (P9) is sublinear in the period.

There is also an exact arithmetic condition at a bounded-order lag. If \(v/p=a/q\) exactly in lowest terms and \(qm<p\), some orbit of addition by v contains no exceptions: there are \(p/q\) such orbits. Summing its q window clocks tours a full period a times, so \(qu=aA\). Hence \(q\mid \gcd(A,p)\). This last conclusion uses exact resonance and cannot be inferred just from (P9).

## Testing the route against unrestricted words

High positive phases, a vanishing full drift, coprime clocks and ordinary-sized least phase do not force any low-defect lag. For each growing upper convergent A/p to \(\lambda\), choose a binary gap word in \(\{1,2\}\) with exactly \(A-p\) two-gaps. All such words have primitive period p because \(\gcd(A,p)=1\). All their rational phases satisfy the precise clocks, and their minima tend to infinity uniformly by \(1/(3\mu)\le2^\Delta-1\). They all satisfy the polynomial upper bound on the minimum proved above.

In fact, a fraction tending to one of these words has at least \(p/50\) exceptions for every proper lag and every target. To see this, first sample independent letters with two-gap probability \(\beta=(A-p)/p\), so \(2\beta(1-\beta)>0.45\) for large p. For any fixed nonidentity lag its permutation cycles have length at least two. Select disjoint edges on these cycles, at least \(p/3\) of them. Along these edges the mismatch indicators are independent with common probability at least 0.45. For their sum S, \(\mathbb E 2^{-S}\le e^{-0.45p/6}\). Consequently \(\mathbb P(S<p/25)\le 2^{p/25}e^{-0.45p/6}\). A union bound works simultaneously over all p−1 lags. Conditioning on the exact number of two-gaps costs at most \(p+1\), because that count equals the integer mean and is a mode of the binomial distribution. Finally every unequal edge \(e_{i+v}\ne e_i\) has \(i\) or \(i+1\) exceptional, so each window discrepancy count is at least half the shift Hamming distance. This proves the assertion.

There are exponentially many such words. Each fixed-composition word prior to conditioning has probability at most \(0.65^p\) for large p. Meanwhile the number of words with reduced denominator at most B is at most \(O(p^{C+2}B^2)\): the reduced least numerator is at most \(d\mu=O(d p^{C+1})\), and each least fraction determines at most one primitive cycle and its p rotations by the deterministic map on odd-denominator rationals. Thus for example exponentially many members of this family have \(d>\exp(p/10)\). They are exact positive rational cycles. They show why an unrestricted proof still needs an ordinary-integer implication beyond the size of \(\mu\), near-criticality and the symbolic clock mean. No conclusion here treats ordinary words with dense defects and short agreement at every lag.
