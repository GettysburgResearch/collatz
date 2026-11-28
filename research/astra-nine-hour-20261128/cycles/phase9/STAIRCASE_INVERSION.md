# The integer threshold of every rational grid clock

Let \(\eta_K\) be the upward-rounded dyadic clock defined in [the rotation theorem](../phase8/DIGITAL_ROTATION.md), and let \(\gamma=\log_2 3\). For any reduced rational \(\gamma<a/q\le2\), set
\[
 b_t=\lfloor(t+1)a/q\rfloor-\lfloor ta/q\rfloor,
 \qquad T_t(x)=\lceil3x/2^{b_t}\rceil,\qquad
 H=T_{q-1}\circ\cdots\circ T_0 .
\]
The composition acts on ordinary nonnegative integers and uses a prescribed mechanical calendar independent of \(K\). Let \(U(a,q)\) be its greatest fixed integer. Then, exactly,
\[
                         \eta_K\ge a/q\quad\Longleftrightarrow\quad K<U(a,q).     \tag{1}
\]
The threshold exists even if the staircase misses \(a/q\) itself. This converts every rational comparison with the autonomous grid map into a greatest-fixed-point problem on a single prescribed calendar. In particular it identifies the right edge of every upper-convergent plateau without a scan over grid resolutions.

### The greatest periodic vector is ordered

Extend a rank vector \(w_0,\ldots,w_{q-1}\) dyadically by \(w_{j+q}=2w_j\) for every integer \(j\). The allowed lattice at rank \(j\) is \(d_j\mathbb Z\), where \(d_j=2^{\lfloor j/q\rfloor}\). Write \(C_d(x)=d\lceil x/d\rceil\). The periodic vector operator is
\[
                         (Tw)_{j+a}=C_{d_{j+a}}(3w_j).
\]
The definition respects extension by doubling. On fundamental coordinates it consists of the chronological maps \(T_t\), since the ranks \(ta\bmod q\) visit every phase. Thus its fixed vectors are in bijection with fixed integers of \(H\), via the coordinate at rank zero.

The operator preserves componentwise order. It also preserves nondecreasing order in the extended rank: if the input is increasing weakly, the next input is larger and its target lattice is a subset of the previous target lattice, so its ceiling cannot be smaller. There is a large ordered integer supersolution. On the fundamental ranks start from \(w_j=\lceil M 2^{j/q}\rceil\). The extension is nondecreasing throughout, including across the seam. The normalized rounding errors in one update are bounded by an absolute constant, while \(2^{a/q}-3>0\), so for sufficiently large \(M\), \(Tw\le w\). More explicitly the real unrounded gap at ranks \(j,j+a\) is \(M 2^{j/q}(2^{a/q}-3)\); taking \(0\le j<q\), the inflation at the input is less than three and rounding at the target adds less than four. The integer vector therefore descends under iteration to a nonnegative fixed vector.

All integer fixed vectors are bounded because \(H(x)=(3^q/2^a)x+O_{a,q}(1)\) with coefficient strictly less than one, and the other coordinates follow from the bounded first coordinate. Take the original supersolution above all of them to obtain their greatest vector \(z\). Its zero coordinate is \(U=U(a,q)\). It is positive because the scalar iteration of \(H\) from one is nondecreasing and bounded by the supersolution. By order preservation through the descent,
\[
                        U=z_0\le z_1\le\cdots\le z_{q-1}\le2U.        \tag{2}
\]

### The greatest vector fails physical rounding at its seam

Shift the lift by one spatial rank, \(z^+_j=z_{j+1}\). The shifted values lie in the allowed lattices. Except when the target rank is \(q-1\bmod q\), its required rounding agrees exactly with that of the shifted original vector. At the exceptional target it rounds onto the lattice twice as fine, so \(Tz^+\le z^+\). If this were an equality at the exceptional rank, \(z^+\) would be a fixed vector above \(z\). They cannot be identical: a period-one lift with \(z_{j+q}=2z_j\) would have \(U=0\). This contradicts greatestness, so the finer rounding is strictly smaller.

In chronological fundamental notation the last winding is \(b_{q-1}=2\), since \(1<a/q\le2\). Write \(x_*=z_{(-a\bmod q)}\) for the state just before the return to rank zero. Its scheduled equation is \(U=\lceil3x_*/4\rceil\), while the shifted finer comparison is \(\lceil3x_*/2\rceil<2U\). Thus
\[
                         4U-3x_*\in\{2,3\}.                           \tag{3}
\]
This defect at the minimum is forced for each rational individually, whether the other rank labels are distinct or repeated.

### Comparing the two clocks

Extend the upward grid ceiling \(F_K(x)=\lceil3x\rceil_{\Lambda_K}\) to arbitrary positive real inputs. If \(K<U\), every fundamental target label \(y\) in the fixed vector is at least \(K+1\). There is no grid point strictly between \(y-1\) and \(y\), since all grid points at least \(K\) are integers. If its scheduled predecessor is \(x\) with winding \(b\), then \(2^b(y-1)<3x\le2^b y\), hence \(F_K(x)\ge2^b y\). Iterating on the periodic rank vector by monotonicity yields \(\eta_K\ge a/q\).

If \(K\ge U\), every fundamental target label \(y\) is a positive integer at most \(2U\le2K\). Every such integer is a grid point: repeatedly double an integer below \(K\) to enter \([K,2K)\), and use the equivalent ray of \(K\) when the integer equals \(2K\). Consequently \(F_K(x)\le2^b y\) on all the scheduled edges, giving \(\eta_K\le a/q\).

Suppose equality held in this last case. Any genuine periodic orbit of the upward grid map, sorted in \([K,2K)\), has \(q\) distinct rays, because its order-preserving rank translation has reduced winding \(a/q\). Start at its minimum \(x_0\). The chronological winding sequence is exactly \(b_t\) and its base representatives satisfy the prescribed ceiling equation even for an edge rounded to the lower seam: upon using the total winding to normalize, an upward-rounded result at \(2K\) halves to \(K=\lceil3x/2^b\rceil\). Thus \(K\le x_0\le U\) and equality throughout gives \(K=x_0=U\). The whole scheduled vector is then \(z\) because its initial coordinate determines every other one. On its last physical edge rounding to \(4K\) requires \(3x_*>4K-2\): the point \(4K-2=2(2K-1)\) belongs to the grid. This contradicts (3). It proves (1), including the strict endpoint.

For example \(U(8,5)=41\), \(U(65,41)=1079\), and \(U(485,306)=78663\). The first resolution with clock below the corresponding rational is exactly the displayed integer in each case. Quantitative control of \(U(a,q)(a/q-\gamma)\) at shrinking positive gaps is still needed for the sharp grid coefficient.
