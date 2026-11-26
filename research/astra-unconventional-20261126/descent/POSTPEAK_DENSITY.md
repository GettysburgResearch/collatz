# Same-component descent after the Mersenne peaks

**Proposed written consequence of the earlier affine-pair absorption estimate.** Fix \(a\ge1\). On every odd-modulus arithmetic progression of the hard indices, a density-one set of parents \(z_m=(2^{m+7}-271)/81,\ m=11+162j\) share their lower component with the strictly smaller canonical parent \(z_{m-162a}\). Every supplied upper certificate transfers with **the same odd count** and \(162a\) fewer clocks. The next comparison keeps the original index \(j\) throughout. Its exceptional set can contain particular prescribed indices. The absorption estimate and the method for exponential parameters are prior written results. [Earlier absorption and exponential parameter theorem](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [Its oriented-process proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

## Uniform count inside an arbitrary ternary address

Choose an odd integer \(Q\ge1\) and \(J\ge 8\) consecutive nonnegative values of \(\ell\) with \(j=b+Q\ell\ge a\). Put \(h=\lfloor\log_2 J\rfloor\), \(m'=m-162a\), \(s=162a\). For all but at most
\[
    C J \min\{1,(1+s)/\sqrt{\log(2J)}\}
\]
of these ordinary indices, there exists \(i\le h\) satisfying
\[
 T^{7+m'+i}(z_{m'})=T^{7+m+i}(z_m),\qquad
 2^{162a}z_{m'}<z_m.
\]
The constant is independent of the exponent interval, \(a,b,Q\). In particular, \(Q\) may be any power of three. Uniformity also permits \(a=o(\sqrt{\log J})\) tending to infinity.

Indeed, the lower parents reach \(2^{m'}-1,2^m-1\) after seven clocks and then \(3^{m'}-1,3^m-1\) after their respective all-odd runs. The latter pair is precisely
\[
     X=3^{m'}-1,\qquad 3^s X+d,\qquad d=3^s-1.
\]
The cited estimate for conditional fair binary digits bounds the number of nonabsorbed source residues modulo \(2^h\) by \(C_0\,2^h(1+s)/\sqrt h\) because \(0<d/3^s<1\). Absorption means that the two affine expressions agree identically on that residue, so it gives a genuine ordinary merger. As \(\ell\) varies, \(3^{m'}\) multiplies by \(3^{162Q}\). Since \(Q\) is odd, \(v_2(3^{162Q}-1)=3\). The order of this multiplier modulo \(2^h\) is exactly \(2^{h-3}\), by successive squaring. Thus one period visits every residue \(X\equiv2\bmod8\) once. An interval of \(J\) exponents is contained in at most 16 periods. The full binary upper count applies to each one, giving the result. Direct subtraction gives \(81(z_m-2^s z_{m'})=271(2^s-1)>0\).

## Physical transfer of the upper certificate

At clock nine the two upper trajectories are \(2^{m-2}\) and \(2^{m'-2}\), respectively, each having used three odd departures. The former reaches the latter after exactly \(s\) even steps. Any hit \(T^H(3z_m)=1\) has \(H\ge9+s\), since its orbit at that clock is \(2^{m'-2}>2\) and the orbit of 1 stays in \(\{1,2\}\). Appending that identical suffix therefore gives
\[
  T^{H-s}(3z_{m'})=1,\qquad Q_{H-s}(3z_{m'})=Q_H(3z_m).
\]
Whenever the displayed lower meeting occurs, badness of \(z_m\) would make the smaller canonical \(z_{m'}\) bad. Such a parent cannot be the least canonical reverse disagreement. This is an exclusion for typical indices on each specified progression. The comparison with a smaller parent alone does not prove either lower orbit reaches 1.

The ternary signed seeds constrain an integral source before its peak. This argument instead relates actual forward orbits after both peaks. Consequently the exceptional fraction tends to zero even inside any one exponent class missed by the small-coefficient signed-seed bound. The underlying probabilistic absorption theorem is a prior written input. The signed-family Lean files certify separate algebraic trajectories. [Signed source theorem](SIGNED_MERSENNE.md) · [Signed-seed count](SIGNED_COVERAGE.md)
