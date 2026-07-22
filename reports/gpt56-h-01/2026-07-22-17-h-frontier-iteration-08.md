# H frontier iteration 08 — structured counterexample attack

**Agent:** `gpt56-h-01`  
**Issue:** #17  
**PR:** #19  
**Status:** theorem-level claims remain `PROPOSED`; finite certificates remain `INTERNAL EXACT`

## Objective

Attack the counterexample side directly rather than add another qualitative
survivor restriction. The preferred target was a positive periodic orbit or a
low-complexity nonperiodic directive with one ordinary initialization.

No counterexample was found. The attempt instead produced two substantial
negative barriers that sharply constrain any structured counterexample.

## New mathematical results

### Cycle minimum

For a positive exact cycle of block period `L` and multiplier `M<1`, a cyclic
rotation with all backward partial products at most one gives

```text
p <= L/(1-M)
```

for one state of the cycle. The cycle minimum obeys the same bound, and its
outgoing block letter is at least three.

### Period exclusion

Combining the cycle-minimum inequality with the exact ordinary-state sweep in
`X-9506` reduces any uncovered cycle of length at most `2,479,700,524` to a
Legendre-quality rational approximation of

```text
kappa=log(4/3)/log(9/8).
```

`X-9507` uses rational atanh-series bounds to reconstruct the relevant
continued-fraction prefix and certifies all lower convergents and all their
multiples. This proves, conditional only on independent review of the native
lemma and the exact finite artifacts,

```text
no positive exact H block cycle has period <= 2,479,700,524.
```

### Entropy--capital barrier

For a nonperiodic finite-alphabet survivor, repeated itinerary factors force
large ordinary-state separation because the repeated block denominator divides
the state difference. If

```text
Gamma=limsup max_(i<N) K_i/log N
```

and `h` is factor entropy, then

```text
h >= e_* log 2 / (Gamma log(9/8)),
```

where `e_*` is the smallest dyadic exponent in the alphabet. Thus zero-entropy
finite-alphabet directives cannot survive with logarithmic capital growth.

This excludes the natural critical Sturmian/Beatty, automatic, and primitive
substitution templates when their capital bank is only logarithmic.

## Exact certificate

New experiment:

```text
experiments/X-9507-h-cycle-complexity/
```

Reproduction:

```bash
python3 -B cycle_period_bound.py --output results/canonical.json
```

Semantic digest:

```text
b3459e07b363633422db9224bd1758abee922dbd0b2cc3b482db2a6efbb37eba
```

Key values:

```text
ordinary sweep bound: 3*2^65
cycle period limit:   2,479,700,524
last lower convergent: 2733776749/1119265172
next upper convergent: 27172759629/11125094063
```

## Counterexample search verdict

No periodic, Sturmian, Beatty, automatic, primitive-substitution, or other
low-complexity slow-bank candidate survived the exact ordinary-integer test.
This is not evidence that all possible counterexamples are impossible, but it
changes what a viable structured construction must contain.

It must be at least one of:

1. a nonperiodic finite-alphabet directive with positive factor entropy and
   capital growth meeting the explicit entropy threshold;
2. an unbounded-letter reset--renewal directive satisfying the fresh-prime,
   prime-reuse, deficit-pressure, and discounted-core budgets;
3. a direct arithmetic construction giving one positive integer and an exact
   induction proving eventual zero carry and legality forever.

The next counterexample-first experiment should search proof-carrying finite
state or substitution systems in branch 1 while tracking both factor entropy
and exact carry stabilization. Merely producing arbitrarily long finite words
or a `Z_2` ghost is not enough.
