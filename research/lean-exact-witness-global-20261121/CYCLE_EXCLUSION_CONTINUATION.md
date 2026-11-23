# Complementary carries and the complete fractional-part fiber

Date: 23 November 2026. **Status: exact written identities and targeted
refutations of proposed closing steps. Positive-cycle exclusion remains
OPEN.** None of this note is counted as a Lean theorem.

This continuation attacked two possible all-word conclusions: an
integrality transfer to the complementary parity cycle, and a bound on
the entire residue fiber of the original numerator. Neither conclusion
was proved. The carries below retain the complete denominator. The two
positive rational controls show that proposed minimum-selection and
noncrossing arguments do not supply the required fiber bound, even when
every state of the displayed cycles is above three.

## 1. The actual targets and the frozen sources

Use the shortcut map on rationals with odd reduced denominator,

\[
 T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.
 \end{cases}
\]

Parity means numerator parity. For a binary word `w` of length `A` and
weight `p`, with one positions `d_0<...<d_(p-1)`, put

\[
 C_w=\sum_{j<p}2^{d_j}3^{p-1-j},\qquad D=2^A-3^p.
 \tag{CE1}
\]

Its rational fixed point is `C_w/D`. A full rotation gives every other
state of its cycle. These are exact rational itineraries: all rotations
have odd denominator, and the first edge identity modulo two forces the
prescribed parity at each phase. Distinct finite words of the same
length cannot have the same fixed point, since its itinerary is unique.

The preceding owned source is PR177,
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
[`HIGH_VARIANCE_ARITHMETIC.md`](HIGH_VARIANCE_ARITHMETIC.md), HC16--HC21.
The current peer inputs were read at these exact revisions:

- PR185, `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
  `research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md`
  and `PRINCIPAL_FIBER_CONTROL.md`: the surviving polynomial denominator
  has a power lower bound, but its actual numerical evaluation can
  undergo further cancellation. That missing arithmetic is retained here.
- PR176, `ff3e068fa44eb85bb918580b2e10e18c027a18e6`,
  `research/lean-global-resolvent-20261121/overview/longshot/cycles/IDENTITY_ATOM_ATTEMPT.md`:
  the exact trace coefficient, full residue-fiber target, support-size
  obstruction to uniform mixing, and comparable-word counterexample.
  Its large enumerations were not repeated for this note.

The proposed all-residue statement is

\[
 N_r(A,p)=\#\{w:|w|=A,\ |w|_1=p,\ C_w\equiv r\pmod D\},
 \qquad \max_rN_r(A,p)<A
 \tag{CE2}
\]

for `A>=3`, `p>=1`, `D>0`. Its zero-residue case would exclude every
nontrivial positive integer cycle. This note neither proves nor refutes
CE2. The controls below refute specific proposed mechanisms for proving it.

## 2. A uniform-alphabet version of the whole-denominator carry

Retaining every shortcut phase gives a useful common format for a word
and its complement. Define

\[
 (L_w x)_i=2x_{i+1}-3^{w_i}x_i,
 \qquad L_w x=w,
 \tag{CE3}
\]

with cyclic indices. Its determinant, up to sign, is the full `D` in
CE1. Since this determinant is odd, reduction modulo two is legitimate
for its rational inverse. Start `c^(0)=w`, set
`b_i^(t)=c_i^(t) mod 2` in `{0,1}`, and iterate

\[
 c_i^{(t+1)}=
 \frac{c_i^{(t)}+3^{w_i}b_i^{(t)}-2b_{i+1}^{(t)}}2.
 \tag{CE4}
\]

If `x^(t)=L_w^(-1)c^(t)`, then

\[
 x^{(t+1)}=(x^{(t)}-b^{(t)})/2.
 \tag{CE5}
\]

Thus these are exactly the binary digits of the original rational
cycle. The carry reaches zero precisely when every coordinate of that
cycle is a nonnegative integer. No factor of `D` has been removed.

The invariant alphabet is independent of the lengths of halving blocks:

\[
 \boxed{\quad
 w_i=0\Longrightarrow c_i^{(t)}\in\{-1,0\},\qquad
 w_i=1\Longrightarrow c_i^{(t)}\in\{-1,0,1,2\}.
 \quad}
 \tag{CE6}
\]

For `w_i=0`, either allowed carry gives the next value `-b_(i+1)`.
For `w_i=1`, carries `-1,0,1,2` give respectively
`1-b_(i+1)`, `-b_(i+1)`, `2-b_(i+1)`, `1-b_(i+1)`.
This proves invariance from the initial vector. Applying the same
construction to `1-w` gives eight possible pairs of carry values at
each phase once `w_i` is fixed.

The finite local alphabet did not produce a uniform invariant forcing
the complementary carry to terminate whenever the original one does.
That would be an additional theorem, not a consequence of CE4--CE6.

## 3. What complementary integrality would settle

Let `y_i` be the rational cycle for `1-w`, aligned with `x_i`. Its full
denominator before reduction is

\[
 \overline D=2^A-3^{A-p},\qquad
 y_0=C_{1-w}/\overline D.
 \tag{CE7}
\]

This rational cycle is the periodic instance of the autoconjugacy
`Omega` studied by Monks--Yazinski. Rationality here follows directly
from a finite word; no rationality conjecture for arbitrary `Omega(n)`
is assumed.

If `x_i` is a positive integer cycle, multiplication of its odd edges
gives `2^A<=4^p`; equality forces every odd state to be one. Hence a
nontrivial cycle has `p>A/2`, and its complementary rational cycle is
positive because `A-p<A/2` implies `3^(A-p)<2^A`.

If even one state of that complementary cycle were an integer, its
whole periodic orbit would be a positive integer cycle. Applying the
same inequality to it gives `2^A<=4^(A-p)`, or `p<=A/2`, a
contradiction. Therefore the following is a genuine sufficient closing
step:

> Prove that a positive integer periodic point has an integral
> complementary periodic point.

This is not claimed as a new reduction; it is closely related to the
known self-conjugacy route. In particular, it must distinguish the
denominator-one case rather than assume that integrality transfers.
Two exact controls keep that distinction visible:

\[
 (-5,-7,-10)\ \longleftrightarrow\ (4/5,2/5,1/5)
 \tag{CE8}
\]

are complementary cycles with words `110` and `001`. Thus signed
integrality does not transfer. The original negative cycle reaches the
negative binary-tail carry face, not zero, so this control is not a
counterexample to the proposed positive zero-carry implication.

For positive rational cycles, `11100` has root `19/5`, while `00011`
has root `40/23`. Both full cycles are positive, and the reduced
denominators are the coprime integers five and twenty-three. Thus
positivity alone does not make the complementary denominator divide
the original denominator. These examples do not decide the additional
denominator-one hypothesis.

### An exact coupled moment, and its limit

With `w_i` the original parity bit,

\[
 4x_{i+1}y_{i+1}=3x_iy_i+w_iy_i+(1-w_i)x_i.
 \tag{CE9}
\]

The individual sum balances are

\[
 \sum_{w_i=0}x_i=\sum_{w_i=1}x_i+p,\qquad
 \sum_{w_i=1}y_i=\sum_{w_i=0}y_i+(A-p).
\]

Summing CE9 and using these identities gives

\[
 \boxed{\frac1A\sum_{i<A}(2x_i-1)(2y_i-1)=3.}
 \tag{CE10}
\]

The identity retains both numerical denominators. A positive integer
original cycle can compensate through complementary rational states
below one; CE10 does not make those rational states integral. The
attempt to obtain complementary divisibility from the coupled moment
or from the local carry alphabet did not close this step.

## 4. The fractional-part interpretation of the full fiber

Fix `A,p,D>0` as in CE1. A residue fiber consists exactly of the
rational periodic points

\[
 x=C_w/D=k+r/D,
 \tag{CE11}
\]

with a common fractional part. Consequently any two points in the
fiber initially differ by an integer.

Let two such points follow their actual words `w,v`, and suppose their
length-`L` prefixes have the same number `h` of odd steps. Then

\[
 T^L(y)-T^L(x)=
 \frac{3^h(y-x)+C_{v[0:L]}-C_{w[0:L]}}{2^L}
 \in\mathbb Z.
 \tag{CE12}
\]

The displayed quotient has denominator a power of two. On the other
hand, both actual endpoints have odd denominator, so the quotient is
an integer. This is an exact synchronization statement, independent of
the size or sign of the endpoints.

Between consecutive equal-count times, the prefix-count difference
has one sign. For a nontrivial excursion, if `v` has the larger count throughout the interior,
its one positions in that block are coordinatewise earlier and
`C_v<C_w`; the reversed excursion gives the reversed sign. A one-clock
block with identical bits has `C_v=C_w`. This
controls the sign of the additive term in CE12. It does not control
the sign or size of the resulting integer difference. The following
positive periodic controls locate the missing inference.

## 5. Distinct cycle minima can share one fractional part

At

\[
 (A,p,D)=(16,10,6487)
\]

the words

```text
1101111111100000
1111101001011100
```

have respective roots

\[
 x=83245/6487,\qquad y=109193/6487=x+4.
 \tag{CE13}
\]

Direct exact replay shows that each root is the minimum of its own
primitive sixteen-state cycle. Their shared numerator residue is
`5401`. Every state in both cycles is greater than twelve.
Thus selecting the unique minimum of each cycle does not make the
fractional-part map injective. A fiber argument requiring one minimum
per residue is false even for positive cycles far above one.

## 6. Common-count returns can reverse real order above a fixed floor

At

\[
 (A,p,D)=(21,13,502829)
\]

take

```text
w = 011111111100011101000
v = 111111111101000000011.
```

Their fixed points are

\[
 x=3703718/502829,\qquad y=4206547/502829=x+1.
 \tag{CE14}
\]

Both are primitive twenty-one-state positive cycles. Their minima
are respectively

\[
 1851859/502829>3,\qquad1590227/502829>3.
\]

At clock fifteen, both prefixes have exactly eleven odd steps, but

\[
 T^{15}(x)=25946461/502829,\qquad
 T^{15}(y)=25443632/502829=T^{15}(x)-1.
 \tag{CE15}
\]

The order of the two points has reversed at a synchronized return.
The complete period returns the integer difference to `+1`.
The initial shared residue is `183915`, a unit modulo `D`.

This refutes a same-fractional-part noncrossing argument even with
primitivity, a positive cyclic floor greater than three, the original
complete denominator, and equality of both elapsed clocks and odd
counts. It does not refute CE2, whose fiber-cardinality bound could
still hold by a different mechanism.

## 7. Evidence and the first unsupported steps

[`cycle_fiber_controls.py`](cycle_fiber_controls.py) directly regenerates
the two displayed cycle pairs, all their exact edge identities,
primitivity, cyclic minima, common residues, and the synchronized
crossing. It also checks the complementary controls and CE10, and
replays the uniform carry recurrence against exact rational binary
digits for those specified words. It uses explicit failure checks,
including under optimized Python. The script is a targeted replay of
the stated controls, not an all-word census or an attempted proof of
CE2. Short exploratory searches located the witnesses; the universal
claims are not inferred from those searches.

The complementary route still needs a proof of integral output at
denominator one. The fiber route still needs a bound strong enough
at residue zero, or the all-residue bound CE2. The local carry
alphabet, synchronized integer differences, minimum selection, and
the proposed noncrossing invariant do not establish either step.

Primary context: Kenneth G. Monks and Jonathan Yazinski,
*The autoconjugacy of the 3x+1 function*, author manuscript dated
10 July 2002, Sections 1--2, Theorems 2.1 and 2.3--2.5, Examples 1,
2 and 5, <https://monks.scranton.edu/files/pubs/AutoConjV13.pdf>.
The paper's conjecture that autoconjugacy preserves all rational
2-adic integers is not used. Its known signed example CE8 is
reconstructed here rather than presented as a newly found cycle.
