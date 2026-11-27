# A quantitative rate for the odd width of an ordinary cycle

Let \(s,X,p\) be the least odd phase, greatest odd phase and primitive odd period of an ordinary positive Collatz cycle. Put \(\nu=4.116201\). For every sufficiently large \(p\), with absolute implied constants,
\[
 \max(0,3-X/s)\ \ll\
       \left(\min\left\{s^{-1/(\nu+1)},\;p^{-1}+p/s\right\}\right)^{1/6}.
                                                                        \tag{1}
\]
In particular \(X\ge3s-O(s^{1-1/(6(\nu+1))})\). The fractional exponent is approximately \(0.03258\). The result applies to all native valuation sequences. The threshold and constant have not been made numerical. This refines the spatial-rank sixth-difference proof of the asymptotic lower bound three, using the same published linear-form input. [Order-six argument, two-grade register, and excursion classification](WIDTH_THREE.md) · [Bondareva, Luchin and Salikhov, Theorem 1, p. 18](https://m.mathnet.ru/links/1d9b9977c1093c37b767dc2d807bd4a2/cheb619.pdf).

## Uniform angle discrepancy

Take any choice \(L\) used to fold each ordinary phase into one octave and write \(\theta_i=\log_2(x_i/L)\bmod1\) in chronological order. For \(\gamma=\log_2 3\),
\[
 \theta_{i+1}=\theta_i+\gamma+\eta_i\pmod 1,\qquad
                  0<\eta_i=\log_2(1+1/(3x_i))\le C/s .
\]
Let \(\Delta\) be the supremum, over circle intervals, of the absolute difference between their empirical angular mass and their length. The cited Theorem 1 applied to \(k\log 3-m\log2\), with \(m\) nearest to \(k\gamma\), gives \(\|k\gamma\|\ge c k^{-\nu}\) for every positive integer \(k\), after reducing \(c>0\) to include bounded \(k\).

Set \(Q=\lfloor s^{\nu/(\nu+1)}\rfloor\). Dirichlet approximation supplies a reduced \(a/q\), \(1\le q\le Q\), with \(|q\gamma-a|\le1/Q\). Reduction from an unreduced fraction preserves that inequality. The preceding lower bound gives \(q\gg Q^{1/\nu}\). From any chronological start, its first \(q\) true angles are within circle distance \(O(q/s+1/Q)\) of the translated \(a/q\)-grid paired date by date. The grid has interval discrepancy \(O(1/q)\). Enlarging or shrinking the tested interval at both ends gives the same bound with \(O(q/s+1/Q)\) added. Average over all starting dates modulo \(p\): each actual point is counted exactly \(q\) times, including when \(q>p\). Thus \(\Delta\ll s^{-1/(\nu+1)}\).

Independently the genuine angular clock \(A=\sum_i v_2(3x_i+1)\) satisfies \(|A/p-\gamma|\le C/s\). For the width range below, the exact rank permutation in the two-grade register gives \(\gcd(A,p)=1\). Comparing a full period to the translated \(A/p\) grid instead gives \(\Delta\ll p^{-1}+p/s\). The empirical angular measure has an atom of size at least \(1/p\), so \(1/p\le\Delta\) by shrinking an interval around an atom. In sorted order the fundamental labels in \([L,2L)\) satisfy
\[
           \left|Z_r/L-2^{r/p}\right|\le C_0\Delta\quad(0\le r<p).        \tag{2}
\]
Indeed the half-open interval from zero to the \(r\)th angle contains exactly \(r\) distinct angles. Exponentiation is Lipschitz on \([0,1]\).

## The shrinking forced interval

We may deal with \(X/s<3\) and \(\delta=3-X/s\) only. The qualitative width theorem gives \(\delta\le1/4\) at all sufficiently large periods. Put \(\epsilon=\delta/12\), \(L=2(1-\epsilon)s\), \(\alpha=\gamma-1\), and
\[
 u=\log_2\big((3-\delta)/(2(1-\epsilon))\big),\qquad
 v=-\log_2(1-\epsilon),\qquad
 w=\tfrac1{20}\min\{\alpha-u,v,2\alpha-1\}.
\]
All three entries are positive and \(c_1\delta\le w\le C_1\delta\). A fundamental mark one requires angle at most \(u\), and a fundamental mark two requires angle at least \(v\) since the smallest possible doubled odd phase is \(2s\).

Suppose \(\delta^6>C_2\Delta\) with a sufficiently large absolute \(C_2\). We have \(\Delta+400/p\ll w\) with an arbitrarily small implied factor by increasing \(C_2\). At any fundamental rank of fraction \(f>\alpha-10w\), all 17 unwrapped labels used by the stencil have mark two and are twice odd integers. Before the seam their angles exceed \(u\) by the discrepancy bound for sorted angles. After the seam their underlying angles are at most \(16/p+\Delta<v\), so they have fundamental mark one and are doubled in the unwrapped register. On every other tuple all unwrapped marks belong to \(\{1,2\}\).

Write \(\alpha_p=A/p-1\), so \(\alpha\le\alpha_p\le\alpha+C/s\). At all sufficiently large \(p\), \(1/2<\alpha_p<2/3\). Every date following a mechanical division by two (the calendar symbol one) has fraction at least \(\alpha_p\), hence is forced in the preceding sense. The run classification of the order-six stencil now applies word for word. Unless its values \(H_r=P(E)Z_r\) have one strict global sign, every rank in
\[
                         I=[\alpha-6w,\alpha-4w]
\]
has \(H_r=0\). Indeed its fraction is less than \(\alpha_p\) and greater than \(1-\alpha_p\): it is a second two, on which the run classification requires \(H=\pm3\) whenever nonzero. Its forced tuple instead requires \(4\mid H\).

To measure such a zero interval, take \(r=\lceil(\alpha-6w)p\rceil\) and \(t=\lfloor wp/720\rfloor\). Our choice of \(C_2\) makes \(wp\) arbitrarily large. Thus \(h=60t/p\) lies between \(w/24\) and \(w/12\). All ranks from \(r\) through \(r+360t\) are in \(pI\). The polynomial \((T^{60t}-1)^6/P(T)\) has only nonnegative shift exponents, hence \((E^{60t}-1)^6Z_r=0\). By (2) the same difference on the array \(2^{r/p}\) has absolute value at most \(64 C_0\Delta\). Its exact value is
\[
                2^{r/p}(2^h-1)^6\ge c_2 w^6\ge c_3\delta^6 .
\]
This contradicts the supposition for an absolute \(C_2\).

The remaining alternative is strict sign everywhere. The full-octave stride convolution then gives \(s\ge c p^6\) with an absolute constant, since \(L\le2s\) and its stencil is fixed. The same BLS theorem and the actual angular clock give \(s\ll p^{\nu+1}\), contradicting the sign alternative for every sufficiently large period, uniformly in \(\delta\). Thus \(\delta^6\le C_2\Delta\), proving (1). This argument leaves an interval below the value three at every finite height.
