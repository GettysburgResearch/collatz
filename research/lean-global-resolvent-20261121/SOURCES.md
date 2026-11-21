# Frozen sources for the global Lean attempt

The accepted repository base is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. This packet is research on a separate branch.

| Source | Exact head | Use |
|---|---|---|
| [PR174](https://github.com/GettysburgResearch/collatz/pull/174) | `7034109ed60a26bc49824e1ed43c239ceca81194` | Dependency-free ordinary-map toolbox, forward/reverse closure equivalences and exponent families. `lean/Collatz/ReverseBasin146.lean`, `Closure.lean` and `Shadow.lean` are copied unchanged from `research/psi-closure-20261121/lean/Collatz/`. The project root and audit are extended for our new modules. |
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146) | `f431078244e868dc699fad011044f0d5e7f76437` | Current terminal-five and whole-interval synchronization interfaces, including new commits on this older PR. The imported core reverse theorem itself is the earlier source version credited inside PR174; no replacement by an uninspected later theorem is made. |
| [PR173](https://github.com/GettysburgResearch/collatz/pull/173) | `a09eb47197cd99f218b3fa013c681df65ea0f69a` | Global interval-survivor criterion and equal-clock inverse fans; used to choose the analytic attack, not imported as an unproved Lean axiom. |
| [PR171](https://github.com/GettysburgResearch/collatz/pull/171) | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | Relative-section recurrence, critical negative moment and full positive-kernel pressure boundary. |
| [PR172](https://github.com/GettysburgResearch/collatz/pull/172) | `b22d94240f3d44a04231508e5dfe9a4947a57125` | Uniform tail descents and the stated remaining all-source certificate obligation. |
| [PR170](https://github.com/GettysburgResearch/collatz/pull/170) | `656063d5efa0f5708356ab2563a4348d39bae013` | Carry transport and terminal-library boundary. |
| [PR164](https://github.com/GettysburgResearch/collatz/pull/164) | `9582df78eb4d768eb748d3cf367ba97582308a52` | Updated direct-R and source-zero descents; old and new source packets are distinguished. |
| [PR169](https://github.com/GettysburgResearch/collatz/pull/169) | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | Our prior paired height contractions and exact primitive-word arithmetic. |

Lean runtime: `leanprover/lean4:v4.34.1`. The core project requires no Mathlib. Any separate Mathlib development in later checkpoints is pinned to `d13f23b723b8a846827a245b89c10fc7d3f11612` and is identified separately because the imported dependency-free induction shim is not intended to be imported together with Mathlib.

The multiset order considered in this pass is the established Dershowitz--Manna order. Its well-foundedness is supplied by Mathlib's `Mathlib.Data.Multiset.DershowitzManna`, not claimed as a new theorem. The question here is whether actual ordinary certificate moves share that order and admit a complete selection theorem.

## Concurrent refresh before checkpoint 3

These newer interfaces were read selectively while the proof attempt continued;
their complete proof packets were not rerun or silently incorporated as axioms.
The original core imports above remain at their original pin.

| Source | Exact refreshed head | Connection to this attempt |
|---|---|---|
| PR173 | `cccf14d13250d3f98ef9b01ddbd304d11294e603` | `research/lean-shell-cover/README.md`: exact dyadic mixing, five-block merger test and predecessor-population transfer. The conversion to ordinary component labels still needs an actual mismatch bound; [FLUX_ATTEMPT.md](FLUX_ATTEMPT.md) identifies the corresponding missing absorption estimate. |
| PR174 | `011b89e5362ea89427c2704e5e6c1f434e860da0` | The change from the imported pin is a literature-note addition, with no change to the copied core Lean files. |
| PR177 | `fe58c189b619d2983940b19a50f1b12798f5651f` | Exact witness and adjacent-source normal forms. Its reported remaining odd-valuation branch retains a larger source multiplier; it does not furnish the missing complete rule selector here. |
| PR178 | `7e40cb5e09f4ed84b96eebf1d2e3fe43fdadf862` | Exact ordinary cylinder lifting and certificate normalization; attribution and current scope were refreshed from the PR, without importing its module. |
| PR179 | `4bf2675bcc78b42a3f17c0dd826e1dfcc4c8f35b` | `research/lean-descent-20261121/INVERSE_RETURN.md`: a contracting inverse comparison and the obstruction to an exclusively smaller-ancestor proof program. Its half-crossing budget is still an explicit unproved universal assertion. The present shared-order program permits other moves. |

## Mandatory forward section: checkpoint 5

The new direct dependency is **PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`**. The four files
`ShellCover.lean`, `ForwardSection.lean`, `SectionDynamics.lean`, and
`RisingReturns.lean`, originally under `research/lean-shell-cover/`, are
copied unchanged into `section/lean/`. Their exact SHA256 values are in
[section/upstream-pins.json](section/upstream-pins.json), and the replay
script checks them before compiling. This supersedes the earlier PR173 pin
only for this new section packet; it does not rewrite prior checkpoint
provenance.

The credited imports supply the ordinary map, its equal-clock inverse fan,
the mandatory density-zero forward section, its first-return map, and the
arbitrarily expanding first-return family. The new work supplies inverse
phase steering, injective oddification of the fan, the bounded-clock marked
population, exact finite count and population transfers, and source-weight
transport statements. None of the new upper survivor estimates or global
closure assertions is imported as a premise disguised as a theorem.

At the start of this pass, the current PR descriptions were also refreshed at
PR174 `c92cd473de3b85ceb945702a726d2eb7350a6af8`, PR175
`8ba80e8cf3d243850611b477cf149dfb3dab2c01`, PR177
`e4403209d87dff65efea5d4cf2a25cdb59556632`, PR178
`cda78d92f404dd3219a7a4ed9322706654eddf29`, PR179
`27a2c7414fdb92eeca57ad552a9ab5c36d8430d8`, PR180
`f87cb69b3dd86257731ddfbab58c87bf3b5f63d6`, and PR181
`5f03d809b4495802971211ef13ff905f741d700d`. These were scoped research
context, not additional code imports or claims that their entire proof
packets were replayed. The existing core and Mathlib developments retain
their earlier frozen sources.
