# Frozen sources for the Lean global attack

The snapshot was read on 2026-11-21. The worktree starts at main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Newer open-PR heads are sources,
not main-branch acceptance. Only the sources explicitly reused below become
formal imports.

| PR | Frozen head | Role |
|---|---|---|
| 174 | `7034109ed60a26bc49824e1ed43c239ceca81194` | Core-only Lean basin and psi-closure development; imported as specified below |
| 173 | `a09eb47197cd99f218b3fa013c681df65ea0f69a` | Shrinking-interval global criterion; research input, not a formal import |
| 146 | `f431078244e868dc699fad011044f0d5e7f76437` | Latest whole-interval synchronization and certified-terminal results; research input |
| 172 | `b22d94240f3d44a04231508e5dfe9a4947a57125` | Uniform-tail witness descent and certificate compiler boundaries |
| 171 | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | Recurrent affine sections and ordinary paired-descent density |
| 170 | `656063d5efa0f5708356ab2563a4348d39bae013` | Carry-four transport and terminal-phase boundary |
| 169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | Further certificate and arithmetic-moment work |
| 168 | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | Prior return-language, witness, conductor, and stationary-boundary pass |
| 164 | `9582df78eb4d768eb748d3cf367ba97582308a52` | Updated reverse-tripling witness descent |

The latest PR metadata and selected relevant theorem statements were read.
This is a research-input snapshot, not a claim of a new audit of every file
or historical PR.

## Exact Lean reuse

All three files below come from
[`research/psi-closure-20261121/lean/Collatz/` at PR174](https://github.com/GettysburgResearch/collatz/tree/7034109ed60a26bc49824e1ed43c239ceca81194/research/psi-closure-20261121/lean/Collatz).

- `ReverseBasin146.lean`: unchanged PR174 source, Git blob
  `becc5a0945269756e6afdecf9444b6762df28bc7`. PR174 credits PR146's
  reverse-basin development and replaces its Mathlib import with a core shim.
- `Closure174.lean`: the unchanged contents of upstream `Closure.lean`,
  Git blob `2bd11db7ce07d653376c2c0672b3441a638dac39`; local filename changed.
- `Shadow174.lean`: upstream `Shadow.lean`, Git blob
  `58b452fd9c85dfeabaeac0f2f56bdbd8afe4193f`; only the import is changed
  from `Collatz.Closure` to `Collatz.Closure174`.

The first new formal module is `CollatzGlobal/OrbitLift.lean`. It credits
the existing ordinary affine-prefix identity; the contribution is its
all-parameter Lean proof and the actual paired-failure transport interface.

No claimed GRH announcement is needed as a premise. No external analytic
theorem or unresolved Collatz closure is added to Lean as an axiom.


## Focused publication refresh

PR173 advanced to `9ca79e54bd2ae9d9cf4c80851f867364fc3a2d3e`.
Its updated README, comparison metadata, and new theorem statement contexts
in `PeriodicWindow.lean`, `DyadicMixing.lean`, `OctaveCriterion.lean`, and
`OctaveDeadline.lean` were inspected. The new sparse ordinary-meeting
criterion and its deadline obstruction are summarized in
[GLOBAL_FORCING.md](GLOBAL_FORCING.md); no Mathlib recompile is claimed.

PR175 at `ad513f1ea609ed47dbcf997df0f09c16557264ee` was read at its
packet README for the relative parity budget. PR176 at
`bff01093f3eb073216f9ec610130d16067fcc1fd` was read at the relevant
`research/lean-global-resolvent-20261121/lean/Collatz/TerminalFive.lean`
statements. Its terminal assumed-failure construction is credited in
[CLOSURE_ROUTE.md](CLOSURE_ROUTE.md), and distinguished from the total
finite algorithm on an arbitrary supplied certificate here. PR177 at
`fe58c189b619d2983940b19a50f1b12798f5651f` was inspected at metadata/body
scope for the exact exponent-witness and adjacent-source induction work.
None of these refreshed results is silently added as a Lean axiom.

## New rank instantiation dependency

The eight concrete negative-reference transformations are reused from
PR168 `e4599b32e4b1a955ac9315d46782d4ad6a5db96c`,
`research/closure-frontier-20261121/NEGATIVE_TEMPLATE_GRAMMAR.md`,
NT2--NT3. The precise older PR164 credit is retained there and in
[COMMON_RANK.md](COMMON_RANK.md). Their ordinary legality remains a
paper-level dependency. The new exact rank guards, formal fixed-clock
conjugation, and independent no-padding check do not constitute a claim
that every old template proof has been translated into Lean.
