# Maps, ranks and operator conventions

This is a reference guide to the existing programs, not a theorem identifying their different state spaces or ranks. Read [scientific status](../../STATE.md) and the relevant [proof route](README.md) before transferring a result between programs.

## Maps and clocks

The shortcut map is `T(n)=n/2` for even n and `(3n+1)/2` for odd n. A shortcut step is not an odd-to-odd step, a whole odd/even run, a section return or a maximal repeated-word module. The external density dossier also uses a raw Collatz clock. Every theorem retains its specified clock.

The section-return program uses `H={n>=4:n=1 mod 3}`, excluding 1. Its first positive-time return is to `H union {1}`, killed at 1. Call it `F_H` here; the source calls it R. This H denotes a section, not the numerical floor in the fixed-height counting statements or every other H-named construction.

## Two distinct ranks

The section/global rank uses

$$
h(n)=v_3(2n+1),\qquad P(n)=\frac{(2n+1)^2}{3^{h(n)}}.
$$

Distinguish the section version from its global extension. The moving-envelope program instead uses, for `n>=2`,

$$
z_a(n)=3^a(n+1)-2^a(2n+1),\qquad
R_a(n)=\frac{z_a(n)^2}{3^{v_3(z_a(n))}},\qquad
R_*(n)=\min_{a\ge0}R_a(n),
$$

with `R_*(1)=0`. The source proves that the minimum reduces to `R_0,R_1,R_2,R_h` (the fourth is needed only for `h>=3`), and that `n-1<=R_*(n)<=n^2`. Its acceleration A consumes the maximal legal number of copies of the active word `1^a0`; it is not the older whole-run map. Neither rank is universally decreasing. Comparing their numerical values does not transfer a theorem between them. [Definitions and proof](../astra-three-routes/pass4/MOVING_GHOST_RANK.md).

In the six-branch representation chart, P and Q instead denote the constants `3^12` and `2^19`. In periodic-word formulas, L is block length and s is odd weight. Repeated letters across sources are not shared mathematical objects.

## Formal-word and actual-prefix ranks

The two ranks above remain in use. Two additional constructions have different candidate domains; they are not replacement names for R_* or P. For nonzero integers d, write `g(d)=d^2/3^v3(|d|)`.

| Rank | Candidates off 1 | Essential convention |
|---|---|---|
| rho | `g(n),g(n-1),g(n+5)` and `g((3^q-2^L)n+A_w)` for every word with `4*3^q>=5*2^L`. | Formal words, potentially physically illegal; fixed 5/4 gap and unreduced forms. Set rho(1)=0. |
| Gamma | `g(n)` and `4^k g(T^k(n)-n)` for every actual prefix with nonzero displacement. | Use raw T inside the definition, even after visiting 1; omit zero displacements. Set Gamma(1)=0 separately. |

[Rho statements](../astra-tail-transport/expanding-word-rank/PROOF.md) · [Gamma statements](../astra-linear-frontier/prefix-rank/PROOF.md). The proved `rho<=R_*` inequality does not establish an ordering with Gamma or transfer any older weight/transport theorem. ALF's P is unchanged with P(1)=3; its completed-section map is absorbed at 1, not made into a new zero-valued P rank.

## Operator domains

Use endpoint rows and source columns. For a deterministic map F killed at 1, `Kf(y)=sum_(F(x)=y) f(x)` on its surviving state space. Write `K_XY=Pi_X K Pi_Y`, extending inputs by zero outside Y. Nonnegative series are pointwise unless a norm-convergence statement is separately proved.

| Program | Region and entry hypothesis | Actual conclusion or limit |
|---|---|---|
| Section resonance | Nonresonant endpoints with the source's `Q(y)<=1`; dominated cone `0<=f<=C/P`. | Retain endpoint charge in the effective return. Exit is resonance or 1. |
| Quarter-safe moving rank | `G_q={n>=2:4R_*(A(n))<=R_*(n)}`; nonnegative finite p-th rank moment, `p>0`. | The combined surviving-safe/unsafe-exit p-moment contracts by `4^(-p)`. |
| Enlarged-safe moving rank | `G_le={n>=2:R_*(A(n))<=R_*(n)}`; source envelope `f<=C/R_*^p` in its stated summable range. | Polynomial residence/mass-tail bounds; the entry envelope must hold again on reuse. |

Here `||f||_p=sum R_*(n)^p |f(n)|`; each unsafe set is the complement of its own safe set among surviving states. The two complements differ. An infinite first rank moment is not infinite unweighted mass and not a divergent individual orbit. Fresh-shell drift need not hold for a transported ensemble. [Exact operator proofs](renewal-transport/README.md).

## Source measures and induced clocks

The tail/clearance papers use **only** the quarter-safe moving-rank region G_q. Their B takes one A step from its unsafe complement, then all successive G_q steps, ending at another unsafe state or 1. Their H is the killed pushforward for B, not the section H above. The clearance input is exactly `1_U/R_*^2`. Source-height tails, endpoint-rank tails, unweighted mass and summed occupation are different quantities; a positive fixed-input residual is not an l1 operator norm.

Gamma instead uses `G_Gamma={n>=2:Gamma(T(n))<Gamma(n)}`. Its safe operator is killed at **both** 1 and exit into the complement; reaching that complement is not convergence. Its subsequent unsafe return starts with a raw shortcut step and then a Gamma-safe excursion, not an old A module or B return. APR-009's moment explosion is a statement about the raw killed shortcut pushforward. It is not automatically an induced-return counterexample.

[Exact tail/clearance domains](../astra-tail-transport/PROOF.md) · [Gamma safe domains](../astra-linear-frontier/prefix-rank/PROOF.md) · [Exact component review](../../reports/post-integration-2026-09-08/CLAIM_MATRIX.md). New joint arguments still need their own review.

## Ordinary and finite scope

In orbit counting, an infinite orbit means an **infinite distinct value set**, not a cycle traced indefinitely. Finite CRT families can have a different ordinary source at each depth. Complete rank balls bound candidate witnesses, not clocks or intermediate peaks. A fixed-depth language or fixed-radius inverse frontier is not an all-time invariant object.

For current hypotheses and corrected clauses use [the results catalog](../RESULTS_CATALOG.md) and [current repaired statements](README.md#current-repaired-statements). Exact `(PR, commit, path, claim ID)` identities and collisions are in [aliases](../../claims/aliases.json); [the audit record](../../claims/reviewed-2026-09-05.json) preserves the component reviews. Source author-stage headers do not override a later scoped review, and a later review does not accept unrelated or changed source statements.
