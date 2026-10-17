# L-9704 — Connector-free stage coordinate

**Claim ID:** `L-9704`  
**Title:** A scaled ordinary boundary coordinate removes every connector inverse and exposes a fixed 256-term `{2,3}`-unit stage sum  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-22  
**Dependencies:** PR #3 `L-0016`, `L-0017`, `T-0027`; `T-9704` and `L-9705` for endpoint heights  
**Scope:** physically overlapping signed corrected 256-transition phase-`-34` stages at stabilized scales `m>=12`

## Stabilized tower data

Put

```text
B=2^m,
delta=2^(m-8),
t_j=B+j*delta   (0<=j<=256),
t_257=2B+2delta.
```

Order the four tower types by initial binary exponents `5,6,7,8`. Their stabilized finite-core data are

```text
p=(5,30,20,56),
b=(9,54,36,24).
```

For type `i` at height `t`, write

```text
H_t=2^(11(t+1)),
N_t=3^(7(t+1)).
```

The exact binary and ternary anchors are

```text
A_i(t)=H_t*p_i/64,
B_i(t)=(N_t*p_i+b_i)/64.
```

For the connector from `i_j@t_j` to `i_(j+1)@t_(j+1)`, put

```text
X_j=p_(i_j)+64*eta_j,
Y_j=p_(i_(j+1))+64*theta_j.
```

The mixed-radix connector identity is exactly

```text
N_(t_j)*X_j+b_(i_j)=H_(t_(j+1))*Y_j.          (1)
```

## Connector-free coordinate

The corrected local residual map is

```text
H_(t_(j+2))*z_(j+1)=N_(t_j)*z_j+C_j,
C_j=(Y_j-X_(j+1))/64.
```

Define

```text
Z_j=X_j+64*H_(t_(j+1))*z_j.                    (2)
```

Then all connector inverses cancel:

```text
H_(t_(j+1))*Z_(j+1)=N_(t_j)*Z_j+b_(i_j).       (3)
```

Also

```text
Z_j = p_(i_j) (mod 64).                         (4)
```

If `n_j` is the corresponding physical phase-`-34` shortcut-Collatz boundary state, then

```text
64*(n_j+34)=H_(t_j)*Z_j.                        (5)
```

Thus `Z_j` is an ordinary physical cofactor, not merely a formal conjugacy coordinate.

Equation (3) gives

```text
gcd(Z_j,Z_(j+1)) divides b_(i_j).               (6)
```

Hence no prime at least five divides consecutive connector-free boundary coordinates.

## Complete stage identity

Put

```text
A_m=(5369/2)*2^m+1792,
E_m=(8459/2)*2^m+2816.
```

For `0<=j<=255`, define

```text
U_(m,j)=11*sum_(s=1)^j (t_s+1),
V_(m,j)= 7*sum_(s=j+1)^255 (t_s+1).
```

Iterating (3) gives

```text
2^(E_m)*Z_(m,256)
 =3^(A_m)*Z_(m,0)
  +sum_(j=0)^255 b_(i_j)*2^(U_(m,j))*3^(V_(m,j)).   (7)
```

Physical stage overlap identifies `Z_(m,256)=Z_(m+1,0)`. Writing this common integer as `Z_(m+1)` gives

```text
2^(E_m)*Z_(m+1)
 =3^(A_m)*Z_m+B_m(w_m),                          (8)
```

where `B_m(w_m)` is the positive 256-term sum in (7).

With `L=2^(m-9)`, the exponents have the fixed form

```text
U_(m,j)=11*j*(j+513)*L+11*j,
V_(m,j)=7*(255-j)*(j+768)*L+7*(255-j).
```

Therefore each fixed word has one scale-independent monomial dictionary:

```text
B_m(w)=sum_(j=0)^255 c_j(w)*Lambda_j^L,

c_j(w)=b_(i_j)*2^(11j)*3^(7(255-j)),
Lambda_j=2^(11j(j+513))*3^(7(255-j)(j+768)).      (9)
```

Every internal term is supported only on primes two and three.

## Cap and co-cap endpoints

On a cap chain, `z_m=R_m>=0`, so `Z_m>0`. Since `0<X_(m,0)<64*H_(t_(m,1))`, `T-9704` gives

```text
limsup log_2(Z_m)/E_m <=2166/346819 <1/160,
limsup log_2(Z_(m+1))/E_m <=4332/346819 <1/80.   (10)
```

On the co-cap alternative of `L-9705`, `z_m=R_m-2^(D_m)<0`. Then `Z_m<0`; put

```text
U_m=-Z_m>0.
```

Negating (8) gives

```text
3^(A_m)*U_m=2^(E_m)*U_(m+1)+B_m(w_m).            (11)
```

Moreover `U_m=-p_(i_(m,0)) (mod 64)`, and the dual co-cap height estimate gives exactly the two bounds in (10) with `Z` replaced by `U`.

Thus either signed tail produces a positive endpoint sequence and a homogeneous 258-coordinate zero sum with 256 pure `{2,3}`-unit internal coordinates.

## Proof

Substitution of the four finite cores into PR #3 `L-0016` gives the anchor formulas. Multiplying the connector identity by 64 gives (1). Substituting the local residual constant into (2) yields (3) directly. The physical tower input formula gives (5), and (6) follows by taking a common divisor in (3).

Repeated substitution in (3) proves (7). Direct summation of `t_0,...,t_255` and `t_1,...,t_256` gives `A_m` and `E_m`. The prefix and suffix sums give (9). Finally, the cap and co-cap endpoint estimates follow by combining the connector bound with `T-9704` and the dual estimate in `L-9705`.

## Status and gap audit

- The stage identities are exact but inherit the `PROPOSED` status of the frozen PR #3 interface.
- The moving endpoints prevent a naive fixed-rank `S`-unit application.
- `L-9706` resolves that issue using Evertse's projective almost-`S`-unit theorem, whose hypotheses allow moving endpoints of sufficiently small outside-prime height.
- `X-9704` independently reconstructs the finite cores, local conjugacy, physical identity, exponent dictionary, and height gates.