# Global-blocker review — ordinary extraction versus full-denominator closure

**Agent:** `gpt56-cycle-01`  
**Issue:** `#55`  
**Review target:** PR `#57`, with independent comparison to PR `#56` and the current repository map  
**Date:** 2026-07-25  
**Status:** no counterexample; exact review and exhaustive periodic-schedule exclusion

## 1. Question asked

The requested reset was to stop treating the following as progress toward the
full objective unless they close the missing implication:

- longer finite-prefix survivors;
- another amplifier or encoding;
- bounded support or finite grammar exclusions;
- growth, refund, or prime turnover conditional on an infinite path;
- proper-factor divisibility for a proposed cycle.

The audit therefore asked only:

1. what exact inference is repeatedly missing between finite compatibility and
   one ordinary infinite orbit?
2. can that inference be supplied from the common properties already proved?
3. if not, can the shared proof schema be refuted?
4. is there one restricted decision whose positive side gives a candidate and
   whose negative side eliminates an exhaustive architecture?

## 2. Blunt answer

The leading positive infinite-orbit programs have not crossed the ordinary
existence boundary.

Their common logical shape is

\[
\forall n\ \exists x_n>0
\text{ satisfying the first }n\text{ gates},
\]

and often also

\[
\exists\alpha\in\mathbf Z_2
\text{ satisfying every finite gate}.
\]

The counterexample objective needs

\[
\exists x\in\mathbf Z_{>0}
\text{ satisfying every gate}.
\]

The exact missing implication is an **archimedean height bound on the initial
ordinary roots**.  For genuinely nested positive seed sets `S_n`, with
`m_n=min S_n`, PR `#57/T-7601` proves

```text
one ordinary all-time seed
<=> sup_n m_n < infinity
<=> m_n eventually stabilizes.
```

No audited positive lane proves this bound or an equivalent eventual-zero
canonical residue theorem.

## 3. Why compactness, refund, and growth cannot supply extraction

PR `#56/R-7801` provides a universal countermodel.  Given any nonordinary
nested dyadic completion, one can decorate it with exact odd-over-dyadic affine
maps such that:

- every finite cylinder has infinitely many positive ordinary roots;
- every legal finite step is integral and positive;
- the expansion factor can exceed any prescribed sequence;
- the infinite inverse-limit path is unique;
- no ordinary integer realizes the complete path.

The construction was independently checked algebraically in this pass.  Its
meaning is architecture-level, not Collatz-specific: no theorem using only
nested congruences, finite compatibility, inverse-limit compactness, and
conditional expansion can produce an ordinary seed.

A successful positive theorem must use a source-specific global relation absent
from that countermodel, such as:

- bounded canonical least roots;
- eventual-zero pulled-back residue blocks;
- a seed-preserving finite invariant containing one explicit initialization;
- a global ranking contradiction on the least roots;
- or a complete finite cycle equality.

## 4. Independent verdict on PR #57

The core packet reconstructs successfully.

### `D-7601`

The distinction among finite compatibility, inverse-limit compatibility, and
ordinary extraction is correct.  One minor presentational note is that the
example `S_n={n,n+1,...}` is a generic nested-set example rather than a native
union of complete residue cylinders.  The noninteger `2`-adic branch is the
correct native cylinder counterexample.

### `L-7601`

Passed.  A compatible canonical residue branch represents a nonnegative
ordinary integer exactly when its appended blocks are eventually zero.  It
represents a negative integer exactly when its blocks are eventually maximal.
For a positive counterexample only the zero face is relevant.

### `T-7601`

Passed.  Nestedness makes the least roots nondecreasing.  A common seed bounds
them; a bounded nondecreasing integer sequence stabilizes; and a stable minimum
belongs to every earlier set by nesting.

This theorem is exact but not a hidden breakthrough by itself.  Proving its
positive side for a fixed counterexample machine already constructs the
restricted counterexample.  The genuine reduction is the **two-sided** decision:

```text
bounded/stable -> explicit seed;
divergent      -> exhaustive architecture eliminated.
```

### `T-7602`

Passed.  Every finite shortcut parity word occupies exactly one class modulo
`2^n`.  Every infinite word determines one `2`-adic seed.  The periodic word

```text
(1110)^infinity
```

has

\[
T^4(x)=\frac{27x+19}{16}
\]

and unique completion

\[
x=-\frac{19}{11}.
\]

Thus exact finite realizability, computability, inverse-limit existence,
supercritical drift, and conditional growth coexist with failure of positive
ordinary extraction.

### `T-7603`

Passed as an exact restricted decision.  For the six-branch rational-base
machine, boundedness of one deterministic least-root sequence is equivalent to
one all-time positive root.  Stabilization would provide the actual seed for
physical replay; divergence would eliminate the complete fixed six-branch
architecture.  The map to a Collatz orbit remains branch-qualified by the cited
PR `#45` / PR `#50` conjugacy.

## 5. New theorem from this review

The explicit ghost of `T-7602` extends to the complete eventually periodic
class.

For a parity block `w` of length `L`, with `s` odd branches,

\[
T^L(x)=\frac{3^s x+C_w}{2^L},
\qquad C_w\ge0.
\]

The periodic schedule `w^infinity` has unique completion

\[
\boxed{x_w=\frac{C_w}{2^L-3^s}.}
\]

Therefore:

- if `3^s>2^L`, the completion is negative;
- if `3^s<2^L`, it is positive and ordinary exactly when the full denominator
  divides `C_w`, in which case it is a positive cycle;
- otherwise the canonical least positive roots of the repeated finite prefixes
  grow exponentially, with an explicit periodic coefficient multiplying
  `2^(mL)`.

This is `L-7501`.

If a positive ordinary orbit has an eventually periodic parity tail, its state
after the finite prefix is the periodic completion above.  It must therefore
lie on a positive cycle.  Hence

\[
\boxed{
\text{no positive divergent Collatz orbit has eventually periodic parity or
accelerated-valuation data.}}
\]

This is `T-7501`.  It eliminates every autonomous bounded-state
schedule-first counterexample proposal over a fixed finite block alphabet.

## 6. What is genuine progress in the repository

The program is not wholly circular.

The following are genuine because they decide an exhaustive declared class or
close an exact implication:

1. the frozen corrected phase-34 class is crossed negatively by PR `#33`, with
   independent reconstruction in PR `#44`;
2. fixed-modulus PDR lassos and several periodic/low-complexity completion
   formats are proved to be ghosts;
3. the positive cycle lane has exact full-denominator equations and at least one
   legitimate mixed-place route by which sufficiently small residue plus
   sufficiently large divisibility would force equality;
4. the six-branch and refund lanes have been reduced to deterministic ordinary
   root problems rather than externally prescribed schedules;
5. `T-7501` now closes the entire eventually periodic parity class.

## 7. What is treading water relative to the full objective

The following may be mathematically correct and reusable, but they do not move
the current global blocker unless connected to the initial least roots or the
whole cycle denominator:

- increasing finite survival depth;
- proving that a hypothetical path grows faster;
- proving that its runtime quotient refunds permanently;
- showing it has capacity for more future digits;
- finding finite SCCs or modular lassos;
- conditional fresh-prime turnover;
- adding another encoding of the same inverse-limit point;
- satisfying more proper factors of `2^A-3^k`;
- finding a closer real near-integer without crossing a mixed-height equality
  threshold.

The issue is not that these results are false.  It is that the unproved
quantifier remains unchanged.

## 8. The exact restricted global targets

### Ordinary-infinite-orbit target

For one fixed machine, define complete nested seed sets `S_n` from the same
initial positive integer and attack only

\[
\boxed{m_n=\min S_n.}
\]

A proof of boundedness must produce eventual stabilization and therefore one
explicit all-time seed.  After physical replay, that seed may enter `K-####`
review.  A proof that `m_n->infinity` eliminates the entire machine.

The six-branch chart is the cleanest current target because it is deterministic,
has one canonical rational-base digit map, and has no external directive.

### Positive-cycle target

For a finite valuation word, attack only

\[
\boxed{C=N(2^A-3^k)}
\]

for one positive integer `N`, followed by exact valuation replay.  A proper
factor, local congruence, or real near-integer is useful only if a proved global
height argument forces the entire equality.  A hit immediately gives a finite
candidate; a no-go theorem can eliminate an exhaustive grammar.

These two blockers are distinct.  Ordinary extraction is not solved by cycle
factorization, and nested-cylinder compactness is not needed for a finite cycle.

## 9. Is the new target genuinely weaker than Collatz?

The answer must be split carefully.

- **Positive side:** “the six-branch minima stabilize” is not logically weaker
  than “Collatz is false.”  It is a specific sufficient statement whose proof
  would already furnish a counterexample.
- **Negative side:** “the six-branch minima tend to infinity” is genuinely
  weaker than Collatz.  It eliminates one exhaustive subsystem and says nothing
  about other orbits.
- **Two-sided decision:** deciding boundedness versus divergence is a narrower,
  well-posed problem than Collatz because either answer has a complete declared
  consequence for one architecture.
- **Periodic theorem:** excluding all eventually periodic schedules is
  genuinely weaker and is now proved unconditionally.

## 10. Final disposition

No ordinary extraction theorem was found for an unrestricted positive lane, and
no full-denominator positive cycle was produced.  It would be misleading to
claim otherwise.

The real advances of this pass are:

1. independent validation of the exact blocker packet;
2. a universal no-go interpretation from the affine countermodel;
3. a complete cycle-or-escape theorem for every eventually periodic shortcut
   schedule;
4. a strict research gate for future contributions:

```text
ordinary lane: change the bound or recurrence for m_n;
cycle lane:    change whole-denominator divisibility or exact replay;
otherwise:     record the result as infrastructure, not global progress.
```

## 11. Files added

```text
research/ordinary-extraction-review/claims/L-7501-periodic-shortcut-fixed-point.md
research/ordinary-extraction-review/claims/T-7501-no-eventually-periodic-divergent-parity.md
research/ordinary-extraction-review/REVIEW_MATRIX.md
research/ordinary-extraction-review/README.md
reports/gpt56-cycle-01/2026-07-25-55-global-blocker-review.md
```

No experiment was introduced because the new implication is completely
algebraic.