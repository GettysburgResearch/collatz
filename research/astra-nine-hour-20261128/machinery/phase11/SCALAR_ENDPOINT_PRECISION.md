# Rational enclosure of the existing scalar criterion endpoint

Leen states the upper tilt \(0.550024\) for finite-relative-entropy absolute continuity. Its scalar inequality actually holds through **0.550024419420**. The new digits below use the same criterion and the same linear branch of the same entropy envelope; they do not change the underlying mechanism. [Leen, tilted Syracuse laws, Theorem B and §4](https://doi.org/10.5281/zenodo.23268832) · [Prior certified interval](../phase4/EXTENDED_TILTED_INTERVAL.md)

Put \(c=(\log2)/(\theta\log3)\) and \(H=-\log\theta-(1-\theta)\log(1-\theta)/\theta\). In this range \(1<c<4/3\), so the scalar excess at its limiting cutoff is exactly
\[
 D(\theta)=H-\frac{\log2}{\theta}
              +\frac43\log2\,(c-1-\log c).
\]
A strict positive excess also holds at a slightly larger cutoff as required in Leen's theorem. Differentiation gives
\[
 \theta^2D'(\theta)=\log(2(1-\theta))
                     -\tfrac43(\log2)\theta(c-1)<0
\]
for \(1/2<\theta<\log2/\log3\) as long as the linear formula applies. At the rationals \(550024419420/10^{12}\) and \(550024419422/10^{12}\), directed evaluation in units \(2^{-80}\) gives respectively the lower bound \(429953158894\) and upper bound \(-1010136773638\) in those units. The criterion changes sign strictly between them. The check uses positive rational logarithms with outward rounding from the phase-four kernel. In evaluating \(c-1-\log c\) it uses monotonicity for \(c>1\). The associated actual-row consequences extend through the stated rational cutoff by the previously proved supplied-target transfer. [Directed integer verifier](check_scalar_endpoint.py)
