# LIT-KTHM-0004 — transcendence of the 64/81 slope and gap frequency

**Sources:** [@Gelfond1934], [@Schneider1935]; authoritative later source [@Baker1966]
**Inspection:** original metadata and publisher source; theorem used as black box
**Proof status:** Gelfond–Schneider BLACK BOX; corollaries proved completely

## Black-box theorem

If `a` is algebraic with `a≠0,1` and `b` is algebraic irrational, then every value of `a^b` is transcendental.

## Corollary 1

```text
beta = log_64(81)
```

is transcendental.

### Proof

It is not rational: if `beta=p/q` with positive integers `p,q`, then

```text
64^p = 81^q,
```

or `2^(6p)=3^(4q)`, contradicting unique factorization.

If `beta` were algebraic, it would therefore be algebraic irrational. Gelfond–Schneider would make `64^beta` transcendental, but by definition `64^beta=81`, an algebraic integer. Contradiction. ∎

## Corollary 2

The gap-frequency parameter

```text
alpha = 1/(beta-1) - 17
```

is transcendental.

### Proof

If `alpha` were algebraic, then

```text
beta = 1 + 1/(alpha+17)
```

would be algebraic, contradicting Corollary 1. ∎

## Native mappings

- `CLAUDE/T-0003`: supplies the transcendental frequency, but not the automaticity theorem.
- The fixed-primitive-substitution obstruction in `H64.md`, together with `LIT-KTHM-0006`.

## Non-applications

Gelfond–Schneider alone says nothing about finite automata, substitutions, Sturmian words, or validity of a carry grammar. Those require separate exact reductions.
