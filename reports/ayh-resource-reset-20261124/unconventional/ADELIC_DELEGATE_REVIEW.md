# Independent review performed by the ordinary-selector delegate

The reviews below concern two manuscripts written by the critical-geometry
delegate. SHA-256 identifies the local UTF-8 source at the final reread.
The Collatz conjecture and the cited research program's upstream analytic
theorems were outside the scope of these checks.

| Reviewed manuscript | SHA-256 | Scope |
| --- | --- | --- |
| Entry-edge gains | 049753c8b7923a32480389e715f3b581f85b3fdbc57472d5dff91b961edf5bb5 | Physical first-entry reconstruction in (1), translated short-clock bound in (3), corrected-height normalization and summability in (6)–(7) |
| Entry threshold | f63e020980fb30fe1711a3cb83aefca7da3475ba24e4426fee5e31348ecfe4c4 | The named-input implications for the convergence window, fixed-target Gaussian lower bound, and the small-coefficient moderate-deviation argument in (6) |

In the first manuscript I checked the marked-time cases on both sides of
the observation clock, including straddling a long halving run, the
uniqueness of the physical entry site along the expanded injective ray,
and the possible multiplicity of marked vertices from a single source.
I checked the affine range bound and entropy split on translated
intervals, the use of the Paper 28/v3 pair count for the longer-clock
result, and the exact cancellation giving
$G_y=P(a)/\min_{v\to y}P(v)$. The full gain includes the fixed-ray
normalizer $M_j$. The one-branch maximum and the sum over distinct
deep leaves are different quantities. [Entry-edge gains](../../../research/ayh-resource-reset-20261124/unconventional/ENTRY_EDGE_GAINS.md)

In the second manuscript I checked the permitted first-passage scale
and common exceptional set in Paper 191/v2, the single-set first-landing
application in Paper 102/v1, and the difference of unconditional
natural counts from the fixed-target law as displayed in Paper 179,
Appendix A. I also checked that the §6.3 coupling from Paper 215 is
applied to every prescribed prefix with a relative error bound, before
summing the rare prefixes. The fixed target is chosen before the limits.
For the selected binomial level the exponent
$1/2+2/16^2$ is smaller than $2/3$, giving a divergent shell sum even
after the bounded-multiplicity conversion to odd leaves. This review
does not independently establish the originating timed Gaussian law or
the affine synchronization theorem. [Entry threshold](../../../research/ayh-resource-reset-20261124/unconventional/ENTRY_THRESHOLD.md)

## Scope of the ordinary-selector contribution

The Lean files in this directory prove ordinary changing-center cylinders
and their parent exclusions, finite inverse-word budget, legality and
uniqueness, the complete prepeak gate, dyadic precision, and the
fixed-source perfect-power exclusions. They also prove the large ordinary
negative terminal from certified residue blocks and bounded-time
separation on the negative exponent address, the nearly full additional
ascent clock for every smaller source, and the all-phase time bound for
every ternary-unit cofactor. The ordinary inverse
density/rounding bound, uniform geometric-base theorem, and joint
counting statements are written proofs. The geometric-base and
rooted-charge results identify their affine absorption or predecessor
density inputs explicitly. Identification of the 334711-bit stabilized
signed derivative with the ordinary kernel input was checked by separate
exact integer calculations. The derivative identification has no Lean
proof in this packet.

I authored the selector material. The critical-geometry delegate
independently checked its uniform geometric-slice argument, sharpened
rounding horizon, and simultaneous progression/clock argument. Parent
review and fresh builds are reported separately. These mutual checks
do not make either author an independent verifier of their own result.
