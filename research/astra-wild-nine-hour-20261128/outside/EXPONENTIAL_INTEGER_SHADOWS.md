# When exponentially accurate integer observations recover a single true source

**Proposed written theorem.** Fix one positive real start and one infinite binary script. The real states use the prescribed affine branches
\[
r_{t+1}=F_{e_t}(r_t),\qquad F_0(r)=r/2,\quad F_1(r)=(3r+1)/2.
\]
Assume \(r_t\to\infty\). For \(\sigma>0\), write \(G_\sigma=\{t:\|r_t\|_{\mathbb R/\mathbb Z}\le e^{-\sigma t}\}\).

1. If \(G_\sigma\) contains an infinite sequence \(t_j\) with \(t_{j+1}/t_j\to1\), the script executes a genuine positive ordinary integer orbit from some finite time onward. This holds in particular if \(G_\sigma\) contains **any set of positive natural density**. If the starting real number is an integer, the entire script was its true parity word.
2. Suppose the start is an ordinary integer and the script makes a wrong choice. Put \(L=\log2\). For \(0<\sigma\le L\), without a speed hypothesis,
   \[
      \overline d(G_\sigma)\le1-(\sigma/\log3)^2 .
   \]
   If \(\log r_t/t\to g\ge0\), the sharper bound is
   \[
      \overline d(G_\sigma)\le1-\frac{\sigma(g+\sigma)}{L(L+g)}.       \tag{1}
   \]
   In particular the full-denominator precision \(2^{-t}\) has upper density zero when the speed exists. For \(\sigma>L\) there are only finitely many such dates. For an algebraic irrational initial real the displayed bounds through \(\sigma=L\) still apply.
3. Nevertheless a wrong script at **any fixed positive ordinary start** can escape with positive lower real exponential growth and satisfy \(\underline d(G_{L/25})>0\). It can follow any requested true prefix before its first wrong letter. On a subset of positive lower density, the nearest integers lie on long *genuine* positive integer segments and agree with the simulated profinite state at every fixed modulus eventually. The nearest integers there even approach the signed fixed point \(-1\) profinitely. [Explicit construction](POSITIVE_LOWER_DENSITY_SHADOWS.md)

Thus positive lower density and positive natural density give genuinely different tests on the single fixed positive source. In the constructed example no subset of its good dates has positive natural density. Nothing here supplies the positive-real escape with regularly spaced accurate returns required to construct a genuine counterexample.

## Integer transport between observations

For a word of length \(d=v-u\) with \(s\) ones, write \(2^d r_v=3^s r_u+C\), with integral \(C\). At good dates take nearest integers \(z_u,z_v\) and signed errors \(h_t=r_t-z_t\). If
\[
                       2^d|h_v|+3^s|h_u|<1,                            \tag{2}
\]
the integer \(2^dz_v-3^sz_u-C\) is zero. All intermediate branches from \(z_u\) are physical. Indeed a wrong branch on an integer creates reduced denominator two, and each subsequent prescribed branch doubles the reduced denominator of a nonintegral dyadic rational. Also \(h_v=3^s2^{-d}h_u\). Call two consecutive good observations linked when that integer vanishes. Condition (2) is sufficient, and all links carry the same rounded orbit by composition.

At an escaping positive real state the log correction for step \(t\) is \(b_t=e_t\log(1+1/(3r_t))\to0\). Thus
\[
        \log(3^s2^{-d})=\log r_v-\log r_u-\sum_{t=u}^{v-1}b_t .      \tag{3}
\]
If \(v/u\to1\), then \(d=o(u)\), so (2) holds for all sufficiently late consecutive observations from the stated sequence. With fixed first linked date \(u\), equation (3) gives \(\log(3^s2^{-d})\ge-o(v)-O_u(1)\) at its unbounded linked endpoints. A fixed nonzero \(h_u\) would contradict \(|h_v|\le e^{-\sigma v}\). Hence \(r_u=z_u\), and every future branch is physical. When \(r_0\) was an integer, reduced denominators also force every branch before \(u\) to have been physical. For a set of positive natural density \(\delta\), its ordered elements satisfy \(t_j\sim j/\delta\), verifying the ratio hypothesis. In fact the same proof works whenever the successive ratios have limit superior strictly less than \(1+\sigma/\log3\): the exponent in each summand of (2) is then at most a fixed negative multiple of \(u\). No bound on the total reciprocal sum is used.

## Counting the missing intervals

After a first wrong letter at index \(N\), the reduced denominator of \(r_u\) is exactly \(2^{u-N}\) for \(u>N\). In particular every roundoff is nonzero and \(|h_u|\ge 2^{-u}\). For an algebraic irrational \(r_0\) the substitute is \(|h_u|\ge\exp(-Lu-o(u))\). Indeed \(2^u h_u=3^{s_u}r_0-j_u\) for an integer \(j_u\), where \(s_u\) counts the preceding ones. Ridout's restricted-denominator approximation theorem gives \(\|3^k r_0\|\ge\exp(-o(k))\) in the logarithmic sense: for every \(\eta>0\) it eventually exceeds \(e^{-\eta k}\). Apply its approximation bound to denominators that are powers of three, reducing the fraction first if necessary. Bounded values of \(k\) have a positive minimum distance. This is the only external theorem in the algebraic extension. [Ridout, *Rational approximations to algebraic numbers*, Mathematika 4 (1957), 125–131](https://doi.org/10.1112/S0025579300001182)

Partition the good dates into maximal linked clusters. Part 1's fixed-start argument rules out an infinitely long linked cluster, even without a gap assumption within that cluster. If there are infinitely many good dates, write \(u,v\) for the first and last good dates of one cluster and \(w\) for the end of the preceding cluster. The following two asymptotic inequalities hold:
\[
                        u/v\ge a-o(1),\qquad w/u\le b+o(1).           \tag{4}
\]

At speed \(g\), use \(a=(g+\sigma)/(L+g)\), \(b=(L+g)/(L+g+\sigma)\). Along the linked cluster, \(|h_v|=|h_u|\exp(g(v-u)+o(v))\) by (3). Comparing the lower bound on \(|h_u|\) with the good bound on \(|h_v|\) proves the first inequality. At the preceding break the integer transport fails. If \(u-w\le (\sigma/(L+g)-\eta)w\) for any fixed \(\eta>0\), (3) gives \(\log 3^{s_{w:u}}=(L+g)(u-w)+o(w)\), while \(L(u-w)\le( L+g)(u-w)\). Both summands in (2) tend to zero, so the break would be impossible. This proves the second inequality.

Without a speed use \(a=\sigma/\log3,\ b=\log3/(\log3+\sigma)\). Since \(r_u+1\le(3/2)^u(r_0+1)\) and \(r_v\ge1\) eventually, (3) bounds the logarithm of the cluster slope below by \(-u\log(3/2)-o(v)-O(1)\). This proves the first inequality. The second follows from (2) using \(3^s,2^d\le3^d\).

For fixed small \(\eta>0\), every sufficiently late cluster contains at most \(u((a-\eta)^{-1}-1)+1\) good dates, while its preceding missing gap contributes at least \(u(1-b-\eta)-1\) distinct bad dates. These gaps are disjoint. The same charge applies to any truncation at a good date inside its cluster, since the number of good dates can only decrease. The end dates of the clusters grow at least geometrically by (4), so endpoint terms cost \(o(T)\) through time \(T\). After summing, dividing, and letting \(\eta\downarrow0\), the upper good fraction is at most
\[
                   \frac{1-a}{1-ab}.
\]
At the endpoint \(a=1\), the same argument gives zero by the limit. Substitution yields the two displayed bounds. Also the bad gaps themselves force \(\underline d(G_\sigma)\le b\,\overline d(G_\sigma)\) when visits are infinite: compare the counting ratios just after \(w\) and just before \(u\). A gap pattern with positive lower and distinct upper density remains possible.

## Relation to earlier approximation results

For a fixed geometric multiplier, estimates for the fractional parts of powers go back to Mahler and include Dubickas's nearest-integer bounds for prescribed rational powers. Here the two multipliers and the inhomogeneous terms vary along a controlled script. The integer recovered in (2) follows *all* the actual shortcut guards from its rounded source. No density conjecture about powers of \(3/2\) is used. [Mahler, original 1957 paper](https://carmamaths.org/resources/mahler/docs/135.pdf) · [Dubickas, *On the distance from a rational power to the nearest integer*](https://www.sciencedirect.com/science/article/pii/S0022314X0500168X)

PR212 bounds repeated templates for a physical integer input. PR215's affine predecessor-overlap theorem describes common ternary measures for inverse controls, and its rounded rotation tracks a cycle envelope. The earlier [affine denominator test](AFFINE_APPROXIMATION_AT_THE_DENOMINATOR.md) compared one finite word with one already-specified positive target and charged a true starting prefix. The results here allow the rounded targets to vary at every date, glue them into one physical tail exactly when the integer numerator vanishes, and count the mandatory gaps on any single escaping off-diagonal script. [PR212, overlapping periodic windows](https://github.com/GettysburgResearch/collatz/blob/36c64bdf5d3e7f13a0bd949a01c3a9d6371681ed/research/astra-global-20261128/broad/OVERLAPPING_PERIODIC_WINDOWS.md) · [PR215, affine classification](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md)
