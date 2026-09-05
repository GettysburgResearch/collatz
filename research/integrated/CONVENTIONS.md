# Conventions for the reviewed mass and rank programs

**Integrated reference guide, not a new theorem or common-rank synthesis.** Exact component verdicts are in [Reviewer A](../../reports/prepublic-2026-09-05/reviewer-a/CLAIM_MATRIX.md) and [Reviewer B](../../reports/prepublic-2026-09-05/reviewer-b/CLAIM_MATRIX.md). Use full source paths and SHAs, not unqualified theorem numbers.

## Maps and clocks

The shortcut map is `T(n)=n/2` for even n and `(3n+1)/2` for odd n. A shortcut step is not an odd-to-odd step, whole odd/even run, section return, or maximal repeated-word module. Each cited theorem retains its own clock. The external natural-density dossier also has a raw Collatz clock.

PR91 uses `H={n>=4:n=1 mod 3}`, excluding 1. Its first positive-time return is to `H union {1}` and is killed at 1. The source calls that return R; here call it `F_H` to avoid confusing it with a rank.

## Two different integer ranks

PR90/91 use `h(n)=v3(2n+1)` and `P(n)=(2n+1)^2/3^h(n)`. Distinguish the original section version from its global extension. PR92 uses

```text
z_a(n)=3^a(n+1)-2^a(2n+1)
R_a(n)=z_a(n)^2/3^v3(z_a(n))
R_*(n)=min_(a>=0) R_a(n), n>=2; R_*(1)=0.
```

The reviewed moving-envelope theorem reduces this minimum to `R_0,R_1,R_2,R_h` (the fourth is needed only for h>=3), and proves `n-1<=R_*(n)<=n^2`. Its acceleration A consumes the maximal legal number of copies of the active word `1^a0`; it differs from the older whole-odd/even-run map. Neither rank is universally decreasing. A comparison of their values does not transfer a theorem from one rank to the other.

## Operator contract at every use

Use endpoint rows and source columns. For a specified deterministic map F killed at 1, `Kf(y)=sum_(F(x)=y) f(x)` on its surviving state space. Define `K_XY=Pi_X K Pi_Y`, extending inputs by zero outside Y. Nonnegative series are pointwise unless a norm-convergence theorem is separately supplied. A restricted inverse series is not automatically a bounded operator on all unsafe inputs.

| Program | Eliminated/safe region | Entry assumption and actual conclusion |
|---|---|---|
| PR91 section resonance | nonresonant endpoints Q(y)<=1 | `0<=f<=C/P`; retain the endpoint Q(y) in the effective-return remainder. Exit is resonance **or 1**. |
| PR92 rank-budget | `G_q={n>=2:4R_*(A(n))<=R_*(n)}` | For p>0 and finite safe-entry p-th rank moment, `norm_p(K_GqGq f)+norm_p(K_UqGq f)<=4^(-p)norm_p(f)`. |
| PR92 spectrum-switch | `G_le={n>=2:R_*(A(n))<=R_*(n)}` | Polynomial residence/mass tails use `f<=C/R_*^p` in the stated summable range; re-establish the envelope at each new entry. |

Here `norm_p(f)=sum R_*(n)^p abs(f(n))`; each U is the complement of its own G among surviving states. The two U sets differ. Unsafe transport need not preserve the finite-moment space or an entry envelope. A safe exit can reach U rather than 1. An infinite first rank moment is not an infinite unweighted mass or an individual divergent orbit. Fresh-shell averaged drift is not drift for an arbitrary transported ensemble.

## Scope and identity

An infinite orbit in the counting argument means an **infinite distinct value set**, equivalently a non-eventually-periodic positive trajectory, not a cycle traced indefinitely. Finite CRT families supply different sources at different parameters, not one ordinary source at every depth. Complete rank balls bound witness endpoints, not clocks or intermediate ranks.

[Aliases](../../claims/aliases.json) resolve namespaces to `(PR, full SHA, path, claim ID)`. Original author-stage PROPOSED headers and publication receipts are preserved; the later exact review governs the reviewed scope. A new conjunction or changed theorem remains pending its own narrow review.
