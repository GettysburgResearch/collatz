# A physical five compiler with arbitrarily long valuation-one runs

**PROPOSED elementary results. The universal five-closure implication, and
Collatz, remain OPEN.** The new mechanism enters the nonzero affine state
`(y,5y+4)`, carries that state through an arbitrarily long run, and exits
back to an ordinary proportional pair. This proves a new unbounded
certificate language. A second short block supplies the additional domain
used by the energy note in this packet.

Throughout, `T(n)=n/2` on even positive integers and `(3n+1)/2` on odd
positive integers. Its odd acceleration is

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

An exponent word `(a_1,...,a_p)` means an **actual** positive odd path,
with every `a_i` its exact valuation. Its shortcut clock is the sum of
its letters. Write `I_a(q)=(2^a q-1)/3` only when this is a positive odd
integer. A first-hit certificate ends at the first occurrence of 1.

## What is inherited, and what is added

[PR157, GCM-002](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md)
already proves that `x in C => 5x in C` for every positive odd ternary
unit `x` would imply Collatz. That implication is the open target, not a
premise below.

[PR166, FL1--FL4](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md)
already constructs the valuation-two ladder and its block compiler. The
same file explicitly describes signed rational denominator clearing for
five. [PR146's bounded-rank note](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md)
gives the broader signed-template and grade framework. We do not claim
that architecture, block concatenation, or the five-closure criterion as
new. [PR146's latest five note](https://github.com/GettysburgResearch/collatz/blob/fd991063721e9c157d318e40bb20131762f7d750/research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md)
also proves that one suitable proportional-return cylinder can carry every
supplied five comparison, and explains why lifting into a covered cylinder
does not itself prove closure.

The additions here are the explicit carry-four entry and exit, their
arbitrary valuation-one repetition, an explicit ordinary unit realization
at every resulting odd rank, and the separate `(1,1,1,b)` block. These
specific identities were not located in the pinned sources above; no
broader priority claim is made.

## CF1. A short block outside the valuation-two cylinders

Suppose `x` has a legal prefix `(1,1,1,b)`, where `b>=6`, ending at `q`.
Then `5x` has the legal prefix

\[
 (1,2,5,b-5),
\]

ending at `5q`, at the same shortcut clock `b+3`. Equivalently,

\[
 \boxed{5 I_1^3 I_b(q)=I_1 I_2 I_5 I_{b-5}(5q).}             \tag{1}
\]

The source affine correction is `65`, and the target correction is

\[
 27+18+24+256=325=5\cdot65.
\]

Both words have four odd inputs. Consequently their inverse numerators
are respectively `2^(b+3)q-65` and five times that integer.
Full divisibility by `3^4` implies every successive inverse division is
integral: reduce the numerator modulo three to check the innermost
inverse, divide, and repeat. Every exponent is positive. An integral
inverse of a positive odd integer is positive and odd. This verifies
ordinary legality, including the exact valuations.

The source domain is precisely

\[
 \boxed{x\equiv271\pmod{512}.}                              \tag{2}
\]

Indeed, three valuation-one steps give `(27x+19)/8`; its next valuation
is at least six exactly when `81x+65=0 mod512`. This congruence also
forces the first three valuations to be one. The least positive member
is 271. The actual endpoint satisfies

\[
 q=\frac{81x+65}{2^{b+3}}\le\frac{81x+65}{512}<\frac{x}{6},
 \qquad x\ge271.                                           \tag{3}
\]

Thus it excludes this whole domain from containing a least failed
five antecedent: `x in C` and `5x notin C` would imply the same failure
at the smaller ordinary unit `q`. Its sources start with valuation one,
so the domain is disjoint from all PR166 valuation-two ladder cylinders.
The energy note uses this exact domain and its complete inverse fibers.

For example, `b=6`, `x=271` gives `q=43`; the target path sends
`1355` to `215`. This example is only a replay of the identity, not its
proof. A direct first-hit family is

\[
 x_k=\frac{2^{31+54k}-65}{81},\qquad k\ge0,
\]

with source word `(1,1,1,28+54k)` and target word
`(1,2,5,23+54k,4)`. Unit members can be selected by their residue modulo
three; the block theorem itself needs no source unit assumption.

## CF2. Entering and leaving a nonzero carry

Define the two fixed words

\[
\begin{aligned}
 E&=(2,1,1,1,2,1,7),\\
 F&=(3,6,1,2,1,1,1).
\end{aligned}
\]

Both contain seven odd inputs and use 15 shortcut steps. Their affine
corrections are respectively `3709` and `149617`, and

\[
 149617-5\cdot3709=4\cdot2^{15}.                            \tag{4}
\]

**Entry.** Whenever `x` has the legal prefix `E` to `y`, the prefix `F`
on `5x` is legal and ends at `5y+4`.

Here is a complete ordinary certificate for the base of the cylinder.
Each row lists all successive positive odd states, including the start.

| Word | Successive states |
|---|---|
| `E` | `25065, 18799, 28199, 42299, 63449, 47587, 71381, 1673` |
| `F` | `125325, 46997, 2203, 3305, 2479, 3719, 5579, 8369` |

The source word is exact precisely on `x=25065 mod65536`. Write its
positive members as `25065+65536k`, `k>=0`. At each intermediate odd
state, the increment is an even nonnegative integer, since the total
division exponent is 15 and the starting increment has valuation 16.
The same observation applies to the target increment `5*65536k`.
Thus both tables lift with all valuations unchanged. The final states
are `y=1673+4374k` and `5y+4`. Equation (4) is an independent affine
check of the final relation.

**Loop.** If `z` has valuation one, then `5z+4` has valuation one and

\[
 U(5z+4)=5U(z)+4.                                          \tag{5}
\]

In fact `3(5z+4)+1=5(3z+1)+8`. Dividing by two gives (5), an odd
integer whenever `U(z)` is odd. Therefore the same carry survives any
number of consecutive valuation-one steps. There is no bound on that
number in the theorem.

**Exit.** If `z` has a legal prefix `(3,b)` to `q`, with `b>=2`, then
`5z+4` has the legal prefix `(4,b-1)` to `5q`:

\[
 \boxed{5 I_3 I_b(q)+4=I_4 I_{b-1}(5q).}                    \tag{6}
\]

For a direct valuation check, put `v=U(z)`. The second source exponent
implies `v=1 mod4`. Thus

\[
 3(5z+4)+1=8(5v+1)
\]

has valuation four. Its odd quotient is `(5v+1)/2`, and the next
numerator is `5(3v+1)/2=5*2^(b-1)q`, giving exactly the claimed final
exponent and endpoint. All values are positive.

## CF3. The unbounded run-one ladder

Combining entry, loop, and exit proves the following all-parameter
physical identity. For every `r>=0`, `b>=2`, and every legal source
prefix

\[
 W_{r,b}=E\,(\underbrace{1,\ldots,1}_{r})\,(3,b)
\]

from `x` to `q`, the target `5x` has the legal prefix

\[
 V_{r,b}=F\,(\underbrace{1,\ldots,1}_{r})\,(4,b-1)
\]

to `5q`. Both prefixes contain `r+9` odd inputs and have shortcut
clock `r+b+18`:

\[
 \boxed{T^{r+b+18}(x)=q,\qquad T^{r+b+18}(5x)=5q.}           \tag{7}
\]

This is an unbounded family of ordinary words. The integer `r` is the
actual length of a supplied valuation-one run; it is neither a bounded
search parameter nor a choice of a different infinite completion.

The source correction has the useful closed form

\[
 \boxed{B_r=1351\,3^{r+5}+2^{r+16}.}                        \tag{8}
\]

To see this, the correction of `(1^r,3,b)` is
`3^(r+2)+2^(r+1)`. Prefixing `E` gives

\[
 3^{r+2}\cdot3709+2^{15}(3^{r+2}+2^{r+1})
 =1351\,3^{r+5}+2^{r+16}.
\]

The target correction is exactly `5B_r`, also obtainable directly from
its word. In contrast to CF1, a run-one block need not lower ordinary
height: its leading multiplier is
`3^(r+9)/2^(r+b+18)`, which can exceed one. The certificate compiler
below terminates by consuming a given finite word, not by assuming
height descent for this family.

## CF4. Explicit positive unit witnesses at every rank at least nine

For `r>=0`, let `t_r` be the least positive residue

\[
 t_r\equiv88\,2^{-r}\pmod{243},\qquad1\le t_r\le242,
\]

and set

\[
 \boxed{\begin{aligned}
 b_r&=2\,3^{r+4}t_r-2,\\
 x_r&=\frac{2^{r+b_r+18}-1351\,3^{r+5}-2^{r+16}}{3^{r+9}}.
 \end{aligned}}                                           \tag{9}
\]

Then `x_r` is a positive odd integer congruent to one modulo three.
Its complete first-hit word is `W_(r,b_r)`, so its odd rank is exactly
`r+9`. The first-hit word for `5x_r` is `V_(r,b_r)` followed by the
single exponent four. The target rank is exactly `r+10`, and its
shortcut clock is four larger than that of the source.

### Integrality and the unit condition

The exact small congruence

\[
 4^{81}\equiv1+178\cdot3^5\pmod{3^{10}}
\]

can be checked by repeated squaring. Cubing proves inductively that

\[
 4^{3^{r+4}}\equiv1+178\cdot3^{r+5}\pmod{3^{r+10}}.
\]

The binomial terms of degree two and higher vanish at this modulus
when raising the expression to `t_r`. Since

\[
 178\cdot88\cdot2^{16}\equiv1351+81\pmod{243},
\]

we get

\[
 2^{r+16}(2^{b_r+2}-1)-1351\,3^{r+5}
 \equiv3^{r+9}\pmod{3^{r+10}}.                             \tag{10}
\]

This is the numerator in (9). It proves divisibility by `3^(r+9)`
and `x_r=1 mod3`.

Every letter of `W_(r,b_r)` is positive, and `b_r>=160`. Starting
backwards from the odd endpoint one, divisibility of the full numerator
implies each successive inverse division is integral, as in CF1.
Each inverse output is odd and positive. The final letter exceeds two,
so its inverse output exceeds one; no subsequent integral inverse of
an odd integer greater than one can be one, because `I_a(u)=1` would
require `2^a u=4`. Thus the source certificate is first-hit. CF2 shows
that the target entry states exceed one, its loop states are `5z+4>1`,
and its exit ends at five without an earlier one. Appending `5->1`
therefore gives the first-hit target certificate.

The first four `(t_r,b_r)` pairs are `(88,14254)`, `(44,21382)`,
`(22,32074)`, and `(11,48112)`. Their large last exponents are genuine
parts of the construction, not claims about efficient certificates.
The finite checker verifies these ordinary examples without printing
their very large starting integers. The proof, rather than that
finite list, supplies every `r`.

## CF5. A compiler on the enlarged block language

Let `D` consist of the following source blocks and their displayed target
replacements:

| Source block | Target block | Status/source |
|---|---|---|
| `(2^r,b)`, `r>=1,b>=4` | `(5,b-3)` if `r=1`; `(4,2^(r-2),3,b-3)` otherwise | PR166 FL1, imported explicitly |
| `(1,1,1,b)`, `b>=6` | `(1,2,5,b-5)` | CF1 |
| `E,1^r,3,b`, `r>=0,b>=2` | `F,1^r,4,b-1` | CF3 |

Here superscripts on letters mean repetitions, not numerical powers.
The three block forms have distinct beginnings: a valuation-two run
followed by a letter at least four; three leading ones; or the specific
prefix `E`, whose second letter is one. Their subsequent parsing is
unambiguous.

For any supplied **complete first-hit certificate** in `D*`, replace
each block and append the final exponent four. This produces a complete
first-hit certificate for `5x`, with exactly one additional odd input
and four additional shortcut steps. Each block transports the same
ordinary comparison to the actual next endpoint. Every replacement
has the same odd count and clock, and no target block encounters one.
The finite input is strictly shortened at each parsing step, so the
compiler terminates on the stated language without a guessed stopping
bound. The empty source word at `x=1` maps to the certificate `(4)`.

The implementation validates its supplied source word first. Malformed
certificates raise an error. A valid first-hit certificate outside the
language returns `UNRESOLVED`; it is never silently treated as a
nonconvergent input or as a completed proof.

## What the attempted completion still needs

The carry state solves arbitrarily long *specified* valuation-one runs.
It does not show that every supplied source certificate enters that
state, and it does not provide an exit after an arbitrary subsequent
word. The rank-one words `(2a)` are immediate examples outside `D*`.
Even unlimited enlargement by balanced proportional blocks cannot
justify a universal finite-terminal compiler: the separate phase note
in this packet gives a stronger obstruction, including certified good
inputs. Such an obstruction concerns that compiler architecture; it
does not refute an energy argument supported only on genuine failures,
or an adaptive construction with a changing comparison and additional
well-founded arithmetic control.

The first missing theorem is a total successful transformation for
arbitrary supplied certificates, or another global argument that
discharges the uncovered inputs. None is supplied here.

## Executable evidence

`check_carry_compiler.py` uses exact integer and rational arithmetic and
explicit exceptions in normal and optimized Python. It verifies the
ordinary entry/loop/exit, the closed correction formulas, CF1 inverse
fibers, the explicit all-rank family at declared finite indices, mixed
block composition, and malformed/unsupported inputs. Its JSON report
records these finite scopes separately. It does not purport to check
the universal quantifiers by enumeration.
