# Scope of the final internal reconstruction reviews

Date: 23 November 2026. These are collaborating-agent mathematical reviews,
with contributions disclosed. They are not external peer review, an audit
of every upstream branch, or proof of the full Collatz conjecture.

## Full-word cycle theorem

The `cycle_ideal` agent authored the balanced-word construction. The
`escape_rigidity` agent independently reconstructed its arbitrary-modulus,
arbitrary-height base theorem, and the `source_surgery` agent separately
reconstructed Sections 1--5. Both found the complete carry, congruences,
parity realization, primitive marker and every-state height argument sound.

The amplification idea was suggested by `escape_rigidity`, and the cycle
author developed the quadratic-height subsequence. Its review is correctly
classified as contributor verification. Root also reconstructed the final
argument, including the positive backward series, upper-convergent sign,
integer amplification condition, and constant 3888. The finite-precision
qualification is essential and retained.

The full statement and exact hashes are in [CYCLE_REVIEW.md](CYCLE_REVIEW.md).
The final note differs from its reviewed mathematical draft only by two
status/replay paragraphs; the reviewer reversed those edits and recovered
the original hash. Both identities are recorded there.

## Finite Lean implementation

Root authored `CycleWordAlgebra.lean`. Both the cycle author and the
source-surgery agent reconstructed all twelve bodies against the complete
chronological word convention; the escape reviewer inspected them too.
The declaration-level proof scope is correctly limited to finite algebra.

The `source_surgery` agent authored `ForcedRoute.lean`. The escape reviewer
reconstructed its written proposition and all twelve public statements;
see [SOURCE_ROUTE_REVIEW.md](SOURCE_ROUTE_REVIEW.md). Root separately checked
the actual step equation, cap-four classification, route induction and
the final changing-source quantifier. The generic Edge predicate guards
the output; actual inputs in this family are supplied by the proved value
residues. A documentation clarification states that distinction. The final
bytes were freshly recompiled and audited after the clarification.

## Standalone doubling/normality control

The source-surgery agent independently reconstructed the control in
`ESCAPE_RIGIDITY.md`, at SHA256
`12394f74ace03beb3cc6e5a4afd4ee20c7826f9bd4f21355d9abbb085c245580`.
Root independently checked the same probability argument.

For a fixed length L, distinct positions in a window starting at n>=L
cannot share an odd part: two such positions would differ by a factor at
least two, hence by at least n>=L. Thus each late window has uniform word
probability. Ordered pairs of positions up to X sharing an odd part number
at most X+2*sum_(s>=1) floor(X/2^s)<=3X. Each pair belongs to at most L^2
pairs of length-L windows, so the word-count variance is O_L(N). After
normalizing it is O_L(1/N). Chebyshev on N=j^2 and Borel--Cantelli give
almost-sure convergence along square cutoffs; the relative intervening
interval length tends to zero, giving convergence at every cutoff.
Countably many finite words can be handled simultaneously.

This proves the existence of exactly doubling-invariant sequences with
fair Bernoulli consecutive-word frequencies. It does not impose the odd
Collatz equation or supply the unproved regularity of the canonical escape
label. The inherited harmonic and routing inputs in that attempt retain
their source-qualified status; these reviewers did not re-audit the full
external analytic chain in this checkpoint.

## Execution is separate

Semantic reviews do not stand in for execution. Fresh Lean/audit receipts,
the unchanged checker replay normally and under optimization, exact damaged
controls, independent Fraction calculations, and the clean complete-checkout
integrity gate are separately recorded in this report packet.
