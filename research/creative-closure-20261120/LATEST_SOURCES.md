# Latest-source audit and the remaining bridge

The pass began with PR157 as the latest research packet. Before publication,
a fresh GitHub read found PR158--160 and a newer PR146 head; the final
preflight also found PR161. The team read
the relevant scientific files at the exact commits below and revised the
attribution and attempted bridge accordingly. Main remained
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.

These are **targeted written-source comparisons**. They do not constitute
blanket acceptance of another packet, execution of its whole checkout,
or a new Lean build. Every new theorem in this packet retains its own
proof and scope. No statement at a later remote head is covered by this
snapshot.

## Frozen latest heads

| PR | Full inspected head | Principal source paths read |
| --- | --- | --- |
| [146](https://github.com/GettysburgResearch/collatz/pull/146) | `e238c63a5d57f96bb063b7472498d1977df51951` | `research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`; `BOUNDED_RANK_TRANSFER.md` |
| [157](https://github.com/GettysburgResearch/collatz/pull/157) | `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`; `transport.md`; `arithmetic.md`; `closing-attempts.md` |
| [158](https://github.com/GettysburgResearch/collatz/pull/158) | `cf49a68bf93e98c97a18dc3d1a4186faf534e422` | `research/ordinary-basin-closure-20261120/CERTIFICATE_CARRY.md`; `EXPANDING_RETURNS.md`; `PRIMITIVE_TRACE.md` |
| [159](https://github.com/GettysburgResearch/collatz/pull/159) | `0e7d2841b1591073c6399f91f3b6944ebcdbdbd5` | `research/allhands-global-closure-20261120/PRIME_SUPPORT_PEAKS.md`; `DIRECTED_BOUNDARY_CIRCULATION.md` |
| [160](https://github.com/GettysburgResearch/collatz/pull/160) | `6d877e718f5ef9d57fe1830912c444359718747a` | `research/closure-attacks-20261120/arithmetic/CLOCK_HEIGHT.md`; `merger/PHYSICAL_CERTIFICATE_BOUNDARY.md`; `merger/SINGLE_MULTIPLIER.md`; `critical/CRITICAL_SINGULARITY.md`; `critical/SINGLE_SLICE_ENERGY.md` |
| [161](https://github.com/GettysburgResearch/collatz/pull/161) | `4a0536b587fc91ee0c7bb1b160c06dda16ddbf23` | `research/source-rigidity-20261120/SHIFTED_SMOOTH_CYCLES.md`; `SPARSE_SMOOTH_EXCURSIONS.md`; `CRITICAL_APPROXIMATE_INVARIANTS.md`; `CARRY_DEBT_RESET.md`; `ENDPOINT_CAPACITY.md` (definitions and opening scope only) |

## Physical certificate transport: what changed

[PR146's deep reverse criterion](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/DEEP_REVERSE_BASIN.md)
gives another sufficient adjacent implication with a precise direction.
At its first nonempty supplied odd rank, four, the target condition is
convergence of every `3^(27j-1)`. Its
[bounded-rank theorem](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md)
decides a lifted-merger question under its stated certified-arm interface.
When that test fails, existence of a stopping certificate for the other
arm remains open. Its direction cannot be reversed by merely renaming
the two arms.

We tested a concrete combination with the new mixed-base carry controller.
The marked-token argument in [CSR-001](source_rank.md) proves that a fixed
supplied odd rank cannot bound its exceptional-rule allowance. The actual
rank-four antecedents already require at least `9j` exceptional carries
from their canonical binary words. More directly, a subsequence of the
required pure-power target words forces arbitrarily many such carries.
Thus every fixed allowance based only on antecedent rank fails on some
target. This is a statement about the specified canonical controller;
source-specific allowances and different justified representations remain
open. No target convergence follows from the congruence construction.

[PR158's certificate-carry note, section 4](https://github.com/GettysburgResearch/collatz/blob/cf49a68bf93e98c97a18dc3d1a4186faf534e422/research/ordinary-basin-closure-20261120/CERTIFICATE_CARRY.md)
already uses `x_r=(2^(6r+4)-7)/9` as a supplied rank-two family and studies
`2x_r-1`. We explicitly credit that source family. The new
[C5-001--002](five_closure.md) settle the **multiplied** target `5x_r` for
every parameter, with exact valuation word `(5,6r-1,4)`. This changes the
target and does not settle the Mersenne obligation attached to `2x_r-1`.

[PR158's expanding-return note](https://github.com/GettysburgResearch/collatz/blob/cf49a68bf93e98c97a18dc3d1a4186faf534e422/research/ordinary-basin-closure-20261120/EXPANDING_RETURNS.md)
already supplies general repeated-word valuation budgets and a switching
resource cycle. [PR160's physical boundary](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/merger/PHYSICAL_CERTIFICATE_BOUNDARY.md),
PC001--004, adds an expanding homogeneous five-pair return. We do not claim
generic expanding returns or failure of resource-only ranks as new. The
distinct computations retained in C5-003--005 concern a specific scalar
ternary controller, an infinite explicitly convergent recharge family with
exact first-hit clocks, and an unbounded output/source ratio on supplied
convergers. The exit quotient's convergence is never inferred from its
multiple's convergence.

The global logical target remains the stronger directed
[PR157 forward-five criterion](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md),
GCM-001--002. The new local block does not establish its missing all-source
premise. PR160's symmetric single-multiplier criterion is not substituted
for that directed statement.

## Spatial analytic balance is not temporal payment

[PR159's directed circulation](https://github.com/GettysburgResearch/collatz/blob/0e7d2841b1591073c6399f91f3b6944ebcdbdbd5/research/allhands-global-closure-20261120/DIRECTED_BOUNDARY_CIRCULATION.md),
DC1--DC3, concerns a common positive spatial flow for ordinary invariant
labels and its functional consequences. Our first-hit capacity,
time-dependent pushed mass, and atom coalescence information are not
ordinary invariant labels. No identity equates their temporal charges
with that tripling flux.

[PR160's critical singularity](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/critical/CRITICAL_SINGULARITY.md),
CS-001--003, and its
[single-slice energy](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/critical/SINGLE_SLICE_ENERGY.md),
SE-001--002, retain their critical normalization and qualified analytic
inputs. The occupation lane instead retains the original atom weights
and imports no positive-density theorem. The newer spatial results do
not establish the missing fixed-input amortized payment.

[PR158's primitive trace](https://github.com/GettysburgResearch/collatz/blob/cf49a68bf93e98c97a18dc3d1a4186faf534e422/research/ordinary-basin-closure-20261120/PRIMITIVE_TRACE.md),
sections 2--5, has an exact finite endpoint-head reduction for a different
Jacobian-weighted moment. Its remaining head upper bound and cycle
qualification are kept separate. Our saturated capacity tail counts each
original once at each endpoint and does not upper-bound repeated time
occupation. See [OCC-001--004 and the source comparison](occupation.md).

The unweighted Hardy construction in [CAF-001--006](analytic_flow.md) is
another distinct normalization. Its signed stationary eigenvectors have
infinite absolute mass, entirely within the known basin of one. Their
small square-norm truncation error cannot be used as a small positive
original-source mass error in any of the preceding arguments.

## Ordered prime height: a stronger restriction, still no conflicting bound

The root read [PR159's prime-support proof](https://github.com/GettysburgResearch/collatz/blob/0e7d2841b1591073c6399f91f3b6944ebcdbdbd5/research/allhands-global-closure-20261120/PRIME_SUPPORT_PEAKS.md),
particularly P13e--f, and
[PR160's localized clock proof](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/arithmetic/CLOCK_HEIGHT.md),
AR-CLOCK-001--006. They improve necessary prime-support budgets for actual
histories and cycle peaks. For example, PR159 states

\[
\max_j n_j\le\max\{4^s n_0,(s+1)^{64s}\},
\qquad \max_{\rm cycle}n<(s+1)^{64s}
\]

on a common prime support of size at most `s`. PR160 localizes prime-power
return charges to high-height components and retains the original-source
term. Both notes credit the earlier prime-power return method; this pass
claims none of those results as new.

These restrictions do not bound prime creation along an arbitrary future.
The symbolic run-energy obstruction and the source-rank carry obstruction
also provide no such upper bound. Requiring a hypothetical escape to
develop more primes and more carry complexity is compatible with both
sets of necessary conditions. No contradiction is inferred by combining
two lower complexity requirements. The full ordinary cycle denominator
and arbitrary growing support remain unresolved.

## Final preflight: PR161's shifted class and critical approximate invariants

A separate source-audit agent read the exact
[shifted-class proof](https://github.com/GettysburgResearch/collatz/blob/4a0536b587fc91ee0c7bb1b160c06dda16ddbf23/research/source-rigidity-20261120/SHIFTED_SMOOTH_CYCLES.md),
SS1--SS4, and
[sparse-excursion proof](https://github.com/GettysburgResearch/collatz/blob/4a0536b587fc91ee0c7bb1b160c06dda16ddbf23/research/source-rigidity-20261120/SPARSE_SMOOTH_EXCURSIONS.md),
SE1--SE2. The root separately read the sparse-excursion proof. The former
closes the cycle and within-class basin questions for odd states whose
shifts have no prime factors outside `{2,3}`. Eventual confinement and
the explicit horizon retain the stated S-unit dependency. The latter
gives a lower bound on visits outside the class for any counterexample
and a sufficient convergence condition if an opposing upper bound is
proved. No such arbitrary-source upper bound is supplied.

There is no closing transfer from OCC-003: its saturated first-hit sum
counts each original once at an endpoint, while PR161's excursion count
counts visits with multiplicity. In particular, finite saturated spatial
mass is compatible with a cycle having linearly many outside-class visits.
Nor does the new class theorem supply a bound for CSR-001's targets.
Every `n=3^(27j-1)` is already outside that shifted class: `3` does not
divide `n+1`, while `v2(n+1)` is one for even exponent and two for odd
exponent. Since the exponent is at least 26, `n+1` is larger than the
corresponding pure power of two and has another prime factor. A
hit-or-exit statement for this class therefore exits immediately on
these initial targets.

The root read
[CRITICAL_APPROXIMATE_INVARIANTS.md](https://github.com/GettysburgResearch/collatz/blob/4a0536b587fc91ee0c7bb1b160c06dda16ddbf23/research/source-rigidity-20261120/CRITICAL_APPROXIMATE_INVARIANTS.md),
CA1--CA3. Its explicit joint approximate invariants concern composition
operators on `ell^p(N,1/n)`, for `p=1,2`. It already gives a non-Fredholm
conclusion at that harmonic normalization. CAF-002--003 concern **exact
signed pushforward eigenvectors on unweighted `ell^2`**, with all support
constructively convergent. Neither the weighting nor the operator is
silently changed in comparing them, and a generic non-Fredholm phenomenon
is not claimed as new to this repository. Both sources explicitly leave
PR157's particular positive-source occupation estimate open.

The root also read [CARRY_DEBT_RESET.md](https://github.com/GettysburgResearch/collatz/blob/4a0536b587fc91ee0c7bb1b160c06dda16ddbf23/research/source-rigidity-20261120/CARRY_DEBT_RESET.md),
CD1--CD3. Its initial valuation-one family and complete-spine reset
already provide known-convergent controls increasing height and both
stopping clocks. We credit that overlapping obstruction rather than
claiming all known-convergent clock failures as a new mechanism. Our
C5-001--002 use the different initial valuation-two paired block;
C5-003--005 analyze a different scalar ternary controller and its debts
and unit exits. CSR-001 adds a literal-rule lower bound on every complete
canonical rewrite derivation, not merely an odd-clock lower bound.

This comparison imports no S-unit theorem into the present proofs and
does not replay or independently certify PR161's complete proof stack.
No scientific claim in our frozen lanes needed correction after the
comparison; the attribution and remaining-obligation assessment were
expanded before the content commit.

## Earlier inputs actually used

The individual notes pin all their earlier dependencies beside the claims.
The nontrivial reused interfaces are the PR152 quarter-safe return
(`2391a9c1e4a7f77233b951d2eb6da92e76652e7c`, AT2--AT3), the PR153
one-simple-path interval bound (`eb04a5d79020cefa0ba46794095b5766c5ff66a4`,
FID-DRIFT-001/002/005), the PR157 fixed-input occupation criterion
(GCT-001--004), and the PR141 prefix-potential accounting
(`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`, HC-5--HC-6). The local
proofs restate the relevant definitions; changing return policy, source,
function space or direction would require another proof.

Primary external operator and rewriting references are version-pinned in
the analytic and symbolic manuscripts. We distinguish source attribution,
new deductions at the declared normalization, independent internal
reconstruction, and bounded execution. None is a substitute for the
still-missing global estimate or physical descent theorem.
