# Checkpoint twelve: joint counterquery and terminal energy transport

Parent published PR177 head:
`8ef9bf0d828fc533721dee1f90c5d78fac80ad39`.

**Full Collatz and the original residue implication remain open.**
The exact arithmetic closing proposition is now `FloorIntervalStep`; the
new module proves its equivalence to both original problems, not the step.

## Formal contribution

`JointMinimalCounterexample` selects a least bad target, a minimum-grade
complete source capturing it, then the maximum source at that same grade.
The finite source ceiling makes the last selection legitimate. The same
supplied certificate carries the original full interval hypothesis, an
arbitrary-target same-grade larger-source hypothesis, the prior on every
smaller target, its own future floor, the canonical nonempty prefix to 11,
and strict coefficient contraction of every nonempty literal prefix.

The proof incorporates the latest PR180 source-value tie, with explicit
credit, in this core-only interface. It does not reset a source witness
or presume that exhausting its finite word closes a target debt.

## Written analytic contribution

`TERMINAL_DIRICHLET_RUN_MASS.md` proves convergence in total mass norm of
the live terminal Dirichlet measure to Cesaro forward transport of the
fixed finite original measure `dF`. It proves that the killed-boundary
remainder tends to zero. Bounded binary-run observables then give the
explicit lower bound `(1+3k)b_infinity`; a positive escape coefficient
forces extended run-weighted energy to diverge. The actual contact reset
has limit `F^2 eta_0` in total variation.

These results retain the exact pinned harmonic, canonical Green and
boundary inputs from the peer analytic work. They are written proofs,
not Lean declarations or new axioms. No matching weighted upper bound
or exclusion of nontrivial cycles is claimed.

## Focused actual execution

`checkpoint-twelve.json` records commands, timings, compiler identity,
all Lean source hashes, new scientific note hashes and proof boundaries.

- Aggregate core-Lean build: **42 jobs passed**.
- New module separately compiled with warnings treated as errors.
- Expanded combined audit: **241 declarations**, including **16 new public
  theorems**. Nine audited declarations are axiom-free.
- Every other axiom set is a subset of `propext`, `Classical.choice`, and
  `Quot.sound`; no conjectural axiom, `sorry`, or `native_decide` is used.
- The 39 unchanged preexisting Lean files match checkpoint eleven's receipt
  by SHA-256. No fresh rebuild of all old proofs is claimed.
- Lean 4.34.1 core only, without Mathlib. No new numerical Collatz range is
  tested; the existing terminal base through 1105 is reused.

The coordinating lead read the entire new Lean module and independently
reconstructed the physical inverse-prefix Jensen bound, finite-component
mass squeeze, original-source ray comparison, bounded run truncation and
killed-boundary accounting. The certificate lane also checked the central
written measure argument. The analytic source qualifications remain intact.

## Latest source delta and publication

`SOURCE_DELTA.json` freezes seven re-read relevant heads, including four
that advanced after the preceding snapshot, and twelve selected source
files. PR185's actual committed tree was used despite its stale description.
This targeted reading is not a new independent replay of peer projects.

The complete clean-checkout integrity/regression gate is run on the final
committed tree before publication. Its checked commit, tree and receipt
digest are recorded on PR177. The API publication tree must match exactly;
the remote ref, parent and tree are re-read after the owned branch update.

The central unfinished work is explicit: prove a successful original-target
return or permitted source improvement for every arbitrary canonical word,
or supply the required arithmetic upper bound for the same energy. The
present checkpoint establishes the stated reductions and transport results;
it does not assert either universal closing argument.
