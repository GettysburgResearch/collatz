# Period-nine Tschakaloff closure and the new periodic frontier

## Result

The fully inspected Väänänen–Wallisser theorem applies to the exact PR #20 periodic phase vector whenever its minimal period has length at most nine.

The source function is

```text
f_q(z)=sum_(n>=0) q^(n(n-1)/2) z^n.
```

For a period-`r` stack word, PR #20 gives one rational linear combination of

```text
f_R(Z), f_R(Zlambda), ..., f_R(Zlambda^(r-1)),
R=lambda^r.
```

The points lie in distinct `R^Z`-orbits. At `p=2`, the source parameter is

```text
1-log(64)/log(81),
```

independent of the word. The source inequality holds through `r=9` and fails at `r=10`.

## Corrected research frontier

```text
minimal eventual period <=9:
  irrational by Väänänen–Wallisser plus the native reduction;

minimal eventual period >=10:
  not covered by that theorem;

balanced nonperiodic 17/18 directive:
  requires period-uniform estimates and S-adic passage.
```

## Why period ten may still be cheaper than the source theorem

Väänänen–Wallisser proves full linear independence of

```text
1,f_R(y_0),...,f_R(y_(r-1)).
```

PR #20 needs only irrationality of one special rational coefficient vector

```text
sum_j C_j f_R(y_j).
```

The dimension-ten failure may therefore reflect the cost of a theorem much stronger than the native target. A tailored Padé construction can impose cancellation against the native coefficient vector—or the low-dimensional q-difference orbit it generates—rather than all coordinate directions.

This is the natural role of the Casoratian, maximal-minor, and quotient-state work: determine whether special-vector irrationality survives after full `r`-dimensional independence stops.

## What to retain from the native period-four program

The period-four work remains useful because it supplies:

- a source-independent proof architecture;
- exact q-binomial and common-denominator models;
- q-Lucas/Cartier state refinement;
- cyclotomic and jet information;
- adjacent-order Casoratians;
- regression tests for any all-period theorem.

Its role should change from “first unresolved fixed period” to “smallest complete laboratory for removing the source theorem's dimension cutoff.”

## Next experiment

Re-run the entire height/vanishing calculation at period ten, reporting every exponent as a function of both Padé order `n` and period `r`. Test four routes:

1. a Padé system tailored to the single native coefficient vector;
2. symbolic maximal-minor factors;
3. growing-width adjacent-order determinants;
4. all-dyadic Cartier recurrences.

The useful endpoint is not only irrationality at `r=10`, but a lower bound whose constants deteriorate slowly enough to survive adjacent standard-word periods tending to infinity.
