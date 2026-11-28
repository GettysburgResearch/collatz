# Initial formal replay status

The first publication preserves the written research and the complete
candidate Lean sources while the strict packet replay is still being
repaired. **There is no passing whole-packet axiom-audit receipt at this
checkpoint.** This file must not be read as a claim of one.

The coordinator's strict runs compiled `MinimumWindow.lean` and
`AffineCorrection.lean` successfully after narrowing their Mathlib
imports. A subsequent fresh run compiled `MinimumWindow` again and
timed out while compiling `AffineCorrection`. The retained
`CHECKPOINT_01_LEAN_ATTEMPT.json` records that unsuccessful batch,
including its dependency pins, flags and elapsed timeout. Earlier runs
also identified missing imports and a multiplication-inequality lemma
in `ContractingCalendar`; source repairs are present but await the
complete repeat. `FiniteCriticalTail` is a new connected candidate
kernel whose written theorem is in the accompanying Markdown.

The source authors separately compiled `ModularQuotient` and
`ProfiniteAncestors`. Those reports are development evidence, not a
substitute for the coordinator's fresh all-declaration audit. Only a
later receipt with `passed: true`, matching source hashes and the
complete declaration list will establish that audit.

The exact Python and C++ controls in this checkpoint did pass their
stated bounded ranges. Their results and the written reconstruction
have separate evidence files. The repository integrity result also
has its own clean-checkout receipt. None of those checks substitutes
for a missing Lean result.
