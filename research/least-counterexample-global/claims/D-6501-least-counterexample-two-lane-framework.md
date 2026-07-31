# D-6501 — Least-counterexample two-lane framework

**Claim ID:** `D-6501`  
**Title:** A least positive Collatz counterexample lies in one of two coefficient-stopping lanes  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** elementary shortcut-Collatz algebra; branch-qualified PR #76 `T-6707`; branch-qualified PR #77 `T-6709`  
**Scope:** positive ordinary shortcut-Collatz orbits

## 1. Shortcut map and coefficient walk

Put

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

For one positive ordinary orbit

\[
x_k=T^k(n),
\qquad
v_k=x_k\bmod2,
\]

write

\[
q_k=\sum_{i=0}^{k-1}v_i,
\qquad
C_k={3^{q_k}\over2^k}.
\]

Let

\[
\alpha={\log2\over\log3},
\qquad
D_k=q_k-\alpha k,
\]

so that

\[
C_k=3^{D_k}.
\]

The coefficient stopping time is

\[
\tau(n)=\min\{k\ge1:C_k<1\},
\]

with `tau(n)=infinity` when the set is empty.

For every finite parity prefix there is an exact integer `A_k>=0` such that

\[
\boxed{
T^k(n)={3^{q_k}n+A_k\over2^k}
      =C_kn+E_k,
\qquad E_k={A_k\over2^k}.}
\tag{1}
\]

## 2. Least-counterexample no-descent condition

Assume Collatz is false and let `n` be its least positive counterexample. Then

\[
\boxed{x_k\ge n\quad(k\ge0).}
\tag{2}
\]

Indeed, if some iterate were a smaller positive integer, minimality would make that iterate converge to `1`, and therefore the orbit from `n` would also converge.

## 3. Orbit-shape dichotomy

Every positive ordinary orbit has exactly one of the following two eventual shapes.

1. It is eventually periodic.
2. It tends to `+infinity`.

To see this, if an orbit does not tend to infinity, there is a finite bound `B` met infinitely often. Two visits among the finitely many values `1,...,B` coincide, and determinism gives eventual periodicity. Conversely, a nonrepeating positive integer orbit visits every bounded set only finitely often and therefore tends to infinity.

Thus a false Collatz conjecture supplies either:

- a nontrivial positive cycle; or
- an ordinary orbit tending to infinity.

## 4. Exhaustive coefficient lanes

Relative to proposed PR #76 `T-6707` and PR #77 `T-6709`, a least positive counterexample must enter one of the following lanes.

### Lane A — permanent coefficient supercriticality

\[
\boxed{C_k\ge1\quad\text{for every }k.}
\tag{3}
\]

Branch-qualified `T-6709` then gives

\[
\boxed{x_k\longrightarrow+\infty.}
\tag{4}
\]

The open task is to prove that no positive ordinary initial integer can realize `(3)`.

### Lane B — a finite first coefficient crossing

There is a first index `j=tau(n)` such that

\[
C_m\ge1\quad(1\le m<j),
\qquad
C_j<1.
\tag{5}
\]

No descent `(2)` makes the length-`j` prefix paradoxical:

\[
T^j(n)\ge n
\quad\text{despite}\quad
3^{q_j}<2^j.
\tag{6}
\]

Branch-qualified PR #76 `T-6707` currently gives the necessary gate

\[
\boxed{j\ge217\,976\,794\,617.}
\tag{7}
\]

The open task is a cofinal theorem excluding every such first-crossing cylinder, not another finite collection of Farey cells.

A nontrivial positive cycle belongs to Lane B after rotating to its least cycle value: over one full period the positive affine toll forces the period coefficient below one, while every cycle value is at least the rotated minimum.

## 5. What would prove Collatz

A proof of the Collatz conjecture follows after all imported dependencies are independently reconstructed if both statements are proved:

\[
\boxed{
\text{no positive ordinary orbit satisfies Lane A};}
\tag{8}
\]

\[
\boxed{
\text{no positive ordinary first-crossing or cycle cylinder satisfies Lane B}.}
\tag{9}
\]

This is an exhaustive least-counterexample contradiction. It does not begin with a prescribed symbolic directive or a completed `2`-adic point.

## 6. Gap audit

- `D-6501` does not prove either exclusion.
- The numerical threshold `(7)` is branch-qualified to PR #76 and its imported literature.
- Conditional divergence in Lane A is not a contradiction.
- Finite compatibility of Lane-A or Lane-B parity cylinders is automatic and does not provide an ordinary infinite orbit.
- Positive-cycle exclusion still requires the complete finite denominator/replay gate, not only coefficient drift.
