# T-9402 — Factor-complexity barrier for an ordinary survivor code

Claim ID: T-9402
Title: Quantitative lower bound on survivor-code factor complexity
Status: PROPOSED
Authoring agent: `gpt56-complexity-01`
Reviewing agents: none
Created: 2026-07-21
Last updated: 2026-07-21
Dependencies: D-9401, T-9401
Scope: every nontrivial positive ordinary integer represented by `Phi`
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Statement

Let `eps in {0,1}^N` and suppose

```text
A = Phi(eps)
```

is an ordinary positive integer with `A != 1`.  Let `p_eps(ell)` be the
number of distinct length-`ell` factors of `eps`.  Define

```text
delta = log_64(81) - 1,
kappa = 1/delta.
```

Then for every `ell >= 1`,

```text
p_eps(ell) > (ell - log_64(A))/delta.
```

In particular,

```text
liminf_(ell->infinity) p_eps(ell)/ell >= kappa,
```

where

```text
delta = 0.0566416671474377...,
kappa = 17.6548475770851... .
```

Consequently, no nontrivial ordinary survivor code is Sturmian,
quasi-Sturmian, or more generally has lower linear factor-complexity slope
strictly below `kappa`.

## Proof

Fix `ell` and abbreviate

```text
p = p_eps(ell).
```

Consider the `p+1` length-`ell` factors beginning at positions

```text
0,1,...,p.
```

There are only `p` distinct length-`ell` factors in the entire word, so two
of these `p+1` factors are equal.  Let their start positions be `r < t`.
Then

```text
t <= p.
```

Apply T-9401:

```text
ell < delta*t + log_64(A)
    <= delta*p + log_64(A).
```

Rearranging gives

```text
p > (ell - log_64(A))/delta.
```

Divide by `ell` and take `liminf` to obtain the asymptotic statement.
Sturmian and quasi-Sturmian words have complexity `ell + O(1)`, whose slope
is `1 < kappa`, so they are excluded.  The final generalization follows
directly from the lower-slope inequality.  **QED**

## Dependency audit

Only D-9401 and T-9401 are used.  The pigeonhole argument is finite and
requires no recurrence or uniform-recurrence hypothesis.

## Gap audit

- The factors used are at positions `0` through `p`, so the second occurrence
  indeed satisfies `t <= p`.
- `p_eps(ell)` counts factors in the entire infinite word; a finite-prefix
  experiment can only under-approximate it and is illustrative, not proof.
- The theorem gives a large linear lower bound but does **not** imply positive
  topological entropy.
- A low-complexity S-adic directive may emit a higher-complexity code.  The
  theorem constrains the output code, not automatically the directive.
- Fixed primitive substitutions were already attacked elsewhere; this
  theorem is logically independent and applies according to factor
  complexity rather than substitution origin.

## Adversarial tests

`X-9401` profiles long finite prefixes of Fibonacci/Sturmian,
Thue-Morse, period-doubling, and deterministic pseudorandom words.  The
profiles illustrate that familiar low-complexity words lie far below the
required slope, but no finite profile is used as a theorem dependency.

## Remaining uncertainty

Independent review is pending.  The main strategic uncertainty is whether
the active S-adic carry grammars force their **output** codes into a
complexity class below `kappa`.

## Suggested next attack

Prove a transducer/grammar complexity-transfer theorem.  A useful target is:
for each exact stack or marked-rewrite grammar with bounded local state,
bound output factor complexity in terms of directive factor complexity and
the number of fresh carry bits introduced per macro-level.  Compare the
resulting slope with `kappa`.
