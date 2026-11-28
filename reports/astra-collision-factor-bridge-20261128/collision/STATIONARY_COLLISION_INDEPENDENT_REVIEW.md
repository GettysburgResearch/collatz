# Independent review: stationary collision consumer

Reviewer: collision lower-bound lane. Reviewed UTC: 2026-11-28T11:08:06.956975+00:00.

**Result: the exact transfer, two-copy observable, and critical-clock identification pass independent reconstruction. The relative two-copy lower bound is not proved.**

## Source pins

- `research/astra-collision-factor-bridge-20261128/factoring/STATIONARY_COLLISION_CONSUMER.md`: `18b3dfb9ac9a0989888a486b4f629b5f75b210f9cd631612bbcdd33688a2a298`.
- `research/astra-collision-factor-bridge-20261128/factoring/CONDUCTOR_AND_STATIONARY_TRANSFER.md`: `b92579470aaea25f24ed5ab5bb076e7cc1386271e6e297a0450d1bd31c31d62d`.
- `research/astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md`: `bd9da43d81cc04abe9ced69692eeeb67ddbb72611606ae14006ced3c2642d70b`.

## Exact finite transfer

For a fixed nonnegative real seed, the full-conductor selector is the pushforward of the integer source window from floor(seed)+1 through floor(seed)+X. Integrality of the selected initial source and uniqueness of its parity word make this a genuine ordinary-source statement. The common-word affine real shift and the vanishing ternary seed term modulo the full grade conductor are both retained. The second seed coordinate need not be independent of the first, but the seed must be independent of the future word.

Coupling overlapping source windows bounds the total variation of the entire endpoint/grade law, with no sum of errors over bins. Projecting to endpoints preserves that bound. Two independent copies of the same coupling give the stated twice-total-variation collision-energy error.

For biased words, the inverse word-probability factor is necessary in each copy. Conditioning on a word cancels exactly its probability, leaving the unweighted ordinary count. The two grades must remain attached to their own final real and ternary coordinates. The fair case has constant reciprocal weight, as stated.

The intersection count is correct for the half-open real interval and nested ternary moduli, including grade zero. Compatibility modulo the smaller conductor chooses the residue of the larger conductor. When X is at most two to the clock, the real intersection has length at most the larger modulus and contains at most one selected integer.

## Clock and object comparison

The endpoint energy is precisely the equality probability for two independent positive uniform sources through X at one common shortcut date. It matches the object in the pinned synchronous phase-dispersion note. The median clock is floor(mu log X), with mu=2/log(4/3) and natural logarithms. Since mu log 2 is greater than one, this clock is beyond the initial binary-information horizon for large X, so the indicator version of the two-copy formula applies.

Writing rho=X/2^h, the fair formula is collision energy = Pr(J=1)/rho^2, up to the displayed vanishing source-window error. The required lower estimate is therefore relative to rho squared. At the median clock, rho=X^(1-mu log 2+o(1)); a merely vanishing absolute error, a fixed-conductor mixing assertion, or an unconditional endpoint marginal does not give the requested precision. The external phase-dispersion and positive-predecessor inputs remain source-qualified; this review does not reprove them.

## A useful exact normalization check

For each fixed initial joint seed, exactly X of the 2^h fair words pass the one-copy selector when X<=2^h. This is because an interval of X consecutive integers contains X distinct parity classes modulo 2^h. Consequently the acceptance event K is independent of the initial seed, and has probability rho exactly. This does not imply independence of K from the final stationary state or from the grade.

For two independent paths, J=1 means both one-copy selectors pass and their unique ordinary endpoint labels agree. Thus the unresolved estimate is exactly a collision lower bound for those selected labels. This interpretation preserves the small-probability normalization; it does not evaluate the conditional endpoint law.

## Scope

The probability and two-copy statements are written proofs. The separately compiled finite interval kernel is narrower than these analytic assertions. No new stationary mixing estimate or one-eighth lower bound is certified by this review.

Review pin refreshed after inspection of the explicit median/common-clock paragraph and its small-probability exponent. The added paragraph agrees with the clock reconstruction above.
