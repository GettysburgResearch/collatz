# L-0017 — Universal mixed-radix connector tiles

Claim ID: `L-0017`  
Title: Every aligned pair of padded tower edges has an exact infinite connector family with one common ordinary high tail  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0016`  
Scope: finite chaining of cycle-padded mismatch towers  
Related counterexample candidates: none

## Statement

Let one tower instance \(E\) end at the phase from which a second tower instance \(F\) begins.

Write their block data from `L-0016` as

\[
E=(A,K,B,G),
\]

\[
F=(\bar A,\bar K,\bar B,\bar G).
\]

Thus the first edge acts by

\[
A+2^K h
\longmapsto
B+3^G h,
\tag{1}
\]

and the second edge is available on quotients

\[
\bar A+2^{\bar K}h'.
\tag{2}
\]

Define \(\eta\) to be the unique integer

\[
0\le\eta<2^{\bar K}
\]

satisfying

\[
\boxed{
B+3^G\eta\equiv\bar A\pmod{2^{\bar K}}.
}
\tag{3}
\]

Put

\[
\boxed{
\theta=
\frac{B+3^G\eta-\bar A}{2^{\bar K}}.
}
\tag{4}
\]

Then:

### 1. Canonical connector seed

The integer \(\eta\) exists uniquely and

\[
\boxed{\theta\ge0.}
\tag{5}
\]

### 2. Exact connector family

For every ordinary integer \(z\ge0\), define

\[
h=\eta+2^{\bar K}z,
\tag{6}
\]

\[
h'=\theta+3^Gz.
\tag{7}
\]

Then

\[
\boxed{
B+3^Gh
=
\bar A+2^{\bar K}h'.
}
\tag{8}
\]

Consequently the first tower edge maps

\[
A+2^K\bigl(\eta+2^{\bar K}z\bigr)
\]

exactly into the input cylinder of the second tower edge:

\[
\boxed{
A+2^K\bigl(\eta+2^{\bar K}z\bigr)
\longmapsto
\bar A+2^{\bar K}\bigl(\theta+3^Gz\bigr).
}
\tag{9}
\]

Every \(z\ge0\) gives an ordinary finite integer and an exact two-block deterministic Collatz trajectory.

### 3. String-tile interpretation

Equation (8) is a finite mixed-radix tile. It rewrites

- the fixed \(\bar K\)-bit binary prefix \(\eta\) of the first high tail;
- into the finite ternary-scaled prefix \(\theta\);
- while preserving the same still-higher ordinary tail \(z\).

The first edge contributes the multiplier \(3^G\), and the next binary cylinder contributes the divisor \(2^{\bar K}\).

### 4. Finite-path compiler

Let

\[
E_0,E_1,\ldots,E_{m-1}
\]

be any finite phase-aligned sequence of padded tower instances. Then there is a nonempty ordinary dyadic cylinder of initial quotients that follows the entire sequence exactly.

More precisely, for some integers

\[
0\le R<2^{\mathcal K},
\qquad
0\le S<3^{\mathcal G},
\]

where

\[
\mathcal K=\sum_{i=0}^{m-1}K_i,
\qquad
\mathcal G=\sum_{i=0}^{m-1}G_i,
\]

all quotients

\[
q_0=R+2^{\mathcal K}z
\qquad(z\ge0)
\]

follow the prescribed blocks, and their final quotients have the form

\[
q_m=S+3^{\mathcal G}z.
\]

Thus arbitrary finite counter schedules are universally compatible. Infinite finite-boundary closure is the only nontrivial remaining issue.

## Proof

Because \(3^G\) is odd, it is invertible modulo \(2^{\bar K}\). Therefore (3) has one solution modulo \(2^{\bar K}\), and choosing its least nonnegative representative gives the unique \(\eta\).

The numerator in (4) is divisible by \(2^{\bar K}\). It cannot be negative. Indeed,

\[
B+3^G\eta\ge0
\]

and

\[
0\le\bar A<2^{\bar K}.
\]

If the numerator were negative, it would lie strictly between \(-2^{\bar K}\) and zero, but no nonzero multiple of \(2^{\bar K}\) lies in that interval. Hence it is nonnegative and \(\theta\ge0\).

Substitute (6):

\[
\begin{aligned}
B+3^Gh
&=B+3^G\eta+3^G2^{\bar K}z\\
&=\bar A+2^{\bar K}\theta+2^{\bar K}3^Gz\\
&=\bar A+2^{\bar K}(\theta+3^Gz)\\
&=\bar A+2^{\bar K}h'.
\end{aligned}
\]

This proves (8). Applying the first replacement identity from `L-0016` proves (9), and the right side is exactly in the second edge's binary cylinder.

For the finite-path statement, concatenate the chronological parity blocks. Their total length is \(\mathcal K\) and total odd count is \(\mathcal G\). The ordinary parity-cylinder affine formula gives one residue \(R\) modulo \(2^{\mathcal K}\) and one output block \(S\) modulo \(3^{\mathcal G}\). Alternatively, iterate the connector construction above. Both give the displayed tail-preserving form. ∎

## Interpretation

This lemma closes a possible false lead:

> Failure to find a finite connector is never the obstruction.

Every adjacent pair of tower instances connects, and every finite schedule has infinitely many ordinary realizations. A successful counterexample proof must therefore show that the connector prefixes regenerate indefinitely from one finite high tail.

The connector map on the free tail is

\[
\eta+2^{\bar K}z
\longmapsto
\theta+3^Gz.
\tag{10}
\]

This is the natural stack rewrite exposed by the tower construction. Its input precision grows in powers of two; its output height grows in powers of three.

## Dependency audit

- `L-0016` supplies the two block-replacement identities and the block bounds.
- The connector is only the Chinese-remainder invertibility of an odd number modulo a power of two.
- The finite-path corollary is also an immediate instance of the ordinary parity-affine cylinder formula.

## Gap audit

- The common tail \(z\) is preserved for one connector, but a later connector imposes another low binary prefix on \(\theta+3^Gz\).
- Recursively satisfying all future prefixes may select only a nonordinary 2-adic tail.
- The lemma proves arbitrary finite depth and must not be cited as infinite closure.

## Adversarial tests

`X-0012` checks every ordered pair of the four self-return tower types at phase \(-34\) for padding heights zero through seven, giving 1,024 exact connector families. It directly replays both Collatz blocks on several values of \(z\).

## Suggested next attack

Study the iteration of (10) as a genuine stack transducer. `L-0018` shows why its growing inverse-power prefixes cannot be compressed into a fixed periodic residue table, while `T-0021` shows that a bounded tail library cannot diverge.