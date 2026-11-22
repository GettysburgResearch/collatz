# Parallel attacks using arithmetic, affine boundaries, and canonical transport

Date: 2026-11-22. **Full Collatz remains OPEN.** This checkpoint supplies
new deductions at the actual closing interfaces, including an exact
calculation of the commutator left in the latest PR177. It includes one
new Lean module with an exact finite inverse-set construction. No
unproved closing statement is introduced as a Lean axiom.

## 1. Exact evaluation of the latest canonical commutator

PR177 advanced during this pass to
`e4ca639326bac73da8c2a698dec8a749e5efbe68`. Its S-unit argument proves
upper Banach density zero for times of bounded binary run count on an
escaping odd orbit. Its energy calculation gives finite original-charge
forcing for every weight `rho^runs` with `1 < rho < 4^(1/40)`, but leaves
the multiplication/transport commutator in equation (47).

[EXACT_RUN_WEIGHT_COMMUTATOR.md](EXACT_RUN_WEIGHT_COMMUTATOR.md) evaluates
that term. Put `w_L=min(rho^runs,rho^L)`. For finite Green depth M, its
signed boundary-drift contribution tends to zero **uniformly in M**, at
each fixed L. The proof controls the negative part of the transported
measure by the unchanged canonical source:

\[
\bigl(L(\nu R_M^2)-\nu R_M^2\bigr)^-\le2d.
\]

Future upper and lower averages of the bounded run weight then pay both
signs of the drift, including killed sources. The full result is

\[
\lim_{N\to\infty}\sup_{M\ge1}\mathfrak C_{N,M}(w_L)
=2\rho^L b_\infty
-2\sum_{E\,\mathrm{escaping}}F_E\sum_{x\in E}d(x)w_L(x),
\]

where `F_E=D_E/c_E` and `b_infinity=sum_E D_E^2/c_E` are the existing
canonical component quantities. The subtracted term is bounded
independently of L by the finite forcing constant. Thus this exact
calculation retains a leading coefficient `2*b_infinity`; it does not
provide the cutoff-uniform upper bound that would force that coefficient
to be zero.

This is a written deduction from the pinned canonical construction and
PR177's S-unit consequence. Those inputs are not formalized in this new
Lean module. The independent scoped review is in the accompanying report
directory.

## 2. Fixed ordinary traces now control the actual moving roots

[MOVING_CESARO_FIBRES.md](MOVING_CESARO_FIBRES.md) imports the ordinary
mean-absolute trace in the pinned Valbuena manuscript and the repository's
finite common contact measure. Its ordinary density is called h; this
is not the function named `G(n)/n` in some other repository notes.

For each original nonperiodic positive odd ternary unit p, retain
`q_k=U^k p` until killing. If `D_j` is the finite ternary density, then

\[
\lim_{R\to\infty}\sup_{k:\,q_k\text{ retained}}\frac1R\sum_{r<R}
\left|\frac{D_{k+r+1}(q_k)}{h(q_k)}-1\right|=0.
\]

The joint real/ternary statement is stronger than convergence of one
averaged measure: the **mean of the per-depth bounded-Lipschitz
distances** tends to zero, uniformly in k. The proof preserves the
terminal ternary digit, possibly negative centered contact clocks, the
real normalization, and the original `n^-4` label weights.

This closes a moving-clock comparison that a fixed-root or
almost-everywhere fibre statement alone does not establish. It has no
quantitative rate and does not make the ordinary escape amplitude small.
Indeed, the actual inverse prefix returning to the same original p gives
the explicit positive submeasure in equation (32).

The input from *A positive semicontinuous density for the Syracuse
stationary law* is pinned to commit
`a7275d5a73814d3d9a400c6fe6577de9542b03a3`, Corollary `cor:integer`,
equation `eq:cesaro-absolute`. Its stated result and normalization were
read independently in two lanes; its analytic/formal dependencies were
not independently replayed. Accordingly, this whole analytic conclusion
is explicitly conditional on those imported results.

### A rigorous tail comparison and its remaining finite term

[TILTED_RENEWAL_FINITE_IMMIGRATION.md](TILTED_RENEWAL_FINITE_IMMIGRATION.md)
uses the Kesten tilted gap law `3/4^e`. Its finite ternary trace has the
exact ordinary expression

\[
T_j(q)=\sum_{U^jx=q}A_j(x)^2,
\qquad
\sum_{j\ge0}\frac{T_j(q)}{q^2}\le\zeta(2)
\]

for every nonperiodic odd q. Thus its mean over **any** R consecutive
inverse depths is at most `zeta(2)/R`, uniformly in q and the initial
depth. The final nonunit inverse endpoints are included here.

Conditional on the scalar Kesten–Goldie tail input recorded in the note,
this budget and the existing reciprocal-path tail bound give a real-tail
inequality with a uniformly vanishing tilted term and a finite ordinary
first-entry term. For retained q_k from a fixed original nonperiodic
positive odd ternary unit p, the aligned Cesàro average of that finite
term converges uniformly in k to

\[
I_M(q_k)=\frac{h(q_k)}{q_k}\Pr_{q_k}^h(\text{hit the finite ancestor set}).
\]

On an escaping original path it still has a positive contribution from
its last small ancestor. The note proves this term instead of assuming
that finite-quotient tail convergence controls an arbitrarily fine
moving ordinary residue.

## 3. Exact block integrality and finite source sets, with Lean

[BoundedLanguage.lean](BoundedLanguage.lean) proves the following for
every affine block `(u*x+c)/v`, with `u>1` and coprime integer u,v. If
`c_e` is its full repeated correction, then

\[
\exists q\in\mathbb Z:\ v^e m=u^e q+c_e
\quad\Longleftrightarrow\quad
u^e\mid (v-u)m-c.
\]

If the defect is zero, every integral inverse source is the same endpoint.
If it is nonzero, Lean proves an effective exponent cutoff. An executable
finite set, filtered by the exact divisibility condition, has exactly the
permitted sources. Lean then proves the exact backward finite-set
recursion and finiteness for an arbitrary finite ordered list of blocks,
with all repetition exponents varying independently. The constructor
`Block.ofCounts` proves the hypotheses for `u=3^s`, `v=2^L`, `s>0`.

[BOUNDED_LANGUAGE_SOURCE_RIGIDITY.md](BOUNDED_LANGUAGE_SOURCE_RIGIDITY.md)
gives the written word-level consequences. With a uniform zero-run bound,
a finite dictionary and a bounded number of powered factors cannot cover
cofinal complete sources to eleven. More strongly, any **regular language
consisting entirely of valid complete words** to a fixed endpoint, with
uniformly bounded zero runs, realizes only finitely many sources. A
regular superset, or finite control coupled to unbounded arithmetic
memory, does not satisfy this hypothesis.

The valuation-optimal cutoff, word-to-affine translation and physical
parities, all-zero block treatment, and automata corollary are written
proofs. The Lean claim is the exact arithmetic and finite recursion
described above; the split is recorded in the build receipt.

### Applying the deep integral-quotient theorem to complete cycle words

[FIXED_BLOCK_INTEGRAL_RIGIDITY.md](FIXED_BLOCK_INTEGRAL_RIGIDITY.md)
applies Corvaja–Zannier (2002), Theorem 2 and Corollary 1. For any fixed
finite block list and affine repetition schedules, infinitely many
integral **full cycle quotients** force the whole quotient to be one
constant integer. The proof establishes root-group confinement and uses
the complete numerator/denominator bidegree to force a constant; it does
not test only a proper denominator factor.

When every block varies, all blocks have the same affine fixed point.
Fixed connecting buffers are retained and can join different phases.
The [regular-cycle corollary](REGULAR_CYCLE_LANGUAGE_COROLLARY.md) follows
by pumping: a regular language consisting entirely of valid nonempty
integral cycle words has finitely many distinct realizers. These results
still allow repetition of any one putative nontrivial positive cycle.

## 4. The adaptive sibling attack

[ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md](ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md)
constructs an actual inverse-tree injection by changing gap exponents.
For retained unit roots with the same residue modulo three, it proves
`V^[r](y) >= 16^(-r) V^[r](x)`. A signed-exponent bijection expresses the
entire accumulated cost through the paired terminal-height ratio.

The proved cost does not yield the inverse-logarithmic sibling leakage
needed to contradict the finite incoming-current budget on escape. No
bound on the required obstacle depth or paired terminal-height ratio
has been obtained. The accompanying reversible-recurrence calculation
overlaps the independently published result in refreshed PR177; it is
retained as a checked hypothesis test, not an additional advance over
that commit.

## 5. Verification and exact scope

- Two new project files were freshly compiled with Lean 4.34.1,
  `warningAsError=true`, and `autoImplicit=false`.
- A separate import/audit checked 16 declarations, including the block
  constructor. All reported axioms are confined to `propext`,
  `Classical.choice`, and `Quot.sound`.
- This module uses pinned Mathlib
  `d13f23b723b8a846827a245b89c10fc7d3f11612`. Its compiled dependencies
  were reused; the manifest lists 2,450 loaded module names, including
  the checked module, rather than claiming 2,450 source rebuilds.
- The prior 21-source core-only build remains byte-for-byte unchanged.
  It was checked by source identity and not rerun.
- The report directory contains source pins, exact build commands,
  source hashes, and scoped internal proof reviews. Repository integrity
  checks are separate from written mathematical proof review.

[Build and review reports](../../../reports/lean-global-closure-20261121/nov22/machinery/)

To rebuild only the new module, use `build_bounded_language.py` with
`--lean`, `--mathlib`, `--deps`, a fresh external `--output` directory,
and an external `--receipt` file. The driver verifies the compiler and
Mathlib pins, compiles the two sources, and writes the audit and import
manifest. No legacy project object is imported.

The remaining closing task is still to eliminate the positive ordinary
escape charge or force original-target descent for arbitrary adaptive
words, and separately exclude nontrivial positive cycles. Neither the
new exact commutator nor the new language rigidity supplies that final
vanishing or descent argument.
