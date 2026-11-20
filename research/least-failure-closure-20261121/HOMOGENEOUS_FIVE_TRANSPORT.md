# Complete recognition of homogeneous five transport

**PROPOSED elementary results. The universal forward-five implication remains
OPEN.** This note gives a complete, finite recognizer for every physical
transport with the same odd count and shortcut clock on its two arms. It
then completely classifies the smallest such transports beginning with an
odd division exponent one. The recognizer is not a complete Collatz solver.

Use the positive shortcut map `T(n)=n/2` on even inputs and `(3n+1)/2` on
odd inputs, and the accelerated odd map

\[
U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

For a legal odd exponent word `w=(a_1,...,a_p)`, all `a_i>=1`, put
`A_0=0`, `A_j=a_1+...+a_j`, `L=A_p`, and

\[
B(w)=\sum_{j=0}^{p-1}3^{p-1-j}2^{A_j}.
\tag{1}
\]

If its actual positive odd source is `x` and endpoint is `q`, then

\[
3^p x+B(w)=2^Lq.
\tag{2}
\]

The endpoint is a ternary unit. A *homogeneous five transport* for this
prefix is another actual positive odd word with `p` odd inputs and shortcut
clock `L`, taking `5x` to `5q`. The two endpoint values are fixed by the
given source prefix; this is not permission to replace the source or its
known endpoint by an unrelated congruence lift.

## Source comparison

PR157 at `64361ecca770092d6c8242dc6211e38818af2e50`,
`research/global-closure-20261120/merger.md`, proves that the physical law
`x in C => 5x in C` for every positive odd ternary unit would imply full
Collatz. Its `closing-attempts.md` retains the rank-one residual family.

PR162 at `2279da37ac612dbe049777354cdedb3c0aa03282`,
`research/creative-closure-20261120/five_closure.md`, proves the two-input
block `(2,b)->(5,b-3)`, `b>=4`. PR166 at
`5996b9f525ca50978bc34f423192c36a87765bf3`,
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`,
extends this to arbitrary runs of twos and compiles the language
`(2+[4,infinity))*`. Those physical identities are credited.

The general affine correction formula is standard and already used in
those sources. The additional results here are the complete unique-decoder
interface, its maximality over all homogeneous block dictionaries, and the
complete first-valuation-one classification below. No external theorem or
GRH assumption enters these statements.

## HT1. A unique correction expansion and complete recognition

For positive integer `C` and positive integer `p`, the following procedure
either recovers the unique increasing positions

\[
0=D_0<D_1<\cdots<D_{p-1},\qquad
C=\sum_{j=0}^{p-1}3^{p-1-j}2^{D_j},
\tag{3}
\]

or correctly certifies that no such expansion exists.

Start with `R=C`. For `r=p,p-1,...,2`, require
`R>3^(r-1)`, put `e=v2(R-3^(r-1))`, require `e>=1`, record `e`, and
replace `R` by `(R-3^(r-1))/2^e`. Finally require `R=1`. The successive
recorded values are `D_1-D_0,...,D_{p-1}-D_{p-2}`.

**Proof.** In any expansion (3), subtracting its first term leaves

\[
2^{D_1}\left(3^{p-2}+
 \sum_{j=2}^{p-1}3^{p-1-j}2^{D_j-D_1}\right).
\]

The parenthesized term is positive and odd. Thus `D_1` is forced by the
binary valuation; dividing leaves an expansion of the same form with one
fewer term. Induction proves necessity and uniqueness. Reversing the
successful steps proves sufficiency. The case `p=1` is exactly `C=1`.
This uses `p-1` valuation/subtraction steps, with integer sizes determined
by the supplied clocks. It is not a claim of bounded cost independent of
those integer sizes. QED.

**Transport theorem.** For the actual source prefix in (2), a homogeneous
five transport exists if and only if the decoder succeeds on `(5B(w),p)`
and its final position satisfies `D_{p-1}<L`. When it exists, its target
word is unique:

\[
(D_1-D_0,\ldots,D_{p-1}-D_{p-2},L-D_{p-1}).
\tag{4}
\]

**Proof.** Any such actual target path has a correction `B'` satisfying
`3^p(5x)+B'=2^L(5q)`. Subtracting five times (2) gives `B'=5B(w)`.
The decoder and final positive gap are therefore necessary.

Conversely the recovered correction gives the full inverse numerator
`2^L(5q)-B'=3^p(5x)`. Full numerator divisibility by `3^p` forces every
successive inverse division to be integral: reduce modulo three to recover
the last inverse step, divide, and repeat. Every exponent in (4) is positive,
so each resulting integer is odd. Starting at positive odd `5q`, all inverse
outputs are positive; an integral quotient `(2^a v-1)/3` cannot be zero
or negative for `v>=1` and `a>=1`. Each division exponent is exact because
its resulting endpoint is odd. The constructed path starts at `5x` by
the full identity. Thus it is an actual ordinary path, not just a rational
affine match. QED.

No target prefix can visit 1: after a visit to 1 the positive accelerated
map stays at 1 and cannot later reach `5q>=5`.

## HT2. A maximal compiler on supplied first-hit certificates

Apply HT1 to the entire supplied first-hit word of `x`, whose endpoint is
`q=1`. If it succeeds, append the exponent four, the actual edge `5->1`.
The result is a first-hit certificate of `5x` with exactly

\[
\omega(5x)=\omega(x)+1,\qquad
\tau(5x)=\tau(x)+4.
\tag{5}
\]

For `x=1` use the one-letter certificate `(4)` directly. Malformed source
certificates are rejected separately from a valid certificate on which
the recognizer returns `UNRESOLVED`.

This one-shot recognizer includes **every** complete compiler formed by
concatenating homogeneous transports of the type defined above, even if
the dictionary is infinite and blocks are selected adaptively. Indeed
concatenating accepted blocks gives an actual transport from `5x` to 5
with the source's total odd count and shortcut clock. HT1 must recover
that word. This is a precise maximality theorem for the named architecture,
not maximality over arbitrary ordinary certificate transformations.

In particular the whole PR166 ladder language is accepted. The new
families below are also accepted, despite beginning with an exponent one.

## HT3. Complete minimal-depth classification at initial exponent one

Suppose the source prefix starts with `a_1=1`. No homogeneous five transport
exists with at most three odd inputs. With exactly four odd inputs, all
possibilities are the following three infinite families:

| Source word | Required last exponent | Unique target word |
|---|---|---|
| `(1,1,1,b)` | `b>=6` | `(1,2,5,b-5)` |
| `(1,1,2,b)` | `b>=4` | `(1,5,1,b-3)` |
| `(1,1,4,b)` | `b>=4` | `(1,3,5,b-3)` |

The classification quantifies over **all** positive intervening division
exponents. It is not inferred from a finite search.

### Excluding shorter words

At one odd input, `B=1` and `5B=5` has no one-term expansion. At two odd
inputs with first exponent one, `B=5`; the required equation
`3+2^u=25` has no solution.

At three odd inputs write the source's first two exponents as `(1,c)`.
Then `B=15+2^(c+1)`. The first target gap is forced to be one, and its
remaining gap would have to satisfy

\[
2^v=5(6+2^c),
\]

which is impossible because the right side is divisible by five.

### The four-input case

Write the source word `(1,c,d,b)`. Its correction is
`B=45+2^(c+1)(3+2^d)`. The first target gap is again forced to be one.
Writing its next two gaps as `u,v`, correction matching becomes

\[
2^u(3+2^v)=5\left[18+2^c(3+2^d)\right].
\tag{6}
\]

If `c>=2`, binary valuation forces `u=1`, and hence

\[
2^v=42+5\cdot2^{c-1}(3+2^d).
\tag{7}
\]

For `c>=3` the right side is 2 modulo four and exceeds two, a contradiction.
For `c=2` it is `72+10*2^d`. At `d=1,2` its odd parts are respectively
23 and 7. For `d>=3` it is `8(9+5*2^(d-2))`, whose parenthesis is odd
and greater than one. Thus `c>=2` is impossible.

For `c=1`, equation (6) is `2^u(3+2^v)=10(12+2^d)`.
At `d=1,2` it yields `(u,v)=(2,5),(5,1)` respectively.
For `d>=3`, valuation forces `u=3` and

\[
2^v=12+5\cdot2^{d-2}.
\tag{8}
\]

At `d=3` the right side is 22; at `d=4` it is 32. At `d>=5` it is
`4(3+5*2^(d-4))`, again with odd part greater than one. Consequently
the only solutions are precisely the three table rows. The requirement
that the final target gap be positive gives their stated thresholds on
`b`. HT1 proves full ordinary legality. QED.

## HT4. Whole source cylinders and smaller physical endpoints

For `a=1,2,4` set respectively

\[
(B,b_0)=(65,6),(73,4),(121,4),\qquad L=a+2+b.
\]

The exact inverse formula is

\[
x=\frac{2^Lq-B}{81},\qquad
T^L(x)=q,\qquad T^L(5x)=5q,
\tag{9}
\]

whenever `b>=b_0`, `q` is positive odd and the source is integral. The
complete source cylinders, with their exact initial exponents, are:

| `a` | Source cylinder | First four exponents |
|---:|---|---|
| 1 | `x=271 mod512` | `(1,1,1,b)`, `b>=6` |
| 2 | `x=135 mod256` | `(1,1,2,b)`, `b>=4` |
| 4 | `x=87 mod1024` | `(1,1,4,b)`, `b>=4` |

**Proof of the cylinder assertion.** Prescribing the first three exact
odd gaps and requiring divisibility at least `2^b0` at the next odd
input fixes one binary residue of modulus `2^(a+2+b0)`. Formula (9)
reduces it to `81x=-B` modulo that modulus, giving the three displayed
residues. Conversely the congruence makes each earlier inverse/forward
division exact and the fourth division at least `b0`; alternatively,
the standard parity-prefix bijection follows directly by reversing each
specified even or odd shortcut step modulo its required power of two.
The eventual endpoint in (9) uses the **full actual** fourth valuation,
so it is odd. Direct reconstruction is included in the checker.

The classes are disjoint, as their first three valuation words differ.
They are outside PR166's initial cylinders, which begin with valuation two.
Their union has density `7/1024` among positive integers before imposing
the ternary-unit guard; its relative density among odd ternary units is
`7/512`. No density conclusion about a fixed exceptional source follows.

Every endpoint obeys `q<=x/3<x`. Indeed
`q=(81x+B)/2^L <= (81x+B)/2^(a+2+b0)`; in the middle row the needed
inequality is `13x>=219`, and every source in that row is at least 135.
The other two rows already satisfy their corresponding inequalities for
every positive source. Thus a least failed forward-five antecedent cannot
belong to any of these cylinders. The two actual arms and the known
membership of `q` in the basin are preserved by (9).

For energy statements restrict the source to `3∤x`; equivalently, for
fixed `q,L`, require `2^Lq-B` not divisible by 243. The endpoint is always
a ternary unit. If an invariant-label five defect is nonzero at the endpoint,
then `q>=5`, because the known edge `5->1` gives zero defect at `q=1`.

There are unconditional first-hit families in all three rows: take `q=1`
and respectively `b=28+54j`, `26+54j`, `20+54j`, `j>=0`. The order of
2 modulo 81 is 54, and the initial clocks `L=31,30,26` meet (9)'s
integrality condition. The source has exactly four odd inputs and the
target exactly five. These formulas remain valid on nonunit sources;
only the unit members are used by the forward-five criterion.

## HT5. A known source with no positive homogeneous first block

There is no positive shortcut clock `t` for which

\[
T^t(35)=5T^t(7).
\tag{10}
\]

This control was supplied by the root and independently replayed here.
The complete finite check is:

| `t` | `T^t(7)` | `T^t(35)` |
|---:|---:|---:|
| 1 | 11 | 53 |
| 2 | 17 | 80 |
| 3 | 26 | 40 |
| 4 | 13 | 20 |
| 5 | 20 | 10 |
| 6 | 10 | 5 |
| 7 | 5 | 8 |
| 8 | 8 | 4 |
| 9 | 4 | 2 |
| 10 | 2 | 1 |
| 11 | 1 | 2 |

No row has ratio five. Thereafter the pair alternates between the last two
rows, proving (10) for every positive clock. Thus even an infinite dictionary
of homogeneous blocks cannot provide a first block at source 7. Allowing
arbitrarily many turns around 1 in its supplied source certificate does
not change these actual trajectories.

Both sources converge: their exact exponent words are `(1,1,2,3,4)` and
`(1,5,4)`. Consequently this excludes an unconditional all-source coverage
claim for the named first-block architecture. It does not exclude a compiler
with separately certified base families or different-clock transformations.
Nor does it refute a renewal argument restricted to nonzero invariant-label
defects: the defect at this known-convergent pair is zero.

## The closing attempt and its exact limitation

The compiler is complete for its precisely named homogeneous transport,
including every possible block dictionary of that kind. That architecture
still omits valid five-convergence certificates with different resources.
For example,

\[
17\xrightarrow{2}13\xrightarrow{3}5\xrightarrow{4}1,
\qquad 85\xrightarrow{8}1.
\]

The source has `p=3,L=9,B=53`. Decoding `5B=265` starts with gap eight
and then fails. There is no homogeneous three-odd-input, nine-clock path
from 85 to 5, although 85 has the displayed shorter certificate to 1.
An `UNRESOLVED` result is therefore not evidence of target nonconvergence.

The rank-one source certificates are all outside this architecture:
`B=1` cannot be transported to `5B` with one odd input. The unbounded
rank-one target family already identified by PR157 remains open here.
Appending turns around 1 changes the source resources and is not justified
by a successful decoder on some unproved padding length. HT5 shows that no
such homogeneous first return exists at all for source 7. For source 17,
its target 85 goes directly to 1 in one odd step and never visits 5, so no
padding after the source's first arrival can turn the complete certificate
into a same-endpoint transport to 5 either.

A full completion must provide a valid transformation that can change
the target odd count/clock or land at a different certified endpoint, and
must prove its success on every supplied witness. No finite carry-state
closure of that larger process has been established in this pass.

## Evidence

`check_homogeneous_five_transport.py` checks the decoder against a finite
independent expansion table, replays source/target paths literally, verifies
the three whole-cylinder controls, compiles mixed complete witnesses, and
retains malformed/unresolved controls. It imports no previous checker and
uses explicit failures that remain active under `-OO`. The universal
recognition and complete four-input classification rest on the proofs
above, not on the finite coefficient table.
