# LIT-KTHM-0039 — The ordinary quadratic bulk is multiplication by two in the formal multiplicative group

**Type:** self-contained p-adic formal-group normalization.  
**Maps to:** `PR3/T-0030` and the inverse logarithmic bulk in `PR3/L-0023`.

## Statement

For `m>=0`, put

```text
Y_m=3^(7*2^m),
V_m=(Y_m-1)/2^(m+2).
```

Then

```text
Y_(m+1)=Y_m^2,                                        (1)
```

and

```text
V_(m+1)=V_m+2^(m+1)V_m^2.                            (2)
```

In the formal multiplicative-group coordinate

```text
U_m=Y_m-1,
```

the update is

```text
U_(m+1)=2U_m+U_m^2,                                  (3)
```

which is the formal group law for doubling. In the logarithmic coordinate,

```text
log_2(Y_(m+1))=2 log_2(Y_m),                          (4)
```

and explicitly

```text
log_2(Y_m)=7*2^m log_2(3).                            (5)
```

## Proof

Equation `(1)` is immediate from the exponent. Write

```text
Y_m=1+2^(m+2)V_m.
```

Squaring gives

```text
Y_(m+1)
 =1+2^(m+3)V_m+2^(2m+4)V_m^2
 =1+2^(m+3)(V_m+2^(m+1)V_m^2),
```

which proves `(2)` and `(3)`. The 2-adic logarithm is a homomorphism on the relevant principal-unit subgroup, so `(4)` follows from `(1)`, and `(5)` follows from the definition of `Y_m`. ∎

## Research consequence

A stage router need not treat `(2)` as a generic nonlinear recurrence. It may be decomposed into:

1. ordinary integer squaring in the physical coordinate;
2. formal-group filtration for low-bit correctness;
3. linear doubling in the logarithmic analysis coordinate;
4. a separate proof that new precision is generated rather than preloaded.

## Non-consequence

The logarithm linearizes analysis but is a completed 2-adic object. A Collatz certificate still has to generate each required future digit from one finite ordinary state.