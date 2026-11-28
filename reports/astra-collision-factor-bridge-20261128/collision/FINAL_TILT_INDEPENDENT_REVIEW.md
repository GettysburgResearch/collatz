# Independent review: near-fair tilt attempt

Reviewer: collision lower-bound lane. Reviewed UTC: 2026-11-28T11:38:14.889042+00:00.

Source: `research/astra-collision-factor-bridge-20261128/arithmetic/FINAL_TILT_ATTEMPT_LEDGER.md`.

SHA-256: `5221a3e4836da6f34d0ad533ee5d46b862a1bb94ba9b7af11ecd3313ff5d1def`.

**Scope and result: Sections 1–2 pass independent mathematical reconstruction.** This review certifies the stated finite/relative transfer calculation and the two small polynomial counterexamples. It certifies no moment-generating-function limit and no median selected-grade lower bound. The separate precritical evaluation and tilted-source literature discussion retain their own source reviews.

The likelihood identity follows by factoring the product of the two near-fair branch weights into their geometric mean and their ratio. Its displayed normalization and exponent parameter are exact. The seed and future word use the same moving bias, with the seed independent of the future. The full-conductor selector therefore produces the shifted ordinary source sum with the correct likelihood attached to each actual grade.

The shifted-window discrepancy has the stated one-sided overlap constant: both departing and arriving sums are nonnegative and bounded by the maximum likelihood times the number of replaced points, so their absolute difference is bounded by that same amount, not twice it. The maximum likelihood is bounded by exp(abs(lambda)*sqrt(h)). The stationary affine-series half-moment is uniformly finite in a fixed sufficiently small neighborhood of one-half, because its denominator is strictly positive there. At h of order log X, these facts give an absolute error tending to zero even after division by the rare selector scale. For a negative fixed tilt parameter, the exact first moment gives the stronger error stated in the note.

The final exponential moment retains its exact finite exponent parameter. Replacing that expectation by a Gaussian moment is not justified by weak convergence alone. Likewise the fair normalization of selector acceptance does not persist under biased word probabilities, and the binomial grade before selection does not determine its conditional law after selection.

The native three-step grade counts were reconstructed directly. For sources one through seven the grades are (2,1,2,1,1,2,3), giving the first polynomial. Sources eight and nine add grades zero and two, respectively, giving the second. The quadratic discriminant is negative in the first example. The normalized coefficients fail the stated log-concavity inequality in the second. These reject the specified all-scale polynomial shortcuts and make no claim against an asymptotic estimate.

A scalar tilted ternary regularity theorem is not, merely by its scalar statement, a joint real-window/full-conductor ordinary-diagonal estimate. No such import is made or endorsed by this review.
