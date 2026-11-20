# A certified fourth-gap-three obstruction to bounded conditional paths

**PROPOSED; method obstruction, not a Collatz counterexample.** The statement
below excludes a uniformly bounded ordinary prefix in a specific smaller-
antecedent proof architecture. It leaves unbounded, certificate-dependent
constructions open. The sources witnessing the obstruction have explicit
finite upper stopping certificates.

Write `T(n)=n/2` for even positive integers and `T(n)=(3n+1)/2` for odd
positive integers. Write `C` for its actual basin of 1, and `U` for its
accelerated odd map. Every integer quantified below is an ordinary integer.

## G1. The precisely guarded graph

For an eligible upper antecedent `X=128h+1`, where `h>0` and `4 ∤ h`,
let `G_X` have all positive integers as vertices, all ordinary edges
`n <-> T(n)`, and only the following additional **directed** arrows:

\[
64j+1\longrightarrow128j+1,
\qquad j>0,\quad4\nmid j,\quad128j+1<X.                 \tag{1}
\]

The direction is essential. If `X` is the least failure of PR146's
reverse implication, a path in this graph transports convergence
backwards from its endpoint to its start. Ordinary intermediate heights
are unrestricted; only the antecedents of the added arrows are bounded.

## G2. No short ordinary path to any smaller integer

Let `L>=1`, and suppose

\[
N>1,\qquad N\equiv1\pmod{3^L},\qquad
N\equiv-1\pmod{2^L}.                                  \tag{2}
\]

There are no `0<=i,j<=L` and positive `y<N` with `T^i(N)=T^j(y)`.
Consequently there is no ordinary undirected walk of length at most
`L` from `N` to any smaller positive integer.

This is the signed fixed-point argument in PR146's
[`ADJACENT_DESCENT.md`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/ADJACENT_DESCENT.md),
restated for its actual general congruence hypotheses. Here is a
self-contained proof of the needed form.

The first `i<=L` inputs from `N` are odd, so, with `u=(N+1)/2^i`,

\[
T^i(N)=3^i u-1.                                        \tag{3}
\]

Reverse the actual `j`-step parity word from `y`, using the rational
branches `E(v)=2v` and `I(v)=(2v-1)/3`. Let `q` be its odd count.
If `q<=i`, reverse this word also from `-1`. The reversal is integral:
its difference from the actual reversal starts at `3^i u`, and retains
enough factors of three before every division. Its result is `-M`,
where `1<=M<=2^(j-q)`. Indeed both branches preserve `(-infinity,-1]`;
`I` does not increase absolute value there, and each `E` doubles it.
The affine difference then gives

\[
y=2^j3^{i-q}u-M
 \ge2^{j-q}\bigl(2^q3^{i-q}u-1\bigr)
 \ge2^i u-1=N.                                        \tag{4}
\]

In particular a suffix with exactly `i` odd inputs and length `i+b`
starts at

\[
w=2^bN+c,\qquad0\le c\le2^b-1.                        \tag{5}
\]

If `q=i+d`, with `1<=d<=L`, split the forward word immediately after
its first `d` odd inputs, at clock `J`. The suffix has form (5).
Reversing the prefix gives a rational affine function of `N`, of slope
`alpha=2^(J+b)/3^d`. Replace the suffix start by `2^b+c`, the value
at `N=1`. Its reversed endpoint `beta` is a positive integer: the
change `2^b(N-1)` is divisible by `3^d`, so every division remains
integral; an integral inverse of a positive integer stays positive.
Replacing the suffix start by `c-2^b<=-1` gives `beta-2alpha<=-1`.
Therefore `alpha>=(beta+1)/2>=1`, and

\[
y=\alpha(N-1)+\beta\ge N.                              \tag{6}
\]

Since `q<=j<=L`, these cases exhaust the possible words. Finally,
cancel every backward edge immediately followed by a forward edge in
an ordinary walk. The remaining walk consists of forward edges followed
by backward edges, yielding a meeting with both clocks bounded by its
original length. This proves the walk assertion.

## G3. Unbounded prefixes in one fixed fourth-valuation class

**Theorem.** For every integer `H>=1`, there are infinitely many
eligible upper antecedents `X in C` whose fourth odd-step valuation
is exactly three, with corresponding lower companion `Y=(X+1)/2`,
such that the following holds. Put `z=U^4(X)` and `N=T^6(Y)`.
Every directed path in `G_X` from `N` to any smaller positive integer
uses **more than `H` ordinary edges before its first added arrow or
before arrival**. In particular this applies to the already certified
target `z<N`.

Choose `L=H+6` and a positive `N` satisfying (2). Set

\[
h=\frac{N-1}{27},\qquad X=128h+1=\frac{128N-101}{27},
\qquad Y=64h+1,\qquad z=\frac{3N-1}{4}.                 \tag{7}
\]

These are positive integers. Because `L>=7`, one has `h=2 (mod4)`;
thus `h` is eligible. Moreover

\[
162h+4=2(3N-1),\qquad v_2(162h+4)=3,
\qquad U^4(X)=z,\qquad T^6(Y)=N.                        \tag{8}
\]

For the fourth-valuation assertion, `N=-1 (mod8)` makes
`3N-1=4 (mod8)`. The first three odd valuations from `X` are all
two; after them the odd state is `54h+1`. The fourth is therefore
exactly three and gives `z`. Finally `z<N` since `N>1`.

Suppose a directed path uses its first added arrow after at most `H`
ordinary edges. Its source is `64j+1` with `j<h`. Appending six
ordinary steps to this ordinary prefix gives an ordinary walk of
length at most `H+6=L` from `N` to

\[
T^6(64j+1)=27j+1<27h+1=N,                              \tag{9}
\]

contrary to G2. Arrival at a smaller integer before any added arrow
is excluded directly by G2. This proves the asserted lower bound
for every `N` satisfying (2), independent of basin membership.

To ensure a genuine certified upper antecedent, choose `z in C` in
the simultaneous residue classes

\[
z\equiv-1\pmod{2^{L-2}},\qquad
z\equiv2\,4^{-1}\pmod{3^{L+1}}.                         \tag{10}
\]

The elementary [basin residue lemma](BASIN_CRT_DENSITY.md) provides
infinitely many such `z`, each with an explicit finite ordinary
certificate. For each of them, `N=(4z+1)/3` is an integer satisfying
(2). In particular `N-1=(4z-2)/3` is divisible by `3^L`, and
`v_2(N+1)=v_2(z+1)+2>=L`. Equations (7)--(8) then certify `X in C`
using that same given certificate for `z`. This completes the theorem.

The basin residue lemma is a construction of many known basin members,
not a closure principle: it never turns a limit of convergent sources
into a certificate for an arbitrary fixed source. No claim about the
lower companion being nonconvergent is made here.

## G4. A proposed ceiling-three atlas is also impossible

Consider the variant where added arrows must satisfy `128j+1<=3N`,
and seek an ordinary or conditional path from every odd ternary unit
`N>1` to a smaller positive integer. For any such added arrow,

\[
T^6(64j+1)=27j+1\le\frac{81N+101}{128}<N               \tag{11}
\]

when `N>=5`. The same CRT argument therefore excludes a uniformly
bounded ordinary prefix before the first added arrow or descent.
More generally it excludes every fixed ceiling factor `C<128/27`
for sufficiently large sources, since the right side becomes
`(27CN+101)/128`.

This is a theorem about bounded-word atlases. An adaptive algorithm
with source-dependent clocks is not excluded. In particular G3 does
not establish a lower bound on the number of **odd inputs** in an
arbitrary accelerated word, nor on its number of conditional arrows.

## Exact remaining step

[The least-failure height theorem](LEAST_FAILURE_HEIGHT.md) reduces a
global first failure to finitely many possible fourth valuations and
gives a known initial basin interval. G3 shows that even the surviving
valuation three cannot be handled by a finite set of uniformly bounded
ordinary paths under the smaller-antecedent guard. A successful proof
may still use the actual unbounded certificate for `z`, an unbounded
ordinary descent, or a different argument entirely. No such complete
construction is established in this packet.

`check_guarded_clock.py` independently checks the algebraic identities,
selected full ordinary predecessor trees, and compressed certified
instances. The universal statements follow from G2--G3, not from
extrapolation of that finite replay.
