# D-8801 — Generalized shortcut map and expanding-chart coding

Claim ID: D-8801  
Title: Generalized odd-multiplier shortcut map, parity words, and binary expanding charts  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: none  
Scope: odd multipliers `a >= 3`; generic binary charts with dyadic source radix  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

For an odd integer `a >= 3`, define the generalized shortcut map on positive
integers by

```text
T_a(n) = n/2          if n is even,
         (a*n+1)/2    if n is odd.
```

For a positive starting value `n`, its length-`L` parity word is

```text
w(n,L) = (eps_0,...,eps_(L-1)),
eps_k = T_a^k(n) mod 2.
```

A binary word `w` is **admissible at `n`** when `w=w(n,L)`. Its weight is

```text
s(w) = sum_(k=0)^(L-1) eps_k.
```

Define its affine correction recursively by

```text
B_a(empty) = 0,
B_a(w0)    = B_a(w),
B_a(w1)    = a*B_a(w) + 2^|w|.
```

Here `w0` and `w1` append the displayed bit to the right of `w`.

For integers

```text
U = 2^m,   m >= 1,
V > U,     V odd,
C = V-U,
```

and a binary directive `eps=(eps_j)_(j>=0)`, define the associated expanding
chart completion

```text
Phi_(U,V)(eps)
  = (C/V) * sum_(j>=0) eps_j * (U/V)^j  in Z_2.
```

The series converges because `v_2(U/V)=m>0`. The normalization is chosen so
that

```text
Phi_(U,V)(111...) = 1.
```

The special control chart used in this packet has

```text
U=4, V=5,
Phi_(4,5)(eps) = (1/5) * sum_(j>=0) eps_j*(4/5)^j.
```

## Definitions

- `Z_2` is the ring of `2`-adic integers.
- `v_2(x)` is the exponent of `2` in a nonzero integer or rational.
- A value is **ordinary** when it lies in the embedded copy of `Z` inside
  `Z_2`, rather than merely being a `2`-adic integer.
- A **same-phase chart** is an identity of the form

  ```text
  T_a^L(2^L q+d) = a^s q+d
  ```

  with one fixed residue phase `d` and one fixed admissible parity word of
  length `L` and weight `s`.

## Motivation

The active repository contains several exact expanding charts at `a=3`. This
definition separates their formal architecture from the numerical multiplier.
The `a=5` control universe has positive fair-parity drift, so a theorem that
survives after replacing the chart constants by `U=4,V=5` is evidence of a
certificate-format obstruction rather than evidence supplied by negative
drift.

## Proof or construction

This file is definitional. Convergence of `Phi_(U,V)` follows from

```text
v_2((U/V)^j) = m*j -> infinity.
```

Since `C=V-U` is odd,

```text
(C/V) * sum_(j>=0) (U/V)^j
  = (C/V) / (1-U/V)
  = 1
```

in `Q_2`, establishing the all-one normalization.

## Dependency audit

None.

## Gap audit

- `V` must be odd for the displayed series to have the intended dyadic
  divisibility and odd-denominator properties.
- `V>U` is used for the real interval estimates in T-8803; `2`-adic convergence
  itself only needs `v_2(U)>0` and `V` odd.
- A directive completion in `Z_2` is not automatically a positive ordinary
  integer.
- A binary directive is not automatically an admissible parity word for an
  arbitrary starting integer; admissibility must be replayed where needed.

## Adversarial tests

Experiment X-8801 replays admissible parity words and checks every affine and
same-phase identity used later in the packet.

## Remaining uncertainty

None in the definitions. The useful mathematical content begins with L-8801.

## Suggested next attack

Parameterize additional repository-specific charts by `(U,V)` and explicitly
mark which parts of their proofs use only dyadic divisibility, which use
`V>U`, and which use the particular arithmetic realization of their phases.
