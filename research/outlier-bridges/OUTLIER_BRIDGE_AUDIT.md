# Outlier bridge audit — remote theories against the live ordinary-integer frontier

**Agent:** `gpt56-outlier-01`
**Issue:** #52
**Date:** 2026-07-23
**Repository cutoff:** active draft work through PR #51; cartography PR #38 pass 4; literature PR #13 wave 7

## Executive finding

The strongest remote connection is **sparse elimination plus non-Archimedean tropical noncancellation**.

The negative-cycle pulse correction from PR #47 is a chain-supported Laurent polynomial in variables `X_i=2^{d_i}`. The cycle denominator is one monomial minus a constant. Eliminating any `X_i` gives a degree-one sparse resultant. Collatz prefix valuations make one monomial in that resultant uniquely smallest 2-adically, so the resultant never vanishes. Its coefficient norm then bounds `X_i` independently of every other pulse height.

This yields `L-8201`:

> For every fixed negative accelerated cycle word, the complete upward pulse cone has only finitely many possible positive-cycle divisibility hits, with explicit support-wise coordinate bounds.

The result closes a structural gap between PR #51's two-pulse theorem and the arbitrary-support formulas of PR #47. It does not bound repetition length and does not construct a cycle.

## Frozen repository bottlenecks

The branch-aware sweep identified three direct interfaces:

1. **Pulse/run-core chart:** one positive forever-defined ordinary state settles the counterexample objective; finite prefixes are free but the ordinary top boundary is open.
2. **PR #49 complement counter:** one forever-defined `(t,i,k)` state gives an explicit unbounded orbit; any survivor must continually create fresh odd-prime support.
3. **Full-denominator positive cycle:** compressed valuation circuits must satisfy the complete denominator, not merely selected factors or near-integrality.

Issue #7 already covers visibly adjacent literature: parity cylinders, automata, Mahler/Fatou/Skolem–Mahler–Lech, `S`-units, rational bases, p-adic automata, Fourier decay, q-Gaussian/Hankel methods, and related tools. The search here intentionally moved further away.

## Bridge A — Sparse resultants and tropical noncancellation

### External object

A sparse resultant eliminates variables from Laurent-polynomial systems while retaining their Newton-support structure. Over a non-Archimedean field, a Laurent polynomial can vanish only where the minimum term valuation is attained at least twice.

### Native object

For fixed negative-cycle pulse support,

```text
D = U*X_1*...*X_e - Q,
H = c_0 + c_1*X_1 + c_2*X_1*X_2 + ... + c_e*X_1*...*X_e.
```

Both are linear in each individual `X_i`.

### Exact output

`L-8201` constructs the reduced resultant

```text
E_i = U*S_i*H_i^- + Q*H_i^+.
```

It proves:

```text
D | H  iff  D | E_i,
v_2(E_i)=A_(p_i+1),
E_i != 0,
X_i <= explicit support-dependent constant.
```

### Why this matters

For a fixed repeated negative-cycle packet, searching larger pulse heights or adding more pulse locations cannot reveal an unbounded resonance. The only infinite axes left in this construction class are the baseline/repetition family and any move beyond coordinatewise pulsing.

### Applicability table

| Requirement | Native status |
|---|---|
| Laurent-polynomial description | Exact from PR #47 pulse formula |
| Linear dependence on one eliminated variable | Exact chain support |
| Resultant identity | Proved directly in `L-8201` |
| Nonzero resultant | Proved by unique 2-adic minimum |
| Positive denominator | Explicitly required before cap |
| Exact valuation replay | Remains inherited from/rechecked against PR #47 formula |

### Immediate next work

- Independent reconstruction.
- Proof-producing all-support enumeration for each fixed repetition.
- Combine with PR #47 commutator or `S`-unit methods to attack repetition length.
- Search for analogous Newton-chain structure in mixed macro-block words.

## Bridge B — Catastrophic convolutional encoders

### External object

In coding theory, an encoder is catastrophic when an infinite-weight information sequence produces a finite-weight code sequence. Polynomial left-prime/minor criteria detect noncatastrophic encoders in stationary linear settings; related tests exist for periodically time-varying encoders.

### Native translation

The ordinary-integer boundary asks for precisely this kind of compression:

```text
infinite branch/directive information
    -> finitely supported high binary blocks
    -> one ordinary positive integer.
```

Any proposed bounded-memory **linear** compiler for that step is a convolutional encoder. If it is noncatastrophic, it cannot perform the required compression. If it is catastrophic, the corresponding zero-output trellis cycle is a finite algebraic object that can be examined for exact Collatz legality.

### Applicability table

| Requirement | PR #12 sanctuary | PR #49 refund | Pulse run-core |
|---|---:|---:|---:|
| finite memory | yes in searched DFA class | no, unbounded counter | no, unbounded quotient |
| linear over fixed finite ring | only after a chosen linearization | no | no |
| time invariant or periodic | potentially | changing modulus | changing run modulus |
| finite-support output criterion | exact ordinary-word semantics | exact but nonlinear | exact but nonlinear |
| direct theorem import | possible for a restricted compiler | not currently | not currently |

### Status

`METHODOLOGICAL / PARTIAL`. This is a format-level falsifier and trellis search recipe, not a current counterexample construction.

### Proposed experiment

For any candidate boundary-memory linear transducer:

1. write its polynomial generator matrix over `F_2[D]` or `Z/(2^r)[D]`;
2. compute the maximal-minor gcd / appropriate ring primeness test;
3. if noncatastrophic, close that certificate class;
4. if catastrophic, extract the zero-output state cycle and replay it through the exact Collatz transducer.

## Bridge C — Primitive divisors as the missing fresh-prime engine

### External object

Primitive-divisor theorems in arithmetic dynamics show that, under degree-at-least-two and orbit hypotheses, new primes divide later numerator terms at all sufficiently large indices.

### Native translation

PR #49 proposes that every infinite complement-counter survivor must introduce infinitely many globally new odd primes into the physical boundary words. That requirement resembles the conclusion of a dynamical Zsigmondy theorem.

### Applicability table

| Standard hypothesis | PR #49 status |
|---|---|
| one fixed rational map | absent: coefficients/modulus change with height |
| degree at least two | absent: local counter update is affine |
| fixed periodic target such as zero | not identified |
| numerator/divisor sequence from iteration | only after a new autonomization |
| infinite orbit | exactly what must be constructed |

### Status

`SPECULATIVE WITH EXPLICIT HYPOTHESIS FAILURE`.

### Concrete target

Construct a fixed algebraic dynamical system `Phi` and an algebraic observable `g` such that legal PR #49 states embed into one orbit and

```text
g(Phi^j(P)) = controlled factor of n_j+34.
```

If `deg Phi>=2` and the primitive-divisor hypotheses can be checked, fresh-prime generation could become automatic rather than an added invariant. Without this autonomization, invoking dynamical Zsigmondy is invalid.

## Bridge D — 2-adic T-functions and residue transitivity

### External object

For global 1-Lipschitz maps on `Z_p`, ergodicity is characterized by single-cycle behavior on every residue ring.

### Native translation

A future inverse address generator for the changing-modulus charts might be a compatible 1-Lipschitz map. Single-cycle residue behavior would then certify maximal address mixing and could prevent hidden finite-state traps.

### Hypothesis failure

The current forward maps divide by powers of two on thin domains and are expanding/partial. They are not global 1-Lipschitz self-maps of `Z_2`. Applying T-function theorems directly to them would be a category error.

### Status

`NEAR-MISS / POSSIBLE INVERSE-MAP TOOL`.

## Bridge E — Homoclinic points are not ordinary integers

Algebraic `Z^d` dynamics uses rapidly decaying or summable homoclinic points to code orbit structure. The repository's ordinary-integer requirement is stronger: in least-significant binary coordinates, the high tail must be exactly zero after a finite point.

Therefore:

```text
homoclinic / summable / exponentially decaying
    does not imply
finite support / ordinary positive integer.
```

This bridge is presently a useful nonapplication theorem. It prevents an attractive symbolic completion from being silently promoted to an ordinary witness.

## Priority ranking

| Rank | Bridge | Logical distance | Current deliverable |
|---:|---|---|---|
| 1 | sparse resultants + tropical valuation | direct cycle offense | `L-8201`, `X-8201` |
| 2 | catastrophic convolutional coding | finite-certificate format audit | concrete trellis/minor test |
| 3 | primitive divisors | PR #49 fresh primes | autonomization target |
| 4 | 2-adic T-functions | inverse address mixing | hypothesis map only |
| 5 | homoclinic dynamics | ordinary-boundary firewall | negative guidance |

## Search and novelty boundary

Repository code, issue, and PR-body searches found no active use of sparse/toric resultants or catastrophic convolutional encoders. The active literature branch contains no file with those topics in its enumerated source suite through wave 7.

This supports only the statement:

> These transfers were not located in the inspected repository state.

It is not a claim that no mathematician has ever made a related observation.

## Bottom line

The outlier search produced one exact theorem-level advance and several sharply delimited transfer programs. The strongest consequence is negative but constructive:

```text
fixed negative-cycle word
    + arbitrary finite pulse support
    + arbitrary positive pulse heights
    -> one explicitly bounded finite search.
```

A positive-cycle breakthrough in this neighborhood must now escape by changing repetition/baseline architecture, not merely by increasing pulse amplitudes inside a fixed packet.
