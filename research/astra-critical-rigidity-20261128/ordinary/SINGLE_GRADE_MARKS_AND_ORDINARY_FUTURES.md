# A single reciprocal grade, its ordinary mark and its subsequent orbit

Fix a bounded real interval \(I=(a,b)\), \(0\le a<b\). Give each positive reduced \(m/3^n\in I\) weight \(2^{-D}\), where \(D\) is its first genuine shortcut date at an integer \(N\), then normalize that single grade to probability. Use \(\log\) for the natural logarithm. Put
\[
 d=\log3-\tfrac43\log2,\quad
 \mu=2/\log(4/3),\quad \sigma^2=2(\log3)^2/\log^3(4/3),\quad
 A=\tfrac43+\mu d,\quad V=\tfrac49(1-\mu\log2)^2+\sigma^2d .
\]

* For every \(B<\infty\), every eligible mark \(N\not\equiv2\bmod3\) with \(|\log N-dn|\le B\sqrt n\) receives **unnormalized** mass at least \(c_{I,B}/(N\sqrt n)\) for all sufficiently large \(n\). Equation (2) gives a total-variation approximation to the full discrete row, retaining its clock lattice.
* After landing, let \(\tau_*(N)\) be the time to the minimum of its ensuing ordinary orbit. The total date \(D+\tau_*(N)\) has centering \(An\), variance scaling \(Vn\) and standard normal limit. Its normalized limit is independent of this ordinary minimum. The entire distribution of that minimum converges in total variation to the ordinary natural-density minimum law.
* For \(k\ge2\) independent samples at the **same grade**, put \(H_n=\lfloor An+u\sqrt{Vn}\rfloor\). At this one absolute date, measured from the original rational sources, the probability that all actual values agree tends to
  \[
                  \Phi(u)^k\sum_C d_C^k/P_C^{\,k-1},                   \tag{1}
  \]
  where the sum is over genuine positive cycles of the shortcut map, with basin density \(d_C\) and least period \(P_C\). Thus universal positive-integer convergence is equivalent to a two-sample probability tending to \(1/8\) at \(u=0\). The probability of eventual same-date merger has the same limit with the factor \(\Phi(u)^k\) omitted.
* For **one fixed aperiodic positive integer \(x\)** and any \(r_j\to\infty\), a positive fraction \(d_{C(x)}\) of ordinary sources sampled through *any* independent \(X_j\to\infty\) actually visit \(T^{r_j}x\). Their true hitting clocks, conditional on such a visit, are asymptotically Gaussian with centering \(r_j+\mu\log X_j\) and variance scaling \(\sigma^2\log X_j\). Both conclusions extend to every full first-landing cohort of a fixed real interval along that orbit and to the single-grade reciprocal rows, as made precise below.

The first claim uses the physical word dictionary and elementary geometric sums. The others consume Leen's proper minimum and shortcut clock laws, including the fixed arithmetic-progression formulation, and the [ordinary phase calculation](SYNCHRONOUS_PHASE_DISPERSION.md). The positive-predecessor and cutoff criteria use Mazur's theorem. These inputs, normalization and prior component-clock results are identified there. The previous [fixed-target renewal result](FIXED_TARGET_RENEWAL_PROFILE.md) sums over all grades; the lower bound here holds at each central grade and each eligible integer individually.

**Prior scope.** Wren observed that predecessor sets are nested along a divergent forward orbit and distinguished a later ascent from the initial descent. Valbuena's occupation theorem factors first-hit weights through a fixed ordinary ancestor and gives a strict extra lower bound in the presence of a divergent orbit. His inverse-clock theorem gives the almost sure growth rate of an actual backwards Syracuse path under a specific probability law at a fixed root. Leen supplies the natural-density clock law for every fixed shortcut target and the joint minimum law on fixed progressions. Equation (6) below uses these minimum and phase observations for a moving *forward* state, with the observation cutoff and forward date allowed to tend to infinity independently. Equation (1) samples two or more independent positive rationals at a prescribed ternary denominator grade, uses each source's own reciprocal landing weight, and compares their physical values at one common *absolute* time. [Wren, November 20, original post and re-ascent discussion](https://rstation.ai/r/collatz/posts/95) · [Valbuena, original manuscript, divergent-excess and inverse-height-clock theorems](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/tao-basin-densities.tex) · [Leen, shortcut minimum, progression and fixed-target laws](https://doi.org/10.5281/zenodo.23269488)

## The geometric bridge at a single integer clock

Let \(e_i\) be independent positive geometrically distributed times with \(\Pr(e_i=j)=3\cdot4^{-j}\), and let \(D_n=\sum_{i=1}^n e_i,\ L=3^n/2^{D_n}\). Write
\[
 Z_n=\tfrac12\sum_{i=1}^n\frac{2^{e_1+\cdots+e_i}}{3^i},\qquad
 Z=\lim_n Z_n .
\]
The positive drift \(d\) gives almost sure finiteness of \(Z\). For \(0<p<1\), \(r_p=\mathbb E(2^{e_1}/3)^p<1\), since the multiplier has expectation one and is nonconstant. The physical word through the \(n\)-th odd is exponentially close in total variation to this tilted geometric sequence, by the [whole-word row law](RECIPROCAL_LANDING_WORDS.md). Given its actual word, its marks are exactly uniform among the eligible integers in \(L(I+Z_n)\). Let \(U\) be uniform on \(I\); let \(D_n'\) have the law of \(D_n\), independent of \(U,Z\). Let \(\mathcal R\) round to a nearest integer congruent to 0 or 1 modulo 3, with arbitrary tie convention. Then
\[
 d_{\rm TV}\bigl(\mathcal L(D,N),\
        \mathcal L(D_n',\,\mathcal R((3^n/2^{D_n'})(U+Z)))\bigr)\to0. \tag{2}
\]
Rounding here uses all eligible integers on the real line. The probability of a nonpositive proxy tends to zero.

Indeed the central bridge \(D_n=t\), \(|t-4n/3|\le B\sqrt n\), makes each fixed initial \(k\)-tuple of gaps tend uniformly in total variation to its unconditioned law. For a fixed tuple of total \(s\), divide the local negative-binomial mass at \(D_{n-k}=t-s\) by that at \(D_n=t\). Stirling's formula shows the ratio tends to one uniformly in the central band. The sum of the probabilities of a sufficiently large finite collection of tuples is close to one, which gives the total-variation statement. Moreover, uniformly in the same \(t\),
\[
 \mathbb E((Z_n-Z_k)^p\mid D_n=t)
             \ll_B \sum_{i>k} r_p^i +\sqrt n\sum_{i>n/2}r_p^i.          \tag{3}
\]
Here \(k\le n\). For each \(i\le n/2\) first condition on its initial gaps and bound the residual point probability by \(O(1/\sqrt n)\), uniformly over the required integer. The supremum bound follows from the negative-binomial mode and Stirling. For \(i>n/2\) use one. Divide by the central point probability \(\gg_B1/\sqrt n\) and use subadditivity of the \(p\)-power. The corresponding unconditional infinite series after \(k\) has \(p\)-moment \(O(r_p^k)\). Thus these bridge laws of \(Z_n\) converge weakly to \(Z\), uniformly for all such central \(t\).

Adding independent uniform \(U\) upgrades the bridge convergence to total variation: on a coupling with shifts converging in probability, translations of uniform measure through a displacement \(h\) differ in total variation by at most \(\min(1,|h|/|I|)\). The subsequence version of the preceding uniform bridge statement suffices. For each word, rounding continuous uniform measure on \(L(I+Z_n)\) gives uniform eligible marks up to \(O_I(1/L)\) in total variation for \(L\ge1\); the consecutive eligible gaps alternate between one and two, so every complete Voronoi cell has length \(3/2\). The central band has \(L\to\infty\) uniformly. Compare the physical word to the tilted one, perform the rounding and bridge replacement there, then let \(B\) grow using the ordinary central limit theorem. This proves (2).

For the single-atom **lower** bound use the exact inverse-word identity directly. The tilt of the original geometric weight \(2^{-t}\) through a word is \(L\), and reversal of the iid word preserves the conditional bridge. For \(b_t=N2^t/3^n\), the eligible mass \(G_{n,I}(N)\) satisfies
\[
 N G_{n,I}(N)=\sum_t b_t\,\Pr(D_n=t)\Pr(Z_n\in b_t-I\mid D_n=t).
                                                                        \tag{4}
\]
The support of \(Z\) contains \([1,\infty)\). In fact its independent recursion uses maps \(f_e(z)=2^e(z+1/2)/3\); every image of a support point is again in the support. Iterating \(f_1\) shows its fixed point 1 is in the support. Consequently every \(1+(2/3)^j(2^{e-1}-1)=f_1^j f_e(1)\) belongs. These points are dense in \([1,\infty)\): at any prescribed positive excess over one choose unbounded \(j,e\) with \(2^{e-1}(2/3)^j\) tending to that excess, by irrationality of \(\log_2(3/2)\), then the subtracted \((2/3)^j\) vanishes.

Choose a fixed \(K>b+2\), and take a \(t\) with \(K\le b_t\le2K\), possible by doubling. At the indicated central marks this \(t\) is in a fixed central clock band, so \(\Pr(D_n=t)\gg_{B,I}1/\sqrt n\). All intervals \(v-I\) for \(v\in[K,2K]\) have positive \(Z\)-probability; shrinking locally to interior intervals and using a finite subcover gives a uniform positive bridge lower bound by (3) and the open-set inequality for weak convergence. Retain this single term in (4). This supplies the claimed pointwise lower bound; a total-variation approximation alone would not imply it.

## The subsequent ordinary minimum and common date

For a word, the eligible marks form the two progressions in \(L(a+Z_n,b+Z_n)\). With probability tending to one \(L\to\infty\), and \(Z_n\) is tight by the word comparison and the \(p\)-moment bound. Uniformly for \(0\le z\le B\), source-uniform statistics on these intervals inherit any joint ordinary natural-density limit valid on each fixed progression \(0,1\bmod3\). For a bounded test with a limiting expectation, subtract its two cumulative progression sums at the endpoints and divide by \(2|I|L/3+O(1)\). Their remainders are \(o_B(L)\) uniformly: split endpoints below \(\varepsilon L\) off by their size and use the ordinary limit uniformly beyond \(\varepsilon L\). This also transfers clocks normalized using \(\log N\) to clocks normalized using \(\log L\), since exceptionally small \(N/L\) have arbitrarily small probability and large \(N/L\) have been truncated. In fact \(Z_n\ge1/3\) for a nonempty word. The proof works for fixed thresholds of a continuous limiting CDF, uniformly on compact sets of varying thresholds by monotonicity.

It follows that, together with the entire word's normalized landing time, the subsequent normalized minimum time and minimum satisfy
\[
 \left(\frac{D-4n/3}{(2/3)\sqrt n},
       \frac{\tau_*(N)-\mu\log L}{\sigma\sqrt{\log L}},m(N)\right)
       \ \Longrightarrow\ (G_1,G_2,M)
\]
with mutually independent standard normals \(G_1,G_2\) and the ordinary discrete minimum law \(M\). Indeed condition on the physical word on a compact truncation, apply the preceding uniform ordinary limit, and integrate bounded tests. On the negligible event \(\log L\le0\) define the second coordinate arbitrarily. Tightness on a countable discrete set also gives total variation for the minimum marginal. The exact identity \(\log L=dn-(D-4n/3)\log2\) gives the asserted centering and variance for \(D+\tau_*(N)\). Here the ordinary clock begins at first integral landing; the minimum is over its ordinary future only. [Leen, original shortcut minimum and progression law](https://doi.org/10.5281/zenodo.23269488)

Fix a genuine cycle \(C\). Conditional on its component, replace \(\tau_*(N)\) by its first cycle-entry time \(t_C(N)\) at \(O_P(1)\) cost as in [the phase calculation](SYNCHRONOUS_PHASE_DISPERSION.md). The natural subprobability having entered that cycle by a specified centered ordinary clock and with any one of its \(P_C\) phases is asymptotically \(d_C\Phi(s)/P_C\). It holds on each fixed source residue modulo three: the neighboring-success proof for the threshold submeasures in that calculation proves their residue independence in total variation. Subtraction of endpoint counts applies also to the threshold \(h=\mu\log L+\sigma s\sqrt{\log L}\), because replacing \(L\) with either positive comparable endpoint changes \(s\) by \(o(1)\); a negligible small endpoint is bounded by its source mass. The same uniform statement holds for a bounded varying \(s\).

Beyond landing, the absolute-date phase of a sampled rational is \(S^{-D}c(N)\); at absolute date \(H\ge D\) its class is \(S^H S^{-D}c(N)\). Given a word, shifting its finitely many equidistributed cycle phases by the known \(D\) permutes them. Apply the last paragraph with remaining clock \(H_n-D\). The two independent Gaussian fluctuations already computed give single-sample phase and entry probability \(d_C\Phi(u)/P_C+o(1)\) for each absolute phase. Also the single-sample absolute date \(D+t_C(N)\) restricted to this basin, normalized with \(A,V\), has continuous finite-measure Gaussian limit \(d_C\,d\Phi\). Its largest atom tends to zero. Equality off the cycle after all samples have landed forces the same future cycle-entry date whenever they belong to this fixed cyclic component. The chance that some sampled source has not yet landed is \(o(1)\) since \(A>4/3\).

For completeness the long-period and infinite tail remains negligible even though the phases shift by different landing dates. Any one-phase-per-component selector in that tail pulls back under each \(S^{-D}\) to another selector. For each word with \(Z_n\le B\) its mass on the eligible interval is at most \(O_{I,B}(1)\) times its unrestricted empirical mass through \(\lceil L(b+B)\rceil\). The long-period bound (4) of the phase calculation is uniform in the choices of phases and applies to every sufficiently large cutoff. Truncate \(Z_n\), use \(L\to\infty\) in probability, then send the period cutoff and truncation to infinity in that order. The summed largest absolute-phase mass in this tail vanishes. Independence gives (1) exactly as in the ordinary case, including the eventual limit without the cutoff. In particular the unknown cycle weights have been transported through the full rational-to-ordinary trajectory.

## A moving target on one actual aperiodic orbit

Write \(C_x\) for the entire ordinary asynchronous component of a fixed aperiodic \(x\). Number its genuine phase classes by \(\phi:C_x\to\mathbb Z\), with \(\phi(x)=0\) and \(\phi(Ty)=\phi(y)+1\). The numbering is single-valued by the phase quotient and absence of cycles. Since \(m(y)\) lies in that component whenever \(y\) does,
\[
               \phi(y)=\phi(m(y))-\tau_*(y),\qquad y\in C_x.             \tag{5}
\]
The discrete minimum is tight; on any fixed finite set of possible minima in \(C_x\) the first term is bounded. Its basin density \(d_{C_x}=\Pr(M\in C_x)\) is positive: Mazur's shortcut predecessor implication for any fixed post-odd state on this orbit gives a positive lower bound.

For any \(r_j\to\infty\) and \(X_j\to\infty\), let \(y\) be uniform through \(X_j\) and \(\tau_z(y)\) the first hitting time of \(z=T^{r_j}x\), infinite on nonvisits. Then for every real \(u\),
\[
 \Pr\{\tau_z(y)\le r_j+\mu\log X_j+\sigma u\sqrt{\log X_j}\}
                  \ \longrightarrow\ d_{C_x}\Phi(u),\qquad
 \Pr\{\tau_z(y)<\infty\}\longrightarrow d_{C_x}.                        \tag{6}
\]
For any fixed finite set \(F\) of possible minima in \(C_x\), each \(m\in F\) eventually meets the orbit of \(x\) and hence visits every \(T^{r_j}x\) for large \(j\), uniformly over \(F\). Except for the vanishing minimum tail as \(F\) exhausts the component, every sampled member of \(C_x\) therefore visits this moving target. A true visit has exact date \(r_j-\phi(y)\), by (5) and nonrepetition. The ordinary minimum clock limit gives (6). This argument allows arbitrary relative growth rates of \(r_j\) and \(X_j\).

The same statement holds in any fixed input progression and any real interval of length comparable to \(X_j\) with endpoints bounded by a fixed multiple of \(X_j\), by the uniform subtraction argument. In particular take \(r_j=t_n\), the date just after the \(n\)-th odd departure of \(x\), and \(X_j=z_n=T^{t_n}x\). For **each** fixed nonempty bounded positive real source interval, the actual first-landing cohort specified by that native prefix is exactly the two admissible residues in \(L_n(I+A_n)\); \(L_n\asymp_x z_n\) and \(A_n\to A_x\). Thus (6) holds as stated at every large grade for its uniform cohort. These eventual visitors genuinely hit the distinguished moving state. No visitor arriving a positive number of steps later can also be its equal-date partner, by aperiodicity. [Exact cohort](FIXED_ORDINARY_LANDING_FIBRES.md) · [Shrinking intervals and subtypical clocks](ORDINARY_PREDECESSORS_IN_SHORT_WINDOWS.md)

Finally sample a reciprocal source at grade \(n\) as above, let \(r_n\to\infty\) be arbitrary, and count the entire clock from this rational's start. The same argument using the uniform proper minimum law conditional on its landing word gives true hit probability tending to \(d_{C_x}\) and
\[
 \Pr\{\text{actual visit to }T^{r_n}x
           \text{ by }r_n+An+u\sqrt{Vn}\}\longrightarrow d_{C_x}\Phi(u).
\]
Before first integer landing the rational cannot equal any such ordinary mark. On visiting paths the exact total date is \(D+r_n-\phi(N)\). Equations (5) and the independent two-clock limit prove the assertion. All moving-target conclusions have an aperiodic-source hypothesis and give no example of such a positive integer.
