# How early can two complete Mersenne trajectories meet?

Use the shortcut map, let \(M_j=2^j-1\), and put \(P_j=3^j-1=T^jM_j\). A postpeak clock starts at \(P_j\). Write \(p_h(x)\) for the number of odd departures before clock \(h\). The results below concern all ordinary words, including comparisons at unequal clocks.

## An elementary separation test

Suppose \(T^hP_j=T^lP_t=y\), \(h,l\le H\), and \(3^j-1>3\cdot6^H\). Then
\[
                 h=l,\qquad j+p_h(P_j)=t+p_l(P_t).
\]
The conclusion requires no lower bound on \(t\). The hypothesis is an exact integer test.

Write \(p=p_h(P_j)\), \(q=p_l(P_t)\). The affine formula gives
\[
         2^h y=3^{j+p}+c_h,\qquad |c_h|\le 3^h.
\]
Indeed \(c_h=B_h-3^p\), where \(0\le B_h\le3^h-2^h\) and \(p\le h\). With \(L=\max(h,l)\) both scaled error terms are at most \(3^L\) in magnitude, because \(2^{L-h}3^h\le3^L\). The difference
\[
              2^{L-h}3^{j+p}-2^{L-l}3^{t+q}
\]
therefore has magnitude at most \(2\cdot3^H\). It is divisible by \(3^{\min(j+p,t+q)}\). On the other hand \(2^h y\ge3^j-1\) since every shortcut on a positive integer is at least a halving. This gives \(y>3\cdot3^H\), whence \(3^{t+q}=2^l y-c_l>2\cdot3^H\). The other power is larger than this bound directly. The difference is zero. Its two-adic valuations agree, so \(h=l\), and then the ternary exponents agree.

## A window through nearly \(j\) postpeak steps

There is an absolute \(C\) such that, for every sufficiently large \(j\) and every \(1\le t<j\), compare the full initial ascents from \(M_j,M_t\) and the first
\[
                  H=\lfloor j-C\log(2+j)\rfloor
\]
postpeak steps on both arms. Every actual common site in these two windows occurs postpeak on both arms at the same clock and with the same augmented grade.

Here we use the classical lower bound for the nonzero homogeneous linear form \(a\log2-b\log3\). For \(|a|,|b|\le 5j\) its absolute value is at least \(c(1+j)^{-A}\) for absolute \(c,A>0\). This is the fixed-input two-logarithm specialization of [Matveev, Corollary 2.3](https://doi.org/10.1070/IM2000v064n06ABEH000314).

On the ascent, at \(0\le u<j\), the site equals \(2^{j-u}3^u-1\). At postpeak \(h\), its distance from the leading monomial \(3^{j+p}2^{-h}\) is at most \((3/2)^h\). For a shared site \(y\), if the native arm is postpeak then \(y\ge(3^j-1)/2^H\). Hence the relative errors of both monomials against \(y\) are at most \(2\cdot3^{H-j}\). If the native arm is still ascending then \(y\ge2^j-1\), and both relative errors are at most \(2(3/4)^j\). For sufficiently large \(C\), the logarithmic ratio of the two leading monomials is smaller than \(c(1+j)^{-A}\). The coefficients of its two logs are bounded by \(5j\), so the monomials agree. Two ascents would force \(j=t\). A native ascent has strictly positive binary exponent while an earlier postpeak monomial has nonpositive binary exponent. A native postpeak monomial has ternary exponent at least \(j\), exceeding that of every earlier ascent. Thus both arms are postpeak. Equality of their two exponents gives the stated clock and grade.

Every synchronized, augmented peak linkage class on the progression \(j=11+162m\) is finite by the [earlier finite-class theorem](../../astra-global-closure-20261124/round13/trace/FINITE_FAMILY.md). Pick the least exponent of each equivalence class, of which there are infinitely many because all classes are finite. Applying the window theorem gives infinitely many actual \(j=11+162m\) with no meeting in these windows with any earlier member of the same progression. The earlier finite-class proof also applies to the full Mersenne sequence. It gives infinitely many exponents with no meeting through their windows with any earlier Mersenne exponent. These two infinite assertions have different index sets. The exact all-earlier controls in [the ordinary analysis](README.md) have indices in the specified progression.

## At unbounded simple clocks it is the difference of clocks that must grow

For a simple segment of departed positive sites, put \(S\) equal to a lower bound for those sites. The occupation estimate gives \(\sum_{v\ge S}1/v\le480S^{-1/80}\), where this sum is over the segment alone. In the shifted coordinate \(v+1\), an odd step has multiplier \(3/2\), an even step has multiplier \((1+1/(v+1))/2\). Thus
\[
          0\le\log\frac{2^h(T^hP_j+1)}{3^{j+p_h(P_j)}}\le480S^{-1/80}.
\]
The same holds on an independently simple segment from \(P_t\). If they meet, subtraction yields
\[
  |(h-l)\log2-(j+p_h(P_j)-t-p_l(P_t))\log3|\le480S^{-1/80}.       \tag{1}
\]
Simplicity is needed separately on each segment. The two segments may intersect. When two orbits meet, minimizing the sum of clocks gives a meeting with both prefixes simple. [Uniform simple-path occupation estimate](../../astra-global-closure-20261124/round12/arithmetic/README.md)

At large \(S\), write \(a=h-l\), \(b=j+p_h-t-p_l\). Equation (1) bounds \(|b|\) by \(2+|a|\). If \((a,b)\ne(0,0)\), the same fixed logarithmic form now gives \(|a|\ge c' S^{\eta}\) for some absolute \(c',\eta>0\). An elementary version has \(|a|\ge (\log_2 S)/80-O(1)\). Indeed for \(S\) large the signs of the nonzero coefficients coincide, and \(|2^{|a|}-3^{|b|}|\ge1\). Dividing by either power and using (1) proves the bound. For a hypothetical bad e6 source every site of its orbit and every site of an intersecting positive orbit is at least the global bad minimum \(s\gg2^j\). A meeting between any two such peaks at independently simple clocks is either synchronized and augmented, or its clock difference is at least \(c''2^{\eta j}\). The bound is independent of both total path lengths and of the choice of \(t\). It leaves mergers with large clock difference and independent direct drops below the minimum open.

The logarithmic-form arguments and simple-path estimates above are written deductions.
