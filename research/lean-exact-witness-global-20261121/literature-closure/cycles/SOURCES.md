# Source and dependency scope for the cycle lane

Date: 23 November 2026. New files in this directory are written mathematics
and exact arithmetic certificates. They contain no imported Lean axiom and
make no unrestricted cycle-exclusion claim.

## Refreshed repository sources

These inspections concern the named claims and files, not an audit of all
historical work on a branch.

- **Owned PR177**, `aaa132e904e4e6d0b438e963f76d72d79e2c7f34`,
  `research/lean-exact-witness-global-20261121/CYCLE_EXCLUSION_CONTINUATION.md`:
  the complete cyclic matrix, six-state carry invariant, equivalence of
  zero termination and nonnegative integer coordinates, and rational
  controls for complementary integrality and noncrossing. The new note
  reuses this carry interface and adds actual nonnegative integer quotient
  categories to the local invariant attempt.
- **PR185**, `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
  `research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md`:
  read in full. Residual polynomial denominator growth precedes numerical
  evaluation gcd cancellation. No lower bound for the actual reduced
  denominator is imported from that theorem. The principal-factor control
  was inspected through the PR's current description and the cited peer
  analyses; this lane does not claim an independent reread of its proof.
- **PR178**, `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`,
  `research/profound-step-20261123/cycles/UNIT_EQUATION_HEIGHT_ATTACK.md`:
  read in full. Its fixed-arity unit equation retains growing rank, and
  its small-height attempt has a quantitative obstruction above `1/8`.
  The external unit-equation proofs were not independently reconstructed
  by this lane.
- **PR178**, `4e204f54136c79cf8c9393b34e3330594f99ae0a`,
  `research/global-closure-20261123/cycles/INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md`:
  read in full. It already contains the whole-state polynomial route,
  the failure of an independent-base equation for the natural nonzero
  dyadic lift, and the exact minimal isogeny degree `D/gcd(D,C)`. The
  finite-support polynomial reformulation was therefore not repackaged as
  a new result here.
- **PR182**, `b78819e95ee7d39f02022de991b42217821e7590`,
  `research/closure-round2-20261123/CYCLE_CANCELLATION.md`:
  read in full. Local complete-gcd transport, window injections, the
  balanced residue polynomial, and the moving-target hypotheses were
  retained. No new uniform gcd theorem follows from those local changes.
- **PR182**, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
  `research/whole-repo-round3-20261123/COMPLETE_CYCLE.md`:
  read in full. Its exact block matching and the failure of independence
  after zero conditioning are not reused as an unproved all-scale saving.
- **PR176**, `ff3e068fa44eb85bb918580b2e10e18c027a18e6`,
  `research/lean-global-resolvent-20261121/overview/longshot/cycles/IDENTITY_ATOM_ATTEMPT.md`:
  read in full. It already covers the full trace coefficient, support-size
  failure of ordinary mixing at the critical clock, and the relevant
  Breuillard--Varju theorem mismatch. The recorded large finite censuses
  were not rerun.

## Primary literature inspected during this pass

These sources guided attempted closures; none is needed as a black box
for the new integer identity or explicit family calculation.

1. **P. Corvaja and U. Zannier**, *A lower bound for the height of a
   rational function at S-unit points*, author preprint
   [math/0311030v2](https://arxiv.org/pdf/math/0311030).
   Theorem 1, its height/gcd equivalence, Corollary 1 and the Main Theorem
   on printed pages 1--2 were inspected directly. Their fixed rational
   functions and finitely generated group, together with the exceptional
   translates, do not provide a uniform all-word estimate for a numerator
   whose support and degree grow. The proof was not rederived.
2. **N. Grieve and J. T.-Y. Wang**, *Greatest common divisors with moving
   targets and consequences for linear recurrence sequences*, author
   preprint [1902.09109v2](https://arxiv.org/pdf/1902.09109).
   Theorem 1.2, the logarithmic gcd definition, and Example 1.3 on printed
   pages 2--3 were inspected directly. Both polynomial degrees are fixed,
   coefficient height must be little-oh of the moving argument height,
   and the conclusion retains a subgroup alternative. The favorable
   alternative is only on an infinite index subset; it is not a bound
   for every index. No growing-degree or exceptional-locus exemption was
   inferred.
3. **E. Breuillard and P. P. Varju**, *Cut-off phenomenon for the ax+b
   Markov chain over a finite field*, author preprint
   [1909.09053v2](https://arxiv.org/pdf/1909.09053).
   The model and Theorems 1--3 on printed pages 1--4 were inspected
   directly. Their fixed multiplier and independent translations are not
   the conditioned Collatz word law. The main cutoff conclusion concerns
   most primes and most multipliers under a Dedekind-zeta hypothesis.
   This lane does not assume that hypothesis, and even assuming it would
   not remove the word-law or complete-composite-modulus differences.

The new certificate was discovered using a linear-programming search,
then converted into 34 explicit local nonnegative-integer witnesses and
an integer coefficient identity. Its proof is the direct sum of these
inequalities. No theorem about numerical optimizer correctness is an
assumption of the result.

## Replay scope

Run from any working directory:

```text
python positive_carry_dual_check.py
python -O positive_carry_dual_check.py
```

The standard-library checker reads its sibling certificate file. It checks
all local witnesses and the complete symbolic coefficient identity,
rejects three corrupted certificates, and independently replays the
explicit family at `k=1,2,7,13,20`. Those five arithmetic controls do not
replace the uniform written proof of the family formula. Normal and
optimized output must be byte-identical. The saved `CHECK_RESULT.json`
is the normal output; it records the exact certificate SHA-256.

No earlier Lean corpus, large census, or remote validation gate was rerun
by this lane. Publication and the repository's required complete-checkout
validation remain with the parent agent.
