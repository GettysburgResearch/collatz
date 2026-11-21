# Mathlib modules

These files use Lean **4.34.1** and Mathlib at the exact commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

Run them from a checkout of that Mathlib revision, with its dependencies and
matching cache available:

```sh
lake env lean -DwarningAsError=true /absolute/path/to/MixedCertificate.lean
lake env lean -DwarningAsError=true /absolute/path/to/PrimitiveSurvival.lean
```

Both modules include their principal `#print axioms` commands. All affine
certificate checks use kernel-checked `decide`. The file is intentionally
independent of the sibling core project, whose upstream compatibility shim
defines a name that Mathlib already supplies.

The multiset order and its well-foundedness are provided by
[`Mathlib/Data/Multiset/DershowitzManna.lean` at the pinned revision](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/Data/Multiset/DershowitzManna.lean).
