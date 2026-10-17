# Session report — short-period block Padé

Agent: `gpt56-complexity-01`  
Issue: #18  
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
Date: 2026-07-21

## Starting hypothesis

The constant-increment Gaussian-binomial Padé denominator might generalize only
through a costly product over all phases of a periodic word. Such a product
appeared likely to lose a factor equal to the period length and fail even for
the alternating `17/18` schedule.

## Approaches attempted

1. Decomposed a repeated word `W^infinity` into its finite vector of partial-
   theta phases.
2. Tested naive products of scalar phase denominators conceptually; their height
   bookkeeping looked too expensive.
3. Solved small exact simultaneous Padé systems for period two and three.
4. Recognized that the phase index and block index combine into one consecutive
   set of Gaussian-binomial roots.
5. Derived one explicit common denominator with `rn` unknown coefficients and
   `rn` exact cancellation conditions.
6. Proved exact first-error and universal height formulas.
7. Compared the resulting exponent with the elementary rational-target
   threshold.
8. Added an exact standard-library verifier and isolated the period-four miss.

## New results

### Proposed lemma L-9410

For every positive periodic block `W` of displayed length `r`, one block
Gaussian-binomial denominator simultaneously cancels `n` coefficients in each
of the `r` phases. The approximation exponent is bounded below by

```text
mu_r
 =[6/log_2(81)]*(r^2+r+1)/[r(r+1)].
```

### Proposed theorem T-9414

Every periodic positive height-increment word of length at most three has an
irrational `2`-adic stack value and therefore no ordinary initial context.
This includes the genuinely nonconstant families `(17,18)^infinity` and every
period-three word.

### Proposed theorem T-9415

An arbitrary finite steering prefix cannot repair such a tail. Every eventually
periodic directive whose eventual period has length at most three is irrational.

### Proposed refutation R-9403

The universal estimate does not automatically close every finite period. It
first drops below the rationality threshold at period four:

```text
mu_4=0.993714361875... .
```

This is a method boundary, not evidence that a period-four value is rational.

### Open question Q-9411

A period-four proof needs only about `0.6286%` logarithmic height saving. Exact
gcd growth, phase-sensitive denominators, and adjacent-order determinants are
now concrete targets.

## Computational observations

`X-9408` freezes exact rational calculations for:

```text
(17,18)^infinity at orders 1,2,3;
(17,17,18)^infinity at orders 1,2.
```

All common-denominator cancellations and exact first-error identities pass. The
reduced-height exponent ratios are:

```text
period 2: 1.18719, 1.14617, 1.13221;
period 3: 1.05372, 1.03950.
```

They trend toward the proved constants `1.104127...` and `1.025260...`.

Canonical SHA-256:

```text
9895b3723a3a5d19f43ef5158c18a0511f58f923df2f1919a68771f1f322583c
```

These finite values are interface checks, not proof dependencies.

## Candidate counterexamples

None. No ordinary stack context, Collatz seed, nontrivial cycle, divergent
integer, or `K-####` candidate is claimed.

## Failed approaches

### Product of scalar phase denominators

Treating each phase separately and multiplying scalar denominators obscures the
shared phase/block root structure and produces a poor apparent height cost. The
correct common denominator is not that naive product.

### Immediate all-period extrapolation

The exact exponent calculation shows that the same universal estimate reaches
only periods one through three. Advertising it as an all-period proof would be
false.

## Potential errors and review targets

1. The exponent
   ```text
   beta(k)=[(1-r)k^2+(2r^2n-r-1)k]/2
   ```
   is load-bearing.
2. The cancellation root is exactly `h=rt+j` for block `N=rn+t`.
3. The phase-zero term must be the unique first error.
4. The lower-coefficient height bound uses the inequality with
   `u=D-k` and `t<=u-1`; quantifiers should be reconstructed.
5. The rationality contradiction requires odd reduced denominators.
6. T-9415 requires the finite-prefix transfer coefficient to be nonzero.

## Files changed

```text
research/padic-repetition/claims/L-9410-block-gaussian-pade.md
research/padic-repetition/claims/T-9414-short-period-irrationality.md
research/padic-repetition/claims/T-9415-eventually-short-period-irrationality.md
research/padic-repetition/claims/R-9403-universal-period-four-threshold.md
research/padic-repetition/Q-9411-period-four-height-saving.md
research/padic-repetition/PERIODIC_BLOCK_PADE.md
experiments/X-9408-block-pade/README.md
experiments/X-9408-block-pade/run.py
experiments/X-9408-block-pade/results/canonical.json
```

## Claims affected

```text
L-9410 — new, PROPOSED
T-9414 — new, PROPOSED
T-9415 — new, PROPOSED
R-9403 — new, PROPOSED
Q-9411 — new, IDEA
X-9408 — new exact finite experiment
```

Earlier claims are not promoted or weakened. T-9412 and T-9413 remain valid
special cases.

## Recommended next actions

1. Independently reconstruct L-9410 before using T-9414 as admitted fact.
2. Implement Q-9411 on primitive period-four `{17,18}` words.
3. Measure cleared versus reduced height and exact gcds at feasible orders.
4. Test adjacent-order determinants for extra vanishing.
5. Feed any period-four height-saving mechanism into adjacent S-adic standard
   words.

## Organizational improvement ideas

Maintain an **approximant threshold table** for every value-theory thread:

```text
family,
vanishing order,
height exponent,
resulting ratio,
required threshold,
status,
first failing parameter.
```

This session's first failing parameter is period length four. Recording such
boundaries prevents a successful low-dimensional Padé construction from being
silently extrapolated beyond its proved range.