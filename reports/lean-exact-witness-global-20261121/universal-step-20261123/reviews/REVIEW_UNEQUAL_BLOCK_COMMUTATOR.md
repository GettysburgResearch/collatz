# Internal reconstruction: unequal contracting block dictionaries

23 November 2026. Reviewer: the `global_cycle` lane. This is a separate
reconstruction of the coordinating manuscript, not an external referee
report or Lean verification. The reviewing lane suggested the stronger
two-block denominator inequality during collaboration before the
manuscript was written; full independence of idea origin is not claimed.

**Verdict: VERIFIED at the written scope below.**

Exact source:

- `research/lean-exact-witness-global-20261121/universal-step-20261123/commutator/UNEQUAL_BLOCK_COMMUTATOR.md`
- SHA256: `2a85e4a68a8ee6b5107b9cbccfc06f5e5bf8295ac2e380353ef9f65d3449ebde`
- Frozen parent: PR177,
  `f47a5ec51aa5853f104013a6d5046d6220ff7423`.

The verdict applies to UC-D, UC-2, the pure-even extension, and the
fixed-k sparse-defect corollary UC12. It does not establish a covering
dictionary for arbitrary Collatz cycles, exclude individual constant
boundary cycles, or extend to expanding blocks.

## 1. Common residue from the complete closed path

I reconstructed the argument directly from
`Q_i x' = P_i x + C_i`, `d_i = Q_i - P_i > 0`, and
`s | d_i C_j - d_j C_i`.

When the reference block contains an odd bit, its `d_0` is coprime to
both 2 and 3. Thus `a = C_0/d_0 (mod s)` exists, and the commutator
divisibility gives `d_i a = C_i (mod s)` for every label. Subtracting
this fixed residue gives the printed edge congruence.

The intermediate Q_i are not inverted modulo the possibly even s.
Composing the whole closed word gives the coefficient

`D = product(Q_i) - product(P_i)`

on `x-a`. When the used word has positive odd count, D is coprime to
six. Cancelling D, not a branch denominator, forces every boundary
state into the same ordinary integer residue modulo s. The argument
uses the complete closing identity; only the complete coefficient's
coprimality with six is needed for this consequence.

## 2. Minimum corner, arbitrary visits and switch counts

A nonconstant finite cyclic integer sequence has an entry into its
minimum from a larger state and an exit from its minimum to a larger
state. The visits may differ when the minimum has plateaus. Thus no
unproved primitive-period assumption is needed.

Writing the two neighboring values as `m+s alpha` and `m+s beta`, with
both alpha and beta positive integers, the literal equations give

`C_i = d_i m - P_i s alpha`,

`C_j = d_j m + Q_j s beta`.

Eliminating the same m gives exactly

`E_ij = s (d_i Q_j beta + d_j P_i alpha)`.

Both d_i,d_j are positive, so this is at least

`s (d_i Q_j + d_j P_i) = s (Q_i Q_j - P_i P_j)`.

The pair has positive E_ij automatically. The strict dictionary
hypothesis therefore contradicts it. The proof is uniform in the
number, order, frequencies, lengths, and positive odd counts of the
chosen blocks, under the stated dictionary assumptions.

## 3. Two blocks, constants, and the sharp boundary

For distinct fixed points, a path using both labels cannot have constant
boundary value: that would solve both `d_i m = C_i`. Using the complete
6-smooth part of the positive commutator therefore proves UC11 with
the full two-block denominator.

For equal shapes, the factor `Q-P` is coprime to six. Hence
`delta_* = (Q-P) Delta_*`, and cancellation gives exactly the other
lane's all-period threshold `Delta_* >= P+Q`. The stronger
period-dependent equal-shape gcd statement is correctly left separate.

If all commutators vanish, all affine fixed points coincide, and the
composition of strict contractions about that point has only that fixed
point. This separately handles the zero-gcd case.

The abstract sharpness example is arithmetically correct:
`4 -> 3` under `3x/4`, and `3 -> 4` under `(3x+23)/8`.
Its commutator and two-block denominator both equal 23. The manuscript
explicitly states that these carries are not a pair of actual Collatz
parity blocks; no counterexample to Collatz is suggested.

## 4. Pure-even extension

The extension does not incorrectly claim that every pure-even block's
`d_i` is a unit modulo three. It chooses a reference label with positive
odd count. The reference d_0 alone is inverted, after which the shared
residue follows for every label, including pure-even ones. The used
word's total odd count makes the full closing D a unit modulo six.

A used word containing only pure-even blocks cannot be a positive
closed path, because it strictly decreases its positive input. Thus
the remaining exception is explicitly and correctly separated.

## 5. Sparse defect UC12

Let u have data `(P,Q,C)` with Q>P, and let t have data `(R,S,B)`.
The chronological convention gives

`C(u^k t) = R C (Q^k-P^k)/(Q-P) + Q^k B`.

Multiplication by `Q-P` and subtraction of
`(S Q^k - R P^k) C` cancel the P^k terms and leave precisely

`Q^k ((Q-P)B - (S-R)C) = Q^k E`.

Thus its part coprime to six is independent of k. Since Q>P>=1 and
Q>=2, both `S Q^k-R P^k` and `S Q^(k+1)-R P^(k+1)` tend to positive
infinity. For every sufficiently large fixed k, both dictionary blocks
contract and UC11 excludes all mixed closed integer paths over
`{u,u^k t}`.

If u is pure-even, nonzero E forces t to contain an odd bit, so every
mixed used word still has positive odd count. If both words were
pure-even, E would be zero and the stated hypothesis would fail.

The scope sentence distinguishing each fixed k from a new infinite
dictionary containing all k is necessary and is present. Pure repetitions
of either word remain outside the mixed-path exclusion.

## 6. Unproved extensions retained

- No universal decomposition of a hypothetical cycle into a suitable
  contracting dictionary was obtained.
- A positive coefficient d_i is essential to the minimum-corner lower
  bound. The ordinary odd one-step branch violates that hypothesis.
- A constant boundary path still requires its own full one-block
  integrality and physical replay analysis.
- These written deductions are not extra Lean declarations.

No source modification was made by this review.
