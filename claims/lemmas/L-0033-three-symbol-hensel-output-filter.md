# L-0033 — Three-symbol Hensel output filter

Claim ID: `L-0033`  
Title: A three-symbol scaled-tail prefix has one canonical input and at most one admissible fourth type  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0028`, `L-0031`  
Scope: stabilized phase-`-34` tower types at scales `m >= 12`  
Related counterexample candidates: none

## Setup

Put

\[
d=2^{m-8},
\qquad
t_j=(256+j)d
\quad(0\le j\le3).
\tag{1}
\]

For the four stabilized types use

\[
p=(5,30,20,56),
\qquad
b=(9,54,36,24).
\tag{2}
\]

Write

\[
T_j=2^{11(t_j+1)},
\qquad
N_j=3^{7(t_j+1)}.
\tag{3}
\]

For a three-symbol prefix `(a,b,c)`, define

\[
\boxed{
M_m=T_1T_2T_3
=2^{U_m},
\qquad
U_m={4257\over128}2^m+33,}
\tag{4}
\]

\[
\boxed{N_m=N_0N_1N_2,}
\tag{5}
\]

and the positive three-step toll

\[
\boxed{
\tau_m(a,b,c)
=N_1N_2 b_a+T_1N_2 b_b+T_1T_2 b_c.}
\tag{6}
\]

The scaled-tail recurrence of `L-0031` composes to

\[
M_m W_3=N_m W_0+\tau_m(a,b,c).
\tag{7}
\]

## Statement 1 — canonical three-symbol address

Define

\[
\boxed{
\rho_m(a,b,c)
=
[-\tau_m(a,b,c)N_m^{-1}]_{M_m},}
\tag{8}
\]

where brackets denote the least nonnegative residue and the inverse is taken
modulo the displayed power of two.

Then:

1. `0 <= rho_m(a,b,c) < M_m`;
2. starting from `W_0=rho_m(a,b,c)`, all three local divisions in (7) are
   integral;
3. the canonical three-step output
   \[
   \boxed{
   \sigma_m(a,b,c)
   ={N_m\rho_m(a,b,c)+\tau_m(a,b,c)\over M_m}}
   \tag{9}
   \]
   is a nonnegative ordinary integer.

The 64 addresses in (8) are pairwise distinct.

### Proof

Equation (8) is exactly the complete composite divisibility condition.  The
odd multipliers and dyadic local radices satisfy the path-domain equivalence of
`L-0028`, so complete divisibility is equivalent to integrality at every local
step.

For distinct prefixes, let `k` be the first differing symbol.  In the positive
toll, the first unequal terms have binary valuations

\[
U_{m,k}+\alpha_{i_k},
\qquad
U_{m,k}+\alpha_{i'_k},
\]

where the four `alpha` values are `0,1,2,3`.  Their difference has valuation
strictly below `U_(m,k+1)`, while all later terms are divisible by
`2^(U_(m,k+1))`.  No cancellation is possible.  Multiplication by the odd unit
`N_m^(-1)` preserves distinctness.  This proves all assertions. ∎

## Statement 2 — six-bit Hensel lift gives the fourth type

Lift (8) by six bits:

\[
\widehat\rho_m(a,b,c)
=
[-\tau_m(a,b,c)N_m^{-1}]_{64M_m}.
\tag{10}
\]

Write uniquely

\[
\boxed{
\widehat\rho_m
=ho_m+M_m h_m,
\qquad
0\le h_m<64.}
\tag{11}
\]

Then the canonical output obeys

\[
\boxed{
\sigma_m(a,b,c)
\equiv-N_m h_m(a,b,c)\pmod {64}.}
\tag{12}
\]

Consequently the prefix has a physically admissible fourth tower type exactly
when

\[
\boxed{
[-N_mh_m(a,b,c)]_{64}
\in\{5,30,20,56\}.}
\tag{13}
\]

When (13) holds, the fourth type is unique.

### Proof

There is an integer `q` with

\[
N_m\widehat\rho_m+\tau_m=64M_mq.
\]

Substituting (11) and comparing with (9) gives

\[
\sigma_m=64q-N_mh_m,
\]

which is (12).  The four residues in (13) are distinct, proving uniqueness. ∎

## Statement 3 — exact completion-height demand

If a fixed-room trajectory of `T-0033` uses the prefix `(a,b,c)` at scale `m`,
then

\[
\boxed{
W_m=\rho_m(a,b,c).}
\tag{14}
\]

Moreover, for every fixed room `C > 0`, the address must lie in the
exponentially small initial part of its full dyadic cylinder:

\[
\boxed{
\log_2 {M_m\over \rho_m(a,b,c)+1}
>
{35913\over5248}2^m
-{1024\over41}m
-O_C(1).}
\tag{15}
\]

### Proof

`T-0033` gives `W_m=floor(C H_m)`.  The elementary bound
`log_2(3)<65/41` gives

\[
\log_2 H_m
<{1083\over41}2^m+{1024\over41}m.
\]

Since

\[
U_m={4257\over128}2^m+33
\]

and

\[
{4257\over128}-{1083\over41}
={35913\over5248}>0,
\]

one has `C H_m < M_m` for every sufficiently large scale.  The stage
congruence therefore identifies the ordinary integer itself with the least
address, proving (14).  The same inequalities give (15). ∎

## Interpretation

The room problem is not a search over four independent symbols.  Three symbols
select one canonical ordinary input, and one six-bit Hensel carry either
selects a unique fourth type or rejects the prefix.

The unresolved all-scale problem is now explicit: control the moving six-bit
block `h_m(a,b,c)` while the required address simultaneously acquires a high
zero block of length `Theta(2^m)` from (15).

## Gap audit

- This lemma does not prove that the allowed set in (13) is eventually empty.
- The six-bit block is the top block of a growing inverse lift; its transition
  is not a bounded-state recurrence.
- A finite audit of (13) is not an all-scale theorem.
- No room, marked initialization, or counterexample is constructed.