# L-9415 — Homogeneous order-two reduction of every periodic stack tail

Claim ID: `L-9415`  
Title: The native periodic value is a nonrational entire solution of one homogeneous second-order `q`-difference equation  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9408`; elementary power-series algebra  
Scope: every positive periodic increment word of arbitrary finite period  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Let

```text
W=d_1...d_r,
r>=1,
T=64/81,
q=T^(9S(W)),
a=T^e,
```

and let the exact finite-word transfer polynomial be

```text
P_W(X)=sum_(j=0)^(r-1) p_j X^j,
p_j in Q_{>0}.
```

Define the periodic-tail function

```text
F_W(X)
 =sum_(k>=0)
   q^[r k(k-1)/2] a^k X^(rk) P_W(q^k X).              (1)
```

At the physical starting-height point

```text
X=T^(9m),
```

this is exactly `Theta(m;W^infinity)`.

## Statement 1 — first-order native equation

The function satisfies

```text
boxed:
F_W(X)=P_W(X)+a X^r F_W(qX).                          (2)
```

### Proof

The `k=0` summand in (1) is `P_W(X)`. Multiplying `F_W(qX)` by `aX^r` and
shifting `k` to `k+1` reproduces every remaining summand. **QED**

## Statement 2 — homogeneous order two

Eliminating the polynomial inhomogeneity between (2) at `X` and at `qX`
gives

```text
boxed:
P_W(qX)F_W(X)
-[P_W(X)+a X^r P_W(qX)]F_W(qX)
+a q^r X^r P_W(X)F_W(q^2X)=0.                         (3)
```

All three coefficient polynomials are nonzero. At every physical point
`q^nT^(9m)>0`, both `P_W(X)` and `P_W(qX)` are strictly positive in the real
embedding, so no singularity is hidden in the reduction.

### Proof

Write

```text
F_W(X)-aX^rF_W(qX)=P_W(X),
F_W(qX)-a q^r X^rF_W(q^2X)=P_W(qX).
```

Multiply the first identity by `P_W(qX)`, the second by `P_W(X)`, and subtract.
**QED**

## Statement 3 — exact coefficient recurrence

Write

```text
F_W(X)=sum_(n>=0) f_n X^n.
```

Then

```text
f_j=p_j,                    0<=j<r,
f_(n+r)=a q^n f_n,          n>=0.                     (4)
```

Equivalently,

```text
f_(j+kr)
 =p_j a^k q^[k j+r k(k-1)/2].                         (5)
```

Every coefficient is a nonzero positive rational number.

## Statement 4 — formal nonrationality

```text
boxed:
F_W(X) notin Q(X).                                     (6)
```

### Proof

In the real embedding, `0<a,q<1`. Formula (5) gives

```text
lim_(n->infinity) |f_n|^(1/n)=0.                       (7)
```

Thus `F_W` is an entire complex function. It is not a polynomial because every
coefficient is nonzero. A rational function holomorphic on the whole complex
plane is a polynomial. Therefore `F_W` is not rational. **QED**

## Statement 5 — rationality propagates down the `q`-orbit

For every nonzero rational `x`, equation (2) gives

```text
F_W(qx)=[F_W(x)-P_W(x)]/(a x^r).                       (8)
```

Consequently,

```text
F_W(x) in Q
 -> F_W(q^n x) in Q for every n>=0.                   (9)
```

In particular, a theorem proving

```text
dim_Q span{F_W(x),F_W(qx)}>=2                         (10)
```

at one physical point immediately proves `F_W(x)` irrational: if the first
value were rational, (8) would make the second rational, and two rational
numbers span a one-dimensional `Q`-space.

## Why this changes the period-ten target

The ten-phase Tschakaloff decomposition diagonalizes (3), but the native value
itself belongs to a homogeneous system of order only two. The dimension-ten
cutoff of Väänänen–Wallisser is therefore not the intrinsic dimension of the
native functional equation.

Matala-aho's published work on values of homogeneous `q`-functional equations
states a dimension-at-least-two theorem under explicit coefficient, place,
solution, and determinant hypotheses. Equation (3), nonrationality (6), and
nonsingularity at the physical orbit provide the exact native input for a full
hypothesis audit. No application is claimed until the source theorem is
inspected line by line.

## Dependency audit

- `L-9408` supplies `P_W`, `S(W)`, `e`, and the repeated-block identity.
- Everything in (1)--(10) is elementary algebra and real convergence.
- No Väänänen–Wallisser, Matala-aho, Bézivin, or Mahler theorem is used in the
  proof.

## Gap audit

- Formal nonrationality does not by itself imply irrationality at a particular
  rational `2`-adic argument.
- A complex-value theorem cannot be silently transferred to `Q_2`.
- A `q`-functional theorem must permit the rational parameter `q=T^(9S(W))`,
  the finite place `2`, the singular factor `X^r` at zero, and the physical
  nonsingular orbit.
- The result is fixed-period. Uniform constants are still needed for the
  balanced S-adic limit.

## Adversarial tests

`X-9413` should reconstruct (2)--(5) for all binary period words through a
frozen length, verify the homogeneous identity symbolically, and check that no
coefficient polynomial vanishes on the physical rational orbit.

## Suggested next attack

Acquire the full Matala-aho theorem and test its exact hypotheses against (3).
If one hypothesis fails, isolate the first failure and reproduce the determinant
argument natively for this triangular order-two system rather than returning to
ten independent phase windows.
