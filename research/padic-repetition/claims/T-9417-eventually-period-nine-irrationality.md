# T-9417 — Eventually periodic stack directives through period nine are irrational

Claim ID: `T-9417`  
Title: No positive eventually periodic height-increment tail of minimal period at most nine selects an ordinary stack context  
Status: `PROPOSED / SOURCE-DEPENDENT`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9407`, `L-9408`, `L-9412`; Väänänen–Wallisser (1991), Theorem 1  
Scope: every positive increment directive eventually periodic with minimal eventual period at most nine  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Statement 1 — periodic tails

Let

```text
W=d_1...d_r,
d_i>=1,
1<=r<=9,
m>=0,
```

and assume `W` has minimal period `r`. Then

```text
Theta(m;W^infinity) notin Q.                          (1)
```

Consequently the unique formal stack context associated by `L-9407` and
`T-9409` to `W^infinity` is irrational and is not an ordinary integer.

## Statement 2 — arbitrary finite steering prefixes

Let `U` be any finite positive increment word and let `W` be as above. Then

```text
Theta(m;U W^infinity) notin Q.                        (2)
```

Thus no finite CRT-steering or initialization prefix can repair a periodic tail
whose minimal period is at most nine.

## Proof of Statement 1

By `L-9412`,

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j f_R(Z lambda^j),                (3)
```

where every `C_j` is a nonzero rational number and the `r` points occupy
distinct multiplicative `R^Z`-orbits.

The same lemma verifies

```text
gamma(R,2)<Gamma(r)
```

because `r<=9`. Väänänen–Wallisser therefore gives rational linear independence
of

```text
1,
f_R(Z),
f_R(Z lambda),
...,
f_R(Z lambda^(r-1)).                                  (4)
```

Suppose (3) were rational. Move that rational number to the left and clear all
rational denominators. The result is a nontrivial integer linear relation among
the values in (4), contradicting their independence. This proves (1).

`L-9407` expresses the selected initial context as a nonzero rational affine
transform of the tail value. A rational context would therefore make the tail
rational, again contradicting (1).

## Proof of Statement 2

The exact finite-prefix transfer of `L-9408` is

```text
Theta(m;U W^infinity)
 =P_U(T^(9m))
  +c_U Theta(m+S(U);W^infinity),                      (5)
```

where `P_U(T^(9m))` and the nonzero multiplier `c_U` are rational.

If the left side were rational, solving (5) for the final periodic tail would
make that tail rational, contradicting Statement 1. **QED**

## Strength relative to the native Padé packet

- `T-9412` and `T-9413` gave a source-independent proof for period one.
- `T-9414` and `T-9415` extended the source-independent proof through period
  three.
- The present source-dependent theorem extends the fixed-period exclusion
  through period nine.
- The native Padé proofs remain valuable because they expose exact error and
  height mechanisms and can be adapted to period-uniform or special-vector
  questions.

## Dependency and source audit

- The periodic phase decomposition and finite-prefix transfer are native exact
  identities.
- Full phase-vector independence is imported from Väänänen–Wallisser.
- `L-9412` reconstructs every source parameter and orbit hypothesis.
- No empirical calculation is a proof dependency.

## Gap audit

- Minimal period ten is not covered by the source's stated numerical condition.
- The theorem does not prove transcendence.
- It does not supply constants uniform in a period tending to infinity.
- It does not cover the balanced nonperiodic `17/18` directive.
- Irrationality of the formal context is an obstruction theorem, not a Collatz
  counterexample construction.

## Adversarial tests

`X-9411` checks the finite phase decomposition, distinct-orbit indexing, and the
exact source-condition endpoint at periods nine and ten.

## Remaining uncertainty

The first fixed-period class not closed by this theorem is minimal period ten.
The strongest current possibility is cheaper **special-vector irrationality**:
the native target is one coefficient vector, not full ten-dimensional
independence.

## Suggested next attack

Extract the exact nine-phase quantitative measure from the source paper and
compare it with the generic scalar-phase Padé exponent in `L-9413` through the
one-phase elimination lemma `L-9414`.
