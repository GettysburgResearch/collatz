# Latest checkpoint — short-period block Padé

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Draft PR:** #20  
**Status:** all theorem-level claims below are `PROPOSED` pending independent reconstruction

## New theorem chain

```text
L-9408  exact finite-word / repeated-block transfer
   |
L-9409  scalar Gaussian-binomial Padé (constant increments)
   |
T-9412  constant-increment irrationality
T-9413  eventually constant irrationality
   |
L-9410  simultaneous block Gaussian-binomial Padé
   |
T-9414  every positive periodic word of length <=3 is irrational
T-9415  every finite prefix followed by such a tail is irrational
```

The exact block approximation exponent is

```text
mu_r
 =[1/log_64(81)]*(1+1/[r(r+1)]).
```

Hence

```text
r=1: 1.419591945535... >1,
r=2: 1.104127068750... >1,
r=3: 1.025260849553... >1,
r=4: 0.993714361875... <1.
```

## Exact conclusion

No positive periodic stack increment word of displayed length `1`, `2`, or `3`
selects an ordinary initial context. An arbitrary finite steering prefix cannot
repair such a tail.

No conclusion is claimed for primitive period four, longer periods, or the
balanced nonperiodic `17/18` directive.

## First unresolved boundary

`R-9403` records that the universal estimate first falls below the rationality
threshold at period four. The logarithmic deficit is

```text
0.006285638124... = 0.6285638124%.
```

`Q-9411` asks whether this can be recovered through exact reduced-height
cancellation, an adjacent-order determinant, or a phase-sensitive denominator.

## Bounded period-four census

`O-9401` / `X-9409` examine the three primitive cyclic `{17,18}` representatives
through Padé order three. Every measured reduced exponent is below one by order
three, and the observed gcds are tiny relative to million-bit reduced heights.
This is finite negative evidence only, not an asymptotic theorem.

## Verification

```text
X-9408  block Padé, periods 2/3
SHA-256 9895b3723a3a5d19f43ef5158c18a0511f58f923df2f1919a68771f1f322583c

X-9409  primitive period-four height census
SHA-256 bf85a00cc1b34aef1d85f5b7e483547b1200ac10e53c02375333447bb1c31546
```

## Review first

1. `claims/L-9410-block-gaussian-pade.md`
2. `claims/T-9414-short-period-irrationality.md`
3. `claims/T-9415-eventually-short-period-irrationality.md`
4. `claims/R-9403-universal-period-four-threshold.md`
5. `PERIODIC_BLOCK_PADE.md`
6. `Q-9411-period-four-height-saving.md`
7. `experiments/X-9408-block-pade/run.py`
8. `claims/O-9401-period-four-finite-height-census.md`
9. `experiments/X-9409-period-four-height/run.py`

## Next theorem target

Prove or refute a quadratic-scale common-factor or determinant saving for
primitive period-four words. Any successful mechanism should then be tested as
a possible local building block for adjacent S-adic standard words in the true
balanced frontier.
