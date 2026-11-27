# All-clock postpeak classification and limits of local analytic tests

**PROPOSED research; Collatz remains open.** This checkpoint adds a finite
criterion for an infinite family of ordinary merger questions, completes
the cyclic bookkeeping of the all-shift kernel proof, and determines how
much information several operator methods retain about a Collatz component.
The precise source files distinguish kernel declarations, written proofs,
bounded arithmetic controls, and imported results.

## A finite word fibre controls every smaller visitor

Write the original ordinary source as `n=2^H v−1`, with `v>0`. Its first
`H` odd departures reach `3^H v−1`. Let a native word `w` of length `t`,
with `f` odd and `q=t−f` even departures, continue to a target `Y`.
For its affine numerator `A_w`, put `C_w=A_w−3^f`.

Under `H≥21q+3`, a positive smaller source can reach `Y` at **any** clock
with odd count `k=H+f−d`, `d≥0`, exactly when some word `β` of length `t`
has the same signed offset and satisfies

\[
 C_\beta=C_w,\qquad 3^d2^f<2^{Q(\beta)+d}.
\]

This is a finite comparison of `t`-letter words. It quantifies over all
positive smaller sources and all lower clocks. Its sufficient direction
constructs a physical source; its necessary direction uses an integral
signed translation and a magnitude trap. The cone depends on the upper
even count, so arbitrarily long upper odd stretches are allowed.
See [the complete core statement](descent/postpeak/POSTPEAK_CORE.md) and
`cone_iff` in [CollisionCone.lean](descent/postpeak/CollisionCone.lean).

Call `w` maximal if no equally long word with that offset has more odd
departures. For `3^K | n−s`, `s∈{0,1}`, the barrier persists beyond the
peak: when `H≥21q+9K+3`, every smaller visitor uses more than `H+f+K`
odds. The proof extracts a visit to a scaled pure-ramp target before the
competing tail. The scale is a positive integer and is treated explicitly;
the comparison is still with the original source `n`.

The root's [scaled finite-budget consumer](root/phase2/SCALED_BUDGET.md)
preserves the first checkpoint's 648-source certificate. For `K≥84` and

\[
 H\ge21q+9(K+12)+3,
\]

the odd count is greater than `H+f+K+12`. No extra convergence oracle or
lower clock cutoff is introduced. Maximality remains a real hypothesis:
matching-offset words of greater weight give explicit cheaper visitors.

The unscaled ternary barriers and prepayment architecture are credited to
PR146 in the first checkpoint. PR201 already has a compensated-peak
classification with a lower-clock restriction and separate unrestricted
families. The new core supplies all cofactors, all lower clocks, the
upper-even-count cone, and its scaled prepaid consumer.

## Cycle complexity and the whole denominator

[CyclicAllShift.lean](cycles/spectrum/CyclicAllShift.lean) now derives the
all-shift bound directly from an actual primitive cyclic branch sequence.
It proves the circular mismatch balance and distinctness needed by the
first checkpoint's physical-pair kernel. This closes the earlier gap
between that kernel's hypotheses and the full cyclic statement.

The written [collective shift estimates](cycles/spectrum/COLLECTIVE.md)
also bound the number of small-distance shifts. If `B` proper shifts have
at most `k` mismatches, `k≥2`, and
`n≥2k(1+log₂(d(m+1)))`, then `B<3(log₂3)k²`.
Their subgroup forces an approximation by a genuinely periodic word.
A separate positive-quantile statement uses only the irrational limiting
odd density and is explicitly identified as a general word argument.

For an arbitrary mechanical factor of any length and slope, the
[Levenshtein bound](cycles/spectrum/MECHANICAL_DISTANCE.md) is

\[
 n<(E+2)\bigl[1+\log_2(d(C+1))+(\log_2 3)(E+2)\bigr],
 \quad C=\frac{u2^n}{3(2^n-3^u)}.
\]

This retains the complete reduced denominator. PR196 already contains the
clean-window edit argument in odd-clock and canonical-digit settings;
the present transfer treats binary shortcut periods, all slopes, and
arbitrary insertions and deletions. The note states the distinctions.

The [geometric-band estimate](cycles/spectrum/BAND_CROSSINGS.md) combines
the cited factor-three residence theorem with the area under the actual
closed walk of band indices. For every grid offset, its crossing count
`c` obeys

\[
 n\le c\,[2\log_2(2m+1)+3]+\tfrac12(\log_2 3)c^2.
\]

The explicit ordinary-cycle numerical corollaries import the identified
height, period, and residence inputs. Those external proofs and large
computations were not rebuilt in this sprint. The Lean numerical
consumers check their stated rational arithmetic, not the external inputs.

Primitive positive rational controls have arbitrarily many four-mismatch
row shifts, critical integer weight, growing minima, vanishing reciprocal
defect, and logarithmically rough full denominators. Nevertheless their
reduced denominator has logarithm asymptotic to the full period. This
shows why local rational controls cannot establish ordinary realization.
The rough-denominator device is credited to PR200.

## Which analytic tests cannot distinguish components

The [operator package](rigidity/phase2/README.md) starts with two formal
ordinary inputs. `BasinBlocks` formalizes PR146's qualitative theorem:
arbitrarily high consecutive blocks reach one prescribed target coprime
to three at a common clock. `FiberInterval` places every fixed-clock
preimage with `j` even departures in an interval containing at most `2^j`
integers. Neither result is an assertion that one fixed source converges.

For the squared-slope composition operator
`Cf(n)=w(n)f(Tn)`, with even weight `1/4` and odd weight `9/4`, the full
graph and known component of 1 have identical power norms and the same
closed spectral disk of radius `9/4`. The exact normalized power norm is
controlled by the actual reflected `3n−1` tree at 1. Explicit terminating
ordinary paths already attain the required growth. These are written
operator proofs, with the finite fibre input checked in Lean.

The stronger [height-observable theorem](rigidity/phase2/HEIGHT_OBSERVABLES.md)
compares every component with the full graph. For any *-polynomial in
`C`, its adjoint, bounded periodic multipliers, and bounded uniformly
continuous functions of `log n`, the **essential norm** is the same.
The corresponding generated Calkin algebras are canonically isometrically
*-isomorphic, so the corresponding essential spectra agree as well.
Ordinary norm equality for arbitrary height multipliers is not asserted.

The root reconstructed both ingredients that make this more than a
local-pattern heuristic. First, every component meets every fixed
arithmetic progression in every sufficiently high multiplicative interval
of fixed relative width. Second, forward occupation measures give a
uniform finite-radius localization estimate on any functional graph.
Together they transplant escaping near-norm vectors while preserving
periodic labels and approximating the log-height labels. The independent
periodic-only proof also handles arbitrarily many unknown cycle cores.

The [dual-height note](rigidity/phase2/DUAL_HEIGHT.md) describes a different
possible certificate. A positive one-edge supersolution with growth
`o(n²)` would rule out escaping trajectories. If its growth were bounded
by `n^α`, `α<2`, the normalized values would have a mandatory lower tail
of order `ε^(1/(2−α))` in every arithmetic progression. Reciprocal moments
at and above that threshold diverge. This constrains the proposed
certificate class; no suitable supersolution has been constructed.

## Review and the remaining universal step

The root read and reconstructed the written arguments above, including
the finite cone, scaled budget, whole-denominator comparisons, exact
operator formulas, localization, and finite parity-cylinder lower tails.
Execution receipts identify which local declarations were rebuilt and
which bounded controls were rerun; process evidence lives in `reports/`.

The postpeak criterion still needs a suitable matching word or a later
merger for each residual source. Cycles with sufficiently complicated
parity words can pass the combinatorial restrictions. The common
essential spectra leave the **exact kernel at 1** unresolved: a nonzero
homogeneous ordinary eigenvector there still detects escape. No current
argument turns the finite-word criteria, a positive density statement,
or analytic approximation into universal positive integer convergence.
