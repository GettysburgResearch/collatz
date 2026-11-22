# Coordinating reconstruction of the new arithmetic and transport claims

This record concerns the exact new files below, not every upstream source.
The writer coordinated the packet and independently reconstructed the
displayed arguments after the separate lanes derived them. It is not an
external human review, an acceptance decision, or a proof of Collatz.

## Independent-exponent cycle classification

File: `arithmetic/FREE_EXPONENT_CYCLES.md`.
SHA256: `f27af626f9de6beaf07562f0a4ef4a1240f99eb5cab04c99a50789a048a4d960`.

**Verdict: VERIFIED as a written deduction from the stated published
Matveev theorem and the exact finite ordinary parity separation.** The
finite core is separately compiled in `BlockCompression.lean`; the
transcendence and classification argument is not part of that Lean proof.

The reconstruction checked the following load-bearing steps.

1. If a positive ordinary segment follows `V^k`, comparing its original
   source with the actual endpoint after one copy gives the same first
   `(k-1)|V|` parity digits. Unless the two integers coincide, their nonzero
   displacement is at least `2^((k-1)|V|)`. The generic bound on an ordinary
   iterate gives both BC3 and the quadratic exit bound BC4. No final-tail
   parity or divisibility assumption is missing.
2. The product budget retains each original successive source. Multiplying
   the head estimate by the tail estimate at its actual endpoint changes
   exponent `e` to `1+2e`; this gives `2^r-1`. The short-period branch is
   pulled back through the actual preceding clocks. The sharper written
   alpha-chain follows from `T(x)+1<=(3/2)(x+1)` and the displayed geometric
   sum; it is not needed for the conservative effective cutoff.
3. Across repeated copies of an affine atom the boundary values are
   monotone, even though the individual shortcut steps need not be. Every
   state inside a copy is at least its start divided by `2^B`. Therefore
   the least block boundary satisfies `m_b<=2^B m`, resolving the necessary
   distinction between boundary minimum and whole-cycle minimum.
4. Multiplying all actual cycle ratios gives the positive form
   `Lambda=N log2-s log3`, with `0<Lambda<N/(3m)`. There is at least one odd
   step, and `s<=N`. Matveev's primary Corollary 2.3 was read directly:
   equations 1.1, 1.3, 1.4, 2.4, 2.6 give the form, coefficient parameter, height
   floor and explicit constant. For the real field Q and algebraic numbers
   2, 3, both chosen heights exceed 0.16, `B*=N`, and
   `C1(2)<=2^32`. Thus `K=2^33` safely gives BC12.
5. Substitution of the polynomial upper bound for `m_b` into the compression
   bound yields BC14. For `N>J(r,B)`, the elementary
   `log2 N<=sqrt N` and the two strict half-bounds contradict BC14. This is
   a genuine terminating bound, not only a polynomial bound on a cycle
   minimum.
6. A supplied word can repeat a shorter cycle arbitrarily often. Taking one
   primitive ordinary period costs at most one extra partial atom, giving
   `J(r+1,B)`. Enumerating full affine numerators and denominators below
   that finite period cutoff, then actually replaying positive candidates,
   is complete. The finite phase automaton supplies ultimately periodic
   allowed counts for each fixed atom and each pair of intermediate phases;
   finite unions of their Cartesian products are the asserted semilinear
   tuple description.

The bound does not classify arbitrary cycles with unbounded atom length or
unbounded number of power blocks. No enormous enumeration was executed.
The comparison with classical fixed-m-cycle results is credited without a
historical novelty claim.

## Complete-source asynchronous boundary residue

File: `transport/ASYNCHRONOUS_RESIDUE.md`.
SHA256: `270b06633aa9ca1c749ef59c2398d196e46aed4a4fe984b09a47081c208dca80`.

**Verdict: VERIFIED under the displayed ordinary harmonic-reference input
A2.** The upstream existence/population argument for that reference was
not re-proved. The review does not promote it from its source-qualified
status.

For a singleton source, injectivity before the first periodic state makes
its occupied endpoints distinct. Harmonicity makes the reference mass
nondecreasing on this segment, proving A7 and hence the exact weighted
triangle bound A6. For two sources, all common points form either an empty
set, a finite common tail before killing, or one infinite common tail.
The first meeting clocks are both retained in A12 and A13. Abel and Cesaro
means of the convergent inverse reference give the same component-capacity
limit. The summable source-pair majorant in A14 is precisely S(a)^2, so the
passage from finite support to all original source pairs is justified.

The fixed projection pi removes initial factors of two and, only for a
ternary nonunit odd state, takes one actual accelerated odd step. It remains
an ordinary orbit point, and pi(n)<=2n. The original weight n^-4 is never
changed to pi(n)^-4. Consequently the square-root domination uses
sum n^-7/2<=7/5 and gives exactly 98/(25gamma).

For a source entering a nontrivial cycle of length p, its normalized Abel
mass converges to 1/p at each cycle point. Its normalized l2 norm is at most
one, uniformly in the discount. Absolute summability of the original
source law permits the Hilbert-norm limit through all sources, even with
infinitely many possible cycles. The resulting second-order residue is
the sum of squared full basin masses divided by the cycle lengths. In the
hybrid norm, its existence forces an infinite first-order residue; absent
such cycles, the escape formula gives the finite residue. Positivity of
every original atom makes the zero-residue criterion sensitive to every
ordinary input, including both failure alternatives.

Three notation errors in the first draft's displays were corrected before
the reviewed hash. No mathematical or quantifier gap was found in A1--A24
under A2. The important missing assertion is vanishing of the actual
critical residue, not its proved boundedness on the nonperiodic domain.

## Separate reviews and formal boundary

The transport lane independently reconstructed the operator classification
W7--W13 in `transport/OPERATOR_REVIEW.md`. It also reconstructed the carry
packet at the exact hashes in `transport/MERGER_REVIEW.md`. Arithmetic
supplied the certified carry family and the separate comparison with
temporal compression. Those scopes do not certify universal capture or a
global repetition principle.

The combined 52-declaration Lean axiom audit is recorded in the execution
report. It checks the formal statements and their dependencies; it does not
convert any external analytic hypothesis or the written Matveev application
into a Lean theorem.
