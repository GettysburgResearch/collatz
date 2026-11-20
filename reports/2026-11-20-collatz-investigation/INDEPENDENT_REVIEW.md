# Independent review and exact verification scope

**Outcome:** the arguments D1–D4 in `DERANDOMIZATION.md` pass this review.
The explicit 13/6 inverse-cone certificate and the newly regenerated small
positive-policy certificate also pass separate exact checks. No claim of
forward Collatz convergence, formal verification, or literature priority
follows from this review.

## Mathematical argument reviewed

- **D1:** weak compactness of the Cesaro occupation measures, the Feller
  property, and uniqueness of the stationary law give uniform convergence
  for every continuous observable. The proof permits the starting states
  to vary with the horizon, which is the essential quantifier.
- **D2:** the minimum-cost operator preserves finite pointwise minima and
  commutes with constants. Therefore
  `V = min(0,F0,...,F^(N-1)0)` satisfies `FV <= V` when `F^N0 <= 0`
  everywhere. Shifting gives a nonnegative integer potential. An extra
  source digit makes its selected action valid for every hidden lift;
  the extra digit must not be omitted.
- **D3:** uniform convergence applied to the expected exponent gives a
  finite horizon with negative expected adjusted cost at every supplied
  state whenever the requested rational slope strictly exceeds the
  stationary mean. A minimum legal word cost is at most this expectation.
  D2 then yields a deterministic robust certificate. No exceptional
  starting states or changing ordinary sources are discarded.
- **D4:** adding fixed positive legal-action noise to a certified
  deterministic selector produces a positive local policy. Integration
  against its stationary law cancels the bounded potential. The remaining
  error is bounded by the noise probability times a fixed finite constant.
  Taking arbitrarily small positive noise proves equality of the two
  infima. Continuity of stationary laws as the noise vanishes is not used.
  Attainment of either infimum is not asserted.

The inverse-cone terminal cost was checked separately. For slope `p/q`,
the final integral inverse exponent is at most two, so the safe rank is
`p*s + W(c) + 2*q - p`. In particular the 39/20 corollary requires the
displayed `+1` offset. The common-prefix and positivity argument from the
explicit certificate applies unchanged. These statements concern inverse
conversion, not a decreasing rank on a forward Collatz orbit.

## Explicit 13/6 certificate

A separately written scalar verifier, importing neither the synthesis
routine nor the main verifier, checked all 354,294 unit rows and all
1,062,882 selected-action lifts. It found the same action counts, maximum
potential 66, and minimum terminal credit one. The all-zero potential was
rejected at residue five.

The packet's standalone verifier was also run successfully, including
6,575 forward affine cone replays through all unit tails of length eight
and selected tails of lengths 40, 100, and 1,000. These affine replays test
all prefixes simultaneously within each selected cone. The proof of the
universal family remains the all-lift arithmetic and rank argument.

## Newly regenerated positive policy

The small positive-policy input was independently synthesized with a
162-cell finite policy iteration. It is not a claimed byte-for-byte replay
of the external paper's unavailable supplemental file. Floating arithmetic
proposed the labels and bias only. The final certificate consists entirely
of integer data, and `verify_small_policy.py` uses only the standard library
and exact integer arithmetic.

The policy reads 486 unit residues modulo 729 and uses both legal cap-six
actions with probabilities 99/100 and 1/100. The verifier reconstructs
every matrix row over the 162 cells modulo 243 by averaging the three
next-digit lifts. It verifies the legal actions, stochastic row sums,
strict positivity of the fifth matrix power, and all rational bias bounds.
The exact extreme bias expressions are

\[
\frac{145286986313}{75000000000},\qquad
\frac{96857990939}{50000000000}.
\]

Both lie strictly between 1937/1000 and 969/500. Averaging against a
stationary cell vector cancels the bias and proves the same bounds on its
stationary mean exponent. Zero-bias and zero-label mutations are rejected.
The certificate SHA-256 is

```
9a9545c9cfc2e6e178b773c9ce255ef4b183e96cc3037e97bb67eb1050f9d6df
```

The finite matrix describes exactly the action on laws whose conditional
tails beyond precision five are Haar. It is not the residue Markov chain
of an arbitrary supplied integer. Consequently this finite verification
does not, by itself, supply a robust pointwise credit inequality.

## External dependency and remaining boundary

[Paper 127, version 1, Theorem 5](https://rstation.ai/problems/collatz/papers/127)
was read directly. Its hypotheses match the packet's `UQ(R)`: exponent cap
at least six, strictly positive probabilities for every legal action, and
finite ternary precision. Its infinite-dimensional uniqueness theorem has
not been independently reproved or formally checked here. The exact small
policy input no longer depends on retrieving its supplement, but the
sub-two robust-certificate existence conclusion still depends on `UQ(6)`.

No numerical horizon, residue precision, or maximum potential for a
39/20 robust certificate has been obtained. D1–D3 establish its existence
and justify an exhaustive search that eventually finds one under the
stated uniqueness hypothesis. The explicit supplied robust table remains
the separately verified 13/6 table. Neither result closes the forward
Collatz problem.
