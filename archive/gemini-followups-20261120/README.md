# Three additional Gemini research packages, preserved verbatim

These are the three archives supplied by the user after the initial audit in
[PR152](https://github.com/GettysburgResearch/collatz/pull/152). The thirty
extracted files are preserved byte-for-byte under `source/`. The manifest
records each original ZIP hash and every extracted file hash. The ZIP
containers themselves are not included in this source archive.

| Supplied ZIP | Extracted source directory |
|---|---|
| `gettysburg_collatz_proof_routes_2026_11_20.zip` | `source/collatz_routes_bundle/` |
| `collatz_full_completion_blueprints_v2_2026-11-20.zip` | `source/collatz_full_completion_blueprints_v2_2026-11-20/` |
| `collatz_farkas_dirichlet_breakthrough_v3_2026-11-20.zip` | `source/collatz_farkas_dirichlet_breakthrough_v3_2026-11-20/` |

The user's description identifies two packages as continuations of the first
Gemini thread and one as a separate thread. The files are treated as proposed
mathematics, not as repository instructions or accepted results. Their
original `PROVEN`, `VERIFIED`, and `breakthrough` labels are preserved as
source text; the accompanying audit determines the narrower valid scope.

In particular, a numerical script returning `PASS` does not establish an
all-exponent Farkas certificate, an ordinary fixed-source transfer theorem,
or the Collatz conjecture. Original numerical outputs and Lean skeletons
remain distinct from our new proofs and replay evidence.

The separate `pinned-pr146/` directory contains byte-exact copies of the
three source proofs used by the ordinary variation argument, at commit
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`. Its adjacent manifest records
their hashes. This dependency cache makes the new finite replay independent
of another worktree or a live network connection. It is not part of the
thirty uploaded files and imports no other claim from PR146.

Start with the
[new scientific packet](../../research/gemini-dirichlet-global-20261120/README.md).
