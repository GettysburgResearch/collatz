# Independent review of the moving predecessor-density profile

**VERIFIED at the stated written, source-qualified scope.** No new analytic input is certified by this review, and no Collatz conclusion is claimed.

- Reviewed file: `research/astra-collision-factor-bridge-20261128/arithmetic/DENSITY_ESCAPE_PROFILE.md`.
- Reviewed SHA-256: `3ae46fb58e43a81e4fbbbe7df74b16ec5cdee8f868ffbb3b094f9e875beacbe5`.
- Review time: 2026-11-28T09:45:40.136717+00:00.
- Reviewer: collision lower-bound lane; proof reconstructed independently of its author.

## Reconstructed claims

For each asynchronous component B, the finite minimum-fiber truncation gives its actual natural density D_B. The difference between B and the union of its minimum fibers below M is bounded by the proper minimum-law tail r(M), uniformly over the component. This supplies the needed countable-family tightness without treating arbitrary natural density as a countably additive measure.

For an escaping odd ray a_j in B, every one of the finitely many minimum labels in B below M eventually meets that ray, and then reaches all its sufficiently late vertices. A common finite merger index therefore gives D_B-r(M) ≤ d(a_j) ≤ D_B. This proves the monotone limit d(a_j) ↑ D_B; taking the increasing union of predecessor sets alone would not prove it.

The imported first-landing estimate implies that every target with d(a) ≥ δ lies on one of finitely many ordinary rays from sources at most M(δ). Every such ray in a cyclic component is finite. Thus all sufficiently large cyclic targets have d(a) < δ, even if there are infinitely many hypothetical cyclic components. Targets in escaping components have d(a) ≤ D_B. Combining this upper bound with the preceding ray limit proves the exact moving limsup identity in Section 4. A positive supremum of the summable component masses is attained.

The eligibility issue is harmless along an escaping odd ray: after an odd departure its target is prime to three. For positivity, one may invoke Mazur's full-map predecessor theorem at the target 2v to obtain shortcut predecessors of an eligible odd v. The author added this explicit map-conversion sentence before the final reviewed hash. The review does not assume a uniform positive predecessor constant.

The targets q_k=(4^k-1)/3, k≥2 and 3∤k, have pairwise disjoint predecessor sets because their odd futures proceed directly to 1. Finite additivity gives summability of their fixed-target densities, so those densities tend to zero. This is a valid obstruction to a uniform positive floor.

Finally, the first-doubling argument in Section 6 has bounded overshoot x_(j+1)<3x_j+1. Consequently log x_j=O(j), and the proposed fixed-positive-density gain would have a divergent harmonic total along any escaping ray. Conversely no escape makes the gain statement eventually vacuous. The note correctly identifies this as an unproved full no-escape obligation, not an unconditional estimate.

## Scope of source checks

The review reconstructs the deductions from the three explicitly named interfaces: the proper minimum law and fixed-target densities, the first-landing bound, and positive predecessor density. It does not enlarge their existing verification status. The recent Paper 202 source pin is `62384ee2c5e3607ee265c8cb2a66c66d8ad3272385c80dc00c560fa016322ab6`; the reviewed note distinguishes its low-density gain obstruction from the still-open fixed-positive-density regime. A later source edit requires a new hash boundary.

Final formatting review: the moving-limsup display uses an explicit LaTeX quad in place of a trailing backslash-space at the line end. This changes only spacing; the final hash above includes that cleanup and no mathematical change.
