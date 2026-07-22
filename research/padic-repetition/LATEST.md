# Latest checkpoint — period nine closed, period ten reduced to one special vector

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Draft PR:** #20  
**Status:** every theorem-level claim below is `PROPOSED` pending independent reconstruction; `T-9417` is additionally source-dependent

## Corrected fixed-period frontier

The wave-5 literature audit supplied and inspected the full theorem of
Väänänen and Wallisser for rational `2`-adic Tschakaloff values.

The exact periodic stack decomposition is

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j f_R(Z lambda^j),
R=lambda^r.
```

`L-9412` reconstructs the source mapping:

```text
- every C_j is rational and nonzero;
- the points Z lambda^j occupy distinct R^Z-orbits;
- gamma=1-log(64)/log(81)=0.053605369642...;
- gamma<Gamma(9);
- gamma>Gamma(10).
```

The endpoint arithmetic is exact:

```text
64^93>81^88,
559^2-325*31^2=156,
64^20<81^19,
401-20^2=1.
```

`T-9417` therefore gives the source-dependent conclusion

```text
minimal eventual period <=9
  => irrational selected 2-adic context
  => no ordinary integer initialization.
```

An arbitrary finite steering prefix cannot repair such a tail.

The first fixed period outside this source theorem is now **period ten**, not
period four.

## Native proof architecture retained

The self-contained native packet remains useful and independently reviewable:

```text
L-9409 -> T-9412 -> T-9413
```

excludes constant and eventually constant tails, while

```text
L-9410 -> T-9414 -> T-9415
```

excludes periodic and eventually periodic tails of minimal period at most
three.

`L-9411` and `T-9416` prove that equal allocation is uniquely optimal throughout
the complete phasewise Gaussian-binomial root-product class. The period-four
laboratory remains a regression suite for all-period and special-vector methods.

## New period-ten special-vector route

### `R-9406` — source cutoff is not a value cutoff

Failure of the Väänänen–Wallisser numerical condition at dimension ten concerns
full independence of

```text
1,f_R(y_0),...,f_R(y_9).
```

The native target is only the special vector

```text
sum_(j=0)^9 C_j f_R(y_j).
```

A tailored construction may therefore be cheaper than full ten-dimensional
independence.

### `L-9413` — every individual phase has a strong scalar Padé family

For every

```text
F_(A,B)
 =sum_(N>=0)(T^A)^[N(N-1)/2](T^B)^N,
```

`L-9413` proves a scalar `q`-binomial Padé family with limiting exponent

```text
9/log_2(81)
 =1.419591945535779...>1,
```

independent of `A` and `B`.

### `L-9414` — one-phase elimination lemma

Suppose nine phase values satisfy a quantitative linear-independence measure

```text
v_2(Lambda)
 <=(omega_9+o(1)) log_2 H(Lambda).
```

Adjoining a tenth scalar phase with Padé exponent `tau` preserves independence
whenever

```text
omega_9<tau.
```

For the stack,

```text
tau=9/log_2(81)=1.419591945535779... .
```

Thus period ten is reduced to the explicit source-normalization test

```text
omega_9 < 9/log_2(81).                                (A)
```

The exact `omega_9` has not yet been transcribed from the source theorem; no
period-ten conclusion is claimed until (A) is decided.

## Two-dimensional `q`-difference formulation

For a fixed period-ten word, define

```text
F_W(X)=Theta(m;W^infinity),
X=T^(9m).
```

The exact transfer identity is

```text
F_W(X)
 =P_W(X)+T^e X^10 F_W(lambda X).
```

Equivalently,

```text
[1      ]   [1       0       ][1             ]
[F_W(X)] = [P_W(X) T^e X^10 ][F_W(lambda X)].
```

Although the periodic diagonalization has ten Tschakaloff phases, the native
value belongs to a two-dimensional triangular `q`-difference orbit. This is the
fallback special-vector route if the exponent comparison (A) fails.

The direct combined moments are

```text
u_N
 =R^[N(N-1)/2] Z^N P_W(X lambda^N).
```

A useful Padé system should cancel these **combined** coefficients rather than
paying separately for all ten phase directions.

## Adjacent-order audit

PR #34 proposes an exact adjacent-order Casoratian rank theorem. `R-9407`
combines its branch-qualified formula with an independent place calculation.
Even granting zero quadratic cofactor-height cost, the absolute scalar ceiling
is

```text
mu_r^adj,max
 =log_81(64)*(r^2+r+3)/(r(r+1)).
```

It first falls below one at `r=7`. At period ten,

```text
mu_10^adj,max
 =log_81(64)*113/110
 =0.972205393003291...<1,
```

certified exactly by

```text
64^113<81^110.
```

Thus scalar aligned adjacent-order combinations cannot be the period-ten
breakthrough even if their cofactors were free. The next determinant must be
phase-sensitive, low-dimensional, or carry/completion-height coupled.

## Verification

`X-9411` freezes:

```text
- the exact source endpoint arithmetic;
- the numerical Gamma(D) table through D=12;
- all 165 phase-pair orbit checks through period ten;
- 30 exact direct-versus-phase decompositions;
- the scalar phase exponent;
- adjacent-order optimistic ceilings through period fifteen.
```

```text
SHA-256
787f91b5cb328f67dac5f71ee89af2a858572493a27b5d61a6504a480e599897
```

Finite checks validate their frozen arithmetic only. They do not prove the
external theorem, `T-9417`, `L-9413`, or period-ten irrationality.

## Review first

1. `claims/L-9412-vaananen-wallisser-interface.md`
2. `claims/T-9417-eventually-period-nine-irrationality.md`
3. `claims/L-9413-generic-scalar-tschakaloff-pade.md`
4. `claims/L-9414-one-phase-special-vector-elimination.md`
5. `claims/R-9406-vw-dimension-ten-cutoff.md`
6. `claims/R-9407-adjacent-order-period-ten-ceiling.md`
7. `Q-9413-period-ten-special-vector.md`
8. `experiments/X-9411-period-nine-source/run.py`
9. `claims/L-9412-vaananen-wallisser-interface.md`
10. `claims/L-9410-block-gaussian-pade.md`

## Next theorem target

Extract the exact dimension-nine Väänänen–Wallisser linear-independence exponent
and decide (A). If it is below `9/log_2(81)`, `L-9414` closes period ten by
one-phase elimination. If not, construct Padé approximants directly for the
two-dimensional triangular `q`-difference system or the combined moment
sequence, with constants tracked uniformly in the period for eventual S-adic
passage.
