# A constructed rounding comparison and exact mandatory meetings

Let \(N\) be an odd positive integer. On all dyadic lifts of the odd integers \(1\le n\le N\), let \(H_N(v)\) be the **least grid point at least \(3v\)**. The same definition on any positive real makes the maps directly comparable across grids. They are nondecreasing and commute with doubling. Each periodic component of the finite odd-part map has the same reduced rotation \(A_N/p_N\), with \(p_N\) its primitive period. These facts follow from the elementary lift proof in [the simultaneous-cut theorem](ROTATION_CUTS.md).

For every primitive ordinary positive cycle \(C\), write \(p,A,s,X\) for its odd period, total valuation, minimum and maximum. For any odd integer \(N\ge X\), let \(P_N(x)\) denote the **strict predecessor of the eligible output** \(3x+1\) in the dyadic grid. For each periodic component \(R\) of \(H_N\), write \(\widetilde R=\{2^j n:n\in R,\ j\in\mathbb Z\}\). Then
\[
 p_N A-pA_N=M_N(R)
 :=\sum_{x\in C}\#\{V\in\widetilde R:x\le V\le P_N(x)/3\}.       \tag{1}
\]
All native valuations are allowed. Every such cycle satisfies \(A/p\ge\rho_N=A_N/p_N\) at every cutoff \(N\ge X\). If also \(N<8s\), the intervals simplify to exact shared odd integers,
\[
 M_N(R)=\#\{x\in C\cap R:3x\le N\}.                                    \tag{1a}
\]
Strict comparison entails a positive meeting in each component. Establishing a contradiction from the required meetings remains open.

## Elementary odd-part map and angular cost

On the odd representatives its lifted raw image is exactly
\[
 H_N(n)=\begin{cases}
  3n &3n\le N,\\
  3n+1 &3n>N,\quad \operatorname{oddpart}(3n+1)\le N,\\
  3n+3 &\text{otherwise}.
 \end{cases}
\]
When \(3n>N\), any noninteger dyadic number above it has odd part above \(N\). The first candidate after \(3n\) is \(3n+1\). If it fails, its dyadic order is exactly one, because division by four would already place its odd part below the cutoff. The odd integer \(3n+2\) is outside, and \(3n+3\) is divisible by four with odd part at most \(N\).

For \(N=8S-1\) the fundamental grid on \([4S,8S)\) consists of **every integer** in the octave. On \(V\) in that octave, write the raw image as \(3V+d\). Its upward rounding costs at most one when \(3V<16S\), and at most three when \(3V\ge16S\). This includes the possible rounding to the very first point of the next octave. Hence \(0< A_N/p_N-\gamma=O(1/S)\), where \(\gamma=\log_2 3\). The strict sign follows because an exact all-tripling closed orbit would have \(3^{p_N}=2^{A_N}\).

As \(S\to\infty\) the angles \(t=\log_2(V/(4S))\) on each component approach Haar by the additive \(O(1/S)\) angular rotation error. With \(w(t)=2\lambda2^{-t}\), \(\lambda=\log2\), the two rounding zones cover \(t<2-\gamma\) and its complement. Both have weighted mass one half. Taylor expansion therefore gives
\[
 \limsup 24\lambda^2 S(A_N/p_N-\gamma)
     =\limsup \frac1{p_N}\sum w(t)d\ \le 2.                  \tag{2}
\]
The same argument handles arbitrary odd \(N\) by fixing \(S=(N+1)/8\) up to a bounded adjustment, or by angular grid mesh \(O(1/N)\) when only convergence to \(\gamma\) is required.

There is a strict improvement when \(\mu(\gamma)\le3\) is explicitly assumed. Let \(b\in\{1,2\}\) be the actual octave shift, including a ceiling which lands at the top seam. Put \(t' = 2^b-1-d\in\{0,1,2,3\}\) and let \(f\) be its nonzero fraction. The signs and this notation refer only to the comparison cycle. Its sorted-order permutation is a translation, so each length-\(k\) mechanical shift sequence has at most \(k+1\) possibilities. Here the cumulative shifts of a starting phase of rank \(r\) are \(\lfloor(r+jA_N)/p_N\rfloor\). If two physical integer representatives have the same \((b,t')\) word, subtracting the affine equations gives a difference divisible by \(2^{\sum b}\). At \(k=\lceil\log_3(8S)\rceil+2\), this exceeds \(4S\), since \(\sum b\ge k A_N/p_N-1\). Thus the word identifies the source within a component. Shannon subadditivity and stationarity give
\[
 \log p_N\le\log(k+1)+k[H(f)+f\log3],\qquad
 H(f)=-f\log f-(1-f)\log(1-f).
\]
The explicit extra irrationality-measure hypothesis gives \(\liminf\log p_N/\log S\ge1/3\), by (2) and reduction of the clock. The comparison \(16^{48}<15^{45}3^{13}\) now yields \(\liminf f>1/16\). At a nonzero deficit the mark loses at least one and \(w(t)\ge\lambda\). The actual shift zones differ from the displayed threshold only in an interval of length \(O(1/S)\), which has vanishing angular mass. Thus the right side of (2) is at most \(2-\lambda/16\).

In particular under the same extra hypothesis, the [weighted ordinary clock theorem](WEIGHTED_CLOCK.md) gives strict \(A_N/p_N<A/p\) on **every integer cut** \(0.98s\le S\le s\) on the growing binary physical branch \(X\le(16s+7)/3\). Indeed \((2-\lambda/16)/0.98<2\), while the ordinary conditional lower constant exceeds two. This assertion holds uniformly in the cuts by taking a contrary subsequence. Without that hypothesis (1) remains an exact ordinary identity.

## Winding at common inputs and common outputs

Let \(G(2^k x)=2^k(3x+1)\) on the true lifts. For each \(x\in C,n\in R\) put
\[
 k(x,n)=\left\lceil\log_2\frac{3x+1}{H_N(n)}\right\rceil-
         \left\lceil\log_2\frac{x}{n}\right\rceil.
\]
This is the signed number of crossings of the integer logarithmic levels. Positive events have \(x\le 2^j n\) and \(H_N(2^j n)<3x+1\). Negative events have \(2^j n<x\) and \(H_N(2^j n)\ge 3x+1\). Summing over both components telescopes by their cyclic permutations and clock shifts, giving \(\sum k=p_N A-pA_N\). In each time-difference class modulo \(g=\gcd(p,p_N)\) the same argument gives \((p_NA-pA_N)/g\).

When \(N\ge X\), the true raw target \(Y=3x+1\) is eligible. A strict true-above input has \(3\cdot 2^j n<Y\), so a negative event would have to satisfy \(2^j H_N(n)=Y\). The common odd output \(y\) is coprime to three. Only the middle reference rule \(3n+1=2^e y\), \(3n>N\), can produce it. Write \(3x+1=2^a y\). Then \(j=a-e\) and \(2^j(3n+1)=3x+1\), so \(2^j n<x\) implies \(j>0\). Reduction modulo three gives even \(j\ge2\). Thus \(x=2^j n+(2^j-1)/3\ge4n+1>N\), a contradiction. There are no negative events. The positive event test is exactly \(x\le V\) and \(3V\le P_N(x)\), proving (1) including its endpoint conventions.

The strict predecessor is explicit. With \(Y=3x+1\) eligible, put
\[
 \delta_N(x)=2^{\,\lceil\log_2(Y/(N+1))\rceil},\qquad P_N(x)=Y-\delta_N(x).
\]
Indeed, in the octave \([(N+1)/2,N+1)\) all grid points are the ordinary integers. In its dilates the predecessor distance scales accordingly, using the lower octave at a boundary. Hence the crossing interval is exactly \([x,x+(1-\delta_N(x))/3]\), interpreted as empty when its right endpoint is below \(x\).

If \(N<8s\), a strict interior input \(x<V<x+1/3\) can only be \(x+1/4\), since any reduced denominator at least eight would require an odd part exceeding \(N\). There is no grid point in \([3x+3/4,3x+1)\), since such a point needs denominator at least four and odd part exceeding \(12s\). This excludes all strict interior inputs. At \(V=x\), the output is strictly below \(3x+1\) exactly when \(3x\le N\). This proves (1a). A shared odd child can have only the common native parent \(m\) or its ordinary sibling \(4m+1\) as reference parent. The previous no-negative argument excludes smaller siblings, while larger siblings have height at least \(16m+5>N\). Thus \((N-1)/4<m\le N/3\) is a forbidden parent interval for a shared child. Its common parent would take the homogeneous reference branch there and its sibling is beyond the cutoff.

## Exact sums over cutoffs and payment by high sites

For adjacent odd cutoffs use subscripts \(-,+\). If both are at least \(X\), then (1) gives
\[
             p_- M_+-p_+M_-=p(p_+A_--p_-A_+).
\]
The Farey switching theorem below makes the right side precisely \(p\) at a strict drop and zero otherwise. Thus for odd \(X\le N_0\le N_1\)
\[
 \frac{M_{N_1}}{p_{N_1}}-\frac{M_{N_0}}{p_{N_0}}
     =p\sum_{N_0<N\le N_1:\,\rho_{N-2}>\rho_N}\frac1{p_{N-2}p_N}.
\]
Either side is independent of the choice of reference components. Sending \(N_1\) to infinity also gives the exact remainder
\[
 \theta-\gamma=\frac{M_{N_0}}{p p_{N_0}}+
 \sum_{N>N_0:\,\rho_{N-2}>\rho_N}\frac1{p_{N-2}p_N},
 \qquad \theta=A/p .
\]
These nonnegative increments constrain the meeting counts. The identity gives no uniform lower bound on their growth.

For any odd \(N\), including \(N<X\), count the positive events across **all** components as \(U_N\), and let \(L_N\) be their total number of odd periodic reference states. Define \(B_N=\#\{x\in C:x>N\}\) and \(V_N=\#\{x\in C:x>4N/3,\ v_2(3x+1)\ge3\}\). Then
\[
 U_N+p L_N(\rho_N-\theta)\le B_N+V_N.                                \tag{1b}
\]
Indeed a negative event at \(x\) must round exactly to the least grid point at least \(3x+1\), since its unrounded reference image is strictly below \(3x+1\). That target has at most one incoming periodic lifted edge across all components, by injectivity on the periodic points. If the true child's odd part exceeds \(N\), charge this event to that child in \(B_N\). Otherwise the target is exactly \(3x+1\) and the argument for (1) implies \(x\ge4n+1>4N/3\) and \(a=e+j\ge3\), so charge it to \(V_N\). Within either group each charged phase occurs once. Subtracting the signed winding sum proves (1b). If \(N<8s\), the same fractional-gap argument still reduces \(U_N\) to shared \(x\) with \(3x\le N\), even when some true targets are missing.

In particular for every finite set \(J\) of odd cutoffs,
\[
 \sum_{N\in J}U_N+p\sum_{N\in J}L_N(\rho_N-\theta)
 \le \sum_{x\in C}\#\{N\in J:N<x\}
    +\sum_{\substack{x\in C\\v_2(3x+1)\ge3}}\#\{N\in J:4N/3<x\}.      \tag{1c}
\]
The right side consists of truncated physical height sums when \(J\) is a consecutive interval. This finite-range restriction becomes a distribution estimate only with quantitative control of the periodic masses and clock deficits on the left.

## One odd insertion, Farey switching and the attained clocks

For any two nested finite positive odd grids \(B\subseteq B'\), homogeneous ceiling on the smaller grid is at least ceiling on the larger one at every real input. Rotations are therefore ordered. If \(B'=B\cup\{n\}\), write \(a/b,c/d\) for the reduced rotations, respectively. Then
\[
                     ad-bc\in\{0,1\}.
\]
Indeed sum the previous ceiling winding expression over an arbitrary periodic component of each grid. In a positive crossing the larger grid's output must be the new odd part \(n\), up to a dyadic factor; an old output eligible in the smaller grid would already bound its ceiling from above. Normalize that target to \(n\). The smaller grid's output must be the **first old lift strictly above \(n\)** since its homogeneous raw input is at most \(n\). Both periodic component maps are injective on their respective lifted orbits. Hence there is at most one positive event across the paired components, including multiplicity: the interval from the new lift to the next old lift has length less than an octave for these full grids, and at most an octave for a general nonempty old grid, with the upper bound permitted. The signed sum is nonnegative by rotation order. At a strict switch all larger-grid components must contain \(n\), and all smaller-grid components must contain the odd part of its next old lift. Both grids consequently have a **unique periodic component** at this switch.

As \(N\) increases through odd integers, \(A_N/p_N\) decreases from 2 to \(\gamma\). The limit follows by bounding the upper rounding error by a constant in an octave at height comparable to \(N\). The successive distinct fractions are Farey neighbors. Every best upper rational approximant \(h/p\) of \(\gamma\) in \((\gamma,2]\), in particular every upper simple continued-fraction convergent, occurs as an actual comparison rotation. Otherwise a strict switch straddles \(h/p\); the denominator of a fraction strictly between two Farey neighbors is at least the sum of their denominators. The lower switch endpoint would then be a closer upper approximant with denominator less than \(p\). Thus there are genuine, integral ceiling orbits at these clocks. They have the displayed three-branch dynamics and need not be native positive Collatz cycles.

The switches have an explicit local surgery. For an odd \(n\ge17\) adjoin \(n\) to the full grid through \(n-2\). At scale \(n\), its immediate old neighbors are \(n-1,n+1\). An old source lift changes precisely if its triple lies in \((n-1,n]\). That source is either \(n/3\) for \(n\equiv0\pmod3\), or \((2n-1)/6\) for \(n\equiv2\pmod3\). For \(n\equiv1\pmod3\) there is none. Indeed any fraction in the input interval with denominator four or greater has odd part above \(n-2\). In the two changing cases the stated source belongs to the old grid and its output switches from \(n+1\) to \(n\).

If \(n\equiv3\pmod4\), the old and new two-step lifted outputs are both \(3(n+1)\). The old intermediate \(n+1\) has odd part at most \((n+1)/4\) and can be tripled exactly. The new intermediate \(n\) uses \(3n+3\). Sending each lift of \(n\) back to the corresponding lift of \(n+1\) and fixing every old point then intertwines the two whole maps, so their rotations agree. Consequently for \(n\ge17\) a strict switch requires \(n\equiv5\) or \(9\pmod{12}\). In these cases \(n=4m+1\). The two-step images via \(n\) and \(n+1\) are \(3n+1\) and \(3n+5\): the latter is twice the old ordinary image of \((n+1)/2\). After division by four these are the adjacent integers \(3m+1,3m+2\). Later iterations may merge; the residue restriction supplies no converse.

[Exact switch and winding replay](check_homogeneous_meetings.py) · [Recorded finite controls](homogeneous_meeting_controls.json)
