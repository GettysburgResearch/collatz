# Latest checkpoint — native period nine closed; period ten isolated

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Draft PR:** #20  
**Status:** every live theorem-level claim below is `PROPOSED` pending independent reconstruction; `T-9417` is additionally source-dependent

## Fixed-period frontier

The periodic stack decomposition is

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) C_j f_R(Z lambda^j),
R=lambda^r.
```

Two independent routes now exclude the same exact period range:

```text
minimal eventual period <=9
  => irrational selected 2-adic context
  => no ordinary integer initialization.
```

- `T-9417` imports Väänänen--Wallisser after the exact source reduction in
  `L-9412`.
- `T-9422` is source-independent and uses the delayed native Padé family in
  `L-9418`.

An arbitrary finite steering prefix cannot repair such a tail. Minimal period
ten is the first fixed period not closed by either route.

## Source-dependent period-nine theorem

`L-9412` verifies:

```text
- every C_j is rational and nonzero;
- the phase points occupy distinct R^Z-orbits;
- gamma=1-log(64)/log(81)=0.053605369642...;
- gamma<Gamma(9);
- gamma>Gamma(10).
```

The exact endpoint arithmetic is

```text
64^93>81^88,
559^2-325*31^2=156,
64^20<81^19,
401-20^2=1.
```

`T-9417` therefore excludes every eventually periodic positive increment tail
of minimal eventual period at most nine.

## Quantitative source bootstrap is closed

The published Väänänen--Wallisser valuation-height exponent is

```text
theta(gamma,D)
 =1+(2D-1+sqrt(1+4D^2))
      /(2-gamma(2D+1+sqrt(1+4D^2))).
```

`R-9408` records

```text
theta(gamma,1)=2.882180476090...,
theta(gamma,9)=2318.657271149...,
```

while the scalar phase Padé exponent of `L-9413` is only

```text
9/log_2(81)=1.419591945535... .
```

Thus the proposed one-phase elimination of `L-9414` cannot extend the published
measure from dimension nine to ten.

`X-9412` digest:

```text
b1f82225c0c8dc5013d5c709e00f924ca5e9e0c178d2c438bf252bfe3add4458
```

## Native homogeneous order-two formulation

For every fixed positive period word `W`, `L-9415` defines a nonrational entire
function satisfying

```text
F_W(X)=P_W(X)+aX^rF_W(qX).
```

Eliminating the inhomogeneous polynomial gives

```text
P_W(qX)F_W(X)
-[P_W(X)+aX^rP_W(qX)]F_W(qX)
+a q^r X^r P_W(X)F_W(q^2X)=0.
```

Although phase diagonalization has dimension `r`, the native functional system
has homogeneous order two. A valid theorem proving

```text
dim_Q span{F_W(x),F_W(qx)}>=2
```

at a physical rational point would imply irrationality of `F_W(x)` because
rationality propagates down the `q`-orbit.

No black-box application is claimed before the exact place, coefficient,
solution, and determinant hypotheses of the relevant source are inspected.

## Delayed-window block Padé

`L-9418` separates denominator degree from cancellation-window position. For

```text
D=rn,
M>=D+1,
```

define

```text
beta_(r,n,M)(k)
 =[(1-r)k^2+(2rM-r-1)k]/2.
```

The exact phase coefficient is

```text
Gamma_(j,N)
 =base_(j,N)
  *prod_(h=0)^(D-1)
    (1-lambda^[h+rM-rN-j]).
```

Every phase vanishes for

```text
M<=N<M+n.
```

The first surviving block is `N=M+n`, with exact error valuation and common
height scale

```text
L_(r,n,M)
 =[r(M+n)(M+n-1)-D(D+1)]/2,

Q_A(r,n,M)
 =[D^2+D+rM^2-rM-2M+2]/2.
```

If `M/n->alpha`, the resulting exponent is

```text
mu_r^delay(alpha)
 =log_81(64)*[((alpha+1)^2-r)/(alpha^2+r)],
```

maximized at

```text
alpha_r^*
 =(2r-1+sqrt(4r^2+1))/2.
```

## Native period-nine theorem

The single rational delay

```text
alpha=37/2
```

works for every `r<=9`. At period nine its shape is `297/281`. The exact
certificates

```text
64^93>81^88,
88*297-93*281=3
```

give an approximation exponent greater than one. `T-9422` therefore proves,
without an external source theorem, that every eventually periodic positive
increment directive of minimal eventual period at most nine has irrational
selected context.

## Exact period-ten delayed-family ceiling

`R-9410` proves for every real delay ratio

```text
f_10(alpha)<263/250
```

because

```text
13alpha^2-500alpha+4880>0
```

has discriminant `-3760`. Together with `64^20<81^19`,

```text
mu_10^delay(alpha)<4997/5000<1.
```

Thus no further placement of one equal-phase delayed Gaussian-binomial window
can close period ten.

`X-9413` digest:

```text
ddce893eef7edf6b15c5b83dc2598bf7a832479507cf2c92309dba2172c8ec4c
```

Frozen checks:

```text
630 Laurent-product identities,
180 exact zero windows,
36 first-error comparisons,
49,680 monomial-height inequalities.
```

## Other exact method closures

- `T-9416`: equal allocation is uniquely optimal in the full phasewise
  root-product class.
- `R-9407`: scalar aligned adjacent-order Casoratians remain below one at period
  ten even with zero quadratic cofactor-height cost.
- `R-9405`: Rochev's single-expanding-place theorem does not directly apply to
  the two-place stack parameter.
- `R-9409`: a rational sequence may have different real and `2`-adic limits; a
  positive real tail bound cannot bound a rational `2`-adic tail numerator.

The denominator-descent lemmas `L-9416` and `L-9417` remain valid, but they do
not by themselves imply finite tail state, periodicity, or irrationality.

## Withdrawn overclaims

The following files are retained as explicit corrections:

```text
T-9418  unbounded-gap irrationality             WITHDRAWN
T-9419  all positive directives irrational      WITHDRAWN
T-9420  rational iff eventually periodic        WITHDRAWN
T-9421  ordinary section equals {0,1}            WITHDRAWN
```

Their common invalid step identified a bounded real completion limit with a
separate rational `2`-adic completion limit. M1 remains open.

## Exact current frontier

```text
minimal eventual periods 1,...,9:
  excluded both natively and source-dependently;

minimal eventual period 10:
  first fixed-period target;

balanced nonperiodic 17/18:
  open; requires period-uniform estimates and S-adic passage;

full ordinary section M1:
  open; requires a genuine numerator/height or stabilization theorem.
```

The load-bearing period-ten routes are now:

1. Padé cancellation of the combined native moment sequence;
2. an applicable theorem for the homogeneous order-two `q`-difference equation;
3. phase-sensitive Hermite--Padé or symbolic maximal-minor factors;
4. a completion-height determinant coupling ordinary and `2`-adic coordinates.

## Review first

1. `claims/L-9418-delayed-window-block-pade.md`
2. `claims/T-9422-native-period-nine-delayed-pade.md`
3. `claims/R-9410-delayed-window-period-ten-ceiling.md`
4. `experiments/X-9413-delayed-window-pade/run.py`
5. `claims/L-9415-homogeneous-order-two-q-difference.md`
6. `claims/R-9408-vw-measure-elimination-fails.md`
7. `claims/R-9409-completion-limit-mismatch.md`
8. `claims/L-9412-vaananen-wallisser-interface.md`
9. `claims/T-9417-eventually-period-nine-irrationality.md`
10. `claims/L-9410-block-gaussian-pade.md`

## Next theorem target

Construct a period-ten approximation that cancels the combined native moments
or exploit the order-two functional equation. The delayed family misses by less
than one percent, but `R-9410` proves that window movement alone is exhausted.
Every next estimate must report exact reduced height and its dependence on both
period and Padé order.