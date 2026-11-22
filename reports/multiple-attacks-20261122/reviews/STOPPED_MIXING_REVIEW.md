# Independent review of the stopped mixing interface

**Reviewed source:** `multiattack_inverse/STOPPED_MIXING_INTERFACE.md`.
**Frozen SHA-256:**
`504c4ac79a5df90a1e5dd53fe90ad919dceed6a5f7a6cf56b396a7c21ab057b7`.

**Verdict:** the actual-law stopped comparison (6), the clipped Haar
maximal bound (10), and the atomic-law limitation are sound in this
frozen revision. The proposed stopped correlation estimate (SM+) remains
explicitly open. No new Lean or Collatz-convergence claim is attached to
this review.

## Actual law and the positive-horizon martingale

The normalization distinction is essential. The finite density is
`D_t=P^t 1` for the full parent operator, whereas the harmonic Doob law
is supported on unit parents with `G>0`. For positive `j`, `D_j`
vanishes at nonunit parents, so

\[
\mathbb E_q^G\left[\frac{D_j(X_{k+1})}{G(X_{k+1})}
\mid\mathcal F_k\right]
=\frac{PD_j(X_k)}{G(X_k)}.
\]

This justifies `Z_k^(t)=D_(t-k)(X_k)/G(X_k)` through
`0<=k<=t-1`. It does not justify a final transition to `D_0=1`, whose
nonunit contributions need not vanish. The frozen version states the
correct restricted range and explicitly excludes that transition.

For `t>=s>=m>=1`, the chosen bounded stopping time
`tau wedge (s-m)` is at most `s-1`. Both martingales are therefore
stopped inside their valid ranges. Their normalized values are bounded
by `4chi` through the pinned every-ordinary-point comparison, so bounded
optional stopping has the required integrability.

On `tau<=s-m`, both remaining density indices are at least `m`.
At the actual contact endpoint, clipping in `F_(m,M)` is inactive,
and subtracting through `D_m` bounds their difference by `2F_(m,M)`.
On the complement, both normalized values lie in `[0,4chi]`, so their
absolute difference is at most `4chi`, not `8chi`. Taking expectations
and dropping the nonnegative indicator from the first term gives exactly

\[
\frac{|D_t(q)-D_s(q)|}{G(q)}
\le2\mathbb E_q^G\!left[
\frac{F_{m,M}(X_\tau)}{G(X_\tau)}\right]
+4\chi\Pr_q^G(\tau>s-m).
\]

The stopped endpoint sum in (3) also has the correct probability weight:
the Doob factors telescope to `omega_w G(x_w)/G(q)`. The denominator
`G(X_tau)` cannot be replaced by the reciprocal endpoint height.

## Haar maximal estimate

Density consistency makes `D_t` a martingale in the ternary cylinder
filtration under Haar probability. The uniform marginal `L^1` estimate
makes it Cauchy in `L^1`, hence supplies the stated integrable terminal
variable. Doob's weak `(1,1)` estimate applies to the absolute value of
`D_t-D_m`, first on finite horizons and then by increasing them.

For `epsilon=C_B m^(-B)<=4M`, integrating
`min(1,epsilon/u)` from zero to `4M` gives precisely
`epsilon(1+log(4M/epsilon))`. Taking a fixed exponent `B>A` absorbs
the logarithm and the finite initial range, proving (10). The supremum
over integer precisions is measurable, and its clipping is legitimate.

## Transfer and the remaining open statement

The stopped actual endpoint law is countably atomic on positive
integers. If an atom has mass `p>0`, its residue cylinder at precision
`t` has Haar measure `3^(-t)` and stopped-law mass at least `p`.
The quotient density is consequently at least `p3^t`. This rules out
a precision-independent bounded trace from Haar `L^1` for arbitrary
test functions. It does not disprove a special arithmetic estimate for
the particular maximal errors `F_(m,M)`.

The conditional summation following (SM+) is valid: deterministic
exponential height growth along actual inverse contacts makes the
inverse logarithmic powers summable, and the finitely many low-height
terms have bounded payoff. The strong Markov property and nonnegative
summation then give finite expected total endpoint error. This remains
conditional on (SM+) and says nothing about the ordinary duration of
the excursions.

The separate tail term in (6), the initial-entrance scope, and the
terminal last-contact measure are all retained in the final note.
The Haar estimate and almost-sure fixed-root contact therefore have
not been promoted to an unsupported uniform moving-root clock bound.
