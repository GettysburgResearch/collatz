# Finite divisibility of an arithmetic-progression spacing

Let $g_0,\dots,g_t$ be natural spacings satisfying $q_jg_{j+1}=3g_j$ for every $j<t$, where each $q_j$ is even. The Lean theorem `two_pow_dvd_start` proves $2^t\mid g_0$. The two corollaries give $2^t\le g_0$ whenever $g_0>0$ and rule out an exact run of $t$ steps with $q_j\in\{2,4\}$ and $0<g_0<2^t$.

The proof inducts on the horizon, applying the induction hypothesis to the tail. The factors $2\mid q_0$ and $2^{t-1}\mid g_1$ combine, then coprimality removes the factor $3$. It applies also when the spacing is the gap between residue-congruent numerators divided by their odd denominator.

`RankSpacingExtinction.lean` closes the finite iteration following the one-step arithmetic-progression interface of `RankConvexityInterfaces.lean`. The three public theorems take the exact mechanical recurrences as hypotheses. Their production by the rank dynamics, avoidance of seams and the asymptotic Diophantine bound are proved in the written arguments. The package compiles the source in an empty directory, separately imports the resulting object and compares the axiom output for all three declarations. Only `propext` and `Quot.sound` occur.
