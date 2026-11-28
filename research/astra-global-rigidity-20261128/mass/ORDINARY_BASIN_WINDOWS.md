# Ordinary predecessor basins segregate on short moving windows

Let \(T(2n)=n,\ T(2n+1)=3n+2\). For each fixed positive integer \(a\), let \(B_a\) be the ordinary sources that eventually visit \(a\), including \(a\). Write
\[
       U_W f(n)=\frac1W\sum_{0\le j<W} f(n+j).
\]
The two positive ordinary roots \(5,85\) have disjoint predecessor basins of positive natural density. For either root, on a uniformly chosen \(n\in[X,2X)\) and any integer \(W=X^{o(1)}\), the local empirical density \(U_W{\bf1}_{B_a}(n)\) converges in distribution to the Bernoulli law with parameter \(d(B_a)\). Their local densities have product tending to zero in mean. At widths \(W=\lfloor X^\epsilon\rfloor,\ 0<\epsilon\le1\), the upper limiting mean product is at most \(C\sqrt\epsilon\) with an absolute constant. All these are statements about the original ordinary map. Neither root belongs to an unknown orbit.

Consequently a general local mixing result for every pair of positive-density fixed inverse trees, with a lower overlap independent of small \(\epsilon\), would contradict this example. A strategy using distinct **complete forward components** requires a property that uses the saturation by all later forward waypoints. A first-target bridge or local limit that applies symmetrically at arbitrary supplied roots cannot alone establish that property.

## A uniform estimate for first-hit colors

For a fixed finite set of positive targets \(A\), let \(F_A(n)\) be the first member of \(A\) hit by the orbit of \(n\), or \(\infty\) if there is none. For any interval \(I\) of \(N\ge2\) consecutive positive starts and any nonnegative integer \(d\),
\[
 \frac{\#\{n\in I:F_A(n)\ne F_A(n+d)\}}{N}
 \ \le\ C \min\!\left(1,\sqrt{\frac{\log(2+d)}{\log(2N)}}\right)
              +C |A| N^{-1/2}.                                       \tag{1}
\]
In particular the bound is uniform over the position of the interval. The first term for *complete component labels* follows directly from the actual same-clock coupling at deadline \(\lfloor\log_2 N\rfloor\). We need the shorter deadline below for *stopped* labels. [PR146, actual growing-gap merger estimate (1), proof and finite-deadline sharpness at 0410811710af2f7da71522ec67233528048adb9a](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

Take \(h=\lfloor (\log_2 N)/2\rfloor\), covering \(I\) by at most \(N2^{-h}+2\) intervals of length \(2^h\), with longer cover at each incomplete endpoint allowed. At most \(C N \min(1,\sqrt{\log(2+d)/\log(2N)})\) pairs have yet to meet at the same clock by \(h\), by the cited finite theorem on each block. Each positive point has at most two one-step preimages under \(T\). Hence the total number of positive starts anywhere that have visited \(A\) by \(h\) is at most \(|A|(2^{h+1}-1)\). Applying this to both \(n,n+d\) costs at most twice this count, also on translated intervals. If neither trajectory has visited \(A\) by the meeting, their first-hit outcomes thereafter agree. This proves (1), with adjusted absolute constants for small \(N\).

The same proof applies to any bounded coloring satisfying \(f(Tn)=f(n)\) outside a finite exceptional set \(A\), replacing the left side by the mismatch proportion. If neither trajectory visits the exceptional set before meeting, the equal terminal colors pull back along both trajectories.

## The actual separated roots

The shortcut sends \(5\) to \(8\) and \(85\) to \(128\). Each subsequently runs down the powers of two and enters \(1,2\). Neither trajectory visits the other supplied root. By forward determinism \(B_5\cap B_{85}=\varnothing\). Each is a fixed odd unit target with positive natural predecessor density on the fixed-basin inputs. The positive lower densities alone suffice for the overlap obstruction. [Fixed-basin natural-source derivation and its frozen dependencies](FIXED_BASIN_NATIVE_WINDOW.md) · [Mazur, positive predecessor lower density for a unit](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

For \(f_a={\bf1}_{B_a}\), averaging (1) over \(0\le d<W\) gives
\[
 \frac1N\sum_{n\in I}|U_Wf_a(n)-f_a(n)|
 \ \le\ C\min\!\left(1,\sqrt{\frac{\log(2+W)}{\log(2N)}}\right)
                   +C N^{-1/2}.                                      \tag{2}
\]
For \(I=[X,2X)\), \(W=X^{o(1)}\), the right side tends to zero. Since the binary random variable \(f_a(n)\) has natural density \(d(B_a)\), its law tends to the indicated Bernoulli law; (2) transfers that assertion to its moving window average. Equivalently \(\mathbb E[(U_Wf_a)^2]\to d(B_a)\) and the variance tends to \(d(B_a)(1-d(B_a))>0\). Both roots have density strictly below one by their disjointness and positive lower densities.

Using \(f_5f_{85}=0\) pointwise and the two estimates (2) bounds the mean of \((U_Wf_5)(U_Wf_{85})\). This gives the claimed zero at subpower widths and \(O(\sqrt\epsilon)\) after the large-\(X\) limit at power width. The conclusion also applies to any uniformly bounded source mark supported on its respective basin, including selected first-arrival rows after summing their actual integer counts.

In particular \(f_5(2n)=f_5(n)\) for every \(n\), and the affine identity \(f_5(2n+1)=f_5(3n+2)\) holds except at the single source \(2n+1=5\). Equation (1) gives this genuine nonconstant coloring zero *upper Banach* density of adjacent changes and quantitative invariance under moving gaps. Its positive and negative colors both have positive natural density. This complements the two-dilation comparison and the one-update mutant by retaining the genuine mapping and the physical precursor set of an ordinary convergent target. [PR211, generic comparison and scope of natural-density control](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/GENERIC_COLORING.md) · [PR211, one-site mutant](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/ONE_SITE_MUTANT.md)

## The quantitative opening for full components

For two distinct full component indicators \(f,g\), their product vanishes pointwise and the same estimate has no early-hit term. Therefore
\[
 \limsup_{X\to\infty}\frac1X\sum_{X\le n<2X}
       U_{\lfloor X^\epsilon\rfloor}f(n)\,
       U_{\lfloor X^\epsilon\rfloor}g(n)\ \le\ C\sqrt\epsilon.        \tag{3}
\]
An independent full-component lower bound \(\eta(\epsilon)\) on this same upper limit would exclude those two components if \(\eta(\epsilon)>C\sqrt\epsilon\) for any admitted \(\epsilon\). In particular any bound satisfying \(\limsup_{\epsilon\downarrow0}\eta(\epsilon)/\sqrt\epsilon=\infty\) suffices without knowing the coalescence constant. Positive densities give only a global product, with the order of averaging different from (3). Neither the lower bound for first landings in widths \(X/(\log X)^{1/9}\) nor the convergence of a fixed-root real mark at fixed physical resolution establishes such an estimate. [PR213, physical source windows for first landings](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/local_first_landing.md) · [Weaver, canonical integer real fibre, §9.2, v2](https://rstation.ai/problems/collatz/papers/19/v2)

## The induced fixed vectors in a density seminorm

On bounded sequences use the Besicovitch square seminorm
\[
 \|u\|_B^2=\limsup_{X\to\infty}X^{-1}\sum_{n\le X}|u(n)|^2.
\]
Composition \(C_Tu(n)=u(Tn)\) respects its null space, and has norm at most \(\sqrt3\) on the quotient. Indeed \(Tn\le(3X+1)/2\) for \(n\le X\) and each value occurs at most twice. Every finite support is null. If \(h=d(B_5)\), then
\[
 (I-C_T){\bf1}_{B_5}={\bf1}_{\{5\}},\qquad
          \|{\bf1}_{B_5}-h\|_B^2=h(1-h)>0.                           \tag{4}
\]
The identity at every point follows directly from first hitting, since the successor of \(5\) never returns to \(5\). Thus the centered class is an exact, nonconstant fixed vector in this quotient even under universal convergence. A coercivity estimate comparing this centered norm with the norm of the one-step defect fails. The same argument works for a mean extending the ordinary Cesàro limits of the functions in (4). An arbitrary translation-invariant Banach mean need not give the same basin mass. In fact both \(B_5\) and \(B_{85}\) contain arbitrarily long intervals: for any fixed \(L\), the union of the \(L\) possible mismatches in (1) has natural density zero, whereas the candidate starting basin has positive lower density. A translation-invariant mean along increasingly long intervals in either basin can assign it mass one. Where a seminorm kills finite supports, the fixed-vector obstruction requires that it also retain a nonzero centered basin class.

There are infinitely many ordinary examples. For \(k\ge2,\ 3\nmid k\) use \(a_k=(4^k-1)/3\); these are odd units, by the order of \(4\) modulo 9. Each proceeds directly to a power of two, and their \(B_{a_k}\) are pairwise disjoint and have strictly positive predecessor density. For \(c=(c_k)\in\ell^\infty\), put \(u_c=\sum_k c_k{\bf1}_{B_{a_k}}\), a pointwise sum with at most one nonzero term. Its defect is \(\sum_k c_k{\bf1}_{\{a_k\}}\), supported on an exponential sequence of zero natural density. The linear map \(c\mapsto[u_c]\) into the quotient's fixed space is injective: a nonzero \(c_k\) contributes at least \(d(B_{a_k})|c_k|^2\) to the squared seminorm. This is a vector-space embedding; no uniform positive lower bound for those basin masses is claimed. The power-of-two gates and their predecessor separation also occur in [PR211, one-site comparison](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/descent/postpeak/stopped/ONE_SITE_MUTANT.md).

An independent one-atom obstruction for full-support summable power weights retains all finite defects and uses no density input. [Positive basin cuts in weighted square spaces](WEIGHTED_BASIN_CUTS.md)

## A low-frequency obstruction for the unweighted ordinary Fourier sum

There are absolute \(\epsilon>0\) sufficiently small for the fixed root \(5\) and constants \(c,L>0\) such that, for all sufficiently large integers \(N\), some \(1\le k\le L N^{1-\epsilon}\) satisfies
\[
 \left|\sum_{n=1}^N \bigl({\bf1}_{B_5}(n)-h_N\bigr)
                    \exp(2\pi i k n/N)\right|
                 \ge c N^{(1+\epsilon)/2},\qquad
 h_N=N^{-1}\sum_{n=1}^N{\bf1}_{B_5}(n).                            \tag{5}
\]
In particular a uniform square-root bound up to logarithmic losses cannot hold for these physical predecessor indicators. This uses the same coalescence obstruction and the ordinary root \(5\). Prime-weighted sums and the indicator of a complete component require separate analysis.

Work on the cyclic group of order \(N\) with normalized counting measure. Put \(f(n)={\bf1}_{B_5}(n)-h_N,\ v=h(1-h)>0\). Set \(W=\lfloor N^\epsilon\rfloor\), \(0<\epsilon<1\). At the cyclic wrap the window changes at most \(W/N\) of the starting sites. Equation (2) on \([1,N]\) and \(|U_Wf-f|\le1\) therefore give \(\|U_W f-f\|_2^2\le C\sqrt\epsilon+o(1)\). As \(\|f\|_2^2\to v\), choose fixed \(\epsilon\) small enough that \(\liminf_N\|U_W f\|_2^2\ge v/4\).

Define \(\widehat f(k)=N^{-1}\sum_n f(n)e^{-2\pi i k n/N}\) and \(D(k)=W^{-1}\sum_{j<W}e^{2\pi i k j/N}\). By Parseval \(\sum_k|D(k)|^2=N/W\), \(\sum_k|\widehat f(k)|^2\le1\), and \(\|U_W f\|_2^2=\sum_k|D(k)|^2|\widehat f(k)|^2\). For \(j=\min(k,N-k)>L N/W\), the geometric-sum formula gives \(|D(k)|\le N/(2Wj)\le1/(2L)\). Taking a fixed large \(L\) bounds that part of the last energy by \(1/(4L^2)<v/16\). Since \(\widehat f(0)=0\), the complementary nonzero frequencies carry energy bounded below by a positive fixed fraction of \(v\) for every large \(N\). Division by \(\sum|D|^2=N/W\) yields \(\max_{0<j\le L N/W}|\widehat f(k)|\ge c_0\sqrt{W/N}\). The reality of \(f\) permits taking positive \(k\le L N/W\), and multiplication by \(N\) gives (5), after absorbing the floor in \(L,c\).
