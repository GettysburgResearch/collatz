# Repeated source blocks can certify successful target descent

## The result and its limit

The carry machine does not have to remain bounded relative to its source in
order to succeed. A long repeated source block fixes many binary digits of
the current target. Those digits can follow a rational Collatz orbit whose
finite multiplier contracts. The source's physical divisibility then pays
the rational orbit's additive offset, giving **strict descent of the actual
current target**, uniformly over all remaining source tails.

The main statement is a compiler with explicit inputs: a repeated source
block, its full affine constant, and one checked contractive prefix of the
associated rational target. It does not assume that every rational orbit
contracts or becomes periodic. It does not prove that every residual source
word reaches such a repeated block.

The distinction matters. For the source block `(2)`, its rational fixed
point is the ordinary integer 1. Permitting an arbitrary affine target
`A r+B` makes its rational shadow `A+B`, which ranges over arbitrary positive
integers. An unconditional claim that every such shadow has a successful
ordinary descent would incorporate the original unsolved arithmetic.

## 1. A finite rational computation controls an actual integer

Throughout, use the repository's shortcut convention

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Fix a positive odd denominator `D`. On integer numerators define

\[
R_D(h)=\begin{cases}h/2&h\text{ even},\\(3h+D)/2&h\text{ odd}.\end{cases}
\]

This describes the Collatz map on the rational number `h/D`, with parity
interpreted in the ring of rationals with odd denominator. Reduction to
lowest terms is unnecessary: cancelling an odd common factor preserves
the numerator parity.

Let `h_j=R_D^j(h)` and let `o_j` count the odd numerator inputs in those `j`
steps. If an actual integer `n` satisfies the complete binary pin

\[
Dn=2^j v+h,\qquad v\ge0,
\]

then it has precisely the same first `j` parity decisions as the rational
shadow and

\[
\boxed{D T^j(n)=3^{o_j}v+h_j.}\tag{1}
\]

This follows by induction. At one step, oddness of `D` gives
`n mod 2=h mod 2`. An even step leaves the high part `v` unchanged; an odd
step multiplies it by 3. The binary horizon loses one bit at each step.
All divisions in the proof are justified by the actual parity equation.

Consequently the exact, sufficient descent test is

\[
3^{o_j}v+h_j<2^jv+h.\tag{2}
\]

If the shadow returns to its initial numerator and `3^{o_j}<2^j`, every
positive high part `v` passes this test. A nonreturning shadow can also pass:
the coefficient saving only has to exceed its endpoint offset.

`RationalShadow.lean` formalizes (1), (2), and the returning special case.
The target is the original integer in the theorem, not an uncharged larger
intermediate carry.

## 2. Any repeated contracting source block supplies the pin

Let `V` be a nonempty positive-gap word. Write

\[
s=|V|,\quad L=\sum V,\quad a=3^s,\quad b=2^L,
\]

and retain the **full** affine numerator `C` of the source block:

\[
F_V(r)=\frac{ar+C}{b}.
\]

For gap words, the recursion is

\[
C([])=0,\qquad C(q::W)=3^{|W|}+2^q C(W).
\]

Suppose the source block contracts, so

\[
D=b-a>0,\qquad c=C/D.
\]

Here `D` is odd, and `c` is the rational fixed point of the source block.
If the supplied **actual integer source trace** starts with `V^e` and reaches
the integer `u`, then

\[
b^e(Du)+a^eC=a^e(Dr)+b^eC,\tag{3}
\]

or, as a signed identity,

\[
b^e(Du-C)=a^e(Dr-C).\tag{4}
\]

Since `a` is odd, (4) implies

\[
\boxed{2^{Le}\mid Dr-C.}\tag{5}
\]

No source tail is discarded, approximated, or replaced by a fabricated
convergence certificate in this deduction. The input is its actual finite
prefix; `u` can be any integer endpoint.

Put `H=Le`, and take enough repetitions that `2^H>C`. Since `r` is a
nonnegative integer, `Dr-C>-2^H`. The divisibility in (5) leaves exactly two
possibilities:

1. `Dr=C`: the source is the single rational fixed point, if that point is
   an integer.
2. `Dr=2^H t+C` for an integer `t≥1`.

The first is a genuine, explicit exception. Its target must be handled
separately, not declared convergent. The second gives a positive high part
of a controlled minimum size.

`RationalSourceBlock.lean` formalizes the full affine identity and this
fixed-point-or-positive-displacement alternative for arbitrary repeated
gap words. `RationalShadow.lean` separately contains the shorter
constant-gap specialization used by the concrete examples.

## 3. The general successful-descent compiler

Consider the current affine target

\[
n=A r+B,\qquad A\ge1,\ B\ge0.
\]

Its rational shadow at the source fixed point is

\[
Ac+B=\frac{h}{D},\qquad h=AC+DB.
\]

Suppose one **finite, certified** numerator prefix of length `j` has `o`
odd steps and endpoint `h_j`, with

\[
\Delta=2^j-3^o>0.\tag{6}
\]

Choose a repetition count `e` whose horizon `H=Le` satisfies

\[
H\ge j,\qquad 2^H>C,
\qquad \Delta A2^{H-j}>\max(0,h_j-h).\tag{7}
\]

Such an `e` exists whenever `L>0`, by ordinary growth of powers of 2.
This is a finite effective threshold once the rational prefix is supplied.
Outside the integer fixed-point exception, (5) yields `t≥1` and

\[
Dn=2^j\bigl(A2^{H-j}t\bigr)+h.
\]

Apply (1), with `v=A2^{H-j}t`. The actual saving is

\[
\boxed{D\bigl(n-T^j(n)\bigr)
=\Delta A2^{H-j}t+h-h_j>0.}\tag{8}
\]

Thus **every physical source beginning with `V^e` produces a strictly
descending current target**, with no restriction on its subsequent source
gaps, terminal source, or total source-word length.

The Lean interface `affine_source_shadow_descent` uses the exact pin and
exact paid inequality. Conditions (6)–(7) are the explicit written recipe
for satisfying that interface uniformly in `t`.

The composed Lean theorem `repeated_word_shadow_dispatch` starts with the
actual repeated `GapTrace`, its full block numerator, the binary horizon,
and the paid inequality for the unit displacement `t=1`. It proves that
the source is the exact integer fixed point or that the current target
strictly descends. `paid_displacement_mono` propagates the unit payment to
all `t≥1`. Finally, `repeated_word_shadow_descent` accepts a separately
certified fixed-source target and discharges the exceptional branch.

### Why an eventual positive rational cycle is enough

An explicitly certified positive rational cycle has an affine return
`x=(3^q x+K)/2^p` with `K>0`, hence `3^q<2^p`. After any finite rational
preperiod, enough repetitions of that cycle make the total prefix
multiplier smaller than 1. It therefore supplies a prefix satisfying
(6), followed by a computable threshold (7).

This is a sufficient method for constructing a certificate, not a theorem
that all rational shadows eventually enter cycles. Only the finite prefix
and its arithmetic are needed for the compiler.

## 4. Three physical carry languages

For the carry `n=9r+2`, take `A=9`, `B=2`. A constant source gap `a` has

\[
C=1,\quad D=2^a-3,\quad c=1/D,
\quad h/D=2+9/D.
\]

The following uniform conclusions are proved over arbitrary positive
integer sources and arbitrary tails of their supplied trace:

| Supplied source prefix | Rational target shadow | Target clock | Odd count | Shadow endpoint | Guaranteed conclusion |
|---|---:|---:|---:|---:|---|
| `(2,2,2)` | `11` | 5 | 3 | `10` | `T^5(9r+2)<9r+2` |
| `(3,3)` | `19/5` | 5 | 3 | `19/5` | `T^5(9r+2)<9r+2` |
| `48` copies of `4` | `35/13` | 192 | 121 | `131/13` | `T^192(9r+2)<9r+2` |

For `(2,2,2)`, the fixed source `r=1` is treated separately by the exact
computation `T^5(11)=10`. All other sources have `r=64t+1`, `t≥1`.
For `(3,3)`, `5r=64t+1`, with `t≥1`. For `48` copies of gap 4,
`13r=2^192 t+1`, also with `t≥1`.

The last case has an exact rational preperiod of 6 clocks followed by a
24-clock cycle with 15 odd steps. A contractive total prefix has
192 clocks and 121 odd steps. Its integer inequality is

\[
9(2^{192}-3^{121})>131-35=96.
\]

The coefficient difference is

\[
2^{192}-3^{121}
=886070835643387132596249934678851296907928561850481193693.
\]

These are infinite source families, not a verification of finitely many
integer starting values. The finite computation concerns only the
rational shadow certificate; the lift to every physical source is a
symbolic theorem.

## 5. Relation to the refreshed repository

PR183's `CARRY_COMPRESSION_BRIDGE.md` already identifies the source fixed
point `1/5`, the target cycle `19/5`, and the distinction between growing
relative ternary carry and shrinking actual target. Its direct ordinary
residue-class descent is also already proved. The gap-3 example above
should not be presented as discovery of that rational cycle or of that
descent. The extension here is the arbitrary-denominator physical lift,
the general full-source-block pin, and the successful-descent compiler.

PR176's `SOURCE_TARGET_INDUCTION.md` already supplies the joint induction
that can consume these strict descents. The outer rank is the supplied
source grade. The inner rank is the current target integer. A descent
`T^j(n)<n` may reuse the same supplied source certificate and its unchanged
outer grade. Our compiler supplies precisely that kind of inner-rank
decrease.

If this compiler is invoked only after transporting the target to some
larger intermediate carry `m`, descent below `m` alone does **not** prove a
decrease below the original target `n`. Such an application needs either
an explicitly paid lower-grade recursive query at `m`, or a composed
inequality showing that the endpoint is below the original `n`. The
statements here keep that obligation visible.

The compiler complements PR185's arbitrary-gap negative-carry law and
finite even-budget theorem. That law gives an exact evolving carry state;
the compiler offers a way to certify a successful exit even when the
relative carry state does not remain bounded.

## 6. The attempted all-gap generalization

For every constant gap `a≥2`, the rational source fixed point is
`1/(2^a-3)`, and the target numerator starts at

\[
h_0=2^{a+1}+3,\qquad D=2^a-3.
\]

Its first `a` numerator steps are odd and satisfy the exact formula

\[
h_j=3^{j+1}2^{a-j}-D\qquad(0\le j\le a).
\]

In particular,

\[
h_a=3^{a+1}-2^a+3.
\]

For even `a≥4`, this has exactly one factor of 2; for odd `a≥3`, exactly
two factors of 2. Thus the immediate even run does not repay the initial
odd-run multiplier for even `a≥4` or odd `a≥5`. Proving a contractive
prefix for **all** `a` requires control of the later rational orbit, beyond
this first binary run. No such all-`a` theorem is claimed here.

More generally, arbitrary source words may change blocks indefinitely.
The new theorem removes the source-tail restriction once its finite
repetition guard and rational prefix certificate hold. It does not prove
that every arbitrary word satisfies one of those guards, and does not
turn a finite block dictionary into universal coverage.

## Proof-status boundary

The Lean files check finite rational computations, the physical ordinary
target lift, source affine identities, source divisibility, and the stated
descent corollaries, including the composed arbitrary-word dispatcher. The
generic effective threshold existence argument and the
positive-cycle sufficient criterion are proved in the text above. They
are not imported as new axioms. No convergence assumption is made for
terminal complements such as `3^p-c`, and no Collatz closure theorem is
asserted.
