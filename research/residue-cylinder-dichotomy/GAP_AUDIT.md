# Ordinary-integer gap audit

## What is now proved inside the frozen classes

### Direct dyadic-boundary class

`T-9702` proves that every infinite four-type direct-boundary directive has infinitely many nonzero initial residue blocks and a unique `Z_2` completion outside all signed ordinary integers.

### Corrected composed 256-transition class

Conditional only on the frozen exact PR #3 stage interface and the displayed external theorem, `T-9705` proves the same conclusion for every physically overlapping infinite corrected-stage directive:

```text
a_k != 0 infinitely often,
the unique Z_2 completion is not in Z.
```

The proof is uniform over arbitrary stage words. It does not assume periodicity, finite-state control, entropy balance, or sampled schedule behavior.

## Every ordinary-integer assumption exposed

### 1. Finite compatibility

Every finite stage prefix still has an exact cylinder and ordinary finite members. No finite member is treated as an infinite initialization.

### 2. Completion versus ordinary integer

The nested cylinders select one point of `Z_2`. `T-9705` assumes this point is a signed ordinary integer only for contradiction, then uses exact stage divisibility to propagate a signed integer trajectory.

### 3. Least representatives and residue blocks

Eventual zero initial residue blocks imply stabilization to a nonnegative ordinary integer. Since `T-9705` excludes every signed integer, eventual zero blocks are impossible. Negative integers are handled separately rather than being inferred from least-representative stabilization.

### 4. Signed quotient

The nonnegative quotient theorem `T-9703` is not silently extended. `L-9705` proves the signed dichotomy exactly:

```text
Y_m -> 0     (cap chain),
Y_m -> -1    (co-cap chain).
```

The co-cap correction `2^(D_m)-R_m` has the same completion-height estimate as the cap correction.

### 5. Positivity and physical states

A positive counterexample would require a nonnegative tail, but the negative result is stronger: signed ordinary residuals are excluded. `L-9704` supplies the direct physical relation

```text
64(n_j+34)=2^(11(t_j+1)) Z_j.
```

No positive marked initialization is constructed or assumed.

### 6. Connector inverses

The proof does not estimate moving Montgomery inverses. The scaled ordinary coordinate in `L-9704` cancels them exactly and leaves one 256-term `{2,3}`-unit stage sum.

### 7. External theorem applicability

`L-9706` specializes Corollary 1 of Evertse (1984) with

```text
S_0={2,3}, n=257, c=1, d=1/50.
```

It verifies:

- primitive integer coordinates;
- a zero sum;
- no proper nonempty vanishing subsum;
- outside-`S_0` product at most `||x||^(1/50)`;
- infinitely many distinct projective points.

No theorem is invoked merely by the phrase “S-unit equation.”

### 8. Primitive gcd

The primitive normalization is explicit. The first internal term bounds the common 2-adic valuation by three, the last bounds the common 3-adic valuation by three, and no prime above three divides an internal term. Thus

```text
gcd <= 2^3*3^3 = 216.
```

### 9. Completion height

The cap/co-cap endpoint product consumes asymptotically at most

```text
6498/346819 < 1/50
```

of the connector-free projective height. This strict `d<1` inequality is the load-bearing Subspace-Theorem gate. A short representative alone was never claimed to be impossible.

### 10. Proper subsums

The homogeneous stage tuple has exactly one positive coordinate and 257 negative coordinates. Every proper subset excluding the positive term is negative; every proper subset containing it omits at least one negative term and is positive. Hence every proper nonempty subsum is nonzero.

### 11. Distinctness

Finiteness of admissible projective points would not contradict a repeated point. `L-9706` uses the ratio between the `2^(E_m)` endpoint coordinate and the `j=0` internal term. Its 2-adic valuation lies in `[E_m-3,E_m+3]` and strictly increases with scale.

### 12. Logarithm, entropy, and ordinary bulk

No digit of `-(7/4)log_2(3)` is initialized. No entropy surplus, branch count, or bit-length surplus is treated as residue membership. PR #3's ordinary bulk `V_m` is not needed for the negative theorem.

## External and native status boundary

- `L-9704`--`T-9705` remain `PROPOSED` pending independent reconstruction.
- Evertse's 1984 Corollary 1 is an external black box; the source statement is reproduced in `L-9706` but not promoted into PR #13's ledger.
- The frozen PR #3 stage formulas retain their native `PROPOSED` status.
- No root claim ledger is changed.

## What remains open

### Independent reconstruction

The mathematical frontier within the frozen class is closed, but review is not. The highest-value review tasks are:

1. reconstruct the scaled connector coordinate from PR #3's tower identities;
2. verify physical overlap and all exponent sums;
3. rederive the signed cap/co-cap quotient dichotomy;
4. inspect Evertse's original Corollary 1;
5. audit the outside-prime product and projective distinctness.

### Transfer beyond the frozen class

`T-9705` does not settle Collatz and does not automatically apply to:

- different negative-cycle phases;
- adaptive stages with different height schedules;
- arbitrary Collatz trajectories outside the corrected stage architecture;
- other repository survivor systems whose internal terms are not pure `{2,3}`-units.

Each new class needs its own exact homogeneous tuple and `d<1` admissibility audit.

### Candidate boundary

No positive ordinary initialization exists in the frozen corrected-stage class, so no `K-####` candidate is created.
