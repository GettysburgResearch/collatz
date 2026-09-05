# L-9804 — Active-cylinder digit recurrence and positive-cone propagation

Claim ID: `L-9804`  
Title: Exact forward mixed-radix digits for the active `64 -> 81` tower cylinders  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-p`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: the active-stack edge identity stated below  
Scope: `PR20/L-9406`, `PR20/T-9409`, and `PR20/Q-9408`  
Related counterexample candidates: none

## Definitions

For a height `h>=0`, put

\[
M(h)=64^{9h+1},
\qquad
A(h)=81^{9h+1},
\qquad
c(h)=\frac{M(h)+17}{81}.
\tag{1}
\]

The quantity `c(h)` is a positive integer because `64^9` is congruent to `1`
modulo `81`; also `0<c(h)<M(h)`.

The active-stack transition from height `m` to height `n` has exact context
equation

\[
A(m)x+81^{9m}=c(n)+M(n)x'.
\tag{2}
\]

Let `r_(m,n)` be the unique canonical residue modulo `M(n)` satisfying

\[
A(m)r_{m,n}+81^{9m}\equiv c(n)\pmod{M(n)},
\tag{3}
\]

and put

\[
k_{m,n}
=\frac{A(m)r_{m,n}+81^{9m}-c(n)}{M(n)}.
\tag{4}
\]

## Statement

### 1. One-edge quotient conjugacy and positivity

For an integer `x`, there exists an integer `x'` satisfying (2) exactly when

\[
x=r_{m,n}+M(n)y
\tag{5}
\]

for an integer `y`, and then

\[
\boxed{x'=A(m)y+k_{m,n}}.
\tag{6}
\]

Moreover `k_(m,n)>=0`. Hence `x>=0` in (5) implies `y>=0` and `x'>=0`.

### 2. One cylinder for every finite directive

For a height directive `m_0,...,m_K`, define

\[
Q_K=\prod_{j=1}^K M(m_j).
\tag{7}
\]

There is exactly one residue class

\[
x_0\equiv R_K\pmod{Q_K},
\qquad0\le R_K<Q_K,
\tag{8}
\]

whose members realize all `K` transitions integrally. Every nonnegative
member of this cylinder has nonnegative intermediate contexts.

The modulus uses the target height on each transition. In particular,

\[
\nu_2(Q_K)=6\sum_{j=1}^K(9m_j+1).
\tag{9}
\]

### 3. Exact forward cylinder digits

Let

\[
P_K=\prod_{i=0}^{K-1}A(m_i).
\tag{10}
\]

Define `t_K` by the exact terminal affine form

\[
x_K(R_K+Q_Kz)=t_K+P_Kz.
\tag{11}
\]

Then the unique new canonical block digit in

\[
R_{K+1}=R_K+Q_Ka_K,
\qquad
0\le a_K<M(m_{K+1}),
\tag{12}
\]

is

\[
\boxed{
a_K=
\left[
P_K^{-1}
(r_{m_K,m_{K+1}}-t_K)
\right]_{M(m_{K+1})}.
}
\tag{13}
\]

The next terminal state is

\[
\boxed{
t_{K+1}
=A(m_K)
\frac{t_K+P_Ka_K-r_{m_K,m_{K+1}}}{M(m_{K+1})}
+k_{m_K,m_{K+1}}.
}
\tag{14}
\]

Initialize with `P_0=1`, `Q_0=1`, `R_0=0`, and `t_0=0`.

### 4. Exact stabilization obstruction

The new block vanishes exactly when

\[
\boxed{
t_K\equiv r_{m_K,m_{K+1}}\pmod{M(m_{K+1})}.
}
\tag{15}
\]

Equivalently,

\[
a_K=0
\iff
\nu_2(t_K-r_{m_K,m_{K+1}})
\ge6(9m_{K+1}+1),
\tag{16}
\]

with `nu_2(0)=infinity`.

Thus it is sufficient for non-stabilization to prove that (16) fails at
infinitely many stages. If, infinitely often,

\[
0\le t_K<M(m_{K+1})
\quad\text{and}\quad
t_K\ne r_{m_K,m_{K+1}},
\tag{17}
\]

then the selected completion point is not an ordinary nonnegative integer.

## Proof

Because `A(m)` is odd, it is invertible modulo the power of two `M(n)`, so
(3) has one canonical solution. Substituting (5) in (2) and using (4) gives
(6); reversing the algebra proves the converse.

The numerator in (4) is a multiple of `M(n)` and is strictly greater than
`-M(n)`, since its first two terms are nonnegative and `c(n)<M(n)`. Therefore
`k_(m,n)>=0`. If `y<=-1`, then (5) and `r_(m,n)<M(n)` would give `x<0`.
This proves the positive-cone assertion.

For the finite-cylinder theorem, work backward. Suppose the suffix beginning
at `x_(i+1)` is one residue `R mod Q`. Equations (5)--(6) give

\[
x_i=r_i+M(m_{i+1})y,
\qquad
x_{i+1}=A(m_i)y+k_i.
\]

Since `A(m_i)` is odd, the suffix condition selects exactly one class

\[
y\equiv A(m_i)^{-1}(R-k_i)\pmod Q.
\]

It therefore selects exactly one class for `x_i` modulo
`M(m_{i+1})Q`, and every member of that class realizes the edge and suffix.
Starting from the unrestricted terminal class modulo `1` proves (7)--(8) and
the converse. The positivity statement follows edge by edge from part 1.

For part 3, insert `z=a_K+M(m_{K+1})w` into (11). The next edge is integral
exactly when

\[
t_K+P_Ka_K\equiv r_{m_K,m_{K+1}}\pmod{M(m_{K+1})}.
\]

The odd number `P_K` is invertible modulo `M(m_{K+1})`; taking the canonical
solution gives (13). Applying the edge formula at `w=0` gives (14). Equation
(15) follows from (13), and (16) is the equivalent power-of-two divisibility
condition. Under (17), congruence (15) fails because both sides are canonical
integers in the same modulus interval. ∎

## Ordinary realization corollary

The cylinders are nested, so `R_{K+1}` is congruent to `R_K` modulo `Q_K`.
Since `nu_2(Q_K)->infinity`, they select one point of `Z_2`. By `L-9801`, that
point is an ordinary nonnegative integer exactly when `a_K=0` eventually.

Part 1 strengthens the source packet's gap note: for a stabilized nonnegative
initial context, nonnegativity of every intermediate context is automatic.
Strict positivity, nontriviality, and the final Collatz chart lift remain
separate obligations.

## Motivation

The cylinder modulus alone measures consumed precision but does not decide
ordinary realization. Equations (13)--(16) turn the remaining block-tail
question into a deterministic valuation problem on explicit terminal states.

## Dependency audit

- Equation (2) is the branch-qualified active-stack identity.
- All other assertions are reconstructed from elementary congruence algebra.
- `L-9801` is used only for the final ordinary-realization corollary.

## Gap audit

- No proof is given that (16) fails infinitely often for every admissible
  `{17,18}` directive.
- Nonnegative does not imply strictly positive or outside a trivial chart
  state.
- Quadratic growth of the modulus is not itself a complexity lower bound.

## Adversarial tests

- Using `M(m_K)` rather than the target `M(m_{K+1})` in one transition gives
  the wrong bit cost; equations (7), (9), and (13) use target indexing.
- Negative embedded integers need not stabilize in canonical nonnegative
  representatives; `L-9801` is intentionally one-sided.
- If `t_K=r_{m_K,m_{K+1}}` as ordinary integers, then (13) visibly gives
  `a_K=0`.

## Remaining uncertainty

The exact late-time behavior of (13)--(14) for balanced `{17,18}` height
directives remains open.

## Suggested next attack

Assume `a_K=0` eventually and substitute (14) repeatedly. Derive an
exponential-polynomial or valuation constraint on the edge residues
`r_{m_K,m_{K+1}}`; refuting that constraint would close `PR20/Q-9408` for the
chosen directive class.
