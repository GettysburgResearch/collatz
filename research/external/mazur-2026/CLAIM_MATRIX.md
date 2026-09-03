# Claim matrix

The statuses below describe this import, not the source author's internal labels.

| ID | Statement | Source evidence | Local import status | Repository relation |
|---|---|---|---|---|
| `MZ-PRED-001` | For each fixed positive `a` with `3 ∤ a`, eventually `π_a(x) ≥ x^(9/10)` for the one-division Collatz map. | Paper v2; three public Lean-checked theorem forms; immutable ProofAtlas source commit `5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f`. | **EXTERNAL SOURCE-QUALIFIED.** Statement and normalization checked; no full source build or payload replay here. | Strong inverse-tree lower bound; does not prove fixed-source coefficient stopping `SC*` or ordinary extraction. |
| `MZ-PRED-002` | Stronger constant-factor form `π_a(x) ≥ C_a x^(901/1000)` eventually. | Same source family. | **EXTERNAL SOURCE-QUALIFIED.** | The strict `0.901` exponent is the useful input to the proposed exponent-race bridge. |
| `MZ-PRED-003` | The level-18 LP vector satisfies `129,140,163` rows and the adaptive potential satisfies `215,233,605` transition inequalities. | Paper reports exact Lean/native checks plus separate Python and C++ replay; payload hashes recorded. | **PARTIAL AUDIT.** Integer coefficient directions and worked rows checked locally; full 645.7 MB payloads not replayed. | Reusable certificate architecture; candidate source of structural potentials and joint transfer-operator methods. |
| `MZ-ND-001` | For every `f(N) → ∞`, a natural-density-one set of positive starts has a raw Collatz iterate below `f(N)` by `C_Coll log N`, with `C_Coll = 1509503/(5000 log 2) < 436`. | Paper v2; public Lean-checked package; immutable ProofAtlas source commit `ca3dd0d63920411213403092aecc6946619eb082`. | **EXTERNAL SOURCE-QUALIFIED.** Statement, quantifiers, and constant identities checked; no full 599-file source build here. | Forward typicality result. It permits a density-zero exceptional set and does not imply convergence or `SC*`. |
| `MZ-ND-002` | Odd-relative natural-density-one Syracuse descent uses `C_Syr = 501501/(5000 log 2) < 145`; for every `0<d<5/143`, the fixed-target timed bad fraction is at most `C_d (log N_0)^(-d)`. | Same source family. | **EXTERNAL SOURCE-QUALIFIED.** Exact exponent and clock arithmetic checked locally. | Supplies the forward side of a possible exponent-race program, but its present fixed-height estimate is linear in the counting endpoint. |
| `MZ-ND-003` | On a natural-density-one set, a hit below `sqrt(N)` occurs in the raw-time window `log N/(2 log 2) < m ≤ C_Coll log N`. | Same source family. | **EXTERNAL SOURCE-QUALIFIED.** Deterministic lower inequality and clock conversion checked locally. | Shows logarithmic raw time is order-sharp for this target, not that constant `436` is sharp. |
| `MZ-BRIDGE-001` | If fixed-target predecessor growth has exponent `γ` and fixed-height logarithmic-time non-descent has counting exponent `β<γ`, then Collatz follows. With `γ=0.901`, any such forward bound with `β<0.901` closes the conjecture. | New synthesis in this packet; elementary least-counterexample proof in `synthesis-and-roadmap.md`. | **PROPOSED CONNECTION; PENDING NARROW REVIEW.** | New direct bridge between inverse basin growth and forward exceptional-set thinning; distinct from resident `RD-BRIDGE-001` (`SC* + FC*`). |

## Required non-claims

- Neither imported paper proves the Collatz conjecture, convergence for every start, or a nontrivial cycle exclusion.
- Natural density one is not pointwise control and does not remove a fixed exceptional source.
- `x^0.90` or `C_a x^0.901` predecessor growth has zero possible natural density and therefore does not contradict a density-zero exceptional set by itself.
- The fixed-target estimate `C_d (log N_0)^(-d) X` has no power saving in `X` when `N_0` is fixed.
- Public Lean checking and source-host review are substantial evidence, but this repository import is not an independent end-to-end replay.
- No priority claim is adopted beyond the dated and qualified language of the source records.
