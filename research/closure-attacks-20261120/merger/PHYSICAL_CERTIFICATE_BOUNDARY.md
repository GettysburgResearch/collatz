# Physical five-pair returns, carry transport, and the first missing step

**Status: PROPOSED unconditional elementary statements and one REFUTED
descent rule.** These calculations concern actual positive ordinary paths.
They do not prove every required merger, and do not turn a failure of one
method into evidence against Collatz.

Use the shortcut map `T` and write

\[
H(x):\quad x\sim5x.
\]

By [M5-001](SINGLE_MULTIPLIER.md), proving `H(x)` for every positive odd
ternary unit would settle Collatz. This is now the only multiplicative
query needed; no `5*3^i` query family has to be solved separately.
PR157's stronger forward-five basin criterion already uses this same
slice; the companion M5-001 proof is an independent short reconstruction
of its symmetric corollary.

## PC-001. Fixed words cannot supply a positive affine family

For a parity word `w` of length `r` with `a` odd letters, write

\[
T_w(z)=\frac{3^a z+C_w}{2^r},\qquad 0\le C_w\le3^r-2^r.
\]

The bound on `C_w` follows by induction: an even letter keeps the numerator
constant, and an odd letter sends it to `3C_w+2^r`. Equality is attained
by the all-odd word.

For fixed words `w,v`, a merger of `x` and `5x` would give

\[
\frac{3^a x+C_w}{2^r}
 =\frac{5\cdot3^b x+C_v}{2^s}.                     \tag{1}
\]

Its coefficient of `x` is nonzero: equality of slopes would require a
product of powers of 2 and 3 to have a factor 5. Thus (1) has at most one
rational solution `x`. In particular no one fixed pair of words proves
`H(x)` on two distinct positive inputs, let alone on a whole residue class.
The same argument applies to any finite ordinary undirected path after
reducing it to a forward-then-backward merger certificate.

This fixed-word obstruction is already present in **PR154**, full SHA
`fe40bb6f88e8094290ef01207d9bf7c4798d35d0`,
`research/structural-reset-20261120/component/PROOF.md`, last paragraph of
“What remains open”. The following explicit clock consequence is included
to clarify its quantitative meaning, without a novelty claim.

**Clock consequence.** If positive `x` and `5x` meet with both clocks at
most `K`, then

\[
x<3^K.                                             \tag{2}
\]

To prove this, suppose for example `r>=s`. Cancel the common power `2^s`
in (1). The denominator in the resulting expression for `x` is a nonzero
integer, whereas the absolute numerator is

\[
|2^{r-s}C_v-C_w|
 \le\max(2^{r-s}C_v,C_w)<3^r\le3^K.
\]

The case `s>=r` is identical, with numerator
`|2^{s-r}C_w-C_v|`. It has the same bound. Thus every universal construction
must use unbounded physical words. This does not prevent a finite program
from generating input-dependent words.

## PC-002. A first same-clock physical return can increase the odd query

For every integer `u>=0`, put

\[
x=5712553+12582912u,\qquad
y=39085825+86093442u.
\]

Both are positive odd ternary units, and `y>x`. There are exact ordinary
paths

\[
T^{21}(x)=y,\qquad T^{21}(5x)=5y.                 \tag{3}
\]

The successive parity words are

```
from x:   101111111111111000010
from 5x:  100100111111111011101
```

Both have 15 odd letters. Their affine constants are respectively
`24340829` and `121704145=5*24340829`. Every `x` above is
`1518249 (mod 2^21)`, so both words are legal on the entire displayed
progression. Equivalently, this is the exact query return

\[
y=R(x)=\frac{14348907x+24340829}{2097152},\qquad
H(x)\Longleftrightarrow H(y).                      \tag{4}
\]

The implication in either direction uses only transport within each
ordinary component. It does not assume `H(x)` or `H(y)`.

This is the **first positive same-clock numerical return to the ratio five**
on this whole progression. At clocks 1 and 2 the difference
`T^j(5x)-5T^j(x)` is `-2,-1`. At clocks 3 through 18, and at clock 20,
that affine function of `u` has both coefficients strictly negative.
At clock 19 it is `1`. At clock 21 it is zero. The companion checker
reconstructs every coefficient using the actual branches, so this first
same-clock return assertion covers every `u>=0` rather than a sample.
It also checks `T^j(x)-5T^j(5x)`: its coefficients have the same sign and
its constant is nonzero throughout clocks 1 through 21. Thus there is no
earlier same-clock ratio-five return in the opposite orientation either.

Since both endpoints in (3) are odd, passing to odd parts does not rescue
numeric descent. For instance the base input `5712553` first returns at
the larger odd parameter `39085825`. Therefore the proposed rule

> Follow the two physical arms at the same clock until their first
> ratio-five return; that return always gives a smaller odd query.

is **REFUTED**. Both same-clock orientations were checked, and at the
displayed return neither parameter has a power of two to remove. This does
not exclude other independent-clock returns or earlier comparisons after
separately stripping powers of two from the two arms.

There is also a useful constructive direction: (3) is an exact strict
reduction of `H(y)` to `H(x)` on the displayed ternary progression. This
is a physically valid branch of a query selector, not a complete cover.

## PC-003. Repeating this expanding return is well-founded

One expanding return does not itself force indefinite expansion. Define

\[
A=14348907=3^{15},\quad B=2097152=2^{21},\quad
C=24340829,\quad D=A-B=12251755>0.
\]

If a positive integer `z` takes this same legal return word, so that
`R(z)=(Az+C)/B` is an integer, then

\[
D R(z)+C=\frac{A}{B}(Dz+C).                       \tag{5}
\]

The integer `Dz+C` is strictly positive. Because `A` is odd, (5) gives

\[
v_2(DR(z)+C)=v_2(Dz+C)-21.                        \tag{6}
\]

Consequently a fixed positive input permits at most

\[
\left\lfloor\frac{v_2(Dz+C)}{21}\right\rfloor
\]

consecutive uses of this word. In fact integrality of each iterate is
equivalent to having the required residue for the return word, since its
slope numerator is odd; thus the valuation counts the maximal consecutive
run exactly. Every value in such a run is positive and increases, but the
valuation rank decreases. This is an unconditional example of the kind of
non-height rank that variable-clock surgery can use.

The same proof works for any one fixed expanding affine return
`R(z)=(az+c)/2^h` with `a` odd, `a>2^h`, `c>0`: use
`v_2((a-2^h)z+c)`. It does **not** provide one rank for arbitrary switching
among different return words. Their affine centers differ. Nor does it
prove that a fixed source must ever have a return before its arms meet.
Those are separate unresolved obligations.

## PC-004. A multiplicative semigroup certificate leaves a carry obligation

Applegate and Lagarias' primary paper proves the weak multiplicative
semigroup theorem and supplies the following certificate for 5 in its
wild semigroup:

\[
5=\frac14\left(\frac{11}{7}\right)^2
 \frac{17}{11}\frac{26}{17}\frac{83}{55}
 \frac{98}{65}\frac{125}{83}.
\]

Source: [*The 3x+1 Semigroup*, arXiv:math/0411140v2, Theorem 1.1 and
Table 3](https://arxiv.org/pdf/math/0411140v2). The authors explicitly
distinguish products of generators from actual Collatz iteration. No part
of their proof is imported as ordinary multiplicative invariance here.

For an odd positive cofactor `m`, the ordinary generator
`2k+1 -> 3k+2` scales as

\[
T\bigl(m(2k+1)\bigr)
  =m(3k+2)-\frac{m-1}{2}.                          \tag{7}
\]

Thus multiplying an ordinary edge by `m` leaves a nonzero additive carry
unless `m=1`. For the first ratio `11/7`, the unproved correction would be
the actual merger of `11m-(m-1)/2` with `11m`. A finite product identity
does not supply these correction mergers or order them by a common
well-founded physical rank. Formula (7) identifies the exact missing
operation in this attempted semigroup-to-merger compiler. The fixed-word
obstruction in PC-001 also forbids compiling it into one finite list of
ordinary affine certificates covering a progression of cofactors.

## Remaining physical task

The single-slice theorem removes the old need to control a separately
indexed unbounded family of powers of three. The actual query `H(x)` is
still unproved for general ordinary odd ternary units. A complete procedure
needs a well-founded rule handling physical query transport, return-word
switching, and sources whose two arms do not return to the selected section.
PC-003 settles repetition of one expanding word only; it is not that
complete rule. PC-004 exposes, but does not discharge, the additive carries.

Latest sources inspected separately were **PR146**
`6863d298187af8b2619efbf78cc4b0aa8e627393`,
`research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md`, and **PR156**
`c5cb84502c7289705d59a8781a65fd845b9b6b14`,
`research/global-rigidity-20261120/Q_SECTION_GUARDS.md`, QG1--QG4. Their
ordinary guards and orientation qualifications are preserved; the pair
in (3) is specifically the homogeneous factor-five pair, not the Q-section
transducer from PR156.

After this argument was written, the newer **PR157** head
`64361ecca770092d6c8242dc6211e38818af2e50` was fetched and inspected.
`research/global-closure-20261120/merger.md`, GCM-001--002, already proves
the stronger directed five criterion.
`research/global-closure-20261120/closing-attempts.md`, GCL-001--002,
already records shifted-power growth from supplied convergent antecedents,
an obstruction to a uniform inverse-lift compiler, and the semigroup
boundary. PC-002 instead supplies a homogeneous **same-clock query return**
whose two odd parameters increase; it is a distinct physical example, not
a claim to have discovered the general difficulty with fixed words.
