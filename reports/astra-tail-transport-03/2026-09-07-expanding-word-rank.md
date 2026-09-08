# Third tail-transport continuation: all-word rank and failed activation

Date: 2026-09-07. Author: `astra-tail-transport-03`.
Research parent: `73572fddd9b8b3cbd8fc03c3a992eb0735d0f62c`, PR105.
Main observed: `ba93d8def5e2b19b4c463485b4a9b1902127db9f`.

**PROPOSED pending independent mathematical review. No end-to-end Collatz
proof was obtained.** This is a new research packet, not a further Reviewer D
review or a silent change to a previously accepted result.

## Goal, attempted mechanism, and result

The task was to force the positive all-future residual from the second packet
to vanish. Rather than perform a larger clearance computation, this pass
attempted a complete arithmetic certificate rule: include every sufficiently
expanding physical parity pattern in one rank, then activate a minimizing
pattern to obtain a strict same-rank decrease.

The rank is computable and proper despite its infinite dictionary. Its
reciprocal is summable by an explicit word-entropy argument. A precisely
guarded family of unbounded old unsafe phases has a provably unique global
minimizer at every phase, and the NEW rank contracts step by step even while
the OLD rank grows. This proves a genuine comparison with a previous obstruction.

However, the universal activation step is false. An explicit exit from those
same phases has an illegal minimizing word and an unbounded rank increase.
Arbitrary fixed forward lookahead also fails. These are all-parameter ordinary
families, not extrapolations from bounded searches. The final global selector
remains open, not merely unreviewed.

## Exact new scope

ATT-201: `rho` includes all words satisfying `4*3^q>=5*2^L`, plus three base
forms; `n-1<=rho<=R_*<=n^2`. For candidate M only lengths `n*2^L<4M` matter.

ATT-202: `N_rho(X)<250X^(39/40)`, `sum 1/rho<=10000`, `sum 1/rho^2<2`.
The proved exponent is not sharp. It supplies no transported-input invariant.

ATT-203: any physically legal minimizing component provides a finite common-rank
certificate. Every tie is tested; the algorithm can return UNRESOLVED.

ATT-204: the six rotations of `111010` become unique global minimizers under
explicit source-precision guards. For all eligible K,e,

    n=(3^e*64^K-73)/17 -> s=(3^(e+4K)-73)/17,
    rho(s)/rho(n)=(81/4096)^K.

All 2K old A-source positions are quarter-unsafe. The old phase was already
known; the global all-word minimum and new stepwise rank identities are the
proposed additional results.

ATT-205: for `h=5 mod16`, h>=21, `s=(3^h-73)/17` is even and

    rho(s/2)/rho(s)>=2^h/4352.

Its unique minimizing word begins with 1 and is illegal. This refutes the
specific attempted completion.

ATT-206: for every finite K, ordinary positive multiples of three have all
first K successor ranks greater than 16 times the initial rho. Their inverse
ancestors alone also never reduce rho. No all-diagram clock bound or single
all-time ordinary shadow is asserted.

## Evidence and review handoff

[Manuscript](../../research/astra-tail-transport/expanding-word-rank/PROOF.md)
contains every proof and the exact failed step.
[Experiment](../../experiments/X-ATT-003-expanding-word-rank/README.md)
gives reproducible commands and evidence tiers.

The generator and the separately structured verifier reconstruct the same
complete finite payload. Normal and optimized verification reject 12 distinct
resealed semantic corruptions. The source census has 4,095 cases and 1,639
local certificates; 2,456 remain unresolved under the tested rule. There are
24 high-precision family sources, 672 physical positions, 60 exhaustively
minimized family positions and 36 fixed-forward-clock controls.

Semantic digest:

    4b4ff957e4c782695a07f3127c52c5d12646f9077c3000748ff683da94886d9a

Both programs have the same author and supply no independent mathematical
peer-review verdict. Large cases check exact hypotheses of the all-word
comparison theorem rather than enumerate an enormous dictionary. Fresh-directory
replay and Git blob comparison bind publication to tested files.

The new commit adds eight files only. Earlier proofs, evidence, review reports,
canonical statuses and workflows remain unchanged. Direct Git access failed
DNS and no authenticated complete checkout was available; no repository-wide
validator run is claimed. GitHub API publication is separately confirmed by
the remote PR/head receipt. External abstract-level browsing informed exploration
but supplied no theorem premise or comprehensive priority certification.

## What independent review should decide

Review finite minimization, the entropy/sublevel sum, the physical certificate,
the global-minimum lemma's zero-cross-constant case, and both exit/delay bounds.
Keep the valid construction separate from the false universal activation claim.
A complete residual merging selector or an actual invariant-mass estimate for
this new rank still needs proof. The old fixed input's positive mass remainder
cannot be reassigned to the new weight `1/rho^2`.
