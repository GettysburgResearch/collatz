# First checkpoint verification

**Pass status:** the six-hour research pass is continuing. This report verifies
the first stable checkpoint, not a proof of the Collatz conjecture.

## Exact science tree

- Local immutable replay commit: `d45b282a12ea86a22e7d8b013b9f2eb104508af2`.
- GitHub science commit: `95c572c0af668be6ada185d35a7ff1041e4e7588`.
- Their identical Git tree: `994d15152f99a8cf7499d7752f96fde9b774d7fd`.
- Complete tracked files in each science checkout: **1,341**.
- Parent: `ed7a6fe30b8602407f77855ceb74ce0489ce9c10`.

The GitHub tree was created from the exact committed UTF-8 blobs and compared
with the local Git tree before publication. The API-created commit has different
author metadata from the local checkpoint, so its commit identifier differs;
the complete source tree is identical. Both commits were retained locally.

## Fresh compiler and exact finite replay

The [unmodified replay receipt](checkpoint_replay/receipt.json) ran from
**01:11:18 to 01:12:38 UTC on 27 November 2026**, in a clean complete detached
checkout with a new, initially empty project-object directory.

All of the following passed:

- **14 new Lean modules**, with **49 of 49 public theorem axiom audits**.
- **One project dependency rebuilt**, `Portal`, with nine additional audits.
  Total: **58 of 58** named audits across 15 compiled project modules.
- Warnings as errors, automatic implicit variables disabled, and only
  `propext`, `Classical.choice`, `Quot.sound` allowed in transitive inventories.
- No `sorry`, `admit`, declared `axiom`, or `native_decide` in the checked
  project proof sources.
- **Ten exact Python control pairs**, with normal and optimized stdout and
  stderr identical. The checkers use explicit guards; no Python `assert`
  nodes were accepted.
- **All eleven repository validation commands**, including the bounded
  regression bundle.
- Source manifests, commit, tree and clean checkout unchanged after replay.

The physical-strip transfer ran with arguments `8 64`. Its independent
eight-step direct enumeration covered 24 starts. Its 64-step transfer covered
all 66 critical mechanical schedules and checked the two inequalities
`E^20 < 2^(23S)` in integer arithmetic. The displayed floating exponents
are not the acceptance test.

Lean was 4.34.1. Mathlib was pinned at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. All **9,114** source/configuration
files selected by the driver matched a fresh pinned Mathlib source checkout,
with manifest `19356a0bbc13f8a6c54ce09ba884b03f2e51aa238e8b83c304d77ac7d6045359`.
Dependency objects were reused; every project object was rebuilt. This is
not a rebuild of Lean itself or of all Mathlib objects.

## API science identity gate

A second complete detached checkout of the actual GitHub science commit
`95c572c0af668be6ada185d35a7ff1041e4e7588` passed all eleven repository commands
at **01:17:38–01:17:44 UTC**. Its 1,341-file checkout and identical tree remained
unchanged. The [receipt](checkpoint_replay/api-science-validation.json) has
SHA256 `d77e83948139f5503200a76473251a4af3eebea4c399a6028afb7e1fcbc42144`.
The already compiled science files are byte-identical; no second mathematical
validation is inferred merely from this integrity gate.

## Mathematical scope

The [independent root review](ROOT_REVIEW.md) reconstructs the written arguments
and identifies their exact external inputs. The fresh finite replay confirms
the stated Lean kernels and controls. It does not formalize the imported
mixing, gcd, Subspace-Theorem, shell-transfer or large-range-verification
results. The full denominator-one cycle case and the original ordinary
escape contradiction remain open.

This report and its raw logs are a reports-only child of the science tree.
Later research is to be checked under its own final science revision.
