# D-7801 — Ordinary survivor towers and canonical cylinder representatives

**Claim ID:** `D-7801`  
**Type:** definition  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-global-01`  
**Created:** 2026-07-25  
**Dependencies:** none  
**Scope:** exact induced integer dynamics and nested congruence constructions

## 1. Canonical nested cylinder chain

A **canonical nested cylinder chain** consists of positive integers

\[
1=M_0\mid M_1\mid M_2\mid\cdots,
\qquad M_N\longrightarrow\infty,
\]

and canonical residues

\[
0\le R_N<M_N
\]

such that

\[
R_{N+1}\equiv R_N\pmod {M_N}.
\]

The chain selects one point of the inverse limit

\[
\varprojlim_N \mathbf Z/M_N\mathbf Z.
\]

When every `M_N` is a power of two, this is one point of `Z_2`.

Its appended mixed-radix digit is

\[
a_N=rac{R_{N+1}-R_N}{M_N},
\qquad
0\le a_N<rac{M_{N+1}}{M_N}.
\]

## 2. Positive ordinary realization

A nonnegative ordinary integer `x` **realizes** the chain when

\[
x\equiv R_N\pmod {M_N}
\qquad(N\ge0).
\]

This is stronger than finite compatibility. Every individual cylinder

\[
R_N+M_N\mathbf Z
\]

contains infinitely many positive integers, regardless of whether one integer realizes all depths.

## 3. Signed ordinary realization

An ordinary integer `x\in\mathbf Z` realizes the chain by the same congruences. In canonical nonnegative representatives:

- a nonnegative realization eventually has `R_N=x`;
- a negative realization `x=-c`, `c>0`, eventually has
  \[
  R_N=M_N-c.
  \]

Thus positive and signed extraction must not be conflated.

## 4. Deterministic survivor tower

Let `F` be a partial deterministic map on positive integers, or an induced return map whose each defined edge has already been proved to replay an exact finite Collatz segment.

For `N\ge0`, define

\[
\mathcal S_N
=
\{x\in\mathbf Z_{>0}: F^j(x)\text{ is defined for }0\le j<N\}.
\]

Additional architecture conditions—allowed types, run constraints, invariant sections, or a specified finite grammar—may be included in the definition of `S_N`, provided they are exact and prefix-closed.

Then

\[
\mathcal S_{N+1}\subseteq\mathcal S_N.
\]

When `S_N` is nonempty, define the **least positive depth-`N` root**

\[
m_N=\min\mathcal S_N.
\]

If `S_N` is empty, put `m_N=+\infty`.

## 5. Architecture decision

A prescribed architecture is:

- **ordinarily inhabited** if
  \[
  \bigcap_{N\ge0}\mathcal S_N\ne\varnothing;
  \]
- **ordinarily empty** if the intersection is empty.

This decision is architecture-specific. It does not quantify over all positive Collatz trajectories.

## 6. Counterexample-complete architecture

An architecture is **counterexample-complete on survivors** when a separate exact theorem proves that every member of

\[
\bigcap_N\mathcal S_N
\]

produces a positive Collatz trajectory that avoids the trivial cycle forever—for example by strict boundary growth, unboundedness, or a nontrivial exact return.

In such an architecture, ordinary extraction of one element of the intersection produces a `K-####` candidate. The replay/growth theorem does not itself prove the intersection is nonempty.