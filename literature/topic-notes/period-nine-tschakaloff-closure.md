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

Re-run the entire height/vanishing calculation at period ten, reporting every exponent as a function of both Padé order `n` and period `r`. Test three routes:

1. symbolic maximal-minor factors;
2. growing-width adjacent-order determinants;
3. all-dyadic Cartier recurrences.

The useful endpoint is not only irrationality at `r=10`, but a lower bound whose constants deteriorate slowly enough to survive adjacent standard-word periods tending to infinity.
