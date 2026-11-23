# Independent review of the critical carry transfer

Date: 2026-11-23. Reviewer: the integer-cycle lane.

**Frozen source:**
`/workspace/scratch/957bb0caa6f2/risk25/endpoint/CRITICAL_CARRY_TRANSFER.md`,
SHA256 `cc45bcd43a450405b7b7cd12dd67fab45d43ac32caac3d875f5fdc5dca04b03d`.
The local bytes were hashed and matched this pin before completing the
review. The verdict applies to those bytes and the stated claims only.

## Verdict

**VERIFIED at the written finite-argument level** for Lemma 1, Theorem 2,
the widening-strip estimate, and Theorem 3. **VERIFIED with the explicitly
retained source hypotheses** for Corollary 4: the stationary lift and
strict collision gap are supplied by the pinned PR180 argument, and the
finite inverse law retains its qualified ordinary harmonic-flow input.
No escape exclusion or upper estimate for the actual word energy and
remainder has been proved.

No change to the frozen mathematical claims is required. The exact
finite controls and external primary-literature proof chains were not
re-executed as part of this review. The review reconstructs the written
arguments and inspects their repository dependencies.

## 1. Balanced family and complete-carry counting

For a positive gap composition of total `A`, the centered prefix sums
have total zero. Starting after a maximum among indices `0,...,m-1`
makes every cyclic centered prefix nonpositive, including wrapped
prefixes. Consequently all words lie in the union of the `m` rotation
images of the balanced family. Periodic words do not invalidate the
lower count `|B|>=binom(A-1,m-1)/m`.

The rotation is used solely in this counting argument. No endpoint
identity for an unchanged ordinary orbit is transported through that
rotation.

If `A<=m log_2 3`, every complete-carry term satisfies
`2^(a_i)/3^i<=1`, including the initial term. Thus `C_w/3^m<=m/3`
and its integer quotient has at most `1+floor(m/3)` possibilities.
At fixed `(A,m)`, an endpoint residue fixes the remainder of `C_w`
because `C_w=2^A rho mod3^m`. The parity decoder then reconstructs
the entire fixed-length shortcut word from its complete carry. Keeping
the integer quotient is essential; it is kept here.

This proves the claimed residue-fiber bound without independence,
random gaps, or loss of the large carry. The exact source congruence in
(10) also enforces the final odd bit, so it supplies legal finite
ordinary paths with exactly the specified valuations. CRT allows a
positive representative prime to three. These are changing finite
witnesses, not an all-time source.

## 2. Critical exponent and widening strip

With `A_m=floor(m log_2 3)`, Stirling's estimate gives
`binom(A_m-1,m-1)>=c m^(-1/2) exp(m Phi(log_2 3))` uniformly after
absorbing finitely many small `m`. The bounded displacement from the
critical slope changes the exponential by an absolute factor. The
balanced-family loss contributes one factor `m`, and the number of carry
quotients contributes another. This gives exactly the stated `m^(5/2)`
upper prefactor, at the full modulus `3^m`.

In the widening family, the actual endpoint includes the last prefix
constraint, and the fixed-total carry bound becomes `m 2^s/3`.
There are at most `2s+1` totals. Summing the fiber bound over totals
therefore gives the exact `R_(m,s)` in (12). The balanced critical family
is a subset, yielding the asserted denominator lower bound. For
`s=o(m)`, all additional logarithms are `o(m)`, so the critical exponent
survives with a subexponential prefactor.

## 3. Full actual law, repeated words, and omitted mass

The retained weights are the literal masses
`t_j=v_j/[N v_(r+j)]` of the original forward states in the full inverse
law. They satisfy `0<t_j<=1/N`; no normalization to the retained mass
is made. The original escaping ray is injective, so the decomposition
of the remaining mass into off-spine, early, and bad-word contributions
is exact and nonnegative.

Every unchanged chronological past word determines the corresponding
endpoint residue. Repeated occurrences of the same word are first
combined into `p_w`; their cross terms remain inside `sum p_w^2`.
Cauchy's inequality on a residue fiber of at most `R` distinct words
gives retained squared norm at most `R sum p_w^2=(R/L)J`.
The omitted positive measure has Euclidean norm at most its mass
`tau`. The Euclidean triangle inequality therefore gives (16), with
all cross terms retained through the square of the sum.

This is an exact comparison on the full endpoint law. In particular,
its word-energy factor `J` has not been replaced by the number of legal
words, a source-box count, or a fresh uniform law. Its expression as
an `L^2` density and its one-power bounded-density consequence are
correct for a subprobability.

## 4. Stationary original-source consumer

I inspected PR180 at
`a436db7b85f37abafea25f42d6f34afed02a29c0`,
`research/whole-source-20261123/COLLISION_CORE.md`, especially Sections
2--4 and 7. The tightness argument gives genuine probability block
limits, consistency under both coordinate deletions gives stationarity,
and chronological reversal of a finite block converts its ternary
coding exactly into `rho_m(w)`. This is reversal of notation for the
past word, not cyclic rotation.

The strict collision gap has two exhaustive cases: one finite Shannon
deficit propagates by subadditive blocking; absent such a deficit,
the geometric product law is forced by equality in relative entropy,
and its Renyi-2 exponent is strictly below its Shannon exponent. The
process-dependent positive gap is therefore the appropriate dependency
for (19). No universal gap is inserted here.

Combining its lower bound with (18) is algebraically correct. If the
omitted mass is less than half the square root of that lower bound,
the retained term must exceed the other half. Squaring and using the
reference estimate gives exactly the alternative (20), including its
one-quarter coefficient and exponent `epsilon_mu m-u_m`.

An upper bound `J_m<=exp(o(m))` together with
`tau_m<=exp(-Phi(ell)m/2+o(m))` would contradict the fixed positive
stationary gap. Neither upper bound is supplied. Merely knowing that
`tau_m` tends to zero would not suffice.

## 5. Precision and retained limitations

The finite diagonal condition is correct: a retained ordinary diagonal
of order `1/N` cannot be `o(sqrt(m)3^(-theta m))` unless
`N sqrt(m)/3^(theta m)` tends to infinity. The range `m^2=O(M)`
by itself does not ensure this. The stationary argument takes the time
limit at fixed resolution first and does not claim a quantitative
exchange with a growing resolution.

I also inspected the complete-carry decoder and weighted accounting in
PR182 at `a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/ACTUAL_COLLISION.md`. The use here
preserves its fixed-clock and complete-carry hypotheses. The original
ordinary harmonic-flow construction and the three external literature
sources remain qualified as in the frozen note; this review does not
independently certify those full constructions.

The precise first unsupported step is an upper estimate for the literal
actual chronological-word energy `J_m` and discarded mass `tau_m` at
the displayed rates. All finite reference-family and transfer claims
remain strictly on their stated side of that boundary.
