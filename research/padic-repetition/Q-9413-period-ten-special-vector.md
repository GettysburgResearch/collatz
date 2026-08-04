# Q-9413 — Period-ten special-vector irrationality

Claim ID: `Q-9413`  
Title: Can the first native-uncovered fixed-period stack value be excluded by its low-dimensional or combined-moment structure?  
Status: `IDEA / PRIMARY FIXED-PERIOD TARGET`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9415`, `L-9418`, `T-9422`, `R-9407`, `R-9408`, `R-9410`  
Scope: primitive positive periodic stack words of minimal period ten

## Exact starting point

For

```text
W=d_1...d_10
```

with minimal period ten,

```text
Theta(m;W^infinity)
 =sum_(j=0)^9 C_j f_R(Z lambda^j).                    (1)
```

The ten points lie in distinct `R^Z`-orbits. The selected value is also

```text
F_W(X),
X=T^(9m),
```

where

```text
F_W(X)=P_W(X)+aX^10F_W(qX).                           (2)
```

The exact source-independent delayed-window family reaches exponent

```text
max mu_10^delay
 =0.994896616714...<1,                                (3)
```

and `R-9410` gives the exact uniform ceiling

```text
mu_10^delay(alpha)<4997/5000.                         (4)
```

Period ten is therefore a small but genuine new-method boundary.

## Closed Route A — published nine-phase measure plus one scalar phase

`L-9414` showed that a nine-phase measure with exponent `omega_9` could be
combined with the scalar phase exponent

```text
tau=9/log_2(81)=1.419591945535...                     (5)
```

only if `omega_9<tau`.

`R-9408` transcribes the actual Väänänen--Wallisser measure:

```text
omega_9=2318.657271149... .                           (6)
```

Thus the published full-direction measure cannot bootstrap dimension nine to
ten. This route is closed, not merely uncomputed.

## Closed Route B — scalar aligned adjacent orders

`R-9407`, using the branch-qualified exact rank formula of PR #34, proves that
even a zero-cofactor-cost scalar adjacent-order construction has period-ten
ceiling

```text
log_81(64)*113/110
 =0.972205393003...<1.                                (7)
```

Scalar aligned neighboring orders therefore cannot be the breakthrough.

## Closed Route C — move one equal-phase cancellation window

`L-9418` permits an independent delayed zero window and improves the native
fixed-period theorem from three to nine. `R-9410` proves (4) for every delay.
No additional window movement within that root-product architecture reaches
period ten.

## Live Route 1 — native homogeneous order two

`L-9415` eliminates the polynomial inhomogeneity from (2) and gives

```text
P_W(qX)F_W(X)
-[P_W(X)+aX^10P_W(qX)]F_W(qX)
+a q^10 X^10 P_W(X)F_W(q^2X)=0.                       (8)
```

The function is entire, nonpolynomial, and formally nonrational. Rationality at
one physical point propagates down its `q`-orbit:

```text
F_W(x) in Q
 -> F_W(q^n x) in Q for every n>=0.                   (9)
```

### Deliverable

Prove, natively or from a fully inspected source theorem,

```text
dim_Q span{F_W(x),F_W(qx)}>=2                         (10)
```

for the physical rational point. Equation (9) then makes `F_W(x)` irrational.
Every source application must explicitly check:

```text
- the finite place and |q|_2<1;
- the rational coefficient polynomials in (8);
- all singular and nonvanishing conditions along the orbit;
- the required analytic or formal solution class;
- the global-height parameter at the archimedean and 2-adic places.
```

A complex theorem or an abstract mention of `q`-functional equations is not an
application.

## Live Route 2 — direct combined-moment Padé

The native block coefficients are

```text
u_N
 =R^[N(N-1)/2] Z^N P_W(X lambda^N).                   (11)
```

A direct scalar Padé system for `(u_N)` spends one condition per **combined**
coefficient rather than cancelling ten phases separately.

### Deliverable

Construct a structured denominator whose exact convolution with (11):

1. cancels a linearly growing interval of combined coefficients;
2. has a proved nonzero first survivor;
3. has an odd evaluated denominator;
4. has an exact common denominator or reduced-height bound;
5. gives limiting exponent greater than one.

The transfer polynomial `P_W` must remain visible. Promising mechanisms are:

```text
- a Christoffel transform of the pure Tschakaloff moment system;
- a phase-sensitive Hermite--Padé matrix;
- symbolic maximal-minor or cyclotomic factors;
- a q-Lucas/Cartier recurrence for the residual moment state;
- a filtered modular Padé lattice with a proof-producing short affine vector.
```

## Live Route 3 — completion-height determinant

Combine several shifted values, errors, or nearest-integer/carry states into one
ordinary integer `N_n` satisfying

```text
v_2(N_n)>log_2|N_n|.                                  (12)
```

The ordinary numerator must be proved nonzero. PR #16's appended block
coordinate and PR #33's exact cylinder recurrence are possible nonvanishing and
height interfaces; neither is currently a proof dependency.

## Period-uniform objective

A fixed period-ten theorem is a milestone, not the final stack result. The
balanced nonperiodic `17/18` directive is approached by standard words whose
lengths grow. Every successful construction must report its dependence on

```text
period r,
Padé order n,
transfer-polynomial height,
first surviving valuation,
reduced global height.
```

The desired endpoint is a bound whose constants deteriorate slowly enough to
survive adjacent standard-word periods tending to infinity.

## Success criteria

### Obstruction

Prove (1) irrational for every primitive positive period-ten word and propagate
the result through arbitrary finite prefixes.

### Construction

If one word instead yields eventual active-cylinder stabilization, reconstruct
its exact ordinary context, prove positivity at every stage, check the chart
class modulo `17`, replay the full Collatz lift, and only then create a
`K-####` candidate.

## Falsification criteria

- The published one-phase measure route is already closed by `R-9408`.
- Delayed equal-phase root products are already closed by `R-9410`.
- A determinant with no nonvanishing proof is not an approximant.
- Pre-reduction height is not reduced height.
- Bounded numerical Padé orders are evidence only.
- A period-ten theorem alone does not settle the growing S-adic frontier.

## Immediate next experiment

Build the exact combined-moment convolution matrix for representative primitive
`{17,18}` period-ten words. Before a broad search, compute:

```text
- symbolic rank and maximal-minor gcds;
- 2-adic row filtration;
- 3-adic/archimedean coefficient height;
- the first affine short-vector obstruction;
- dependence on cyclic and reversal class.
```

The first invariant that is uniform across the primitive classes should become
the next theorem target.