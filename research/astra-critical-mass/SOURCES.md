# Sources, provenance, and trust boundary

## Frozen repository inputs

Canonical repository: GettysburgResearch/collatz.

- main: `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
- PR #87: `e9adc409031a61f3801c4ee1e1e6deeb34188eb7`.
- PR #88: `c28922fb6d1c070bf86a76192f40bc9ea3edd67c`.

Read for the scientific interface:

- [AGENTS.md at frozen main](https://github.com/GettysburgResearch/collatz/blob/9704bcf1ff33cc9e2b729e0c40137a1e55b95397/AGENTS.md).
- [Research map](https://github.com/GettysburgResearch/collatz/blob/9704bcf1ff33cc9e2b729e0c40137a1e55b95397/docs/RESEARCH_MAP.md).
- [Resident coefficient-stopping packet](https://github.com/GettysburgResearch/collatz/blob/9704bcf1ff33cc9e2b729e0c40137a1e55b95397/research/integrated/coefficient-stopping/README.md).
- [PR #87 fixed-height attack](https://github.com/GettysburgResearch/collatz/blob/e9adc409031a61f3801c4ee1e1e6deeb34188eb7/research/external/mazur-2026/fixed-height-power-saving-attack.md).
- [PR #87 predecessor digest](https://github.com/GettysburgResearch/collatz/blob/e9adc409031a61f3801c4ee1e1e6deeb34188eb7/research/external/mazur-2026/predecessor-x090.md).
- [PR #88 actual mathematical file](https://github.com/GettysburgResearch/collatz/blob/c28922fb6d1c070bf86a76192f40bc9ea3edd67c/research/external/mazur-2026/fixed-height-forward-power-saving.md).

The PR #88 description advertises other paths and T-FHP identifiers that were
not the actual retrieved mathematical file. This packet uses the concrete
MZ-FH file above, not those advertised paths. It does not alter PR #88.
PR #88 already establishes the all-subset mass-conservation obstruction;
that observation is credited rather than claimed as a new Astra result.

## External predecessor input: source-qualified only

Lech Mazur, *Certified x^0.90 Lower Bounds for Collatz Predecessor Sets*,
version 2, 17 July 2026, source release 1.0.0.

- [Published theorem surface](https://www.proofatlas.ai/collatz-predecessor-090/).
- [Source index](https://www.proofatlas.ai/sources/collatz-predecessor-090/).
- Published checked-source commit: `5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f`.
- Exact declaration: `predecessor_count_lower_bound_0901`.

The displayed declaration supplies a positive target-dependent constant for
the eventual lower bound c_b X^(901/1000), for every fixed positive target not
divisible by 3, using the one-division shortcut map. This is the only external
mathematical input used by T-ASTRA-001's Collatz implication.

The public theorem and source pages were rechecked in this session. The full
Lean import closure and the large coefficient/potential payloads were **not**
rebuilt or replayed. The release discloses two generated native_decide
computation assertions, in addition to standard logical axioms. No assertion
of kernel-only replay or independent verification is made here. No PDF is
redistributed or newly claimed to have been audited in this session.

## Other literature and novelty

The predecessor import and the first-passage program are related to the broader
stopping-time and transport literature. The primary-source abstract of
[Tao, arXiv:1909.03562](https://arxiv.org/abs/1909.03562) was consulted as
background, not used as a proof dependency. No logarithmic-density theorem
is silently promoted to a fixed-height or all-source conclusion.

The new elementary arguments were reconstructed in this session. A broad
literature-priority search was not completed. The claims are contributions
to the repository's explicit proof graph, not declarations of external priority.

## New local dependencies

PROOF.md -> elementary arithmetic, finite affine composition, nonnegative
summation, geometric series, and the proofs contained in that same file.
T-ASTRA-001's final implication additionally uses the source-qualified P(gamma).
FIRST_PASSAGE.md proves its finite parity-cylinder interface directly.
The experiment uses only Python's standard library.

Two separately written implementations were executed locally. Their agreement
is a computational cross-check, not a second independent author or a formal
mathematical verification. All new theorem statuses remain PROPOSED.
