# Second six-hour checkpoint: reconstruction and evidence boundary

This is a review of the files frozen by the second checkpoint manifest. It is
not a proof of Collatz and does not extend to later edits or other PRs.

## Closed correction support: VERIFIED WITH EXPLICIT ANALYTIC INPUTS

The root reconstructed `escape/CLOSED_CORRECTION_SUPPORT.md` from the selected
joint floor in Weaver 12, Lemma 13 and the bridge in its Theorem 14. Summing the
central negative-binomial window gives a depth-independent multiplier mass.
Removing the last letter costs at most the total single-letter multiplier 3
and ensures unit endpoints. The trace floor then bounds the canonical
probability of bounded real offset at every selected-cylinder root. A genuine
one-letter inverse bridge transfers it to every positive odd unit root `y`,
with the actual estimate `h(y)*mu_y([0,C*y/M]) >= c*y/M` for `M>=y`.

At a fixed ordinary root the first-hit correction `s` increases by `s(x)/(3*x)`
on each edge. Conditioning one fixed canonical inverse probability on the
specific prefix to the true edge target transfers the local mass estimate to
an interval of radius `O(1/x)` around every crossed phase. Uniform reciprocal
packing bounds `s` away from zero. Differentiation of a singular finite measure
then leaves only finitely many distinct crossing integers at almost every
phase. Every first-hit path below that phase crosses one of these finite
edges, so all its correction values lie below their maximum lower endpoint.
The resulting left gap contradicts a density point of a positive-length
closed range. The argument includes finite first-hit words on zero-probability
exceptional rays; it does not replace the closure by an almost-sure carrier.

The component version uses one bilateral corrected-mark law and the exact
grade flux `h(y)*F(y)/y`, rather than separately chosen root probabilities.
Each actual forward product tail tends to one, giving the necessary eventual
crossing. The same local mass and differentiation argument applies.

Retained inputs are the source-qualified joint floor and bridge, all-unit
trace floor, canonical inverse-path law and its normal gap frequencies,
qualitative synchronization/singularity theorem, and uniform reciprocal
packing. The proof resolves the closed-support length question singled out in
Weaver 175 §12 under those inputs. The review does not independently reprove
the complete external analytic chain. Root 1 itself is a positive-density
basin with null closed correction support, so nullity is not asserted to
exclude an escaping component.

`root/ClosedSupport.lean` formally checks the abstract finite-crossing argument,
the gap in the closed range, and countability outside an explicitly supplied
exceptional set. Its final theorem keeps normalized local mass and its
vanishing outside that set as premises. It does not formalize the singular
probability, differentiation theorem, or their Collatz realization. The
topology is explicitly an order topology on the reals and second countable.

## Graded correction sets: VERIFIED WITH THE STATED ESCAPE INPUTS

For distinct fixed-grade states, heights tend to infinity along a subsequence;
the edge correction tends to zero, putting every accumulation point in the
next grade closure. Conversely each unit target has infinitely many legal
unit parents and their marks converge to its mark. Uniform reciprocal tails
above a height cutoff imply uniform convergence of high-grade corrections to
one. Equality of correction values at two unit vertices would make their
integer ratio a `2,3`-unit; because both are odd ternary units, the vertices
must coincide. These facts give the stated countable compact sets, derivative
ranks, and intersection `{1}`.

The level multiplicity uses the **actual** forward walk `2*k-S_k`, whose up
jumps are at most one and whose lower linear drift follows from `P(a_k)>1`.
At the hit of a prescribed integer level, the source-qualified selected joint
floor supplies many actual inverse words of exact total `2*k`, after one
bounded bridge. Their endpoint, grade and corrected height agree exactly.
Distinct words produce distinct sources by deterministic forward dynamics.
This is a conditional structural theorem, not a vanishing-charge argument.

## Primitive characters: VERIFIED AT THE WRITTEN ALGEBRAIC LEVEL

The root checked the conductor split of the original-law Dirichlet series,
the geometric character factor `1/(2*chi(2)-1)`, and the primitive Gauss-ratio
matrix. Its columns satisfy `J*J=3I`; treating the rows as orthogonal would be
incorrect. The discrete-log normal operator is the cyclic kernel obtained by
periodizing `2^(-|d|)` on the actual allowed sites. Its two-site blocks have
eigenvalues above and below one. This supports the stated absence of a simple
norm contraction, and proves no sign for the Dirichlet functional.

`global/check_primitive.py` checks the Gauss ratio, original-law recurrence,
conductor separation and tight-column identities over exact finite fields,
and the Gram entries over exact rational numbers at `q=9,27,81`. The root
replaced optimizable Python `assert` statements by explicit checks, then
replayed both normal and optimized Python. Both complete JSON payloads match
the retained record byte for byte. These finite-field identities are controls
on the written proof, not a substitute for its all-level complex identities.

## Canonical births: VERIFIED WITH FIXED-DENSITY INPUT

The signed shortcut preserves the negative and nonnegative half-lines.
Combining this with exact affine translation proves equality of every integer
threshold and hence the high quotient. The representative-window criterion
therefore concerns true positive sources with unrestricted gap exponents.
The binary prefix bijection gives the stated binomial octave counts.

For each fixed parent prefix the unique new lift in octave `r` is
`2^r+[-lambda] mod 2^r`. Substitution gives its exact corrected reciprocal
weight `2^(-b-r)/(2*q*(1+u_r))`. This identity is essential: bounded comparison
with octave weights does not preserve a signed inequality. Approximation of
the original ternary density by a fixed level in `L1`, followed by CRT on the
complete representative interval, gives the independent real/binary limit.
The three last-gap expectations `0,-3/4,-5/4` sum with geometric octave weights
to the strictly negative entrance current `-log(2)/2`.

The incoming trace tests the **next** gap. That current is zero in the stated
limit, not the negative last-gap value. For ages `s<=c*n`, choose
`2*c<d<log2(3)` and retain `d*n` binary digits. CRT total variation decays at
every fixed ternary approximation; the geometric clock exceeds those digits
with vanishing probability. On the retained large-height set, actual survival
factors tend uniformly to one. This justifies the growing-age cancellation.
It does not include all earlier cohorts, so the total linear trace sign is
still open. `CanonicalBirths.lean` proves only the exact signed translation,
threshold, quotient and representative-window statements.

## Bounded-cycle quotient and coloring control: VERIFIED AT THE STATED SCOPE

For the source-specific bounded alternative, replacing a phase by
`v=(x-(-1)^previousGap)/6` gives a positive integer smaller than the original
minimum and with good `v` and `3*v`. Direct substitution produces alternating
nonzero `+1,-1` defects; homogeneous run compression preserves the exact clock.
The negative defect cannot be discarded. The cyclic product comparison rules
out straightening all defects to positive forcings at smaller heights while
retaining the same total counts. `TernaryQuotient.lean` checks the finite
arithmetic only; the bounded-alternative input and goodness remain cited.

The coloring extension explicitly allows finitely many exceptional edges.
The actual ancestor indicator of 5 gives a nonconstant positive-density
control. It shows why the asymptotic compression and fixed additive-pattern
properties alone cannot establish constancy of an exactly invariant coloring.

## Executed verification

`LEAN_SECOND.json` records nine modules built into fresh temporary project
objects against pinned Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. All 73 public theorem inventories
contain only `Classical.choice`, `Quot.sound`, and `propext`. Warnings were
errors and automatic implicit variables were disabled. Cached external
dependency objects were reused. The analytic arguments above are not included
in that formal count. `global/primitive_root_replay.json` records the exact
finite checker replay and source identities. Complete-checkout repository
validation is recorded separately from mathematical review.
