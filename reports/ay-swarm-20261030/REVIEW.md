# AYH order swarm: frozen source review and execution receipts

## Status and immutable scope

**Collatz remains unresolved. All new mathematics is PROPOSED at project level.**
This is an in-session review by a root researcher and three independently
working specialist agents. It is not external peer review, a formal proof
assistant build, or a promotion into the repository's accepted-result registry.

The exact reviewed science commit is
[`d3b67fbf33f73ac80bb1339a3061e821d84c926c`](https://github.com/GettysburgResearch/collatz/commit/d3b67fbf33f73ac80bb1339a3061e821d84c926c),
tree `070e1be404688f93fb395c6d00b9edee4e008487`. It adds sixteen files to main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Review identity is the full science
commit together with the path and claim IDs below. A later reporting commit
adds this directory and clarifies README's empirical-coverage wording. All
proof-note and executable-source blobs remain unchanged.

The scientific entry point is
[the packet README](../../research/ay-swarm-20261030/README.md).
Published attribution, source pins, earlier project context, and novelty
limitations are in [SOURCES.md](../../research/ay-swarm-20261030/SOURCES.md).
In particular, AYH already proved termination of every one-rule deletion.
This packet does not claim priority for that theorem or certify that every
new formulation is unprecedented in the literature.

## What was independently reconstructed

In this table, **VERIFIED** means that another agent reconstructed the stated
argument at the frozen scope. It does not mean an all-input computational
test, external acceptance, or verification of neighboring open statements.

| Frozen path under `research/ay-swarm-20261030/` | Claim scope | In-session verdict and reconstruction |
|---|---|---|
| `orders.md` | O1 | VERIFIED: the two-rule context-order contradiction and the separate inflationary-map obstruction on a well-order; partial orders and state-dependent ranks remain outside its scope. |
| `orders.md` | O2–O3 | VERIFIED: the five-coordinate contextual difference table and the rewrite-budget accounting. The number of exceptional `ag` events is a parameter, not a proved bound for one arbitrary source. |
| `orders.md` | O4–O5 | VERIFIED: disjoint redexes, terminating/confluent normalization, residual lifting, binary-start frontier invariance, shielding during multi-`g` bursts, and descent of `(#g, first-g position)`. The section-return iteration remains OPEN. |
| `carry-geometry.md` | CG1–CG8 and the affine-rank obstruction | VERIFIED: the binary carry recurrence including the high boundary, signed singleton-run flux, exact odd-macro `ag` count, maximal source guard for `K`, unbounded one-event debt family, and incompatible affine inequalities. The guarded class is explicitly not invariant. |
| `srs-semantics.md` | SRS-01–SRS-04 | VERIFIED: unit decrease of administrative cost, exact dynamic replenishment, labelled random descent, and the characterization `F(value)+H` of unit-administration potentials. The weighted arithmetic decrease condition on `F` is OPEN. |
| `srs-semantics.md` | SRS-05 | VERIFIED WITH FIXES during drafting: require a finite nonempty collection of computable scalar charts, each strictly decreasing on every retained contextual rule. Universal exposed-winner coverage is OPEN. Multistage relative certificates are not silently converted into scalar charts. |
| `srs-semantics.md` | SRS-06–SRS-07 | VERIFIED: exact published matrices, lower-bound matrix defects, the small-index inverse-matrix case, Fibonacci separation, and failure of every fixed sub-Fibonacci nonnegative repair on the displayed family. This is a theorem about one specified published chart. |
| `representation-dag.md` | DAG-01–DAG-03 | VERIFIED WITH FIXES during drafting: exact quotient-node reachability was clarified; finite-fibre recursion, scalar dynamic programming, the vector-correlation boundary, and the all-nonnegative-real additive obstruction were independently reconstructed by two specialists. The universal obstruction uses an elementary case proof, not floating-point optimization. |
| `synthesis.md` | SYN-01 | VERIFIED: all auxiliary rules decrease `H`, even steps decrease the valuation coordinate, and precisely the stated odd guard decreases `K`. Every excluded nonterminal odd dynamic edge increases the lexicographic rank. Independent code checked 1,296 literal instances. |
| `synthesis.md` | SYN-02–SYN-03 | VERIFIED: the two clocks are not identified, ranks cannot be switched without a shared budget, and the section-return bound is `55L^2+18L+1`. A specialist independently checked the final polynomial-bound derivation. No decreasing rank for all returns has been supplied. |

The orders and semantics specialists checked each other's overlap. The carry
specialist separately reconstructed the published-chart Fibonacci argument
and the joint microscopic order. The semantics specialist compared compressed
carry counts to literal counts for every rule on 2,047 odd sources, covering
24,574 literal events. The root independently reconstructed the joint order
and small complete-fibre cost tables without importing the track modules.

Review retained several important failures: `9 ->_U 7` defeats the global
`K` rank; `25 ->_U 19` defeats a popcount-tie shortcut; one critical event
can have unbounded popcount cost; simple frontier length/count ranks fail;
and the selected published matrix envelope fails on an infinite family.
These examples are preserved in the scientific notes and data.

## Actual execution evidence

- [verification.json](verification.json) records eight successful executions:
  all four author programs normally and under `-O`, with exact byte equality
  to all four recorded result files. It also contains the root's independent
  microscopic-order and additive-table checks.
- [cross-checks.json](cross-checks.json) records the final independent checks
  and final source identities. The verifier was run normally and under `-O`
  after source freeze, and those two JSON outputs were byte-identical.
- [science-checkout.json](science-checkout.json) is the successful complete,
  clean-checkout validation of the exact science commit above: 331 tracked
  files, with the same commit and tree recorded before and after execution.
- [baseline-checkout.json](baseline-checkout.json) records the successful
  complete-checkout validation of the unchanged 315-file source baseline.
- [checkout-refusal.json](checkout-refusal.json) preserves an earlier refused
  attempt while new files were staged and HEAD still pointed to the baseline.
  The driver correctly rejected the dirty index before running checks. It is
  not counted as a successful checkout execution.

The full replay finished before documentation-only clarifications in README
and synthesis: the compressed run transducer handles ordinary binary odd
macros, not a complete section return; the result records retain failure
counts and representative examples, not a listing of every failed source.
Therefore its recorded hashes for those two prose files are earlier identities.
All five executable source
hashes and all four result artifacts are unchanged. The final cross-check
receipt pins every final prose and program blob, and the independent final
SYN-03 review covers the frozen text. No replay receipt was relabeled.

Selected bounded coverage, not universal convergence evidence:

| Program | Actual finite coverage |
|---|---|
| `orders.py` | 35,739 short contextual edges; 2,000 long contexts; 781 mixed normalization sources; 22,781 arbitrary-word prefixes; 1,024 binary starts; 30,534 frontier edges and 184,308 literal steps; 18,202 administrative edges and 12,332 single-`g` edges. |
| `carry_geometry.py` | 32,768 odd sources through 65,535; 18,510 rank decreases and 14,258 nondecreases; representative failures retained; 2,730 run skeletons; 256 parameters of the paired obstruction family; four enormous exact run cases. |
| `srs_semantics.py` | 7,421 local edges; 781 administrative normalizations; 512 binary sources under three schedules with 235,023 rewrites; 156 mixed-source schedules; exact matrix checks and 504 complete-fibre bands. |
| `representation_dag.py` | 83,788 representation words through value 1,024; 384 independent scalar-minimum checks; quotient DAGs at 64, 256, 1,024 and 4,096 bits, with 5,265,223 nodes in the largest case; all 1,023 nonzero weight tuples in the small search rejected. |
| `verify_packet.py` | 781 proper words and 1,296 literal edges; 3,125 additive-cost tuples and 28,125 exact complete-fibre formula checks, independently implemented. |

The mathematical notes prove the universal scoped statements separately.
Large finite inputs, exact arithmetic, and passing optimized-mode checks do
not prove the remaining all-input Collatz claim. No external Lean build,
unrelated legacy large search, or new Collatz verification record is claimed.

## Remaining proof obligations and handoff

The strongest constructive reduction is a total computable return operation
on single-`g` words `c u a g d`, with values `6p+2` and a polynomial literal
budget for each return. A well-founded order across every nonterminal return
would complete this route. The present work does not bound the number of
returns or their source lengths.

The next search should retain ordered carry intervals and exact run lengths.
The proved obstructions reject several simpler scalar substitutes; they do
not establish that a more elaborate order exists. A second route is to build
a finite family of valid scalar deletion charts and prove universal coverage
by an exposed minimizer. That coverage is likewise OPEN.

The guarded microscopic ordinal and the ten-rule positional ordinal cannot
be combined by choosing whichever decreases on the current rule. Any such
switching construction needs an independently proved common well-founded
budget. This is an explicit unresolved mathematical obligation.

## Final source identities

The table below is generated from the final cross-check receipt. All entries
except README are blobs in the frozen science commit; README contains the
reporting clarification described above. Full SHA-256 identities, including
the result-file identities, are retained in the JSON receipts.

| Path | Git blob |
|---|---|
| `experiments/ay-swarm-20261030/carry_geometry.py` | `1053d6681c60d1a1da056e1c7ad3b7243ed81f0d` |
| `experiments/ay-swarm-20261030/orders.py` | `0cc2328e6a440f1dc1192051283af9ba32894f0c` |
| `experiments/ay-swarm-20261030/representation_dag.py` | `4847287765f246c7d073dc49d8464ad7a894cfd4` |
| `experiments/ay-swarm-20261030/srs_semantics.py` | `c285350f0028ab76170c6e3bff6a81d1bb42e144` |
| `experiments/ay-swarm-20261030/verify_packet.py` | `dd77fda66229a3270bee645ab8a43a3c6f9f4bc7` |
| `research/ay-swarm-20261030/README.md` | `b0f6b8d53cf606d356050023a5c2e4d26384ec31` |
| `research/ay-swarm-20261030/SOURCES.md` | `14029c68c1950014daf09fd8cf8684c2dcb68c3f` |
| `research/ay-swarm-20261030/carry-geometry.md` | `9a6a32368b4e702266adfa839234cc15d655905a` |
| `research/ay-swarm-20261030/orders.md` | `80ffba49de277525622368a327329e34cb043133` |
| `research/ay-swarm-20261030/representation-dag.md` | `fca148f3ab9611141f5945a75033969f7ce0e946` |
| `research/ay-swarm-20261030/srs-semantics.md` | `077053af235dec9236a9a3bda7e54f28a406d6c1` |
| `research/ay-swarm-20261030/synthesis.md` | `bb66ebed63f393e074a5e6e4295659631ef3f15e` |
