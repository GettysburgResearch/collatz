# Frozen dependencies and targeted literature check

## Repository sources

All paths below are pinned to PR140 head
`6bee3183ff7f29f2e20ca88ab94bc7745c1af602`; their original review boundaries
remain in force. No old claim is promoted by being cited here.

| Source | Used here |
|---|---|
| `research/novel-swarm-20261030/pass3/PRESSURE_BRIDGE.md`, B1 | First-hit definition, simple-path reciprocal budget and uniform discount. Blob `2b4507c017df314997ebf7f8e3ec053e7b5388fe`. |
| `research/novel-swarm-20261030/pass3/ORDINARY_BOUNDARY.md`, Q2--Q4 | Component vectors, their positive masses, and eventual-periodicity equivalence. |
| `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-401/402 | Credited cylinder counting and optimized recursive exponent. Blob `16c943601ce791afb1bbd5f02f3a9ea88ef38520`. PF-001b explicitly adds finite-endpoint deletion, not a new entropy constant. |
| `research/astra-three-routes/pass3/FINITE_RECORDS.md`, T-A3-651 | Finite simple-path bound, reconstructed in B1. |
| `research/novel-swarm-20261030/pass2/INVERSE_PRESSURE.md`, P1--P2 | All-history versus first-hit pressure and exact cycle repetitions. |
| `research/novel-swarm-20261030/CONCENTRATION.md`, E5 | Open fixed-source occupation target; no pressure-to-E5 implication is imported. |
| `research/integrated/ERRATA.md` | Distinct values versus repeated cycles; orbit counts cannot be transferred to predecessor basins. |

PR142's fixed-depth inverse-density discussion already distinguishes positive
ordinary targets from the negative reference spike. PF-003 makes a particular
all-modulus power-supersolution obstruction explicit using positive shadows;
it does not claim discovery of the negative spike or the all-one family.

## External sources inspected on 2026-10-31

Mikhail Neklyudov, *Functional analysis approach to the Collatz conjecture*,
arXiv:2106.11859 (2021), introduction and Sections 2/4:
https://arxiv.org/abs/2106.11859

This is prior context for operator/fixed-space formulations. Its unweighted
operators and function spaces are DIFFERENT from PF-002. In particular its
Hardy-space fixed-point assertion is not applied to the derivative-weighted
ordinary operator here. No theorem from that paper is a dependency, and no
exhaustive priority audit has been performed.

The ProofAtlas interface for Lech Mazur's *Positive Lower Density of Collatz
Predecessors*, manuscript v1.0, was also inspected:
https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

It advertises target-dependent positive lower predecessor density and a
conditional density-one convergence criterion, not unconditional density-one
convergence. No Lean build or manuscript-proof audit was performed here.
NONE of PF-001--008 uses that external density claim. The target-density
conclusion in PF-001 cannot be substituted for its starting-source premise.

The inherited orbit-packing account credits Garcia--Tal's 1999 orbit-sparsity
tradition. The proof used here is the pinned repository reconstruction above;
this session does not claim to have independently audited that entire paper.

## A related current finite-energy programme: source-qualified, not imported

Lucas Valbuena, `x1xhlol/collatz-two-coordinate-obstruction`, frozen at
`a7275d5a73814d3d9a400c6fe6577de9542b03a3`:
https://github.com/x1xhlol/collatz-two-coordinate-obstruction/tree/a7275d5a73814d3d9a400c6fe6577de9542b03a3

The root README and `formal-cylinder-energy/README.md` were read, the latter
at blob `22527f03e57e480f44f8b8c2f280ef10e28d51eb`. That bundle advertises
an equivalence between eventual periodicity and a sublinear finite masked
cylinder energy. It retains an open small-ancestor contribution and permits
nontrivial positive cycles. This is relevant prior context for finite-energy
criteria, not an established input to the present proofs.

Its quantity uses `h_K(N)=canonicalRho K N/N`, an odd finite target head and
a no-return mask. The root README also reports a quadratic Haar L2 bound for
the ORIGINAL geometric Syracuse law. Our Z_q instead weights histories by
the SQUARE of the affine derivative; our S_q is an unmasked positive-integer
trace. Those objects are different. No claimed external quadratic estimate
is transferred to (M). The advertised Lean build records were not replayed,
and the full manuscripts/proofs were not independently audited here.

PF-006--008 are proved from the pinned repository inputs and elementary
Hilbert-space and summability arguments. No external energy theorem is a
dependency. This targeted comparison is not an exhaustive novelty audit.
