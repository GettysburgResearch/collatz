# T-9808 -- Stage tolls decode the full word and leave finitely many rooms

Claim ID: `T-9808`
Title: The positive stage toll is a lossless dyadic code, so at most `4^256` fixed rooms can support eventual corrected-stage tails
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: branch-qualified `PR3/L-0031`, `T-0033`, and contextual `T-0036` at `c37e96efd0dcc9dd610d59041234dc57e74090fd`
Scope: eventual positive ordinary tails in the stabilized corrected 256-transition phase-34 stage architecture
Related counterexample candidates: none

## Setup

Fix a scale `m>=12`, put `B=2^m`, and use the corrected heights

\[
t_{m,j}=B+j{B\over256}
\qquad(0\le j\le256).
\tag{1}
\]

The four stabilized types have pairwise distinct dyadic toll exponents:

\[
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)=(0,1,2,3),
\qquad
(\beta_0,\beta_1,\beta_2,\beta_3)=(2,3,2,1).
\tag{2}
\]

For `0<=k<=256`, extend the prefix exponents of `PR3/L-0031` by

\[
U_{m,k}
=11\sum_{r=1}^{k}(t_{m,r}+1),
\tag{3}
\]

so `U_(m,0)=0` and

\[
U_{m,256}=\mathcal E_m
={8459\over2}B+2816.
\tag{4}
\]

For `0<=k<256`, put

\[
V_{m,k}
=7\sum_{r=k+1}^{255}(t_{m,r}+1).
\tag{5}
\]

For a stage word

\[
w=(i_0,\ldots,i_{255})\in\{0,1,2,3\}^{256},
\tag{6}
\]

its positive toll is

\[
\boxed{
\mathcal T_m(w)
=\sum_{k=0}^{255}
2^{U_{m,k}+\alpha_{i_k}}
3^{V_{m,k}+\beta_{i_k}}.
}
\tag{7}
\]

The branch-qualified scaled-tail equation is

\[
\boxed{
2^{\mathcal E_m}W_{m+1}
=3^{\mathcal A_m}W_m+\mathcal T_m(w_m),
}
\tag{8}
\]

where

\[
\mathcal A_m={5369\over2}B+1792.
\tag{9}
\]

## Theorem 1 -- every toll prefix is a lossless dyadic code

For `1<=q<=256`, the residue

\[
\boxed{
\mathcal T_m(w)\pmod {2^{U_{m,q}}}
}
\tag{10}
\]

determines exactly the prefix `(i_0,...,i_(q-1))`.  In particular, the map

\[
\boxed{
w\longmapsto
\mathcal T_m(w)\pmod {2^{\mathcal E_m}}
}
\tag{11}
\]

is injective on all `4^256` stage words.

### Explicit decoder

Let `Z_0` be the residue in (10), viewed modulo `2^(U_(m,q))`.  Once the
first `k` letters have been decoded, subtract their exact toll terms and put

\[
Z_k
=\left[
\mathcal T_m(w)
-\sum_{r=0}^{k-1}
2^{U_{m,r}+\alpha_{i_r}}
3^{V_{m,r}+\beta_{i_r}}
\right]_{2^{U_{m,q}}}.
\tag{12}
\]

Then, for every `0<=k<q`,

\[
\boxed{
i_k=\nu_2(Z_k)-U_{m,k}.
}
\tag{13}
\]

Thus the decoder uses one valuation and one exact subtraction per letter.

### Proof

The gap between consecutive prefix exponents is

\[
U_{m,k+1}-U_{m,k}
=11(t_{m,k+1}+1)>3.
\tag{14}
\]

After the first `k` terms have been removed, the `k`-th remaining term has
valuation `U_(m,k)+alpha_(i_k)`, while every later term is divisible by
`2^(U_(m,k+1))`.  Equation (14) makes the first valuation unique, so reduction
modulo `2^(U_(m,q))` preserves it and proves (13).

Equivalently, if two prefixes first differ at `k`, the difference of their
`k`-th toll terms has valuation

\[
U_{m,k}+\min\{\alpha_{i_k},\alpha_{i'_k}\}
<U_{m,k+1},
\tag{15}
\]

because the two `alpha` values are distinct and all powers of three are odd.
Every later difference is divisible by `2^(U_(m,k+1))`, so it cannot cancel
(15).  The two residues in (10) are distinct. **QED**

## Theorem 2 -- the incoming boundary word determines the stage word

Define the `4^256` incoming residue addresses

\[
\boxed{
\rho_m(w)
=\left[-3^{-\mathcal A_m}\mathcal T_m(w)
\right]_{2^{\mathcal E_m}}.
}
\tag{16}
\]

Here `3^(-mathcal A_m)` denotes the inverse of `3^(mathcal A_m)` modulo the
displayed dyadic modulus.

They are pairwise distinct.  Every valid ordinary stage satisfies

\[
\boxed{
W_m\equiv\rho_m(w_m)\pmod {2^{\mathcal E_m}}.
}
\tag{17}
\]

Consequently, `W_m mod 2^(mathcal E_m)` determines the whole 256-symbol word
`w_m`.  It also supplies a recognition algorithm: multiply the incoming
residue by `-3^(mathcal A_m)` and apply (12)--(13).

### Proof

The factor `3^(mathcal A_m)` is a unit modulo `2^(mathcal E_m)`, so
Theorem 1 makes the addresses in (16) distinct.  Reducing (8) modulo
`2^(mathcal E_m)` gives

\[
3^{\mathcal A_m}W_m+\mathcal T_m(w_m)\equiv0
\pmod {2^{\mathcal E_m}},
\tag{18}
\]

which is exactly (17). **QED**

## Theorem 3 -- at most `4^256` fixed rooms support eventual tails

Let `mathscr C` be the set of positive real numbers `C` for which there is an
eventual positive ordinary corrected-stage tail and a scale `m_0(C)` such that

\[
\boxed{
W_m=\lfloor C H_m\rfloor
\qquad(m\ge m_0(C)),
}
\tag{19}
\]

with the `PR3/T-0033` homogeneous scale

\[
H_m
={3^{a_m}\over2^{e_m}},
\quad
a_m={5369\over2}2^m+1792m,
\quad
e_m={8459\over2}2^m+2816m.
\tag{20}
\]

Then

\[
\boxed{
\#\mathscr C\le4^{256}=2^{512}.
}
\tag{21}
\]

Moreover, one room determines at most one eventual boundary-word and
stage-word tail.  Consequently the set of eventual tails, modulo deletion of
a finite initial segment, also has cardinality at most `4^256`.

### Proof

The exact inequalities

\[
{84\over53}<\log_2 3<{8\over5}
\tag{22}
\]

follow respectively from `L-0025` and `3^5<2^8`.  The lower bound gives

\[
\log_2H_m
>{2669\over106}2^m+{1280\over53}m,
\tag{23}
\]

so `H_m` tends to infinity.  The upper bound gives

\[
\log_2H_m
<{657\over10}2^m+{256\over5}m.
\tag{24}
\]

Combining (4) and (24),

\[
\boxed{
\mathcal E_m-\log_2H_m
>{20819\over5}2^m+2816-{256\over5}m
\longrightarrow+\infty.
}
\tag{25}
\]

Suppose for contradiction that `mathscr C` contains `4^256+1` distinct
rooms `C_1,...,C_(4^256+1)`.  Put

\[
K=1+\max_j C_j,
\qquad
d=\min_{r\ne s}|C_r-C_s|>0.
\tag{26}
\]

Choose one scale `m` beyond all their starting scales and so large that

\[
K H_m<2^{\mathcal E_m},
\qquad
H_m^{-1}<d.
\tag{27}
\]

This is possible by (23) and (25).  For every selected room, (19) and (27)
give

\[
0\le W_m<2^{\mathcal E_m}.
\tag{28}
\]

Equations (17) and (28) therefore force `W_m` to equal one of the `4^256`
least residues `rho_m(w)`.  Hence all the rooms lie in the union of the
`4^256` half-open intervals

\[
\boxed{
I_m(w)
=\left[
{\rho_m(w)\over H_m},
{\rho_m(w)+1\over H_m}
\right).
}
\tag{29}
\]

Every interval has diameter `H_m^(-1)<d`, so it contains at most one of the
chosen rooms.  The `4^256` intervals cannot contain `4^256+1` rooms.  This
contradiction proves (21).

Finally, a fixed `C` determines every boundary word through (19), and
Theorem 2 determines the stage word at every sufficiently late scale.  Thus
two valid tails with the same room are eventually identical in both sets of
coordinates. **QED**

## What this advances

- `PR3/L-0031` presents the toll as a positive S-unit sum.  Theorems 1--2 add
  a different structural fact: its separated dyadic valuations make it a
  lossless finite-word code, and the incoming ordinary boundary already
  contains that code.
- `PR3/T-0033` makes every assumed path a shrinking-target orbit of one real
  room, and refreshed `PR3/T-0036` extends that coding to every local boundary.
  Theorem 3 adds a global cardinality theorem absent from both source claims:
  the exceptional room set is finite, not merely null or zero-dimensional.
- The cap-to-correction search no longer branches independently over a stage
  word after `W_m` (or the room) is fixed.  Any joint room/seam state should
  decode the word first and test its 84 seams second.

## Dependency audit

- Equations (1)--(9) are the branch-qualified stabilized table and positive
  stage normal form of `PR3/L-0031`.  The separated-valuation decoding is
  proved here and does not use the S-unit theorem.  The `L-0031` blob is
  unchanged between the initially audited head `3ee981e` and refreshed head
  `c37e96e`.
- The only imported conclusion from `PR3/T-0033` is the conditional floor law
  (19) with the exact scale (20).  Its much smaller positive fractional-defect
  window is not needed for the cardinality bound.  Refreshed `PR3/T-0036`
  independently makes the whole local type sequence a floor-orbit coding but
  does not prove that only finitely many rooms can support such a coding.
- The lower logarithm bound in (22) is the elementary inequality recorded in
  `PR3/L-0025`; the upper bound is proved by `3^5<2^8`.
- No PR #34 seam theorem is a proof dependency.  Those constraints can only
  remove decoded rooms or words.

## Gap and scope audit

- The bound `2^512` is finite but enormous.  It gives neither an effective
  list of the room values nor a decision procedure for their infinite tails.
- The theorem is conditional on the proposed PR #3 positive stage equation
  and fixed-room law.  It does not promote those source claims.
- A finite exceptional set can be nonempty.  No room, ordinary initialization,
  cap stitch, or Collatz counterexample is constructed or excluded.
- Eventual tails with the same room coincide after both enter the corrected
  architecture; distinct finite histories before that scale are not counted.
- The decoder recognizes the source-type word.  It does not by itself prove
  that the decoded word satisfies every connector, collar, and triple seam.

## Adversarial checks

- The proof uses the distinct vector `alpha=(0,1,2,3)`, not the noninjective
  vector `beta=(2,3,2,1)`.
- Reduction is modulo `2^(mathcal E_m)`, the binary exponent in the scaled
  `W` equation, not the residual-stage depth `D_m`.
- Large odd powers of three may wrap modulo the dyadic modulus, but their
  valuations below the modulus are unchanged; the unique first valuation in
  (13) cannot cancel.
- The room count does not assume one uniform upper bound for all possible
  rooms.  The contradiction selects only finitely many rooms, then chooses a
  common `K` and a common late scale.
- Bounded exact replays on shortened four- and six-letter analogues recovered
  every word from its toll residue and found no residue collisions.  These
  checks audit the decoder only; the proof is the valuation separation.

## Suggested next attack

Use (16) to replace the free 256-symbol choice at a fixed scale by the single
incoming residue `floor(C H_m) mod 2^(mathcal E_m)`.  Intersect the decoded
word's head cell from `T-9802`, its 84 PR #34 triple seams, and the exact
connector-prefix interval of `PR3/T-0034`.  Any uniform failure removes one of
only finitely many possible eventual rooms.
