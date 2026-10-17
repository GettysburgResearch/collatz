# T-8514 — The logarithmic core decoder has four explicit full isometric branches

**Claim ID:** `T-8514`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8514`; elementary LTE and finite marker arithmetic  
**Scope:** every active intrinsic state at a multiple-of-sixteen height

## Statement

Fix a state

\[
(t,\gamma,i),
\qquad
16\mid t,
\quad
t\ge3744,
\quad
\gamma\in\{1,2,3\},
\quad
i\in\{0,1,2,3\}.
\]

Use the logarithmic coordinate of `L-8514`:

\[
\alpha=\log_9(-3^\delta C),
\qquad
\delta\equiv1+\gamma-\beta_i\pmod2,
\tag{1}
\]

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\qquad
r=(G-\delta)/2,
\tag{2}
\]

and put

```text
beta=(2,3,2,1),
p=(5,30,20,56).
```

For each target type `j`, define

\[
\boxed{
v_j=D+j-3,}
\tag{3}
\]

\[
\boxed{
c_{i,j}
=
\left[
3^{-(\beta_i+1)}{p_j\over2^j}
\right]_{2^{6-j}}.}
\tag{4}
\]

The fixed table is

| current `i` | `j=0` mod `64` | `j=1` mod `32` | `j=2` mod `16` | `j=3` mod `8` |
|---:|---:|---:|---:|---:|
| `0` | `31` | `29` | `15` | `5` |
| `1` | `53` | `31` | `5` | `7` |
| `2` | `31` | `29` | `15` | `5` |
| `3` | `29` | `23` | `13` | `7` |

### 1. Four equal-radius branch balls

The intrinsic core has a legal transition of target type `j` exactly when

\[
\boxed{
\alpha
\in
\mathcal B_{t,\gamma,i,j}
:=-r+2^{v_j}
\left(
 c_{i,j}+2^{6-j}\mathbf Z_2
\right).}
\tag{5}
\]

Equivalently,

\[
\alpha+r=2^{v_j}u,
\qquad
u_2(u)=0,
\qquad
u_2(u-c_{i,j})\ge6-j.
\tag{6}
\]

All four balls have the same radius:

\[
\boxed{
\mathcal B_{t,\gamma,i,j}
\text{ is one residue modulo }2^{D+3}.}
\tag{7}
\]

They are pairwise disjoint because their translated elements have the four distinct exact valuations

\[
D-3,\ D-2,\ D-1,\ D.
\]

Each branch ball lies inside the short source-marker ball of `L-8514`.

### 2. Exact normalized branch map

For a point in branch `j`, write

\[
\boxed{
u=c_{i,j}+2^{6-j}z,
\qquad z\in\mathbf Z_2.}
\tag{8}
\]

Put

\[
\delta'_j
\equiv
1+\beta_i-\beta_j
\pmod2,
\tag{9}
\]

and define

\[
\boxed{
N_{t,i,j}(u)
=
3^{\delta'_j}
{9^{2^{v_j}u}-1\over2^{v_j+3}}
\in1+8\mathbf Z_2.}
\tag{10}
\]

Let

\[
a'_{i,j}=a_{\beta_i,j}
\tag{11}
\]

be the short next-marker residue from the table in `L-8514`. Then

\[
\boxed{
\alpha'
=
\log_9 N_{t,i,j}(u)
\equiv
 a'_{i,j}
\pmod {2^{3-j}}.}
\tag{12}
\]

Define the normalized section

\[
\boxed{
F_{t,\gamma,i,j}(z)
=
{\alpha'-a'_{i,j}\over2^{3-j}}
\in\mathbf Z_2.}
\tag{13}
\]

### 3. Every branch is a bijective isometry

For all `z,z' in Z_2`,

\[
\boxed{
\nu_2\!\left(
F_{t,\gamma,i,j}(z)-F_{t,\gamma,i,j}(z')
\right)
=
\nu_2(z-z').}
\tag{14}
\]

Consequently

\[
\boxed{
F_{t,\gamma,i,j}:\mathbf Z_2
\overset{\sim}{\longrightarrow}
\mathbf Z_2}
\tag{15}
\]

is a bijective 2-adic isometry.

Thus each finite state has four disjoint legal Hensel balls, and every one of the four branches maps onto the full normalized coordinate of its next finite state `(t+16,beta_i,j)`.

## Proof

### The fixed normalized unit

For `v>=0`, put

\[
R_v={9^{2^v}-1\over2^{v+3}}.
\tag{16}
\]

Direct calculation gives

\[
R_4\equiv61\equiv-3\pmod {64}.
\tag{17}
\]

Squaring `9^(2^v)=1+2^(v+3)R_v` gives

\[
\boxed{
R_{v+1}=R_v+2^{v+2}R_v^2.}
\tag{18}
\]

For `v>=4`, the second term is divisible by `64`. Hence

\[
\boxed{R_v\equiv-3\pmod {64}\qquad(v\ge4).}
\tag{19}
\]

For odd `u in Z_2`, the divided power series satisfies

\[
{9^{2^vu}-1\over9^{2^v}-1}
\equiv u
\pmod {2^{6-j}},
\tag{20}
\]

because `9^(2^v)` is congruent to one modulo `2^(v+3)` and `v+3>=6-j` throughout the active range. This follows first for ordinary positive odd `u` from the geometric sum and then for all odd `u in Z_2` by continuity; equivalently expand `(1+x)^u` with `x` divisible by `2^(v+3)`.

Combining `(19)--(20)` gives

\[
\boxed{
{9^{2^vu}-1\over2^{v+3}}
\equiv-3u
\pmod {2^{6-j}}.}
\tag{21}
\]

### Branch criterion

`L-8514` gives

\[
3^GC+1=1-9^{\alpha+r}.
\tag{22}
\]

A target-`j` transition has full binary exponent

\[
D+j.
\]

By LTE,

\[
\nu_2(9^w-1)=3+\nu_2(w),
\tag{23}
\]

so exact valuation is equivalent to

\[
\alpha+r=2^{v_j}u
\]

with `u` odd.

The next core is

\[
C'=-{9^{2^{v_j}u}-1\over2^{v_j+3}}.
\tag{24}
\]

Its physical source marker is

\[
2^j3^{\beta_i}C'\equiv p_j\pmod {64}.
\tag{25}
\]

Divide by `2^j` and substitute `(21)`. Equation `(25)` becomes

\[
3^{\beta_i+1}u
\equiv
{p_j\over2^j}
\pmod {2^{6-j}},
\tag{26}
\]

which is exactly `(4)--(6)`.

Since

\[
v_j+6-j=D+3,
\]

all branch moduli are equal, proving `(7)`. The translated exact valuations distinguish the branches.

The source-marker table in `L-8514` is also automatic: because `v_j>D-3>=3-i`, equation `(5)` gives

\[
\alpha\equiv-r\pmod {2^{3-i}},
\]

and the twelve direct finite checks give

\[
-r\equiv a_{\gamma,i}\pmod {2^{3-i}}.
\]

### Output coordinate

Equation `(24)` gives

\[
-3^{\delta'_j}C'=N_{t,i,j}(u).
\]

The physical marker `(25)`, applied in the finite-marker equivalence of `L-8514`, proves `(10)--(12)`.

### Exact isometry

Take two allowed odd units `u,u'` in the same branch. The factor `3^(delta')` cancels, and

\[
{N(u)\over N(u')}-1
=
{9^{2^{v_j}u'}
\left(9^{2^{v_j}(u-u')}-1\right)

over
9^{2^{v_j}u'}-1}.
\tag{27}
\]

Because `u'` is odd, LTE gives

\[
\nu_2(9^{2^{v_j}u'}-1)=v_j+3,
\]

while the numerator difference has valuation

\[
v_j+3+\nu_2(u-u').
\]

Therefore

\[
\boxed{
\nu_2\!\left({N(u)\over N(u')}-1\right)
=\nu_2(u-u').}
\tag{28}
\]

On `1+8Z_2`, the 2-adic logarithm preserves valuation. Dividing by `log9`, whose valuation is three, gives

\[
\nu_2(\alpha'(u)-\alpha'(u'))
=
u_2(u-u')-3.
\tag{29}
\]

From `(8)`,

\[
\nu_2(u-u')=6-j+\nu_2(z-z').
\]

After division by `2^(3-j)` in `(13)`, equation `(14)` follows.

For every `n`, an isometry induces an injection on the finite set `Z/2^nZ`, hence a bijection. The compatible inverse residues give a preimage of every point in `Z_2`, proving `(15)`. ∎

## Eureka consequence

At the completion level, the remaining decoder is an exact four-branch full shift:

```text
four disjoint source balls of one common depth D+3;
each branch labelled by one physical type j;
each normalized branch is an isometric bijection Z_2 -> Z_2.
```

There is no local symbolic obstruction, no loss of sections, and no shrinking of the normalized output coordinate. Every finite type word has exactly one logarithmic cylinder, and every infinite type directive has exactly one `2`-adic logarithmic completion.

The ordinary-integer boundary is consequently isolated with unusual precision: one must show that at least one of these completed logarithmic points equals `log_9(-3^delta C)` for a positive ordinary core `C`, or prove that none do.

## Gap audit

- Full-shift abundance is a statement in `Z_2`; it does not produce an ordinary positive core.
- The inverse image of an ordinary negative unit under `log_9` is generally a nonordinary `2`-adic integer.
- A periodic or automatic branch itinerary may still be excluded by existing irrationality results.
- Surjectivity of every local branch does not imply stabilization of the initial ordinary core cylinder.
- No finite initial integer or all-time ordinary routing invariant is supplied.