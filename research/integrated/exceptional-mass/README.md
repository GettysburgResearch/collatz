# Exceptional mass and fixed-height descent

This guide connects the project's counting and operator results without asserting a new accepted synthesis. Use the shortcut map `T(n)=n/2` for even n and `(3n+1)/2` for odd n. Other maps and clocks are explicit in the cited source statements. [Scientific status](../../../STATE.md) · [Cumulative results](../../RESULTS_CATALOG.md).

## What is established

For integer `X>=2`, define

$$
N(X)=\{1\le n\le X:T^k(n)\ge n\text{ for }0\le k\le\lfloor\log_2X\rfloor\}.
$$

The reviewed native theorem is `#N(X)<=6499+2X^(19/20)`. At dyadic scale, no-descent roots have exact exponential rate `h_2(log 2/log 3)`, where `h_2` is binary entropy. The proof counts parity cylinders using a binomial tail; a rotation argument supplies the matching entropy lower rate. [Exact statements and proofs, MZ-FH-001–004](../../external/mazur-2026/fixed-height-forward-power-saving.md).

This is failure to descend below the **starting value**, not failure to reach a fixed floor. Global minima, coefficient-supercritical roots, all survivor starts and their predecessor basins are different populations. Repeated generic pullback loses a fixed power saving; a positive gain uniform over **every** endpoint subset is impossible by mass conservation.

The [critical-mass proof](../../astra-critical-mass/PROOF.md) supplies conditional exponent/critical-endpoint and killed-weight criteria. The [first-passage proof](../../astra-critical-mass/FIRST_PASSAGE.md) retains exact arithmetic-progression integrality, every survival prefix and its endpoint interval. [Mellin identities](../../astra-three-routes/ROUTE1_MELLIN.md) and [ordinary boundary charge](../../astra-three-routes/pass3/BOUNDARY_CHARGE.md) retain actual sources, killed states and finite-horizon/transport assumptions. The independently supported `8.6140<G_256<8.9619` enclosure is finite-time evidence, not a bound uniform over all horizons.

## A failed uniform residue-share bound

For the fixed floor `H=64`, let `chi_k(n)` indicate that `T^j(n)>64` for every `0<=j<=k`. At Mellin exponent `s=3/2`, put `M_k=sum_n chi_k(n)n^(-3/2)` and `Q_k=sum_{y>=98, y=2 mod 3} chi_k(y)y^(-3/2)`. The endpoint cutoff is part of the killed odd-predecessor condition and must not be dropped.

The proposed ceiling **`Q_k<=M_k/3` for all k is refuted**: at `k=19`, a complete inverse cone and directed rational tail bounds give `3Q_19>M_19`. This is an actual finite-time survivor-population counterexample, not evidence of a divergent orbit. It was independently reconstructed; the larger depth-36/40 numerical protocols do not inherit that replay. [Definitions, exact certificate construction and counterexample](../../astra-three-routes/ROUTE1_MELLIN.md).

This failure does not rule out all aggregate contraction. The same source's sufficient eventual bound `Q_k<=(69/200)M_k` remains an **open hypothesis**, not a replacement result already established.

## The fixed-floor route remains conditional

A survivor-count estimate can contradict a predecessor lower bound only for **actual eternal survivors above one certified floor** and an eligible fixed target. The [external dossier](../../external/mazur-2026/README.md) remains source-qualified: the stronger predecessor exponent is `c_b X^0.901` with positive target-dependent `c_b` and cutoff; the unit-coefficient endpoint is `0.90`. Its fixed-floor forward-density result still has counting exponent one. No complete local Lean or large external-payload replay is implied.

A strictly positive summable killed-state weight satisfying the stated pointwise strict supersolution criterion would supply another route; no global such weight is constructed. Neither weighted equidistribution in the centered system nor a finite inverse cone supplies the missing survivor estimate by itself.

## Source tails and clearance

For the moving rank R_*, put `w(n)=1/R_*(n)^2` on n>=2. [ATT-001–006](../../astra-tail-transport/PROOF.md) establish the sharp ordinary-source tail `1/(9N^2)<=sum_(n>N)w(n)<=43/N^2`. At each fixed positive raw shortcut clock k, the transported endpoint-rank tail is `Theta_k(1/Y)`: fractional moments below one are finite, while the first moment is infinite. The weak-first constant grows at rate `(9/4)^k`; that is not a uniform-in-time tightness bound. ATT-006 separately identifies divergent-basin escape mass and nontrivial-cycle occupation mass. Both must vanish. Its optional SC* interpretation also uses the existing [actual-tail theorem](../../astra-three-routes/pass2/SC_TAIL_AND_ECHO.md), not just a change of notation.

The [clearance proof](../../astra-tail-transport/repeated-spikes/PROOF.md), ATT-101–105, keeps the **fixed initial** input `w_U=1_U/R_*^2`. Here U is the quarter-unsafe set for maximal repeated-word acceleration A, and H pushes mass through one actual unsafe return, killed at 1. Complete initial rank balls and a finite forward-closed clearance forest yield

$$
\|H^j w_U\|_1\le 12/2^{48}\qquad\text{for every }j\ge52.
$$

The finite part includes 163,168 non-core rank-ball sources at `Y=2^32`, 78,828 unsafe roots and 111,763 forest vertices, including 32,935 outside the starting ball. Their largest hitting times are 52 unsafe returns and 261 raw shortcut steps. The unknown initial rank tail is bounded once by `12Y^(-3/2)`; deterministic killed transport cannot increase its unweighted mass. The same input has the corresponding bound at every raw time k>=261. This does **not** equate the two clocks.

These counts were independently reconstructed in the [source review](../../../reports/post-integration-2026-09-08/README.md); [native certificate and replay contract](../../../experiments/X-ATT-002-repeated-spikes/README.md). The result is a genuine all-future bound with a **positive** residual, not an extrapolated finite-time trend, natural density, a percentage solved, or a vanishing theorem. The finite Green enclosure above remains a different result.

Every finite power of H still has unweighted l1 operator norm one, so the displayed small fixed-input bound cannot be multiplied at successive blocks. A proved cofinal family of clearances, or another argument forcing the residual to zero, remains missing. Changing from R_* to rho or Gamma changes the weight and generally the return operator; the numerical bound does not transfer. [Current import and replay record](../../../reports/integration-2026-09-08/README.md).

## Current timed bootstrap

**Proposed corrected formulation, pending review of this exact presentation.** This collects the existing killed-transfer criterion and its positive-beta restriction; it does not claim a new accepted theorem or verify the missing premise.

Fix a floor H, constants `0<r<1`, `D>0`, `delta>0`, `c>0`, and a sufficiently large finite base scale `X_H`. For every sufficiently large integer X, suppose a partial map `F_X` is defined on `[1,X]` outside `E_X` and satisfies

$$
F_X(n)=T^{t_X(n)}(n),\quad 0\le t_X(n)\le c\log X,
\quad 1\le F_X(n)\le\lfloor X^r\rfloor,\quad
\#E_X\le KX^{1-D},
$$

with K independent of X. Define `L_H(X)=0` for `X<=X_H`, and otherwise

$$
L_H(X)=\lceil c\log X\rceil+L_H(\lfloor X^r\rfloor),\qquad
S_H(X)=\{1\le n\le X:T^j(n)>H\ (0\le j\le L_H(X))\}.
$$

Require **survivor-specific pullback**, for a constant `K_H` independent of X:

$$
\#\{n\le X:n\notin E_X,\ F_X(n)\in S_H(\lfloor X^r\rfloor)\}
\le K_H X^{1-r-\delta}\#S_H(\lfloor X^r\rfloor).
$$

For

$$
\beta>\max\{0,\,1-D,\,1-\delta/(1-r)\},
$$

the proposed conclusion is `#S_H(X)=O_H(X^beta)`. Moreover, for any fixed `C>c/(1-r)`, the starts `n<=X` staying above H for every integer `0<=j<=C log n` have the same upper bound.

**Proof route.** Split survivors into `E_X` and the pullback to the smaller survivor set. The two resulting exponent gaps are positive, closing strong induction after enlarging the constant over the finite base range. The recursive clock is at most `c log X/(1-r)+O_H(log log X)`; dyadic shelling gives the source-dependent clock bound. **Beta must be positive** for that shell sum. The unrestricted nonpositive timed endpoint is not accepted. [Original criterion and proof, section 7](../../external/mazur-2026/fixed-height-forward-power-saving.md#7-exact-sufficient-criterion-killed-set-decorrelation) · [Correction provenance](../ERRATA.md#e-integration-001--positive-beta-timed-bootstrap).

No physical descent family with the required reusable gain is supplied. The native no-descent theorem gives descent below n, not automatically below `X^r`. Crossing the external `0.901` exponent remains conditional on the full predecessor/fixed-floor hypotheses, not merely on numerical parameter choices.

## Evidence and next task

[Nonmutating fixed-height replay](../../external/mazur-2026/check_fixed_height_forward.py) checks its declared finite arithmetic; it does not prove the asymptotic analysis or survivor-specific premise. Other finite mass/source-tail certificates retain their individual replay limits. [Evidence instructions](../../../docs/REPLAY_POLICY.md).

The next task is [a survivor-specific gain or actual fixed-floor estimate](../../open-obligations/README.md#survivor-specific-transfer). It must survive repeated transport; a floor increasing with time is not one fixed floor.

<details><summary>Exact clause-level review and source identities</summary>

[Counting/critical-mass review](../../../reports/prepublic-2026-09-05/reviewer-a/CLAIM_MATRIX.md), especially RA-010–031 and RA-076; [Mellin/boundary review](../../../reports/prepublic-2026-09-05/reviewer-b/CLAIM_MATRIX.md). Exact source/review commits and evidence residency are in [the integration record](../../../claims/reviewed-2026-09-05.json). Complete historical encoded corpora and external payloads not replayed retain that limit. The proposed presentation above is not covered by a new independent review.

</details>
