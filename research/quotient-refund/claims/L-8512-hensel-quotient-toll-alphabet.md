# L-8512 — The intrinsic Hensel quotient routes through one affine copy of the fixed toll alphabet

**Claim ID:** `L-8512`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `T-8507`, the block inverses of `L-8506`  
**Scope:** every intrinsic primitive-core state at a multiple-of-sixteen height

## Statement

Fix an intrinsic finite state

\[
(t,\gamma,i),
\qquad
16\mid t,
\quad
\gamma\in\{1,2,3\},
\quad
i\in\{0,1,2,3\}.
\]

Put

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\qquad
A=3^G,
\tag{1}
\]

with

```text
beta=(2,3,2,1),
b=(9,54,36,24),
b_j=2^j 3^(beta_j).
```

Define the canonical high inverse and its ordinary carry

\[
\boxed{a=[-A^{-1}]_{2^D},}
\tag{2}
\]

\[
\boxed{h=\frac{Aa+1}{2^D}.}
\tag{3}
\]

### 1. Unimodular Hensel coordinate

The matrix

\[
\boxed{
\mathcal H_{t,\gamma,i}
=
\begin{pmatrix}
2^D&a\\
A&h
\end{pmatrix}
\in\operatorname{SL}_2(\mathbf Z).}
\tag{4}
\]

Every positive core satisfying the high divisibility gate has one unique form

\[
\boxed{C=a+2^Dq,\qquad q\in\mathbf Z_{\ge0},}
\tag{5}
\]

and its exact high quotient is

\[
\boxed{Y=\frac{AC+1}{2^D}=h+Aq.}
\tag{6}
\]

Conversely the ordinary Hensel quotient is intrinsic:

\[
\boxed{q=hC-aY.}
\tag{7}
\]

The core is primitive exactly when

\[
\boxed{3\nmid a+2^Dq.}
\tag{8}
\]

### 2. Direct changing-modulus recurrence

Suppose the current six-bit gate selects target type `j`. Then

\[
C'=Y/2^j.
\]

At the next finite state `(t+16,beta_i,j)`, put

\[
G'_j=7(t+17)+\beta_i-\beta_j,
\qquad
D'_j=11(t+33)-j,
\tag{9}
\]

\[
A'_j=3^{G'_j},
\qquad
a'_j=[-(A'_j)^{-1}]_{2^{D'_j}}.
\tag{10}
\]

Let

\[
\boxed{H_t=2^{11(t+33)}.}
\tag{11}
\]

Then the next high divisibility is equivalent to the one exact affine quotient equation

\[
\boxed{
H_tq'=Aq+h-2^ja'_j,}
\tag{12}
\]

where `q'>=0` is the next intrinsic Hensel quotient.

### 3. Fixed toll alphabet for all four huge residues

Put

\[
\boxed{E=7(t+17)+\beta_i.}
\tag{13}
\]

For every target type `j`, define

\[
\boxed{x_j=2^ja'_j.}
\tag{14}
\]

Then

\[
\boxed{
x_j=[-b_j3^{-E}]_{H_t}.}
\tag{15}
\]

Consequently the current target-`j` gate together with the complete next high divisibility is exactly

\[
\boxed{
q\equiv\varrho_j
:=
\left[
-A^{-1}h-3^{-(G+E)}b_j
\right]_{H_t}
\pmod {H_t}.}
\tag{16}
\]

Equivalently, with

\[
\Lambda=[-A^{-1}h]_{H_t},
\qquad
U=[-3^{-(G+E)}]_{H_t},
\tag{17}
\]

all four complete residues are

\[
\boxed{
\varrho_j=[\Lambda+Ub_j]_{H_t},
\qquad j=0,1,2,3.}
\tag{18}
\]

The multiplier `U` is odd, and the four `b_j` are distinct modulo `H_t`, so the four `varrho_j` are distinct.

Moreover `(16)` automatically gives the correct current physical six-bit target:

\[
\boxed{
[3^{\beta_i}(h+A\varrho_j)]_{64}=p_j,}
\tag{19}
\]

where

```text
p=(5,30,20,56).
```

Thus no separate target-cell condition is missing from `(16)`.

### 4. Exact primitive-lift gate

For a fixed `j`, write

\[
q=\varrho_j+H_t\ell.
\tag{20}
\]

Because `2^D H_t` is a unit modulo three, exactly one residue of `ell mod3` makes

\[
a+2^Dq
\]

divisible by three. Let

\[
\boxed{V_{t,\gamma,i,j}\subset\{0,1,2\}}
\tag{21}
\]

be the complementary two-element set. Then `(20)` is a legal primitive source exactly when

\[
\boxed{\ell\bmod3\in V_{t,\gamma,i,j}.}
\tag{22}
\]

The next core is automatically prime to three, because `AC+1` is congruent to one modulo three and its divisor is a power of two.

### 5. Exact refund in the Hensel quotient

Define the nonnegative canonical carry

\[
\boxed{
\tau_j=
\frac{A\varrho_j+h-x_j}{H_t}.}
\tag{23}
\]

For every ordinary `ell>=0`, the affine identity

\[
\boxed{
q=\varrho_j+H_t\ell
\quad\Longmapsto\quad
q'=\tau_j+A\ell}
\tag{24}
\]

holds. It is a legal primitive-core transition precisely for the two allowed classes `(22)`.

Thus the full enormous next-boundary selector is one affine copy of the fixed four-symbol toll alphabet `b`, followed by one exact ternary exclusion and the same odd multiplicative refund `A=3^G`.

## Proof

Equation `(3)` gives

\[
2^Dh-Aa=1,
\]

which proves `(4)`. Multiplying `(5)` by `A`, adding one, and using `(3)` proves `(6)`. The inverse of the determinant-one matrix in `(4)` is

\[
\begin{pmatrix}h&-a\\-A&2^D\end{pmatrix},
\]

so `(7)` follows. Equation `(8)` is the definition of the primitive core in this coordinate.

At the next state, high divisibility says

\[
C'=a'_j+2^{D'_j}q'.
\]

Multiplying by `2^j` and using `C'=Y/2^j` gives

\[
Y=2^ja'_j+2^{D'_j+j}q'.
\]

Since `D'_j+j=11(t+33)`, substituting `(6)` proves `(12)`.

For `(15)`, note that

\[
E=G'_j+\beta_j.
\]

The next inverse relation gives

\[
A'_ja'_j\equiv-1\pmod {2^{D'_j}}.
\]

Multiplying by `2^j3^(beta_j)` yields

\[
3^E x_j
\equiv
-2^j3^{\beta_j}
=-b_j
\pmod {H_t}.
\]

Both `x_j` and the canonical residue in `(15)` lie in `[0,H_t)`, proving equality.

Equation `(12)` is integral exactly when

\[
Aq+h\equiv x_j\pmod {H_t}.
\]

Substitute `(15)` and multiply by `A^{-1}` to obtain `(16)--(18)`. Distinctness follows because `U` is a unit and the four fixed integers `b_j` are distinct and smaller than `H_t`.

For `(19)`, equation `(12)` gives

\[
h+A\varrho_j\equiv x_j=2^ja'_j\pmod {64}.
\]

The automatic source-marker identity of `T-8507`, applied to the next state `(t+16,beta_i,j)`, is

\[
2^j3^{\beta_i}a'_j\equiv p_j\pmod {64}.
\]

This proves `(19)`.

Under `(20)`, the source core is

\[
C=a+2^D\varrho_j+2^DH_t\ell.
\]

Its coefficient of `ell` is a ternary unit, so exactly one class modulo three is forbidden and the other two give `(21)--(22)`. The next core is prime to three by the observation following `(22)`.

Finally `(23)` is integral by `(16)`. Its numerator is greater than `-H_t` and divisible by `H_t`, so `tau_j>=0`. Substituting `(20)` in `(12)` proves `(24)`. ∎

## Constructive meaning

This coordinate removes the local eight-block bookkeeping before the top-boundary step.

```text
ordinary root state:
  one Hensel quotient q;

complete next selector:
  q mod H_t lies in Lambda + U*{9,54,36,24};

primitive gate:
  two allowed classes of the free lift mod3;

next quotient:
  q' = tau_j + 3^G*ell.
```

The four moving billion-bit residues are therefore not arbitrary. They are one affine image of a fixed four-integer alphabet, and the coordinate change is generated by the same finite inverse arithmetic already present in the packet.

The normalized routing remainder may also be written as

\[
[-3^E(Aq+h)]_{H_t}\in\{9,54,36,24\},
\]

so the target type is the unique fixed toll returned by one exact modular evaluation.

## Gap audit

- A fixed toll alphabet does not prove that one finite ordinary quotient hits it forever.
- The affine parameters `Lambda` and `U` change with the height and finite state.
- The theorem does not make the canonical carries `tau_j` equal or periodic.
- The two-of-three primitive lift gate remains an exact changing-state condition.
- No initial integer, self-covering quotient class, or all-time routing invariant is supplied.