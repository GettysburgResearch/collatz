# L-9406 — Active one-stage quotient conjugacy

Claim ID: L-9406  
Title: Every exact stack transition is an odd affine isometry on the unused high quotient  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: every pair of nonnegative stack heights  
Related counterexample candidates: issue #4 active stack frontier; no `K-####` candidate

## Setup

For a stack height `m>=0`, put

```text
L_m = 9m+1,
M_m = 64^(L_m),
A_m = 81^(L_m),
c_m = (M_m+17)/81.
```

The exact stage word is

```text
S_m(x)=M_m*x+c_m,
```

and the amplifier identity sends it to

```text
81^(9m)*(81x+1)=A_m*x+81^(9m).
```

Fix a next height `n>=0`.  Let `r_(m,n)` be the unique residue in
`[0,M_n)` satisfying

```text
A_m*r_(m,n)+81^(9m) = c_n mod M_n.             (1)
```

Equivalently,

```text
r_(m,n)
 = A_m^(-1)*(c_n-81^(9m)) mod M_n.             (2)
```

Define the integer carry

```text
k_(m,n)
 = [A_m*r_(m,n)+81^(9m)-c_n]/M_n.              (3)
```

## Statement

An ordinary context `x` regenerates exactly from height `m` to height `n` iff

```text
x=r_(m,n)+M_n*y                                (4)
```

for one integer `y`.  In that case the next context is exactly

```text
x' = A_m*y+k_(m,n).                             (5)
```

Thus the unused high quotient undergoes an odd affine map.  In particular, for
all integers `y,z`,

```text
v_2(x'(y)-x'(z))=v_2(y-z).                      (6)
```

The one-stage transition neither creates nor destroys `2`-adic precision in
the unconsumed quotient.

More generally, if the next context must lie in one residue cylinder

```text
x'=R+Q*Z,
```

where `Q` is a power of `2`, then (5) fixes exactly one class

```text
y = A_m^(-1)*(R-k_(m,n)) mod Q.                (7)
```

Every additional exact future cylinder therefore selects quotient digits but
does not branch into multiple compatible quotient classes.

## Proof

Substitute (4) into the amplifier output:

```text
A_m*x+81^(9m)
 =A_m*r_(m,n)+81^(9m)+A_m*M_n*y
 =c_n+M_n*(k_(m,n)+A_m*y).                      (8)
```

The right side is `S_n(x')` exactly when (5) holds.  Conversely, integrality of
`x'` forces (1), hence (4), because `A_m` is odd and invertible modulo `M_n`.
This proves the equivalence and (5).

Since `A_m` is odd,

```text
v_2(A_m(y-z))=v_2(y-z),
```

which proves (6).  Reducing (5) modulo `Q` and inverting `A_m` proves (7).
**QED**

## Relationship to the demand map

Reducing (2) at any depth `j<=L_n` gives

```text
r_(m,n) mod 64^j
 =17*81^(-(9m+2))-81^(-1) mod 64^j
 =D_j(m).
```

Thus the next height determines **how many** digits of the universal demand
`D(m)` are consumed.  It does not alter those demanded digits.

## Dependency audit

The proof is direct algebra from the stack identity.  No branch-external
rigidity theorem, experiment, or probabilistic assumption is used.

## Gap audit

- Precision preservation in the unused quotient does not say that the quotient
  is small, positive, or ordinary at infinite depth.
- Active steering may transport arbitrarily many preloaded digits through the
  odd affine maps.
- The lemma does not prove that future demand digits are statistically
  independent or computationally hard to generate.

## Adversarial tests

`X-9404` checks the residue, carry, exact stage equality, and valuation
preservation on a frozen grid of height pairs and quotient values.

## Remaining uncertainty

Independent reconstruction is pending.  The infinite question is whether the
nested quotient digits selected by (7) eventually terminate in one ordinary
initial context or define only a nonordinary `2`-adic point.

## Suggested next attack

Compose (7) over an entire height directive and compare the resulting initial
cylinder with the ordinary least-representative stabilization criterion in
T-9409.
