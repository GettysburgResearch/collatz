# A primitive-source moment that retains every counterexample

**Status: exact arithmetic reduction; the limiting estimate is OPEN.**

This pass tried to close the global analytic estimate, including cycles. It
found a source-side word moment with an exact, exponentially accurate
comparison to the mass of ordinary sources that have not reached 1. It
does not prove that the moment tends to zero. Unlike the earlier
correction-product moment, this moment detects nontrivial cycles as well
as nonperiodic orbits and needs no orbit-sparsity input.

The new Lean development constructs ordinary source cylinders from the
finite word equations. It does not assume a cylinder partition, a random
residue model, or convergence of any original source.

## Map and arithmetic objects

For a positive odd integer n, let

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

In particular U(1)=1. A word w=(a_1,...,a_q) has all a_i>=1. Write

\[
A_j=\sum_{i=1}^j a_i,\qquad
C_w=\sum_{j=0}^{q-1}3^{q-1-j}2^{A_j}.
\]

Let r_w be the unique positive odd representative below 2*3^q satisfying

\[
2^{A_q}r_w\equiv C_w\pmod{3^q},
\]

and let

\[
b_w=\frac{2^{A_q}r_w-C_w}{3^q}.
\]

Every word has an ordinary positive odd source b_w, with
0<b_w<2^(A_q+1), and its complete cylinder is

\[
n=b_w+2^{A_q+1}k,\qquad
U^q(n)=r_w+2\cdot3^qk,\qquad k\ge0.\tag{P1}
\]

The cylinders are disjoint and cover every positive odd source. This is
the familiar arithmetic identity from PR169, but the new Lean file
reconstructs its existence, complete inverse legality, and partition
instead of importing it as an assumption.

## Why the inverse congruence gives ordinary sources

The residue r_w is obtained by inverting 2^(A_q+1) modulo 3^q and then
choosing the representative 2t+1. To undo the last letter a_q, the full
congruence implies 2^(a_q)r_w=1 modulo 3. Thus
m=(2^(a_q)r_w-1)/3 is an integer. Because a_q>=1 and r_w is positive
odd, divisibility excludes a numerator below 3: m is positive odd.
Cancelling that last factor of 3 leaves exactly the full congruence for
the preceding word and target m. Induction realizes every inverse step
as an ordinary positive odd integer.

The finite affine identity

\[
2^{A_q}r_w=3^q b_w+C_w
\]

and r_w<2*3^q imply the source bound b_w<2^(A_q+1). Translating b_w
by a nonnegative multiple of 2^(A_q+1) preserves all exact valuations
and translates the endpoint by the same multiple of 2*3^q. Conversely,
any actual endpoint for that word is odd and has the same residue modulo
3^q, hence has the form on the right of P1. The affine identity then
forces its original source to have the form on the left. Distinct words
cannot share a source, since the source's valuations are uniquely
defined by its ordinary trajectory.

## The moment and the exact survivor decomposition

Define

\[
B_q=\sum_{w:r_w\ne1} b_w^{-4},\qquad
A_q=\sum_{\substack{n>0\text{ odd}\\U^q(n)\ne1}} n^{-4}.
\tag{P2}
\]

Every higher lift k>=1 in P1 has endpoint strictly above 1. Therefore
all higher lifts survive at time q, even when the primitive endpoint is
1. Positive summation over the complete disjoint partition gives

\[
A_q=B_q+R_q,\qquad
R_q=\sum_w\sum_{k\ge1}
       (b_w+2^{A_q(w)+1}k)^{-4}.\tag{P3}
\]

Here A_q(w) denotes the word's total valuation; the survivor mass A_q
on the left is a different object. The Lean file uses separate names
`total` and `aliveMass` to prevent this notational overlap.

The complete alphabet has an exact geometric sum:

\[
\sum_w2^{-4A_q(w)}
=\left(\sum_{a\ge1}16^{-a}\right)^q=15^{-q}.
\]

Since b_w>0 and the ordinary fourth-power zeta sum is below 2,

\[
0<R_q<\frac{\zeta(4)}{16}\,15^{-q}
       <\frac18\,15^{-q}.\tag{P4}
\]

This covers all positive valuations and all higher lifts. No finite
alphabet truncation is used. For q=0 the empty word has b=r=1, so B_0=0
while A_0 is the positive fourth-power mass of the odd integers above 1;
P3 and P4 still hold.

## Exact full-convergence criterion

The survivor indicators decrease because U fixes 1. Their summable
dominating weight is n^-4. Consequently

\[
\lim_{q\to\infty}A_q
=\sum_{\substack{n>0\text{ odd}\\
                 U^q(n)\ne1\text{ for every }q}} n^{-4}.
\tag{P5}
\]

Every individual summand is strictly positive. By P3--P4,

\[
\boxed{\text{Every positive odd source reaches 1}
       \iff \lim_{q\to\infty}B_q=0.}\tag{P6}
\]

This includes nontrivial cycles: a source on any such cycle contributes
the same n^-4 to A_q at every time, so its contribution cannot disappear
through a growing affine correction product. Even sources reduce by
halving to positive odd sources, so the left side is full Collatz.

The upper envelope B_q+(1/8)15^-q provides a finite-time quantitative
interface. If it is below N^-4, every positive odd source at most N has
reached 1 by time q. This is a consequence of retaining the same
source's n^-4 contribution; it is not an asserted bound on the envelope.

## What the closing attempt did and did not supply

The old soft potential J_q(n)^4/U^q(n)^4 equals
n^-4 I_q(n)^-4. It loses mass on every positive cycle, including a
hypothetical nontrivial one, and its mass can also move to larger
endpoints. Subtracting the primitive words with r_w=1 from the new
source denominator avoids both scope errors.

The missing estimate is now exactly B_q->0. Existing stationary
ternary estimates control endpoint residues under coefficient weights;
they do not control this source denominator. The identity
b_w=(2^A r_w-C_w)/3^q retains the affine offset, whose cancellation
cannot be discarded uniformly. Uniform sourcewise killing is also
unavailable: prescribed long initial valuation-one blocks start at
arbitrarily large ordinary sources and retain correction-product mass
arbitrarily close to one for any fixed observation length.

The latest failure-amplification results produce long blocks of a
hypothetical failed component at large height. They supply no upper
bound on the Dirichlet mass of that component, and are compatible with
finite positive mass in P5. No proof of B_q->0, and hence no full theorem,
has been obtained in this pass.

## Source scope and formalization boundary

Reviewed interfaces were PR171 at
`2bd243b3e05eaa5543adeb2894637b053c9662ca`
(`CRITICAL_NEGATIVE_MOMENT_INTERFACE.md`, `FULL_THEOREM_ATTEMPT.md`, and
`SIMPLE_PREFIX_PRODUCT_SIEVE.md`); PR173 at
`a09eb47197cd99f218b3fa013c681df65ea0f69a`
(`research/lean-shell-cover/README.md` and `ShellCover.lean`); and PR146
at `f431078244e868dc699fad011044f0d5e7f76437`
(`CRITICAL_INTERVALS.md` and `WHOLE_INTERVAL_SYNCHRONIZATION.md`).
They motivate the global boundary discussion, but none of their
asymptotic claims is an assumption of the new cylinder construction.

The companion `PrimitiveSurvival.lean` formalizes the following targets:

- `cylinderMap_bijective`: the complete ordinary word-source partition;
- `aliveMass_decomposition`: A_q=B_q+R_q;
- `wordWeight_sum`: the full-alphabet geometric identity 15^(-q);
- `liftRemainder_bound`: R_q<=zetaFour/16*(1/15)^q, where `zetaFour`
  is the actual convergent fourth-power series;
- `fullCollatz_iff_primitiveMoment_tendsto_zero`: P6, including an
  explicit equivalence with the ordinary integer map n/2 or 3n+1.

The exact Lean bound is the displayed zetaFour bound, with non-strict
inequality. The written simplification to the loose strict constant 1/8
uses the elementary zeta(4)<2 estimate; that numerical simplification is
not a separate theorem in the Lean file. The source-birth/absorption
attempt and its exact finite obstruction are in `FLUX_ATTEMPT.md`, not
part of the compiled theorem set.

Compilation uses Lean 4.34.1 and mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. From that built mathlib
checkout, run `lake env lean /absolute/path/to/PrimitiveSurvival.lean`.
The file ends with axiom checks for the four principal declarations.
The accompanying execution log records the actual final run; it is not
a proof of the still-open limit on the right of P6.
