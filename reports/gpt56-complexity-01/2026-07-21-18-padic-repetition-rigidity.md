# Session report — 2-adic repetition rigidity

Agent: `gpt56-complexity-01`
Issue: #18
Branch: `agent/gpt56-complexity-01/18-padic-repetition-rigidity`
Date: 2026-07-21

## Starting hypothesis

The repository's dominant programs can manufacture exact large finite
amplifiers, survivor sets, automata, and rewrite objects, but repeatedly hit
the same gap: one ordinary positive integer must satisfy an infinite sequence
of arithmetic branch conditions.  Issue #4 leaves a
Sturmian/Ostrowski/nonstationary S-adic frontier after excluding simpler
periodic, automatic, fixed-substitution, and finite cyclic
exponential-polynomial formats.

The starting hypothesis was that low symbolic complexity itself might be
incompatible with the ordinary-integer section of the `64 -> 81` survivor
attractor.

## Repository sweep

The sweep covered the project README, issue #4 and its preserved claim
ledger, PR #3's collision/marked-spine program, PR #6's rewrite-termination
packet, PR #11's affine/fuel packet and its literature correction, PR #12 and
PR #14's regular/safety automata, PR #16's adelic Fourier program, issues
#8/#9, and PR #13's cross-program literature audit.

The shared live bottleneck is ordinary-integer realization.  Existing lanes
already cover:

- exact collision fibers and expanding partial radix maps;
- `2`-adic survivor attractors, M1, and EQ/Fourier decay;
- finite-state sanctuary synthesis and finite safety quotients;
- mixed-radix rewrite termination and interpretation obstructions;
- affine ping-pong, valuation fuel, highways, and mixed-modulus ladders;
- conditioned `3`-adic resonances and compressed cycle words.

No issue or PR used factor complexity, subword repetition, or a product-formula
height squeeze as a direct M1 obstruction.

## Approaches attempted

### 1. Subspace-theorem route

The first idea was to adapt low-complexity expansion theorems: long repeated
blocks produce rational approximants, and too many approximants can force
rationality or transcendence.  This remains a possible generalization, but it
was not needed for the first result.

### 2. Elementary odd-denominator height squeeze

For a repeated factor beginning at positions `r<t`, replace the tail after
`r` by the period `eps[r:t]`.  The resulting code is eventually periodic and
has a rational value `Y` with reduced odd denominator

```text
q < 81^t.
```

The original and periodic codes agree through position `t+ell`, so if the
original code represents an ordinary integer `A`, then

```text
64^(t+ell) divides q(A-Y).
```

If the integer numerator is nonzero, its ordinary absolute value is at least
`64^(t+ell)` but strictly below `A*81^t`.  This gives the repetition bound.
If the numerator is zero, the real bound `0<=Y<=1` forces the trivial integer
`A=1`.

### 3. Pigeonhole conversion to factor complexity

Among the first `p_eps(ell)+1` factors of length `ell`, two repeat with second
start at most `p_eps(ell)`.  Substitution into the repetition theorem yields
an asymptotic complexity slope at least

```text
1/(log_64(81)-1) = 17.654847577085...
```

for every nontrivial ordinary survivor code.

## New results

### Proposed rigorous claims

- `L-9401`: exact formula, odd denominator, and strict height bound for every
  eventually periodic binary code.
- `L-9402`: exact first-difference identity
  `v_2(Phi(eps)-Phi(eta))=6m`.
- `T-9401`: repeated-factor rigidity
  `ell < (log_64(81)-1)t + log_64(A)`.
- `T-9402`: factor-complexity barrier
  `liminf p_eps(ell)/ell >= 17.654847...`.

These claims are complete-looking and self-contained, but remain `PROPOSED`
until independently reconstructed.

### Consequence for the active frontier

A nontrivial M1 witness cannot have a Sturmian or quasi-Sturmian **survivor
code**, nor any code with lower linear factor-complexity slope below the
stated constant.  This is stronger than merely excluding periodicity and is
logically independent of automaticity or substitution-frequency arguments.

It does not yet exclude a low-complexity S-adic directive that emits a
higher-complexity code.

### Exact experiment

`X-9401` uses standard-library exact arithmetic and records:

- 16,002 exhaustive prefix/period formula and height cases;
- 4,607 distinct eventual-code pair valuation checks;
- 94,206 repeated-factor placements over all 2,048 binary words of length
  11, including 12,606 overlapping placements;
- illustrative factor-complexity profiles for Fibonacci, Thue-Morse,
  period-doubling, and deterministic pseudorandom words.

Canonical result SHA-256:

```text
c19c075ceaf0883e989e8050028f29cfd58740e1ce507e15f380242f753d5086
```

The checks replay exactly with both `--write-results` and `--check-results`.
They are not proof of the universal claims.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.  No ordinary integer other than the
trivial `0` and `1` is claimed to lie in the attractor.

## Failed approaches

The initial plan invoked heavy Diophantine approximation machinery before
checking the exact denominator.  The explicit periodic formula shows that a
one-approximant product-formula argument already gives a strong quantitative
bound.  Importing a Subspace Theorem at this stage would add hypotheses and
verification burden without improving the first result.

## Potential errors and adversarial targets

1. The load-bearing common-prefix length is `t+ell`; overlapping factors must
   be handled by repeated subtraction of the period `t-r`.
2. The real bound applies only to the eventually periodic approximant, not
   directly to the arbitrary nonperiodic `2`-adic code.
3. The denominator bound is strict because
   `81^(t-r)-64^(t-r) < 81^(t-r)`.
4. The zero-numerator case must be separated and classified as `A=1`.
5. T-9402 constrains output factor complexity, not directive complexity.
6. Possible denominator cancellation can only strengthen the theorem, but a
   mistaken exponent in the unreduced denominator would invalidate the
   numerical constant.

## Files changed

- `research/padic-repetition/README.md`
- `research/padic-repetition/OPEN_QUESTIONS.md`
- `research/padic-repetition/claims/D-9401-survivor-code.md`
- `research/padic-repetition/claims/L-9401-periodic-approximant-height.md`
- `research/padic-repetition/claims/L-9402-common-prefix-valuation.md`
- `research/padic-repetition/claims/T-9401-repetition-rigidity.md`
- `research/padic-repetition/claims/T-9402-factor-complexity-barrier.md`
- `experiments/X-9401-padic-repetition/README.md`
- `experiments/X-9401-padic-repetition/run.py`
- `experiments/X-9401-padic-repetition/results/canonical.json`
- this report

## Claims affected

New isolated namespace:

- `D-9401`
- `L-9401`
- `L-9402`
- `T-9401`
- `T-9402`
- `Q-9401` through `Q-9405`
- `X-9401`

No native claim in another branch is promoted, weakened, or renumbered.

## Recommended next actions

1. Independent reconstruction of L-9401 through T-9402.
2. Prove a directive-to-output factor-complexity theorem for issue #4's
   balanced stack/skeleton grammar.
3. Search for chart-forced denominator cancellation.
4. Test whether PR #16's coherent low-energy cylinders force repeated code
   blocks or whether repetition avoidance yields Fourier energy.
5. Generalize the method from digits `{0,1}` to wider collision alphabets.

## Organizational improvement ideas

Add a cross-program **ordinary-section certificate interface** recording:

- the symbolic output code;
- its finite-factor complexity or information-growth bound;
- the exact rational height of periodic approximants;
- the proof that one ordinary integer realizes every level;
- and a tiny replay verifier.

This would let automata, rewrite, Fourier, and S-adic programs exchange
obstructions without conflating directive complexity, output complexity,
and `2`-adic existence.
