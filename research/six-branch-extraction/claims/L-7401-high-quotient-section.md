# L-7401 — Exact high-quotient section and immediate language exit

Claim ID: `L-7401`  
Title: Every two-step legal root has a high quotient whose first canonical digit lies outside the six-branch alphabet  
Status: `PROPOSED`  
Authoring agent: `gpt56-extraction-01`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: `D-7401`  
Scope: the direct ordinary quotient `floor(x/Q)` in the six-branch system  
Related counterexample candidates: none

## Statement

Use the source/output data of `D-7401`. If a positive root begins with types

\[
i\longrightarrow j,
\]

write

\[
x=r_i+Qk,
\qquad
F(x)=c_i+Pk=r_j+Qk'.
\]

Then

\[
\boxed{Qk'=Pk+c_i-r_j.}
\]

The canonical first digit of the ordinary high quotient `k` is

\[
\boxed{b_{ij}=[c_i-r_j]_Q.}
\]

The complete matrix `(b_(ij))`, with rows indexed by the current type and columns by the next type, is

\[
\begin{pmatrix}
4024&491448&384440&1912&292464&357191\\
41391&4527&421807&39279&329831&394558\\
149859&112995&5987&147747&438299&503026\\
6165&493589&386581&4053&294605&359332\\
235937&199073&92065&233825&89&64816\\
177480&140616&33608&175368&465920&6359
\end{pmatrix}.
\]

None of these 36 digits lies in

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

Consequently:

\[
\boxed{
 x\in S_2
 \quad\Longrightarrow\quad
 \left\lfloor{x\over Q}\right\rfloor\notin S_1.}
\]

In particular, the canonical base-`Q` high quotient is never a smaller root of the same restricted language.

## Proof

Substituting `x=r_i+Qk` into the first branch gives

\[
F(x)=c_i+Pk.
\]

If the next type is `j`, write this output as `r_j+Qk'`; subtraction gives the displayed quotient recurrence. The canonical digit of `k` is

\[
[-Pk]_Q=[c_i-r_j]_Q.
\]

For a compact exact disjointness check, reduce modulo `2048`. The allowed alphabet reduces to

\[
\{0,1536,960,824,1695\}.
\]

The quotient-digit matrix reduces to

\[
\begin{pmatrix}
1976&1976&1464&1912&1648&839\\
431&431&1967&367&103&1342\\
355&355&1891&291&27&1266\\
21&21&1557&2005&1741&932\\
417&417&1953&353&89&1328\\
1352&1352&840&1288&1024&215
\end{pmatrix},
\]

whose entries avoid the allowed residue set. Therefore no `b_(ij)` is in `A`. ∎

## Motivation

The most natural ordinary extraction attempt is recursive: remove the first canonical `Q`-block, prove that the smaller high quotient belongs to the same survivor language, and iterate. This lemma proves that this route fails at the first possible step for every one of the 36 transition pairs.

## Dependency audit

Only the exact source/output table of `D-7401` is used.

## Gap audit

- Failure of direct quotient closure does not prove that the original least roots diverge.
- A richer nonlinear or infinite-state section could still preserve the language.
- The table is exhaustive for its 36 exact cases; it is not a bounded experiment extrapolated to later depths.

## Adversarial tests

- Every ordered pair `i -> j` is relevant because every finite word has positive ordinary representatives.
- The quotient digit is the canonical digit `[-Pk]_Q`, not the base-`Q` digit `k mod Q`; these must not be conflated.
- Disjointness modulo `2048` is sufficient for disjointness modulo `Q=2^19`.

## Remaining uncertainty

The section tree beyond this first quotient is genuinely infinite-state; this lemma does not classify it.

## Suggested next attack

Any recursive extraction must use information richer than the ordinary quotient alone. The exact global alternative remains a uniform bound for the original least roots or a proof that they escape.