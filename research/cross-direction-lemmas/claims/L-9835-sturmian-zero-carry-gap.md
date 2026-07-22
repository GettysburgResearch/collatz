# L-9835 — Logarithmic zero-carry gaps in the Sturmian H compiler

Claim ID: `L-9835`  
Title: The phase cocycle bounds every zero-interface run logarithmically in its starting endpoint  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: exact H cylinder concatenation; `L-9822`, `L-9829`, `L-9833`  
Scope: the unique physical interface-carry stream along the forced renormalized `10/30` schedule  
Related counterexample candidates: endpoint-descent-only reset models

## Definitions

Let

\[
R_{i+1}=T(R_i),
\qquad
R_i\in\mathcal K=\left(1,\frac{81}{64}\right],
\tag{1}
\]

be the renormalized phase orbit of `L-9822`, and let its forced suffix be

\[
z_i=
\begin{cases}
30,&1<R_i\le32/27,\\
10,&32/27<R_i\le81/64.
\end{cases}
\tag{2}
\]

Append these suffixes to a fixed exact H prefix as in `L-9833`. Write
`(V_i,Y_i)` for the odd numerator and canonical endpoint of the growing word,
and let `h_i` be the exact interface block used at stage `i`.

Put

\[
\Lambda=\frac{81}{64},
\qquad
Q=\frac{3584}{1631}.
\tag{3}
\]

Here `Q` is the fixed point of the larger of the two zero-interface affine
maps below.

## Statement

### 1. Exact affine dynamics during a zero block

If `h_i=0`, then the endpoint update is

\[
\boxed{
Y_{i+1}=p_{z_i}Y_i+\frac7{16},
}
\tag{4}
\]

where

\[
\boxed{
p_{10}=\frac{81}{128},
\qquad
p_{30}=\frac{6561}{8192}.
}
\tag{5}
\]

The input to a zero block also satisfies

\[
Y_i\ge A_{z_i}
=
\begin{cases}
72,&z_i=10,\\
4608,&z_i=30.
\end{cases}
\tag{6}
\]

Thus every stage which is about to use a zero block has `Y_i>=72`.

### 2. Exact slope cocycle

The raw endpoint slopes and the renormalized phase multipliers satisfy

\[
\boxed{
p_{z_i}=\frac34\frac{R_{i+1}}{R_i}.
}
\tag{7}
\]

Consequently, for every `t>=0`,

\[
\boxed{
\prod_{s=0}^{t-1}p_{z_{i+s}}
=\left(\frac34\right)^t\frac{R_{i+t}}{R_i}.
}
\tag{8}
\]

Moreover,

\[
p_{30}Q+\frac7{16}=Q,
\qquad
p_{10}Q+\frac7{16}<Q.
\tag{9}
\]

Hence, if

\[
h_i=h_{i+1}=\cdots=h_{i+t-1}=0,
\tag{10}
\]

then

\[
\boxed{
Y_{i+t}-Q
\le
\left(\frac34\right)^t
\frac{R_{i+t}}{R_i}(Y_i-Q)
<
\Lambda\left(\frac34\right)^t(Y_i-Q).
}
\tag{11}
\]

The first inequality retains the exact phase information; the second is the
uniform envelope on the half-open invariant core.

### 3. Logarithmic deterministic gap bound

Suppose a zero run of length `L>=1` starts at stage `i`:

\[
h_i=h_{i+1}=\cdots=h_{i+L-1}=0.
\tag{12}
\]

Then its last input obeys the phase-aware bound

\[
\boxed{
A_{z_{i+L-1}}-Q
\le
\left(\frac34\right)^{L-1}
\frac{R_{i+L-1}}{R_i}(Y_i-Q).
}
\tag{13}
\]

In particular,

\[
\boxed{
L
\le
\left\lceil
\frac{
\log\!\left(
\Lambda\dfrac{Y_i-Q}{72-Q}
\right)
}{\log(4/3)}
\right\rceil.
}
\tag{14}
\]

Thus zero-interface gaps are logarithmic, rather than merely linear, in the
current endpoint. Equivalently, a zero run of length `L` requires

\[
\boxed{
Y_i
>
Q+\frac{64}{81}(72-Q)
\left(\frac43\right)^{L-1}.
}
\tag{15}
\]

### 4. The logarithmic order is optimal for the zero-transition relation

For a suffix `z`, define its exact zero-interface relation by

\[
A_z+U_zj\longmapsto Y_z+V_zj,
\qquad j\in\mathbb Z_{\ge0}.
\tag{16}
\]

Let

\[
Z_L=z_i z_{i+1}\cdots z_{i+L-1}
\tag{17}
\]

be any length-`L` segment of the forced schedule, and let `A_{Z_L}` be the
canonical input of the exact composite suffix word. Starting the relation at
`A_{Z_L}` gives exactly `L` consecutive zero-interface transitions and ends
at the canonical endpoint `Y_{Z_L}`.

Therefore arbitrarily long finite zero paths exist in the exact scalar
transition relation. Their starting values satisfy

\[
\boxed{
Q+\frac{64}{81}(72-Q)
\left(\frac43\right)^{L-1}
<A_{Z_L}<U_{Z_L}\le2^{13L}.
}
\tag{18}
\]

Consequently the `O(log Y)` scale of (14) cannot be replaced by `o(log Y)`
using only the exact zero-interface relations.

### 5. A global logarithmic lower bound for nonzero blocks

Let

\[
M(n)=\#\{0\le i<n:h_i\ne0\}.
\tag{19}
\]

Write

\[
\rho
=\frac{\log(2187/2048)}{\log(81/64)},
\qquad
a
=\frac{(8-4\rho)\log3}{\log(4/3)}
\approx26.29253.
\tag{20}
\]

Then

\[
\boxed{
M(n)
\ge
\frac{\log n}{\log(1+a)}-O_{V_0}(1).
}
\tag{21}
\]

In particular, the exact carry stream has quantitatively more than merely
infinitely many nonzero blocks: it has at least logarithmically many up to
stage `n`.

### 6. Precise density boundary

The estimates above do **not** prove positive lower density. At an arbitrary
interface, including a nonzero one, exact concatenation gives

\[
\boxed{
Y_{i+1}
=p_{z_i}(Y_i+h_iV_i)+\frac7{16}.
}
\tag{22}
\]

Thus a nonzero block introduces the uncontrolled term `p_(z_i)h_iV_i`.
Neither endpoint descent nor the phase rotation bounds the new endpoint in
terms of the old endpoint alone. Since `V_i` grows exponentially, (14) is
compatible with zero runs whose lengths grow linearly in their starting
index.

This is a genuine logical obstruction, not a claim that the physical carry
stream has zero density. A binary sequence whose nonzero positions grow
geometrically has zero density while its successive zero gaps are `O(i)`;
therefore it satisfies the only index-scale consequence obtainable by
combining (14) with `Y_i<V_i`. More strongly, part 4 supplies exact zero paths
of every requested finite length, so an endpoint-descent-only model can join
such paths by unconstrained resets at geometrically separated stages.

A positive-density theorem needs additional arithmetic control of the
nonzero reset in (22), or a residue argument forbidding most of the long
zero-transition cylinders from being reached by the unique physical carry
stream.

## Proof

When `h_i=0`, `L-9833` gives

\[
\begin{array}{c|c}
z_i&Y_i\longmapsto Y_{i+1}\\ \hline
10&72+128j\longmapsto46+81j,\\
30&4608+8192j\longmapsto3691+6561j.
\end{array}
\tag{23}
\]

Eliminating `j` gives (4)--(6). The phase branches of `L-9822` are

\[
R_{i+1}
=
\begin{cases}
(27/32)R_i,&z_i=10,\\
(2187/2048)R_i,&z_i=30.
\end{cases}
\tag{24}
\]

Multiplying either factor by `3/4` gives the corresponding value in (5),
which proves (7); telescoping proves (8).

The number `Q=3584/1631` solves

\[
Q=\frac{6561}{8192}Q+\frac7{16}.
\]

The fixed point for the `10` map is `56/47<Q`, proving (9). Subtracting `Q`
from (4), applying (9), and iterating gives the first inequality in (11).
Because both phases lie in `(1,81/64]`, their ratio is strictly below
`81/64`, proving the second.

For a run of length `L`, the last zero-block input satisfies

\[
Y_{i+L-1}\ge A_{z_{i+L-1}}\ge72.
\]

Apply (11) with `t=L-1` to obtain (13) and

\[
72-Q
<\Lambda\left(\frac34\right)^{L-1}(Y_i-Q).
\]

Taking logarithms, using that `L-1` is an integer, proves (14); rearranging
proves (15).

For part 4, decompose the exact composite cylinder `Z_L` at its first suffix.
Its canonical input has the form `A_(z_i)+U_(z_i)j`. Its image under (16) is
the exact interface input for the remaining composite word. Induction gives
all `L` zero transitions and the final endpoint `Y_(Z_L)`. Apply (15) to this
path. The canonical bound gives

\[
0<A_{Z_L}<U_{Z_L}
=\prod_{s=0}^{L-1}U_{z_{i+s}}
\le2^{13L},
\]

which proves (18) and logarithmic optimality.

For part 5, `L-9829` gives

\[
V_s
=V_0\,3^{8s-4N_{10}(s)}
<V_0\,3^{(8-4\rho)s+4}.
\tag{25}
\]

Since `Y_s<V_s`, a zero run beginning at `s` has length at most

\[
as+O_{V_0}(1)
\tag{26}
\]

by (14). If `r_k<r_(k+1)` are consecutive nonzero-block indices, (26)
therefore yields

\[
r_{k+1}
\le(1+a)r_k+O_{V_0}(1).
\tag{27}
\]

Iteration gives `r_k=O_(V_0)((1+a)^k)`, and inversion proves (21).

Finally, the general interface equation is

\[
Y_i+h_iV_i=A_{z_i}+j_iU_{z_i},
\]

while the suffix output is `Y_(z_i)+j_iV_(z_i)`. Eliminating `j_i` and using
`Y_z-(V_z/U_z)A_z=7/16` gives (22). This identifies exactly the uncontrolled
reset term and proves the stated density boundary. ∎

## Motivation

`L-9833` used strict endpoint descent to show only that zero blocks cannot be
eventual. The affine maps in that proof carry substantially more information.
Their slopes are precisely the raw completed-suffix multipliers, and the
renormalized phase dynamics factors out their common `3/4`. This turns the
entire product along a zero run into one telescoping phase ratio and gives the
logarithmic gap law.

The result also isolates the next real obstacle. Long zero runs themselves
are completely controlled; what remains uncontrolled is how high a nonzero
interface can reset the endpoint through its growing odd coordinate.

## Dependency audit

- `L-9833` supplies the exact zero-interface cylinder maps and canonical
  positivity.
- `L-9822` supplies the invariant phase core and the two renormalized
  multipliers; their relation to the raw slopes is checked directly.
- `L-9829` supplies the exact odd-coordinate growth and bounded Sturmian
  discrepancy used only in part 5.
- Exact cylinder concatenation supplies the composite-input construction in
  part 4 and the general interface equation used in (22).
- No empirical carry-frequency claim is used.

## Gap audit

- Positive lower density of `{i:h_i!=0}` is not proved.
- The exact zero paths in part 4 live in the scalar suffix-cylinder relation;
  they do not assert that one fixed physical prefix reaches every such
  starting endpoint.
- The logarithmic count (21) is compatible with zero lower density.
- Later forced symbols still come from the terminal-zero-renormalized phase
  system and are not proved to be repeated physical first crossings.

## Adversarial tests

- The final endpoint of a zero run need not be at least `72`; the proof uses
  the input to its last block, `Y_(i+L-1)`, which is at least `72`.
- The `30` map has the larger slope and the larger fixed point. Choosing
  `Q=3584/1631` makes it an exact fixed point and makes the `10` inequality
  point in the required direction.
- The phase ratio is strictly below `81/64` because the numerator is at most
  `81/64` while the denominator is strictly greater than `1`.
- Equation (22) includes `h_iV_i`; omitting the unbounded odd coordinate would
  create a false density conclusion.
- Part 4 proves optimality only for the zero-transition relation, not the
  existence of arbitrarily long zero gaps on the one nested physical path.

## Remaining uncertainty

Whether the unique physical carry stream has positive lower density remains
open. It would suffice to control the reachable residue classes at nonzero
interfaces strongly enough to improve (26) from linear to a uniform or
sublinear-in-index gap bound.

## Suggested next attack

Study the reset ratio `Y_(i+1)/V_(i+1)` at indices with `h_i!=0`. A uniform
exclusion of the composite zero-cylinder input residues near
`A_(z_(i+1)...z_(i+L))` could turn the logarithmic endpoint bound into a
uniform gap bound and hence positive lower density.
