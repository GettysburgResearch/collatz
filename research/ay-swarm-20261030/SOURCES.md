# Sources, frozen context, and novelty limits

## External mathematical source

Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule,
**An Automated Approach to the Collatz Conjecture**, *Journal of Automated
Reasoning* 67, article 15 (2023),
[DOI 10.1007/s10817-022-09658-8](https://doi.org/10.1007/s10817-022-09658-8).
The full text inspected for this pass is
[arXiv:2105.14697v3](https://arxiv.org/html/2105.14697v3).

The relevant parts are Section 3.2 (the exact mixed-base system, canonical
word reduction, and Collatz equivalence), Section 4.3 (termination of all
eleven one-rule deletions), and Example 4.3 (the particular natural matrix
certificate analyzed in `srs-semantics.md`). The mathematical definitions
and displayed certificate were inspected directly; the existing upstream SAT
searches were not rerun. The old CMU paper URL currently redirects to the
author's homepage, so the versioned arXiv text is used here.

| Object | Frozen identity |
|---|---|
| [Upstream repository](https://github.com/emreyolcu/rewriting-collatz/tree/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340) | `8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340` |
| [`rules/collatz-T.srs`](https://github.com/emreyolcu/rewriting-collatz/blob/8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340/rules/collatz-T.srs) | Git blob `789362dc9f9e0546fbb8f19c90fbf7554fce725a` |
| Upstream README | Git blob `c8e6c9d9765041d3e9184fbfdbc0d38b555439c7` |

No assertion that a previously open deletion subsystem has now been solved
is made: all eleven deletion terminations are prior published results. The
new work here is the explicit alternative ranks, exact budgets and guards,
the concrete quotient/search interface, and the stated method obstructions.
General results about nonoverlapping rewriting, finite fibres, and scalar
dynamic programming are elementary specializations, not priority claims.
This was not an exhaustive literature-priority audit.

## Project context actually inspected

The base commit is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, with tree
`1c25c17df24491de6187445f1a1d355d5a7660c3` and 315 tracked files. The complete
source tree and original signed commit object were reconstructed from the
GitHub connector after ordinary Git networking failed. Every source blob and
the complete tree matched the upstream Git identities. The standard clean
checkout validator then passed. This is actual complete-checkout validation,
not an API-tree inspection relabeled as execution.

The entrypoint, README, research map, results catalogue, resident errata,
finite-safety packet, completion-ghost packet, and open obligations were read.
The earlier AYH port was inspected at
[PR #6](https://github.com/GettysburgResearch/collatz/pull/6), head
`4810a0771da61a1cb609ef8707dfcf7f0f6e666f`, including
`research/termination-frontier/README.md` and `CLAIM_INVENTORY.md`.
That source contains the exact rule port, the standard match-height
obstruction, and quarantined earlier leads. Its unavailable legacy theorems
are not dependencies of the present proofs.

Recent PR metadata and descriptions were checked to orient this pass:

| PR | Observed head | Subject |
|---:|---|---|
| [139](https://github.com/GettysburgResearch/collatz/pull/139) | `c0e51c5bd90eb16fdf1caa294b6b74e972c58d1a` | Fixed-source ternary splices and H restart budget |
| [138](https://github.com/GettysburgResearch/collatz/pull/138) | `a3f006a1281939156b2068c5be5248bcf3c61dd1` | Anchored capacities and dyadic completion |
| [137](https://github.com/GettysburgResearch/collatz/pull/137) | `2911b53930cbd31f623d3e0586ca3613854f0143` | Component rigidity |
| [136](https://github.com/GettysburgResearch/collatz/pull/136) | `fc55ecf265f23b263983fb7eebd95a4c4b0f0787` | Escape restarts |
| [135](https://github.com/GettysburgResearch/collatz/pull/135) | `40c59116ba9a3f94565d9782e4ffe3c97cc0ce71` | Fixed-source splicing |

This is not a review of all files in those PRs, and none of their proposed
universal conclusions is assumed. In particular the present rank `H(s)` is
an administrative string potential, **not** the arithmetic H-system or the
restart rank in another programme. The overloaded letter is resolved by its
argument and definition, not by an implicit transfer theorem.

## Evidence classification

All new mathematical statements remain **PROPOSED at project level**.
The in-session agents reconstructed one another's arguments at the file
identities recorded in the [review](../../reports/ay-swarm-20261030/REVIEW.md).
That is useful independent reasoning within this pass, not external peer
review, a formal proof assistant build, or canonical acceptance. Executable
checks establish only their documented finite scopes. Neither the positive
partial ranks nor the negative order results imply a complete Collatz proof.
