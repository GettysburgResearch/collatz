# Integration and public-readiness checklist

Baseline `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`. **Recommendations only.** No edits below have been applied to source packets or canonical records. Any new wording/repair/synthesis needs its own review.

## Release blockers and precise fixes

| ID | Owner / priority | Exact edit or action | Acceptance test / present status |
|---|---|---|---|
| F01 | Integrator / blocking | Qualify #92 claim and artifact identities by full SHA+path+ID; distinguish both fifth-pass schema families. Update the insufficient PR-only rule in `claims/README.md`, `claims/aliases.json`, `CONTRIBUTING.md` and integration guidance through a separate reviewed change. | A lookup for T-A3-1051 resolves to two explicitly distinct statements; neither canonical record is overwritten. **OPEN** |
| F02 | Integrator / blocking | Resolve the #91/#92 shared README with a neutral mathematical index. Add links to rank-budget and spectrum-switch as separate siblings. Correct `experiments/X-ASTRA3-005-spectrum-switch/README.md` to its own `pass5-spectrum-switch/README.md`. Refresh #92 PR description separately while preserving historical report prose. | Every new theorem reachable in <=3 meaningful links without knowing an agent/pass name. **OPEN** |
| F03 | Mathematical editor / required | Handle A=0 before T-A3-453's logarithmic cutoff; keep the nonempty A>0 clause separate. Say “infinite distinct value set / non-eventually-periodic orbit” in T-A3-403/451 summaries. | Word `0` has empty d-interval, no log(0); periodic orbit is not fed to the injective counting argument. Proposed correction only. **OPEN** |
| F04 | Packet author/integrator / required | Put domain, source/end projections, absorbing state, norm and entry-envelope assumptions next to every exported K, A and resolvent formula. Explicitly distinguish G_q, G_le and #91's nonresonant set. | `3->4` is not misclassified; unsafe moment counterexample coexists visibly with the valid safe theorem. **OPEN** |
| F05 | Checker maintainer / required | Replace critical assertion-only validation or refuse optimized execution. Prioritize `X-ASTRA3-002-three-routes/verify.py::validate/verify_ranks`; document policy for early generator/internal assertions. | Recomputed-hash scope, coverage, missing-row and endpoint mutations fail under the supported interpreter modes. Current early -O safety not certified. **OPEN** |
| F06 | Owner / blocking before licensed release | Record intended text/code/data license and third-party provenance/permissions. No root LICENSE was present at baseline. Check external fragments and legacy data separately; do not copy the Mazur PDFs merely because they are hosted publicly. | Owner-approved license/provenance inventory, no undocumented third-party redistribution. No legal clearance claimed. **OPEN** |
| F07 | Integrator / blocking for acceptance | Give each newly accepted component a readable local packet, exact source and review pin, evidence tier and next missing lemma. Keep this review separate from repository promotion. | Accepted theorem body locally readable; conditional premise visibly OPEN; all imported rewordings independently reviewed. **OPEN** |
| F08 | Integrator / required | Preserve old archive cutoff and unresolved #67/#68/#69, mixed source verdicts, later unrevised theorem deltas, factor-repair dependencies and pending periodic/bridge synthesis. | No historical record gains a new verdict retroactively; old paths remain valid. **OPEN** |
| F09 | Infrastructure reviewer / blocking operational check | Obtain full authenticated checkout; run `python tools/check_integration_state.py` at baseline and proposed integration. Add separate validation of new namespace collisions, schema coverage, active links and artifact manifests—not a workflow in this PR. | Actual stdout/exit code with full checkout SHA, not fixture-only output. **NOT RUN HERE** |
| F10 | Owner / public launch | Review secrets/history, repository permissions and untrusted-code execution separately. This task does not authorize changing protections, visibility or Actions. | Dedicated owner/security receipt. Not inferred from absence of .github or from mathematical review. **UNREVIEWED** |
| F11 | Numerical reviewer / evidence label | Keep #92 pass1 large cone and pass2–4 canonical numeric claims labelled inspected/not fully replayed here. Targeted k19 test and proof audit are not the entire old protocol. Schedule those replays only when needed as accepted proof dependencies. | Exact script blob, payload digest, command and coverage receipt for each promoted numeric claim. **PARTIAL** |
| F12 | Curator / required | Keep source author/session identity distinct from publishing agent and independent reviewer. Preserve #92 import receipts, prepublication corrections and separate alternative fifth-pass authorship. | Citation tuple reaches original proof and publication record; no broad novelty claim without literature review. **OPEN** |

## Concrete public reading-path edits

| Surface | Baseline audit | Proposed change |
|---|---|---|
| `README.md` | Correct unsolved warning and human/agent paths; no false closure. | Add a compact “accepted results / reviewed but not integrated / open goals” panel only after decisions, linking mathematics not PR chronology. Keep two-minute orientation. |
| `AGENTS.md` | Explore/review/integrate separation is helpful; exact SHA policy sound. | Add path-qualified identity rule and require operator domain/absorbing set on transfer contributions; do not burden exploration with registry forms. |
| `docs/RESEARCH_MAP.md` | SC*, FC*, ordinary extraction and source-qualified synthesis clearly separated. | Add reviewed orbitwise SC-tail result and moving-rank programs as new source-qualified/accepted-by-decision components. Explicitly preserve positive-cycle and unsafe-control gaps. |
| `research/integrated/README.md` | Seven packets / eight records, periodic exception visible. | Add new packets only after exact integration review; do not replace pending periodic wording with an inferred status. |
| `research/RESULTS_CATALOG.md` | Good subject organization; preserves mixed/unreplayed older work. | Add rows for new destinations D1–D9 with exact evidence and open premise. Keep alternatives, no full-branch blanket verification. |
| `claims/*` | Independent status/residency fields sound; PR-only alias rule no longer sufficient. | Extend alias key and add path collisions. Keep mathematical verdict, acceptance and proof/dependency residency separate. |
| `STATE.md`, `docs/integration/CURRENT.md` | Appropriate nontransactional pointers. | Leave as pointers; no new front-stage pass log. |
| `archive/README.md` | Historical cutoff boundaries correctly immutable. | Append a new review-wave pointer after publication; do not edit 2026-08-01 facts. |
| `tools/check_integration_state.py` | Curated structure/status checker, not math verification. | Extend curated input coverage when integrating new packets; unit-test duplicate IDs, wrong sibling link and missing artifact. Do not claim this proves theorem correctness. |

## Proposed mathematical destinations

These are **destination proposals**, not newly created integrated records.

| Code | Suggested local destination after narrow extraction review | Content / retained boundary |
|---|---|---|
| D0 | `research/open-obligations/` and adjacent refutation sidebars | Unsafe control, full cover, SC*/cycles; rejected strengthenings remain separate from repairs. |
| D1 | `research/integrated/section-resonance/` | #91 exact section/fan, charged weight, safe elimination; retained resonance not convergence. |
| D2 | `research/integrated/source-charge/` | Prefixwise no-descent resource budget and frozen jets; upper charge hypothesis open. |
| D3 | `research/integrated/guarded-repayment/` | Separate P and R_* families; exact future-word/valuation guards and same-rank composition. |
| D4 | `research/integrated/survivor-mass/` | #92 exact Mellin / canonical boundary formulas; all-time bias unproved, external race qualified. |
| D5 | `research/integrated/return-echo/` | Same displacement, full denominator, physical continuation; rational control visible. |
| D6 | `research/integrated/rank-method-boundaries/` | Linear, separate nonlinear, joint finite observation restrictions; administrative carry normalization. |
| D7 | `research/integrated/orbitwise-coefficient-tail/` | Distinct-orbit counting, finite correction, SC tail and conditional local records; positive cycles remain. |
| D8 | `research/integrated/moving-rank-safe-dynamics/` | Total acceleration, computable minimum, properness, two spectrum proofs, two explicitly different safe regions. |
| D9 | `research/integrated/merging-resource-bounds/` | Finite rank fibers, witness endpoint lists, compulsory excursions, guarded near-optimal family; no temporal coverage. |

## Preserve these older unresolved boundaries

`IC-PERIODIC-001` stays SOURCE-QUALIFIED for its exact synthesis; `RD-BRIDGE-001` stays PROPOSED pending narrow review; SC* and FC* stay OPEN. `IC-REF-001` is an accepted refutation, not a verified original; `IC-REP-001` is a separate nonconstant repair with its exact PR16 dependencies (`900ba417c968d8a41bc56a30d3ccc941284d8ce2`) and review (`a518db7feece37513ddcda729553e8b8c4c4d657`) still source-pinned. The original 45-source/42-reviewed wave and unreviewed PRs 67–69 are immutable. Mixed #34/#42/#47 and later unreviewed M-6712/L-6916 additions do not inherit this review.
