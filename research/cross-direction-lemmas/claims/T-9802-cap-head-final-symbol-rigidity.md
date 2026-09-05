# T-9802 -- Stabilized cap heads split into four rigid dyadic translates

Claim ID: `T-9802`
Title: The final tower symbol translates every stabilized head correction by one of four fixed sixty-fourth-modulus offsets
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave13-cap-head`
Reviewing agents: `gpt56-synthesis-01-wave13-survivor-twohot`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9821` and `L-9898`; frozen `PR3/T-0027`, `L-0016`, and `L-0017`
Scope: the four-symbol head of the frozen corrected phase-`-34` stage at every stabilized scale `m>=12`
Related counterexample candidates: none

## Setup

Put

\[
B=2^m,
\qquad
d=B/256,
\qquad
t_j=B+jd
\quad(0\le j\le3),
\tag{1}
\]

and assume `m>=12`.  Use the stabilized finite-core constants of `L-9898`,

\[
(p_0,p_1,p_2,p_3)=(5,30,20,56),
\qquad
(b_0,b_1,b_2,b_3)=(9,54,36,24).
\tag{2}
\]

For `0<=j<=2`, write

\[
n_j=3^{7(t_j+1)}.
\tag{3}
\]

For the two head transitions put

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

For a word

\[
\tau=(\iota_0,\iota_1,\iota_2,\iota_3)
\in\{0,1,2,3\}^4,
\tag{5}
\]

let `X_j,Y_j,C_j,F`, and `r^H_m(tau)` be the exact stabilized connector
quantities of `L-9898` and `L-9821`.  Thus `X_j,Y_j` connect
`iota_j@t_j` to `iota_(j+1)@t_(j+1)`,

\[
C_j={Y_j-X_{j+1}\over64}
\quad(j=0,1),
\tag{6}
\]

\[
F=n_1C_0+q_0C_1,
\qquad
r^H_m(\tau)=[-FP^{-1}]_Q.
\tag{7}
\]

Finally define the exact cell width

\[
\mathcal C_m={Q\over64}.
\tag{8}
\]

## Statement 1 -- exact final-symbol translation law

Fix the first three symbols `(a,b,c)`.  For `k in {0,1,2,3}`, abbreviate

\[
r_k=r^H_m(a,b,c,k).
\tag{9}
\]

Then

\[
\boxed{
r_k=
\left[r_0+\kappa_k\mathcal C_m\right]_Q,
\qquad
(\kappa_0,\kappa_1,\kappa_2,\kappa_3)=(0,3,53,1).
}
\tag{10}
\]

The four translations are independent of `m` and of `(a,b,c)`.  In
particular, the final symbol supplies only a rigid six-bit cell translation;
it does not create a fourth independent inverse-power stream.

## Statement 2 -- complete cell and small-word classification

Write the base correction uniquely as

\[
r_0=\mathcal C_m A+U,
\qquad
0\le A<64,
\qquad
0\le U<\mathcal C_m.
\tag{11}
\]

Then all four corrections have the same within-cell remainder:

\[
\boxed{
r_k
=
\mathcal C_m[A+\kappa_k]_{64}+U.
}
\tag{12}
\]

Consequently, for every real threshold `0<H<=C_m`, at most one final symbol
can satisfy `r_k<H`.  More exactly,

\[
r_k<H
\quad\Longleftrightarrow\quad
[A+\kappa_k]_{64}=0
\ \hbox{ and }\ U<H.
\tag{13}
\]

The only possible base-cell/final-symbol pairs are

\[
\boxed{
(A,k)\in\{(0,0),(61,1),(11,2),(63,3)\}.
}
\tag{14}
\]

This also classifies exact zeros: `r_k=0` if and only if its pair occurs in
(14) and `U=0`.  Thus there is at most one zero in each final-symbol quartet,
although the theorem does not assert that a zero occurs.

## Statement 3 -- three quarters of all head words have a uniform exponential lower bound

The four cell indices in (12) are distinct.  Therefore at least three
members of every quartet satisfy

\[
\boxed{
r_k\ge\mathcal C_m={Q\over64}.
}
\tag{15}
\]

Since

\[
Q=2^{D^{(H)}_m},
\qquad
D^{(H)}_m={5687\over256}B+22,
\tag{16}
\]

(15) is the explicit lower bound

\[
\boxed{
r_k\ge
2^{(5687/256)2^m+16}
}
\tag{17}
\]

for at least `3*4^3=192` of the 256 stabilized head words at every
`m>=12`.

## Statement 4 -- consequence for every hypothetical cap chain

Suppose the conditional cap-chain hypotheses of `L-9821` hold.  That lemma
gives the head cusp

\[
r^H_m(\tau)<2^{h_{m,0}}
\tag{18}
\]

at every sufficiently late scale and proves

\[
D^{(H)}_m-h_{m,0}\longrightarrow+\infty.
\tag{19}
\]

Hence, after increasing the eventual threshold if necessary,

\[
2^{h_{m,0}}\le2^{D^{(H)}_m-6}=\mathcal C_m.
\tag{20}
\]

Equations (13)--(14) now imply

\[
\boxed{
\#\{\tau\in\{0,1,2,3\}^4:
r^H_m(\tau)<2^{h_{m,0}}\}
\le64.
}
\tag{21}
\]

More strongly, once the first three symbols are fixed, the top six-bit cell
`A` in (11) either forbids all four final symbols or determines the unique
possible final symbol by (14).  The remaining unresolved datum is only the
within-cell remainder `U`.

## Proof

Only the last connector `X_2` depends on the final symbol `k`.  Formula
`L-9898/(8)` gives

\[
X_2(c,k)
=
\left[(q_1p_k-b_c)n_2^{-1}\right]_{64q_1}.
\tag{22}
\]

Subtract the case `k=0`.  Modulo `64q_1`,

\[
X_2(c,k)-X_2(c,0)
\equiv
q_1(p_k-p_0)n_2^{-1}.
\tag{23}
\]

Both connector values are congruent to `p_c` modulo 64, so their difference
is divisible by 64.  Dividing (23) by 64 therefore gives, modulo `q_1`,

\[
{X_2(c,k)-X_2(c,0)\over64}
\equiv
{q_1\over64}(p_k-p_0)n_2^{-1}.
\tag{24}
\]

The quantities `C_0` and `Y_1` are already fixed by `(a,b,c)`.  Equations
(6)--(7) and (24) yield

\[
F_k-F_0
\equiv
-{Q\over64}(p_k-p_0)n_2^{-1}
\pmod Q.
\tag{25}
\]

Multiplying by `-P^{-1}` gives

\[
r_k-r_0
\equiv
{Q\over64}(p_k-p_0)n_2^{-1}P^{-1}
\pmod Q.
\tag{26}
\]

Because `m>=12`, each of `t_0,t_1,t_2` is divisible by 16.  The order of
3 modulo 64 is 16, so

\[
n_2\equiv3^7\equiv11\pmod {64},
\qquad
n_2^{-1}\equiv35\pmod {64},
\tag{27}
\]

while

\[
P\equiv3^{14}\equiv57\pmod {64},
\qquad
P^{-1}\equiv9\pmod {64}.
\tag{28}
\]

Thus

\[
n_2^{-1}P^{-1}\equiv35\cdot9\equiv59\pmod {64}.
\tag{29}
\]

Using (2),

\[
59(p_k-p_0)\pmod {64}
=
(0,3,53,1),
\tag{30}
\]

in final-symbol order `k=0,1,2,3`.  Since multiplication of a coefficient
by `Q/64` depends only on that coefficient modulo 64, equations (26)--(30)
prove the least-residue identity (10).

Euclidean division of `r_0` by `C_m` proves (11).  Translation by an integral
number of cells leaves the within-cell remainder unchanged and reduces the
cell index modulo 64, proving (12).  The four offsets in (10) are distinct.
For `H<=C_m`, a value in `[0,H)` must lie in cell zero, which proves
(13)--(15).  Equation (16) is `L-9821/(19)`, so (17) follows.  Finally,
`L-9821/(20)` proves (19), and (18)--(20) let us apply the just-proved
classification at every sufficiently late cap-chain scale.  This proves
(21). **QED**

## What this advances

- It gives a symbolic, all-stabilized-scale theorem rather than extrapolating
  the finite seam failures at scales 12 and 13.
- It proves the target lower bound `Q/64` for at least 192 of the 256 head
  words at every scale.
- It reduces the only potentially cusp-admissible words to at most one final
  symbol for each three-symbol prefix.
- It identifies the exact remaining object: 64 within-cell inverse-power
  remainders `U`, rather than 256 unrelated full head corrections.

## Dependency audit

- `L-9898` supplies the corrected stabilized core table, connector formula
  (22), the local constants (6), and the two-transition head composition
  (7).  The proof rederives the required final-symbol dependence directly;
  its finite seam enumeration is not used.
- Frozen `PR3/L-0016` and `L-0017` are the underlying source of the four core
  anchors and canonical mixed-radix connectors.  Frozen `PR3/T-0027`
  supplies the corrected height schedule.
- `L-9821` supplies only the cap-chain cusp consequence (18)--(20), whose
  completion-height input ultimately comes from branch-qualified
  `PR33/T-9704`, `L-9703`, `T-9703`, and `L-9702`.
- Statements 1--3 are unconditional inside the frozen stabilized head
  algebra.  Only Statement 4 assumes a hypothetical cap chain.

## Gap audit

- The theorem does not bound the exceptional within-cell remainder `U` away
  from zero.  Up to 64 words remain, so no lower bound for `L^H_m` and no cap
  exclusion follows.
- Exact zero is classified but not excluded.  Proving `U>0`, let alone an
  exponential lower bound for `U`, remains a native truncated-inverse-power
  problem.
- The offsets are proved for `m>=12`, where all four finite cores have
  stabilized modulo 64.  No assertion is made for earlier scales.
- The branch-qualified cap inputs and the frozen collision schedule remain
  proposed interfaces.  No marked initialization or Collatz conclusion is
  claimed.

## Adversarial checks

- The corrected type-three core `(p_3,b_3)=(56,24)` is used in (2).
- The offset order `(0,3,53,1)` is the final-symbol order `(0,1,2,3)`, not
  sorted cell order.
- Circular wrap at cell 64 is retained in (12); it is exactly why the four
  possible base cells in (14) are `0,61,11,63`.
- Exact integer replay of all 64 prefix quartets at each of `m=12` and
  `m=13` recovered (10) for all 256 words at each scale.  These bounded
  checks audit the symbolic proof and are not extrapolated.
- Memory snapshots before and after the bounded replays ranged from 25.3 to
  26.8 percent used (at least 11.27 GiB free); no large-scale or full-stage
  enumeration was performed.

## Suggested next attack

For each three-symbol prefix, study the within-cell remainder

\[
U_m(a,b,c)
=
r^H_m(a,b,c,0)\bmod {Q\over64}.
\tag{31}
\]

Only prefixes whose six-bit cell lies in `{0,61,11,63}` can matter.  A lower
bound

\[
U_m(a,b,c)\ge2^{h_{m,0}}
\tag{32}
\]

on those exceptional scale classes would finish the head-cusp obstruction;
all other words are already excluded by (15).
