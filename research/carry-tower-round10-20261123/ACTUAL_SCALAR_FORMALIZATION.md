# The actual scalar criterion, formalized from the Collatz map

23 November 2026. Published parent PR182:
c369ae3c426ec6aaf9a280ec9578b9910c2147d5.

**Status: the actual-map scalar construction and convergence criterion
are proved in Lean. Universal triadic membership and Collatz remain
OPEN.** This closes a formalization gap in the parent's written
criterion. It does not supply its missing universal arithmetic input.

## 1. Exact map, scalar, and source

For a positive odd natural number q, define

\[
g(q)=v_2(3q+1),\qquad
U(q)=\frac{3q+1}{2^{g(q)}},\qquad q_i=U^i(q),
\]

\[
S_N(q)=\sum_{i<N}\frac{g(q_i)}{3^{i+1}},
\qquad
h(q)=\sum_{i\ge0}\frac{g(q_i)}{3^{i+1}}.
\tag{1}
\]

[ActualScalar.lean](ActualScalar.lean) defines these objects itself:
gap uses Nat.factorization, oddMap is natural-number division,
orbit is recursion on that map, and scalar is a real tsum.
The proof first establishes the complete equation
2^(gap q) * oddMap q = 3*q+1, positivity, and oddness. There is
no abstract orbit hypothesis, custom axiom, assumed scalar recurrence,
or imported repository convergence theorem.

The written predecessor is
research/repo-synthesis-round8-20261123/GERM_BRIDGE.md, R8-G1--G2,
at the parent head above, Git blob
540110f09cf68e3309fd83fea9c7ae497536ded4.
Its actual scalar criterion is the claim being formalized.
The current file does not formalize the separate germ identity
h(q)=2B'_q(1) or any measure-theoretic theorem.

All formal declarations are in namespace
Collatz.CarryTowerRoundTen.ActualScalar.

## 2. The series exists unconditionally

**R10-G1 (actual construction and bounds).** For every positive odd q,
the actual series (1) is summable and

\[
\boxed{\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q).}
\tag{2}
\]

The construction is independent of convergence of the orbit.
The complete ordinary equation and q>=1 give

\[
2^{g(q)}U(q)=3q+1\le4q,
\quad
g(q)+\log_2U(q)\le2+\log_2q.
\tag{3}
\]

Set E(q)=1+log_2(q)/3. Since log_2 U(q)>=0, equation (3)
implies the supersolution inequality

\[
\frac{g(q)+E(Uq)}3\le E(q).
\tag{4}
\]

Induction bounds every nonnegative finite prefix by E(q).
The theorem summable_of_sum_range_le therefore proves actual real
summability before any tsum recurrence is used. Thus the Lean
convention for the sum of a nonsummable family cannot supply a false
scalar value here. Splitting the first term of this summable series
proves the recurrence.

Every odd-state gap is at least one. Comparing with the summable
geometric series gives h(q)>=1/2. Equality would, by the recurrence
and the same lower bound at Uq, force g(q)=1 and h(Uq)=1/2.
Repeating forces every actual gap to equal one. The complete equations
would then give, for every i,

\[
2^i(q_i+1)=3^i(q+1).
\tag{5}
\]

Since powers of two and three are coprime, 2^i would divide the fixed
positive integer q+1 for every i. Taking i=q+1 contradicts
q+1<2^(q+1). This proves the strict lower bound.

The principal declarations are scalar_summable, scalar_upper,
scalar_recurrence, not_all_gaps_one, and scalar_strict_lower.

### Exact finite tails

The same file proves, for every N,

\[
\boxed{h(q)=S_N(q)+3^{-N}h(q_N).}
\tag{6}
\]

Consequently it proves the actual interval

\[
\boxed{
S_N(q)+\frac{1}{2\cdot3^N}<h(q)
\le S_N(q)+\frac{1+\log_2(q_N)/3}{3^N}.}
\tag{7}
\]

These are scalar_tail, scalar_tail_lower, and scalar_tail_upper.
The endpoint is the literal actual iterate orbit q N; it is not a
chosen finite witness.

## 3. Integer scalar arithmetic forces actual convergence

**R10-G2.** If the actual h(q) is an integer, some actual iterate
of q under U is one.

The proof uses a logarithmic potential

\[
V(q)=\log q-h(q)\log2.
\tag{8}
\]

The unconditional scalar upper bound gives

\[
V(q)\ge\frac23\log q-\log2\ge-\log2.
\tag{9}
\]

If h(q) is an integer, the scalar recurrence preserves integrality
at every future actual state. The lower bound then gives h(q_i)>=1.
If the orbit never reaches one, positivity and oddness give
q_i>=3 everywhere. Combining the complete ordinary equation with
the actual scalar recurrence yields

\[
\begin{aligned}
V(Uq)-V(q)
 &=\log(3+1/q)-2h(q)\log2\\
 &\le\log(10/3)-\log4
 =\log(5/6)<0.
\end{aligned}
\tag{10}
\]

Thus V would decrease by a fixed negative amount at each actual
step while retaining the lower bound (9). An Archimedean argument
gives a contradiction. The formal theorem integer_scalar_converges
concludes exists i, orbit q i = 1.

This proof uses a different convenient potential from the parent's
written integer-scalar proof. It retains the same actual-map
conclusion and does not assume the orbit is bounded or periodic.

## 4. Full actual equivalence with a triadic rational value

**R10-G3 (formal convergence criterion).** For every positive odd q,

\[
\boxed{
(\exists i\ge0,\ U^i(q)=1)
\quad\Longleftrightarrow\quad
(\exists a\in\mathbb Z,\ r\in\mathbb N,\ h(q)=a/3^r).}
\tag{11}
\]

The denominator clears along the actual map. If
h(q)=a/3^(r+1), then

\[
h(Uq)=\frac{a-g(q)3^r}{3^r}.
\]

After r actual transitions the scalar is integral, so R10-G2 applies.
In the other direction, the complete map fixes one and has g(1)=2;
the recurrence gives h(1)=1. Backward substitution along an actual
prefix reaching one yields h(q)=a/3^N with integer a.

The exact top-level declaration is:

    theorem converges_iff_triadic (q : ℕ) (hq : 0 < q) (hodd : Odd q) :
        Converges q ↔ ∃ a : ℤ, ∃ r : ℕ, scalar q = (a : ℝ) / 3 ^ r

Here Converges q is defined as exists i, orbit q i = 1,
with the orbit from Section 1. The theorem is about the accelerated
positive odd map. No separately defined even-source or unaccelerated
map is presented as formalized by this declaration.

## 5. Formal scope, verification, and the missing assertion

All the analytic and arithmetic steps in Sections 2--4 occur in the
same Lean module. The separate execution report records a fresh
compile, compiler and Mathlib hashes, strict flags, and an axiom audit
of every new declaration. Only the usual Lean/Mathlib logical axioms
are permitted in that audit; no admitted proof is permitted.

The formalization constructs the actual infinite scalar and proves
the actual convergence conclusion, rather than only a finite
recurrence under a supplied scalar hypothesis. It remains an
equivalence. The following universal assertion is **not** a theorem
in this packet:

\[
\forall q>0\text{ odd},\quad h(q)\in\mathbb Z[1/3].
\tag{OPEN}
\]

Supplying an a and r already satisfying the right-hand side is enough
for the formal convergence theorem. No method here supplies them for
every q. The three companion attacks investigate the actual arithmetic
and return dynamics that could eventually force that missing step.
