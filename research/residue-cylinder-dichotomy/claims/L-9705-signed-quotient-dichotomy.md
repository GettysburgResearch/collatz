# L-9705 — Signed quotient extinction and the cap/co-cap dichotomy

**Claim ID:** `L-9705`  
**Title:** Every signed ordinary corrected-stage trajectory eventually has quotient zero or minus one, with the same completion-height bound in both cases  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-22  
**Dependencies:** `L-9702`, `L-9703`, `T-9703`, `T-9704`; frozen PR #3 `T-0027` stage interface  
**Scope:** every signed ordinary integer trajectory through the corrected 256-transition stage system

## Exact signed continuation

At scale `m`, write the complete canonical stage tile as

```text
z_m=R_m+Q_m*Y_m,
z_(m+1)=S_m+P_m*Y_m,

Q_m=2^(D_m),
P_m=3^(A_m),
0<=R_m<Q_m,
0<=S_m<P_m.
```

Continuation into the next stage is

```text
S_m+P_m*Y_m=R_(m+1)+Q_(m+1)*Y_(m+1).             (1)
```

`T-9703` gives

```text
kappa_m=P_m/Q_(m+1)<1/4.                          (2)
```

## Nonnegative tail

If `Y_m>=0`, equation (1) forces `Y_(m+1)>=0` and

```text
0<=Y_(m+1)<kappa_m*(Y_m+1)<(Y_m+1)/4.             (3)
```

For an integer `Y_m>=1`, the right side is at most `Y_m/2`; `Y_m=0` forces `Y_(m+1)=0`. Hence every nonnegative tail reaches

```text
Y_m=0,
z_m=R_m,
S_m=R_(m+1).                                      (4)
```

## Negative tail

If `Y_m<=-1`, the stage output is at most `S_m-P_m<0`, so `Y_(m+1)<=-1`. Put

```text
K_m=-Y_m-1>=0.
```

Substitution in (1) gives

```text
Q_(m+1)*K_(m+1)
 =P_m*K_m+(P_m-S_m)-(Q_(m+1)-R_(m+1)).            (5)
```

Since `P_m-S_m<=P_m` and `Q_(m+1)-R_(m+1)>=1`,

```text
0<=K_(m+1)<kappa_m*(K_m+1)<(K_m+1)/4.             (6)
```

Thus `K_m` reaches zero. Every negative tail eventually has

```text
Y_m=-1,
z_m=R_m-Q_m,
P_m-S_m=Q_(m+1)-R_(m+1).                          (7)
```

Define the positive co-cap corrections

```text
Rbar_m=Q_m-R_m,
Sbar_m=P_m-S_m.
```

The tail condition is

```text
Sbar_m=Rbar_(m+1).                                 (8)
```

## Dual completion-height bound

Write the normalized complete stage map as

```text
z_(m+1)=Lambda_m*z_m+beta_m.
```

On a co-cap tail, `z_m=-Rbar_m`, so

```text
Rbar_(m+1)=Lambda_m*Rbar_m-beta_m.                 (9)
```

`L-9703` gives

```text
|beta_m|<256*Lambda_m,
Lambda_m>257.
```

Therefore

```text
Rbar_(m+1)+257
 <Lambda_m*(Rbar_m+257).                           (10)
```

This is exactly the shifted recurrence used in `T-9704`. Hence

```text
limsup log_2(Rbar_m+257)/D_m
 <=161341/44508739
 <1/275.                                           (11)
```

The cap and co-cap alternatives have the same ordinary-height budget.

## Consequence

Every signed ordinary completion must eventually become either an exponentially short cap chain near zero or an exponentially short co-cap chain near the top of the complete dyadic cylinder. `L-9706` excludes both by the same projective almost-`S`-unit argument.

## Adversarial audit

- The fixed negative quotient is `Y=-1`, not zero.
- The dual correction is `Q-R`, and the dual output is `P-S`.
- Strict negativity uses `S<P`.
- The `+257` shift requires the strict lower bound `Lambda>257`.
- `X-9704` exhausts exact small signed quotient continuations independently.