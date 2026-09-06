# Renewal and the transported distribution

Renewal organizes a trajectory into section returns or runs so that a useful part of its transfer operator can be controlled. The central remaining question is what happens to the **actual distribution after re-entry**. This guide states existing component results and their domains, not a new combined operator theorem.

## Section return and resonance

The section program uses `H={n>=4:n=1 mod 3}` and a total first positive-time return to `H union {1}`. Write that return as `F_H` and kill it at 1. Its complete inverse fan and reciprocal section-rank weight `V=1/P` give the stated bound `KV(y)<=Q(y)V(y)/2`. Nonresonant arrival halves P; the effective resonance-return resolvent acts on the dominated positive cone `0<=f<=CV`, retaining the endpoint charge `Q(y)`.

The conclusion is entrance into resonance **or 1**, not universal convergence. [Exact return, inverse fan, charge and operator definitions](../../astra-three-routes/ROUTE_1_TRANSFER.md). The companion [source-height proof](../../astra-three-routes/ROUTE_2_SOURCE_HEIGHT.md) gives actual no-descent pressure and conditional clock/jet consequences; a universal upper charge budget remains open.

## Two safe estimates, not one interchangeable safe set

For the moving rank `R_*` and its acceleration A, distinguish

$$
G_q=\{n\ge2:4R_*(A(n))\le R_*(n)\},\qquad
G_{\le}=\{n\ge2:R_*(A(n))\le R_*(n)\}.
$$

The rank, acceleration and value at 1 are defined in [conventions](../CONVENTIONS.md). With `K_XY=Pi_X K Pi_Y` (source Y, endpoint X) and `||f||_p=sum R_*(n)^p |f(n)|`, the **quarter-safe** theorem gives, for `p>0` and nonnegative finite-p-moment safe-entry input,

$$
\|K_{G_qG_q}f\|_p+\|K_{U_qG_q}f\|_p\le4^{-p}\|f\|_p.
$$

Here `U_q` is the surviving complement; an exit can reach it rather than 1. [Exact theorem and proof](../../astra-three-routes/pass5/RANK_MOMENTS.md).

The **enlarged-safe** theorem instead gives residence and mass-tail bounds with its specified envelope `f<=C/R_*^p` in the source's summable parameter range. Reuse requires re-establishing that envelope; it is not a distribution-free version of the quarter-safe result. [Exact domain, constants and proof](../../astra-three-routes/pass5-spectrum-switch/INDUCED_MASS.md).

## What averaging has and has not established

[Whole-run renewal](../../astra-critical-mass/RUN_RENEWAL.md) supplies complete coding, fresh-shell asymptotics and cofinal drift. [Corridor occupation](../../astra-three-routes/pass4/RENEWAL_MASS.md) controls its initial corridor, and repeated use needs its stated safe-entry envelope. These claims do not authorize replacing a transported distribution by a fresh one.

A reviewed unsafe-return construction takes a summable distribution with finite first rank moment to one with infinite first rank moment. This refutes the proposed invariant moment domain, not convergence of any individual source. Monomial and reciprocal-rank weight failures likewise delimit specific supersolutions. Source-charge controls also differ: a descending source is not a counterexample to a no-descent-only assertion.

## How this relates to the other programs

[Mass bounds](../exceptional-mass/README.md) would benefit from a valid retained-unsafe estimate. [Rank repayment](../rank-merging/README.md) may suggest amortization, but the section rank and moving rank are different functions and their clocks differ. Combining the programs needs a new proved interface; safe contraction and guarded repayment do not establish it by juxtaposition. The H-system and weighted-equidistribution results provide additional models, not an automatic transport theorem for this operator.

## Next contribution and evidence

[Target an invariant input class or reusable unsafe budget](../../open-obligations/README.md#unsafe-transport). State the map, killed states, projections, norm and re-entry hypothesis before proposing an estimate. Test it against the moment-explosion and fresh-versus-transported controls.

Finite replay checks formulas and declared finite coverage; it does not establish arbitrary re-entry. [Replay instructions](../../../docs/REPLAY_POLICY.md).

<details><summary>Exact component review and evidence limits</summary>

[Section/moving-rank claim review](../../../reports/prepublic-2026-09-05/reviewer-b/CLAIM_MATRIX.md) and [whole-run claim review](../../../reports/prepublic-2026-09-05/reviewer-a/CLAIM_MATRIX.md); [source/review identities](../../../claims/reviewed-2026-09-05.json). The section payload and both alternative final rank-packet payloads have recorded replays. Earlier protocols and complete encoded corpora retain their narrower inspection/reconstruction limits. These source verdicts do not constitute a review of a new synthesis.

</details>
