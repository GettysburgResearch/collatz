# Source, review, and execution record

This record supports the [research packet](../../research/beeping-density-swarm-20261030/README.md)
dated 2026-10-30. It does not promote the packet into the accepted baseline.
Collatz remains unresolved. The proposed local theorems have written proofs,
scoped reconstruction, and bounded implementation checks. No proof assistant
certification or outside mathematical acceptance of this packet is claimed.

## Repository and comparison scope

The research branch starts from main at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, whose tree is
`1c25c17df24491de6187445f1a1d355d5a7660c3`.
The entry instructions, scientific map, integrated index and scoped errata
were read. Relevant later source packets were inspected at the following
frozen revisions. This was a targeted dependency and duplication check, not
an exhaustive new review of every historical PR.

| Source | Frozen revision | Material used or compared |
|---|---|---|
| [PR106](https://github.com/GettysburgResearch/collatz/pull/106) | `7b7471ea0e7b359a2ac46fb1e6aff269331509c3` | Actual-prefix Gamma, its finite evaluator and periodic selection, and one-step spikes, under `research/astra-linear-frontier/prefix-rank/`. Gamma is inherited, not claimed new. |
| [PR134](https://github.com/GettysburgResearch/collatz/pull/134) | `025f2683c19bfedc3eeff0303206b20c889c8005` | `research/paired-comparison/endpoint-transplant/PROOF.md`: thick basins, finite pattern transfer, and root-capped inverses. This is distinct from an analytic positive-density theorem. |
| [PR137](https://github.com/GettysburgResearch/collatz/pull/137) | `2911b53930cbd31f623d3e0586ca3613854f0143` | `research/component-rigidity/pass1/PROOF.md` and `pass2/PROOF.md`: invariant components, relative windows, finite-boundary obstruction and variation target. |
| [PR139](https://github.com/GettysburgResearch/collatz/pull/139) | `c0e51c5bd90eb16fdf1caa294b6b74e972c58d1a` | Source-budget ternary splice and restart-budget notes; fixed positive sources must remain distinct from completion witnesses. |

The additions are isolated under `research/`, `experiments/`, and `reports/`,
with one navigation row in `research/README.md`. They do not modify the
accepted theorem catalog, old frozen proofs, old evidence, workflows, or
other contributors' branches.

## External sources and evidence ceilings

| Source | Identity and reading scope | Qualification |
|---|---|---|
| [Mazur fast positive-density paper](https://proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf) | Supplied v2.1 paper and source/formalization pages; reported source pin `830b9d3f38f2a8da8cd921bf6a9310dd69336fd0`. | The fast positive-density statement is an external premise of the soft-clock criterion. Current v003 build evidence is source-reported, with accepted-result publication pending. No local Lean rebuild was executed. |
| [Positive-density predecessor paper](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) | Paper and formalization page; reported assembled pin `c290ac229b379d2b51026d3e86140496870d6f39`. | Positive density for each admissible target remains source-qualified here. Reported formalization status is not a new local replay. |
| [Lau target-dependent theorem](https://hexagonmath.org/2610.00249v2) | Hexagon v2, including theorem and inverse-law/census sections of the 71-page PDF. The identifier is a Hexagon identifier, not an arXiv identifier. | The stated coefficient is proportional to `t^(-25/11)` with an explicit very small absolute constant. We did not independently replay the analytic proof or its formalization. |
| [Mira's beeping machine](https://github.com/Mira-Cult/math/blob/c465130c54f992c5cf0e5c93c752a79c2e0a7398/turing-machines/collatz-beeping17/README.md) | Commit `c465130c54f992c5cf0e5c93c752a79c2e0a7398`; README blob `f72177efd330776e41b63e98297c25565b813691`. The literal table and complete canonical invariant were reconstructed. | The equivalence is supported here by a written all-parameter macro argument and a separately written bounded literal interpreter. No Lean proof is claimed. |
| [OpenAI single-fold manuscript](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae/preprints/Single-fold-Diophantine-representations-September-24-2026) | Commit `4eaee87548250b2682affda7d05d947c05554bae`; main theorem, consequences, and rank-one proof files inspected. The full manuscript was not independently verified. | The finite/infinite polynomial corollary is explicitly conditional on the asserted single-fold theorem. No numerical polynomial coefficients are supplied. Machine, density-spike, and rank results do not depend on it. |
| [Yolcu--Aaronson--Heule implementation](https://github.com/emreyolcu/rewriting-collatz/tree/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340) | Exact shortcut rewrite system checked against the authors' repository and theorem 3.17 of their published paper. | Representation equivalence is not a new termination proof. |
| Nashida barrier preprints | `harappa/collatz-termination-certificate-dichotomy` at `a138adb7c7efaec8addd06722f40f015c7f2d9be`; `harappa/collatz-matrix-interpretation-barriers` at `8e7d6da6319c1c1b36ce3549fe06e00d0586a025`. | The general barriers remain source-qualified, not independently formalized or accepted here. The separately replayed author checker covers 22 finite witness rows only. Exact blobs and scope are in the [source note](../../research/beeping-density-swarm-20261030/YAH_AND_NASHIDA_SOURCES.md). |

The root also opened the supplied PDF directly. No third-party PDF, Lean
development, or upstream source tree is redistributed in this packet.

## Independent reconstruction and final corrections

The density, rank, and machine tracks had distinct agent owners. Root
developed the near-invariance obstruction and synthesized the packet. A
different agent reconstructed the density and rank arguments rather than
merely approving their summaries. This is internal mathematical review in
the same research session, not independent external peer review.

| Review | Explicit scope |
|---|---|
| [REGULARITY_REVIEW.md](../../research/beeping-density-swarm-20261030/REGULARITY_REVIEW.md) | DREG-001--007, norm completion and parity ergodicity, computable-real versus exact-output distinction, conditional variance, majority examples, and slow oscillation. The external density theorems remain premises. |
| [NEGATIVE_SPIKE_REVIEW.md](../../research/beeping-density-swarm-20261030/NEGATIVE_SPIKE_REVIEW.md) | DSP-001--005, clipping and critical strong-moment obstruction, initial-run cap, positive fixed-target bound, resolvent distinction, and fixed-cutoff mask lemma. No bound uniform over moving positive endpoints is inferred. |
| [RANK_ENVELOPE_REVIEW.md](../../research/beeping-density-swarm-20261030/RANK_ENVELOPE_REVIEW.md) | ORD-001--005, finite evaluation and moment spaces, contact hitting, critical rational envelope, complete inverse fans, Fibonacci node bound, and the exact rows at 26 and 44. |
| Machine and synthesis audit | Root checked the canonical macros, clock algebra and quantifiers; the literal simulator is separately written. Final audit corrected “at or beyond the original hole” to “strictly beyond,” restricted finite clock prefixes to arithmetic segments before the first hit of one, and made the current terminal-set qualification explicit. |

For each fixed `p>0`, the rank packet now includes the explicit mass on
`3^h` witnessing strict inclusion of the Phi-moment space in the Gamma-moment
space. The final audit supplied and checked that witness. Document relocation
also changed executable links and commands. The final exact file identities
are recorded in [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json); older draft
hashes mentioned within a review remain historical identities, not hashes of
the relocated final files.

## Actual execution

After copying the final programs and saved payloads into the publication
directories, the following command was executed from the complete repository:

```bash
python -X utf8 -B experiments/beeping-density-swarm-20261030/replay_packet.py --output /tmp/collatz_beeping_packet_replay.json
```

It exited zero and reported **PASS: six suites, 12 subprocesses, complete
saved-JSON equality in normal and optimized modes**. The run used Python
3.12.14 on Linux. The unmodified aggregate result is
[packet_replay.json](packet_replay.json). Coverage, individual commands, and
per-suite evidence are listed in the [experiment README](../../experiments/beeping-density-swarm-20261030/README.md).
Checks were not broadened into large historical searches or external builds.

The complete-checkout structural gate is run after the final content has
been committed, using `python -X utf8 -B tools/validate.py` with its receipt
outside the checkout. Its actual commit/tree identity and result belong in
the publication PR so that recording the result does not change the validated
tree. This paragraph is an execution protocol, not a claim that a pre-commit
or partial-tree check passed. A passing structural gate does not establish
any mathematical theorem.

## Remaining research obligations

The full-proof routes remain blocked at explicit mathematical steps:

1. Mean concentration/dyadic regularity for the actual soft stopping clock.
2. A strictly positive summable inverse supersolution or a total physical
   lower-rank merger for the induced contact process, with the terminal set
   and source domain fixed.
3. A uniform or summable positive-source inverse budget that survives the
   actual changing endpoints under transport.

The packet does not replace any of these with finite computation,
nonconstructive completion witnesses, or unproved typicality assumptions.
