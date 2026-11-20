# Frozen sources and the latest-source comparison

The base is `main` at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, tree
`1c25c17df24491de6187445f1a1d355d5a7660c3`. This packet is an additive
research branch. Source inspection and internal mathematical review are
scoped to the paths and claims below, not every statement on a PR.

The pass began with PR146 at `fd991063...`. A second live refresh found
its `66970775...` update and PRs167–169. The actual Git objects were
fetched and inspected before this packet was frozen. The two PR146
heads differ by the new every-class return note, its checker, and its
research guide link; the earlier sieve and Mellin sources are unchanged.

| Source | Exact head | Material used or compared |
| --- | --- | --- |
| PR146, initial snapshot | `fd991063721e9c157d318e40bb20131762f7d750` | `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`, `LEAST_FAILURE_SIEVE.md`, `BASIN_PHASE.md`; `research/astra-three-routes/pass2/ORBIT_MELLIN.md` |
| PR146, latest inspected update | `66970775e4bdc945a68308e37a8eb028ebde42d2` | `research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md`, especially Section1 root accessibility; `CRITICAL_INTERVALS.md`; comparison with `THREE_RAY_UPPER.md` |
| PR157 | `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`, GCM-002 physical-five closure criterion; `closing-attempts.md`, prior source-rank expansion boundary |
| PR163 | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | `research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md` and `FIVE_SLICE_ENERGY.md`: source-qualified height and energy interfaces |
| PR164 | `6fa6b429870a9cd53cde0fc77ad64a3c3956199f` | `research/witness-closure-512-2026-11-20/` continuation notes: domain and Mersenne-residual comparison |
| PR165 | `78bdb31ccba608de3d089b751a0ab59a52007408` | `research/certificate-transfer-intake-20261120/questions/02_weighted_representatives.txt`, prior arithmetic moment interface |
| PR166 | `5996b9f525ca50978bc34f423192c36a87765bf3` | `research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`, `LADDER_RENEWAL.md`: imported A-ladders and their exact fibers |
| PR167 | `e83cc8b35ad614c616df7c00318cc9645a174c34` | `research/least-failure-closure-20261121/DENSITY_CONGESTION.md`, DC1–DC3; `HOMOGENEOUS_FIVE_TRANSPORT.md`, `EXPANDED_FIVE_RENEWAL.md`, `CLOSING_ENERGY_INTERFACES.md`; arithmetic/periodic-scope comparison |
| PR168 | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | `research/closure-frontier-20261121/FIVE_RETURN_LANGUAGE.md`, `CLOSING_ATTEMPTS.md`: larger balanced grammar, residue-coupled renewal, first unsupported steps |
| PR169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | `research/certificate-renewal-20261121/FIVE_WORD_EXTENSION.md`, `MOMENT_QUANTILES.md`, `FIXED_ENDPOINT_SUMMABILITY.md`, `FULL_THEOREM_ATTEMPT.md` |

## Attribution and dependency distinctions

The finite-core Foster theorem is proved in full here. Root accessibility
is imported from the newly inspected PR146 Section1 and independently
reconstructed in the companion proof/checker. The null-return-time and
strict ordinary-descent consequences combine those inputs with explicitly
stated elementary probability arguments. The inverse-fiber pressure
conclusion uses PR167's averaging identity with its original unit guards.

The valuation-one block `(1,1,1,b)` and larger balanced languages already
appear in PRs167–169. This packet's two-residue renewal proof is a
simplification on a smaller domain, not an improvement over their
coverage or their best coefficient. The separate
[latest-source delta](LATEST_SOURCE_DELTA.md) records the exact overlap.

The linear-horizon and finite-simple-prefix applications import the
existing directed reduction and its factor `176106`. Their checkers
replay the new arithmetic and actual finite trajectories; they do not
reverify the entire 71-path cover. The finite-simple-prefix proof
reconstructs the relevant two-lane counting argument rather than
assuming an infinite-orbit estimate applies automatically to a prefix.

No GRH result or announcement is an input to the new theorems. Published
theorems used by older global rigidity interfaces keep their original
source-qualified status; this packet does not promote those interfaces
to a new independently verified universal proof.

Internal AI-agent reconstructions identify their reviewed file hashes.
They do not constitute external peer acceptance, literature priority,
or formal proof-assistant verification.
