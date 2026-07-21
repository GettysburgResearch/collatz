# Session report: the marginal tower (final push)

```
Agent: claude-01  Issue: #4  Branch: claude/collatz-migration-math-osr370
Date: 2026-07-21 (session 10; single push, no loop)
```

L-0019 (PROPOSED): exact one-level Fourier contraction for the wrap
marginal — |ŵ_K(ψ)| ≤ |cos(πψ·64^{−(K−1)}/81)|·|R̂_{K−1}(uψ)|, shift
a unit cycling the period-9 AP; the 9-cycle cosine product < 1 ∀ψ≠0
is the per-period gain a closed recursion would deliver.

O-0018: the tower obstruction, exact — the mod-81 marginal is driven
by mod-81² data below (verified element-by-element at K = 12); the
walk is an inverse-limit skew product, mirror-dual (via T-0027) of
the M2 digit wall. EQ must beat the tower by averaging or import
measure-rigidity (Q-0005's interface — now precisely located).

O-0019: the first marginal MIXES empirically at CLT rate (Fourier
max 0.231 → 0.0088, TV 0.221 → 0.0080 over K = 8…16, ≈ 2^{−K/2}).

Standing after the day: every object named, every obstruction exact,
contraction measured and one level of it proved. Next thresholds:
close the tower's averaged recursion (beat §23 with §22's gain), or
the Q-0006 ceiling, or reviews. Driver identity + creep verification
inline (this report is the log of record for session-10 numerics;
scripts of prior sessions cover the machinery).
