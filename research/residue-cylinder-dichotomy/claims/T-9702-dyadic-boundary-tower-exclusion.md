# T-9702 — Dyadic boundary tower directives never stabilize

**Claim ID:** `T-9702`  
**Title:** Every direct dyadic boundary directive in the four phase-`-34` tower types has infinitely many nonzero residue blocks  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `D-9701`, `L-9701`, `T-9701`  
**Scope:** all infinite type directives, all starting scales `m_0>=0`  
**Related counterexample candidates:** none

## Motivation

This is the first full-class side-A theorem in the packet. It tests the completion-height program on a concrete PR #3 tower system with arbitrary finite control and one growing scale counter, while retaining exact physical Collatz replay for every finite prefix.

## Definitions

All tower data and the direct boundary recurrence are defined in `D-9701`. The cumulative cylinders and blocks are those of `L-9701`.

## Statement

Fix any starting scale \(m_0\ge0\), put

\[
t_n=2^{m_0+n},
\]

and choose an arbitrary infinite type directive

\[
i_0,i_1,i_2,\ldots\in\{5,6,7,8\}.
\]

For the direct boundary recurrence of `D-9701`,

\[
h_{n+1}
=
\frac{N_nh_n+C_n}{q_n},
\tag{1}
\]

where

\[
N_n=3^{7(t_n+1)},
\tag{2}
\]

\[
q_n=2^{11(2t_n+1)},
\tag{3}
\]

\[
C_n=B_{i_n}(t_n)-A_{i_{n+1}}(2t_n),
\tag{4}
\]

let

\[
R_k\pmod{Q_k}
\]

be the unique initial cylinder for the first \(k\) transitions, and let

\[
a_k=\frac{R_{k+1}-R_k}{Q_k}.
\]

Then:

### 1. Full-class nonstabilization

\[
\boxed{a_k\ne0\text{ for infinitely many }k.}
\tag{5}
\]

### 2. No ordinary integer completion

The unique point

\[
h_0^*\in\mathbb Z_2
\]

selected by the nested cylinders satisfies

\[
\boxed{h_0^*\notin\mathbb Z.}
\tag{6}
\]

In particular it is not a nonnegative ordinary initialization.

### 3. No hidden positive path

There is no signed integer \(h_0\) whose exact recurrence (1) is integral for
all future steps. Therefore there is a fortiori no positive high-tail
initialization and no `K-####` candidate in this class.

The theorem quantifies all \(4^{\mathbb N}\) type directives, and hence every
finite-control subshift on the four types.

## Proof

Fix one step and abbreviate

\[
t=t_n,
\quad N=N_n,
\quad q=q_n,
\quad A=A_{i_{n+1}}(2t),
\quad B=B_{i_n}(t).
\]

Then

\[
h'=\frac{Nh+B-A}{q}.
\tag{7}
\]

### Step 1. Uniform contraction

The elementary integer inequality

\[
3^7=2187<4096=2^{12}
\tag{8}
\]

gives

\[
N=3^{7(t+1)}<2^{12(t+1)}.
\]

Since

\[
q=2^{11(2t+1)}=2^{22t+11},
\]

we obtain, for every \(t\ge1\),

\[
\boxed{
\frac Nq<2^{1-10t}\le2^{-9}=\frac1{512}.
}
\tag{9}
\]

By the tower bounds,

\[
0<B<N.
\tag{10}
\]

Also

\[
A=2^{K_{i_{n+1}}(2t)}
\frac{\mu_{i_{n+1}}(2t)}{2^{r_{i_{n+1}}+1}}
=q\frac\mu{2^{r+1}}.
\]

Here \(r+1\in\{3,4,5,6\}\) and \(\mu\) is odd with
\(1\le\mu<2^{r+1}\). Therefore

\[
\boxed{
\frac q{64}\le A\le\frac{63q}{64}.
}
\tag{11}
\]

For every integer transition,

\[
\begin{aligned}
|h'|
&\le \frac Nq|h|+\frac Bq+\frac Aq\\
&<\frac1{512}|h|+\frac1{512}+1.
\end{aligned}
\]

Thus

\[
\boxed{
|h'|<\frac1{512}|h|+\frac{513}{512}.
}
\tag{12}
\]

This is hypothesis (3) of `T-9701` with

\[
c=\frac1{512},
\qquad d=\frac{513}{512}.
\]

Moreover

\[
\frac d{1-c}
=
\frac{513}{511}
<2.
\tag{13}
\]

### Step 2. Exact exclusion of the finite trap

Take

\[
h\in\{-1,0,1\}.
\]

We show in every case that

\[
-q<Nh+B-A<0.
\tag{14}
\]

For \(h=1\), equations (9)--(11) give

\[
N+B<2N<\frac q{256}<\frac q{64}\le A,
\]

while \(A<q\). Hence (14).

For \(h=0\),

\[
B<N<\frac q{512}<\frac q{64}\le A<q,
\]

so again (14).

For \(h=-1\), the numerator is negative. Its absolute value is bounded by

\[
A+N-B<A+N
\le\frac{63q}{64}+\frac q{512}
=\frac{505q}{512}<q.
\]

Thus (14) holds in the third case as well.

A nonzero integer strictly between \(-q\) and \(0\) is not divisible by \(q\).
Therefore no integer in the trap

\[
\{-1,0,1\}=\{h\in\mathbb Z:|h|<2\}
\]

has a next integral transition.

### Step 3. Apply the finite-trap theorem

Equations (12)--(14) satisfy `T-9701` with trap radius \(B=2\). Hence no
ordinary integer belongs to all nested cylinders. By `L-9701`, the new residue
blocks cannot be eventually zero. This proves (5)--(6). ∎

## Exact physical interpretation

For every finite prefix and every sufficiently large member of its initial
cylinder, all high tails are nonnegative. Equation (15) of `D-9701` then joins
the tower blocks exactly, and

\[
T^{11(t_n+1)}(x_n)=x_{n+1}
\]

with exactly \(7(t_n+1)\) odd shortcut steps.

Thus the theorem does not deny finite physical realizability. It proves that
the compatible initial cylinders keep demanding genuinely new high binary
blocks and never collapse to one ordinary integer.

## Dependency audit

- The finite tower formulas and bounds are the branch-qualified interface of PR
  #3 `L-0016`/`L-0017`.
- The cylinder and block algebra is re-proved in `L-9701`.
- The infinite step is the elementary contraction theorem `T-9701`.
- No p-adic logarithm, symbolic embedding theorem, entropy estimate,
  equidistribution assumption, or finite search is a proof dependency.

## Nonapplication to the 256-transition stage

The direct dyadic connector has slope less than \(1/512\). PR #3's corrected
256-transition **composite** has positive logarithmic slope and a proved stage
surplus. Replacing that composite by (1) would be a false identification.
`Q-9701` records the unresolved supercritical transfer.


## Adversarial tests

`X-9701` checks the worst dyadic height `t=1` and five later heights for all 16 type pairs, verifies `512N<q`, the full target-anchor interval, and every trap numerator. Its independent checker directly executes the shortcut map on five longer positive certificates. A reviewer should also inspect the strict inequalities in the `h=-1` case, where sign mistakes are easiest.

## Remaining uncertainty

The proof is complete-looking for the frozen direct-boundary class, but its dependence on PR #3's proposed tower interface still requires independent reconstruction. No claim is made for any schedule that inserts the 256 chronological intermediate connectors.

## Suggested next attack

Try to identify a finite forbidden state forced by a long zero-block run in the composed stage quotient `Y_m`, using PR #3 `L-0029` to remove the logarithmic prefix and `T-0030` to replace the inverse-logarithm oracle by a forward ordinary bulk word.
