# Coordinating reconstruction of the complete inverse-kernel extension

23 November 2026. **VERIFIED in its displayed written scope.** This review
is by the coordinating agent, who coauthored the underlying sparse-minimum
argument. The all-branch extension was authored by the escape lane. This
is a reconstruction of its additional deductions, not external referee
acceptance or an independent discovery of the shared input.

Source:
`research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/ALL_BRANCH_CAPACITY.md`

SHA256:
`26fac702d7178ea9ecf41fc673975fa4d9d2961c10e4f63fda5bcb5c75896fe3`.

## Reconstructed steps

1. **AC1--AC2.** An inverse parent of q_(j+1) other than q_j cannot be
   any ray point, by injectivity of the same odd ray. After one odd step
   it enters that ray forever. The full shortcut basins of these roots
   are therefore disjoint: intermediate states on an odd-to-odd edge
   are even. Classifying the first hit of the ray gives exactly the
   initial basin, later ray atoms, and these off-spine basins. No vertex
   of the unit component is dropped.
2. **AC3.** The capacity increment includes the new atom r(q_(j+1))^s
   plus every off-spine basin mass. The original spine basin is the
   one removed term. Nonperiodicity makes the predecessor-depth
   interpretation unambiguous.
3. **AC4.** A parent at height at most Y forces its target to be at most
   4Y/2^e. Counting the actual ray at each exponent and summing the
   complete geometric series gives the displayed constant. With
   beta=39/40>3/4, 2^beta>5/3 and 4^beta<4 give
   4*4^beta/(2^beta-1)<24.
4. **AC5.** The already reconstructed general first-hit split BM4
   applies to this larger root set. At H=floor(log_2 X/25), its root
   contribution is below 48 X^(624/625). The no-descent terms have
   coefficients 1,2^(1/32),1; their sum with 48 is below 64 and all
   exponents are at most 799/800. This proves the stated enlarged
   minimum bound without a predecessor-population hypothesis.
5. **AC6--AC7.** Apply the complete finite source cutoff and dyadic
   concavity argument with 64 replacing 12. Power 1/s is strictly inside
   its summability range. Nonnegative subadditivity in AC3 and Tonelli
   retain every side branch. The remaining ray-atom sum is at most 160
   by the inherited ordinary reciprocal bound. The resulting constant
   uses unnormalized masses, so its ray independence is legitimate.
6. **AC8.** The ratio of actual pressure weights is
   r(v_(j,e))/r(q_j)=2^(a_j-e). Each displayed kernel term is exactly
   (b_(j,e)/A_s(q_j))^(1/s), which is at most
   A_s(q_0)^(-1/s)b_(j,e)^(1/s). Both legal colours, every lower
   exponent and all larger exponents remain in the index family.

## Boundaries retained

The infinite partition, real power estimates, and countable sums remain
written proofs. The generic graph/cutoff declarations in the existing
new Lean module do not silently certify those analytic deductions. This
review ran no new computational census and claims no additional Lean
declarations. The extension provides neither a chronological convergence
rate for capacity nor the missing lower Green comparison. It is a
necessary all-branch constraint under a hypothetical escape, not a proof
that an escaping component exists or has been excluded.
