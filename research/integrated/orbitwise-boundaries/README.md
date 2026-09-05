# Orbitwise coefficient tails, echoes, and method boundaries

**Resident reference assembly; no new cycle-exclusion or bridge promotion.** The exact local components were independently reviewed by B at PR92 `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`; its [claim matrix](../../../reports/prepublic-2026-09-05/reviewer-b/CLAIM_MATRIX.md) is pinned by review commit `ea5faf5bcdd49a693e450dc0eeda83ace807f2f3`. A's [finite-weight review](../../../reports/prepublic-2026-09-05/reviewer-a/CLAIM_MATRIX.md) is a separate source chain.

## Orbitwise is not basinwise

The injective counting argument applies to the distinct states of a non-eventually-periodic positive orbit. It is not an estimate for the many-to-one predecessor basin of that orbit. The reciprocal correction is bounded on that distinct orbit, its coefficient sequence tends to infinity and attains a global minimum, and this yields an actual coefficient-supercritical tail of that same ordinary orbit.

With the exact source conventions, this gives the reviewed SC*/eventual-periodicity crosswalk. It **does not exclude nontrivial positive cycles**. A cycle traced forever is not an infinite distinct value set, and periodic positive tails have a block coefficient below one. The old `IC-PERIODIC-001` exact synthesis and `RD-BRIDGE-001` still retain their pending narrow-review flags.

| Local proof | Reviewed scope / warning |
|---|---|
| [Orbitwise Mellin bounds](../../astra-three-routes/pass2/ORBIT_MELLIN.md) | T-A3-401–403: injective-set counts and orbitwise reciprocal bounds. Interpret the infinite-orbit clauses as infinite distinct value sets. |
| [SC tails and continuation](../../astra-three-routes/pass2/SC_TAIL_AND_ECHO.md) | T-A3-451–453 and L-A3-452: actual SC tail, near-minimum source location, complete displacement/CRT continuation. The logarithmic cutoff needs the [A=0 guard](../ERRATA.md). |
| [First return echo](../../astra-three-routes/ROUTE2_RETURN_ECHO.md) | One common displacement, complete denominator, source/end legality and all proper prefixes. Rational controls are not ordinary realization. |
| [Finite simple-path records](../../astra-three-routes/pass3/FINITE_RECORDS.md) | Finite reciprocal budget and record windows; local bounds imply descent or repetition conditionally. Spatial location is not elapsed time. |

## What the rank obstructions actually exclude

| Local proof | Method class, not a universal impossibility result |
|---|---|
| [Linear profile ranks](../../astra-three-routes/ROUTE3_RANKS.md) | Stated finite affine-valuation scalar ranks at fixed blocks; separate whole-run argument. |
| [Separate nonlinear profiles](../../astra-three-routes/pass2/NONLINEAR_PROFILE_RANKS.md) | Arbitrary separate finite-valued valuation profiles under the exact hypotheses. |
| [Joint arithmetic observations](../../astra-three-routes/pass3/JOINT_ARITHMETIC_RANKS.md) | Fixed finite joint polynomial-valuation/residue observations, including bounded menus of whole-run macros. Unbounded moving indices are outside the class. |
| [Finite dictionaries and histories](../../astra-critical-mass/CONTINUATION.md) | PR90 finite guarded dictionaries, even rays, fixed blocks and relative truncation limitations; not all infinite aggregate estimates. |
| [Carry normalization](../../astra-three-routes/CARRY_NORMALIZATION.md) | Six administrative value-preserving rules terminate. This is not termination of the full boundary-coupled Collatz rewrite system. |

Every long finite CRT shadow may have a different positive ordinary source. No obstruction proof silently extracts one all-time ordinary witness. Conversely, a finite-feature obstruction must not be advertised as a theorem excluding the moving-rank program.

## Evidence and remaining gap

B read the proof-bearing files and checker interfaces, but did not replay all earlier PR92 numerical protocols. Its targeted finite cone and the separately replayed fifth-pass corpora have explicit boundaries in [validation](../../../reports/prepublic-2026-09-05/reviewer-b/VALIDATION.md).

The remaining obligations include universal local coefficient windows, all-word ordinary echo exclusion, and nontrivial-cycle exclusion with the complete denominator and physical replay. They remain [open](../../open-obligations/README.md); the two old pending syntheses are not upgraded by a new crosswalk in another packet.
