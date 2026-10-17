# Iteration 12: intrinsic renewal height and the exact source gate

All theorem-level claims remain `PROPOSED` pending independent review.
`X-9510` is an exact finite computation and does not prove an infinite-orbit
statement.

This iteration imports the strongest constructive lesson from the repository's
quotient-refund work: the final runtime state should be recoverable from one
ordinary integer, without trusted type or carry metadata.  The renewal
one-counter system of `ITERATION_11` admits such a compression.

Write `v_p` for the ordinary `p`-adic valuation of a nonzero integer.  At a
nonzero renewal the bridge equations are

\[
3^aX+1=8^RU,
\qquad
4^bY+1=9^RU,
\tag{1}
\]

with

\[
a,R,b\ge1,
\qquad X\equiv Y\equiv5\pmod6,
\qquad U\equiv1\pmod4.
\tag{2}
\]

---

## L-9529: the intrinsic one-integer renewal decoder

**Claim ID:** `L-9529`  
**Title:** One positive integer contains the full renewal type, bridge core, and next renewal  
**Status:** `PROPOSED`  
**Dependencies:** `D-9501`, `L-9518`  
**Scope:** exact positive H renewal states

### Domain and map

For a positive integer `Z`, perform the following forced decoding.

1. Put
   \[
   a=v_3(Z),\qquad X=Z/3^a.
   \tag{3}
   \]
   Require
   \[
   a\ge1,
   \qquad X\equiv5\pmod6.
   \tag{4}
   \]
2. Put
   \[
   e=v_2(Z+1).
   \tag{5}
   \]
   Require `e=3R` for an integer `R>=1`, and define
   \[
   U=(Z+1)/8^R.
   \tag{6}
   \]
   Require `U=1 mod 4`.
3. Put
   \[
   f=v_2(9^RU-1).
   \tag{7}
   \]
   Require `f=2b` for an integer `b>=1`, and define
   \[
   Y=(9^RU-1)/4^b.
   \tag{8}
   \]
   Require `Y=5 mod 6`.

When every test succeeds, define

\[
\boxed{\mathcal R(Z)=3^bY.}
\tag{9}
\]

The map is deterministic and partial on `Z_(>0)`.  The decoded data are exactly
one renewal type and bridge:

\[
\boxed{(a,R,b,X,U,Y).}
\tag{10}
\]

### Exact physical reconstruction

The corresponding exact H block state is

\[
\boxed{p=4(Z+1),\qquad n={4Z\over3}.}
\tag{11}
\]

It has current nonzero block letter `R`.  After that block and exactly `b-1`
zero letters, the next renewal height is `mathcal R(Z)`.  Consequently its
block itinerary begins

\[
R,0^{b-1},\ldots .
\tag{12}
\]

Conversely, every positive exact renewal state gives one `Z` in the domain of
`mathcal R`, and its next renewal is (9).  Therefore

\[
\boxed{
\text{a positive infinite H orbit exists}
\iff
\text{some }Z_0\in\mathbb Z_{>0}\text{ has }\mathcal R^j(Z_0)
\text{ defined for every }j.}
\tag{13}
\]

The lift to shortcut Collatz is then the already-recorded map `N=8n+1`.

### Exact affine law and sign

Put

\[
A(R,b)=\left({9\over8}\right)^R
       \left({3\over4}\right)^b,
\qquad
c_b=\left({3\over4}\right)^b.
\tag{14}
\]

The intrinsic map satisfies

\[
\boxed{
\mathcal R(Z)=A(R,b)(Z+1)-c_b.}
\tag{15}
\]

Hence

\[
\boxed{
A(R,b)>1\Longrightarrow\mathcal R(Z)>Z,}
\tag{16}
\]

and

\[
\boxed{
A(R,b)<1\Longrightarrow\mathcal R(Z)\le Z.}
\tag{17}
\]

Equality in (17) repeats the complete intrinsic state and therefore lies on a
periodic orbit.  On a nonperiodic orbit the inequality is strict.  With

\[
\kappa={\log(4/3)\over\log(9/8)},
\tag{18}
\]

this is the exact sign law

\[
\operatorname{sgn}(\mathcal R(Z)-Z)
=
\operatorname{sgn}(R-\kappa b)
\tag{19}
\]

away from a periodic equality.

### Proof

At an exact block state put

\[
Z=(p-4)/4.
\tag{20}
\]

The first equation of (1) gives

\[
Z=3^aX,
\qquad
Z+1=8^RU,
\tag{21}
\]

so the first two valuation tests recover `a,R,X,U` uniquely.  The second bridge
equation recovers `b,Y` uniquely.  After the nonzero block `R`,

\[
p_1-4=3(9^RU-1)=3\,4^bY.
\tag{22}
\]

Every following zero block multiplies `p-4` by `3/4`.  After `b-1` such blocks,

\[
p_{\rm next}-4=4\,3^bY,
\tag{23}
\]

which proves (9)--(12).  Every infinite H orbit has infinitely many nonzero
block letters; an eventual all-zero tail would make `p-4` equal
`(3/4)^j` times one fixed nonzero integer for all `j`.  This proves (13).

Substitute `Z+1=8^RU` and (8) into (9):

\[
\begin{aligned}
\mathcal R(Z)
&={3^b\over4^b}(9^RU-1)\\
&=\left({9\over8}\right)^R
  \left({3\over4}\right)^b(Z+1)
  -\left({3\over4}\right)^b,
\end{aligned}
\]

proving (15).  If `A>1`, both terms in

\[
\mathcal R(Z)-Z=(A-1)(Z+1)+(1-c_b)
\tag{24}
\]

are positive.  If `A<1`, then `mathcal R(Z)<Z+1`; integrality gives (17).
The equality and nonperiodicity statements follow because `Z` uniquely
recovers all data.  QED.

---

## L-9530: exact predecessor and source test

**Claim ID:** `L-9530`  
**Title:** The intrinsic renewal map has at most one predecessor, given by one ternary valuation test  
**Status:** `PROPOSED`  
**Dependencies:** `L-9529`

Let `Z` lie in the domain of `mathcal R` and write

\[
Z=3^aX,
\qquad X\equiv5\pmod6.
\tag{25}
\]

Form

\[
T=4^aX+1,
\qquad m=v_3(T).
\tag{26}
\]

Then `Z` has an exact positive renewal predecessor if and only if all of the
following hold:

1. `m` is a positive even integer, say
   \[
   m=2R_-;
   \tag{27}
   \]
2. with
   \[
   U_-={T\over9^{R_-}},
   \qquad
   Z_-=8^{R_-}U_--1,
   \tag{28}
   \]
   one has
   \[
   a_-=v_3(Z_-)\ge1,
   \qquad
   X_-={Z_-\over3^{a_-}}\equiv5\pmod6.
   \tag{29}
   \]

When these conditions hold, the predecessor is unique and

\[
\boxed{\mathcal R(Z_-)=Z.}
\tag{30}
\]

Its renewal type is `(a_-,R_-,a)`.

### Proof

A predecessor must satisfy the bridge ending at the current core `X`:

\[
4^aX+1=9^{R_-}U_-.
\tag{31}
\]

Because `3` does not divide `U_-`, the valuation in (26) must be exactly the
even integer `2R_-`, proving necessity and uniqueness of (27)--(28).  The
predecessor renewal height is then forced to be `Z_-`.  It is a legal renewal
height exactly under (29).

Conversely, (27)--(29) imply `U_-=1 mod 4`, because `a>=1` makes the numerator
in (26) equal to one modulo four and `9^(R_-)=1 mod 4`.  Moreover

\[
Z_-+1=8^{R_-}U_-,
\qquad
9^{R_-}U_--1=4^aX.
\tag{32}
\]

The two exact valuations in the intrinsic decoder are therefore `3R_-` and
`2a`, and its output is `3^aX=Z`.  QED.

---

## T-9519: minimal-survivor source gate

**Claim ID:** `T-9519`  
**Title:** A least nonperiodic renewal survivor must expand forward but has no expanding predecessor  
**Status:** `PROPOSED`  
**Dependencies:** `L-9529`, `L-9530`  
**Scope:** conditional on existence of a nonperiodic infinite positive H orbit

Suppose nonperiodic infinite renewal orbits exist, and choose the least positive
starting height `Z_0` among all of them.  Decode its current type as

\[
(a_0,R_0,b_0).
\tag{33}
\]

Then

\[
\boxed{R_0>\kappa b_0.}
\tag{34}
\]

If the exact predecessor test of `L-9530` succeeds and its nonzero letter is
`R_-`, then

\[
\boxed{R_-\le\kappa a_0.}
\tag{35}
\]

Thus a least counterexample must lie in one explicit arithmetic source gate:
it expands at its first forward renewal, but its unique possible predecessor is
absent or locally nonexpanding.

### Proof

The next height is itself the start of a nonperiodic infinite orbit.  Minimality
rules out a smaller next height, while equality would repeat the intrinsic
state and make the orbit periodic.  Hence `mathcal R(Z_0)>Z_0`, and (34) follows
from (19).

If a predecessor exists and `R_->kappa a_0`, the predecessor sign law makes
`Z_-<Z_0`.  Its forward orbit reaches `Z_0` and is therefore nonperiodic and
infinite, contradicting the choice of `Z_0`.  This proves (35).  QED.

---

## R-9510: what the intrinsic compression does and does not solve

**Claim ID:** `R-9510`  
**Title:** Trusted renewal metadata has been eliminated, but ordinary infinite definedness remains the sole gate  
**Status:** `PROPOSED`

The intrinsic map removes the type/counter redundancy of `ITERATION_11`:
`Z` itself recovers every valuation, bridge core, zero-room length, next state,
and possible predecessor.  An unconditional counterexample certificate can now
begin with one written positive integer `Z_0` and one induction proving that the
three valuation tests in `L-9529` recur forever.

This does not make a finite trajectory, a source state, a compatible `Z_2`
point, or a long renewal chain into a counterexample.  The exact remaining
obligation is still all-time ordinary definedness.

---

## X-9510: intrinsic decoder and predecessor audit

The exact standard-library audit enumerates

\[
1\le a,R,b\le18,
\qquad
0\le k\le127.
\tag{36}
\]

For all

\[
746,496
\tag{37}
\]

ordinary type/counter states it checks:

1. type/counter reconstruction agrees with the intrinsic `Z` decoder;
2. the predecessor formula in `L-9530` returns the original `Z` after one
   forward step;
3. the intrinsic next-renewal test agrees with the `ITERATION_11` counter
   decoder;
4. no positive renewal cycle occurs in the bounded replay.

The frozen totals are

\[
\begin{array}{l|r}
\text{states}&746,496\\
\text{defined next renewals}&35,551\\
\text{states with no predecessor}&699,847\\
\text{states with an expanding predecessor}&24\\
\text{maximum exact renewal life}&5.
\end{array}
\tag{38}

The maximizing tested state has

\[
(a,R,b,k)=(11,1,16,121),
\qquad
Z=4,423,817,593,825,817,031,
\tag{39}
\]

and exits after five renewals.  This is finite negative evidence only.

Semantic digest:

```text
2934e2bbe9fb0291581f22fe6495774eab3db1c88907d96632d2d49ff7134af2
```

Canonical JSON file digest:

```text
8ea3beb09b306044cc15dfbd23e91df41f61427fe4a77d4d20f4662a8b50e830
```

---

## Q-9514: one-integer unconditional counterexample atom

**Claim ID:** `Q-9514`  
**Title:** Find one positive intrinsic renewal height whose decoder is defined forever  
**Status:** `IDEA`

The complete negative objective is now:

\[
\boxed{
\text{Exhibit one }Z_0\in\mathbb Z_{>0}
\text{ such that }\mathcal R^j(Z_0)
\text{ is defined for every }j\ge0.}
\tag{40}
\]

The corresponding explicit H seed and shortcut-Collatz seed are

\[
\boxed{n_0={4Z_0\over3},}
\qquad
\boxed{N_0=8n_0+1.}
\tag{41}

A valid certificate must give one finite `Z_0` and an ordinary inductive
invariant proving, at every iterate:

1. positive ternary valuation and residual class `5 mod 6`;
2. `v_2(Z+1)` is a positive multiple of three;
3. the second valuation is a positive even integer with residual class
   `5 mod 6`;
4. positivity and nontermination.

No future type word, completed `2`-adic address, or trusted carry metadata is
allowed.  A positive solution of (40) is an unconditional H counterexample and,
through `L-9501`, an unconditional Collatz counterexample.
