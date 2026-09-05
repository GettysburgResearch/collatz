# T-9825 -- The cap base-cell chart freezes one low bit per scale

Claim ID: `T-9825`
Title: The base cell and connector word lie on a fixed affine 2-adic line through \(m-6\) bits, with parity controlling the first boundary bit
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave14-period-ten`; `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local T-9820 and T-9817; stabilized head notation from T-9806; frozen corrected PR #3 connector algebra used by T-9820
Scope: every stabilized phase-34 head at scale \(m\ge12\), for all sixteen first-symbol pairs
Related counterexample candidates: none

## Setup

Put

\[
 d_m=2^{m-8},
 \qquad
 t_{m,j}=(256+j)d_m
 \qquad(0\le j\le3),
\tag{1}
\]

and

\[
 N_{m,j}=3^{7(t_{m,j}+1)},
 \qquad
 T_{m,j}=2^{11(t_{m,j}+1)}.
\tag{2}
\]

As in T-9820, write

\[
 P_m=N_{m,0}N_{m,1},
 \qquad
 M_m=64T_{m,3}.
\tag{3}
\]

For a fixed first-symbol pair \((a,b)\), let \(J_m(a,b)\),
\(Z_m(a,b)\), and \(X_{m,2}\) be the base cell, scaled connector word,
and base \(0@t_{m,2}\) to \(0@t_{m,3}\) connector of T-9820.  Its two
exact source identities are

\[
 \boxed{
 P_mJ_m(a,b)\equiv X_{m,2}-Z_m(a,b)\pmod {M_m},
 }
\tag{4}
\]

and

\[
 \boxed{
 N_{m,2}X_{m,2}
 \equiv T_{m,3}p_0-b_0\pmod {M_m},
 \qquad
 (p_0,b_0)=(5,9).
 }
\tag{5}
\]

Define the scale-independent 2-adic units

\[
 C=-9\cdot3^{-7}\in\mathbf Z_2^\times,
 \qquad
 \beta=3^{14},
 \qquad
 r_m=m-6.
\tag{6}
\]

Every negative power of \(3\) below is taken in \(\mathbf Z_2^\times\),
or equivalently reduced in the indicated finite dyadic quotient.

## Theorem 1 -- exact coefficient stabilization and its first failure

For every \(m\ge12\),

\[
 \boxed{
 \bigl(
 \nu_2(N_{m,0}-3^7),
 \nu_2(N_{m,1}-3^7),
 \nu_2(N_{m,2}-3^7),
 \nu_2(N_{m,3}-3^7)
 \bigr)
 =
 (m+2,m-6,m-5,m-6).
 }
\tag{7}
\]

In particular, all four odd factors have the common stable prefix

\[
 N_{m,j}\equiv3^7\pmod {2^{r_m}}
 \qquad(0\le j\le3).
\tag{8}
\]

The two-factor coefficient has the sharp valuation

\[
 \boxed{
 \nu_2(P_m-3^{14})=r_m.
 }
\tag{9}
\]

Consequently its first nonstable bit is universal:

\[
 \boxed{
 P_m\equiv3^{14}+2^{r_m}
 \pmod {2^{r_m+1}}.
 }
\tag{10}
\]

The base right connector is stable one bit farther:

\[
 \boxed{
 X_{m,2}\equiv C
 \pmod {2^{r_m+1}}.
 }
\tag{11}
\]

### Proof

Factor

\[
 N_{m,j}-3^7
 =3^7\left(3^{7t_{m,j}}-1\right).
\tag{12}
\]

Every \(t_{m,j}\) is even.  The elementary \(2\)-adic LTE identity gives

\[
 \nu_2\left(3^{7t_{m,j}}-1\right)
 =
 \nu_2(3-1)+\nu_2(3+1)+\nu_2(7t_{m,j})-1
 =
 2+\nu_2(t_{m,j}).
\tag{13}
\]

The schedule has

\[
 \bigl(
 \nu_2(t_{m,0}),
 \nu_2(t_{m,1}),
 \nu_2(t_{m,2}),
 \nu_2(t_{m,3})
 \bigr)
 =
 (m,m-8,m-7,m-8),
\tag{14}
\]

because \(256,257,258,259\) have respective valuations
\(8,0,1,0\).  Equations (12)--(14) prove (7)--(8).

Next,

\[
 P_m
 =3^{14}3^{7(t_{m,0}+t_{m,1})},
 \qquad
 t_{m,0}+t_{m,1}=513d_m.
\tag{15}
\]

Since \(513\) is odd, the same LTE calculation gives

\[
 \nu_2(P_m-3^{14})
 =
 2+\nu_2(513d_m)
 =
 m-6=r_m.
\tag{16}
\]

This proves (9).  Dividing \(P_m-3^{14}\) by \(2^{r_m}\) leaves an odd
integer, so its residue modulo \(2\) is one.  This is exactly (10).

Finally,

\[
 \nu_2(T_{m,3})
 =11(259d_m+1)>m-5=r_m+1.
\tag{17}
\]

Equation (7) gives \(N_{m,2}\equiv3^7\pmod {2^{r_m+1}}\).
Reduce (5) modulo \(2^{r_m+1}\); the \(T_{m,3}p_0\) term vanishes and
the odd coefficient is invertible.  Therefore

\[
 X_{m,2}
 \equiv-9N_{m,2}^{-1}
 \equiv-9\cdot3^{-7}
 =C
 \pmod {2^{r_m+1}},
\tag{18}
\]

which proves (11). **QED**

## Theorem 2 -- a growing fixed affine code and its boundary bit

At every stabilized scale and for every \((a,b)\),

\[
 \boxed{
 Z_m(a,b)
 \equiv C-\beta J_m(a,b)
 \pmod {2^{r_m}}.
 }
\tag{19}
\]

Equivalently,

\[
 \boxed{
 J_m(a,b)
 \equiv
 -9\cdot3^{-21}-3^{-14}Z_m(a,b)
 \pmod {2^{r_m}}.
 }
\tag{20}
\]

Because both slopes are odd, (19)--(20) are inverse affine
permutations of \(\mathbf Z/2^{r_m}\mathbf Z\).  Thus the first \(m-6\)
bits of \(J_m(a,b)\) and \(Z_m(a,b)\) contain exactly the same
same-scale information.

The first bit beyond this stable affine prefix is not free.  It is controlled
exactly by the parity of the base cell:

\[
 \boxed{
 Z_m(a,b)
 \equiv
 C-\beta J_m(a,b)+2^{r_m}J_m(a,b)
 \pmod {2^{r_m+1}}.
 }
\tag{21}
\]

Equivalently, the 2-adic integer

\[
 \mathcal D_m(a,b)
 =
 {Z_m(a,b)-C+\beta J_m(a,b)\over2^{r_m}}
\tag{22}
\]

satisfies

\[
 \boxed{
 \mathcal D_m(a,b)
 \equiv J_m(a,b)
 \equiv Z_m(a,b)+1
 \pmod2.
 }
\tag{23}
\]

### Proof

The exponent of \(M_m\) is much larger than \(r_m+1\), so (4) may be
reduced at either precision used below.  Modulo \(2^{r_m}\), equations
(8), (11), and (4) give

\[
 Z_m(a,b)
 \equiv X_{m,2}-P_mJ_m(a,b)
 \equiv C-\beta J_m(a,b),
\tag{24}
\]

which is (19).  Multiplication by the odd inverse
\(\beta^{-1}=3^{-14}\) gives (20).

At precision \(2^{r_m+1}\), substitute (10)--(11) into (4):

\[
 \begin{aligned}
 Z_m(a,b)
 &\equiv C-(\beta+2^{r_m})J_m(a,b)\\
 &\equiv C-\beta J_m(a,b)+2^{r_m}J_m(a,b)
 \pmod {2^{r_m+1}}.
 \end{aligned}
\tag{25}
\]

The last sign may be changed because
\(2\cdot2^{r_m}J_m\) is divisible by \(2^{r_m+1}\).
Equation (25) proves (21), shows that (22) is integral in
\(\mathbf Z_2\), and gives its first congruence in (23).  Reducing
(19) modulo \(2\), where \(C\) and \(\beta\) are odd, gives
\(Z_m\equiv J_m+1\pmod2\), proving the second. **QED**

## Corollary -- only one lane can cancel three growing-carry bits

For the four joint connector coefficients of T-9820,

\[
 H_{m,c}(a,b)
 =
 T_{m,3}p_0-b_c-N_{m,2}Z_m(a,b),
\tag{26}
\]

where

\[
 (b_0,b_1,b_2,b_3)=(9,54,36,24),
\tag{27}
\]

the growing affine code gives

\[
 \boxed{
 H_{m,c}(a,b)
 \equiv
 3^{21}J_m(a,b)+9-b_c
 \pmod {2^{r_m}}.
 }
\tag{28}
\]

Hence, for every \(1\le k\le r_m\),

\[
 \boxed{
 2^k\mid H_{m,c}(a,b)
 \quad\Longleftrightarrow\quad
 J_m(a,b)\equiv(b_c-9)3^{-21}\pmod {2^k}.
 }
\tag{29}
\]

Uniformly in \(m,a,b\),

\[
 \boxed{
 \#\{c:2^k\mid H_{m,c}\}
 \le
 \begin{cases}
 3,&k=1,\\
 2,&k=2,\\
 1,&3\le k\le r_m.
 \end{cases}
 }
\tag{30}
\]

Thus at most one third-symbol lane can cancel three or more bits of the
growing Newton carry from T-9820/Theorem 2.  At least three lanes lose at
most two carry bits, while the parity dichotomy of T-9820 still forces one
or three lanes to lose none.

### Proof

Modulo \(2^{r_m}\), equation (17) kills the first term in (26).
Equations (8) and (19) then give

\[
 N_{m,2}Z_m
 \equiv
 3^7(C-\beta J_m)
 =
 -9-3^{21}J_m.
\tag{31}
\]

Substitution proves (28), and multiplication by \(3^{-21}\) proves (29).

For fixed \(J_m\), simultaneous divisibility on two lanes requires the
corresponding \(b_c\) values to agree modulo \(2^k\).  Their residues are

\[
 \begin{array}{c|rrrr}
 c&0&1&2&3\\ \hline
 b_c\bmod2&1&0&0&0\\
 b_c\bmod4&1&2&0&0\\
 b_c\bmod8&1&6&4&0.
 \end{array}
\tag{32}
\]

The largest fiber sizes are therefore \(3,2,1\) at precisions
\(2,4,8\).  Distinctness modulo \(8\) persists at every higher dyadic
precision, proving (30). **QED**

## What this advances

- T-9820 fixed the affine chart only modulo \(64\).  Equations (19)--(20)
  extend the same scale-independent chart through \(m-6\) bits, one
  additional bit whenever the scale increments.
- Equation (21) identifies the first coefficient-stabilization failure
  exactly: it contributes no new state beyond the already known parity of
  \(J_m\), equivalently the opposite parity of \(Z_m\).
- Equations (28)--(30) strengthen the joint-carry conclusion of T-9820.
  Large cancellation cannot occur on several third-symbol lanes: at most
  one lane can erase three or more Newton-carry bits.
- Combining (30) with `T-9820/(27)` gives a twelve-bit universal-fiber
  consequence.  At every transition at least three lanes have `h<=2`, hence
  `Delta_m-h>=12`.  On each such lane the image contains
  `2^(Delta_m-h-12)` distinct joint-cell corrections in every one of the 4096
  top-twelve blocks.  Multiplication by `H` has a `2^h`-element kernel on the
  full compatible-lift fiber, so each block has `2^(Delta_m-12)` original
  lift preimages.  This applies to the live PR #3 two-block filter after the
  affine crosswalk below, but does not assert branching of the distinguished
  source.
- Any low-bit cap or room decoder at precision at most \(m-6\) may use one
  fixed affine coordinate rather than transporting separate base-cell and
  connector-word coordinates or scale-dependent coefficients.

## Dependency, novelty, and source audit

- T-9820 supplies the exact identities (4)--(5), the definitions of
  \(J_m,Z_m,X_{m,2},H_{m,c}\), and the fixed-modulo-\(64\) endpoint.
  The present claim does not rederive its connector telescoping.
- T-9817 supplies the corrected stabilized schedule (1), while T-9806
  supplies the common cap-head notation.  The needed schedule and
  coefficient definitions are restated in (1)--(3).
- The only arithmetic input beyond those identities is elementary LTE for
  \(3^n-1\) with even \(n\).  No equidistribution, transcendence, or
  finite-computation theorem is used.
- The valuation vector (7), sharp product boundary (9)--(10), growing
  fixed-coefficient affine code (19)--(23), and lane bound (30) are new.
  T-9802 records only \(P_m\equiv3^{14}\pmod {64}\); T-9817 normalizes the
  three-factor inverse; T-9820 records only the fixed six-bit affine chart.
- The corrected connector formulas used by T-9820 are frozen at PR #3 source
  head `c37e96efd0dcc9dd610d59041234dc57e74090fd`; comparison through live
  `PR3` head `537e1cab2e8dacc444e973e730daa463273bab6f` found those source files
  unchanged.  New `PR3/L-0033` and `T-0039` give the exact contextual
  crosswalk
  `h_(L0033)=A_m+25 mod64`,
  `q_(T0039)=floor(64ell_m/T_3)`, and
  `64A_m+q_(T0039)=floor(s_(m,c)/(T_3/64))`.  Their allowed-output/zero-input
  test is therefore an affine labeling of the top twelve joint-cell bits.
  Equations (19)--(23) control the least-significant `m-6` bits, separated
  from that moving window by exponentially many unknown bits.
- Live `PR33/T-9705` separately proposes universal ordinary exclusion for the
  complete frozen stage class at
  `c9d62bce3e93f5785f72e4520bc576863d9379eb` through a connector-free
  Evertse argument.  It is neither used nor audited here.  If that external
  proof chain survives review, it supersedes the need for a low-bit
  room-pruning proof in that frozen class; it does not contradict the
  same-scale identities above.
- Notation is fenced across the live packets: this claim's integral connector
  `Z_m` is neither the real defect digit `Z_n` of `PR3/L-0034` nor the physical
  scaled boundary `Z_j` of `PR33/L-9704`; `h_(L0033)` is an output digit, not
  the valuation `h=nu_2(H)` used in the carry count.

## Gap and scope audit

- This is strictly a same-scale theorem.  It gives no relation from
  \(J_m\) to \(J_{m+1}\), from \(Z_m\) to \(Z_{m+1}\), or between their
  distinguished source carries.
- The stable width \(m-6\) grows only linearly in \(m\), whereas the cap
  modulus has \(2849\cdot2^{m-8}+17\) bits.  The room filter samples the
  moving top six bits, so (19) alone gives no cofinal survivor avoidance.
- Sharpness of (9) means the coefficient \(P_m\) itself does not retain the
  fixed slope one bit farther.  For an individual pair with even \(J_m\),
  the correction in (21) can vanish; no claim of pairwise sharpness is made.
- The lane bound (30) restricts cancellation multiplicity, not which lane
  is decoded by an actual room.  It proves neither a room-pruning theorem
  nor a cap-stitch transition.
- Even the 4096-value two-block conclusion above belongs to the universal
  compatible-lift information model.  The actual source chooses one correlated
  carry and may still avoid almost every abstract lift.
- The symbols \(3^{-7},3^{-14},3^{-21}\) denote 2-adic units, not real
  negative powers used in an archimedean estimate.
- No bounded computation is extrapolated, and no cap chain, fixed room,
  marked initialization, or Collatz conclusion is proved or refuted.

## Exact and adversarial checks

- Direct modular replay for every \(12\le m\le24\) verified the four LTE
  endpoints (7), the exact first product bit (10), and the connector residue
  (11).  These checks are redundant with the proof.
- At \(m=12\), \(r_m=6\), and

\[
 C\equiv5,
 \qquad
 \beta\equiv57,
 \qquad
 3^{-14}\equiv9,
 \qquad
 -9\cdot3^{-21}\equiv45
 \pmod {64}.
\tag{33}
\]

  Thus (19)--(20) recover exactly T-9820/(36)--(37).
- The bottleneck is \(N_{m,1}\), not \(N_{m,2}\): equation (7) gives the
  latter one additional stable bit, which is exactly why \(X_{m,2}\) is
  valid at the boundary precision used in (21).
- The plus sign on the correction in (21) is intentional.  Its direct
  derivation gives \(-2^{r_m}J_m\), and the two signs are identical modulo
  \(2^{r_m+1}\).
- Equation (30) includes a possible zero coefficient \(H_{m,c}=0\);
  treating its valuation as infinite does not change the divisibility
  count.

## Suggested next attack

Derive a source-specific transition for either \(J_m(a,b)\) or
\(Z_m(a,b)\) after conjugating by the fixed affine chart (19).  The present
result removes coefficient drift from a linearly growing low-bit window and
shows that its first boundary bit is already known, but a useful cap
recurrence must still transport the exponentially moving high window sampled
by the room quotient.
