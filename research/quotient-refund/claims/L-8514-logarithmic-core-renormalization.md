# L-8514 — The primitive-core decoder is an exact base-nine logarithmic renormalization

**Claim ID:** `L-8514`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `T-8507`; elementary `2`-adic logarithm and LTE  
**Cross-interface:** PR #51 `L-8005`  
**Scope:** every legal intrinsic primitive-core transition

## 1. Finite marker normalization

Fix an intrinsic state

\[
(t,\gamma,i,C),
\qquad
16\mid t,
\quad
\gamma\in\{1,2,3\},
\quad
i\in\{0,1,2,3\},
\quad
\gcd(C,6)=1.
\]

Put

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\tag{1}
\]

with

```text
beta=(2,3,2,1),
p=(5,30,20,56).
```

The source marker is

\[
2^i3^\gamma C\equiv p_i\pmod {64}.
\tag{2}
\]

Define

\[
\boxed{
\delta_{\gamma,i}
\equiv
G
\equiv
1+\gamma-\beta_i
\pmod2,}
\tag{3}
\]

with `delta_(gamma,i) in {0,1}`. Then

\[
\boxed{-3^{\delta_{\gamma,i}}C\in1+8\mathbf Z_2.}
\tag{4}
\]

Let

\[
\boxed{
\alpha=\log_9(-3^{\delta_{\gamma,i}}C)
\in\mathbf Z_2,}
\tag{5}
\]

where `log_9` is the inverse of the group isomorphism

\[
\mathbf Z_2\longrightarrow1+8\mathbf Z_2,
\qquad
x\longmapsto9^x.
\]

The complete source marker `(2)` becomes one short additive residue

\[
\boxed{
\alpha\equiv a_{\gamma,i}
\pmod {2^{\max(3-i,0)}},}
\tag{6}
\]

where the finite table is

| `gamma` | `i=0` mod `8` | `i=1` mod `4` | `i=2` mod `2` | `i=3` |
|---:|---:|---:|---:|---:|
| `1` | `5` | `2` | `1` | `0` |
| `2` | `5` | `1` | `1` | `0` |
| `3` | `4` | `1` | `0` | `0` |

For `i=3` the modulus is one and the last entry is only a placeholder.

## 2. Exact valuation router

Put

\[
\boxed{
r=\frac{G-\delta_{\gamma,i}}2,}
\tag{7}
\]

\[
\boxed{w=\alpha+r.}
\tag{8}
\]

Since

\[
C=-3^{-\delta_{\gamma,i}}9^\alpha,
\]

the core numerator becomes

\[
\boxed{
3^GC+1=1-9^w.}
\tag{9}
\]

Let

\[
L=11(t+17)+j-i
\tag{10}
\]

be the full binary exponent of a prospective target type `j`.

Then an ordinary transition has exact target type `j` if and only if

\[
\boxed{
\nu_2(w)=L-3
=11(t+17)+j-i-3,}
\tag{11}
\]

and the normalized output satisfies the next short marker described below.

Equivalently, whenever `w!=0`, the valuation alone proposes the unique integer

\[
\boxed{
j=
u_2(w)-11(t+17)+i+3.}
\tag{12}
\]

The transition can be legal only when this value lies in `{0,1,2,3}`.

## 3. Normalized-unit renormalization

For the proposed target `j`, put

\[
\boxed{
\delta'=\delta_{\beta_i,j}
\equiv1+\beta_i-\beta_j
\pmod2.}
\tag{13}
\]

Define the normalized unit

\[
\boxed{
\mathcal U_{\delta'}(w)
=
3^{\delta'}
\frac{9^w-1}{2^{3+\nu_2(w)}}.}
\tag{14}
\]

The transition is legal exactly when

\[
\boxed{
\mathcal U_{\delta'}(w)
\in1+8\mathbf Z_2}
\tag{15}
\]

and its logarithm satisfies the next finite marker

\[
\boxed{
\alpha'
:=
\log_9(\mathcal U_{\delta'}(w))
\equiv
a_{\beta_i,j}
\pmod {2^{\max(3-j,0)}}.}
\tag{16}
\]

When `(11)` and `(16)` hold, the exact next ordinary core is

\[
\boxed{
C'=
\frac{1-9^w}{2^{3+\nu_2(w)}}>0,}
\tag{17}
\]

and

\[
\boxed{-3^{\delta'}C'=9^{\alpha'}.}
\tag{18}
\]

The finite state updates to

\[
(t+16,\beta_i,j,\alpha').
\]

Thus the intrinsic core decoder is conjugate to the exact `2`-adic Gauss-type map

```text
alpha
 -> w=alpha+r
 -> j=v2(w)-11(t+17)+i+3
 -> normalized unit 3^delta'*(9^w-1)/2^(3+v2(w))
 -> alpha'=log_9(normalized unit),
```

with only the short marker `(16)` remaining after the valuation selects `j`.

## Proof

### Base-nine logarithm and source marker

The usual `2`-adic logarithm maps `1+8Z_2` isomorphically to `8Z_2`. Since

\[
\log9=8\cdot u
\]

for a `2`-adic unit `u`, exponentiation by nine is an isomorphism from `Z_2` to `1+8Z_2`.

From `(2)`, divide by `2^i` modulo `2^(6-i)`. Direct substitution of the four rows `p_i`, the three values of `gamma`, and `(3)` gives

\[
-3^{\delta_{\gamma,i}}C\equiv1\pmod8,
\]

proving `(4)`. The same twelve finite checks give the displayed residues modulo `2^(6-i)`. Because

\[
\nu_2(9^x-9^y)=3+\nu_2(x-y),
\]

reduction of `9^alpha` modulo `2^(6-i)` is equivalent to reduction of `alpha` modulo `2^(3-i)`, proving `(6)` and the table.

### Valuation identity

Equation `(3)` makes `G-delta` even, so `(5)` gives

\[
3^GC
=-3^{G-\delta}9^\alpha
=-9^{\alpha+(G-\delta)/2}.
\]

This proves `(7)--(9)`.

For every nonzero `w in Z_2`,

\[
\boxed{
\nu_2(9^w-1)=3+\nu_2(w).}
\tag{19}
\]

For ordinary nonzero integers this is LTE. For general `w`, it follows from the base-nine logarithm isomorphism, or by approximation by ordinary odd units after extracting the exact power of two.

An exact core transition is

\[
2^LC'=1-9^w
\]

with `C'` odd. Taking valuations and using `(19)` proves `(11)--(12)`.

### Output marker

Equation `(17)` follows from `(9)` and `(11)`. The right side is positive as an ordinary integer because

\[
9^\alpha=-3^\delta C
\]

is the negative ordinary integer represented by the source core, so `9^w` is also negative ordinary.

Multiplying `(17)` by `-3^(delta')` gives `(14)` and `(18)`. The next physical marker is equivalent, by the first part of the proof applied to `(beta_i,j,C')`, to membership in `1+8Z_2` and the short logarithmic residue `(16)`. This proves both directions. ∎

## Constructive meaning

The giant next-type divisibility has a fixed-coordinate interpretation:

```text
one translated 2-adic logarithm w=alpha+r
must have one of four consecutive exact valuations;
the normalized unit is fed back through the same log_9 map;
only <=3 marker bits remain after the valuation chooses the type.
```

This is the phase-34 analogue of PR #51 `L-8005`. Both live positive architectures are exact `+1` Syracuse cores whose run/type resource is the valuation of a translated base-nine logarithmic coordinate.

The new coordinate suggests a concrete ambitious target: find a finite union of logarithmic balls that is invariant under `(14)--(16)`, intersects the logarithms of negative ordinary units `-3^delta C`, and forces the valuation window `(11)` forever.

## Gap audit

- `alpha` is generally a genuine `2`-adic integer, not an ordinary exponent.
- An invariant logarithmic ball does not by itself prove that its inverse image is a positive ordinary core.
- The valuation condition must be paired with the next short marker `(16)`.
- A periodic or automatic logarithmic itinerary may still select only a nonordinary completion.
- No invariant family, explicit core, or counterexample integer is supplied.