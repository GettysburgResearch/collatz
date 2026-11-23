# Template-selection execution and proof boundary

23 November 2026. **Full Collatz and the original residue-512 implication
remain OPEN.**

[Scientific statement](../../../../research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/TEMPLATE_SELECTION.md)
· [Exact executions](REPLAY.json) · [Primary-source ledger](SOURCES.json)

## What is established

For every nonempty actual shortcut parity prefix at a positive integer x,
a nonintegral reduced rational fixed center c/d has `|dx-c|>x`. This is
an all-word theorem. Its written proof combines the complete carry bound,
the actual source lattice, and a universal two-power gap proved using
Matveev's original Corollary 2.3 plus an exact finite continued-fraction
certificate.

Minimizing all nonzero reduced prefix displacements has a complete finite
evaluator using only `floor(log_2(x+1))` actual prefixes and a finite
sublevel height bound. Equality of that minimum with the elementary
rounded rank for every x is equivalent to exclusion of nonstandard
positive cycles. The equivalence is not a proof of either side.

A supplied complete ordinary word x→1 compiles to a paid changing-center
macro, with explicit handling of the short word 2→1. The compiler does
not discover an unknown target termination word.

## Formal scope

`TemplateSelection.lean` contains **13 new public declarations**:

- cleared carry-to-center inequalities;
- exact coefficient-to-descent conversion in the native binary window;
- primitive nonzero displacement and the all-source finite height consumer;
- literal ordinary source-lattice and nonintegral-template consumers;
- finite word-horizon and proper-sublevel bounds;
- complete multiplier/carry bounds;
- the supplied terminal word's paid inequality and exact source rank.

The real center bound is an explicit hypothesis of the ordinary
nonintegral consumer. Matveev's theorem, the real-logarithm reduction,
continued-fraction coverage and the global cycle-equivalence statement
are written proofs. No new axiom is added to represent those arguments.

The module uses Mathlib at `d13f23b723b8a846827a245b89c10fc7d3f11612`
and the unchanged `AdaptiveLattice.lean` / `LatticeDescent.lean` dependencies.
Their 13 and 20 declarations are not counted as new. Lean is 4.34.1,
compiler `5045d0056413266e57c625dcd7c365b10e377c52`.

## Exact finite certificate and controls

The Python checker uses only exact integers and `fractions.Fraction`.
Its rational logarithm enclosures contain 128 terms. It certifies all
continued-fraction digits through the first denominator greater than
`10^12`, namely `5409303924479`; all reduced upper convergents below the
cutoff and all their possible multiples are accounted for in the proof.
The proof's large-exponent range is analytic, not a numerical census.

The ordinary controls include all 8,190 words of lengths 1–12 at three
actual positive sources per word: 24,570 actual traces, including 24,393
nonintegral-template cases. The supplied-witness compiler covers 1,023
ordinary sources and 41,074 literal shortcut steps. These finite examples
validate the implementation; they are not used to extrapolate an infinite
Collatz assertion.

The controls retain the need for an ordinary integer source, actual
parity legality, exclusion of zero from the positive-score minimum,
the integral-center exception, and padding the short terminal word.
Explicit failing guards are used instead of Python assertions.

Final actual executions and byte-identical normal/optimized output are
recorded in `REPLAY.json`, `normal.json`, `optimized.json` and the audit
logs. Strict compilation uses `-j 1 -DwarningAsError=true` and prints the
axioms of all thirteen new declarations. The complete-checkout publication
gate is the coordinating agent's separate responsibility.
