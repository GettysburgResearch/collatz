# Scoped review of the tilted renewal comparison

Date: 2026-11-22. Reviewer lane: arithmetic. This file records that lane's
completed independent reconstruction, communicated to the integrating agent.

Reviewed source:
`research/lean-global-closure-20261121/machinery/TILTED_RENEWAL_FINITE_IMMIGRATION.md`

SHA256: `fa0c72ac7e35aa2defd0b970461acc7908f170cfe231463bbc37c87660a69551`.

**PASS in the stated conditional scope.** The imported scalar-tail,
ordinary-trace, and reciprocal-path results were not re-proved in this
review. No Lean or full Collatz conclusion is asserted.

1. A length-j tilted word has probability `3^j/4^S`; its density
   coefficient is exactly `A_j^2`. The finite ternary residue includes
   nonunit last inverse endpoints. No extra ternary digit was inserted.
2. A fixed source has at most one hitting depth at a nonperiodic root.
   The affine identity bounds `A_j^2/q^2` by `1/x^2`. Nonnegative
   summation proves the complete depth budget and every block-average
   bound.
3. In the real-tail decomposition, the small-prefix term has coefficient
   exactly `2*C_T/theta`. The other prefixes first hit the finite set;
   factoring their first hit leaves `D_(j-ell)(x)` with its full original
   coefficient. A nonunit hit contributes only through `D_0=1`, at one
   depth, and costs at most `1/(R*x)` after averaging.
4. At each fixed endpoint x, the continuation index is
   `r+1-d_p(x)`. Let `E_R(x)` be the mean absolute error of this shifted
   density, using zero before contact, against h(x). The supremum in
   equation (13) is bounded by the finite sum
   `sum_(x in K_M) E_R(x)/x`. Every term tends to zero. This checks
   negative shifts, missing initial slots, changing first-hit subsets,
   and the uniformity in k without a uniform theorem over all integers.
5. With the explicit nonperiodic unit original source p, its last small
   ancestor x* is a unit. The actual reversed segment first hits the
   finite set there, and its retained product gives precisely the
   positive lower bound in (15).

The final unit-root and unit-source conventions, and h=0 at nonunit
endpoints, were reread at the displayed hash. The surviving immigration
term is essential. Its disappearance and escape exclusion are not proved.
