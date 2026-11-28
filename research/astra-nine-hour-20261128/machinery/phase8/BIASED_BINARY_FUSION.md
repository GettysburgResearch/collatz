# Translation overlap of the biased binary source is exactly counted fusion

Let the physical shortcut be \(T(x)=x/2\) on even dyadic integers and \((3x+1)/2\) on odd ones. The first \(t\) parities of the successive states give a bijection between residues modulo \(2^t\) and binary words of length \(t\). Denote by \(\rho_\theta\) the pullback of iid Bernoulli parities of parameter \(0<\theta<1\). Put \(q=1-\theta\), \(F_t(x)=\sum_{j<t}(T^jx\bmod2)\). For an integer \(h\), let
\[
 C_h=\{x:\text{some }t\ge0\text{ has }T^t(x+h)=T^t x,\ F_t(x+h)=F_t(x)\}.
\]
These are cylinder events in their union: on an initial pair of words with equal counts, the two affine endpoint functions have the same slope, so equality at one input forces equality on the whole cylinder. Write \(\sigma_h(E)=\rho_\theta(E+h)\) on source-oriented sets. For \(\theta\ne1/2\), the maximal common submeasure of \(\sigma_h\) and \(\rho_\theta\) is exactly \(\rho_\theta|_{C_h}=\sigma_h|_{C_h}\). In particular their total variation distance in the probability convention is \(1-\rho_\theta(C_h)\).

Indeed, on the dyadic cylinder of depth \(t\) at \(x\) the likelihood ratio is
\[
 M_t(x)=\frac{\sigma_h(x+2^t\mathbb Z_2)}{\rho_\theta(x+2^t\mathbb Z_2)}
       =(\theta/q)^{F_t(x+h)-F_t(x)}.                                      \tag{1}
\]
This nonnegative likelihood-ratio martingale converges \(\rho_\theta\)-almost surely to the density of the absolutely continuous part of \(\sigma_h\) relative to \(\rho_\theta\). If its limit is finite and strictly positive and \(\theta/q\ne1\), the integer count difference is eventually a constant \(d\). Subsequent parity bits then coincide forever; injectivity of the full binary parity coding gives \(T^t(x+h)=T^tx\) from that date on. When \(d\ne0\), the two fixed word endpoint functions have distinct slopes, so for each finite pair this happens at at most one dyadic point. The binary source is atomless. The remaining possibility is counted fusion, on which the ratio eventually equals one. This proves the decomposition. The same proof covers every fixed \(h\in\mathbb Z_2\), with the same exceptional countable set for that \(h\).

For an ordinary nonzero integer \(h\), the overlap is positive. Choose a positive counted-fusion cylinder by the [canonical steering theorem](../phase7/DETERMINISTIC_COUNTED_FUSION.md), starting the pair with count gap zero and integer offset \(h\); the raw coordinate need not be initially odd. The probability of that cylinder is positive for every nondegenerate tilt. Also, the parity bits at index \(v_2(h)\) of \(x\) and \(x+h\) are opposite for every \(x\): their earlier parities agree and their initial difference loses exactly one power of two at each previous step. Testing that bit gives
\[
    |2\theta-1|\le\|\sigma_h-\rho_\theta\|_{\rm TV}<1\qquad(h\in\mathbb Z\setminus\{0\}).
\]
At \(\theta=1/2\) all translations preserve binary Haar, and the separate ordinary synchronization theorem gives \(\rho_{1/2}(C_h)=1\) for fixed integer \(h\). The disintegration for biased sources above comes from their exact finite likelihood ratios. It gives no uniform lower density of fusions among specified positive integer starts. [Leen, scalar pair absorption](https://doi.org/10.5281/zenodo.23268751) · [lean_assurance_lab, Paper 212, qualitative steering](https://rstation.ai/problems/collatz/papers/212)

There is a complete decision criterion for arbitrary dyadic translations:
\[
 \sigma_h\not\perp\rho_\theta \quad\Longleftrightarrow\quad h\in\mathbb Z[1/3]
 \qquad(h\in\mathbb Z_2,\ \theta\ne1/2).                               \tag{2}
\]
For necessity, put \(T^t(x)=(3^F x+D_u)/2^t\) on one word and use \(D_v\) for the translated word. Counted fusion gives \(3^F h=D_u-D_v\), both integer constants. For sufficiency write \(h=d/3^k\). Under *binary Haar* both points have infinitely many odd departures almost surely, by translation invariance and the parity bijection. Choose one finite pair of words of common length \(t\) with both counts at least \(k\). Interchange the pair if needed, replacing \(h\) by \(-h\), so the second count \(F'\) is at least the first \(F\). For endpoints \(z,z'\), the relation is \(z'=3^{F'-F}z+C\), with
\[
  C=(3^{F'} h+D_v-3^{F'-F}D_u)/2^t\in\mathbb Z.
\]
The numerator is an ordinary integer, and \(C\in\mathbb Z_2\) from the endpoint relation. As the unused binary input varies, \(z\) ranges over all \(\mathbb Z_2\), with \(z'\) forced by this relation. Apply finite canonical steering with already credited count gap \(F'-F\). Pulling the resulting finite cylinder back gives a positive-probability counted-fusion cylinder for the biased source, proving (2). This uses existence under Haar to choose a finite prefix only. The final cylinder itself has strictly positive mass under the given bias. For example, every translate by \(1/3^k\) has positive common mass, and every translate by \(1/5\) is singular.

## All two-adic affine maps

More generally let \(g(x)=a x+b\) with arbitrary \(a\in\mathbb Q_2^\times\), \(b\in\mathbb Q_2\), and set \(r=v_2(a)\). Extend \(\rho_\theta\) by zero outside \(\mathbb Z_2\), and use the source-oriented \(\sigma_g(E)=\rho_\theta(gE)\) on \(\mathbb Z_2\). For every biased parameter,
\[
  \sigma_g\not\perp\rho_\theta
   \quad\Longleftrightarrow\quad a=2^r3^k\ (k\in\mathbb Z),\qquad
                         b\in 2^{\min(r,0)}\mathbb Z[1/3].              \tag{3}
\]
When (3) holds, form the open set \(C_g\) of all finite aligned pairs of words, where \(gx\in\mathbb Z_2\) and, for some \(n\ge\max(0,-r)\),
\[
                T^{n+r}(gx)=T^n(x),\qquad F_{n+r}(gx)-F_n(x)=-k.
\]
Then the absolutely continuous part of \(\sigma_g\) is \(q^r(q/\theta)^k\rho_\theta|_{C_g}\). Thus the common mass is \(\min(1,q^r(q/\theta)^k)\rho_\theta(C_g)\). The operand orientation here keeps \(\rho_\theta\) on source space.

At a point with \(gx\in\mathbb Z_2\), the map sends its ball of depth \(n\) exactly onto the ball of depth \(n+r\) about \(gx\). The cylinder likelihood ratio is consequently \(q^r(\theta/q)^{F_{n+r}(gx)-F_n(x)}\). Elsewhere the numerator is eventually zero. A positive limiting density forces the count difference eventually constant; then the two aligned future states have the same full parity code. Equality of the two word endpoint functions on a positive-mass set of one word pair forces equality of slopes and offsets. With its counts denoted \(F,F'\), these give
\[
                  a=2^r3^{F-F'},\qquad 3^{F'}b=2^rD_u-D_v.
\]
There are just countably many pairs; when the slopes differ each has at most one possible solution. This proves necessity and the asserted density when matched.

For sufficiency first take \(r\ge0\), so \(b\in\mathbb Z[1/3]\). Binary Haar at \(x\) pushes to normalized Haar on the open ball \(b+2^r\mathbb Z_2\). Choose one finite pair of depths \(n,n+r\) with both counts arbitrarily large; such pairs exist since both marginal parity orbits see infinitely many ones almost surely. Set \(K=k+F'-F\). If \(K\ge0\), the endpoint pair satisfies \(z'=3^Kz+C\), where
\[
 C=(3^{F'}b+D_v-2^r3^K D_u)/2^{n+r}.
\]
The numerator is integral after choosing the counts large enough to clear the fixed ternary denominator of \(b\). The endpoints are dyadic integral, giving \(C\in\mathbb Z\). If \(K<0\), use the inverse formula with \(g^{-1}\), exchanging the endpoints: its translation has only a fixed power of three and a fixed power of two in its denominator. The coefficient on the other word now has \(3^{-K}\), so the normalized offset has only powers of two downstairs once \(F,F'\) are large, and dyadic integrality again makes it an ordinary integer. The endpoint of the lower-count canonical stream ranges freely over \(\mathbb Z_2\), since the two balls of the specified depths are carried bijectively onto each other by \(g\) and a word maps its ball onto \(\mathbb Z_2\). Use the [finite canonical steering theorem](../phase7/DETERMINISTIC_COUNTED_FUSION.md) with initial gap \(|K|\). Its successful finite word pulls back to a cylinder in \(C_g\). Finally \(r<0\) follows by inverting the entire transformation: the inverse slope has positive valuation and its translation \(-b/a\) belongs to \(\mathbb Z[1/3]\) exactly when \(b\in2^r\mathbb Z[1/3]\). Nonsingularity is unchanged by exchanging the two measures and applying the measurable bijection \(g\). In (3) the set of transformations with overlap need not be a group, since the two compact source supports must meet in each test.
