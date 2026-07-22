# L-9840 — Finite-suffix zero-descent no-go theorem

Claim ID: `L-9840`  
Title: A finite H suffix architecture with uniformly descending zero interfaces cannot contain an ordinary nonnegative nested seed  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: exact H cylinder concatenation; the nested-cylinder stabilization principle of `L-9801`  
Scope: arbitrary finite families of nonempty exact H suffix words  
Related counterexample candidates: none

## Definitions

Let `F` be a finite family of nonempty exact H words. For each suffix
`z in F`, write its normalized affine and canonical data as

\[
f_z(x)=\frac{V_zx+B_z}{U_z},
\qquad
0\le A_z<U_z,
\qquad
0<Y_z<V_z,
\qquad
Y_z=f_z(A_z).
\tag{1}
\]

Here `U_z` is a positive power of two, `V_z` is odd, and nonemptiness gives
`U_z>=2` and `B_z>0`.

Fix an infinite schedule

\[
z_0,z_1,z_2,\ldots\in\mathcal F
\tag{2}
\]

and a fixed exact prefix `w_0`. Form the nested words

\[
w_n=w_0z_0z_1\cdots z_{n-1},
\tag{3}
\]

with canonical data `(U_n,V_n,A_n,Y_n)`. At the interface `w_n|z_n`, let
`h_n,j_n` be the exact carries. Thus

\[
\boxed{
Y_n+h_nV_n=A_{z_n}+j_nU_{z_n},
\qquad
0\le h_n<U_{z_n},
\qquad
0\le j_n<V_n,
}
\tag{4}
\]

and exact concatenation gives

\[
\boxed{
\begin{aligned}
U_{n+1}&=U_nU_{z_n},
&V_{n+1}&=V_nV_{z_n},\\
A_{n+1}&=A_n+h_nU_n,
&Y_{n+1}&=Y_{z_n}+j_nV_{z_n}.
\end{aligned}
}
\tag{5}
\]

For a suffix `z`, define its zero-interface displacement polynomial

\[
\boxed{
\delta_z(j)
=(A_z-Y_z)+j(U_z-V_z)
\qquad(j\in\mathbb Z_{\ge0}).
}
\tag{6}
\]

## Statement

### 1. Exact zero-interface displacement

If `h_n=0` and `z_n=z`, then

\[
\boxed{
Y_n=A_z+j_nU_z,
\qquad
Y_{n+1}=Y_z+j_nV_z,
}
\tag{7}
\]

and consequently

\[
\boxed{
Y_n-Y_{n+1}=\delta_z(j_n).
}
\tag{8}
\]

Thus the sign of every zero-interface endpoint change is determined entirely
by the four canonical integers `(U_z,V_z,A_z,Y_z)` and the ordinary quotient
`j_n`.

### 2. Exact robust-descent criterion

For one suffix `z`, the following are equivalent:

1. Every zero-interface instance strictly decreases the endpoint:

   \[
   \delta_z(j)>0
   \qquad\text{for every }j\in\mathbb Z_{\ge0}.
   \tag{9}
   \]

2. Its multiplier and canonical displacement satisfy

   \[
   \boxed{
   U_z\ge V_z
   \qquad\text{and}\qquad
   A_z>Y_z.
   }
   \tag{10}
   \]

Call a suffix satisfying (10) **zero-descending**. This is an exact finite-data
test, not merely a sufficient estimate.

### 3. Finite-family no-go theorem

Assume every suffix in `F` is zero-descending. Equivalently,

\[
\boxed{
U_z\ge V_z
\quad\text{and}\quad
A_z>Y_z
\qquad(z\in\mathcal F).
}
\tag{11}
\]

Then for every infinite schedule (2), the interface blocks are not eventually
zero:

\[
\boxed{
h_n\ne0
\quad\text{for infinitely many }n.
}
\tag{12}
\]

The compatible canonical inputs have a unique 2-adic limit

\[
\boxed{
A_\infty
=A_0
+U_0\sum_{n\ge0}
h_n\prod_{r=0}^{n-1}U_{z_r}
\in\mathbb Z_2,
}
\tag{13}
\]

and this limit is not an ordinary nonnegative integer:

\[
\boxed{
A_\infty\notin\mathbb Z_{\ge0}.
}
\tag{14}
\]

The same conclusion holds if (11) is true only for every suffix used after
some finite stage. A finite exceptional prefix cannot repair the no-go.

### 4. Uniform finite-family descent

Because `F` is finite, under (11) the positive integer

\[
\boxed{
\eta_\mathcal F
=\min_{z\in\mathcal F}(A_z-Y_z)
\ge1
}
\tag{15}
\]

is well defined. Every zero-interface stage satisfies

\[
\boxed{
Y_n-Y_{n+1}\ge\eta_\mathcal F.
}
\tag{16}
\]

Hence a run of `L` zero interfaces beginning at endpoint `Y_s>0` obeys the
general deterministic bound

\[
\boxed{
L\le
\left\lfloor\frac{Y_s-1}{\eta_\mathcal F}\right\rfloor.
}
\tag{17}
\]

No phase dynamics or special suffix constants are needed for this bound.

### 5. Complementary suffix-design rule

For each suffix define its non-descent quotient set

\[
\mathcal N_z
=\{j\in\mathbb Z_{\ge0}:\delta_z(j)\le0\}.
\tag{18}
\]

Writing

\[
d_z=U_z-V_z,
\qquad
\Delta_z=A_z-Y_z,
\tag{19}
\]

this set is exactly

\[
\boxed{
\mathcal N_z=
\begin{cases}
\varnothing,
&d_z>0,\ \Delta_z>0,\\[1mm]
\left\{0,\ldots,
\left\lfloor\dfrac{-\Delta_z}{d_z}\right\rfloor
\right\},
&d_z>0,\ \Delta_z\le0,\\[3mm]
\varnothing,
&d_z=0,\ \Delta_z>0,\\[1mm]
\mathbb Z_{\ge0},
&d_z=0,\ \Delta_z\le0,\\[1mm]
\left\{
j\ge
\max\!\left(0,
\left\lceil\dfrac{\Delta_z}{-d_z}\right\rceil
\right)
\right\},
&d_z<0.
\end{cases}
}
\tag{20}
\]

Suppose some future suffix architecture is intended to admit an ordinary
nonnegative point in its infinite nested intersection. Then its eventual
zero-interface tail must satisfy

\[
\boxed{
j_n\in\mathcal N_{z_n}
\quad\text{for infinitely many }n.
}
\tag{21}
\]

In particular, the architecture must use infinitely often a suffix which
violates at least one half of the robust criterion:

\[
\boxed{
U_z<V_z
\qquad\text{or}\qquad
A_z\le Y_z.
}
\tag{22}
\]

This is the complementary design rule. Merely adding such a suffix to the
alphabet is not enough: the eventual schedule must reach it infinitely often
at quotients in the explicit set (20). Otherwise strict endpoint descent
returns and the ordinary-seed no-go still applies.

### 6. Interpretation boundary

The theorem concerns nested exact H cylinders and their canonical inputs. It
does not assert that an arbitrary symbolic suffix schedule represents
repeated physical first crossings of one Collatz orbit. Conversely, (22) is
only a necessary design condition for an architecture which hopes to retain
an ordinary seed; it is not a construction of such a seed.

## Proof

If `h_n=0`, equation (4) becomes

\[
Y_n=A_z+j_nU_z.
\]

Since `Y_n>=0` and `0<=A_z<U_z`, its quotient is nonnegative. The endpoint
formula in (5) gives the second identity in (7), and subtraction proves (8).

Now `delta_z(j)` is affine in `j`. If `U_z-V_z>=0`, its minimum on the
nonnegative integers occurs at `j=0`, so it is strictly positive everywhere
exactly when `A_z-Y_z>0`. If `U_z-V_z<0`, it tends to minus infinity and
cannot be strictly positive for every `j`. This proves the equivalence
(9)--(10).

Iterating the input identities in (5) gives

\[
\begin{aligned}
U_n
&=U_0\prod_{r=0}^{n-1}U_{z_r},\\
A_n
&=A_0
+U_0\sum_{r=0}^{n-1}
h_r\prod_{s=0}^{r-1}U_{z_s}.
\end{aligned}
\tag{23}
\]

Every suffix is nonempty, so its power-of-two denominator is at least two.
Thus `U_n` tends to infinity, the canonical residues satisfy

\[
A_{n+1}\equiv A_n\pmod{U_n},
\qquad
0\le A_n<U_n,
\tag{24}
\]

and they define the 2-adic limit (13).

The limit is an ordinary nonnegative integer if and only if the blocks `h_n`
are eventually zero. Indeed, eventual zero blocks make (5) stabilize `A_n`.
Conversely, if (A_\infty=N\ge0), then once (U_n>N), the canonical residue of
`N` modulo `U_n` is `N` itself. Hence `A_n=N` thereafter, and (5) forces all
later `h_n=0`.

Assume for contradiction that this happens under (11). After the first
nonempty appended word, every endpoint is a positive integer because its
affine additive numerator is positive. Equations (8), (10), and (11) then
give an infinite strictly descending sequence of positive integers. This is
impossible, proving (12)--(14). The same proof starts after any finite
exceptional prefix.

Under (11), equation (6) gives

\[
\delta_z(j)
\ge A_z-Y_z
\ge\eta_\mathcal F.
\]

Summing over a zero run proves (16), while positivity of its final endpoint
gives

\[
1\le Y_{s+L}
\le Y_s-L\eta_\mathcal F,
\]

which is (17).

Solving the one affine inequality

\[
\Delta_z+jd_z\le0,
\qquad j\in\mathbb Z_{\ge0},
\]

in the three cases `d_z>0`, `d_z=0`, and `d_z<0` gives (20).

Finally, suppose an ordinary nonnegative nested seed exists. Its input blocks
are eventually zero by the stabilization argument. If (21) failed, then
`delta_(z_n)(j_n)>0` at every sufficiently late stage, again producing an
infinite strict descent of positive integral endpoints. Thus (21) is
necessary. The set `N_z` is empty exactly when (10) holds, so (22) follows.
This completes the proof. ∎

## Motivation

The special `10/30` argument in `L-9833` uses two explicit endpoint maps.
Their decisive feature is not their numerical size: both suffixes have a
nonexpanding multiplier numerator and a strictly positive canonical input
displacement. Formula (6) isolates exactly that invariant feature for every
exact H suffix.

The resulting theorem is a reusable architecture test. A finite proposed
suffix compiler can be rejected by checking two integer inequalities per
suffix. The complementary table also says precisely what kind of suffix and
which quotient regime a successful replacement must reach.

## Dependency audit

- Only the exact H concatenation identities (4)--(5) and canonical ranges are
  used.
- The nested-cylinder stabilization principle of `L-9801` is reproved in the
  needed variable-radix form.
- Finiteness is used for the uniform constant `eta_F`; the qualitative no-go
  needs only that every eventual suffix pass (10) and that denominators tend
  to infinity.
- No `10/30` constants, phase rotation, empirical carry signs, or density
  assumptions occur.

## Gap audit

- Violating (10) is necessary, not sufficient, for retaining an ordinary
  nested seed.
- A non-descent-capable suffix used only finitely often cannot help.
- Even when such a suffix recurs, its actual quotient must lie in (20)
  infinitely often.
- The theorem does not classify a nonordinary 2-adic limit as irrational,
  transcendental, or nonrational.

## Adversarial tests

- If `U_z<V_z` but `A_z>Y_z`, small quotients may still decrease; only the
  sufficiently large quotient tail in (20) avoids descent.
- If `U_z>V_z` but `A_z<=Y_z`, only finitely many small quotients may avoid
  descent; using the suffix at large quotients does not evade the theorem.
- Equality `A_z=Y_z` permits a stationary endpoint at `j=0`, so strict
  descent genuinely requires `A_z>Y_z`.
- Equality `U_z=V_z` is included for algebraic completeness, although a
  nonempty exact H word cannot normally equate a positive power of two with
  an odd power of three.
- Positivity, integrality, and eventual zero blocks are all essential. An
  infinite strictly decreasing real sequence would not give the contradiction.

## Remaining uncertainty

The theorem identifies the necessary escape hatch but does not construct a
finite suffix family whose reachable quotient dynamics uses that escape hatch
infinitely often while satisfying the other H and Collatz constraints.

## Suggested next attack

Search for exact H suffixes violating (10), then determine their reachable
quotient sets rather than merely their formal sets (20). A viable architecture
must force visits to those non-descent quotient ranges infinitely often while
preserving the intended multiplier-return or first-crossing semantics.
