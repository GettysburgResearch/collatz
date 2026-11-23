# Integration and independent mathematical review

Date: 2026-11-23. Reviewer: root research lane.

The root reconstructed the cycle and collision arguments independently of
the child lanes' final verdicts, and reviewed the final integration changes.
The verdict is PASS within the written and finite-formal scopes stated
below. This is not a full Collatz proof or a priority claim.

## Current files

| Packet-relative file | SHA256 |
|---|---|
| `RESIDUAL_UNIT_EXCLUSION.md` | `012f012d063fe5a4f08015da3a5d022cf580e3c630625ee81c174a7f657940ca` |
| `PRIMITIVE_RESIDUAL_DEGREE.md` | `ef823ecb00302060890f0858e1713ac967c11cbfd31723a8fe47f43402ab5b7b` |
| `PRIMITIVE_DENOMINATOR_GROWTH.md` | `e0921fe30a77472cc6c17477f8e6b9edbc042c5d80ce37b09840310a969b0430` |
| `PRINCIPAL_FIBER_CONTROL.md` | `1d395d9c0dff61736f03a5628abb0fe2ffbadb87f83b359530888200b8dafb36` |
| `COLLISION_LOGARITHMIC_GAIN.md` | `d25d348e2af2b5439e8e28aa87d28a1b9b2c901722e1e6a3eeeaa93965def0da` |
| `lean/ResidualWord.lean` | `420d1eb7976dca248cc4e85846586e253751379907739bc6a2bd816aca3f79e6` |
| `lean/DistinctWordBudget.lean` | `2b5c3d9e4ccc96f9923c33bf38feb9670810da87ae08bbe33cf54d5dd126eb54` |
| `certificates/check_collision_budget.py` | `5e48eb3cfad0a0fb934d87f9c1736414c39d16cd9db4da560d07bd5de8227ecb` |
| `certificates/check_factor_growth_gap.py` | `ce0461731035a067b03b1a1e155aa8c07d0b29ac46c2fc5790cb3cd898238d43` |
| `certificates/check_principal_fiber_control.py` | `7c6fd1e7bf36cee9c7140de8296c745823212a5bd9c73a1af5a829ca1070d6ba` |

## Cycle argument and the new growth step

The principal binomial's irreducibility follows from integrality of the
absolute constant coefficient of any monic factor and coprimality of its
reduced exponents. Positivity at its real root ensures the factor survives
in F_0. Unit value then forces the reduced pair (2,1), by arithmetic modulo
eight. All residual roots have radius four; equality in the product of
distances to three forces exactly the simple root four. The quotient and
both alternating phases follow. The 12-theorem Lean module proves the
finite polynomial/word consequences and displays the generic irreducibility
premise explicitly.

The degree proof keeps the original word: its normalized coefficient
period L forces the integer shift ell=AL/p in its actual odd-position set,
including wraparound. Primitivity therefore makes the support order lcm
p. The rational images alpha^b/2^a form complete cyclotomic conjugacy
classes. All b principal roots map to one, leaving at most n-b nontrivial
images. Hence the sum of their totients is at most n-b, and the elementary
order bound proves g<=3^(n-b) and p<=3^(n-1). The note's final formatting
change only joins a split inline formula; its proof is unchanged.

For the value-growth theorem the root checked the coefficient-reciprocity
identity and support deflation, the Matveev specialization against the
primary Annals Theorem 9.4, the finite/infinite cutoff logic, and the exact
continued-fraction candidate selection. The Ramanujan calculation for
A=2p retains full conjugacy classes; the positive sign of every h>1 factor
is now explicit. The small totients and the principal factor's unit value
are included. Thus D_pol>(3/2)^(n-1)>=p^log_3(3/2) follows for every
nontrivial primitive positive word, with the stated analytic input.

This lower bound is for the polynomial denominator before the further
integer gcd at three. It supplies no bound for the resulting reduced
rational denominator. The unbounded control family was independently
reconstructed: its exact numerator, polynomial coprimality, unique zero-run
primitivity, complete 5-primary absorption, all-phase floor, and strict
nonintegrality intervals all hold. It tests the correct evaluation fibre.

## Collision argument

The squared hockey-stick identity counts distinct positive words with
positive deficit. Cauchy's inequality applies to the given word law, with
no independent source law introduced. The actual affine relation projects
its past word to the endpoint residue and increases collision energy.
The time-window ratio (M-m+1)/(M+1) is retained and squared.

The earlier exact retracing identity gives ordinary measure domination by
v_0/C for every inverse clock. This multiplication preserves the
exponentially small bound without subtracting an uncontrolled error.
Injectivity gives the harmonic reciprocal-sum bound and thus mean cost
ell*m+O(1) for m^2<=TM. Fixed-offset Stirling bounds give exactly the
square-root gain. No claim of the corresponding Shannon improvement is
made. The bounded-height duration theorem uses a separate genuine
ordinary injection at modulus at least the entire segment height. It
makes no claim about discontiguous low-height visits across high excursions.

## Exact integration deltas from independent review snapshots

The independent residual-word review pins the original main note at
3d6619371246f4918e0c5a57eee2ef1c2f08b76c0794fddcaba869baab498eaf.
Its mathematical proof is unchanged in the current file. Only references
to the superseded weaker optional theorem now point to the stronger
quantitative note, and the formalization status is updated from planned
to the actual finite bridge. The earlier optional note and checker were
never published in this packet and are omitted in favor of the stronger
single argument and certificate.

The independent collision review pins the note at
5a71d0f241bf9ac60b8125909b010d32d6b1d1716cb6b991ff8d3babf58fd017.
The current note only clarifies its parameter as 0<T<infinity. The
nonpositive cases had an empty precision range; no proof or constant
claim changes. The current DistinctWordBudget source exactly matches the
reviewed final hash 2b5c3d9e4ccc96f9923c33bf38feb9670810da87ae08bbe33cf54d5dd126eb54.

The collision indexing checker's assertions were mechanically replaced by
explicit require checks, so optimized Python retains every check. Its
inputs, ranges, calculations and output counts are unchanged. The final
clean replay independently records both modes and all compiler output.
No child-local verification receipt is promoted to an execution of the
published repository commit.

## Review boundary

The child reviews retain their exact original source hashes. Their scope
is not silently extended to edits. The current hashes above and this
integration review identify the complete current mathematical scope.
The general algebraic-number and asymptotic arguments remain written
proofs. The new formal modules have 21 public audits; external analytic
inputs, ordinary harmonic flow and full Collatz are not formalized or
assumed as new axioms.
