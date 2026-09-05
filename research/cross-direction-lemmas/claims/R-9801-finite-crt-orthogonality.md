# R-9801 — Finite CRT orthogonality of itinerary and reciprocal carries

Claim ID: `R-9801`  
Title: Finite reciprocal-carry sparsity cannot force logarithmically long itinerary repetition  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: the exact `64 -> 81` chart recurrence and reciprocal lift definition, both restated below  
Scope: refutation of a local complexity–carry transference proposed between PR #16 and PR #20  
Related counterexample candidates: none

## Definitions

An itinerary prefix of length `L` records `L` legal applications of the
`64 -> 81` chart recurrence; it does not assert infinite survival. A reciprocal
lift prefix of length `R` is `(q_0)` when `R=1` and the tuple
`(q_0,d_0,...,d_(R-2))` when `R>=2`, as in `PR16/L-9309`. The quantities
`mathcal E_K(h)` and `W_K(h)` are respectively
the signed reciprocal phase energy and the number of nonzero integral carries
at phase depth `K`. A repeated factor is required to occur wholly within the
finite word under discussion, and `A` is *primitive* when `64` does not divide
`A`.

## Refuted conjectural implication

A tempting bridge between active programs is:

> A sparse reciprocal carry word for a Fourier numerator coupled to the same
> positive integer as a finite survivor prefix should force a repeated chart
> factor of length at least the logarithm of that prefix length.

This is false at every finite depth, even after setting the Fourier numerator
equal to the survivor integer and imposing positivity and primitiveness.

## Statement

Fix integers `K,L>=1` and a phase-prefix length `1<=R<=K`.

For a binary word \(u=u_0\cdots u_{L-1}\), define

\[
\alpha_u\equiv
\sum_{j=0}^{L-1}
\frac{17u_j64^j}{81^{j+1}}
\pmod{64^L},
\tag{1}
\]

where odd denominators are inverted modulo `64^L`.

Let `gamma` be any admissible reciprocal lift prefix of length `R` from
`PR16/L-9309`. It selects one residue

\[
A\equiv\beta_\gamma\pmod{81^R}.
\tag{2}
\]

Then the two requirements are independent: there is exactly one class

\[
\boxed{
A\equiv A(u,\gamma)\pmod{64^L81^R}
}
\tag{3}
\]

whose integers have itinerary prefix `u` and reciprocal phase prefix `gamma`.
The class contains arbitrarily large positive representatives, for which all
first `L` chart states are positive.

In particular, for every `K>=2` there is a positive primitive integer `A` such
that

\[
\mathcal E_K(A)=W_K(A)=0
\tag{4}
\]

while its length-`K` itinerary has no repeated factor of length at least

\[
\lceil\log_2K\rceil.
\tag{5}
\]

Thus no theorem using only finite reciprocal carry count or energy can force a
repeated itinerary factor of length at least `ceil(log_2 K)`. Any stronger
bridge must add a genuinely infinite or archimedean hypothesis, such as
stabilization of one fixed ordinary representative across all depths.

## Proof

The chart recurrence is

\[
A_{j+1}=\frac{81A_j-17u_j}{64}.
\tag{6}
\]

Iterating it backward gives

\[
A=
\sum_{j<L}\frac{17u_j64^j}{81^{j+1}}
+\left(\frac{64}{81}\right)^LA_L.
\tag{7}
\]

Hence a chart orbit with prefix `u` satisfies (1). Conversely, (1) makes the
successive numerators in (6) divisible by `64`; induction gives the prescribed
finite itinerary. Choosing a sufficiently large positive representative of
the class makes all finitely many affine states in (6) positive.

For the reciprocal lift, the level `R-1` residue satisfies

\[
q_{R-1}(A)
\equiv-17A64^{R-1-K}\pmod{81^R}.
\tag{8}
\]

The coefficient of `A` is a unit modulo `81^R`. The lift-prefix bijection of
`PR16/L-9309` therefore makes every prefix `gamma` equivalent to exactly one
class (2). Since `64^L` and `81^R` are coprime, the Chinese remainder theorem
gives exactly one combined class modulo their product. This proves (3).

For the zero-energy example, take `L=R=K`, choose `u_0=1`, and choose the zero
phase prefix. Equation (3) supplies positive integers satisfying

\[
A\equiv\alpha_u\pmod{64^K},
\qquad
A\equiv0\pmod{81^K}.
\tag{9}
\]

Because \(u_0=1\), equation (1) gives \(A\equiv1\pmod{64}\), so `A` is
primitive for the phase theorem. The second congruence makes every reciprocal
phase through level `K-1` equal to zero. Hence its phase energy and number of
nonzero carries are both zero, proving (4).

Let \(m=\lceil\log_2 K\rceil\). Choose `u` as a length-`K` segment of a binary de
Bruijn cycle of order `m`, rotated so that `u_0=1`. The length-`m` factors
beginning inside this segment are distinct because the cycle contains each
binary word of length `m` exactly once and `K<=2^m`. If two longer factors
were equal, their first `m` symbols would be equal. Thus no repeated factor
has length at least `m`, proving (5). ∎

## What sparse carries do encode

For signed normalized phases `x_ell`, the integral carries satisfy

\[
a_\ell=64x_\ell-81x_{\ell+1},
\qquad |a_\ell|\le72.
\]

Given the initial signed residue and the carry word, the recurrence

\[
s_{\ell+1}=64s_\ell-a_\ell81^{\ell+1}
\]

reconstructs the phase chain and hence the frequency residue modulo `81^K`.
Therefore, for every integer `0<=w<=K-1`,

\[
\#\{h\bmod81^K:W_K(h)\le w\}
\le
81\sum_{j=0}^w\binom{K-1}{j}144^j.
\tag{10}
\]

Sparse carries really are a short description—but of an `81`-adic frequency
residue. Itinerary repetition is a `64`-adic collision between tail states.
Finite CRT independence prevents one from implying the other.

## Motivation

`L-9803` explains why the two programs share the constant
`1/(log_64(81)-1)`. This refutation shows what that numerical duality does not
mean: their symbolic words are not locally identified.

## Dependency audit

- Equation (6) is the exact active-chart recurrence.
- Equation (8) and the lift-prefix bijection are the definitions/proof content
  of `PR16/L-9309`.
- The remaining proof uses finite affine induction, CRT, and the elementary
  existence of binary de Bruijn cycles.

## Gap audit

- The constructed integer depends on `K`; no one integer is shown to survive
  all depths.
- Its least positive CRT representative may grow like `64^K81^K`.
- Consequently the height term in completion-height rigidity can grow
  linearly with `K`; the example does not contradict `PR16/L-9310`.
- The result refutes a local implication, not every possible global
  complexity–carry bridge.

## Adversarial tests

- The condition \(u_0=1\) ensures \(A\equiv1\pmod{64}\) and hence the needed
  primitiveness.
- A repeated factor longer than `m` would contain a repeated length-`m`
  prefix, so the de Bruijn argument covers every length at least `m`.
- Setting `h=A` is built into (8)--(9); the independence is not obtained by
  choosing an unrelated Fourier numerator.

## Remaining uncertainty

None in the finite orthogonality statement. A global diagonal-section theorem
for one stabilized `A` remains open.

## Suggested next attack

Study the least representatives of the simultaneous cylinders

\[
A\equiv\alpha_u\pmod{64^L},
\qquad
A\equiv\beta_\gamma\pmod{81^R}
\]

as \(L,R\to\infty\). By `L-9801`, ordinary realization is exactly eventual
stabilization; that global condition is absent from the finite countermodels.
