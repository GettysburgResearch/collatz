# Whole-repository reassessment: exact source boxes and an elementary global count

Date: 2026-11-23. Parent: `b78819e95ee7d39f02022de991b42217821e7590`.

**Collatz remains unresolved.** This continuation reassessed the repository
and ran three parallel attacks on the current closing steps, with a fourth
line developed by the principal researcher. The main positive result is a
Lean-checked finite injection that keeps the complete word, its two clocks,
and the original ordinary source. It gives a precise decomposition of the
actual collision problem into contributions from different source boxes.
A separate elementary proof strengthens this branch's general orbit-count
input; that bound is a reconstruction, with stronger prior literature
explicitly credited.

The new work does not restate the preceding checkpoint as a fresh result.
Its simultaneous pressure maximum and full numerical gcd transport are
preserved in [`closure-round2-20261123`](../closure-round2-20261123/README.md).

## 1. Exact source boxes control actual residue collisions

Take a literal odd Collatz window with `m` odd transitions, total binary
clock `A`, source `p`, and endpoint `q`. Keep its complete ordered carry

\[
C=\sum_{i=0}^{m-1}3^{m-1-i}2^{g_1+\cdots+g_i},\qquad
2^Aq=3^mp+C.
\]

The new finite theorem fixes the three integers

\[
\left(A,\left\lfloor C/3^m\right\rfloor,
          \left\lfloor p/2^A\right\rfloor\right).
\]

Within that box, `q mod 3^m` determines the complete word, its original
source, and its ordinary endpoint. On an injective ordinary orbit it
also determines the occurrence index. The absolute source height can be
arbitrarily large.

The proof first decodes a complete word from its length, odd count and
carry. The endpoint residue determines the carry remainder; its supplied
quotient therefore fixes the carry. Equal carries then imply equal source
residues modulo `2^A`, and the source quotient fixes the source itself.
All affine terms remain present.

For arbitrary original nonnegative weights `t_j`, the collision energy
inside one box is exactly its ordinary diagonal `sum_j t_j^2`. A wider
carry-quotient interval of width `R` allows at most `R` distinct words per
residue. In that case the bound keeps repeated occurrences:

\[
\operatorname{Col}_{3^m}(\sigma)
\le R\sum_w\left(\sum_{j:W_j=w}t_j\right)^2.
\]

The [full argument](ACTUAL_COLLISION.md) supplies the physical carry-width
bound, translated source-interval version, and same-law inverse-window
consumer. It preserves all cross-box terms. Their accumulation is still
uncontrolled; the finite injection is not a global mixing theorem.

The ordinary diagonal also gives a necessary precision budget. For the
source-qualified retained inverse law with `N=M+1` roots, a full collision
upper of order `o(sqrt(m)*3^(-theta*m))` requires

\[
N\sqrt m/3^{\theta m}\longrightarrow\infty.
\]

The lower-bound admissibility condition `m^2=O(M)` alone does not imply
this. In particular a precision comparable to `sqrt(M)` cannot satisfy
the proposed full-collision upper. The published lower bound remains
usable at logarithmic precisions and sufficiently large source windows.

**Formal scope:** sixteen statements in [CarryFibers.lean](CarryFibers.lean).
The exact physical identities are explicit hypotheses of its endpoint
consumers. The infinite harmonic-flow construction and collision lower
bound remain pinned, source-qualified inputs in the written application.

## 2. All separated visits admit a direct critical-exponent count

The [elementary reconstruction](GLOBAL_ORBIT_COUNT.md) proves, uniformly
for every forward-invariant set `S` of positive odd integers on which the
odd map is injective,

\[
\#(S\cap[1,X])=O\!\left(
\frac{X^\theta}{\sqrt{1+\log X}}\right),\qquad
\theta=H_2(\log_3 2)=0.949955527188\ldots.
\]

Choose one common odd-step count near `log_3(X/8)`. Large total binary
clocks send their original sources into the same set below `X/2`, and
injectivity charges them there. Small total clocks occupy a binomially
bounded collection of complete ordinary residue classes. Iterating that
height reduction gives the displayed estimate, without requiring all
intermediate orbit values to stay below `X`.

This strengthens the local `4X^(39/40)` input used in our previous
pressure proof. It gives distinct-state moments for `s>theta` and a
smaller correction-product loss at a large component floor. It does not
prove convergence at the critical Mellin exponent or eliminate a
positive escaping pressure atom. The note credits stronger pre-existing
literature and makes no record claim.

**Formal scope:** three finite statements in
[OrbitCounting.lean](OrbitCounting.lean) prove the complete-carry bound,
high-clock height compression, and injective cardinal charge. Binomial
asymptotics, the infinite scale recursion and the integral consequences
are supplied as written proofs and independently reviewed.

## 3. Two direct closing attacks that did not close

[TRIADIC_CLOSURE.md](TRIADIC_CLOSURE.md) attempts to construct PR178's
finite triadic certificate for the unchanged ordinary source. The previous
pressure maximum makes every complementary real prefix contract by less
than `(3/4)^K`. However, legal numerators at a fixed denominator still lie
in one translated progression modulo `2^K`. Contraction does not control
that translation. Optimizing the denominator within the candidate's own
height permits only `O(sqrt K)` exponents. The note computes exactly why
the obvious pigeonhole argument gives an extra forbidden odd denominator
and insufficient height saving. Its source-height capacity bound limits
this particular conservative certificate, without claiming that any
ordinary source fails at all later clocks.

[COMPLETE_CYCLE.md](COMPLETE_CYCLE.md) attacks the complete numerical zero
residue by splitting the full ordered carry at arbitrary scales. At a
short enough scale the zero equation is a partial matching between block
words. But after conditioning on that equation the blocks can determine
each other completely. Iterating an unconditioned small-atom estimate
therefore fails. The known cycle's repetitions supply an exact four-pair
control. The resulting single matching bound is weaker than the existing
polynomial zero-fibre census; no cycle exclusion is claimed.

These failed attempts are kept close to their exact first unsupported
inferences. No new Lean wrappers were added merely to increase the
number of conditional closing theorems.

## 4. Repository scope and the next central task

The [reassessment](REPO_REASSESSMENT.md) connects the older centered,
algebraic, mass, renewal, rank, extraction and rewrite families to the
current source, cycle and actual-law routes. The report inventory records
all 145 PR metadata entries, 122 open and 23 closed, at the inspection
snapshot. Selected current and older source files were read in depth;
the inventory is not a claim to have rechecked every proof or replayed
every branch.

The immediate mathematical target is now sharper: control the mass and
residue alignment of the **different boxes actually occupied by one
unchanged orbit**, at a precision compatible with its atomic diagonal.
Any proposed bound must pay for all omitted inverse branches and cannot
replace the moving law by a fresh independent distribution. The triadic
source construction and full-denominator zero exclusion remain separate
possible routes to a complete proof.

## 5. Verification and reproducibility

The [report directory](../../reports/2026-11-23-whole-repo-round3/README.md)
records exact reviewed bytes, fresh Lean compilation and axiom audits,
normal/optimized exact replay, and the complete-checkout integrity gate.
The new modules import the unchanged chronological carry definitions from
the previous high-variance checkpoint. All older tracked Lean files are
preserved byte-for-byte.

[exact_replay.py](exact_replay.py) independently exercises complete carry
decoding, original-source box injection, repeated-word mass, cross-box
terms, physical carry width, exact binomial identities, and finite
separated-visit charging with an explicit terminal allowance. It does not
fabricate an infinite orbit or use bounded experiments to infer the
conjecture.
