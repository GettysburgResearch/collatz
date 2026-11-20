# Arithmetic comparison with the publication refresh

**Conclusion: the inspected new arithmetic results do not close the
global gap, contradict SRC-001--005, or supersede the rank-only cycle
ceiling.** They substantially strengthen fixed-core excursion restrictions
and give an unconditional all-time moment estimate. Their remaining
obligations are explicit and remain unproved after combining them with
the frozen shifted-rank results.

This is an independent scientific comparison. The arguments identified
below were read and reconstructed; no new orbit search or rerun of their
numerical reports was needed. The existing arithmetic proofs, checker,
and report were left unchanged.

## Exact source identities

The fetched refs were checked to have these exact commit heads:

| PR | Full commit SHA |
|---|---|
| 167 | `e83cc8b35ad614c616df7c00318cc9645a174c34` |
| 169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` |

Within PR167, the relevant files and claims are:

* `research/least-failure-closure-20261121/MULTISTEP_CORE_RETURNS.md`,
  RU1--RU3.
* `research/least-failure-closure-20261121/FIXED_DEFECT_CORE_RETURNS.md`,
  FD1--FD3.
* `research/least-failure-closure-20261121/EXCURSION_FREQUENCY.md`,
  EF1--EF4.

Within PR169, they are:

* `research/certificate-renewal-20261121/MOMENT_QUANTILES.md`,
  MQ1--MQ5 and the conditional closing criteria BC, NC, QC, PC.
* `research/certificate-renewal-20261121/FIXED_ENDPOINT_SUMMABILITY.md`,
  ES1--ES4.
* `research/certificate-renewal-20261121/FULL_THEOREM_ATTEMPT.md`,
  section 3, as the author's statement of the remaining arithmetic gap.

The occupancy dependency was also read at PR153,
`eb04a5d79020cefa0ba46794095b5766c5ff66a4`,
`research/fixed-integer-descent/drift.md`, FID-DRIFT-002 and
FID-DRIFT-005. Its finite simple-path and fixed-constant qualifications
agree with their use in MQ2--MQ5.

## 1. PR167 strengthens return control without requiring intermediate cores

RU1 classifies every vanishing subsum of the full shifted path equation:
the only exception is the all-valuation-one word. The forced binary
valuation argument checks, including the one-edge boundary case.
RU2 can therefore count fixed-length paths with prescribed endpoint
cores while allowing arbitrary intermediate cores.

FD1 compresses the equation further, retaining only the defect
corrections. Its proper-subsum argument also checks: an actual defect
source has shifted binary valuation one; after each forced pair of
correction terms the partial sum is the actual shifted state multiplied
by its accumulated powers. The next valuation-one run fixes the exact
valuation of that partial sum, forcing the next pair. Thus no proper
subsum vanishes.

FD2 applies the stated Evertse prime-pool theorem to this nondegenerate
equation. With `d` defects there are `2d+1` variables, independent of
the intervening run lengths. The positive correction coordinates recover
the defect positions and cumulative exponents separately by their
2-adic and 3-adic valuations. The count is therefore genuinely a count
of distinct canonical ordinary segments. FD3 correctly distinguishes
that count from the finite but height-dependent end-run extensions.

This is a stronger return statement than SRC-001 in one direction:
intermediate states can leave the prescribed endpoint core classes,
and the total length is unrestricted at fixed defect count. It gives
finitely many completed excursions with any bounded defect budget.
Its conclusion about growing defect counts requires infinitely many
completed excursions along a nonrepeating orbit; it neither forces an
unfinished excursion to return nor controls unbounded defect budgets.

The arithmetic nondegeneracy and injections revealed no error in this
comparison. The finite counts retain the explicitly stated external
Evertse dependency; they are not height estimates.

### Relation to the frozen rank claims

FD2 is uniform in endpoint cores for a fixed finite prime pool. SRC-001
instead uses the general-rank ESS theorem for arbitrary rational
generators and a bounded number of cosets. A rank-one generator may
involve arbitrarily many primes, so a bound depending on prime-pool
cardinality cannot be substituted for the rank-only bound.

Neither RU2 nor FD2 supplies SRC-004's numerical cycle height ceiling
uniform over all unspecified generators and coset representatives.
SRC-004 additionally uses the classical fixed-local-minimum cycle
bound reconstructed in SRC-003. That classical ingredient remains
credited as such. The one-edge nondegeneracy mechanism remains credited
to PR161; the refresh does not support a broader novelty claim for it.

The two kinds of uniformity are complementary. The new compressed
nondegeneracy argument could support a further general-rank return
extension, but no such extension is needed for, or silently included in,
the frozen SRC statements.

## 2. PR167 improves the fixed-prime-family frequency conclusion

EF1's block accounting includes endpoint vertices, internal core-to-core
defects, and initial or final outside runs. Its two bounds combine
correctly: short gaps are bounded by RU2, while each remaining gap
consumes many disjoint outside vertices; the exact run clock then bounds
the number of vertices that the inside blocks can contain.

For a fixed source and fixed finite shifted-core family, EF2--EF3 give

\[
\frac{C_N}{\log N}\longrightarrow\infty,
\qquad
\liminf_{N\to\infty}
\frac{C_N}{\log(N+1)
(\log\log(N+1)/\log\log\log(N+1))^{1/3}}>0
\]

on a nonperiodic orbit, with the explicit constant in that source.
The choice of the growing gap cutoff in EF3 respects the displayed
solution-count bound. EF4 correctly combines this with the separate
shifted-smooth cycle exclusion to obtain a sufficient condition on
the actual outside-visit count.

These improve the earlier logarithmic restrictions for a fixed prime
pool. They do not replace SRC-002's statement about arbitrary bounded
multiplicative rank. Outside visits are neither distinct primes nor
independent valuation vectors. No upper estimate for `C_N` is proved.
Continued rank creation and excursions of increasing defect count can
satisfy all these lower bounds simultaneously.

## 3. PR169 proves an all-time estimate at a different endpoint weight

The ordinary primitive-word decomposition in MQ1 is sound. Full
numerator divisibility gives every inverse step, and a negative odd
source cannot reach its positive representative under the prescribed
actual steps. Distinct words at a fixed length have distinct primitive
sources. The cylinder tail calculation gives

\[
\mathcal D_q=P_q+R_q,
\qquad 0<R_q<\tfrac12(3/5)^q.
\]

ES1 handles repeated visits to a hypothetical positive cycle by its
strictly contracting cycle Jacobian. ES3 makes this a direct all-time
telescoping result. For one fixed original source,

\[
V_q=(J_q/n_q)^4=1/(n_0^4I_q^4),\qquad
V_q-V_{q+1}
=V_q\left[1-\left(\frac{3n_q}{3n_q+1}\right)^4\right].
\]

The stated polynomial factorization proves the sharp lower bound
`175/(256n_q)` for the bracket. Positive summation over time and
sources therefore gives the unconditional theorem

\[
\sum_{q\ge1}\sum_w\frac{J_w^4}{r_w^5}<\frac{512}{175}.
\]

The primitive injection is needed only within each fixed time;
repeated use of one source at different times is already paid by the
per-source telescope. No convergence or cycle exclusion is assumed.
The constant is sharp for the per-source bound at the fixed point one.

ES4 correctly removes the region `r_w<=q` from the averaged closing
question: that region has cumulative second-denominator mass `o(N^3)`,
whereas PC is normalized by `N^(59/19)`. The remaining condition is
the same normalized liminf for the actual tail `r_w>q`.

This is a genuine unconditional global estimate, but it leaves three
endpoint powers between its summand and the original `P_q`. On a
hypothetical nonperiodic orbit, the occupancy theorem already permits
`I_q` to have a finite limit and `V_q` a positive limit. The telescope
then leaves that positive residual. Equivalently its per-source fifth
weight is `1/(n_0^4 I_q^4 n_q)`, compatible with the known finite
reciprocal budget. No argument in ES3 forces the residual to vanish or
controls the growing-endpoint second-denominator tail.

## 4. The new moment criteria are conditional closing inputs

MQ2--MQ5 retain one fixed hypothetical nonperiodic source throughout.
Their occupancy, sorting, and moment inequalities have the stated
directions. In particular such a source forces `P_q` to tend to
infinity; consequently even a bounded cofinal subsequence, criterion
BC, would exclude all nonperiodic orbits. The negative-average,
quantile, and positive-average criteria NC, QC, PC are also valid
sufficient conditions. The paper does not prove that the actual
arithmetic sequence satisfies any of them.

All four criteria concern nonperiodic orbits. Repeated cycle times
cannot be counted by simple-path occupancy, and their `I_q` is not
bounded. ES3 explicitly accommodates cycles; it does not remove this
restriction. SRC-004's finite decision for each prescribed rank and
coset count does not exclude cycles of arbitrarily large ranks.
Taking the union over all ranks supplies no global ceiling or completed
cycle exclusion.

## Consequence for this packet

No correction to SRC-001--005 is indicated. Their remaining contribution
is the prime-identity-independent shifted-rank defect bound and its
effective cycle-height composition, together with the certified family
showing why a universal rank budget is unavailable. PR167 supplies
stronger information about unrestricted intermediate excursions, and
PR169 supplies the all-time fifth-weight estimate and weaker conditional
moment targets. None furnishes a bound on continued rank creation,
forces sufficiently few outside visits, proves BC/NC/QC/PC, or excludes
every nontrivial positive cycle. These remain the actual global gaps.
