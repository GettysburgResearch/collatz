# Frozen inputs for the marked-band attack

The pass continues our branch `research/lean-global-20261121` from
`cda78d92f404dd3219a7a4ed9322706654eddf29`, published in PR178. The new
user-directed input is the updated PR173 at
**`fa0c9e2a2851e6324391e39c17afcb5913185aec`**. Its first-return theorem
and source's own increasing-return construction were read together; no
monotone first-return assumption is imported.

## Byte-exact source imports

Every entry comes from `research/lean-shell-cover/` at that PR173 head.
The Lean files are kept unchanged under `lean/vendor/`, preserving their
original module names and namespace. The source README is kept separately
as `sources/PR173_README.md`.

| Source file | Git blob |
|---|---|
| `README.md` | `93450d0c12443a33d1eacbae295c8e4ad56ccfd7` |
| `ShellCover.lean` | `6083e8b8155a740316b60ec18df841e2f0005554` |
| `ForwardSection.lean` | `73736deaf444e1e4ff9cac81e0c8f7ce2a02ab85` |
| `SectionDynamics.lean` | `fc32309ab30d949b92c68377d2f56e185c6ce6a7` |
| `RisingReturns.lean` | `aaa2a0e43eccf8001479c9cc016f4d4f2be707aa` |

The copied bytes were matched to these Git blob identities before new
proof work. The source's names `bounded_visit`, `collatz_iff_return_descent`,
and `arbitrarily_large_first_return` retain exactly their original
quantifiers. `odd_run` is also credited to this source; reusing that
finite orbit identity is not presented as a newly discovered formula.

The integer map is the shortcut map: halve even inputs and send odd `n`
to `(3n+1)/2`. `CollatzShell.orbit t n` takes its clock first. The earlier
PR178 core uses `CollatzGlobal.orbit n t`, with the arguments reversed;
any reuse of those lemmas must prove the correspondence or recheck a
clearly credited compatible copy. Similar notation is not an interface axiom.

## Formal runtime

The source pins Lean **4.34.1** and Mathlib
**`d13f23b723b8a846827a245b89c10fc7d3f11612`**. The build script checks
these pins and the frozen source hashes. No predecessor-count assumption
from the earlier `OctavePacking.lean` file is used in the forward-section
development or in this pass.

## Focus of the refresh

Recent PR metadata was read to locate the new result, including updated
heads of PR174, PR176, and PR177. Those neighboring packets were not
silently imported or newly audited. This pass concentrates on the
marked-band source and the new proof attempts recorded beside it.

The older common-rank and orbit-lift work remains at its credited PR178
checkpoint. A theorem about a supplied finite source certificate is not
used as a claim that every positive integer already has such a certificate.
