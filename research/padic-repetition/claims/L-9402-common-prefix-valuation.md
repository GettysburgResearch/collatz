# L-9402 — Exact separation by the first differing code digit

Claim ID: L-9402
Title: First-difference `2`-adic valuation for binary survivor codes
Status: PROPOSED
Authoring agent: `gpt56-complexity-01`
Reviewing agents: none
Created: 2026-07-21
Last updated: 2026-07-21
Dependencies: D-9401
Scope: all distinct binary sequences
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Statement

Let `eps, eta in {0,1}^N` be distinct, and let `m` be their first differing
position.  Then

```text
v_2(Phi(eps) - Phi(eta)) = 6m.
```

In particular:

1. if two codes agree through positions `0,...,N-1`, then

   ```text
   Phi(eps) - Phi(eta) belongs to 64^N * Z_2;
   ```

2. `Phi` is injective.

If both values are rational with odd denominators and

```text
Phi(eps) - Phi(eta) = z/q,
```

where `z` is an integer and `q` is odd, then agreement through the first
`N` digits implies

```text
64^N divides z.
```

## Proof

At the first differing digit, factor the difference as

```text
Phi(eps) - Phi(eta)
= (17/81) * (64/81)^m
  * [ (eps_m - eta_m)
      + 64 * sum_(j>=1)
          (eps_(m+j) - eta_(m+j))*64^(j-1)/81^j ].
```

The bracket lies in `Z_2`.  Its first term is `+1` or `-1`, while the
remaining term is divisible by `64`; hence the bracket is odd and is a
`2`-adic unit.  The prefactor has valuation exactly `6m`, proving the first
claim.

The common-prefix and injectivity statements follow immediately.  For the
rational specialization, an odd denominator is a unit in `Z_2`, so
membership in `64^N Z_2` is equivalent to divisibility of the integer
numerator by `64^N`.  **QED**

## Dependency audit

Only D-9401 is used.

## Gap audit

- Exact equality requires a *first* differing position.  With only a shared
  prefix, the safe conclusion is the lower bound `v_2 >= 6N`.
- Oddness of the rational denominator is essential when translating a
  `2`-adic valuation to ordinary numerator divisibility.
- Infinite tails converge in `Z_2` because each further term gains at least
  six powers of `2`.

## Adversarial tests

`X-9401` compares many distinct eventually periodic codes as exact rational
numbers and verifies that the numerator valuation is exactly six times the
first differing position, including differences inside the preperiod and
inside the periodic tail.

## Remaining uncertainty

None known; independent review is pending.

## Suggested next attack

Generalize the lemma to a digit alphabet `D` whose pairwise differences may
have nonzero `2`-adic valuation.  The resulting weighted first-difference
bound could apply to wider collision fibers.
