# L-8002 — Exact run-core and quotient-refund normal form for the negative-three-cycle chart

**Claim ID:** `L-8002`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** local `O-8001`; local `L-8004` for the lossless image normalization  
**Scope:** positive ordinary paths in the negative-three-cycle pulse chart

## 1. The exact normalized chart

Local `O-8001` gives the physical coordinate

\[
 h=\frac{n+5}{2}
\]

and the exact block system

\[
 h=8q\longmapsto9q,
 \qquad
 h=3+16q\longmapsto3+9q.
\tag{1}
\]

Both outputs are divisible by three. Therefore every infinite path enters,
after at most one block, the invariant image `h=3z`. Local `L-8004` proves
that the resulting lossless normalized chart is

\[
 \boxed{
 F(z)=
 \begin{cases}
 9z/8,&8\mid z,\\[1mm]
 (9z+7)/16,&z\equiv1\pmod {16},
 \end{cases}}
\tag{2}
\]

with physical shortcut-Collatz state

\[
 \boxed{n=6z-5.}
\tag{3}
\]

Write the branches in (2) as `A` and `B`. Every legal edge is one exact finite
Collatz block; no completion or limiting interpretation occurs.

A finite positive integer cannot follow `A` forever, because each `A` edge
removes three powers of two. Hence every infinite chart path contains
infinitely many `B` edges.

## 2. Maximal-run section

Start immediately after a `B` edge. For the next `B` edge to occur, the state
must have the form

\[
 z=2^{3r}u,
 \qquad r\ge0,
 \qquad u\text{ odd},
\tag{4}
\]

and satisfy

\[
 9^ru\equiv1\pmod {16}.
\tag{5}
\]

Then exactly `r` successive `A` edges occur, followed by one `B`, and

\[
 \boxed{z^+=\frac{9^{r+1}u+7}{16}.}
\tag{6}
\]

Conversely, (4)–(5) imply that `A^rB` is legal and has output (6).

If the next maximal run has length `s`, write

\[
 z^+=2^{3s}u^+,
 \qquad u^+\text{ odd}.
\tag{7}
\]

The exact core recurrence is

\[
 \boxed{2^{4+3s}u^+=9^{r+1}u+7.}
\tag{8}
\]

Every core arising after a completed macro obeys

\[
 \boxed{
 u^+\equiv
 \begin{cases}
 1\pmod {144},&s\text{ even},\\
 89\pmod {144},&s\text{ odd}.
 \end{cases}}
\tag{9}
\]

Indeed, reducing (8) modulo `9` gives `u^+ congruent (-1)^s mod9`; the next
`B` condition gives `u^+ congruent 1 mod16` for even `s` and `9 mod16` for
odd `s`. CRT gives (9).

## 3. One ordinary quotient for every ordered run pair

For `s>=0` put

\[
 M_s=2^{4+3s},
 \qquad
 L_s=16M_s=2^{8+3s},
\tag{10}
\]

and

\[
 b_s=
 \begin{cases}
 1,&s\text{ even},\\
 9,&s\text{ odd}.
 \end{cases}
\tag{11}
\]

Define

\[
 \boxed{
 a_{r,s}=[(M_sb_s-7)9^{-(r+1)}]_{L_s}.}
\tag{12}
\]

It is odd. A current core `u` produces a legal next section of exact run
length `s` if and only if

\[
 \boxed{u\equiv a_{r,s}\pmod {L_s}.}
\tag{13}
\]

The modulus is `16M_s`, not merely `2M_s`: equation (13) simultaneously
forces exact valuation and the following `B` condition.

Write

\[
 u=a_{r,s}+L_sk,
 \qquad k\in\mathbf Z.
\tag{14}
\]

Put

\[
 c_{r,s}=\frac{9^{r+1}a_{r,s}+7}{M_s}.
\tag{15}
\]

Then `c_(r,s) congruent b_s mod16`, and

\[
 \boxed{u^+=c_{r,s}+16\,9^{r+1}k.}
\tag{16}
\]

Thus the entire unbounded freedom remaining after two run labels is one
ordinary quotient `k`.

## 4. Exact three-run refund transition

Fix a prospective following run `t`. Condition (16) lies in the next cylinder
exactly when

\[
 u^+\equiv a_{s,t}\pmod {L_t}.
\tag{17}
\]

Both `c_(r,s)` and `a_(s,t)` are congruent to `b_s mod16`, so define

\[
 \boxed{
 \rho_{r,s,t}=
 \left[
 9^{-(r+1)}\frac{a_{s,t}-c_{r,s}}{16}
 \right]_{M_t}.}
\tag{18}
\]

Then (17) is equivalent to

\[
 \boxed{k\equiv\rho_{r,s,t}\pmod {M_t}.}
\tag{19}
\]

Writing

\[
 k=\rho_{r,s,t}+M_t\ell,
\tag{20}
\]

one obtains

\[
 \boxed{k^+=\sigma_{r,s,t}+9^{r+1}\ell,}
\tag{21}
\]

where

\[
 \sigma_{r,s,t}
 =\frac{c_{r,s}+16\,9^{r+1}\rho_{r,s,t}-a_{s,t}}{L_t}
 \in\mathbf Z.
\tag{22}
\]

Equations (19)–(21) are the exact quotient-refund law. One future cylinder
costs `M_t=2^(4+3t)` in the current quotient, while the unused lift is
transported with odd multiplier `9^(r+1)`.

## 5. Deterministic form

No future run need be supplied externally. From an ordinary state `(r,s,k)`,
form (16), then compute

\[
 v=\nu_2(9^{s+1}u^++7).
\tag{23}
\]

If `v<4`, or `v-4` is not divisible by `3`, or the resulting odd core fails
the next `B` congruence, the chart stops. Otherwise

\[
 t=(v-4)/3
\]

is the unique next run and (21) gives the unique next quotient. Hence the run
labels are outputs of one deterministic partial arithmetic map; they are not a
directive oracle.

## 6. Proof and scope audit

- The normalization `h=3z` is justified by the fact that every output of the
  original `h` chart is divisible by three. It is not an unproved restriction
  to a special initial class.
- Every division by `16` in (18) and (22) is integral because both relevant
  odd cores have the same required residue `b_s mod16`.
- Pairwise finite cylinders do not prove one infinite ordinary path. Infinite
  definedness of the deterministic quotient map is the remaining existence
  obligation.
- The update is multiplicative and uses exact changing-modulus remainders. It
  is outside the additive, fixed-residue one-counter obstruction of
  branch-qualified `PR34/L-9915`.
- Local `L-8004` supplies a further invariant subchart `7|z`, in which the
  core constant simplifies from `+7` to `+1`.

## 7. Suggested next attack

Search for a forward-invariant class in which every emitted run is at least
five. In that region the physical macro is strictly increasing by `T-8002`;
therefore an infinite-definedness certificate alone finishes the
counterexample construction.