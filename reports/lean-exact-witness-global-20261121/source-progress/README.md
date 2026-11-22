# Checkpoint eleven: actual source progress and original target floors

Parent published PR177 head:
`46a76145ef21e93318eff25da8cf00c5342fd7d2`.

The scientific entrypoint is the
[research README](../../../research/lean-exact-witness-global-20261121/README.md).
Full Collatz and the original residue implication remain open.

## Proved mathematical statements

`NegativeShadow` proves that every negative odd shadow `-m`, with `m>0`,
has a nonempty prefix of at most `3m` odd events whose coefficient satisfies
`2^A<=3^r`. Its exact ordinary clock is positive and less than `2r<=6m`.
The argument uses the full affine correction and the negative sign of the
endpoint, with no assumption about eventual negative behavior.

For a positive source `q+m=2^D*u`, `D>=6m`, the same literal prefix lifts to
an actual positive path ending at a larger odd source. `SourceOrbitProgress`
advances the supplied complete source certificate, proves a strict drop in
its original grade, retains the initial even run, and closes the entire
original interval under its original induction hypothesis. The real
negative-block guard is part of the theorem's statement.

`RootedSourceFloor` independently supplies a canonical source for every
target at least 177. It lies above half the original target and every state
after it remains below that floor. The selector cuts an actual finite
bounded-four prefix to 11 and returns the exact initial exponent, clock
decomposition, unused suffix and complete certificate. For a target `3 mod4`,
an odd-source cap return or a cap paid by the gap just consumed is strictly
below the original target. These facts do not assume success of every carry.

The written note `STRICT_PREFIX_CONTRACTION.md` extracts cofinal complete
bounded-four sources with strictly contracting coefficient prefixes. A
stronger cofinal family is larger than every later odd state, so it admits
no future odd-source-growth selector. These finite-word deductions keep the
coverage boundary of the negative-shadow rule explicit. They are written
mathematics, not additional Lean declarations in this checkpoint.

## Formal execution scope

`checkpoint-eleven.json` records actual commands, durations, all current Lean
source hashes, new note hashes, compiler identity and proof boundaries.
This is an incremental continuation of checkpoint ten's fresh build.
The 36 unchanged preexisting Lean files were matched to that receipt by
SHA-256; no fresh rebuild of all old proofs is claimed.

- Aggregate `lake build`: **41 jobs passed**.
- Each of the three new modules also passed a separate direct compile with
  warnings treated as errors.
- The complete expanded `Audit.lean` checked **225 declarations**, including
  **41 new public theorems**.
- Nine audited declarations use no axioms. Every other axiom set is a
  subset of `propext`, `Classical.choice`, and `Quot.sound`.
- No new module contains `sorry`, a custom conjectural axiom or
  `native_decide`.

The package uses core Lean 4.34.1 without Mathlib. The logs are
`checkpoint-eleven-build.txt`, `checkpoint-eleven-axioms.txt`, and the three
`checkpoint-eleven-strict-*.txt` files. Empty strict logs indicate successful
warning-free executions; the exit codes are in the JSON receipt.

These are structural, all-word and all-exponent results under their stated
hypotheses. No new bounded Collatz search or numerical verification threshold
is used. The only fixed finite orbit in the source selector is the explicitly
forward-closed path from 11, whose ordinary peak is 26.

## Publication and remaining theorem

A complete clean-checkout integrity/regression gate is run on the final
committed tree before publication. PR177 records its checked commit, tree,
command and receipt digest. The API publication tree must equal that checked
tree, and the remote head is re-read after updating the owned branch.

`ElevenIntervalStep` remains unproved. The canonical source selector supplies
the source and preserves the original target floor; it does not force every
target to return to a certified cap. The interval consumers keep the original
grade induction premise explicit. No coverage premise is introduced as an
axiom and no full Collatz proof is claimed.
