# Independent review of the finite contact reference

**Verdict:** `CONTACT_RETURN_FINITE_REFERENCE.md` and the seven public
statements in `ContactReturnContraction.lean` are sound within their
stated source-qualified domain. The finite reference belongs to the
induced contact transport. The separation between induced contact time
and ordinary excursion time is essential and is retained correctly.

## Arithmetic and branching

The two-parent table is correct in every unit residue modulo nine.
Integrality requires `2^e q` to be 1 modulo three; the parent is also a
ternary unit exactly when `2^e q` is 4 or 7 modulo nine. The six powers
of two permute the six unit residues, giving precisely the displayed two
exponents. For odd positive `q`, the selected parents are positive and
odd, and `(2^e q-1)/3<64q/3`.

At a contact, the ratio estimate follows in the correct direction from
`nu(parent)>=gamma/parent` and `nu(q)<=M/(delta q)`. The strict lower
bound exceeds `epsilon=3delta gamma/(64M)` for each chosen parent.
At least one is outside any specified incoming branch. Harmonicity then
gives the used branch mass at most `(1-epsilon)nu(q)`. Every proper
ancestor in that branch has no larger mass than its branch root.

The nonperiodic domain matters: a periodic parent would have a periodic
image, so these parents stay in the domain, and no extra cycle lap can
identify distinct source-to-target paths.

## The actual first-return law and its antichain

For a fixed target contact, distinct first-return contact ancestors are
incomparable. If one reached the other, that later contact would occur
before the designated first return to the target. Their actual inverse
branches are therefore disjoint. Expanding harmonicity to a common depth
larger than all depths in a finite subcollection proves the finite row
mass bound; increasing finite subsets proves the countable bound.

The inverse path probability telescopes to `nu(x)/nu(q)`. A physical
nonperiodic source has a unique hitting depth and unique path, so the
first-return event is counted once. The row sums are subprobabilities;
the asserted equality only applies where the separately supplied
almost-sure contact theorem is available. That equality is not used in
the contraction proof.

The **column** condition is different and is used correctly: a fixed
original source has at most one next forward contact. Thus summing
fiber energies charges every retained original source at most once.
No missing row mass is silently identified with forward absorption.

## Finite reference and energy

The contact bound `nu(q)<=M/(delta q)` proves summability of `nu(q)^2`.
Combining the individual branch ratio with the harmonic row budget gives
`J(nu^2)<=rho nu^2` on the contact set. Cauchy--Schwarz on each complete
fiber proves the displayed energy contraction, and uniqueness of the
next target justifies summing over targets. The countable extension
uses nonnegative convergence and the same finite inequalities.

The seven Lean statements implement precisely these finite operations.
`square_reference_row` uses the maximum incoming atom and row sum;
`fiber_energy_bound` retains the square of the full colliding sum;
`finite_source_energy_contraction` uses the exact fiber partition;
the remaining four statements prove geometric iteration and the two
height orientations. Their hypotheses match their mathematical uses.
None of these Lean statements asserts the analytic construction of
`nu`, the arithmetic parent table, or the countable first-return law.

## Heights and the logarithmic series

Along forward contacts, reference mass grows by at least `rho^(-1)`
per return. Comparing the initial lower bound with the final upper
bound gives `q_k<=(M/(delta gamma))rho^k q_0`, including the constant
and the direction of the inequality. Positivity of the final integer
then gives the stated logarithmic bound on the number of returns.
Replacing the first contact by the original source is valid by ordinary
harmonic monotonicity along the initial actual excursion.

In the inverse direction the same comparison gives
`x_j>=(delta gamma/M)rho^(-j)x_0`. With the specified ceiling `J_0`,
indices `j=J_0+ell`, `ell>=1`, obey `x_j>=exp(kappa ell)`.
The first `J_0+1` terms cost at most `(log 3)^(-A)` each, and the
remaining terms are bounded by `kappa^(-A)sum_(ell>=1)ell^(-A)`.
The integral bound `1+1/(A-1)` is correct for every real `A>1`.

This is a uniform series bound in **contact index**. The note correctly
does not insert that index in an estimate whose error depends on the
full ordinary prefix length. The conditional excursion implication uses
the correct square moment and the denominator `1-sqrt(rho)`.

## Combined closure attempt

The companion `EXCURSION_RESOLVENT_INTERFACE.md` was also inspected.
Its source-preserving identity `R(1)S eta=S_T eta` is correct: the
immigration weights telescope to one minus the actual path product.
Its uniform comparison `delta S eta<=S_T eta<=S eta` proves positive
last-contact sources survive that correction.

The stronger maximal-domain factorization is written separately in
`HARMONIC_KERNEL_FACTORIZATION.md`. Exact terminal-source accounting
and its componentwise capacity consequence are written in
`CONTACT_EXIT_ACCOUNTING.md`. These deductions impose a quantitative
contact-mass budget but do not make a positive escaping capacity vanish.
