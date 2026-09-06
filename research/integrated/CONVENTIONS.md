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

## Operator domains

Use endpoint rows and source columns. For a deterministic map F killed at 1, `Kf(y)=sum_(F(x)=y) f(x)` on its surviving state space. Write `K_XY=Pi_X K Pi_Y`, extending inputs by zero outside Y. Nonnegative series are pointwise unless a norm-convergence statement is separately proved.

| Program | Region and entry hypothesis | Actual conclusion or limit |
|---|---|---|
| Section resonance | Nonresonant endpoints with the source's `Q(y)<=1`; dominated cone `0<=f<=C/P`. | Retain endpoint charge in the effective return. Exit is resonance or 1. |
| Quarter-safe moving rank | `G_q={n>=2:4R_*(A(n))<=R_*(n)}`; nonnegative finite p-th rank moment, `p>0`. | The combined surviving-safe/unsafe-exit p-moment contracts by `4^(-p)`. |
| Enlarged-safe moving rank | `G_le={n>=2:R_*(A(n))<=R_*(n)}`; source envelope `f<=C/R_*^p` in its stated summable range. | Polynomial residence/mass-tail bounds; the entry envelope must hold again on reuse. |

Here `||f||_p=sum R_*(n)^p |f(n)|`; each unsafe set is the complement of its own safe set among surviving states. The two complements differ. An infinite first rank moment is not infinite unweighted mass and not a divergent individual orbit. Fresh-shell drift need not hold for a transported ensemble. [Exact operator proofs](renewal-transport/README.md).

## Ordinary and finite scope

In orbit counting, an infinite orbit means an **infinite distinct value set**, not a cycle traced indefinitely. Finite CRT families can have a different ordinary source at each depth. Complete rank balls bound candidate witnesses, not clocks or intermediate peaks. A fixed-depth language or fixed-radius inverse frontier is not an all-time invariant object.

For current hypotheses and corrected clauses use [the results catalog](../RESULTS_CATALOG.md) and [current repaired statements](README.md#current-repaired-statements). Exact `(PR, commit, path, claim ID)` identities and collisions are in [aliases](../../claims/aliases.json); [the audit record](../../claims/reviewed-2026-09-05.json) preserves the component reviews. Source author-stage headers do not override a later scoped review, and a later review does not accept unrelated or changed source statements.
