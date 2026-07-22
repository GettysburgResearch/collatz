# T-9806 -- Stabilized cap heads have an exact two-level dyadic cell hierarchy

Claim ID: `T-9806`
Title: The last two tower symbols occupy sixteen distinct cells above one common within-cell remainder
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Reviewing agents: `gpt56-synthesis-01-wave14-quant-fresh-primes`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9802`, `L-9821`, and `L-9898`; frozen `PR3/L-0016`, `L-0017`, and `T-0027`
Contextual interface: local `T-9808`
Scope: the four-symbol head of the frozen corrected phase-`-34` stage at every stabilized scale `m>=12`
Related counterexample candidates: none

## Setup

Use the notation and corrected stabilized core table of `T-9802`.  Thus

\[
B=2^m,
\qquad
d=B/256,
\qquad
t_j=B+jd
\quad(0\le j\le3),
\tag{1}
\]

\[
(p_0,p_1,p_2,p_3)=(5,30,20,56),
\qquad
(b_0,b_1,b_2,b_3)=(9,54,36,24),
\tag{2}
\]

and

\[
n_j=3^{7(t_j+1)}\quad(0\le j\le2),
\tag{3}
\]

\[
q_0=2^{11(t_2+1)},
\qquad
q_1=2^{11(t_3+1)},
\qquad
P=n_0n_1,
\qquad
Q=q_0q_1.
\tag{4}
\]

For a head word `(a,b,c,k)`, let

\[
r_{c,k}=r^H_m(a,b,c,k)
=\left[-F_{c,k}P^{-1}\right]_Q
\tag{5}
\]

be the canonical input correction of `L-9821/(25)`.  Throughout the claim,
the first two symbols `(a,b)` are fixed.  Define the second-level cell width

\[
\mathcal W_m={q_0\over64},
\tag{6}
\]

the odd unit

\[
u_m=\left[(n_2P)^{-1}\right]_{64q_1},
\tag{7}
\]

and, for `0<=c,k<=3`,

\[
\Delta b_c=b_c-b_0,
\qquad
\Delta p_k=p_k-p_0,
\tag{8}
\]

\[
\omega_{c,k}
=\left[u_m(q_1\Delta p_k-\Delta b_c)\right]_{64q_1}.
\tag{9}
\]

## Statement 1 -- exact two-level translation law

Write the base correction uniquely as

\[
r_{0,0}=\mathcal W_mJ+V,
\qquad
0\le J<64q_1,
\qquad
0\le V<\mathcal W_m.
\tag{10}
\]

Then every choice of the last two symbols satisfies

\[
\boxed{
r_{c,k}
=\mathcal W_m[J+\omega_{c,k}]_{64q_1}+V.
}
\tag{11}
\]

Thus, after `(a,b)` is fixed, all sixteen corrections have exactly the same
within-`mathcal W_m` remainder.  The third and final symbols change only the cell
index in the cyclic group `Z/(64q_1)Z`.

This refines the `Q/64` cells of `T-9802`: since

\[
{Q\over64}=q_1\mathcal W_m,
\tag{12}
\]

the final symbol moves among the sixty-four coarse cells, whereas the third
symbol moves within and across their `q_1` second-level cells.

## Statement 2 -- the two symbols occupy complementary six-bit directions

Put

\[
\delta_c=[-u_m\Delta b_c]_{64q_1},
\qquad
\kappa_k=[u_m\Delta p_k]_{64}.
\tag{13}
\]

Then

\[
\boxed{
\omega_{c,k}=[\delta_c+q_1\kappa_k]_{64q_1}.
}
\tag{14}
\]

At every stabilized scale,

\[
u_m\equiv59\pmod {64},
\tag{15}
\]

so the final-symbol offsets are exactly those of `T-9802`,

\[
\boxed{
(\kappa_0,\kappa_1,\kappa_2,\kappa_3)=(0,3,53,1),
}
\tag{16}
\]

while the lowest six bits of the third-symbol offsets are

\[
\boxed{
(\delta_0,\delta_1,\delta_2,\delta_3)
\equiv(0,33,7,11)\pmod {64}.
}
\tag{17}
\]

In particular, `k` is invisible in the lowest six bits of the second-level
cell index because `64` divides `q_1`, while the four choices of `c` have
four distinct lowest-six-bit signatures.  The higher bits of `delta_c`
remain genuine truncated inverse-power data; (17) does not assert that they
stabilize.

## Statement 3 -- exact small-threshold and zero classification

The sixteen offsets `omega_(c,k)` are pairwise distinct modulo `64q_1`.
Consequently, for every real threshold `0<H<=mathcal W_m`,

\[
\boxed{
r_{c,k}<H
\quad\Longleftrightarrow\quad
[J+\omega_{c,k}]_{64q_1}=0
\ \hbox{and}\ V<H.
}
\tag{18}
\]

For each fixed `(a,b)`, at most one of the sixteen choices `(c,k)` can
satisfy (18).  Globally over all 256 head words,

\[
\boxed{
\#\{(a,b,c,k):r^H_m(a,b,c,k)<H\}\le16
\qquad(0<H\le\mathcal W_m),
}
\tag{19}
\]

and at least 240 head corrections obey

\[
\boxed{r^H_m(a,b,c,k)\ge\mathcal W_m.}
\tag{20}
\]

The same statement includes exact zeros: there are at most sixteen zero
head corrections at any stabilized scale.  No assertion is made that a zero
actually occurs.

## Statement 4 -- why this hierarchy does not yet sharpen the cap cusp

The second-level width has exact logarithmic size

\[
\log_2\mathcal W_m
=11(t_2+1)-6
={1419\over128}B+5.
\tag{21}
\]

Under the conditional cap-chain hypotheses of `L-9821`, the head threshold
is `2^(h_(m,0))`, where

\[
h_{m,0}
=\left\lceil
{161341\over10496}B+{1024\over41}m+K_M
\right\rceil.
\tag{22}
\]

Since

\[
{161341\over10496}-{1419\over128}
={44983\over10496}>0,
\tag{23}
\]

we have

\[
h_{m,0}-\log_2\mathcal W_m
\ge
{44983\over10496}B+{1024\over41}m+K_M-5
\longrightarrow+\infty.
\tag{24}
\]

Therefore the actual cap cusp is eventually exponentially *wider* than one
`mathcal W_m` cell.  The bound (19) cannot be substituted into `L-9821/(27)`, and
this claim does not reduce the current conditional count of 64
cusp-admissible head words from `T-9802`.  Its gain is the exact hierarchy,
the sharper zero classification, and a precise identification of the next
inverse-power datum.

## Proof

Let `X_j,Y_j` be the canonical connector integers of `L-9898`.  For the
connector from `b@t_1` to `c@t_2`, the exact identity is

\[
n_1X_1+b_b=q_0Y_1.
\tag{25}
\]

Using `C_0=(Y_0-X_1)/64`, `C_1=(Y_1-X_2)/64`, and
`F=n_1C_0+q_0C_1`, telescope the internal connector:

\[
\begin{aligned}
64F_{c,k}
&=n_1(Y_0-X_1)+q_0(Y_1-X_2)\\
&=n_1Y_0+b_b-q_0X_2(c,k).
\end{aligned}
\tag{26}
\]

The first two terms in the last line depend only on `(a,b)`.  Hence

\[
F_{c,k}-F_{0,0}
=-{q_0\over64}\bigl(X_2(c,k)-X_2(0,0)\bigr).
\tag{27}
\]

The stabilized connector formula gives

\[
X_2(c,k)
\equiv(q_1p_k-b_c)n_2^{-1}pmod {64q_1}.
\tag{28}
\]

Multiplying (27) by `-P^(-1)` and using `Q=q_0q_1` proves

\[
r_{c,k}-r_{0,0}
\equiv
\mathcal W_m u_m(q_1\Delta p_k-\Delta b_c)
\pmod Q.
\tag{29}
\]

Because `Q/W_m=64q_1`, Euclidean division (10) turns (29) into the exact
least-residue formula (11).  Separating the two summands in (9) proves
(14).

For `m>=12`, each of `t_0,t_1,t_2` is divisible by 16.  Since 3 has order
16 modulo 64,

\[
n_0n_1n_2\equiv(3^7)^3\equiv51\pmod {64},
\qquad
51^{-1}\equiv59\pmod {64},
\tag{30}
\]

which proves (15).  Substitution of (2) into (13) gives (16)--(17).

It remains to prove that the offsets are distinct.  If
`omega_(c,k)=omega_(c',k')` modulo `64q_1`, cancel the odd unit `u_m` in
(9) and reduce first modulo `q_1`:

\[
b_c-b_{c'}\equiv0\pmod {q_1}.
\tag{31}
\]

The four values `b_c` are distinct and their pairwise differences have
absolute value below `q_1`, so `c=c'`.  Dividing the remaining congruence by
`q_1` gives

\[
p_k-p_{k'}\equiv0\pmod {64}.
\tag{32}
\]

The four values `p_k` are distinct modulo 64, so `k=k'`.  Formula (11) now
proves (18)--(20).  Finally, (21)--(24) are direct substitutions from (1),
(6), and `L-9821/(7)`. **QED**

## What this advances

- It replaces 64 apparently unrelated within-coarse-cell remainders by 16
  blocks, one for each first-symbol pair, each with one common remainder and
  sixteen explicit cyclic translates.
- It separates the two rightmost symbols into complementary directions:
  the final symbol supplies the coarse six-bit shift, while the third symbol
  has a distinct low-six-bit second-level signature.
- It improves the unconditional exact-zero bound from at most 64 in
  `T-9802` to at most 16.
- Under the room decoder of `T-9808`, the symbols `(a,b,c,k)` are not a free
  alphabet: a room supplies one decoded head, and (11) gives its exact
  two-level cell test.  The present cusp width is too large for that test to
  delete a room by itself.
- It shows exactly why this extra algebra does not by itself improve the
  present cap-chain count: the newly exposed cell is below, not above, the
  known cusp height.

## Dependency audit

- `L-9898/(8)--(12)` supplies the corrected connector formula, connector
  identity, and local constants used in (25)--(28).  The proof rederives the
  complete dependence on `(c,k)` and does not use its finite seam tables.
- `T-9802` supplies the stabilized head notation and independently agrees
  with the final-symbol quotient `(0,3,53,1)`; (26)--(30) rederive that
  quotient inside the finer hierarchy.
- `L-9821` is used only in Statement 4 to compare the new width with the
  conditional cap cusp.  Statements 1--3 are unconditional inside the
  frozen stabilized head algebra.
- Frozen `PR3/L-0016` and `L-0017` underlie the four core anchors and exact
  connector identity; frozen `PR3/T-0027` supplies the corrected height
  schedule.  No later unfrozen source formula is imported.
- `T-9808` is contextual only: its incoming-boundary decoder explains how
  to apply this hierarchy to a fixed room, but no theorem here depends on
  its room-finiteness conclusion.

## Gap audit

- The higher bits of `delta_c`, equivalently the residues of small odd
  multiples of `(n_0n_1n_2)^(-1)` modulo `q_1`, are not bounded away from
  the cusp.  This is the remaining native truncated-inverse-power problem.
- Because `h_(m,0)-log_2(mathcal W_m)` grows linearly in `2^m`, the small-threshold
  count (19) is not an all-late cap exclusion and does not further filter
  the at most 64 coarse-cell heads from `T-9802` under the presently known
  height bound, even when the ambient word is decoded from a `T-9808` room.
- Exact zeros are narrowed to at most sixteen but are not excluded.
- The result applies only for `m>=12`, after the four finite cores stabilize.
  No marked initialization or Collatz conclusion is claimed.

## Adversarial checks

- The corrected type-three core `(p_3,b_3)=(56,24)` is used in both offset
  vectors.
- The factor in (27) is `q_0/64`, not `q_1/64`: the internal connector
  cancellation leaves the right boundary `X_2`, while the second residual
  denominator multiplies it.
- The inverse in (7) contains all three odd factors `n_0n_1n_2`; omitting
  `n_2` changes both six-bit vectors.
- Circular wrap is retained in (11) and (14).  Pairwise distinctness is in
  `Z/(64q_1)Z`, not an assertion that the integer representatives are
  monotonically ordered.
- Separate exact-integer replays at bounded stabilized scales `m=12` and
  `m=13` reconstructed all 256 connector corrections and recovered (11),
  the common remainders, and all sixteen distinct cells in each `(a,b)`
  block.  The proof does not extrapolate those tables.

## Suggested next attack

For the at most four coarse-cell survivors in each fixed `(a,b)` block,
study the higher quotient and lower `q_1` residue of

\[
\delta_c
=\left[-(b_c-b_0)(n_0n_1n_2)^{-1}\right]_{64q_1}.
\tag{33}
\]

A useful next theorem must control an interval of width
`2^(h_(m,0))/mathcal W_m`, whose logarithm has leading coefficient
`44983/10496`; merely resolving any fixed number of additional low bits
cannot reach the present cap cusp.
