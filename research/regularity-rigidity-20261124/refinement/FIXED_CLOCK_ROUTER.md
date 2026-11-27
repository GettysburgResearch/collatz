# A finite certificate for an 88-clock paired routing block

**PROPOSED written consequence of a completely replayed finite certificate.**
The certificate below covers every unit residue modulo 3^9. It is an exact
Python computation with literal ordinary trajectories, not a Lean proof of
the finite table. The elementary two-block alternative in
[LOCAL_FIBER_ROWS.md](LOCAL_FIBER_ROWS.md) needs no enumeration. Neither
construction proves the fixed-ordinary-target central pressure estimate PT
or the Collatz conjecture.

Use the shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n.
The marked A word is 101000. At x=64t+49 it gives

\[
 T^6(x)=9t+7,\qquad T^6(5x)=5(9t+7),
\]

with two odd inputs on each arm, no earlier equal-count ratio-five return,
and an odd next source when t is even. Padding by common even steps gives
the affine map

\[
 F_a(z)=\frac{9z+7}{2^a},\qquad a\ge6.
\]

Here the particular parity cylinder and odd terminal sentinel are imposed
by the inverse divisibility and the supplied odd endpoint. The single A
branch is from PR146 and was used in PR200; the two-A exact-clock family
appears in PR195 round six. This note changes the finite routing bank,
not the underlying branch.

## Four blocks and the complete finite certificate

Take four chronological exponents a,b,c,d, each at least 6, whose sum is
88. The resulting word has eight odd inputs on each arm and affine map

\[
 F_w(z)=\frac{3^8z+C_w}{2^{88}},\qquad
 C_w=7\left(9^3+9^2 2^a+9\,2^{a+b}+2^{a+b+c}\right).
 \tag{1}
\]

There are exactly 47,905 such compositions. The exact certificate is:

> For each unit residue u modulo 3^8=6561, the carries in (1) congruent
> to u occupy at least two distinct lifts modulo 3^9=19683.

The checker enumerates every composition. It independently reconstructs
its complete binary word and affine carry, checks carry injectivity, and
records the distinct fine lifts. Among the 4,374 coarse unit classes,
249 have two occupied lifts and 4,125 have all three. No class is missing.
All integer guards are explicit exceptions, so optimization of Python
does not disable them.

Let q be any ternary unit and put z=2^88 q modulo 3^9. From the two
certified carries in the coarse class z modulo 3^8, choose one different
from z modulo 3^9. Then

\[
 x=\frac{2^{88}q-C_w}{3^8}\in\mathbb Z_3^\times.
 \tag{2}
\]

This proves coverage on all of U=Z_3^×. For every positive odd ordinary ternary unit q,
(2) gives a literal positive odd ordinary x, with
T^88(x)=q and T^88(5x)=5q, and eight odd inputs on each arm.

To justify physical realization, the full inverse equation can be peeled
from the last A block. Reducing it modulo 9 forces that last inverse to
be integral; dividing by 9 leaves the shorter composite inverse. Continue
through all four blocks. Each integral inverse (2^a y-7)/9 at positive
odd y is positive and odd for a>=6, and is congruent to 49 modulo 64.
The six-clock identities then apply, and the remaining a-6 steps are
literal common halvings. Every interior mark is a ternary unit because
its forward numerator is 7 modulo 3. This argument holds for all positive
odd ordinary ternary units q, not merely the finite representatives used
by the checker.

For a separate direct check, the program chooses a positive odd
representative of each of the 13,122 fine unit classes, constructs (2),
and replays both arms. It checks the first return at six in each block,
the padding, the odd sentinels and all final counts: 26,244 arm paths and
2,309,472 individual shortcut steps. The 87-clock version of this same
four-A grammar supplies a negative control: coarse carry class 1732
has fewer than two fine lifts. We do not assert global optimality of 88
over other word families.

The real map also obeys

\[
 0< C_w/2^{88}\le7/55,\qquad F_w([0,1/2])\subset[0,1/2].
 \tag{3}
\]

Each A map has slope at most 9/64 and offset at most 7/64, so a finite
composition has offset at most (7/64)/(1-9/64)=7/55. In fact each
individual A map already preserves [0,1/2]. The checker verifies the
integer inequality 55 C_w <= 7·2^88 for every word.

## Consequence for simultaneous coarse localization

Use the central row (e,p) supplied by Theorem 1 of LOCAL_FIBER_ROWS.md
at scale H. Given any coarse precision k>=1, put j=ceil(k/8) and

\[
 E=e+88j,\quad P=p+8j,\quad G'=2^E/3^P.
\]

For every unit cylinder C modulo 3^k, iterate (2) outward j times from
one representative of C. The resulting suffix has the same 88j clocks
and 8j odd count in every case. Its ternary contraction sends the whole
of U into C, and (3) preserves the bounded real offset. Appending it to
each word of the base row yields, in every such C, at least

\[
 \frac{c\,3^{P+1-k}}{H}
\]

fine classes, each with

\[
 N_{E,P,1/2}(r)\ \ge\ \frac{cG'}{H}
       \left(\frac{3^8}{2^{88}}\right)^j.
 \tag{4}
\]

The constant c is independent of H, k and C, conditional on the base
row's stated inputs. Injectivity on fine classes follows from the exact
ternary valuation increase 8j. The cardinality comparison loses at most
3^8 because 0<=8j-k<=7. Also
|2P-E|<=C sqrt(H)+72j. Thus k=o(H) preserves balance and the near-linear
exponential order of inverse multiplicity; k=O(log H) gives polynomial
losses. The same final clock works for all coarse classes.

The endpoint in (4) still ranges over favorable fine classes. It is not
a lower bound at the class of a specified ordinary integer at full
precision P+1. This is the same essential quantifier boundary as in
Theorem 2 of the elementary construction.

## Replay and exact sources

Run `python -X utf8 -B check_fixed_clock_router.py --receipt /path/to/receipt.json`.
The receipt includes the source hash and a SHA-256 digest of the entire
deterministic selector over all fine unit classes. Reconstructing that
selector is part of the replay; it is not an unauthenticated external table.

- PR146, f431078244e868dc699fad011044f0d5e7f76437,
  research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md,
  marked return convention and elementary A branch.
- PR200, abf36c63b4d0181541d7e029d390d6f636940750,
  research/regularity-rigidity-20261124/pointwise-fibers/PAIRED_FIBERS.md,
  exact ordinary decoder and carry incidence.
- PR195, 0e8a7f9f965416189b30b57b8aa818fbcb7757c7,
  research/astra-global-closure-20261124/round6/renewal/README.md,
  equations (2)–(3), the prior paired A grammar and real offset bound.

The infinite counting input in (4) is a written, source-qualified theorem;
the finite certificate supplies the routing step alone.
