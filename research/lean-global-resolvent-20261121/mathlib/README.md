# Mathlib modules

These files use Lean **4.34.1** and Mathlib at the exact commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

Run them from a checkout of that Mathlib revision, with its dependencies and
matching cache available:

```sh
lake env lean -DwarningAsError=true /absolute/path/to/MixedCertificate.lean
lake env lean -DwarningAsError=true /absolute/path/to/PrimitiveSurvival.lean
lake env lean -DwarningAsError=true /absolute/path/to/OddCertificateMeasure.lean
```

The modules include their principal `#print axioms` commands. All finite
affine certificate checks use kernel-checked `decide`. These modules keep a
separate interface from the sibling core project, whose upstream induction
shim defines a name that Mathlib already supplies.

The multiset order and its well-foundedness are provided by
[`Mathlib/Data/Multiset/DershowitzManna.lean` at the pinned revision](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/Data/Multiset/DershowitzManna.lean).

## Composed unbounded reset

`OddResetCertificate.lean` imports `OddCertificateMeasure` and rechecks the
needed frozen core proof bodies against a small explicit map interface. It
proves the iteration-convention equality before applying the certificate
measure theorem. Its two final statements are
`complete_certificate_descent` and `complete_failed_reset` in namespace
`CollatzOddResetPort`.

The generated source is committed and reviewable. To reproduce it, run
`python build_odd_reset_certificate.py` from this directory. The generator
reads `../lean/Collatz/`, verifies the frozen source hashes, and regenerates
the file. Generation is not a substitute for its Lean check.

For compilation, start a shell with `lake env bash` from the pinned Mathlib
checkout. In that shell, use an absolute writable output directory and the
absolute path to this `mathlib` directory:

```sh
collatz_mathlib_sources=/absolute/path/to/research/lean-global-resolvent-20261121/mathlib
collatz_olean_output=/absolute/path/to/scratch/collatz-oleans
mkdir -p "$collatz_olean_output"
export LEAN_PATH="$collatz_olean_output:$LEAN_PATH"
lean -DwarningAsError=true --root="$collatz_mathlib_sources" \
  -o "$collatz_olean_output/OddCertificateMeasure.olean" \
  "$collatz_mathlib_sources/OddCertificateMeasure.lean"
lean -DwarningAsError=true --root="$collatz_mathlib_sources" \
  "$collatz_mathlib_sources/OddResetCertificate.lean"
```
