# Dynamics checkpoint 2

The [moving-band argument](../../../research/astra-wild-nine-hour-20261128/dynamics/MOVING_BAND_ENERGY.md) gives a source-qualified written bound for the total spatial Fourier energy of a moving band. The argument is uniform in the original source cutoff, the bounded observable, and both unit branch twists. Root independently reconstructed its reduction from the signed native joint estimate and scalar counted-fusion estimate. Neither review re-proves the signed estimate's underlying physical-fibre theorem. Fixed-target positivity and existence of the visit-to-five density are external inputs. The conditional grade-cell corollary and square-wave computation are written deductions.

[SourceEnvelope.lean](../../../research/astra-wild-nine-hour-20261128/dynamics/SourceEnvelope.lean) states the finite ordinary identity with its numerator bound. For true source n, clock t and odd count q it supplies a nonnegative d with
\[
 2^t T^t(n)=3^q n+d,\qquad 3d+3^q\le 3^q2^t.
\]
Dividing and using the elementary logarithm inequality gives the source phase estimate in the written proof. The Fourier analysis, renewal, imported estimates and infinite-time consequences are separate from this finite kernel. Earlier proof attempts were rejected in the even-branch inequality. The current source replaces the remaining inferred nonnegativity with an explicit natural-number comparison. Fresh object replay in Lean 4.34.1 was started after rebuilding OrdinaryPhaseBound in a temporary module directory. Its status at this commit is pending under memory pressure. No successful local compilation of the new declaration is claimed in this interim receipt.

The project command `python -X utf8 -B tools/validate.py` reported `PASS checkout validation; not mathematical verification`. The open global step is a treatment of exact low-boundary data that could preclude the diffuse residual component variance which the genuine finitely defective observable retains.
