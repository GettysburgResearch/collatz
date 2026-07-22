# L-9879 -- Critical H cores repel repeats and saturate residue capacity

Claim ID: `L-9879`  
Title: Repeated H odd cores force exponential completion height, and critical cores are asymptotically injective  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `PR19/D-9501`; critical consequences use `PR19/T-9508`  
Scope: exact infinite H block chains; Parts 2--3 are conditional on the critical alternative `Z_infinity>0`  
Related counterexample candidates: none

## Statement

Let an exact H block chain have letters `r_n>=0` and odd cores `u_n>0`, so

\[
p_n=2^{3r_n+2}u_n,
\qquad
u_n\equiv1\pmod4,
\tag{1}
\]

and the exact adjacent recurrence is

\[
\boxed{
2^{3r_{n+1}+2}u_{n+1}
-3^{2r_n+1}u_n
=1.
}
\tag{2}
\]

### 1. Exact repeated-core completion height

If `i<j`, `u_i=u_j`, and the two states are distinct, then

\[
\boxed{
\nu_2(r_j-r_i)
\ge
3\min(r_{i+1},r_{j+1})-1.
}
\tag{3}
\]

When the minimum on the right is at least one, equivalently,

\[
\boxed{
2^{3\min(r_{i+1},r_{j+1})-1}
\mid r_j-r_i.
}
\tag{4}
\]

This is an exact two-occurrence completion-height bound requiring no imported
2-adic logarithm theorem.

### 2. Near-injectivity in the critical regime

Assume the critical alternative of `PR19/T-9508`:

\[
Z_\infty>0,
\qquad
c_*=\frac{\log9}{\log8},
\qquad
r_n\sim A c_*^n,
\quad
A=(c_*-1)Z_\infty>0.
\tag{5}
\]

If `u_i=u_j` with `i<j`, then

\[
\boxed{
j
\ge
\left(
\frac{3Ac_*\log2}{\log c_*}+o(1)
\right)c_*^i.
}
\tag{6}
\]

Thus repeats of one core are separated by exponentially large orbit-index
gaps.  In particular,

\[
\boxed{
\#\{u_i:0\le i<N\}
\ge
N-\log_{c_*}N-O(1).
}
\tag{7}
\]

All but `O(log N)` positions among the first `N` therefore contribute
pairwise distinct core values.

### 3. Sharp two-residue capacity consequences

Exact H legality forces

\[
\boxed{
u_i\equiv
\begin{cases}
1\pmod {12},&r_i\text{ even},\\
5\pmod {12},&r_i\text{ odd}.
\end{cases}
}
\tag{8}
\]

Consequently, uniformly for `U>=1`,

\[
\boxed{
\#\{0\le i<N:u_i\le U\}
\le
\frac U6+\log_{c_*}N+O(1).
}
\tag{9}
\]

The parity-resolved bounds are

\[
\boxed{
\begin{aligned}
\#\{i<N:r_i\text{ even},u_i\le U\}
&\le\frac U{12}+O(\log N),\\
\#\{i<N:r_i\text{ odd},u_i\le U\}
&\le\frac U{12}+O(\log N).
\end{aligned}
}
\tag{10}
\]

In particular,

\[
\boxed{
\max_{i<N}u_i\ge6N-O(\log N),
}
\tag{11}
\]

\[
\boxed{
\sum_{i<N}\log u_i
\ge
N\log N-O(N),
}
\tag{12}
\]

and

\[
\boxed{
\limsup_{n\to\infty}\frac{u_n}{n}\ge6.
}
\tag{13}
\]

For every fixed `0<=alpha<1`,

\[
\boxed{
\#\{i<N:u_i\le i^\alpha\}
=O(N^\alpha+\log N)=o(N).
}
\tag{14}
\]

Hence a critical exact chain cannot have an eventual sublinear polynomial
envelope `u_n<=C(n+1)^alpha`.  Since `log r_n=n log c_*+O(1)`, one also has

\[
\boxed{
\limsup_{n\to\infty}\frac{u_n}{\log r_n}
\ge
\frac6{\log c_*}
=108.9015\ldots .
}
\tag{15}
\]

## Definitions

The block coordinates are those of `PR19/D-9501`: `r_n` is the number of
second-branch H steps following one first-branch step, and `u_n` is the odd
core after removing the exact power `2^(3r_n+2)` from `p_n=3n_n+4`.

The qualifier **critical** refers only to the alternative `Z_infinity>0` in
`PR19/T-9508`.  It supplies the asymptotic (5) and the discounted core budget;
the universal repeated-core theorem (3) does not use that alternative.

## Motivation

`PR19/Q-9504` asks for a one-occurrence upper bound on

\[
\nu_2(3^{2r+1}u+1)
\]

strong enough to exclude a critical near-Pillai chain.  Such a logarithmic
form estimate is not imported here.  Instead, subtracting two occurrences of
the same core makes the unknown cofactors disappear and gives the exact
divisibility (3).

In the critical regime, the required divisibility is far larger than the
ordinary difference between two nearby `r`-values.  Repeated cores are pushed
to tower-separated indices.  Combining this asymptotic multiplicity one with
the two exact residue classes (8) turns the abstract completion-height law
into the sharp elementary capacity constant six.

## Proof

### Repeated-core divisibility

Suppose `u_i=u_j=u`.  Subtract (2) at the two indices:

\[
u(3^{2r_j+1}-3^{2r_i+1})
=
2^{3r_{j+1}+2}u_{j+1}
-2^{3r_{i+1}+2}u_{i+1}.
\tag{16}
\]

The right side is divisible by

\[
2^{3\min(r_{i+1},r_{j+1})+2}.
\tag{17}
\]

Equal cores and equal `r`-values would give equal states by (1), so the
distinct-state hypothesis makes

\[
d=|r_j-r_i|>0.
\tag{18}
\]

Because `u` is odd, the valuation of the left side is

\[
\begin{aligned}
\nu_2(3^{2r_j+1}-3^{2r_i+1})
&=\nu_2(3^{2d}-1)\\
&=3+\nu_2(d),
\end{aligned}
\tag{19}
\]

by elementary LTE.  Comparing (17) and (19) proves (3), and (4) is its
divisibility form.

### Critical repeat gaps

Under (5), `r_n` is eventually strictly increasing.  For a sufficiently late
repeat with `i<j`, equation (4) gives

\[
r_j-r_i
\ge
2^{3r_{i+1}-1}.
\tag{20}
\]

On the other hand, `r_j=Ac_*^j(1+o(1))`.  Taking logarithms in (20) gives

\[
j\log c_*+\log A+o(1)
\ge
(3r_{i+1}-1)\log2
=3Ac_*^{i+1}\log2\,(1+o(1)).
\tag{21}
\]

Division by `log c_*` proves (6).

Choose a fixed

\[
0<\beta<\frac{3Ac_*\log2}{\log c_*}.
\tag{22}
\]

For large `N`, if

\[
i\ge\log_{c_*}(N/\beta)+O(1),
\tag{23}
\]

then a later equal core would have index `j>=N`.  Hence the cores in the tail
from (23) through `N-1` are pairwise distinct.  Their number proves (7).

### Residue capacity

Every exact state satisfies `p_i=1 mod 3`.  Since

\[
2^{3r_i+2}
\equiv
\begin{cases}
1\pmod3,&r_i\text{ even},\\
-1\pmod3,&r_i\text{ odd},
\end{cases}
\tag{24}
\]

and `u_i=1 mod 4`, CRT gives (8).

Only two residue classes modulo 12 are therefore available.  Among the late
pairwise distinct cores from (7), at most `U/6+O(1)` are at most `U`; the
first `O(log N)` positions are uncontrolled.  This proves (9).  Keeping the
parity label and using one class modulo 12 proves (10).

Taking `U` just below the maximum core proves (11).  For (12), sort the
`N-O(log N)` distinct late cores increasingly.  The capacity bound says that
the `k`-th such core is at least `6k-O(1)`.  Hence

\[
\sum_{i<N}\log u_i
\ge
\sum_{k\le N-O(\log N)}\log(6k-O(1))
=N\log N-O(N)
\tag{25}
\]

by the elementary factorial estimate.

For every `N`, (11) supplies an index `i_N<N` with
`u_(i_N)>=6N-O(log N)`.  These indices are unbounded, and
`i_N<N`, so (13) follows.  If `u_i<=i^alpha` and `i<N`, then
`u_i<=N^alpha`; applying (9) with `U=N^alpha` proves (14).  Finally substitute
`log r_n=n log c_*+O(1)` into (13) to obtain (15).  This completes the proof.
QED

## Dependency audit

- `PR19/D-9501` supplies the exact core factorization, congruences, and
  recurrence (2).
- `PR19/T-9508` is used only for the critical asymptotic (5).  The repeated-
  core theorem (3) is unconditional for exact chains.
- Elementary LTE supplies (19); no 2-adic logarithm, Baker estimate, S-unit
  theorem, or empirical hypothesis is used.
- The capacity statements use only (7) and the exact CRT classes (8).

## Gap audit

- The theorem does not exclude the critical regime.  A nearly injective core
  sequence with `u_n` of roughly linear size is compatible with every bound
  above and with the discounted budget of `T-9508`.
- Repeated cores are not impossible; they may recur at tower-separated
  indices.
- Distinct core values need not introduce distinct prime factors.
- The critical asymptotic is branch-qualified and remains `PROPOSED`.
- The result excludes sublinear envelopes in orbit time, not cores polynomial
  in `r_n`; the latter allowance is exponentially larger.
- No ordinary H survivor or Collatz counterexample is constructed.

## Adversarial tests

- The right side of (16) is divisible by the smaller next-state power of two,
  not necessarily by the larger one.
- LTE is applied to `3^(2d)-1`; the exact valuation is `3+nu_2(d)`.  Using the
  odd-exponent formula would lose two powers of two.
- When `min(r_(i+1),r_(j+1))=0`, (3) is true but its displayed divisibility
  exponent is negative; equation (4) is asserted only when the minimum is at
  least one.
- Equal cores alone do not imply equal states.  Distinct states are used to
  ensure `r_i!=r_j` before LTE.
- The tail cores in (23) may equal some early cores, but they are pairwise
  distinct among themselves; this is already enough for (7).
- The factor six comes from two classes modulo 12.  A phase-frequency theorem
  could improve it, but no such frequency is assumed.

## Remaining uncertainty

Can the exact two-occurrence bound be combined with a one-occurrence height
estimate or a phase-frequency law to force faster-than-linear core growth?
Either improvement could conflict with the discounted critical budget; the
present capacity bound alone does not.

## Suggested next attack

Track the signed rounded-critical deficit

\[
d_n=\lceil c_*r_n\rceil-r_{n+1}.
\]

An exact multiplicative balance for `u_(n+1)/u_n` in terms of `d_n` would
quantify how often the chain must leave the contracting rounded-critical
regime and may turn the near-injectivity bound into a genuine finite-trap
dichotomy.
