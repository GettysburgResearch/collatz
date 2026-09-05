# Claim-level review matrix — reviewer A

Cutoff: **2026-09-05 15:52:28 UTC**. These verdicts are review findings, not canonical status changes. A VERIFIED conditional implication does not establish its hypothesis. A source's successful finite pilot does not establish its all-time target.

## Exact source keys and inheritance

- **S87:** `e9adc409031a61f3801c4ee1e1e6deeb34188eb7`.
- **S88:** `c28922fb6d1c070bf86a76192f40bc9ea3edd67c`.
- **S90:** `78ac7c8489f1df81230402808b1f4b77b18fae73`.

Every entry inherits its subsection's full source SHA, exact path, dependencies, proposed destination, and correction default. Row-specific qualifications override these defaults. Together these fields are the exact SHA/path/ID key; **ID alone is unsafe** because CLOCK_DEFECT and BOUNDARY_FAN reuse numbers. Origin commits are in INVENTORY.md.

VERIFIED means the stated narrow written argument was independently reconstructed. VERIFIED WITH FIXES is limited to the explicitly reviewed scope. GAP-BLOCKED distinguishes open mathematics from unperformed certification. REJECTED applies to a specified false strengthening or unsafe acceptance contract, not indiscriminately to its PR. **NOT REVIEWED** is an explicit evidence boundary, never an implied passing verdict.

All destinations below are proposals. All otherwise passing rows still require the shared editorial/evidence release actions A1–A7 in ACTION_MAP.md. Proposed repairs RP-A1–A4 remain separate and pending review.

## PR #87 — external predecessor dossier

Source S87, `research/external/mazur-2026/predecessor-x090.md`. Dependencies: Mazur manuscript v2 and immutable public source `5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f`, including its large generated certificates. Destination: existing external predecessor dossier and evidence ledger, not an independently accepted resident external theorem. Default correction: preserve EXTERNAL SOURCE-QUALIFIED and distinguish original author evidence from reviewer checks.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-001 / MZ-PRED-001 | VERIFIED WITH FIXES | Faithful eventual unit-coefficient X^0.90 statement for each fixed positive target not divisible by three. Manuscript statement, proof architecture and public main declaration inspected. | Release: qualification above; no independent acceptance of full external proof. |
| RA-002 / MZ-PRED-002 | VERIFIED WITH FIXES | Faithful stronger c_b X^0.901 statement. Direct declaration inspected; exact coefficient directions independently checked. | Retain positive target-dependent constant and cutoff; do not replace them with a unit constant at .901. |
| RA-003 / MZ-PRED-003; full external acceptance | GAP-BLOCKED | **NOT REVIEWED end to end:** 129140163 LP rows and215233605 potential transitions. Reviewer checked coefficient comparisons and three worked rows, not645700815 bytes of payload. | Release: full replay or an explicitly accepted external-trust policy before an independent-computation label. Generated native_decide trust must remain visible. |

## PR #87 — external natural-density dossier

Source S87, `research/external/mazur-2026/natural-density-log-time.md`. Dependencies: manuscript v2; public source `ca3dd0d63920411213403092aecc6946619eb082`; analytic/formal input chain. Destination: existing external natural-density dossier. Default correction: retain source qualification and distinguish raw, shortcut and odd-to-odd clocks.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-004 / MZ-ND-001 | VERIFIED WITH FIXES | Faithful natural-density-one logarithmic raw-clock statement for every diverging threshold, not convergence. Parsed manuscript, selected proof passages, main Lean surface and recorded evidence inspected. | Release: retain one C before the threshold function; no full formal-build claim. |
| RA-005 / MZ-ND-002 | VERIFIED WITH FIXES | Odd-relative density and fixed-floor fraction O((log H)^-d), 0<d<5/143. Exact clock and exponent-margin arithmetic reconstructed. Endpoint count remains exponent one in X. | Quantitative source floor H>=2. Do not insert log1; explain any odd H=1 normalization separately. |
| RA-006 / MZ-ND-003 | VERIFIED | Deterministic lower raw hitting-clock for a hit below sqrt(N), from N/2^m<sqrt(N). This establishes order of the clock, not optimality of436. | None for the deterministic implication. The imported upper theorem remains source-qualified. |
| RA-007 / full599-file closure | GAP-BLOCKED | **NOT REVIEWED:** complete182625-line formal/analytic dependency closure. Main theorem surface and recorded evidence are not an independently executed kernel build. | Release: preserve external evidence ceiling. Destination: external evidence ledger. |

## PR #87 — provenance

Source S87, `research/external/mazur-2026/sources.json`. Dependencies: the immutable source releases, paper manifests and notice. Destination: external `sources.json`, `papers/README.md` and `NOTICE.md`.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-008 / source-version fingerprints | VERIFIED WITH FIXES | Manuscript worktree and public release commits are different identities. Declaration pins and recorded sizes/hash strings cross-checked; raw-byte acquisition failed. | Release: hashes were NOT independently recomputed; attribute the original57-check replay. No PDF redistribution. |

## PR #87 — original conditional synthesis

Source S87, `research/external/mazur-2026/synthesis-and-roadmap.md`. Dependencies: its explicit INV(gamma) and FWD(beta) hypotheses, not an assumed fixed-floor theorem. Destination: proposed `research/integrated/exceptional-mass/`. Default correction: conditional wording only; preserve the missing premise.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-009 / INV+FWD bridge | VERIFIED | For beta<gamma, the least-counterexample and odd-core count give a contradiction. Logarithmic odd-core loss is harmless for a strict power gap. Includes cycles. | Prefer the later endpoint-one/critical refinement for orientation. Original remains valid, not refuted. |

## PR #87 — focused local forward attack

Source S87, `research/external/mazur-2026/fixed-height-power-saving-attack.md`. Dependencies: exact parity cylinders, elementary product/counting arguments, and any recurrence explicitly assumed. Only the final bridge additionally uses INV(gamma). Destination: proposed coefficient-counting and exceptional-mass packets. Default correction: retain the exact population and conditional hypothesis.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-010 / Proposition1; MZ-BRIDGE-001 | VERIFIED | A single eternal odd floor H=1 with beta<gamma suffices. The timed bound is stronger. Odd-core contradiction independently reconstructed. | Later T-ASTRA-001 strengthens this; no need to erase the original implication. |
| RA-011 / Theorem2; MZ-FWD-001 | VERIFIED | SC sources are O(X^eta log X), not all exceptional starts. Exact parity bijection/terminal binomial proof reconstructed; reviewer checks through depth12. | No basin extrapolation. |
| RA-012 / Proposition3 | VERIFIED | SC language has entropy eta=h2(log2/log3). Cyclic-minimum rotation and Stirling argument reconstructed; finite rotation cases checked. | Thinness is not emptiness. |
| RA-013 / Theorem4; MZ-FWD-002 | VERIFIED | Global forward minima have the stated O(X^eta log X) count. Dyadic product estimate and entropy-continuity upper bound reconstructed. | Minima do not represent basin mass without multiplicity. |
| RA-014 / Lemma5; MZ-FWD-003 | VERIFIED | Normalized dyadic recurrence has stated geometric solution; resonance of equal rates retains a factor j. Exact2*93^10<100^10 reproduced. | Recurrence is conditional. |
| RA-015 / MZ-FWD-R01 | VERIFIED WITH FIXES | Abstract repeated fiber/scale loss and phase-length ceilings checked. Full source-specific Inselmann attribution was NOT independently compared throughout. | Release: separate proved abstract algebra from source-qualified literature attribution. Destination: method-boundary appendix. |
| RA-016 / actual .93 contraction | GAP-BLOCKED | Actual survivor contraction yielding a fixed-floor power saving is unproved. Finite entropy counts do not instantiate it. | Mathematical open obligation, not a requirement to suppress qualified partial results. Destination: roadmap. |

## PR #88 — native MZ-FH file

Source S88, `research/external/mazur-2026/fixed-height-forward-power-saving.md`. Dependencies: its exact parity/product arguments and explicitly hypothesized physical descent, local saving, scale reduction, and survivor-specific fiber gain. Destination: proposed coefficient-counting packet and exceptional-mass method-boundaries. Default correction: no root-to-basin or finite-to-all-time promotion.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-017 / MZ-FH-001 | VERIFIED | Native-horizon no-descent count <=6499+2X^(19/20). Product bound above6500 and parity injection reconstructed; both large integer inequalities pass. | None beyond scope. |
| RA-018 / MZ-FH-002 | VERIFIED | Sharp exponential rate eta for native-horizon no-descent roots. Ballot lower bound and source-size-split upper proof reconstructed. | Not a fixed-floor exceptional-basin count. |
| RA-019 / MZ-FH-003 | VERIFIED | Generic X^(1-r) fibers transform saving D into rD and lose fixed endpoint power under repeated scale reduction. | Architecture-specific obstruction, not all methods. |
| RA-020 / MZ-FH-004 | VERIFIED | A positive extra fiber saving uniform over all endpoint subsets contradicts mass conservation. | Preserve the refutation and survivor-specific alternative. |
| RA-021 / MZ-FH-005 intended positive-beta range | VERIFIED WITH FIXES | Recursive bootstrap and horizon proof work for intended beta>0 and beta>max(1-D,1-delta/(1-r)). Reviewer reconstructed the induction and clock. | Release: RP-A1 explicitly delimit positive-beta timed application. No actual parameters/fiber theorem supplied. |
| RA-022 / MZ-FH-005 unrestricted beta<=0 endpoint | GAP-BLOCKED | Printed every-beta wording lacks a positivity guard. Dyadic shell summation does not justify preserving a nonpositive exponent or ignoring small-source clock contributions. | Mathematical statement/proof endpoint: restrict or prove separately. No actual Collatz counterexample to this conditional is asserted. RP-A1 pending, not retroactive verification. |
| RA-023 / actual decorrelation(19) | GAP-BLOCKED | No actual local split and survivor fiber gain crossing .901 are established. The checker tests illustrative algebra only. | OPEN roadmap hypothesis. |
| RA-076 / stronger all-subset fiber premise | REJECTED | Its asserted universal positive counting saving is impossible by MZ-FH-004. | Keep the false strengthening separately identified. |

## PR #90 — critical mass and killed weights

Source S90, `research/astra-critical-mass/PROOF.md`. Dependencies: elementary local operator/weight proofs; only T-ASTRA-001's final Collatz implication uses source-qualified P(gamma). Destination: exceptional-mass and weight-obstruction packets. Default correction: preserve killing at1, positivity/summability and finite/uniform boundaries.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-024 / T-ASTRA-001 | VERIFIED | Critical liminf total count, sublog weighted mass, and odd little-o forms suffice under P(gamma). Dyadic saturation and partial summation reconstructed. | Does NOT claim odd-count liminf alone. |
| RA-025 / T-ASTRA-007 | VERIFIED | Critical logarithmic recurrence retains saving when kappa*r^(-p)<1. Exact substitution reconstructed. | Actual recurrence remains uninstantiated. |
| RA-026 / T-ASTRA-002 | VERIFIED | Positive summable killed Lw<w excludes invariant exceptional set; uniform Green mass is sufficient. Correctly removes inverse source1 at endpoint2. | Conditional criterion, not a constructed global supersolution. |
| RA-027 / T-ASTRA-003 | VERIFIED | Power-like n^(-s+o(1)) pointwise inverse weights fail eventual nonexpansion for fixed blocks. | Actual all-odd ordinary paths; not a 2-adic extraction or all-weight obstruction. |
| RA-028 / L-ASTRA-004 | VERIFIED | w0 summability<=3, analytic source tail and exact drift on two residue classes. Elementary splitting and class identities reconstructed. | Third class fails; do not extend. |
| RA-029 / T-ASTRA-005 | VERIFIED | Infinite even-ray repair fails every fixed floor/block for1<a<2. Valuation stabilization, domination and ordinary spikes inspected. | Not a refutation of integrated all-depth Green control. |
| RA-030 / finite G256 enclosure | VERIFIED | Reviewer independently reconstructed all sources through2^18 and five horizons, retained one unresolved at256, and analytic omitted tail:8.6140<G256<8.9619. | Finite-time only; full source-encoded artifact hash has separate rowRA-080. |
| RA-071 / Q-ASTRA-001 | GAP-BLOCKED | sup_K G_K<infinity, including working ceiling16, is unproved. | Mathematical OPEN target; finite tail grows with K at fixed cutoff. Destination: roadmap. |

## PR #90 — first-passage interface

Source S90, `research/astra-critical-mass/FIRST_PASSAGE.md`. Dependencies: positive physical first-passage dynamics and full integrality. Destination: proposed `research/integrated/first-passage-fibers/`. Correction default: keep all prefix and unresolved-source guards.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-031 / L-ASTRA-006 | VERIFIED | Exact endpoint AP, strict real interval and source-mass identity including unresolved sources; endpoint support is (Y/2,Y]. Complete reviewer AP/source comparisons give99 and233 starts. | No endpoint mixing or extra fiber saving follows from this compiler. |

## PR #90 — finite dictionaries and quantitative burden

Source S90, `research/astra-critical-mass/CONTINUATION.md`. Dependencies: local killed operator and weights in PROOF.md; stated finite positive/guarded affine forms. Destination: weight-obstructions and finite-history interface. Correction default: none beyond the exact method class and assumptions.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-032 / T-ASTRA-008 | VERIFIED | Fixed weighted exponential Green target forces logarithmic hitting time; stated converse requires sufficiently small exponent rate. Single-source and geometric argument reconstructed. | Stronger than qualitative convergence. |
| RA-033 / T-ASTRA-009 | VERIFIED | Existence of some positive summable strict supersolution iff Collatz. Converse construction uses known stopping times. | No unconditional computable solution from this converse. |
| RA-034 / L-ASTRA-010 | VERIFIED | Summability/tails of finite affine valuation dictionaries and even rays with their positivity, zero and size guards. | Do not drop guards. |
| RA-035 / T-ASTRA-011 | VERIFIED | Finite dictionary plus all even rays fails every fixed bounded block menu. Ordinary CRT spike and escaping-centre proof reconstructed. | Not all infinite dictionaries or aggregate estimates. |
| RA-036 / C-ASTRA-012 | VERIFIED | Finite Green-history compiler is correct with ordinary congruence and killing guards. | Unguarded dictionary is only a majorant; cannot identify it with actual history mass. |
| RA-037 / C-ASTRA-013 | VERIFIED | A deeper actual history defeats uniform relative error for a fixed truncation. | Summable spike family does not refute integrated global Green bound. |

## PR #90 — ordinary run renewal

Source S90, `research/astra-critical-mass/RUN_RENEWAL.md`. Dependencies: exact total packet map, fixed-r arithmetic cylinders, retained affine errors; no independent parity after transport. Destination: proposed `research/integrated/ordinary-run-renewal/`. Default correction: fresh-shell and finite-time scope; release checker hardening RA-088 is separate.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-038 / T-ASTRA-014 | VERIFIED | Whole odd/even-run F is total; inverse coding is complete/nonduplicating; endpoint killing captures core entry. Exact run reversal reconstructed. | Packet count is not shortcut clock. |
| RA-039 / L-ASTRA-015 | VERIFIED | Integrated one-packet omitted inverse tail <=(72/5)2^(-5B/4). Full series estimate reconstructed. | Not invariant seed bound after arbitrary returns. |
| RA-040 / T-ASTRA-016 | VERIFIED | Ordinary fixed-r shell moment tends to P_theta^r under theta((log2 3)^r-1)<1. Exact cylinders and affine-error accounting inspected. | Does not imply transported distribution independence. |
| RA-041 / C-ASTRA-017 | VERIFIED | Stated cofinal one-packet fresh-shell bound22/25 and two-packet estimate. Reviewer checked radical pressure, all50 base inequalities and all5 shift25 ratios; written induction inspected. | Not pointwise drift or a uniform-in-r theorem. |
| RA-042 / T-ASTRA-018 | VERIFIED | Actual signed discrepancy sublinearity would imply convergence. Finite-time summability, telescoping and persistent source mass argument reconstructed. | The signed budget itself is OPEN; see MINIMUM_RANK Section0. |
| RA-043 / R-ASTRA-019 | VERIFIED | Blind fresh-shell iteration is refuted on actual full-support seed: scaled masses21<22<23<24. Reviewer literal packet replay and full omitted-source estimate reproduce it. | Does not assert undiscounted masses increase or rule out eventual decay. |
| RA-072 / Q-ASTRA-002 | GAP-BLOCKED | Actual sublinear signed discrepancy is unproved. | Mathematical OPEN target; no automatic cancellation. Destination: roadmap. |
| RA-077 / blind fresh-shell iteration | REJECTED | Fresh ensemble inequality cannot simply be reused on the actual transported ensemble. | Preserve R-ASTRA-019 as the separate valid refutation. |

## PR #90 — minimum-rank merging

Source S90, `research/astra-critical-mass/MINIMUM_RANK.md`. Dependencies: #91 section/fan/rank definitions at `b8c88843726ee7ac11cf91323c69bf911ca50706`, rederived locally; no other #91 theorem assumed. Destination: proposed `research/integrated/rank-merging/`. Default correction: retain positive ordinary common endpoint, all rank guards and unresolved residuals.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-044 / Section0 | VERIFIED | Signed discrepancy plus initial mass is comparable to cumulative occupation. Reconstructed from0<=p_j<=q*m_j. | Telescoping identity alone supplies no cancellation estimate. |
| RA-045 / T-ASTRA-020 | VERIFIED | Complete section/fan minimum and conditional total lower-rank merger criterion. Reviewer checked5461 complete physical fans. | Minimum component rank is not minimum cycle value. |
| RA-046 / T-ASTRA-021 | VERIFIED | h=1/even reductions and the specified h=2 residual of five progressions. Rank comparisons and necessary residue test reconstructed. | Not complete residual elimination or a claim all remaining inputs are exceptional. |
| RA-047 / T-ASTRA-022 | VERIFIED | Backward rank estimate with full positivity, integrality and physical replay. Shifted B>0 identity reconstructed. | Proper-factor congruences are insufficient. |
| RA-048 / T-ASTRA-023 | VERIFIED | Two reverse returns bypass arbitrary prescribed finite forward rank delay on CRT families.100110 formula and all-parameter guards inspected. | Source varies with parameters; no infinite ordinary witness. |
| RA-049 / T-ASTRA-024 | VERIFIED | Upward merging diagrams lift with initial strict drop and limiting rank ratio<=1. Fractional-linear monotonicity inspected;769/1822 replayed. | A finite rank drop alone does not justify every lift. |
| RA-073 / Q-ASTRA-003 | GAP-BLOCKED | Universal total physical lower-rank merging cover is unproved. | Mathematical OPEN target; normalization can halt at an unresolved residual. Destination: roadmap. |

## PR #90 — remainder cancellation

Source S90, `research/astra-critical-mass/REMAINDER_CANCELLATION.md`. Dependencies: global P=(2n+1)^2/3^h, exact shifted affine remainders, ordinary positive sources. Destination: rank-merging and preserved method refutations. Default correction: no finite-cover or synchronous-to-asynchronous extrapolation.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-050 / T-ASTRA-025 | VERIFIED | Global rank normalization and basin-stability equivalence. h=0/h=1/even-high cases and induction reconstructed. | Basin stability itself is not proved. |
| RA-051 / T-ASTRA-026 | VERIFIED | Equal-clock equal-remainder words yield exact ternary quotient and rank loss when odd counts differ appropriately. | Full integer congruence and positive witness required. |
| RA-052 / T-ASTRA-027 | VERIFIED | Named seven/ten-step progression rules. Reviewer physically replayed661/73 and8779/975; symbolic lifting inspected. | Full425-rule artifact has separate replay boundary. |
| RA-053 / T-ASTRA-028 | VERIFIED | Deep initial ternary precision forces stated finite forward rank barrier; ordinary CRT bypass exists. | No universal forward or merging clock claimed. |
| RA-054 / R-ASTRA-029 | VERIFIED | Universal equal-clock merger with (n-4)/9 is false. Reviewer checked13/1 and859/95 paths and permanent opposite phases. | Does not refute ordinary asynchronous merging or convergence. |
| RA-074 / universal x->9x+4 basin stability | GAP-BLOCKED | Equivalent closure premise remains unproved. | Mathematical OPEN target; homogeneous finite rules do not establish it. Destination: roadmap. |

## PR #90 — unequal clocks

Source S90, `research/astra-critical-mass/CLOCK_DEFECT.md`. Dependencies: local rank/remainder arguments and exact **shortcut clocks**, not section-return radius. Destination: rank-merging/clock-defect packet. Default correction: preserve all guards; resolve display-ID collisions under A3 without rewriting originals.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-055 / T-ASTRA-030 | VERIFIED | If3^H>=12^M, every lower-rank merger with both clocks<=M is exact homogeneous same-clock stripping. Defect bound, noncancelling valuation and empty-word cases inspected. | Not a theorem that some diagram exists beyond this lower bound. |
| RA-056 / C-ASTRA-031 | VERIFIED | Specified CRT family has minimum diagram clock in [M_H+1,4H+1]. All-odd obstruction and explicit1^(4H)0 upper certificate inspected. | Family-local Theta(H), not a global bound. |
| RA-057 / L-ASTRA-032 | VERIFIED | A nonzero fixed defect freezes witness valuation below the source precision threshold. | Ordinary integrality, positivity and limiting rank guard retained. |
| RA-058 / T-ASTRA-033 | VERIFIED |859/517 and its progression work at h=2; the same words fail at higher depth. Named physical merger reproduced; depth algebra inspected. | Do not promote to all h. |
| RA-059 / T-ASTRA-034 rule contract | VERIFIED | Every accepted rule gives an upward infinite lower-rank progression with frozen h=2. Both ternary lifts, positive minimal source, exact witness and limit inspected in compiler. | The complete263-rule census is separately NOT replayed. |

## PR #90 — inverse boundaries

Source S90, `research/astra-critical-mass/BOUNDARY_FAN.md`. Dependencies: local section/fan/minimum formulas. Destination: proposed `research/integrated/inverse-frontier/`. Default correction: distinguish this file's IDs from CLOCK_DEFECT; retain the negative recursive-pruning result.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-060 / T-ASTRA-030 | VERIFIED | Complete radius-two inverse minimum from at most five candidates. Reviewer1364 full balls match. | Not an all-depth recursive pruning theorem. |
| RA-061 / T-ASTRA-031 | VERIFIED | Three disjoint subprogressions remove the stated radius-two part of the old h=2 residual. Fan algebra and progression guards inspected. | Counts overlap other certificate families; do not add them globally. |
| RA-062 / T-ASTRA-032 | VERIFIED | Three-parameter ordinary bridge families give quarter-rank reduction and arbitrary prescribed finite forward delay. | Full10 1^a0 formula and CRT guards, not fixed-source extraction. |
| RA-063 / L-ASTRA-033 | VERIFIED | No positive T^5 fixed point; implies no equal-clock meeting for the specified five-step bridge. All32 words independently checked. | Excludes one finite cycle length only. |
| RA-064 / R-ASTRA-034 | VERIFIED | Greedy least-ancestor iteration and recursive boundary-only deletion are false.29371/69619 and208363/4445077 independently reconstructed. | Preserve both counterexamples. |
| RA-078 / recursive boundary-only pruning | REJECTED | Radius-two minimum identity cannot be iterated by permanently deleting interiors. | Separate valid replacement is the AS7 remaining-depth rule, not retrospective verification. |

## PR #90 — inverse shadows and full inverse-only obstruction

Source S90, `research/astra-critical-mass/INVERSE_SHADOW_FRONTIER.md`. Dependencies: signed physical inverse tree, positive integer P on compared sources, explicit finite-depth precision thresholds. Destination: inverse-frontier packet and method-boundary record. Default correction: finite-radius termination is not a total merging cover.

| Key / ID | Verdict | Scope and evidence | Required correction / blocker |
|---|---|---|---|
| RA-065 / L-AS7-001 | VERIFIED | Negative comparison tree and B_r<=(r+1)^2+1. Entire reviewer radius10 tree and exact table reproduced. | No negative-to-positive all-depth extraction. |
| RA-066 / T-AS7-002 | VERIFIED | Deep interiors are physical affine shadows; all compared ranks exceed(64/3)parent rank. Strict precision and full-cone bijection proof inspected. | Boundary cancellation cannot be assumed away when the guard fails. |
| RA-067 / T-AS7-003 | VERIFIED | Remaining-depth pruning is lossless for every fixed inverse radius; branching<=D^2+1. Reviewer388 complete/pruned positive cases agree. | Not a bit-complexity bound or universal stopping result. |
| RA-068 / T-AS7-004 | VERIFIED | Strict record frontier plus sufficient extra valuation gives positive ordinary lower-rank families. CRT and full replay guards inspected. | Reaching a frontier alone does not force rank loss. |
| RA-069 / C-AS7-005 | VERIFIED | Specified delayed interior chain has unbounded chosen delay and then a guarded rank gain. Elementary4-power valuation and finite bridge inspected. | Not a universal minimal diagram clock. |
| RA-070 / R-AS7-006 | VERIFIED |121 has no cheaper ancestor at any depth. Any cheaper merger first moves forward at least54 shortcut steps;40 attains it. Reviewer enumerated all cheaper sources and their entire forward closure. | This all-depth negative result has a complete finite witness-pool proof. |
| RA-075 / Q-AS7-001 | GAP-BLOCKED | Total finite forward-endpoint/cheaper-source selector remains unproved. | Mathematical OPEN target. Destination: roadmap, not an accepted theorem. |
| RA-079 / universal inverse-only cheaper ancestor | REJECTED | Unlimited inverse-only search cannot certify every ordinary root. | Preserve121 counterexample; allow genuinely forward-accessible diagrams in future research. |

## Complete encoded artifacts — independent replay boundaries

All rows in this section use **S90** and exact path `experiments/<directory>/results/canonical.json`. Dependencies: corresponding proof and both source implementations, all statically inspected. **All verdicts are GAP-BLOCKED for release of the complete independent-artifact claim; all full encoded artifacts are NOT REVIEWED end to end.** This does not negate the narrower reviewer results. Destination: backstage reproducible evidence linked to extracted packets. Required correction: retain source-reported status or replay the complete immutable corpus before accepting its aggregate hash/count.

| Key / exact directory (artifact ID) | Evidence actually obtained | Evidence NOT obtained |
|---|---|---|
| RA-080 / X-ASTRA-001-critical-mass | Independent finite Green and two complete AP maps. | Every pilot/weight row and source canonical hash. |
| RA-081 / X-ASTRA-002-transport-closure | Both programs statically read; symbolic weight and compiler proofs reviewed. | Complete63-row witness/889-compiler artifact and original hash. |
| RA-082 / X-ASTRA-003-run-renewal | Independent50 bases,5 induction ratios and actual transported counterexample. | Complete original canonical hash; unsafe optimized acceptance is separately rejected below. |
| RA-083 / X-ASTRA-004-minimum-rank |5461 fans,1364 radius-two checks and named diagrams reconstructed. | Full87381-row census and all37 tiles. |
| RA-084 / X-ASTRA-005-remainder-cancellation | Named physical rules and phase controls reconstructed. | Full425-rule encoded census. |
| RA-085 / X-ASTRA-006-clock-defect | Both programs statically audited; analytic rule contract and named merger checked. | All263 rules and404 residual binary classes regenerated. |
| RA-086 / X-ASTRA-006-boundary-fan | Modest complete balls and both failed-pruning examples reconstructed. | Full87381-root encoded census. |
| RA-087 / X-AS7-001-shadow-frontier | Whole radius10 negative table,388 positive comparisons and121 certificate. | Complete1632-family encoded artifact and original hash. |

## Checker and release-specific claims

The source SHA/path column is the exact source key; dependencies and destinations are explicit per row. These are not global mathematical verdicts on the source PRs.

| Key / source / ID | Verdict, scope and evidence | Dependencies; correction; proposed destination |
|---|---|---|
| RA-088 / S90 `experiments/X-ASTRA-003-run-renewal/verify.py` / optimized acceptance contract | REJECTED. Assert-only validate loses all acceptance checks under-O. Reviewer isolated source-equivalent function rejects a resealed false payload normally and accepts it optimized. The full upstream command was NOT run. | Python assert semantics and frozen source function. RELEASE blocker: RP-A2 explicit exceptions or fail-closed guard, followed by new-byte replay. Checker erratum/release gate. |
| RA-089 / S87 `research/external/mazur-2026/check_import.py` / arithmetic scope | VERIFIED WITH FIXES. Integer/rational portions are exact; some clock/delta diagnostics use floating tolerances. Optional PDF mode hashes supplied bytes, not proof correctness. Static read and15 reviewer exact constants. | sources.json and source PDFs when supplied. RELEASE: separate exact comparisons from diagnostics; do not claim reviewer PDF replay. External evidence harness. |
| RA-090 / S88 `research/external/mazur-2026/check_fixed_height_attack.py` / frozen verification interface | VERIFIED WITH FIXES. Inspected finite arithmetic is sound, but default execution regenerates/overwrites its report. Reviewer depth12 and large integer comparisons independently pass. | Stated finite integer/Fraction checks only. RELEASE: RP-A3 nonmutating --check and unique output path, then replay. Coefficient-counting evidence harness. |
| RA-091 / S90 `research/astra-critical-mass/README.md` / orientation | VERIFIED WITH FIXES. At the frozen head, README and PR description stop at clock-defect; the actual tree includes boundary-fan and inverse-shadow. | Actual eight-commit history and publication reports. RELEASE: exact current pass inventory and filename-qualified aliases; preserve historical authoring receipts. Packet index/backstage provenance. |

## Count and non-promotion boundary

This matrix has **91 entries:58 VERIFIED,10 VERIFIED WITH FIXES,18 GAP-BLOCKED,5 REJECTED**. Counts combine theorem, method-boundary, artifact and editorial entries; they are not a percentage of a Collatz proof or an approval of whole PRs. External proof closures and complete encoded artifacts remain explicitly unreviewed. The full #91/#92 programmes and the unsubmitted fixed-height branch are outside this review. Proposed repairs are not applied to or substituted for their flawed originals.
