# L-8002 — Exact run-core and quotient-refund normal form for the negative-three-cycle chart

**Claim ID:** `L-8002`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** local `O-8001` for the exact physical block chart  
**Scope:** positive ordinary paths in the negative-three-cycle pulse chart

## 1. The exact chart

Local `O-8001` gives the partial map

\[
F(z)=
\begin{cases}
9z/8,&8\mid z,\\[1mm]
(9z+7)/16,&z\equiv1\pmod {16},
\end{cases}
\tag{1}
\]

with physical shortcut-Collatz state

\[
 n=6z-5.
\tag{2}
\]

Write the two branches as `A` and `B`, respectively. Every legal chart edge is
one exact finite Collatz block; no completion or limiting interpretation occurs.

A finite positive integer cannot follow `A` forever, because each `A` step lowers
its exact 2-adic valuation by three. Hence every infinite chart path contains
infinitely many `B` edges.

## 2. Maximal-run section

Start immediately after a `B` edge. For the next `B` edge to occur, the state
must have the form

\[
 z=2^{3r}u,
 \qquad r\ge0,
 \qquad u\text{ odd},
\tag{3}
\]

and must satisfy

\[
 9^r u\equiv1\pmod {16}.
\tag{4}
\]

Then exactly `r` successive `A` edges occur, followed by one `B`, and the next
section state is

\[
 \boxed{
 z^+=\frac{9^{r+1}u+7}{16}.}
\tag{5}
\]

Conversely, (3)–(4) imply that the finite block `A^r B` is legal and has output
(5).

If the next maximal run has length `s`, write

\[
 z^+=2^{3s}u^+,
 \qquad u^+\text{ odd}.
\tag{6}
\]

The exact core recurrence is

\[
 \boxed{
 2^{4+3s}u^+=9^{r+1}u+7.}
\tag{7}
\]

Every core arising after a completed macro obeys the fixed congruence

\[
 \boxed{
 u^+\equiv
 \begin{cases}
 1\pmod {144},&s\text{ even},\\
 89\pmod {144},&s\text{ odd}.
 \end{cases}}
\tag{8}
\]

### Proof of (8)

Modulo `9`, equation (7) gives

\[
 2^{4+3s}u^+\equiv7\pmod9.
\]

Since `2^(4+3s) congruent 7(-1)^s mod 9`, this yields

\[
 u^+\equiv(-1)^s\pmod9.
\]

The next `B` legality condition is `9^s u^+ congruent 1 mod 16`. Because
`9^2 congruent 1 mod 16`, this says `u^+ congruent 1 mod 16` for even `s` and
`u^+ congruent 9 mod 16` for odd `s`. CRT gives (8). ∎

## 3. One ordinary quotient for every ordered run pair

For `s>=0` put

\[
 M_s=2^{4+3s},
 \qquad
 L_s=16M_s=2^{8+3s},
\tag{9}
\]

and

\[
 b_s=
 \begin{cases}
 1,&s\text{ even},\\
 9,&s\text{ odd}.
 \end{cases}
\tag{10}
\]

Define the unique residue

\[
 \boxed{
 a_{r,s}=
 \left[(M_s b_s-7)9^{-(r+1)}\right]_{L_s}.}
\tag{11}
\]

It is odd. A current core `u` produces a legal next section of exact run length
`s` if and only if

\[
 \boxed{u\equiv a_{r,s}\pmod {L_s}.}
\tag{12}
\]

Indeed, (12) is exactly

\[
 9^{r+1}u+7\equiv M_s b_s\pmod {16M_s},
\]

which says simultaneously that the quotient in (7) is odd and satisfies the
next `B` condition modulo `16`.

Write

\[
 u=a_{r,s}+L_s k,
 \qquad k\in\mathbf Z.
\tag{13}
\]

Put

\[
 c_{r,s}=\frac{9^{r+1}a_{r,s}+7}{M_s}.
\tag{14}
\]

Then `c_(r,s) congruent b_s mod 16`, and the next core is

\[
 \boxed{
 u^+=c_{r,s}+16\,9^{r+1}k.}
\tag{15}
\]

Thus the entire unbounded freedom remaining after the two run labels is one
ordinary integer quotient `k`.

## 4. Exact three-run refund transition

Fix a prospective following run `t`. The condition that (15) lie in the next
cylinder is

\[
 u^+\equiv a_{s,t}\pmod {L_t}.
\tag{16}
\]

Both `c_(r,s)` and `a_(s,t)` are congruent to `b_s mod 16`, so define

\[
 \boxed{
 \rho_{r,s,t}=
 \left[
 9^{-(r+1)}\frac{a_{s,t}-c_{r,s}}{16}
 \right]_{M_t}.}
\tag{17}
\]

Then (16) is equivalent to

\[
 \boxed{k\equiv\rho_{r,s,t}\pmod {M_t}.}
\tag{18}
\]

Writing

\[
 k=\rho_{r,s,t}+M_t\ell,
\tag{19}
\]

one obtains

\[
 \boxed{
 k^+=\sigma_{r,s,t}+9^{r+1}\ell,}
\tag{20}
\]

where

\[
 \sigma_{r,s,t}
 =\frac{c_{r,s}+16\,9^{r+1}\rho_{r,s,t}-a_{s,t}}{L_t}
 \in\mathbf Z.
\tag{21}
\]

Equations (18)–(20) are the exact quotient-refund law. One future cylinder costs
`M_t=2^(4+3t)` in the current quotient, while the unused lift is transported
with odd multiplier `9^(r+1)`.

## 5. Deterministic form

No future run need be supplied externally. From an ordinary state `(r,s,k)`,
form (15), then compute

\[
 v=\nu_2(9^{s+1}u^++7).
\]

If `v<4`, or `v-4` is not divisible by `3`, or the resulting odd core fails the
next `B` congruence, the chart stops. Otherwise

\[
 t=(v-4)/3
\]

is the unique next run and `(20)` gives the unique next quotient. Hence the
run labels are outputs of one deterministic partial arithmetic map; they are
not a directive oracle.

## 6. Proof audit

- The modulus in (11) is `16 M_s`, not merely `2 M_s`: exact valuation alone
  would not guarantee the next `B` edge.
- All divisions by `16` in (17) and (21) are integral because both relevant
  odd cores have the same required residue `b_s mod 16`.
- Pairwise finite cylinders do not prove one infinite ordinary path. Infinite
  definedness of the deterministic quotient map is the remaining existence
  obligation.
- The update is multiplicative and uses exact changing-modulus remainders. It
  is outside the additive, fixed-residue one-counter obstruction of branch-
  qualified `PR34/L-9915`.

## 7. Suggested next attack

Search for a forward-invariant class in which every emitted run is at least
five. In that region the physical macro map is strictly increasing by
`T-8002`; therefore an infinite-definedness certificate alone would finish the
counterexample construction.