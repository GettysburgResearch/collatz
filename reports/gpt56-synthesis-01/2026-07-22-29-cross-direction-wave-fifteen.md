# Cross-direction lemma forge: wave fifteen

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Starting point

Wave fourteen left four concrete interfaces:

- replace the full 256-symbol toll modulus in the fixed-room count by the
  shortest prefix that actually outruns the real room scale;
- absorb the bounded binary and ternary endpoint signatures before applying
  the quantitative S-unit theorem;
- match PR #3's native two-place approximation to an exact sourced form of
  Ridout's theorem; and
- turn PR #20's new native order-two q-difference equation into an explicit
  functional-rank and determinant input.

The final audited source heads are PR #3 `c37e96e`, PR #13 `dc7f966`, PR #33
`2cfe250`, and PR #20 `aa9cf71`.  PR #20 moved after the first draft from
`93739b4` to `aa9cf71`; the move only added `L-9416`, `L-9417`, and
`T-9418`--`T-9421`.  The `L-9408` and `L-9415` blobs used by `T-9812` are
unchanged.  The new scalar irrationality and rational-code classification do
not contain the solution Casoratian proved here, but they change its intended
next use from scalar irrationality to stronger two-value estimates.

## Delegation and review

- The prefix lane derived the exact first three toll exponents and proved the
  64-room packing theorem.
- The quantitative-prime lane froze both endpoint signatures and recomputed
  the correlated tuple-group rank.
- The cap/Ridout lane audited the exact projective theorem and all three local
  target factors.
- The integrating lane derived the native solution Casoratian and its exact
  physical valuation.

Every theorem received a nonauthoring cold review.  `T-9811` was strengthened
during review from a rational-or-transcendental dichotomy to transcendence:
Ridout's theorem permits rational algebraic targets as well.  `T-9812`'s
2-adic rearrangement was repaired by passing through finite truncations and
proving unconditional convergence of the paired sum.  All four claims remain
`PROPOSED`.

## New results

### `T-9809` -- only three toll symbols are needed

For the corrected stage heights, the first two relevant prefix exponents are

```text
U_(m,2)=(5665/256)2^m+22,
U_(m,3)=(4257/128)2^m+33.
```

Exact rational bounds `84/53<log_2(3)<65/41` give opposite exponential gaps:

```text
U_(m,3)-log_2(H_m) -> +infinity,
U_(m,2)-log_2(H_m) -> -infinity.
```

The first three toll symbols therefore produce 64 distinct incoming residues
modulo a dyadic modulus eventually larger than every fixed finite collection
of room heights.  The same finite-subset packing argument used in `T-9808`
then gives

```text
number of eventual rooms <= 64.
```

Each room still determines at most one full eventual boundary and word tail.
Length three is the shortest prefix for this one-scale modulus method; that is
not a lower bound for arguments combining several scales or other primes.

### `T-9810` -- endpoint signatures remove the structural primes

For each stage, freeze the context

```text
(incoming ternary signature, 256-symbol word, outgoing endpoint type).
```

There are at most `3*4^256*4=12*4^256` such contexts.  Exact endpoint
factorization moves every bounded power of `2` and `3` into fixed
coefficients.  If `f` is the number of endpoint primes outside `{2,3}`, all
solutions for one context lie in a tuple group of rank at most

```text
2f+1,
```

one common scale direction plus two endpoint directions per fresh prime.
With `C=1542^771` this yields, when the incoming signature is available,

```text
N <= 12*4^256 floor(exp(C(2f+2))).
```

Without an initial ternary signature, discard only the first stage and use
`N-1` with the post-initial prime set.  Relative to the direct conversion of
`T-9805`, the exponent improves from `2f+6` to `2f+2`; the constant remains
far too large for computation.

### `T-9811` -- every hypothetical fixed room is transcendental

PR #3 supplies reduced rationals `xi_m=P_m/Q_m` with

```text
|C_infinity-xi_m| |P_m|_2 |Q_m|_3
  < H(xi_m)^(-2-1/1024).
```

Ridout's exact projective theorem applies at

```text
S={infinity,2,3},
targets=(C_infinity,0,infinity).
```

The three minimum factors are exactly the real error, `|P_m|_2`, and
`|Q_m|_3`, and the projective height is exactly `max(|P_m|,Q_m)`.  The reduced
denominators strictly increase, so the approximants are infinitely many and
distinct.  If the room were algebraic, this would contradict Ridout's finite
exceptional-set theorem.  Thus every room attached to an assumed infinite
ordinary corrected-stage path is transcendental.

This is a conditional classification, not room existence or nonexistence.
The theorem is ineffective and supplies no largest exceptional scale.

### `T-9812` -- an exact native q-Casoratian

For a positive periodic increment word, let `F_W` be PR #20's periodic-tail
solution and `q=(64/81)^(9S)`.  The first-order equation and formal
nonrationality imply

```text
dim_(Q(X)) span{F_W(X),F_W(qX)}=2.
```

Its first solution Casoratian has the exact sum-of-squares expansion

```text
Delta_W(X)
 =F_W(X)F_W(q^2 X)-F_W(qX)^2
 =sum_(i<j) f_i f_j (q^i-q^j)^2 X^(i+j).
```

It is positive for real `X>0`.  At the physical point `x=(64/81)^(9m)`, the
`(0,1)` pair is the unique term of least 2-adic valuation, giving

```text
v_2(Delta_W(x))=54(m+d_1)+6.
```

Hence the two-by-two physical sample matrix is nonsingular over both the real
and 2-adic embeddings.  This does not itself prove Q-linear independence of
the specialized values.  At the refreshed PR #20 head scalar irrationality is
already known by an elementary denominator argument; the next source audit
should target a quantitative two-value independence measure or stronger
arithmetic classification.

## Exact checks and review

- `T-9809`: both rational logarithmic comparisons, the 64-prefix decoder,
  and the finite-set room packing proof were independently reconstructed.
- `T-9810`: endpoint valuations, the three-by-four signature count,
  coefficient absorption, tuple generators, rank, final endpoint retention,
  and integer inversion were cold-reviewed.
- `T-9811`: the primary Ridout citation and Bilu's authoritative exact
  projective formulation were checked; a separate reviewer verified target
  matching, reduction, height, and distinct denominators.
- `T-9812`: formal independence, coefficient symmetrization, the period-one
  edge case, finite-truncation passage, unique least-valuation pair, and the
  no-specialization-overclaim boundary were reconstructed independently.

No finite computation is used as a theorem premise.

Memory remained healthy throughout integration; the final pre-commit snapshot
had 10.07 GiB free with 34.7% of physical memory in use.

## Candidate counterexamples

None.  No `K-####` candidate is proposed.

## Closed routes and remaining boundaries

- The fixed-room cardinality falls from `4^256` to 64, but the finite set may
  still be nonempty and is not effectively listed.
- The structural endpoint primes no longer tax the S-unit rank, but two
  directions per fresh prime remain and the ESS constant is astronomical.
- Every hypothetical fixed room is transcendental, but no independent theorem
  yet forces it to be algebraic.
- The periodic q-difference solution has an exact nonzero physical
  Casoratian, but value-level Q-linear independence and effective measures are
  not proved by that determinant alone.

## Files changed

Four theorem files, the packet claim/status/verification ledgers, and this
append-only report.  No canonical root ledger or competing branch file is
changed.

## Recommended next actions

1. Intersect the 64 three-symbol room addresses with the exact cap-head cells
   and 84 seam constraints; determine whether their address maps align or are
   only safely bounded by a Cartesian product.
2. Test whether adjacent corrected-stage equations share enough endpoint
   exponent geometry to reduce the two fresh-prime directions globally.
3. Seek a native criterion making the PR #3 room algebraic; together with
   `T-9811` that would exclude every assumed ordinary path.
4. Audit a precise p-adic q-functional theorem only for a stronger
   two-value rank or measure, using `T-9812`'s exact determinant and valuation
   as hypotheses.

## Organizational improvement ideas

When a live source adds a stronger theorem while a downstream claim is under
review, record whether it supersedes the result, merely changes its intended
application, or leaves it disjoint.  Also distinguish three separate notions
for q-functional systems: formal rank over `Q(X)`, nonsingularity after
specialization, and arithmetic linear independence of specialized values.
None may be silently substituted for another.
