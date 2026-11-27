# Executed final verification

**All declared checks passed. Collatz remains unproved.** This report records
the immutable science snapshot from the six-hour continuation begun at
22:45:41 UTC on 26 November 2026. The later reports-only child preserves
that complete scientific tree and adds these execution records.

## Exact science snapshot

| Object | Value |
|---|---|
| GitHub science commit | `91f35d74955196c31443604f13b782e8eb8c8326` |
| Local replay commit | `cd20122b1bb92bac45702475a075195bc46729eb` |
| Identical complete Git tree | `dbd092ab9f47a5d8eede443252e6cca006f87e86` |
| Parent on the owned GitHub branch | `75eac0cbc744469ae2886bc2f140685c484e9fe7` |
| Tracked files in each science checkout | 1,477 |
| Full replay started | 2026-11-27 04:13:22 UTC |
| Full replay finished | 2026-11-27 04:15:25 UTC |

The GitHub tree was created from the exact committed file contents and
required to equal the locally replayed tree. The actual API commit was
reconstructed byte-for-byte as a Git commit object, checked against its
GitHub hash, and used for a second complete clean checkout. No source file
was changed to make the verification pass.

## Lean results

- **25 new Lean modules**, with **93 of 93 public theorem axiom inventories**
  checked exactly once.
- The earlier project dependency `Portal` was rebuilt from source, with
  **9 additional inventories**: **102 of 102 total**, across 26 project modules.
- Every project object was compiled into a new empty directory. Warnings
  were errors and automatic implicit variables were disabled.
- The checker rejects unchecked `sorry`, `admit`, declared `axiom`, and
  `native_decide` tokens in the audited source text.
- Every printed transitive axiom set was contained in `propext`,
  `Classical.choice`, and `Quot.sound`.

The pinned compiler was Lean 4.34.1. Mathlib was pinned at
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
All **9,114** selected Mathlib source/configuration files matched a fresh
checkout of that revision, with zero mismatches. Their combined manifest
was `19356a0bbc13f8a6c54ce09ba884b03f2e51aa238e8b83c304d77ac7d6045359`.
Pinned dependency objects were reused; every project object was rebuilt.

Lean checks the displayed finite and algebraic propositions. The written
graph, Fourier, asymptotic, Subspace-Theorem and measure arguments retain
their own stated external inputs. This receipt does not convert those
arguments into fully formalized theorems or discharge any open premise.

## Deterministic controls and integrity

All **18 declared Python controls** ran in both normal and optimized modes.
Each pair had identical complete stdout and stderr. The checker parsed
the complete output with Python's arbitrary-precision integers and compared
it with its full retained JSON report. All comparisons passed. No removable
Python `assert` nodes occurred in these controls.

The controls include the 64-step physical-strip energy certificate, the
256-step rank-support count, the 512-step full-mask moment certificate,
the actual-history rational controls, exact upper-word and distortion
controls, ordinary parent rows, and the original-floor enumeration. The
independent direct ordinary replay checked **262,440** CRT representatives
and matched **all 40** retained residue counts.

All **11 repository regression-validation commands** passed inside the
immutable replay. A second complete checkout of the actual GitHub science
commit passed the same 11 integrity commands at **04:17:04–04:17:09 UTC**.
These validators check repository integrity and bounded regression
fixtures; they do not certify a universal mathematical conclusion.

The replay's before/after source manifests, commit, tree and clean working
state were identical. The actual API science checkout also remained clean
and unchanged.

## Receipts and review

- [Complete replay receipt](final_replay/receipt.json), SHA-256
  `ae7580786b01ab98ef8fe015a36c36e3f351a2d0c390f4d1b2a832f64e0ee3fb`.
- [Replay integrity receipt](final_replay/repository-validation.json).
- [Actual API science integrity receipt](final_replay/api-science-validation.json),
  SHA-256 `af0c9087745c4f4692a4a62b22dd22ecca5b3820add761f89bdd3c0a467c7014`.
- Raw command stdout/stderr are retained beside the receipts in
  [final_replay](final_replay).
- [Reproducible driver](replay.py), [root mathematical review](ROOT_REVIEW.md),
  and [closing-status report](../../research/astra-sixhour-20261127/CLOSURE_STATUS.md).

The root reconstructed the retained arguments. The arithmetic agent
independently reviewed the root's full-mask moment argument; the descent
agent independently reviewed the final asymmetric four-phase/core proof;
the transport agent independently reviewed the final all-gap upper proof.
Their reviews found no gap within the expressly stated scopes. These are
internal research reviews, distinct from Lean verification and external
mathematical review.
