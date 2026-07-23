# L-8251 — Nine-B two-place synchronizer and the maximal common prime-to-six boundary residue

**Claim ID:** `L-8251`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-23  
**Last updated:** 2026-07-23  
**Issue:** #52  
**Dependencies:** branch-qualified PR #51 `O-8001`, `L-8004`, and `T-8003` for the physical chart and the nine-run growth gate  
**Scope:** the invariant divisible-seven run core, grouped from one high run to the next across eight intervening zero runs  
**Related counterexample candidates:** none

## Statement

Use the verified normalized chart

\[
A:z=8q\longmapsto 9q,
\qquad
B:z=1+16q\longmapsto1+9q,
\qquad
n=6z-5.
\tag{1}
\]

Inside the invariant `7|z` subchart, write a section state as

\[
z=7\,2^{3r}v,
\qquad
r\ge0,
\qquad
v>0\text{ odd}.
\tag{2}
\]

After the `r` consecutive `A` edges, the state immediately before `B` is

\[
p=7\,9^r v.
\tag{3}
\]

Assume that nine consecutive `B` edges are legal, equivalently

\[
p\equiv1\pmod {16^9},
\tag{4}
\]

and define the ordinary boundary coordinate

\[
\boxed{
W=\frac{p-1}{16^9}.}
\tag{5}
\]

Then `W` is a positive integer and

\[
W\equiv-1\equiv6\pmod7.
\tag{6}
\]

Let `s>=0`. The following are equivalent.

1. After the nine `B` edges, the exact next high run has length `s`, and after those `s` `A` edges the next pre-`B` state again has the form `1+16^9 W'` for an integer `W'`.
2. The integer

   \[
   9^s(1+9^9W)-2^{3s}
   \tag{7}
   \]

   is divisible by \(2^{3s+36}\).

When these conditions hold,

\[
\boxed{
F_s(W)=W'
=
\frac{9^s(1+9^9W)-2^{3s}}
     {2^{3s+36}}.}
\tag{8}
\]

Moreover,

\[
\nu_2(1+9^9W)=3s,
\qquad
W'\equiv6\pmod7,
\qquad
9^s\mid1+16^9W'.
\tag{9}
\]

The final divisibility is automatic from `(18)`: the current run's entire power of `3` is refunded into the next boundary rather than becoming another free constraint.

Thus one high run, eight zero runs, and the following high run are compressed into one exact partial map on one ordinary integer.

Now put

\[
\boxed{
D_9=16^9-9^9=68\,332\,056\,247}
\tag{10}
\]

and let

\[
\boxed{
\omega=37\,933\,813\,917}
\tag{11}
\]

be the unique residue modulo \(D_9\) satisfying

\[
9^9\omega+1\equiv0\pmod {D_9}.
\tag{12}
\]

Because \(16^9\equiv9^9\pmod {D_9}\), the same residue also satisfies

\[
16^9\omega+1\equiv0\pmod {D_9}.
\tag{13}
\]

For every `s>=0` and every defined branch `(8)`,

\[
\boxed{
W\equiv\omega\pmod {D_9}
\quad\Longrightarrow\quad
F_s(W)\equiv\omega\pmod {D_9}.}
\tag{14}
\]

The prime-to-`6` modulus factors as

\[
D_9=7\cdot13\cdot19\cdot37\cdot163\cdot6553.
\tag{15}
\]

Finally, \(D_9\) is maximal in the following exact sense.

> Let `M` be odd and coprime to `3`. Suppose one residue `eta mod M` is fixed modulo `M` by two consecutive branch formulas \(F_q,F_{q+1}\). Then \(M\mid D_9\), and `eta` satisfies both boundary congruences
> \[
> 9^9\eta+1\equiv16^9\eta+1\equiv0\pmod M.
> \]

Consequently, for any run alphabet containing two consecutive labels—such as `{64,65}`—no larger branch-independent congruence modulus **coprime to `6`** of this fixed-residue form exists. Powers of `3` encode the current run and are deliberately excluded from this maximality statement.

## Motivation

PR #51 reduces the full constructive goal to one positive ordinary run-core path with enough run resource. The exact finite-window criterion allows one high run followed by eight zero runs:

\[
r+0+\cdots+0\ge44.
\]

Grouping those nine macros should therefore remove the resource counter entirely. The surprise is that the grouped map possesses a branch-independent ordinary modulus containing six distinct odd primes. This is stronger than the previously visible invariant `7|z` and removes all odd-modulus bookkeeping from the remaining top-boundary problem.

The construction is not a `2`-adic completion. Every quantity in `(5)` and `(8)` is an ordinary integer whenever the displayed divisibility holds.

## Proof

### 1. Nine exact `B` edges

The branch `B` is centered at its fixed point `1`:

\[
B(x)-1=\frac9{16}(x-1).
\tag{16}
\]

Therefore `(4)` implies

\[
B^9(p)
=
1+\frac{9^9}{16^9}(p-1)
=
1+9^9W.
\tag{17}
\]

This is the section state after the high run and nine `B` edges.

### 2. The next high run and next synchronized boundary

Suppose `(7)` is divisible by \(2^{3s+36}\), and define `W'` by `(8)`. Rearranging gives

\[
9^s(1+9^9W)
=
2^{3s}(1+2^{36}W').
\tag{18}
\]

The factor in parentheses on the right is odd. Hence

\[
\nu_2(1+9^9W)=3s.
\tag{19}
\]

Thus `(17)` undergoes exactly `s` `A` edges. Those edges multiply by \(9^s/2^{3s}\), and `(18)` shows that their output is

\[
1+2^{36}W'=1+16^9W',
\tag{20}
\]

the next synchronized pre-`B` boundary.

Conversely, an exact next high run `s` followed by a synchronized integer boundary must satisfy `(18)`, hence `(7)` is divisible by \(2^{3s+36}\). This proves the equivalence and `(8)--(9)` except for the residue modulo seven.

If `W=-1 mod7`, then \(9^9=16^9=1\pmod7\), and `(8)` gives `W'=-1 mod7`. This proves `(6)` and the second part of `(9)`.

### 3. The common prime-to-six invariant

The congruences `(12)--(13)` imply that

\[
a=\frac{9^9\omega+1}{D_9},
\qquad
b=\frac{16^9\omega+1}{D_9}
\tag{21}
\]

are integers. If \(W=\omega+D_9X\), substitute in `(8)` and use `(21)`:

\[
\begin{aligned}
2^{3s+36}(F_s(W)-\omega)
&=
9^{s+9}(W-\omega)\\
&\quad+
9^s(1+9^9\omega)
-
2^{3s}(1+16^9\omega).
\end{aligned}
\tag{22}
\]

Every term on the right is divisible by \(D_9\). Since \(D_9\) is odd, the denominator on the left is invertible modulo \(D_9\), proving `(14)`.

Direct exact arithmetic gives `(10)--(15)`.

### 4. Prime-to-six maximality

For a residue `eta mod M`, multiply the fixed-residue condition

\[
F_s(\eta)\equiv\eta\pmod M
\]

by the power-of-two denominator. Put

\[
A_\eta=1+9^9\eta,
\qquad
B_\eta=1+16^9\eta.
\tag{23}
\]

The condition becomes

\[
9^sA_\eta\equiv8^sB_\eta\pmod M.
\tag{24}
\]

Assume `(24)` for `s=q` and `s=q+1`. Multiply the first congruence by `9` and subtract the second:

\[
8^qB_\eta\equiv0\pmod M.
\tag{25}
\]

Because `M` is odd, `8` is invertible, so \(B_\eta=0\pmod M\). Equation `(24)` then gives \(A_\eta=0\pmod M\). In particular, `eta` is a unit modulo `M`, because `M` is coprime to `3` and \(9^9\eta=-1\).

Subtracting the two boundary congruences gives

\[
(16^9-9^9)\eta\equiv0\pmod M.
\]

Since `eta` is a unit, \(M\mid D_9\). This proves maximality.

## Exact ordinary counterexample interface

A positive answer consists of:

1. a positive integer \(W_0\equiv\omega\pmod {D_9}\);
2. an initial high run `r_0>=44` for which
   \[
   9^{r_0}\mid1+16^9W_0;
   \]
3. an infinite deterministic sequence of defined branches
   \[
   W_{j+1}=F_{r_{j+1}}(W_j),
   \qquad
   r_j\ge44.
   \]

The initial physical core is

\[
v_0=\frac{1+16^9W_0}{7\,9^{r_0}},
\qquad
z_0=7\,2^{3r_0}v_0,
\qquad
n_0=6z_0-5.
\tag{26}
\]

Every grouped transition then physically replays one high run and eight zero runs. Each nine-run block has total at least `44`, so branch-qualified PR #51 `T-8003` gives an unbounded positive Collatz orbit.

This is a complete finite acceptance gate. It does not assert that such a \(W_0\) has been found.

## Dependency audit

1. `O-8001` supplies the exact chart `(1)`.
2. `L-8004` supplies the invariant divisible-seven physical interpretation.
3. `T-8003` supplies the final divergence implication from nine-run resource.
4. Equations `(5)--(25)` are proved here by elementary integer algebra.
5. No external literature theorem is a logical dependency.

## Gap audit

This result does **not**:

- produce a forever-defined `W`;
- infer an ordinary integer from a compatible sequence of residues;
- prove that the canonical representative of a finite branch word survives one additional block;
- make periodic or affine branch schedules ordinary;
- produce a positive cycle;
- or resolve Collatz.

The remaining obstruction is exactly the changing power-of-two top boundary in `(8)`.

## Adversarial tests

`X-8251` contains two separately written standard-library implementations. They verify:

- the constants and factorization `(10)--(15)`;
- the raw and centered maps;
- exact physical `A^r B^9 A^s` replay;
- the invariant residue on 1,649 branch instances;
- the high-run threshold;
- and the changing-modulus quotient laws used in `L-8252`.

## Suggested next attack

Work in the centered quotient of `L-8252`. The fixed prime-to-`6` modulus, divisible-seven constraint, nine-run resource counter, and physical-growth proof are all discharged there. The sole live condition is a dyadic changing-cylinder recurrence.
