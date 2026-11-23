# Higher-digit tail interpolation and its exact candidate lattice

**Date:** 2026-11-23. **Status:** exact written constructions and lattice
classification; no universal successful witness construction. This is a
separate extension of the frozen `SOURCE_AWARE_TRIADIC_CONSTRUCTION.md`
and does not alter that note or its Lean receipt.

The earlier reset theorem applies to rules local modulo three, including
polynomials in `Z[X]` calibrated by `h(1)=2`, `h(2)=1`. The following
construction leaves that class and really can remove the reset. The
question is whether it also creates a small enough successful witness.

Put `R=Z[1/3]`. Keep one actual prefix of the shortcut orbit of `n>0`:

\[
x=T^K(n),\quad U=2^K,\quad p=p_K,\quad b=b_K,
\qquad Ux=3^p n+C,
\]

with the unchanged complementary carry `D=D_K`. A terminal value `z`
pulls back to

\[
                         I_K(z)=(Uz-D)/3^b.                \tag{1}
\]

Throughout the interpolation construction assume `x>2`. The two terminal
core states are separately calibrated and require no interpolation.

## 1. A higher-digit polynomial really removes a reset

Consider

\[
H(X)=3-X+\frac{(X-1)(X-2)(X-3)}3.                         \tag{2}
\]

It lies in `R[X]`, takes integer values at every integer, and is calibrated
at one and two. Its correction is even: a product of three consecutive
integers is divisible by six. Thus `H(t)` has parity opposite to `t` for
every integer. Its residue modulo three can depend on a higher base-three
digit; it need not satisfy the earlier local rule `H(t)=-t mod 3`.

For the actual source `n=6`, the prefix is

\[
                           6\to3\to5\to8,
\]

with word `011`, `K=3`, `p=2`, `b=1`, `C=10`, `D=1`.
The reflection has value `3-8=-5`, giving numerator `-41`, a unit at
three. In contrast, `H(8)=65`, giving numerator

\[
                       8\cdot65-1=519=3\cdot173.
\]

The initial candidate is the integer `173`. It matches the three prefix
bits and the terminal complementary parity. This is a real removal of
the denominator reset, without changing the ordinary source.

## 2. The complete value lattice for calibrated triadic-coefficient polynomials

For a fixed integer `x>2`, set

\[
G=(x-1)(x-2),\quad t=v_3(G),\quad g=G/3^t.
\]

Thus `g` is a positive even integer coprime to three. Every `h in R[X]`
with `h(1)=2`, `h(2)=1` has the exact factorization

\[
h(X)=3-X+(X-1)(X-2)q(X),\qquad q\in R[X].                \tag{3}
\]

Conversely, any expression (3) is calibrated. Evaluating (3) gives the
complete value set

\[
\boxed{\{h(x):h\in R[X],\ h(1)=2,\ h(2)=1\}
                       =3-x+gR.}                         \tag{4}
\]

The reverse inclusion in (4) already uses constant `q`, so degree two
suffices. Moreover, every such polynomial has opposite parity at all
integer inputs: reduction modulo two is defined for every coefficient
in `R`, and its calibrated values determine the two residue classes.

### Requiring integer outputs everywhere does not shrink the integer part

The integer values in (4) are `3-x+gZ`. Every one of them is attained even
if `h` is additionally required to take integer values at **every**
integer. Here is an explicit construction.

Choose `j>=1` so that `d=3^j<=x<3d`, and put

\[
v=(d-1)/2=v_3(d!),\qquad
B_j(X)=\frac{X(X-1)\cdots(X-d+1)}{3^v}.
\]

The integer `F=d!/3^v` is coprime to three and even, and
`B_j(X)=F binom(X,d)`. Thus `B_j` belongs to `R[X]`, takes even integer
values on all integers, and vanishes at one and two. The same statements
for negative integer inputs follow from
`binom(-m,d)=(-1)^d binom(m+d-1,d)`.

Writing `x=qd+s` with `q` equal to one or two and `0<=s<d`, reduction of
`(1+Z)^x` modulo three gives

\[
(1+Z)^x\equiv(1+Z^d)^q(1+Z)^s\pmod3.
\]

Its coefficient of `Z^d` shows `binom(x,d)=q mod3`. Hence `B_j(x)` is a
unit at three. Because it has the factors `X-1` and `X-2` and only powers
of three in its denominator, `g` divides `B_j(x)`. Consequently

\[
                         \gcd(G,B_j(x))=g.
\]

Choose ordinary Bezout coefficients `u,v_0` with
`uG+v_0 B_j(x)=g`, and define

\[
P_x(X)=u(X-1)(X-2)+v_0 B_j(X).
\]

Then `P_x(1)=P_x(2)=0`, `P_x(x)=g`, and `P_x` takes even integer values
everywhere. The polynomials `3-X+cP_x(X)`, `c in Z`, realize exactly
`3-x+gZ`. The potentially large degree and Bezout coefficients are not
being presented as small-height data.

## 3. Exact fixed-denominator candidates: a stricter residue lattice

Suppose the proposed initial witness is `a/3^r`, with `a in Z`, `r>=0`.
Equation (1) forces its terminal value to be

\[
z=\frac{3^b a+3^rD}{2^K3^r}.
\]

By (4), this terminal value is supplied by a calibrated polynomial in
`R[X]` **if and only if**

\[
\boxed{
2^K g\mid 3^b a+3^rD-2^K3^r(3-x).
}                                                        \tag{5}
\]

Indeed, after subtracting `3-x`, membership in `gR` is exactly the
displayed divisibility, since `2^K g` is coprime to three. The same
divisibility automatically cancels all powers of two in the terminal
denominator, so the terminal point lies in `R` and is legal. Conversely,
the constant choice `q=(z-(3-x))/G` in (3) belongs to `R` whenever (5)
holds.

Since `3^b` is invertible modulo `2^K g`, (5) gives exactly one residue
class of initial numerators modulo `2^K g`. Increasing polynomial degree
does not enlarge this class. For integer initial candidates (`r=0`), the
integer-valued construction of Section 2 attains every member of it.

This gives a positive construction: because `g` is a unit at three,
one can always choose `h(x)=3-x+gc` so that `2^Kh(x)-D` is divisible by
the whole `3^b`. But the resulting integer numerator belongs to a lattice
of spacing `2^K g`. It need not be small. Centering gives only the generic
bound `|a|<=2^(K-1)g`; it does not give the exponentially smaller numerator
required by the triadic stopping horizon.

The restriction is also arithmetic, not just a degree cost. For example,
the known value `Omega(8)=-1/9` differs from `3-8` by `44/9`, which is not
in `14R`. Thus **no** polynomial in `R[X]` calibrated at one and two can
take the exact value `Omega(8)` at eight. Allowing its coefficients to
depend on eight does not remove that obstruction. This concerns the
coefficient ring of the interpolating polynomial, not triadicity of its
desired value.

## 4. Full integer-valued interpolation exactly recovers the original lattice

The Newton/Mahler basis permits the larger class of rational-coefficient
polynomials that take values in `R` at every integer. This class is not
the same as `R[X]`: binomial polynomials can have primes other than three
in their monomial coefficients while still taking integer values.

For **any** terminal `z in R` with parity opposite to the fixed `x>2`,
the explicit polynomial

\[
\boxed{
J_{x,z}(X)=3-X+\bigl(z-(3-x)\bigr)\binom Xx
}                                                        \tag{6}
\]

takes values in `R` on every integer, is calibrated at one and two, and
has `J_(x,z)(x)=z`. Its correction coefficient belongs to `2R`, so its
parity is opposite to its integer argument everywhere.

Therefore this larger calibrated polynomial class produces **exactly
all** initial triadic candidates that pass the actual first `K` parity
tests and the terminal test. If `e=x mod2`, these candidates satisfy

\[
3^b a+3^rD\equiv2^K(1-e)\pmod{2^{K+1}}.                 \tag{7}
\]

To check (7), first divide its numerator by `2^K`: its remaining parity
is the parity of `z`, since `3^r` is odd. Conversely, (7) constructs a
triadic terminal `z` of the required parity, and (6) supplies the global
polynomial wrapper. Thus the new freedom exactly recovers the ordinary
fixed-denominator complementary-residue lattice at one extra test.
It does not impose a stronger condition favorable to small numerators.

## 5. The same source control, including the actual height cost

Return to `n=6`, `K=3`, `x=8`. Here `g=14`. Calibrated polynomials in
`R[X]` can give integer initial candidates exactly in the class

\[
                            a=61\pmod{112}.
\]

The centered member is `-51`. It is attained by

\[
h_*(X)=3-X-\frac{(X-1)(X-2)(9-X)}3,
\]

which takes integer values everywhere; the cubic correction is divisible
by three for every integer input. It gives `h_*(8)=-19` and
`(8(-19)-1)/3=-51`.

In the full integer-valued class (6), the initial class is instead
`a=13 mod16`, whose centered member is `-3`. Its terminal value is `-1`,
and the polynomial `3-X+4 binom(X,8)` realizes it.

The existing amortized horizon is

\[
H=9\operatorname{bl}\bigl(n\max(1,|a|)F(r)\bigr)+1,
\qquad F(0)=1.
\]

All three constructions cancel the entire denominator, but their own
horizons are:

| Construction | Terminal value at 8 | Initial integer `a` | Required horizon `H` |
|---|---:|---:|---:|
| Higher-digit cubic (2) | 65 | 173 | 100 |
| Centered calibrated `R[X]` candidate | -19 | -51 | 82 |
| Centered full integer-valued candidate | -1 | -3 | 46 |

Each exceeds the available clock three. These are exact values from one
unchanged ordinary prefix, not a search census or evidence against later
success for the source.

## 6. Outcome

Higher base-three digits can genuinely cancel denominators that every
local-modulo-three rule leaves intact. The complete triadic-coefficient
polynomial construction, however, gives the stricter lattice (5), with
an additional factor `g`. The full integer-valued Newton construction
removes that factor but is exactly equivalent to the original candidate
lattice (7).

Neither construction supplies a new bound on its smallest residue. In
(6), writing down the polynomial after choosing `z` merely represents
the selected candidate; it does not choose a small one. The unanswered
construction question therefore remains the odd-coefficient closure in
the frozen note, or a new source-dependent estimate on the actual
smallest residue. No further bounded enumeration was used to replace
that step.

All statements in this extension have written-proof scope. The frozen
Lean module and receipt do not formalize this interpolation theorem.
