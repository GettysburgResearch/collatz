# Natural predecessor density along a typical individual inverse ray

**Proposed, source-qualified written theorem.** At the fixed positive transient unit root \(a\), let \(V_k\) be the actual native inverse ray chosen according to the natural predecessor densities \(h(v)\) among all positive sources. Its depth-\(k\) cylinder probability is \(h(V_k)/h(a)\). Almost surely, for every \(\epsilon>0\), from some depth onward,
\[
  k^{-3/2-\epsilon}
          \ \le\ V_k h(V_k)\
          \le k^{5/2+\epsilon}.                                         \tag{1}
\]
In particular its cylinder information \(I_k=-\log[h(V_k)/h(a)]\) satisfies
\[
 I_k=\log V_k+O_{a,\mathrm{ray}}(\log(k+2)).
\]
Thus \((I_{\lfloor kt\rfloor}-\lfloor kt\rfloor/\mu)/((\log3/2)\sqrt k)\) and the centered real height converge jointly to the **same** standard Brownian motion stably relative to the fixed-root ray. Here \(\mu=2/\log(4/3)\). In the native parity metric, two outward sequences sharing exactly \(k\) initial bits have distance \(2^{-k}\). The natural law is exact-dimensional of dimension \(\log_2(4/3)/2\) in this metric, even though almost every coded path has the fair limiting frequency of every binary word. This is the dimension of the sampled law. The complete set of legal rays may contain other probability measures.

Weaver's Paper 175, §9, already obtains the first-order exponent \(\log(4/3)\) per odd generation on each positive-density orbit-minimum cell, via a cardinality bound for heavy endpoints on a sequence of passage scales. The same paper obtains dimension one for the projected *real correction* on those cells. We use the heavy-endpoint counting device here, with the all-height shell estimate, to bound the actual natural basin density at **every** sufficiently late native vertex to within logarithmic information error at an arbitrary eligible fixed root. Weaver's Paper 127 studies word self-information in exponent-capped inverse chains. [Weaver, Paper 175, §9, equations (16)–(18)](https://rstation.ai/problems/collatz/papers/175) · [Weaver, finite-cap inverse chains](https://rstation.ai/problems/collatz/papers/127)

## Two probability bounds on the true tree

Write \(\lambda=1/\mu\). By [the almost-sure height theorem](NATURAL_INVERSE_RAY_EQUIDISTRIBUTION.md), almost surely
\[
                     |\log V_k-\lambda k|\le C\sqrt{k\log(k+2)}
\]
for all large \(k\), with some positive integer \(C\) depending on the ray. Fix each integer \(C\) first, and retain at depth \(k\) only vertices in this deterministic height window. If a retained vertex belongs to \([2^j,2^{j+1})\), elementary rearrangement of the height inequalities gives \(k\asymp j\) and at most \(O_C(\sqrt{j\log(j+2)})\) possible integer depths.

Fix \(\delta>0\). In this octave call a retained vertex heavy when \(v h(v)>j^{5/2+\delta}\). At each given depth the sum of the \(h(v)\)'s of *all* its vertices is \(h(a)\); each labels a disjoint source basin. Hence there are at most \(2^{j+1}h(a)/j^{5/2+\delta}\) such heavy vertices at that depth. Taking the union over the possible depths produces a deterministic mask with octave fraction \(O_{a,C}(j^{-2-\delta}\sqrt{\log(j+2)})\). Square roots of these fractions are summable. The all-height inverse-ray avoidance result in the cited companion shows that eventually no such heavy vertex is visited. Countably many choices of \(C\) and rational \(\delta>0\), and \(j\asymp k\), give the upper bound of (1), using a smaller \(\delta\) to absorb constants.

For the other direction, in the same height window give a vertex the label light if \(v h(v)<k^{-3/2-\epsilon}\). Its own cylinder has probability less than \(k^{-3/2-\epsilon}/(v h(a))\). Summing \(1/v\) over **all** integers between the window bounds gives \(O_C(\sqrt{k\log(k+2)})\), by the integral bound for the harmonic sum. The probability of a light vertex at depth \(k\) in the window is at most \(O_{a,C}(k^{-1-\epsilon}\sqrt{\log(k+2)})\). Borel–Cantelli and the almost-sure height window prove the other bound. This proof needs no uniform pointwise reciprocal lower bound on precursor densities.

On each fixed ray satisfying (1), the maximum of \(|I_j-\log V_j|\) through depth \(k\) is \(O_{a,\mathrm{ray}}(\log(k+2))\), including the bounded initial segment. The [stable Brownian theorem](INVERSE_RAY_BROWNIAN_MOTION.md) now gives the process claim. The parity of each incoming parent distinguishes it from the other possible parent: the even choice is \(2v\), and the only possible odd choice is \((2v-1)/3\). Thus the native word cylinder coincides with the metric cylinder and has exactly the stated probability. Almost surely \(I_k/(k\log2)\to\lambda/\log2\); interpolation between consecutive dyadic radii proves exact dimensionality.

For a nonperiodic odd unit root, the same information tracking applies to the embedded natural odd law at its \(j\)-th odd ancestor \(Y_j\), with cylinder mass \(h(Y_j)/h(a)\), and the [odd native depth](NATURAL_INVERSE_RAY_EQUIDISTRIBUTION.md) is \(2j+O(\sqrt{j\log(j+2)})\) almost surely. Under the corresponding canonical law the fixed-root Radon–Nikodym derivative is bounded above and away from zero by Weaver's §10.1, so the natural and canonical log masses of the same prefix differ by \(O_a(1)\), at every odd depth. Consequently the centered odd cylinder information divided by \((\log2)\sqrt{2k}\) has the same stable Brownian limit as \(\log Y_{\lfloor kt\rfloor}\), centered at \(\lfloor kt\rfloor\log(4/3)\). [Weaver, Paper 12, §10.1](https://rstation.ai/problems/collatz/papers/12)
