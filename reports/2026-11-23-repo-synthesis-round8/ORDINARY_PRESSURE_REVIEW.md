# Independent review of the phase and pressure deductions

23 November 2026. Reviewer: the ordinary-source construction lane.
Parent: `3954c775ba74e1f40776ff38cb4282698d4a334a`.

## Frozen scope

This review concerns the following exact local Git blobs, before their
publication under a new full commit:

| Path within this packet | Git blob |
| --- | --- |
| `PRESSURE_CONSTRUCTION.md` | `7ef222d23f59a2dffd936dbfa93765df064db166` |
| `pressure_controls.py` | `ff6936ae3bc57daa8ebe10bdfa07f92aeb2af592` |

The real scalar is the actual positive ordinary series in the companion
`GERM_BRIDGE.md`, R8-G1, pinned by the reviewed note to blob
`540110f09cf68e3309fd83fea9c7ae497536ded4`. The escaping correction
product and ordinary pressure maximum in R8-P5 remain the explicitly
source-qualified input pinned in the reviewed note. This review does
not reclassify that upstream input or nearby PR claims.

**Verdict: VERIFIED at the level of the stated written deductions and
their explicit hypotheses.** The all-exponent claims remain written
mathematics. Neither this review nor the finite controls are a Lean
formalization of the complete phase family or its real-series attachment.

## Reconstructed arguments

**R8-P1.** Clearing the ternary denominator by actual odd steps leaves
the stated tripling orbit of reduced fractional parts. The unique lift
in `(1/2,3/2]` is correct, including the essential value `m(1/2)=3/2`.
For consecutive lifts, `3m_i-m_(i+1)` is an integer strictly between
zero and four; its sum is `2S`. Therefore the proposed block comparison
is exact rational arithmetic. Any nonconvergent orbit avoids every
verified odd source through Q, so every remaining odd state is at least
Q+2. This supplies the numerator bound in the complete W ratio. The
unconditional scalar upper bound supplies a positive lower bound for W,
making strict block contraction contradictory. No boundedness of the
integer carries is required. Conversely, termination makes the scalar
triadic, so a reduced residual denominator greater than one is genuinely
excluded. The argument concerns the complete denominator and phase.

**R8-P2.** A tripling orbit containing negative one pairs each reduced
fraction f with `1-f`. For d>2, neither zero nor one half occurs, and
the paired lifts sum to two. The d=2 endpoint is separately correct.
The displayed prime-power negative-one exponents lift by the binomial
argument; their doubled moduli and the stated quadrupled seven-power
moduli follow by the additional parity congruence. Arbitrary products
are correctly left outside the conclusion.

**R8-P3.** The elementary binary valuation induction gives the exact
order `2^(k-2)` for k>=3; the possible smaller exponent one is excluded
directly by `3!=1 mod 8`. Cardinality then identifies the complete two
cosets as residues `{1,3}` and `{5,7}` modulo eight. For k>=4, translation
by half the modulus preserves each coset and gives equal lower and
upper halves. The arithmetic progression sums produce lift means
`1-2/d` and `1+2/d`. The worst mean is 7/8, and the exact contraction
comparison passes. The exceptional modulus eight does not have the
half-translation property and correctly retains mean 3/4 for its
`{5,7}` orbit. Negative-cycle realization does not become positive
ordinary realization.

**R8-P4.** The binomial valuation argument proves the stated order at
every p-power, including a nontrivial initial valuation w. Reduction
of an orbit of length `tM` to length t has exactly M distinct points
over each base residue. These are all possible lifts, not a selected
portion of a residue fiber. Counting the fractions below one half in
an odd fiber gives exactly

\[
\mu_k=1+(\mu_w-1)/M.
\]

Since every base lift exceeds one half and `M>=p>=5`, the resulting
mean exceeds 9/10. This checks both the complete-fiber argument and the
uniform all-exponent estimate. The note correctly leaves `11^2` outside
this family and does not apply the conclusion to arbitrary denominators
merely divisible by an excluded prime power.

**R8-P5, conditional on its pinned pressure input.** The complete edge
identity gives `g_i=log_2(3)+ell_(i+1)-ell_i`. The uniform component
lower bound and actual ordinary growth make `ell_i=O(i+1)`, justifying
the discounted boundary term. Both logarithmic formulas reconstruct.
At the same maximum source, telescoping gives `2^A_j<3^j` for every
nonempty prefix. This yields the floor-clock scalar ceiling. Actual
escape makes the logarithmic pressure ratio tend to minus infinity,
so at least one floor-clock term is strictly deficient and the first
inequality is strict. The rational tail formula follows from the exact
sum of `j/3^j` and `log_2(3)<8/5`. The last paragraph correctly prevents
reapplying a maximum-source ceiling after moving forward to clear a
ternary denominator. The ceiling remains above 5/8.

## Independent finite checks executed

A separate Python harness, without importing the reviewed control
script, constructed tripling cosets using powers of three and a set
partition of all reduced residues. It confirmed the complete two-power
means for exponents 3 through 12. It also checked full reduction fibers,
lifted orders, and the exact mean identity for

\[
5^3,\ 7^3,\ 11^3,\ 13^2,\ 19^2,\ 23^2,\ 29^2.
\]

The respective orbit counts were `1,1,22,4,1,2,1`; the valuation w
was two at p=11 and one for the other displayed primes. Every tested
high-prime-power mean exceeded 9/10. The additional primes 19, 23,
and 29 are separate checks of the written fiber argument, not an
extension of the theorem's scope by sampling.

The harness independently replayed all positive odd starts through 31
to one; the longest such replay had 41 odd steps. It verified the
strict finite-floor threshold `100^5<2^8*33^5` and recomputed the exact
pressure upper bounds at J=6 and J=20. All these independent checks
passed. The reviewed script was also inspected for complete reduced
numerator coverage, exact comparisons, and checks that remain enabled
under optimization. Its separate full execution receipt belongs to
the producing lane and the root replay.

These checks support the finite domains stated here. The universal
denominator-family proofs are the reconstructed arguments above;
none produces rationality of an arbitrary actual scalar, controls a
fixed ordinary source's exceptional carries, or completes Collatz.
